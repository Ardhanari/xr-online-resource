
# Extinction Rebellion - online resource

Extinction Rebellion - online aims to provide access to various resources across the internet on climate crisis, extinction rebellion and news and data in a user-friendly way. Different types of documents are grouped in categories and new entries can be added by anyone at any time. Logged in users can also edit and delete records as well as upvote these they deem valuable.

![responsive view](https://i.imgur.com/sA8SKpa.png)

## Table of content

### 1. [Project Design](#Project-Design)
-   [Design](#Design)
-   [Colours](#Colours)
-   [Fonts](#Fonts)
-   [User objectives](#User-objectives)
-   [Developer objectives](#Developer-objectives)

### 2. [Features](#Features)
-   [Existing features](#Existing-features)
-   [Features left to implement](#Features-left-to-implement)

### 3. [Information architecture](#Information-architecture)

### 4. [User testing](#User-testing)

### 5. [Technologies Used](#Technologies-Used)

### 6. [Deployment](#Deployment)

### 7. [Acknowledgements](#Acknowledgements)


## Project design
'Extinction Rebellion - online resource' came to my mind as something very simple and clear to use. The layout from the beginning was supposed to be minimalistic and unobtrusive. Main goal of this website after all is to facilitate access to other sites and doing it efficient, not elaborately.

The objective for me while building this website was to achieve maximum usability in minimalistic look. The site is supposed to be lightweight, toned and serve its main purpose above everything else - provide easy access to resources spread across the internet. Therefore, no pictures and redundant elements are present across the website.



### Design

The process started with creating mockups that served as a guide as to what pages should be created, how the information should be spread across them and how they are supposed to look like.

The design was based loosely on Extinction Rebellion main design programme as well as inspired by [posters designed for Polish branch of XR](https://drive.google.com/open?id=1KUBdPTM1kT6CaU6jUGheIx_EsBva6fC5).

**[mention any changes between mockups and final project]**

### Colours

Colour scheme is clear and straighforward:

-   #202020 - background
-   #000000 - navigation and button backgrounds
-   #ffffff - font and icon color
-   #00FF66 - link indicator in these instances where links are not styled as buttons
-   #F44336 - warning text

Limited palette makes sure the focus of the user is directed straight to the information. It is intended to present but not overshadow the content, making sure it stays in the background.

On the other hand, placing the elements on the pages makes sure that, despite limited colors, the website is not boring to the eye.


### Fonts

-   The resource uses two fonts across all pages - Fuxced Caps, which is offcial Extinction Rebellion font and simple sans-serif font.

-   The reasoning behind it was simple - one is brand font specified by XR brand guide and is used for titles and headings, the other is there just to make sure the rest of the website displays properly.


### User objectives

-   The website has been designed for people needing access to various resources spread across the internet. We all probably were in that place before, where we know something (article, document, video) exists, but any attempt to googling brings no relevant results. This small database is intended to make this process easier.

-   Links are grouped by categories. Categories represent type of media referenced in the database: Articles, News, Social media posts, Blogs/Vlogs, offline sources, Documents, Other sources. This reasoning was chosen above other proposed categories split. The other proposed solution was to group resources by their themes. Unfortunately in many cases, resources are either multi-thematic. Another issue with that solution was defining categories and making them crystal clear to the end user. Categories representing types of resources rather than their subjects/themes are more strict and therefore easier to understand and use.

-   Voting option (available to logged in users) allows users to vote on helpful resources, so they appear higher on the page (and may be noticed by others) more easily.

-   All users can add links, logged in users can on top of that edit records if they feel like they can improve them or delete these, that are irrelevant.


### Developers objectives

-   User-friendly front-end application, allowing easy and frustration-proof access to the database
-   Adding little brick to the global project such as Extinction Rebellion
-   Portfolio use


### User stories

- User engaging in the online discussion, needing specific links as arguments
- User searching a resource they remember but cannot find via google
- User looking for more information on a specific subject

### Hopes for the website are:

-   To serve its purpose, at least in limited capacity


## Features

-   Easy access to all records on the main page (read)

-   Voting function on each record, allowing user to have an influence over how the records are sorted/displayed by default

-   Option to sort records by date added or number of votes

-   Every record have it’s own detail page, that displays additional informations/options

-   including editing the information about the record (update)...

-   ...and deleting the record entirely (delete) - at least from accessing it from the front-end, the records are moved to a hidden collection, as a way of protecting perfectly valid records to be lost due to a mistake or malicious action.

-   Easy way to add new entries - user fills out the form and the link with all it’s information is added to the database instantly (create)

### Existing features

#### Navigation

-   Following links are visible: Home, Add new link, Categories and Log in (or Log out if user is already logged in)

-   Users on mobile devices have these in foldable menu

-   Desktop users have these on the top of the site in a fixed navigation bar


##### Breadcrumbs
- Allow easy navigation between pages without using browser's 'back' and 'forward' buttons

#### Pages:

##### Home Page

-   Displays all records from the repo collection, from newest to oldest, with their title, category, URL and upvotes.

-   Allows sorting displayed records by the time they were added or number of upvotes

-   Allows to access their detail pages as well as go straight to the source material


##### Login

-   Allows user to log in, if their profile was created before

-   As of the time of writing this document, user cannot register themselves.


##### Browse categories

-   Provides overview of all categories available, along with their short descriptions (if available)


##### Single category

-   Displays all records belonging to selected category in the same style as Home Page


##### Single Record

-   Displays detailed information on a single record - that includes everything displayed on the homepage + its description

-   Allows logged in users to vote on a record

-   Allows logged in users to edit or delete a record


##### Add Record

-   Contains form allowing user to add new entry to the database

-   Obligatory fields: Title, URL (validated), Category

-   Description field is not obligatory


##### Edit Record

-   Displays the same form as ‘Add record’ page but with fields pre-populated with existing information

-   Keeps existing ‘date_added’ and ‘votes’ values behind the scenes

-   Disallows saving the record with empty fields


##### Confirm Deletion

-   Offers one last step before deleting the record from the collection


### Features left to implement

####  SECURITY???
![](https://i.imgur.com/xvW4iAR.png?1)
- This project is initially released with barely any security at all. What is lacking and will be amended as soon as possible is:
	- secure password storage
	- registration available to users and confirmed by email, together with protection from spamming db with fake users data
	- option to reset/change password by user

#### Search

-  It's not a proper repository without keyword search. This feature was cut from initial release due to various instances of force majeure during development of this project.

#### Voting
- This needs to be improved to allow voting only oncer per record per user.


## Information Architecture

A MongoDB NoSQL database was used in the creation of this website. Database used to store data consists of 4 collections:

### Repo

#### Main (links) collection structure:

    {

	    _id : ObjectId(),

	    title : String,

	    url : String,

	    desc : String,

	    category : String,

	    date_added : Date,

	    votes : Int32

    }

### Users

#### Registered users collection structure:

    {

	    _id : ObjectId(),

	    login : String,

	    password : String,

	    email : String,

	    date_created : Date

    }

### Categories

#### Categories collection structure:

    {

	    _id : ObjectId(),

	    category_name : String,

	    desc : String

    }

### Deleted

Hidden collection gathering all records deleted from Repo.

Follows the same structure as documents in Repo.

## User testing

The following tests were performed to test usibility and functionality. At the time of a final testing, all features passed the functionality test as expected.

-   **(describe tests)**


### Bugs found during development and initial testing

The following bugs were found when performing the initial tests.

- using 'back' and 'forward' buttons in the browser sometimes causes record_id to be lost and makes URL broken.
    - one way to solve is to create custom 404 page,
    - the other way: to catch these errors and prevent them
- editing record would remove its date and number of votes (fixed in one of the [commits](https://github.com/Ardhanari/xr-online-resource-5.10-backup-/commit/22a430cfefb0cc097a6d4abf00de894cd382e9df))

## Technologies Used
### Tools

-   AWS [Cloud9](https://aws.amazon.com/cloud9/)
-   [GitPod](https://gitpod.io)
-   [Git](https://git-scm.com/)
    -   Version control during the development process.
-   [GitHub](https://github.com/)
    -   Remote repository.
-   [Figma](https://www.figma.com/)
    -   Building mockups
-   [Google Chrome - Dev Tools](https://www.google.com/chrome/)
    -   Testing responsiveness, and manually debugging code.
-   [PIP](https://pip.pypa.io/en/stable/installing/)
    -   Installing tools needed in this project.
-   [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    -   Hosting database used for this project


### Libraries

-   [JQuery](https://jquery.com/)
	-   Simplifies DOM manipulation.
-   [Materialize](https://materializecss.com/)
    -   Speeds up the development process and creating responsiveness design
-   [Material Icons](https://material.io/resources/icons/)
-   [PyMongo](https://api.mongodb.com/python/current/)
    -   Facilitates communication between Python and MongoDB.
-   [Flask](https://flask.palletsprojects.com/en/1.1.x/)
-   [Jinja](http://jinja.pocoo.org/docs/2.10/)


### Programming languages

-   This project uses HTML, CSS, JavaScript and Python.
-   The code was validated/formatted using following tools respectively: [W3C HTML Validator](https://validator.w3.org/), [W3C CSS validator](https://jigsaw.w3.org/css-validator/) and [Pythoniter](https://pythoniter.appspot.com/)
-   README.md written with grand help of [stackedit.io](http://stackedit.io)


### Deployment

-   This project was developed using the AWS Cloud9 and GitPod.
-   This project was regularly pushed to its GitHub repository [https://github.com/Ardhanari/xr-online-resource-5.10-backup-](https://github.com/Ardhanari/xr-online-resource-5.10-backup-), full list of commits is available at [https://github.com/Ardhanari/xr-online-resource-5.10-backup-/commits/master](https://github.com/Ardhanari/xr-online-resource-5.10-backup-/commits/master)
-   The project was deployed on [Heroku](http://xr-online-resource.herokuapp.com/)


## Deployment
### Local deployment

You need Python3, pip, Git and MongoDB to run this project locally.

1.  Go to [this page](https://github.com/Ardhanari/xr-online-resource-5.10-backup-) and click on ‘Clone or download’ button
2.  Copy the URL from ‘Clone with HTTPS’ tab
3.  Open your terminal/bash
4.  While being in the location you want the cloned directory to be saved, type git clone and paste the URL that you copied, accept with Enter
5.  Create virtual environment with environment variables (IP, PORT, MONGO_URI, SECRET_KEY)
    OR:
    -   Define these variables in app.py as follows:
    -   'IP', '0.0.0.0'
    -   'PORT', '8000'
    -   'SECRET_KEY', your string of choice
    -   'MONGO_URI', mongo_uri of your database, see [documentation](https://docs.atlas.mongodb.com/driver-connection/)
6.  Install all required modules from requirements.txt using pip3 install -r requirements.txt in your terminal
7.  Now the project is ready to be run locally

### Heroku deployment

1.  Install heroku using pip.
2.  Log in to your account typing heroku login in the terminal and following the steps.
3.  requirements.txt and Procfile are necessary files for deployment. To create requirements.txt, use command `pip freeze > requirements.txt` in the terminal
4.  To create Procfile, use: `echo web: python3 app.py > Procfile`
5.  Commit and push existing files to your repository on GitHub
6.  Create new app in [your heroku dashboard](https://dashboard.heroku.com/apps), set its name and region.
7.  On app’s dashboard select Deploy and then choose GitHub (you can also skip pushing your files to github and push them directly to heroku the same way it is done with GitHub)
8.  On the same dashboard set environmental variables by selecting ‘Reveal Config Vars’ in Settings and adding:
    -   IP - ‘0.0.0.0’
    -   PORT - ‘8000’
    -   MONGO_URI - mongo_uri of your database, see [documentation](https://docs.atlas.mongodb.com/driver-connection/)
    -   SECRET_KEY - key of your choice
    -   DEBUG - ‘False’
10.  Your site is now succesfully deployed on Heroku.

### Acknowledgements

-   Many thanks to my CI mentor Seun Owonikoko for help
-   Code Institute Slack community’s both solid help and sense of humour should be praised
-   Code Institute materials were my support not only for learning prior starting this Milestone Project but also as a reference while building it
-   Many thanks to all Extinction Rebellion people for brave fight and standing together as an example for the whole world. Also for:
	-   brand guidelines, style and font
	-   bringing purpose to many of us

### Disclaimer
-   All the entries in the database are references created by users. There are no hosted files on site’s server.
-   Project built as a Milestone Project 3 for Code Institute