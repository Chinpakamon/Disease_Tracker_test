## Longevity InTime Test Tasks

### About project:

This is a project that involves creating a RESTful API with Django, integrating
authentication and authorization, setting up Celery for message queues, and
building a management panel with CRUD operations.

### Test Tasks:

Backend:

- Project Setup and Version Control.
- API Design and Implementation.
- Secure Password Hashing and Storage.
- Validation, Error Handling, and Documentation.
- Custom User Model and Authentication.
- Message Queue with Celery.
- Database and Deployment.

### Project Requests and Responses:

- Registration -> ```http://127.0.0.1:8000/register/```:

```commandline
Request:
{
    "username": "Vladislav",
    "email": "your_email@gmail.com",
    "password": "Lolkek12"
}

Response:
{
    "username": "Vladislav",
    "email": "your_email@gmail.com",
    "id": 1
}
```

- After registration, an OTP code will be sent to your email for confirmation.
This is implemented using Celery.
```commandline
Ваш код подтвержения регистрации.

от ...@yandex.ru
Время 15:25 (2 часа назад)
кому: мне

Ваш код OTP: 721457
```

- Receiving a token -> ```http://127.0.0.1:8000/auth/token/login/```:
```commandline
Request:
{
    "username": "Vladislav",
    "email": "your_email@gmail.com",
    "password": "Lolkek12"
}

Response:
{
    "auth_token": "2da97e83e7d9c664e7f9b0d645f752b0d3c1ff3e"
}
```
- Delete your account sent delete request to -> ```http://127.0.0.1:8000/auth/users/me/```:
```commandline
Request:
{
    "username": "Vladislav",
    "email": "your_email@gmail.com",
    "current_password": "Lolkek12"
}
```

- Link to swagger documentation -> ```http://127.0.0.1:8000/swagger/```

[More endpoints and requests in documentation](https://djoser.readthedocs.io/en/latest/base_endpoints.html)

### Project installation:

- Cloning the repository:

```git clone git@github.com:Chinpakamon/Disease_Tracker_test.git```

- Installing a virtual environment:

```python3 -m venv venv```

- Activate a virtual environment:

```siurce venv/bin/activate```

- Install requirements.txt:

```pip install -r requirements.txt```

- Create a .env file and format it as .env.example.


- Make migrations:

```python3 manage.py makemigrations && python3 manage.pt migrate```

- Run Redis in docker ([documentation](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#redis)):

```docker run -d -p 6379:6379 redis```

- Run logs for Celery tasks:

```celery -A backand worker -l info```

- Start the server:

```python3 manage.py runserver```