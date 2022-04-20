from django.db import models
# from user.models import newuser
# Create your models here.
class birthday_data(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    user_id = models.IntegerField(default='0',null=True,blank=True)

    def __str__(self):
        return self.name