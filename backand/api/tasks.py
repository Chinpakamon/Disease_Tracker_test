from backand.celery import app
from .service import send


@app.task
def send_otp_email(email):
    send(email)
