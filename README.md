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
This project is a simple user authentication system built with Django, integrating Djoser for user registration and token-based login, along with JavaScript for frontend interaction. Key features include user account creation via `/auth/users/`, token retrieval for authentication via `/auth/token/login/`, and a protected profile view at `/profileManager/profile/` that displays user information for authenticated users. The JavaScript implementation covers key concepts such as asynchronous programming using `async/await`, handling HTTP requests with the `fetch` API, managing state with `localStorage` for storing authentication tokens, and working with form events using the `onsubmit` handler for dynamic interaction between the frontend and backend. This project demonstrates the basics of Django REST Framework (DRF), Djoser, and frontend-backend integration.

