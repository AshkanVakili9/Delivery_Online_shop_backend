
# Delivery_Online_shop_backend


Introduction: Online shop restful backend

Technologies used: Django, django_rest_framework, Docker, Nginx.

Purpose: The purpose of this project is to create an online shop backend that provides users with necessary features like product listings, cart management, order tracking and delivery system for costumers.


# Setup and Run the Project

Prerequisites


* Docker should be installed and running on your machine.


Steps


1. Clone the project from the GitHub repository.

* https://github.com/NoobstrGTR/Delivery_Online_shop_backend.git

2. Move into the project directory and run "docker-compose up" to start the project. 

3. Open your web browser and go to http://localhost:8000/ to view the app api's.


# Project Structure


The project starts with the following folders:
django folder contains the backend configuration and codes for different type of backend apps such as: 
# user_app
that includes user model and authentication based on phone number and password.
# store app
for third party person who can register a new stor inside the website.
# product app
this part include product models and like category subcategory tags images for product_line. 
# history app
this app contains comments, rate and adding product to favorite table.
# cart app 
here is the cart model for the customers who can buy products.


# Run The Proejct Without Docker

Explain how to get started with the project without docker and nginx, from installation to running the server.

1. install python 

2. py -m venv venv

3. .\venv\Scripts\activate

4. cd ./django

5. pip install -r req.txt

6. py manage.py makemigrations

7. py manage.py migrate

8. py manage.py createsuperuser

9. py manage.py runserver


# Database Schema

you can find the schema in a picture inside the directory named "Database_Schema.png"
![alt text]([http://url/to/Database_Schema.png](https://github.com/AshkanVakili9/Delivery_Online_shop_backend/blob/main/django/Database_Schema.png)
