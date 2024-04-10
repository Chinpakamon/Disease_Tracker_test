## Longevity InTime Test Tasks

#### About project:

This is a project that involves creating a RESTful API with Django, integrating
authentication and authorization, setting up Celery for message queues, and
building a management panel with CRUD operations.

#### Test Tasks:

Backend:

1. Project Setup and Version Control.
2. API Design and Implementation.
3. Secure Password Hashing and Storage.
4. Validation, Error Handling, and Documentation.
5. Custom User Model and Authentication.
6. Message Queue with Celery.
7. Database and Deployment.

#### Project Requests and Responses:

1)Registration -> ```http://127.0.0.1:8000/register/```:

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

2)After registration, an OTP code will be sent to your email for confirmation.
This is implemented using Celery.
```commandline
Ваш код подтвержения регистрации.

от ...@yandex.ru
Время 15:25 (2 часа назад)
кому: мне

Ваш код OTP: 721457
```

3)Receiving a token -> ```http://127.0.0.1:8000/auth/token/login/```:
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
4)Delete your account sent delete request to -> ```http://127.0.0.1:8000/auth/users/me/```:
```commandline
Request:
{
    "username": "Vladislav",
    "email": "your_email@gmail.com",
    "current_password": "Lolkek12"
}
```

#### Project installation:

1)Cloning the repository:

```git clone git@github.com:Chinpakamon/Disease_Tracker_test.git```

2)Installing a virtual environment:

```python3 -m venv venv```

3) Activate a virtual environment:

```siurce venv/bin/activate```

3)Install requirements.txt:

```pip install -r requirements.txt```

4)Create a .env file and format it as .env.example.

5)Make migrations:

```python3 manage.py makemigrations && python3 manage.pt migrate```

6)Run Redis in docker ([documentation](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#redis)):

```docker run -d -p 6379:6379 redis```

7)Run logs for Celery tasks:

```celery -A backand worker -l info```


8)Start the server:

```python3 manage.py runserver```