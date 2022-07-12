import uuid

from django.db import models

# Create your models here.


class Project(models.Model):

    # when django add to the database create an int id form 0
    # we dont want this we better add a 16char id witch is unique and we dont
    # have conflicts
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    # we tell tha this is a table

    # title = character field max lenth is parameter
    # for how chars can take
    # cannot be empty
    title = models.CharField(max_length=200)

    # ta row in database for large text
    # null is parameter for if empty to create table add null to have the table
    # with blank we can add this without text else it cannot submit
    description = models.TextField(null=True, blank=True)

    # here we pass a link to database if we want
    # null = true allow vallue to be in database
    # blank = True allow to submit form if field is empty
    demo_link = models.CharField(max_length=2000, null=True, blank=True)

    # a link for source code
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # here we create a field for votes shome is positive and some negative
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    # here we set an IntegerField  and default count = 0
    vote_count = models.IntegerField(default=0, null=True, blank=True)

    # ManyToManyField this is for many to many relashionship
    # here we store our tags
    tags = models.ManyToManyField("Tag", blank=True)

    # this give us tha date and the time field
    # when we create this give us the stamp of the created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (("up", "Up Vote"), ("down", "Down Vote"))
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    # SET_NULL = the Reviews will set to null if delete else CASCADE will
    # delete eurything
    # here this is one to one relashionship
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # owner =
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
