# Testing #

## Manual testing ##

### Responsiveness ###

I have tried to make the site as responsive as possible, but there still might be some issues. Time was a small factor in this. I tried to make it as best as I could.

- User story being tested: As a User, I want to be able to easily navigate the site on mobile, desktop and tablet

  - Test:
    - Each page of the website was created based on a desktop first approach because that will be the main place where the website will be used. After that for tablet and mobile.
    More information about responsiveness testing can be found in Compatibility and Responsiveness section
    - Results: Small issues, to name a view: Footer covering products on tablet and mobile view. Bag view not propperly visible.
  - Verdict: The issues found are fixed, the test passed.

### Navigation ###

- User story being tested: As a User, I want to easily navigate the site on mobile, Desktop and tablet.
  - Test:
    - Click on each link in the navigation bar to see if they're pointing the user to the correct page.
    - Check if navigation is changing links to the 'hamburger button' on tablets and mobile devices when resizing.
    - Check if navigation is fixed/show on the top of the page on each page when scrolled down - all devices.
    - Click the Account icon when the user is not logged in to a user account to see the 'Login' and 'Register' buttons on the dropdown menu are visible.
    - Click the Account icon when the user is logged in to see if the standard user 'Profile' section and 'Wishlist' section are visible.
    - Click the Account icon when Super User is logged in to see all standard user links plus product management link for adding a product is visible.
    - Click on the GetGameCodes logo - link to see if the user will be navigated to the Home Page.
  - Verdict: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Home Page ###

- Test:
  - Scroll down on Home Page to see, if all information is displayed correctly and easy to read.
  - Click on all links provide on the Home page and see if they lead to the correct pages.
- Results:
  - All information is present and pleasantly presented, leading to the correct pages.
- Verdict: Tests passed, everything works as expected, no bugs were found during the testing. Functionality covered.

### Products Page ###

- User stories being tested: As a User, I want to be able to view a list of all games to buy.
- User stories being tested: As a User, I want to be able to sort the list of games.
- User stories being tested: As a User, I want to be able to sort for specific game category.
- User stories being tested: As a User, I want to be able to easily see what I’ve searched for and the Number of results.
  - Test:
    - Click on the All Products Link in the navbar.
    - Search icon clicked/enter button pressed when the field is empty.
    - Search icon clicked/enter button pressed when the field is not empty.
    - Change filtering option.
    - Click on the 'product image to go to product details'.
    - Click on the 'Add to bag' button.
    - Click on the 'Wishlist' button.
  - Results:
    - All available products displayed.
    - When the search field is empty an error message is displayed; 'Please enter a valid search criteria'.
    - When the search field isn't empty search term is displayed below search box. Products matching the search term are displayed.
    - When Category links in navbar are clicked only products matching clicked category are presented.
    - When Single Category is clicked and filtering option is applied, page is showing products in the correct order.
    - All clicked buttons lead to correct pages.
  - Verdict: Tests passed, everything works as expected. Functionality covered.

- As a Super user I want to be able to edit/delete a product.
  - Test:
    - Click edit and delete buttons on product card.
  - Result:
    - Edit button links to product management so you can edit the product.
    - Delete button deletes a product from the database.

### Products Detail Page ###

- Test:
  - Click on the add to bag button.
  - Click on the add to wishlist button.
  - Click on the keep shopping button.
- Result:
  - Clicking the buttons leads to the correct page or action.
- Verdict:
  - Tests passed, everything works as expected. Functionality covered.

- Test:
  - Click on the quantity + or - buttons.
- Result:
  - Quantity updates as expected.
- Verdict:
  - Tests passed, everything works as expected. Functionality covered.

### Reviews ( On products detail page ) ###

- User stories being tested: As a logged in User and Super User, I want to be able to add a review to a games detail page.
- User stories being tested: As a logged in User and Super User, I want to be able to edit or delete a review I have created.
  - Test:
    - Click on Submit a review button
    - Click on edit button
    - Click on delete button
  - Result:
    - When clicking on the Submit a review button, a form presents itself to add a review and adds it to the review section.
    - When clicking on the edit button the same form presents itself and you can edit your review.
    - When clicking on the delete button you get a warning and can delete your review.
  - Verdict:
    - Tests passed, everything works as expected. Functionality covered.

