from django.db import models

# Create your models here.


class Project(models.Model):
    # we tell tha this is a table

    # title = character field max lenth is parameter
    # for how chars can take
    # cannot be empty
    title = models.CharField(max_length=200)

    # ta row in database for large text
    # null is parameter for if empty to create table
    # with blank we can add this without text else it cannot submit
    description = models.TextField(null=True, blank=True)

    # here we pass a link to database if we want
    # null = true allow vallue to be in database
    # blank = True allow to submit form
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
