# Get Game Codes #

## A place for gamers to get their game keys ##

![Header Image](wireframes/header_image.png)

## Project goals ##

To give Gamers a site where they can buy their favorite game keys, and read or leave reviews about the games they bought or want to buy.

- [UX](#ux)
  - [User Goals](#user-goals)
  - [Scope](#scope)
- [Structure of the website](#structure-of-the-website)
  - [View for a guest user](#view-for-a-guest-user)
  - [View for logged in user](#view-for-logged-in-user)
  - [User Stories](#user-stories)
- [User Requirements and Expectations](#user-requirements-and-expectations)
  - [Requirements](#requirements)
  - [Expectations](#expectations)
- [Design Choices](#design-choices)
  - [Colors](#colors)
  - [Fonts](#fonts)
  - [Icons](#icons)
  - [Structure](#structure)
- [Wireframes and Data Models](#wireframes-and-data-models)
  - [Wireframes](#wireframes)
  - [Data Models](#data-models)
- [Features](#features)
  - [Features that are implemented](#features-that-are-implemented)
  - [Features to be implemented](#features-to-be-implemented)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Libraries and Frameworks](#libraries-and-frameworks)
- [Front End](#front-end)
- [Back End](#back-end)
  - [Tools](#tools)
- [Testing and Bugs](#testing-and-bugs)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
- [Credit](#credit)
  - [Source credits](#source-credits)
  - [Image credits](#image-credits)
  - [Special thanks](#special-thanks)

## UX ##

### User Goals ###

- The website has to work well on all devices like mobile phones, tables and desktops
- The login procedure should be clear and feedback should be given when appropriate
- The registration process should be clear, easy to do and feedback should be given when appropriate
- The website has to be easy to use and easy to update information
- Visually appealing website

### Scope ###

An easy to navigate and responsive website that is fun to use and allows users as well as site owners, to perform CRUD operations. Users can sign up and, once logged in, they can leave reviews about games. These users can see their purchase history, and manage their account settings.

## Structure of the website ##

### View for a guest user ###

A user that is not logged in and/or registered, will see a homepage with a list of multiple games that they can buy. Starting with the highest ranked game avalible.
The user will be given the option to create an account on every page, where they can view their purchase history and gives them the option to leave reviews on games they have bought.

### View for logged in user ###

A logged in user will benefit from the full functionality of the site. The navigation bar will contain an extra button called: 'Logout' when they are logged into their account.
This user is now able to leave reviews on games they have purchased and register themselfs for the site blog where gamers share there full experiences with their favorite game.
In the profile tab they can see and change their personal information and view their purchase history.

### User Stories ###

This file is not complete. Changes might be made during development, depending on functionality and usability.

| as a/an…    | I want to be able to…                                                          | So that I can…                                                                                               |
|-------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| User        | Easily navigate the site on mobile, Desktop and tablet                         | Quickly look if the game I am looking for is on the site                                                     |
|             | View a list of games to buy                                                    | Choose something to buy                                                                                      |
|             | Read blog posts                                                                | Get informed about games I’m planning to buy                                                                 |
|             | Easily register for an account                                                 | Have a personal account                                                                                      |
|             | Sort the list of games                                                         | See best rates, best prices and search product by category                                                   |
|             | Sort for specific game category or platform                                    | Find best-priced or best-rated product in a specific category                                                |
|             | Easily see what I’ve searched for and the Number of results                    | Quickly decide whether the product I want is available                                                       |
|Logged User  | Easy to follow payment procedure                                               | Order quickly and start gaming                                                                               |
|             | View the items in my bag                                                       | See what I’ve ordered and what the total cost is                                                             |
|             | Enter my payment info easily                                                   | Check out quickly without problems                                                                           |
|             | Have my information stored secure                                              | Rest assured my personal info is safe                                                                        |
|             | Get an order confirmation with game key after checkout                         | Keep a copy for future reference/waranty                                                                     |
|             | Easily leave a review                                                          | Let people know what I think about the game                                                                  |
|             | Easily login or logout                                                         | Access my personal account information                                                                       |
|             | Easily recover my password in case I forgot                                    | Recover access to my account                                                                                 |
|             | Receive an email confirmation after registering                                | Verify that my account registration was successful                                                           |
|             | Have a personalized account page                                               | View my personal order history and order confirmations and save My payment information                       |
|             | Get a subscription to receive an email when A new newsletter becomes available | Check if there are any deals on games I'd like to buy                                               |
| Store owner | Add a product                                                                  | Add new items to my store                                                                                    |
|             | Edit a product                                                                 | Edt product details                                                                                          |
|             | Delete a product                                                               | Delete a product                                                                                             |
|             | Add blog posts                                                                 | Inform registered users about games they might want to buy                                          |
|             | Edit Blog posts                                                                | Change the content of a blog I have posted                                                          |
|             | Delete blogposts                                                               | Remove a blog I have posted                                                                         |
|             | Add owners review                                                              | Give my personal opinion on a game                                                                  |
|             | Edit owners review                                                             | Change my opinion on a game                                                                         |
|             | Delete owners review                                                           | Remove my opinion on a game                                                                         |
|             |                                                                                |                                                                                                              |

## User Requirements and Expectations ##

### Requirements ###

- Easy to navigate by using buttons in navbar
- functional account page with a good overview
- Easy way to find the game they are looking for
- Ability to save favorite games to wishlist
- Ability to contact the site owner

### Expectations ###

- Registering for an account should be easy and straight forward.
- To have a account page that has a clear overview of games I have bought and my personal info.
- It should be easy and quick to buy an game.

## Design Choices ##

I chose a simple design that doesn't distract users from the main goal of the site, selling games.

### Colors ###

I have used [Coolors](https://coolors.co/) for creating my color scheme.

![Color scheme](wireframes/color_pallet.png)

FFFFFF : Mainly for text on the site as the backgrounds are dark colors.
192839 : As main background color.
1F143D : For navbar and footer background.
CC0000 : Used mainly for important messages or discount icons.
00CC00 : Main use is for most buttons on the site.

### Fonts ###

For headers and titles on the site: [Inter](https://fonts.google.com/specimen/Inter?preview.text=Get%20Game%20Codes&preview.text_type=custom)

For main text on the site: [Roboto](https://fonts.google.com/specimen/Roboto)

Fonts are from [Google Fonts.](https://fonts.google.com/)

### Icons ###

Icons used are from [Font Awesome.](https://fontawesome.com/) The are used in moderation and match the colors and overall feel of the design.

Icon used in logo is from [flaticon](https://www.flaticon.com/)

### Structure ###

For the structure I have used [Bootstrap.](https://getbootstrap.com/)

## Wireframes and Data Models ##

Wireframes where created at the very beginning of this project, and have been followed as much as possible.

### Wireframes ###

For creating my wireframes I have used [Balsamiq](https://balsamiq.com/)

[Desktop](wireframes/wireframes_desktop.pdf)

[Tablet and Mobile](wireframes/wireframes_tabletmobile.pdf)

### Data Models ###

During the development, I worked with sqlite3 databases, installed with Django. For production I have used [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql).

- The User model I have used in this project was provided by Django Allauth. It is a part of default django.contrib.auth.models.

## Features ##

### Features that are implemented ###

- Registration functionality
- Log In and Out functionality
- Able to leave reviews on purchased games
- Sign Up for newsletter (MailChimp)
- Contact site owner
- Having a profile page
- Able to add games to wishlist

- CRUD Functions:
- Create:
  - Account (profile)
  - Add review to game
  - Create wishlist

- Read:
  - Account (profile)
  - General info (game info, game reviews, purchased games,)
  - Wishlist

- Update:
  - Account(profile)
  - reviews
  - Wishlist

### Features to be implemented ###

- Giftcards (for Steam, Epic Games, Psn store etc..)

## Technologies used ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JS](https://nl.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Frameworks ###

## Front End ##

- [Font Awesome](https://fontawesome.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)
- [jQuery](https://jquery.com/)

## Back End ##

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Pillow](https://pypi.org/project/Pillow/)
- [Gunicorn](https://gunicorn.org/)
- [PEP8](http://pep8online.com/)
- [Stripe](https://stripe.com/en-nl)

### Tools ###

- [Git](https://git-scm.com/)
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [Balsamiq](https://balsamiq.com/)
- [W3C HTML Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
- [Gimp](https://www.gimp.org/)
- [Tinypng](https://tinypng.com/)
- [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab)
- [For generating a table of content:](http://ecotrust-canada.github.io/markdown-toc/)

## Testing and Bugs ##

## Deployment ##

### Local Deployment ###

## Credit ##

### Source credits ###

### Image credits ###

I used [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab) for creating my [logo](media/logo.png)
The icon used in the logo is from [flaticon](https://www.flaticon.com/)

### Special thanks ###

**Site for educational purposes only!**
