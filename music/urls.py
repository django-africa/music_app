from django.urls import include, path
from music.forms import (
    AddressChainedSelect2WigdetForm,AlbumSelect2WidgetForm,
    HeavySelect2MultipleWidgetForm, HeavySelect2WidgetForm,
    ModelSelect2TagWidget, Select2WidgetForm 
)

from music.views import TemplateView, heavy_data_1, heavy_data_2

urlpatterns = [
    path('select2_widget', TemplateView.as_view(form_class=Select2WidgetForm, success_url='/'), name='select2_widget'),
    path('heavy_select2_widget', TemplateView.as_view(form_class=HeavySelect2WidgetForm, success_url='/'), name='heavy_select2_widget'),
    path('heavy_select2_multiple_widget', TemplateView.as_view(form_class=HeavySelect2MultipleWidgetForm, success_url='/'), name='heavy_select2_multiple_widget'),
    path('model_select2_widget', TemplateView.as_view(form_class=AlbumSelect2WidgetForm, success_url='/'), name='model_select2_widget'),
    path('model_select2_tag_widget', TemplateView.as_view(form_class=ModelSelect2TagWidget, success_url='/'), name='model_select2_tag_widget'),
    path('model_select2_chained_widget', TemplateView.as_view(form_class=AddressChainedSelect2WigdetForm, success_url='/'), name='address_chained_select2_widget'),
    path('heavy_data_1', heavy_data_1, name='heavy_data_1'),
    path('heavy_data_2', heavy_data_2, name='heavy_data_2')
]


