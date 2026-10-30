# Zuri Bistro - Restaurant Website

A Django website for a restaurant, built entirely on an Android phone.

## Features
- Home page with opening hours and contact details
- Menu grouped by category, managed from the admin
- Online table reservations saved to the admin
- Mobile-friendly design

## Tech
Python, Django, SQLite, HTML/CSS

## Run locally
    pip install django tzdata
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