### Wishlist Page ( In My Account dropdown ) ###

- User story being tested: As a logged in User and Super User, I want to be able to easily add a product to my wishlist
  - Test:
    - Click on the wishlist buttons
  - Result:
    - After click on wishlist buttons the product appears on the wishlist page.
  - Verdict:
    - Tests passed, everything works as expected. Functionality covered.

### Checkout Page ###

- User stories being tested: As a User, I expect to enter my payment info easily, have a easy way to follow payment procedure, have my information stored secure, get an order confirmation after checkout.
  - Test:
    - Add product to bag/checkout.
    - Try to click on the 'Secure Checkout' button.
    - Try to submit the form with incorrect email address (missing @).
    - Try to submit the form without providing a card number.
    - Add Stripe Test card information and click the 'Make a Payment' button.
  - Results:
    - Button is blocked until the user will provide all required information.
    - Form shows an error with wrong incorrect email address style.
    - Error message displayed by Stripe.
    - After successful test payment, the Payment Success Page / Checkout Success page is displayed.
- Verdict: Tests passed, works as expected. Functionality covered.

#### Checkout Success Page ####

- User story being tested: As a User, I want to Get an order confirmation after checkout.
  - Test:
    - Select one product to purchase
    - add selected workshop to bag
    - Fulfill information if not logged in to account
    - Provide card details
    - Click the 'Secure Checkout' button
  - Results:
    - After successful payment user is transferred to the Checkout Success page
    - Order confirmation is displayed on the screen. If the user is logged in, this summary is also displayed on the profile page
  - Verdict:
    - Tests passed, works as expected. Functionality covered.

### Profile page ( In My Account icon ) ###

My Profile - Order Review Page

- User story being tested: As a User, I want to have a personalized account page where I can view my personal information and update them and see what orders I’ve made.
  - Test:
    - Click on the My Account icon.
    - Choose to view either My Profile or Wishlist.
    - Click on order user want to display.
  - Results:
    - If the user is logged in My profile is displayed, otherwise, user has options for login or register.
    - After logging in user is navigated to the Homepage.
    - After clicking the My account icon, a dropdown is shown with the option to view either the My profile page or Wishlist page.
    - After clicking on an order on the My profile page, the order is shown.
  - Verdict: Tests passed, works as expected. Functionality covered.

Login/Register

- User story being tested: As a User, I want to easily register for an account, easily login or logout, easily recover my password in case I forgot, receive an email confirmation after Registering.
  - Test:
    - Click on the My Account icon when not logged in.
    - Click on the Login link.
    - Try to Login in with empty input fields.
    - Try to Login in with an incorrect password.
    - Try to Login in with the wrong email address.
    - Try to Login with correct credentials.
  - Results:
    - After clicking on the My Account icon user is presented with the login and register links.
    - Clicking either of them redirects them to the correct form page.
    - Login form validation system is displaying error messages
    - When all credentials are correct, the user is returned to the homepage and a success message is shown.
  - Verdict: Tests passed, works as expected. Functionality covered.

Page when SuperUser (CRUD)

- Site owner stories being tested: As a site owner, I would like to add/edit/delete a Product, add/edit/delete a Review.
  - Test:
    - When a superuser is logged in, additional function become active (Product management).
    - Try to access the Product management page with superuser account.
    - Click on Add product button on product management page
    - Trying to Add/Edit selected element with empty random required fields
     -Trying to Add/Edit selected element with all required fields filled
  - Results:
    - All links point to the correct page and that page gives the correct options for adding, editing and deleting Product or reviews.
    - All forms are validated and give an appropriate message when submitting.
    - When a user is logged in with superuser account, Product management page is displayed.
    - All links are pointing superuser to correct Admin page.
    - Remove functionality works as expected. By clicking Remove button all instance is removed including images if assigned to.
    - When the Edit button is clicked super user is navigated to the Edit Form Page of the selected instance.
    - When Add button is clicked super user is navigated to Add Form page of the selected instance.
    - When Add/Edit form is submitted and required fields are not placed or have incorrect format validation system is showing messages and the form is not submitted until all criteria match.
    - When Add/Edit form is submitted and required fields are correctly filled in form is submitted. The instance is added or edited and updated in the database.
  - Verdict: Tests passed, works as expected. Functionality covered.

