# Cookery Instructions

### An online cookery Instructions Website created by Vijayalakshmi Dhandapani.

[View live site here](http://ms3-cookery-instructions.herokuapp.com/)

![Responsive-view](static/images/responsive_img.JPG)

# Milestone Project 3

This site is made by using **HTML**, **CSS**, **javascript**, **Python**, **MongoDB**, and **Flask Framework**. 
The purpose of this site is to show CRUD functionality and Database accessibilty.
***
## Table of Contents

* [Project Overview](#project-overview)

* [User Experience](#user-experience)
    
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)

* [Planes of Development](#planes-of-development)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
        * [Wireframe](#wireframe)
        * [Database Schema](#database-schema)
        * [Sitemap](#sitemap)
    * [Surface](#surface)
        * [Color](#color)
        * [Typography](#typography)
        * [Images](#images)

* [Database model](#database-model)

* [Features](#features)
    * [Features Used](#features-used)
    * [Features to be implementd in Future](#features-to-be-implemented-in-future)

* [Technologies used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks](#frameworks)
    * [Extensions and Kits](#extensions-and-kits) 
    * [Project Management](#project-management)
    * [Tools](#tools)

* [Resources](#resources)

* [Testing](#testing)

* [Deployment](#deployment)
    * [Prerequisites](#prerequisites)
    * [How to Clone Bazaar](#how-to-clone-bazaar)
    * [How to Deploy to Heroku](#how-to-deploy-to-heroku)

* [Credits](#credits)
    * [Content](#content)
    * [Code](#code)
    * [Acknowledgments](#acknowledgments)
***

## Project Overview

The Cookery Instructions website for people who simply love cooking, or even just beginning to be interested in cooking.

People, who would like to see someone's recipes for new ideas or to share their own recipes with other people.

The purpose of this site is to serving the best recipes in simply and easily.

All the recipes are visible to all the users to they don't need to create an account if they just would like to see recipes.

If users would like to create and post their own recipes or known recipes they need to create an account. The process of creating an account is very simple.

The website is designed to be suitable for use on all devices, from mobile to desktop.

[Go back to Top](#table-of-content)
***

## User experience

### User Goals

1. As a user, I want to display and work on my site in all devices from large screen monitors, Laptops to tablets and phones.
2. As a user, I want the website to be visually simple and easy cooking recipes.
3. As a user, I want to find the recipe listing feature to be searchable, so user can serach for specific recipes.
4. As a user, I want an easy login or signup to the website.
5. As a user, I want the website to be easy to add,edit or delete their own recipes.
6. As a user, I want the website that focuses on healthier choices and delicious meals.

### User Stories

1. As a user, I want to be able to easily find the favourite dishes that I am looking for.
2. As a user, I want to search the dishes by using simple words.
3. As a user, I want to select dishes by their appearance.
4. As a user, I want to know the ingredients,method and cooking instruction for specific dishes.
5. As a user, I want to contact the admin of the page if I am facing some technical issues.
6. As a user, I want to register or sign up my account and able to add their own recipes.
7. As a registered user, I want to login my account and make some changes to my recipes.
8. As a registered user, I want to login my account and add another recipes.
9. As a registered user, I want to login my account and remover my recipes.
10. As a registered user, I want to login from mobile or tablets and expect the site and image to be fully responsive.
11. As a registered user, I want to logout easily.

[Go back to Top](#table-of-content)
***

## Planes of Development
### Strategy

The aim of making this site is to make a website that has CRUD mechanism and Database access functionality.
I decided to make a cookery instructions site, which will work as a platform for peoples to learn new varieties of dishes in very simple and easy method.
People who have less experience in cooking and would just like to see recipes, they can do it simply by visiting the website where all the recipes are shown.
To see recipes, users do not need to register so it is hassle-free.
The main goal of this wbsite is to provide a recipe platform that is easy to use.

### Scope
To achieve users goals, below are the minimum features to be included in this project.
CRUD (Create,Read,Update and Delete) functions are required for this project so these are implemented as a part of essential features.

- Simple Home page design that first time users can easily understand the purpose of the website.
- Recipes are displayed in a grid of "cards" consisting of an image and recipe title, clicking on a recipe button takes you to the recipe details page.
- All the recipes are shown on Recipes details page.
- Register page where users can create an account to create(add), post and edit their recipes.
- Login page where users can log in to the website.
- Logout function that users can log out the website.
- Profile pages where users can see all their recipes and access to create(add), edit and remove their recipes.
- Create(add) Recipe page where users can create(add) and post their recipes.
- Edit Recipe function that users can edit their recipes.
- Delete Recipe function that users can delete theri recipes.
- Search by a keyword(s) function that users can search for specific recipes.
- 404 page that appears for invalid URL and takes user back to *Home* page of the website safely.
- Users can contact the admin easily for Support or Feedback.

### Structure
- This website consists of multi-pages, where pages are connected through Navigation Bar or Python. 
- The navigation bar will have links for the Home page, Recipes, Login, Signup, and Support/Feedback form. 
- The navigation links will change and show the logout and add new recipe option Once the user is logged in. 
- The navigation bar will be collapsible for Mobile view and expand in a sidebar when clicked. 
- There will be a footer, which will show the social network. It will be sticky and always remain at the end of the page. 
- There are two forms will be there, one for Login and the other for signup. 
- The support / Feedback form will also be there for the user to contact and get support from admin.
- There will be pages for adding the new recipes and Editing the already published recipes by the specify users. User can also delete their recipes or post if they want. 
- Admin will have the power to delete any post if that is unsuitable for the page. 
- All the data will be stored in MongoDB and Flask framework will be used to develop the site and finally, it will be deployed by using Heroku.

### **Skeleton**
#### **Wireframe**
The wireframe for this project has been made for Three screen sizes(Laptop View, Tablet View and Mobile View).

The wireframes for this Project can be seen here.
[Wireframe](static/images/wireframe.pdf)

#### **Database Schema**
The Schema is pepared for the better understanding of the Database Collection.

This Project has 3 collection. Categories,recipes and users.

Database Schema can be seen here. [Schema](static/images/database_schema.pdf)

#### **Sitemap**
Sitemap is prepared for this site to understand the navigation of the pages.

Sitemap can be seen here. [Sitemap](static/images/sitemap.pdf)

### **Surface**
#### **Color**
The color theme is used from Materializecss.com. It is decided by keeping Hero image in consideration and mainly two colours cyan(#006064 ) 
and light-blue(#03a9f4) and their shades are used according to the page requirement.




 

