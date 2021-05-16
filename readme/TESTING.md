# TESTING

## Navigation

All links were checked and were working as anticipated. Some links, such as product management requires a login, therefore, even if a user tries to force the page (whether logged in or not), and are not part of the administrative team, the user will be denied access.

### Mobile Navigation

A hamburger style collapse is in operation for users on small screen devices.

### Desktop Navigation

A full width navbar is in operation allowing users to see their options in an easy to follow format.

## SHOP FRONT

### Home Page and Products

#### Home Page

A user must be logged in to go to their game profile or buy any equipment. If a user attempts to purchase an item without being logged in, they will be redirected to their login page. The item they had added to their bag will still be there however.

#### Products Page

The pages listing products display the correct information, for each product and the number of products.
The "back to top" button works as expected. Administrators can edit and delete products, but must be logged in at the time.

#### Search

Searching works to find products that are located on the Warmaster's product pages.

#### Filtering

Filtering works in both the products and game item pages.

#### Product Details

Administrators can edit and delete products, but must be logged in at the time. Users can click on the images to see a modal version of the product.

#### Add Product (Administrative)

Admins can add a product to the page and images upload to AWS and are available instantly.

#### Edit Product (Administrative)

Admins can edit product details or change an image.

#### Shopping Bag

The shopping bag displays all items selected by the user.
Updating the quantities of products in the bag works as intended.
It is possible to remove an item from the bag.
Clicking "Secure Checkout" leads to the checkout page with free gift if available.
If the shopping cart is empty, it is displayed as such.

#### Secure Checkout

Form (with hidden inputs) loads appropriately.
Items added and free gift if appropriate reflect user's purchase requests.
Items display with their correct price, image, name and quantity.
New profile information updates if requested.
Hidden inputs do not interfere with user's profile information.
Stripe payment and webhooks work as anticipated, payments are accepted using test cards.
Unsuccessful payments return message with appropriate information.
Cards requiring authentication do not allow purchase without authentication method.
A failed authentication comes up with a message: "We are unable to authenticate your payment method. Please choose a different payment method and try again."
A card with insufficient funds returns a message: " Your card has insufficient funds."

#### User Profile

Full address details are available for input, but are not required.
Updating individual fields updates the information on the profile and also for checkout.
Order history is displayed as anticipated and provides a full user purchase history.
The user's email as displayed is the email used to receive information about purchases.

#### Login and Logout

Users can login using their Google Account directly with no password required. User's can create an account on Warmasters with their Google Account. Conversely, a user can create an account using their email and successfully login with their password. User's can logout successfully when requesting to do so. The choice can be made at login whether to stay logged in or not. This is done with a checkbox "remember me".

### Game Pages

#### Create Character

Users are prompted to create a character before any purchases are made. This way a user will have a storage to keep their items as well as a character that the user will use in the role playing part of the game. Currently, four characters are available for use. On creation of a character a user receives 50 gold, and a storage size of 5000. Subsequently, the users bag is also created to hold 50 units and the trade can hold 200 units. All this is created when a user first makes their profile.

#### Character Profile

Users can access their game profile with their created character to access items they have purchased. Items are first sent to their storage, although a limit of 5000 units has been set, this is not in action while under test mode. Users can move or delete items. Items that are moved are deleted from their current location and created in their new location. There is no limit to the number of times an item can be moved. User's are greeted with a strong warning message if they are choosing to delete an item.

### Responsiveness

This application was tested for responsiveness across a variety of devices to ensure content remained readable and editable on various screen sizes.

The navigation, layout and various functionalities (login, logout, add, view, delete and update reviews) were tested across various screen sizes with Chrome Developer Tools.

These tests were performed on the following devices and browsers:

    Chrome and Firefox on Mac OS
    Chrome on Huawei P20
    Chrome and Firefox on Windows based 15in (38cm) Laptop
    Chrome and Firefox on Windows based 32in (71cm) Desktop

Tests were conducted by various members of the Code Institute's Slack Community, friends, family, and tutors from Code Institute.

### Known Bugs

All care was taken to ensure all bugs were removed. However, several times on Firefox on the developer's Windows based PC, the "delete" warning on items in a user's game profile would not activate. Restarting the server also did not solve the issue either. However, the issue is not able to be recreated on any other device and is considered a local only issue while under development.

The 404 error page was tested by removing the "Development" boolean at Heroku, but could not be tested locally. The 500 error page was not tested at all and could not be reproduced. However, it is anticipated that the Django standard 500 error page will suffice should the custom built page fail to load.
