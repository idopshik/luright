from django.db import models

# Create your models here.

class Mitglieder(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)


class ProfilePic(models.Model):
    mitglieder = models.ForeignKey(Mitglieder,
                             related_name='images_created',
                             on_delete=models.CASCADE)
                            blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created = models.DateField(auto_now_add=True, blank=True)

