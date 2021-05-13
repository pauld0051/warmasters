# WARMASTERS

[![Warmasters Logo](readme/images/w-icon.png)](https://warmasters.herokuapp.com/)

Warmasters (alpha-release) is the proof of concept to use Django to build a fantasy role playing game with a shop to purchase items for in-game use.

- [UX](#ux)
  - [Project Goal](#project-goal)
  - [User Stories](#user-stories)
    - [User Stories for Customers](#user-stories-for-customers)
    - [User Stories for Shop Administrators](#user-stories-for-warmasters-administrators)
  - [Wireframes](#wireframes)
  - [Data Structure](#data-structure)
  - [Design](#design)
    - [Typography](#typography)
    - [Colours](#colours)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Home Page](#home-page)
    - [Product Page](#product-page)
    - [Product View](#product-view)
    - [User's Profile Page](#profile-page)
    - [User Login and Sign-Up](#user-account)
    - [Shopping Bag](#shopping-bag)
    - [Secure Checkout](#secure-checkout)
    - [Game Profile](#game-profile)
    - [Administrator features](#administrator-features)
  - [Features Left to implement](#features-left-to-implement)
- [Testing](#testing)
  -[Testing Webhooks](#testing-webhooks)
  -[ngrok method](#ngrok-method)
  -[Stripe CLI method](#stripe-cli-method)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Technologies](#technologies)
- [Tools Used](#tools-used)
- [Credits](#credits)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

---

Welcome to Warmasters - the alpha testing for the shopfront and user profile, game profile, and storage of items. The game is in the development stage, with the proof of concept being released in this alpha version. Users will be able to login, create a profile, create a game profile, purchase items for up and coming missions and move items between storage, bags (for missions) and trade.

Access the site: <https://warmasters.herokuapp.com/>

[![Am-I-Responsive](https://github.com/pauld0051/warmasters/blob/2f30ee9089ab79518715d998be93dc3406a82206/readme/images/amiresponsive-warmasters.png)](https://warmasters.herokuapp.com/)

## UX

### Project Goal

This is the fourth and final Milestone Project in Code Institute's Fullstack Development program. The purpose of this project was to create an e-commerce site using the Django framework, static file hosting with AWS, and a functional payment system with Stripe. The e-commerce section of the site is fully functional, Stripe payments and webhooks are operational and all static files, including media (images) are located at Amazon Web Services (AWS). The site is ready for the second alpha phase, setting up the game play. This will still use Django's framework.

The site's frontend and payment system was inspired by Code Institute's Boutique Ado project: [Boutique Ado Code](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546)

### User Stories

#### User Stories for Customers

Table 1: User Stories for Customers at [Warmasters](<(https://warmasters.herokuapp.com/)>)
A gamer would like to: | So the gamer can: | Page(s) associated:
--- | --- | ---
Browse for products to use in the game | Purchase products to use in game | <https://warmasters.herokuapp.com/products/>
Register using email or Google accounts | Easily access an account and receive an email to confirm registration | <https://warmasters.herokuapp.com/accounts/social/signup/>
Login to an account using email or Google (dependent on registration method) | Keep logged in permanently with a "remember me" checkbox | <https://warmasters.herokuapp.com/accounts/login/>
Search products | Choose products best suited for the game mission | <https://warmasters.herokuapp.com/products/?q=sword>
Filter products based on categories | Sort through items that are needed for a mission | <https://warmasters.herokuapp.com/products/?q=sword&sort=price&direction=asc>
Filter products by price | Game on a budget | <https://warmasters.herokuapp.com/products/?sort=price&direction=asc>
Filter products based on an admin rating | Choose products that will serve best in a mission | <https://warmasters.herokuapp.com/products/?sort=rating&direction=asc>
Sort products by their name | Find products based on a name | <https://warmasters.herokuapp.com/products/?sort=rating&direction=asc>
Read product descriptions | Get a better understanding of the purpose of the item | <https://warmasters.herokuapp.com/products/33/>
See special offers | Get a free gift with purchases over a set price | <https://warmasters.herokuapp.com/>
Buy a product for in game use and view in a shopping cart before purchase | Use the item during game play | <https://warmasters.herokuapp.com/bag/>
Update the number of items in the shopping cart before purchase | Purchase more items needed for game play | <https://warmasters.herokuapp.com/bag/>
Pay by using a credit card in from a safe and reputable source | Instantly purchase game items and have them delivered to the game profile | <https://warmasters.herokuapp.com/checkout/>
Buy a product and have the item delivered instantly to the game profile | Login to their account to have the item delivered to their storage | <https://warmasters.herokuapp.com/game/game_item_storage/>
Create a profile | Return and purchase items without needing to fill in details again | <https://warmasters.herokuapp.com/profile/>
Create a game profile | Use an in-game profile to have items delivered to instantly | <https://warmasters.herokuapp.com/game/make_profile/>
Create a character | Make a character to use during play based on one of four mythical characters | <https://warmasters.herokuapp.com/game/create_character/>
Update profile information | Keep up to date data | <https://warmasters.herokuapp.com/profile/>
View previous purchases | See purchase history on the profile | <https://warmasters.herokuapp.com/profile/>
Receive an email confirming a purchase | Have a receipt and confirmation of purchase in an email | \*Purchase an item and have the email sent
See items in storage, bag or trade locations | Use the items in an appropriate location | <https://warmasters.herokuapp.com/game/game_item_bag/> <https://warmasters.herokuapp.com/game/game_item_storage/> <https://warmasters.herokuapp.com/game/game_item_trade/>

- _Table 1 provides details of customer's wants and outcomes with the associated page links._

#### User Stories for Warmasters Administrators

Table 2: Admin Stories for site administrators at [Warmasters](<(https://warmasters.herokuapp.com/)>)
-- _note: some pages may not be accessible without being an administrator or superuser. Request access via email_
An admin would like to: | So the admin can: | Page(s) associated:
--- | --- | ---
Add/Update/Delete a product | Keep the store up to date with the latest items for missions - only admins have access to these features | <https://warmasters.herokuapp.com/products/add/> -- delete and edit can be done from the product page: <https://warmasters.herokuapp.com/products/> (only viewable when logged in as an administrator)

- _Table 2 details the types of actions an administrator can do from the website, however, all administrators will also have access to the database through Django's admin panel._

All new game items' images are added to AWS automatically. Currently the administration page is located at the default Django admin link. This will be altered during beta release as a security measure.

The original urls.py location for the Django administration panel:
`path('admin/', admin.site.urls),`

This will be updated to a random key and administrators will need to bookmark the page.

### Wireframes

Following the user stories, wireframes were drawn to provide a starting point and guidance throughout the development process. Some minor changes occurred based on new outcomes and limitations in the code.

Image 1: The game profile page on desktop
![Warmasters Desktop Wireframes](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/profile-page-desktop.png)
Image 2: The game profile page on mobile
![Warmasters Mobile Wireframes](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/profile-page-mobile.png)

Other wireframes:
All pages are set up to mimic one and other, even in the game and shop pages. The backpack, storage and trade pages are identical except the headings.

#### Mobile Wireframes

Image 2: The game backpack/storage/trade page on mobile
![Warmasters Mobile Wireframe - Backpack](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/backpack-mobile.png)
Image 3: The products page on mobile
![Warmasters Mobile Wireframe - Products](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/product-page-mobile.png)
Image 4: The user profile page on mobile
![Warmasters Mobile Wireframe - Profile](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/users-page-mobile.png)

#### Desktop Wireframes

Image 5: The game backpack/storage/trade page on desktop
![Warmasters Mobile Wireframe - Backpack](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/backpack-desktop.png)
Image 6: The products page on desktop
![Warmasters Mobile Wireframe - Backpack](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/product-page-desktop.png)
Image 7: The user profile page on desktop
![Warmasters Mobile Wireframe - Backpack](https://github.com/pauld0051/warmasters/blob/ff5fd959e275782166637795e0fa8495a810a9e4/readme/images/users-page-desktop.png)

### DESIGN

The application was built using Bootstrap and its responsive grid system with a mobile-first precedent. The font, colours and design were all to give a dark _fantasy_ feel about the site. Colours were chosen to best suit those with colour deficiency vision.

#### Typography

One Google Font was used throughout the site; Medieval Sharp: <https://fonts.google.com/specimen/MedievalSharp?preview.text_type=custom>
The site also uses [Fontawesome](https://fontawesome.com/) icons throughout.

#### Colours

Colours were chosen to best reflect the dark fantasy theme that the site was portraying. This includes the colour of text, background, imagery, overlays and headers.

##### Main Site

![#555](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/555.jpg) - Background - #555

![#4e342e](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/4e342e.jpg) - Overlay - #4e342e

![#212529](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/212529.jpg) - Product badges - #212529

![#b71c1c](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/b71c1c.jpg) - Button hover effect - #b71c1c

![#dce775](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/dce775.jpg) - Horizontal rule - #dce775

#### Fonts

![#ffea00](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/ffea00.jpg) - Text headings - #ffea00

![#e0e0e0](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/e0e0e0.jpg) - Light coloured text - #e0e0e0

![#bdbdbd](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/bdbdbd.jpg) - Darker coloured text -#bdbdbd

![#c6ff00](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/c6ff00.jpg) - Lime coloured text - #c6ff00

![#b71c1c](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/b71c1c.jpg) - Flame icons - #b71c1c

![#6c757d](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/6c757d.jpg) - All Auth forms (login) - #6c757d

![#aab7c4](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/aab7c4.jpg) - Placeholder text - #aab7c4

![#222](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/222.jpg) - Border colours on forms - #222

![#17a2b8](https://github.com/pauld0051/warmasters/blob/master/readme/images/colours/17a2b8.jpg) - Text info - #17a2b8

## FEATURES

### Existing Features

#### Home Page

- The first thing a user will see when entering the site is a large full-cover background picture depicting a lone warrior about to enter a dungeon (source: <https://theinnergamer.net/wp-content/uploads/2017/03/what-is-dungeons-dragons.jpg>)
- A large banner spreading the width of the page with red flame icons indicate a current special on purchases
- A large welcome and button with "Login to Play" or "Fight Now" (dependent on login status respectively) is displayed
- Users can access all products in the top navigation banner and access their own game profile through the "Fight Now" button or on the user My Account navigation icon
- Users can search through the Warmaster's site for items that are available to purchase

#### Product Page

- Products are shown with an image against a white card background and a large "Add to Bag" button located bottom left
- Administrators will have access to Edit and Delete options on products
- Product images link to the product detail page where a product description is also available
- Products all display:
  - Product Image
  - Product Name
  - Price (in $US)
  - Category tag
  - Add to Bag button
  - Star rating (set by admin)
    - If admin:
      - Edit button
      - Delete button
- Clicking on "add to bag" brings up a *toast* which allows a user to go their bag and adjust their purchase accordingly
- Scroll to top function located bottom right as an arrow

#### Product View

- A larger, clickable display picture
- A modal displaying the picture of the item
  - Name of item
  - Price of item
  - Decorated with a fantasy map background
- Name of item
- Price (in $US)
- Category tag
- Add to Bag button
- Star rating (set by admin)
- Full description
- Quantity to add to bag
- Return to shop page button
- Add to bag button

#### Profile Page

- User's name displayed at the top
- Your information updatable form
  - Phone number
  - Address
  - Address 2
  - Town or city
  - County, state, or locality
  - Postal code
  - Country
- Update Information button
- Order history (right hand panel on large screens)
  - Order number
  - Date
  - Item name
  - Quantity
  - Order total
  - Clickable order number with ink to the order

#### User Account

- Login via email or Google account
- Sign up with email, an encrypted password is stored for security
- Sign up with Google, no password required

##### Shopping Bag

- Notifies user when empty
- Displays:
  - Product image
  - Product name
  - Price
  - Updatable quantity
  - Subtotal
  - Remove item
  - Bag total
  - Grand total
  - Link to secure checkout or back to shopping

#### Secure Checkout

- User information form:
  - Name
  - Email
  - Phone number
  - Country
  - Card information (secured by Stripe)
- Order summary:
  - Product image
  - Item name
  - Quantity
  - Subtotal
  - Order total
  - Free gift (if applicable)
  - Grand total
- Complete order button or back to shopping

#### Game Profile

- Character profile
- Link to:
  - Backpack
    - Items in backpack
    - Move or delete items
  - Storage
    - Items in storage
    - Move or delete items
  - Trade
    - Items in trade
    - Move or delete items

#### Administrator Features

- On product pages, an administrator has additional links to edit a products information or delete the product from the shop
- Administrators have access to Django's Admin Panel

#### Features Left To Implement

This site is in an alpha production phase and currently is standing as a proof of concept. The game page will lead to missions which will allow the user to utilise their purchased items and build an army to adventure through a fantasy world designed fully by the imagination of the author.

Users may be able to purchase physical game-paraphernalia and fan products, this will require using Stripe's already implemented address system check-up.

A trading post will be set up where users can purchase other user's equipment and items using gold they have earned in the game or purchased from the shop. Users will be restricted in bag size, storage size and the amount of items they can have in their trading post. The code is there for the limitation of size already, however, code to allow for the increase in size is in the next phase of coding. Users wil be able to purchase bigger backpacks, storage areas and more items able to be traded. Items currently have a weight and size associated with them. This will form part of the limits in the backpack for instance (both size and weight).

A friend system will be implemented too, so users can follow their friends and join in battles as well as missions together.

## TESTING

Testing was done manually throughout the development process. The full rundown of the testing can be found [here](https://github.com/pauld0051/warmasters/blob/master/readme/TESTING.md).

Additionally, all code was validated in the following ways:

HTML - All pages were successfully run through the [W3C HTML Validator](https://validator.w3.org/) to ensure compliance with the standards set by the W3C. Some errors unavoidably occur due to common ID names which are re-used according to Django. For instance this allows users to be either on a mobile or desktop device and still have access to identical features.

CSS - CSS validation with the [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/) returned some expected and necessary flags from vendor extensions. Other than that, the code complies to the W3C standards.

Python - All Python code was checked using VS Code's PyLinter. Some "no 'objects' member" errors occurred in the linter. On careful scrutiny and consultation with Django experts, this flag is picked up by the linter, but is not an error and can be ignored. Other linters, specialized in Django, can be installed and used which will not pick up and flag these as an error.

### Testing Webhooks

#### ngrok Method

    1. For a Windows based VS Code download the ngrok zip file from ngrok
    2. Unzip and run ngrok anywhere (it's stand-alone)
    3. type ngrok.exe http [your local server port] (this project was using either 5000 or 8000 for the port depending if other applications were open at the time)
    4. Get the https address that is assigned to you
    5. Add that to the hosts in: settings.py - ALLOWED_HOSTS = [your_number_here.ngrok.io"]
    6. Add your Webhook to Stripe the same way as the video for eg: https://your_ngrok_site.ngrok.io/checkout/wh/
    7. Send a webhook following the video and check the terminal for success!

#### Stripe CLI Method

    Download the latest Stripe CLI and put it in an easy directory to access on your main computer drive

    The following is for Windows based computers:

    To install the Stripe CLI on Windows:

    1. Download the latest windows zip file from https://github.com/stripe/stripe-cli/releases/latest
    2. Unzip the stripe_X.X.X_windows_x86_64.zip file
    3. Run the unzipped .exe file in your terminal

    From there follow the instructions: https://stripe.com/docs/stripe-cli/webhooks#forward-events

## KNOWN BUGS

In order to get Stripe's webhooks to operate correctly a series of hidden fields were added to the base code in the form to allow input of street address1, street address2, country, and postcode. These are hidden on the template through the forms.py using: `self.fields['[field_name]'].widget = forms.HiddenInput()`

Django's secret key generator: <https://djecrety.ir/>

To use the [amiresponsive](http://ami.responsivedesign.is/#) site you need to allow "clickjacking" according to Django Docs: <https://docs.djangoproject.com/en/3.1/ref/clickjacking/>
For this case the middleware clickjacking line remains in the main app's `settings.py` file:

```python
MIDDLEWARE = [
    ...
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ...
]
```

In the `views.py` for the index/home page:

```python
from django.views.decorators.clickjacking import xframe_options_exempt
```

And above the function:

`@xframe_options_exempt`
