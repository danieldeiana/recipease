# Recipease

## Intro

This recipe site focuses on meals that are quick, easy, healthy and only have up to 8 ingredients.

Designed to fit around busy lifestyles, the user experience is simple and clean with limited clutter.

## Site flow

Meals can be filtered on the home screen by ingredient, category(ie breakfast) and name

User can save favourites and comment on recipes by signing up to premium

## Technologies

I shall be using Python with the following packages and technologies:

* django for the web framework
* postgresql for the database
* python-decouple, to seperate config info from code
* django-filter, to siplify the user filtering of objects in browser
* stripe to aid in the process of taking payments

## Run on your machine

* First clone the repository into your favourite virtual environment:

`$ git clone https://github.com/danieldeiana/recipease.git`

* Activate you virtual environment and whilst in the root folder (containing manage.py) run the following:

`$ python manage.py runserver`

* Then visit [localhost](http://127.0.0.1:8000/) in your browser

## Additional info

The css for the project has been kept in one file, within the recipe app

Due to complications using images with Heroku as a hobbyist, I've decided to create a image charfield(string) in the Meal model and link to external images