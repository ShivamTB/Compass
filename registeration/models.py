from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Referrals(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='user')
    referrer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='referred_by')