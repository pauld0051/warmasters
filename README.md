# WARMASTERS

[![Warmasters Logo](readme/images/w-icon.png)](https://warmasters.herokuapp.com/)

Warmasters (alpha-release) is the proof of concept to use Django to build a fantasy role playing game with a shop to purchase items for in-game use.

- [UX](#ux)
  - [Project Goal](#project-goal)
  - [User Stories](#user-stories)
    - [User Stories for Customers](#user-stories-for-customers)
    - [User Stories for Shop Administrators](#user-stories-for-shop-administrators)
  - [Wireframes](#wireframes)
  - [Data Structure](#data-structure)
  - [Design](#design)
    - [Typography](#typography)
    - [Colors](#colors)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Home Page](#home-page)
    - [Product Listing](#product-listing)
    - [Product View](#product-view)
    - [Producers Page](#producers-page)
    - [User Account](#user-account)
    - [Shopping Cart](#shopping-cart)
    - [Payment](#payment)
    - [Administrator features](#administrator-features)
  - [Features Left to implement](#features-left-to-implement)
- [Testing](#testing)
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

Access the site: <https://pros-and-cons-1.herokuapp.com/>



## Testing Webhooks

### NGROK Method

    1. For a Windows based VS Code download the ngrok zip file from ngrok
    2. Unzip and run ngrok anywhere (it's stand-alone)
    3. type ngrok.exe http [your local server port] (I use 5000, but you might be using 8000 which is common)
    4. Get the https address that is assigned to you
    5. Add that to the hosts in settings.py - ALLOWED_HOSTS = [your_number_here.ngrok.io"]
    6. Add your Webhook to Stripe the same way as the video for eg: https://your_ngrok_site.ngrok.io/checkout/wh/
    7. Send a webhook following the video and check the terminal for success!

### Stripe CLI Method (preferred)

    Download the latest Stripe CLI and put it in an easy directory to access on your main computer drive

    The following is for Windows based computers:

    To install the Stripe CLI on Windows:

    1. Download the latest windows zip file from https://github.com/stripe/stripe-cli/releases/latest
    2. Unzip the stripe_X.X.X_windows_x86_64.zip file
    3. Run the unzipped .exe file in your terminal

    From there follow the instructions: https://stripe.com/docs/stripe-cli/webhooks#forward-events

### Known Bugs

In order to get Stripe's webhooks to operate correctly a series of hidden fields were added to the base code in the form to allow input of street address1, street address2, country, and postcode. These are hidden on the template through the forms.py using: `self.fields['[field_name]'].widget = forms.HiddenInput()`

Django's secret key: https://djecrety.ir/
