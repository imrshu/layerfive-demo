from django.db import models


class UserDescription(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    mobile = models.IntegerField()
    address1 = models.TextField(null=True, blank=True)
    address2 = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=15)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'User Description'

    def __str__(self):
        return self.firstname + self.lastname
