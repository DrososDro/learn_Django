import uuid

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

    # a link for source code
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    # this give us tha date and the time field
    # when we create this give us the stamp of the created
    create = models.DateTimeField(auto_now_add=True)

    # when django add to the database create an int id form 0
    # we dont want this we better add a 16char id witch is unique and we dont
    # have conflicts
    id = models.UUIDField(defalt=uuid.uuid4, unique=True, primary_key=True)
