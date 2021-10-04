# Project Name: I Need A Hero

## Project aim
The site's aim is to provide a marketplace for people who want to workout from home or in their surrounding area's.
The products available are easily identifiable as being suitable for home, outdoors, done by day, or by night where
a customer may need to aware of noise levels.

Firstly the site offers a hand-holding approach with succint product descriptions and clearly outline goals.
We endevour to shy away from too much text or fluff and want people to sign up and buy without having to dive 
down the fittness and health rabbit-hole of conflicting information. 

Getting people started is our primary goal.

[View Live Version here](https://total-health-at-home.herokuapp.com/)

## User Experiance (UX)

### User stories
-    ## First Time Visitor Goals
        * I want easily understand the site's purpose. 
        * I want to navigate the site's content.
        * I want to see all available products and their distinct features based on my preferences.
        * I want to make a purchase without signing in.

-    ##   Returning / Registered User Goals
        * I want to see my order history.
        * I want to review products I've bought.
        * I want to suggest alterations on the site.

-    ## Administrator Goals
        * View, approve or delete user testimonials and product reviews.
        * I want to add, delete or edit products / Categories.
        * I want to view all users, their emails, and verification status via Django

### Design
-    ### Colour Scheme
        * rgb(57, 250, 18) (Green) & rgb(106, 164, 187) (Blue),
        are utlised thourghout for contrast against the sites grey background and default white. 
        * While standard user buttons and link adhere to the green, white, blue consensus, Admin buttons for deletion are purposefully garish to further guard against accidental instigation.
            
-    ### Typography
        * 'Permenant Marker' and 'Shadows into light' are used throughout for headers, messages, buttons etc 
        Both from [Google Fonts](https://fonts.google.com). Sans Serif is used a fallback. 

-    ### Imagery
        * Product Images, and Hero Image were sourced from unsplash.com
            * [Hero Image](https://unsplash.com/photos/PHIgYUGQPvU)
            * [Product: Molten Monk](https://unsplash.com/photos/_Wi5bi-yjXI)
            * [Product: Ninja](https://unsplash.com/photos/E3CZ_AtzixY)
            * [Product: Water Dragon](https://unsplash.com/photos/a4_vdJ3gbHE)           
            * [Product: Dynamite](https://unsplash.com/photos/Oi31uKsnM1Q)        
            * [Product: Dance Machine](https://unsplash.com/photos/JsQ6K5CfJ7s)     
            * [Product: The Fox](https://unsplash.com/photos/CQl3Y5bV6FA)   
            * [Product: Mountain Lion](https://unsplash.com/photos/aMBhrrveocw)   


*   ### Wireframes
    * Index page [here](readme/wireframes/Wireframe_Index.pdf)
    * Products [here](readme/wireframes/Wireframe_Product.pdf)
    * Product Details[here](readme/wireframes/Wireframe_Product_Detail.pdff)
    * Bag [here](readme/wireframes/Wireframe_Bag.pdf)
    * Profile[here](readme/wireframes/Wireframe_Profile.pdf)

## Features
-   Responsive on all devices with:
    *   CSS Media Queries for scaling card images on screen resizing.
    *   Collaspible Header with hamburger for mobile devices.
-   Contains interactive elements such as:
    *   Product filtering by catgeory and product element such as 'day', indoors', 'night' etc.
    *   User authentication via registeration with verification email /log in/ log out.
    *   Loops to hide/show various navigation options depending on user status.
    *   Form for adding testimonials viewable (after admin approval) to all other users.
    *   Form for adding product reviews both viewabale (after admin approval) to all other users, and impact the given rating of a product.
    *   C.R.U.D. functionality scaled with user status.(user/ unregistered / admin).

## Technologies Used
### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python 3](https://www.python.org/)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used
- [GMAIL](https://www.google.com/gmail/) - for verification emails via Django
- [GitHub](https://github.com)
- [Jquery](https://jquery.com/)
- [GitPod](https://www.gitpod.io/) - IDE.
- [Boostrap (including JQuery)](https://getbootstrap.com/) -Utilized for responsiveness via columns, buttons and navbars.
- [Google Fonts](https://fonts.google.com) - Used for fonts throughout.
- [Font Awesome](https://fontawesome.com/)  - For icons.
- [Django](https://www.djangoproject.com/) - For authentication and administration.
- [AWS](https://aws.amazon.com/) - For hosting static and media files
- [Heroku](https://www.heroku.com/) - For hosting.
- [Stripe](https://stripe.com/en-ie) - For payment intergartion.
- [Gmail](https://www.google.com) - For automated emails.

## Testing
-   Using [W3C validator](https://validator.w3.org/) both HTML and CSS were checked by direct input. Issues arising were promptly corrected. 
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

-   [JsHINT](https://jshint.com)- Used for Java Script validation. Warnings relating to the use of 'let' to declare variables.
    The script was not amended to address these.


### Testing User Stories from User Experience (UX) section.
### First Time Visitor Goals :

*  I want to easily understand the site's purpose.
    1.  The index page utilises eye-cathcing colours, fonts and clean lines with an upfront description
        of the sites aim.
    2.  Users are immediately granted access to the site's products, existing testimonials and product reviews.
     
* I want to navigate the site's content.
    1.  A static, collaspible header contains all the nav elemnets available to new users. Although 
        registration/login is required to access more functions, the main content is available to read.

* I want to see all available products and their distinct features based on my preferences.
    1.  The Products page lists all available products on cards. The costs and core category are front and center.
    2.  The Products page contains seven filtering options designed to help users find applicable products.
    3.  Further product information, such as verified customer reviews and product rating, is available on the 
        details page by clicking the product image or using a prominent 'more info' button.

* I want to make a purchase without signing in.
    1.  Although new users are encouraged to register by signing in and verifiying their email to gain access 
        to a wellness element, registeration is not necessary to make a purchase. 
    2.  Users are also reminded that by registering the site can save their info in a custom profile page, 
        as well as allow them to review the site and their purchased products.
    3.  Upon adding an item to their bag, a user is alerted via a toast message and given the option to navigate directly to the checkout, or remain on
        their current page.
    4.  On the bag page their total costs, product count and product details are listed for inspection. They can choose to add more items to, or remove items from, 
        their bag before checking out.
    5.  At Checkout, the user is presented with a form to fill in with their details. Here they are kept abreast of their total costs, and current bag contents.
    6.  Upon submitting a valid form the user's card is charged and they are redirected to a checkout_success page listing all relevant order information. 
        They should be notified of an impending email with the similiar information.

### Returning / Registered User Goals :

*  * I want to see my order history.
    1.  Order History is available on a returning user's Profile page. It details each order seperately and lists the products purchased in those instances. 
     
* * I want to review products I've bought.
    1.  Navigating to the Order History section a clickable order number is avaiable to expand particular orders.
    2.  The subsection of 'Order details' lists the products bought in this instance with an option to see more information on the product,
        as well as a link to review that product.
    3.  Upon deciding to review a product the user is brought to a form which pre-populates the user's name and the product to be reviewed.
        The form allows for a description of feedback and a choice to mark the review as positive or negative.  
    4.  Although product reviews are sent for admin approval a user can see their reveiw (unapproved or approved) on the product details page as well as
        in the feedback section on their profile. Unapproved reviews or testimonials remain hidden to other users. 

* I want to suggest alterations on the site.
    1.  Users can suggest reviews for the overall site via their feedback section on their profile page available after their first purchase using a verified account.
    2.  Clicking the 'Add a testimonial' link generates a simple form with the user's username pre-populated. Users can leave their response and submit it for admin approval.
    3.  Although testimonials are sent for admin approval a user can see their testimonial (unapproved or approved) in the feedback section on their profile.


### Administrator Goals :

* View, approve or delete user testimonials and product reviews.
    1.  CRUD operations for reviews and testimonials are available to the admin in two area's depending on their approval status.
    2.  Approved testimonials are lsited on the index page accompanied by an 'Edit/Delete' button viewable only to the admin. Once clicked 
        the admin is brought to the edit_testimonial page and asked to confirm their intentions as editing or deleting.
        If editing a tetsimonial, the approved testimonial is generated. Only the description and approval status' can be edited.
        If Deleting a testimonial, the admin must confirm consecutive delete actions via intentionally garish buttons.
    3.  Approved product reviews are lsited on their related product details page accompanied by an 'Edit/Delete' button viewable only to the admin. Once clicked 
        the admin is brought to the edit_review page and asked to confirm their intentions as editing or deleting.
        If editing a review, the approved review is generated. Only the description, feedback and approval status' can be edited.
        If Deleting a review, the admin must confirm consecutive delete actions via intentionally garish buttons.
    4.  Unapproved testimonials are lsited in the 'admin tools' section on the admin's profile page accompanied by an 'Edit/Delete' button viewable only to the admin.
        Once clicked the admin is brought to the edit_testimonial page and asked to confirm their intentions as editing or deleting.
        If editing a tetsimonial, the approved testimonial is generated. Only the description and approval status' can be edited.
        If Deleting a testimonial, the admin must confirm consecutive delete actions via intentionally garish buttons. 
    5.  Unapproved product reviews are lsited in the 'admin tools' section on the admin's profile page accompanied by an 'Edit/Delete' button viewable only to the admin.
        Once clicked the admin is brought to the edit_review page and asked to confirm their intentions as editing or deleting.
        If editing a review, the approved testimonial is generated. Only the description and approval status' can be edited.
        If Deleting a review, the admin must confirm consecutive delete actions via intentionally garish buttons.

* I want to add, delete or edit products / Categories.
    1.  Adding new products can be done via the admin's profile in the 'Admin Tools' section.
    2.  The 'add_product' form contains fields for all relevant information (category, name, price etc) as well as an option to upload a suitable product image.
    3.  Products can be edited from their individual details page which generates a 'edit_product' form populated with the products current details.  
    4.  Products can be deleted from their individual details page via a delete button only available to the admin. The admin must confirm consecutive
        delete actions via intentionally garish buttons which use jquery to display. 
    5.  Categories can only be edited, created or deleted from the Django admin interface under their respective section. Accessible by appendind '/admin' to the main site url.
    6.  All previous listed admin CRUD operations done from the site can also be executed form the Django admin interface.

* I want to view all users, their emails, and verification status via Django
    1.  All current user information (verified or pending verification) is available via the site's admin interface. Accessible by '/admin' to the main site url.


## Further Testing

### Security / Access 
####   User based access

*   URL access:
    *   Sensitive views are protected by requesting users by authenticated, and their account meets certain criteria. Since users can create reviews and testimonials,
        relying wholly on authentication doesn't suffice. The site employs a variety of checks depening on the users intentions. The site may check if a user has previous orders, or has purchased a specific product. It may check if a user has previously submitted a product review and deny multiple reviews of the same product. Testimonials are resticted to one per registered user with a previous orders.
        A notable acception found is for the Order_history page. If an authenticated user, with their own previous orders, obtains someone's unique order number, they can access that order's information via the url. A suggested fix would be to add a username field to the order model which could be directly compared to the current user. 
*   Unregistered user:
    *   Can only view the following pages. Home, Products, Product details, bag, 
    *   Cannot create, edit or delete products, reviews or testimonials.
    *   Cannot login prior to registering.
    *   Cannot use url to access any extra pages.
*   Registered and logged in users with no orders:
    *   Can also view the profile page in addition to Home, Products, Product details, bag.
    *   Cannot create, edit or delete products, reviews or testimonials.
    *   Cannot use url to access any extra pages.
*   Registered and logged in users with orders:
    *   Can also view the profile page in addition to Home, Products, Product details, bag.
    *   Can create one review per product they've purchased. Can create one testimonial.
    *   Can url to access checkout_success page if they obtain another users order number.
*   Admin :
    *   Can view all pages, access CRUD via the site buttons hidden from other users or the admin interface.
    *   Can access all CRUD operations as per the main site with the addition of categories and user info from the admin interface (Django).

#### Links
*   Internal page links and external links were manually tested. 
#### Loops
*   Loops are utilised throughout to check user status and decide which nav bar elements can be viewed.
*   Loops are also tasked with displaying a user's unapproved testimonials and reviews on their profile page, 
    and highlight user's approved testimonials on the home page and reviews on the intended product detail page.
*   Loops direct users of all status' to their next step. An unregistered user is directed to sign up. 
    A registered user with no orders is prompted to make their first purchase in the profile tab. A registered user with previous
    orders is nudged to review their products and submit a testimonial.
#### Views
*   Display error, info, warning or success messages via toasts dependant on the user's action.
*   Check various user status' around reviews, testimonials to dictate user access.
### Forms
*   Validation is achieved via [crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/).
*   Payment forms involving stripe are handled by java script in the checkout app's static folder.
### Known Bugs
*   As outlined above referencing the Order_History view  If an authenticated user, with their own previous orders, obtains someone's unique order number, they can access that order's information via the url. A suggested fix would be to add a username field to the order model which could be directly compared to the current user. This was discovered close to Milestone deadline with not enough time to implement and test a fix.


## Deployment 
### Heroku
1.  Create a requirements.txt file. Command in gitpod is 'pip3 freeze --local> requirements.txt'
2.  Create a Procfile (Capital 'P' and no file extension).
3.  Push the two new files to your repository. 
4.  Login in to [Heroku](https://www.heroku.com/) and from the dasjboard select 'New' > 'Create new app'.
5.  Create a unique app name utilising '-' instead of spaces. Select your closest region from the dropdown. Then click
    'Create app'.
6.  To connect the app use the 'Connect to Github' option for a simplified process. Enusre you github user profile
    is display after selction. Then, serach for the github repository you wish to connect. Then click 'Connect'.
7.  Go to settings at the top of the heroku page. Then, scroll down 'Reveal Config Vars'. 
8.  Here you enter the following data from your env .py file : Keys for IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
    and their corresponding values.
9.  Return to the delopy tab in heroku and click 'Enable Automatic Deployment, then 'Deploy Branch'.
10. Upon success you will see 'Your app was successfully deployed' and an option to view the app.
11. A live version can be found here: [Total Health At Home](https://total-health-at-home.herokuapp.com/)

### Github
The project was developed using [GitPod](https://www.gitpod.io/) workspace, committed to git and pushed to 
[GitHub](https://github.com) using the built in function within Gitpod.
To deploy this page from the [GitHub respository](https://github.com/FirmoDaniel/Total_Health_At_Home), the following steps were taken.
1.  Log in to **GitHub**.
2.  From the list of repositories on screen select 'I_Need_A_Hero'.
3.  Select **Settings** from the menu.
4.  Scroll down to **GitHub Pages**
5.  Under **Source** click the dropdown menu labelled **none** and select the **Main Branch**.
6.  On selecting **Master Branch** the is automatically refreshed, the website is now deployed.
7.  A link can be found in the **GitHub pages section**, and also in the about section within **I_Need_A_Hero**.

### Cloning
1. Go to GitHub Repository: [Total_Health_At_Home](https://github.com/FirmoDaniel/Total_Health_At_Home)
2. Select 'Code' dropdown button (next to green 'gitpod' button).
3. These are your three options **Clone-Options**.

    * Copy the URL to your local IDE such as [Visual Studio](https://code.visualstudio.com).
    * Intsall [GitHub desktop](https://desktop.github.com/).
    * Download the Zip file and use with local IDE such as [Visual Studio](https://code.visualstudio.com).


## Credits   
### Code
1.  CSS for taken from Course Institute (see base.css starting line 154 > 208)

### Content
1.  Initial product idea's abd descriptions created by the developer. The Images sourced from Unsplash as detailed in the Design/Imagery section above.
2.  README layout taken from Code Institute's sample [README](https://github.com/Code-Institute-Solutions/SampleREADME).


### Acknowledgements
1. Code Institute Tutorials, student support and my Mentor.