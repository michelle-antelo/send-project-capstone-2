# Send Project App
By Michelle Antelo
___
Table Of Contents
- [Send Project App](#send-project-app)
  - [App Heroku Link](#app-heroku-link)
  - [Description](#description)
    - [MVP](#mvp)
    - [Planned Bonus Features](#planned-bonus-features)
  - [Api](#api)
  - [Initializing Project](#initializing-project)
  - [Data Flow](#data-flow)
  - [Database Schema](#database-schema)
___
## App Heroku Link

___
## Description
New climber at a bouldering gym wants some more information on how to figure out a move on this V2! Never fear, The Send Project is here! Through this app, climbers can view information on all of the routes in the gym along with basic climbing holds and techniques. Information includes images, videos, techniques utilized, sections, wall angles, hold types, along with ratings and comments from other climbers! Along with viewing vital information, climbers will be able to create accounts that allow them to save climbs along with uploading their send videos to their accounts. Here their friends can view their posts along with congratulating them! 
___
### MVP
- Add/Remove Routes
  - Display route info
- Add Users/Admins
  - User Database
  - User page 
    - Logout Button
    - Edit User Button
    - User Data Display
  - Edit user Page
  - Login/Signup
    - Login User form
    - Signup User Form

___
### Planned Bonus Features
- 
___
## Api
  I created the API
___

## Initializing Project
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ createdb send_project   
    $ db.create.all()
    $ flask run
___
## Data Flow
Login Flow
UI --> Login --> Authenticate --> UI
Update User Flow
UI --> Database --> UI
___
## Database Schema
* User
  * UID
  * Username (Required)
  * Password (Required)
  * Email (Required)
  * Profile photo (Default)
  * Bio (Default)
  * Parks Id's
  * Friend Id's
___