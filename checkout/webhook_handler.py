from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhook"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f' Unhandled Webhook recieved: {event["type"]}',
            status=200)

    # PAYMENT INTENT SUCCEEDED
    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded from stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.saveinfo

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping  # may not need shipping , see stripe elements line 81
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean Data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already exists in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                for item_id, __ in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]} | SUCCESS: Created Order in Webhook',
            status=200)

    #  PAYMENT INTENT FAILED

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed from stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
