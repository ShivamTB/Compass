from django.contrib.auth.models import User
from registeration.send_email import send_registeration_email

user = User.objects.get(id=1)

send_registeration_email(user)