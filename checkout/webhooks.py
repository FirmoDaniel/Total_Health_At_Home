from django.conf import settings
from django.http import HttpResponse
from checkout.webhook_handler import StripeWH_Handler
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """ listen for WH from Stripe """
    # setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get stripe wh data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
         payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    print('success mofo!')
    return HttpResponse(status=200)
