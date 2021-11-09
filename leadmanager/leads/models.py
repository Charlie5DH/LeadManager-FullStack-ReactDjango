from django.db import models

# Create your models here.
# the model is basically the different fields we have
# after creating the models we have to create the miigrations to the
# database


class Lead(models.Model):
    '''
    Lead model class.

    Fields are:

    name: which is a char field
    email: is unique, char field
    message: char field, max length 500, optional
    created_at: a date time field which updates automatically
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
