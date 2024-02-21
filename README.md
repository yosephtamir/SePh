# SePh
### Value your Time, Secure your property!
![landingpage](./images/landingpage.png)
## Challenge statement
Finding a house or property in Addis Ababa is very difficult, mainly because real estate(house) agents charge more than necessary and secondly because there is no time to go and look for a house for ownself.

To address this shortage, I plan to develop a website that will connect people looking for homes with people who have homes. This is done by people registering on the website and posting about the house. Then the house seekers choose the right one from the listed houses and make an agreement with the person who posted it through a chat room to rent the house they want.

## Run the app
to run the app use python3.8 -m web.app
### Check it out on https://yosephtamir.pythonanywhere.com/

## Admin area
administrators can add a city, subcity and category of the property using the following end points

1. 0.0.0.0:5000/city
2. 0.0.0.0:5000/subcity
3. 0.0.0.0:5000/category

### hint: we can use exceptional userids to access the links

## Database
For the ease of use SQLLite database is used in this project and can be changed from "/models/engine/db_storage.py" according to your needs.
Every database abstraction is located in /models/* directory. In this project SQLAlchemy is used as an Object Relational Mapper(ORM) Every Class of the table inherits from the basemodel located in /models directory

### This project has 10 db tables
1. user: is used to hold all datas of a user up on registration. most of the other tables are associated to a single user.
2. city, subcity, and category: are independent tables that can only be accessed by admins
3. chatroom, and messages : are used to make communications possible within the app
    chatroom is used for mapping conversations of two users in one while message is a child table of the room(Messages between two users has only one chatroom parent)
4. property holds a property details of a user's property: since a user can have multiple property their relation is one to many.
5. propertyimage: datas of images associated to a property is held in this table. it has one to many relation with a property(since single property can have upto three images)
6. roomusers: is optional db table used to hold roomusers of a single user. (This is not implemented in this project)

## The app
app.py contains all the routes to the web app with all the abstractions used to be served in the web pages

## Recommendations
The frontend of the app is not fully implemented yet, and jquery  is planned to be used. API will be developed soon.

## Licence
Copyright Protected

## Authors
1. Yoseph Tamirat

## Advisors
1. Inclusive Technologies