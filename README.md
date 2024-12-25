# Django projects

```
django-manage startproject myproject
python manage.py runserver
```
```
pip install djangorestframework
```
```
python manage.py startapp name
```

## CRUD operations

This project creates a simple page where users can create, edit, and delete books, with all actions displayed on the same page. The project uses the **Django framework** and **Bootstrap** to provide a clean, responsive UI. The following key concepts are used:

- **Form Handling**: Data is sent using HTML forms with POST method.

- **Built-in Template Tags and Filters**: Django's template tags and filters are used to send and receive data for performing CRUD operations and handling variables from view functions.

- **Bootstrap**: Bootstrap is used to style the table and buttons, providing a responsive layout.
  
- **Django Forms**: Django's built-in form handling simplifies the process of managing form inputs, making it easier to create, edit, and delete book entries.

> Note: For more advanced implementation I will use <code>genericview</code> and <code>viewset</code> from rest framework


## User Authentication System
Create a backend system for user registration and login with session or token-based authentication. 
This project focuses on securely managing user credentials and sessions. Users should be able to register, 
log in, and access protected resources based on their authentication status. Implementing this system involves 
handling password encryption, user sessions or tokens, and secure login procedures.

- create the apis(acreate user and curd operations) and test using insomnia
- make the views to login and male crud operation with json format, use genericview or apivews
- review the meta course about apis

```
pip install djangorestframework-authtoken
```

You first need to install rest framework token authentication, authtoken or simplejwt. Update Django settings, migrate the database, 