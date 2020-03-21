from django import forms
from django.utils.encoding import force_text

from django_select2.forms import (
  HeavySelect2Widget, HeavySelect2MultipleWidget, ModelSelect2Widget,
  ModelSelect2MultipleWidget, ModelSelect2TagWidget, Select2Widget,
  Select2MultipleWidget
)

from music import models
from music.models import Country, City, Artist, Grene, Groupie, Album 


class TitleSerchFieldMixin:
    search_fields = [
        'title_icontains',
        'pk_startswith'
    ]

class TitleModelSelect2Widget( TitleSerchFieldMixin, ModelSelect2Widget):
    pass

class TitleModelSelect2MultipleWidget (TitleSerchFieldMixin, ModelSelect2MultipleWidget):
    pass

class GreneSelect2TagWidget( TitleSerchFieldMixin, ModelSelect2TagWidget):
    model = models.Grene

    def create_value (self, value):
        self.get_queryset().create(title=value)

class ArtistCustomTitleWidget(ModelSelect2Widget):
    model = models.Artist
    search_fields = [
        'title_icontains'
    ]

    def label_from_instace( self, obj):
        return force_text(obj.title).upper()

class GreneCustomTitleWidget(ModelSelect2Widget):
    model = models.Grene
    search_fields = [
        'title_icontains'
    ]

    def label_from_instace( self, obj):
        return force_text(obj.title).upper()

class AlbumSelect2WidgetForm( forms.ModelForm):
    class Meta:
        model = models.Album
        fields = (
            'artist',
            'primary_grene'
        )
        widget = {
            'artist': Select2Widget,
            'primary_grene': Select2Widget,
        }

class AlbumSelect2MultipleWidgetForm( forms.ModelForm):
    class Meta:
        model = models.Album
        fields = (
            'artist',
            'featured_artist'
        )
        widget = {
            'artist': Select2MultipleWidget,
            'featured_artist': Select2MultipleWidget,
        }

class AlbumModelSelect2WidgetForm( forms.ModelForm):
    class Meta:
        model = models.Album
        fields = (
            'artist',
            'primary_grene'
        )
        widget = {
            'artist': ArtistCustomTitleWidget,
            'primary_grene': GreneCustomTitleWidget,
        }

    def __init__(self, *args, **kwargs):
        super(AlbumModelSelect2WidgetForm, self).__init__(*args, **kwargs)
        self.fields['primary_grene'].initial=2

class AlbumModelSelect2MultipleWidgetRequiredForm( forms.ModelForm):
    class Meta:
        model = models.Album
        fields = (
            'artist',
            'featured_artist'
        )
        widget = {
            'artist': TitleModelSelect2MultipleWidget,
            'featured_artist': TitleModelSelect2MultipleWidget,
        }

class AlbumModelSelect2MultipleWidgetForm( forms.ModelForm):
    title = forms.CharField( max_length=50)
    grenes = forms.ModelMultipleChoiceField(widget=ModelSelect2MultipleWidget(
        queryset= models.Grene.objects.all(),
        search_fields= ['title_icontains'],
    ), queryset= models.Grene.objects.all(), required=True)

    featured_artist = forms.ModelMultipleChoiceField(widget=ModelSelect2MultipleWidget(
        queryset= models.Artist.objects.all(),
        search_fields= ['title_icontains'],
    ), queryset= models.Artist.objects.all(), required=False)  

NUMBER_CHOICE = [
     (1,'One'),
     (2, 'Two'),
     (3, 'Three'),
     (4, 'Four'),
 ]

class Select2WidgetForm( forms.Form):
    number = forms.ChoiceField(widget=Select2Widget, choices=NUMBER_CHOICE, required=False)

class HeavySelect2WidgetForm (forms.Form):
    artist = forms.ChoiceField( widget=HeavySelect2Widget(data_view='heavy_data_1'), choices=NUMBER_CHOICE)
    primary_grene = forms.ChoiceField( widget=HeavySelect2Widget(data_view='heavy_data_1'), choices=NUMBER_CHOICE, required=False)

class HeavySelect2MultipleWidgetForm ( forms.Form):
    title = forms.CharField(max_length=50)
    grene = forms.MultipleChoiceField( widget=HeavySelect2MultipleWidget(data_view='heavy_data_1', choices=NUMBER_CHOICE, attrs={'data-minimum-length': 0},),
        choices=NUMBER_CHOICE )
    featured_artist = forms.MultipleChoiceField( widget=HeavySelect2MultipleWidget(data_view='heavy_data_2', choices=NUMBER_CHOICE, attrs={'data-minimum-length': 0},),
        choices=NUMBER_CHOICE, required=False )
    
    def clean_title(self):
        if len(self.cleaned_data['title'])< 3:
            raise forms.ValidationError('Title Must Have More than 3 Character.')
        return self.clean_data['title']

class ModelSelect2TagWidgetForm ( forms.ModelForm):
    class Meta:
        model = Album
        fields = ['grene']
        widget = {
            'grene' : GreneSelect2TagWidget
        }
        
class AddressChainedSelect2WigdetForm( forms.Form):
    country = forms.ModelChoiceField( 
        queryset=Country.objects.all(),
        label = 'Country',
        widget=ModelSelect2Widget(
            search_fields = ['name_icontains'],
            max_result = 500,
            dependent_fields = { 'city': 'cities'},
            attrs = { 'data-minimum-input-length': 0},
        ) )

    city = forms.ModelChoiceField( 
        queryset=City.objects.all(),
        label = 'City',
        widget= ModelSelect2Widget(
            search_fields = ['name_icontains'],
            max_result = 500,
            dependent_fields = { 'country': 'country'},
            attrs = { 'data-minimum-input-length': 0},
        ) )

    city = forms.ModelChoiceField( queryset=City.objects.all(),
        label = 'City not Interdependent',
        widget= ModelSelect2Widget(
            search_fields = ['name_icontains'],
            max_result = 500,
            dependent_fields = { 'country': 'country'},
            attrs = { 'data-minimum-input-length': 0},
        ) )

class GroupieForm ( forms.ModelForm):
    class Meta:
        model = models.Groupie
        fields ='__all__'
        widgets = {
            'obsession': ArtistCustomTitleWidget
        }