## Validators ##

### HTML ###

All the HTML files were validated by using online code validator W3C HTML Validation Service. Errors were found about: img element missing alt, p element not allowed as child of h4 element, duplicate id, open elements.
All mentioned errors have been resolved. There is an error regarding hr elements: 'Error: The color attribute on the hr element is obsolete.  Use CSS instead.' but I am not able to get the hr element to take the color that I want using CSS.

### CSS ###

All the CSS files were validated by using an online code validator W3C CSS Validation Service. There were 2 errors and several warnings found. Errors found are 'Value Error : right only 0 can be a unit. You must put a unit after your number : 0.1' 'Property backdrop-filter doesn't exist : blur(10px)' Also, there are warnings about -WebKit- as validator is catching it as 'an unknown vendor extension'.

### JavaScript ###

All the JavaScript files were validated by using an online code validator JSHint.com. A missing semicolon was added to resolve an error. jshint esversion: 6 was added at the top of the Javascript files to resolve 2 errors. 2 warnings about undefined variables can be ignored. Own code is syntactically valid.

### Python ###

All Python files were validated by using an online code validator Pep8. File changes were made to make the code PEP8 compliant where possible.

## Debug = True ##

While developing an app, the local debugger: debug=True was on. Every time when the application has an error, the debugger was displaying an error message page. Thanks to that I could catch all errors and fix them straight away.

## Compatibility and Responsiveness ##

This website had been being tested during the development in Microsoft Edge. using Web Development Tools.

Mostly I've used Web Inspector and Responsive Design Mode to preview different webpages across various screen sizes, orientations, and resolutions, as well as custom viewports and user agents.

It has also been tested on different browsers.

I have used a responsiveness test app [responsively.app](https://responsively.app/) to test responsiveness further then just with the Development Tools.

## Bugs ##

### During development ###

**When trying to delete a product from a users wishlist an error occured:**

- *Error:* MultipleObjectsReturned at /wishlist/delete/2; get() returned more than one WishlistItem -- it returned 2!

- *Cause:* The get request tries to get the product requested out of all the wishlists where the product is saved in. So when more then 1 user has the same product saved in their wishlist, this error occurs.

- *Solution:* Added 'wishlist_id=wishlist_user' to get request, to specify out of wich wishlist the product has to be removed.

**While styling footer to stay on the bottom of the page. The footer aligned right on the profile page only.**

- *Cause:* Have not found the direct cause of why it is aligning right only on that page. It might have taken some styling from the content above it somehow.

- *Solution:* Wrapping the block content in base.hmtl inside a empty div has resolved the issue. Most likely because this seperated the content from the footer completely, making sure the footer does not take on any styling from the content.  

**Not able to find the column for first and last name in the user information.**

- *Cause:* I have not found what the direct cause of the issue was. The most likely cause is that something went wrong with migrating, but after reapplying migrations the error was not fixed.

- *Solution:* Seeing as I did not need these columns per se, I removed the first and last name colums from their respective models.

**Automatic emails were not being send after checkout or as email verification for a new user.**

- *Cause:* In the heroku config variables of my app, Deployment was set to 0 but was still in enviroment. So emails were send to local enviroment.

- *Solution:* Removing Development from the confic variables completely solved the issue.

**Error being shown when trying to open product details.**

- *Cause:* The column for the reviews was not found as i did not add them to the postgres database.

- *Solution:* Making new fixtures after adding the reviews in the Django admin and loading them to postgres resolved the issue.

**Error: Property backdrop-filter doesn't exist : blur(10px).**

- *Cause:* It is styling from bootstrap.min.css 4.4.1 so not much i can do about it.

- *Solution:* No solution found. It does not cause any issues, so i left it as it is.
