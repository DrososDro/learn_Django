from django.forms import ModelForm
from .models import Project





class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' # this shows all the fields
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
