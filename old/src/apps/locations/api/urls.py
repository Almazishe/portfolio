from django.urls import path

from . import views

# API's obtaining locations(Cities, Countries) functionalities | '/api/1.0.0/locations/<path>'
urlpatterns = [
    path('cities/list', views.CityListView.as_view(), name='city-list'),
    path('cities/create', views.CityCreateView.as_view(), name='city-create'),
    path('city/<slug>', views.CityRetrieveUpdateDeleteView.as_view(), name='city-rud'),
    path('countries/list', views.CountryListView.as_view(), name='country-list'),
    path('countries/create', views.CountryCreateView.as_view(), name='country-create'),
    path('country/<slug>', views.CountryRetrieveUpdateDeleteView.as_view(), name='country-rud'),
]
