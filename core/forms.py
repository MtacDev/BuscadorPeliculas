from django.forms import ModelForm, Textarea
from .models import pelis, form2, form3

class pelisForm(ModelForm):
    class Meta:
        model = pelis
        fields = ['nom_peli']

class pelisform2(ModelForm):    
    class Meta:
        model = form2
        fields = '__all__'

class pelisform3(ModelForm): 
    class Meta:
        model = form3
        fields = '__all__'  