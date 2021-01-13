from rest_framework.generics import ListAPIView, \
    RetrieveUpdateDestroyAPIView, \
    CreateAPIView
from rest_framework.permissions import AllowAny, \
    IsAuthenticated, \
    IsAdminUser

from apps.locations.models import City, Country

from .serializers import CitySerializer, \
    CountrySerializer


class CityListView(ListAPIView):
    """ Cities list api view """

    serializer_class = CitySerializer
    permission_classes = (AllowAny,)
    queryset = City.objects.all()


class CityCreateView(CreateAPIView):
    """ City create api view """

    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,
                          IsAdminUser)
    queryset = City.objects.all()


class CityRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """ City detail | update | delete api view """

    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,
                          IsAdminUser)
    queryset = City.objects.all()
    lookup_field = 'slug'


class CountryListView(ListAPIView):
    """ Countries list api view """

    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    queryset = Country.objects.all()


class CountryCreateView(CreateAPIView):
    """ City create api view """

    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,
                          IsAdminUser)
    queryset = Country.objects.all()


class CountryRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """ Country detail | update | delete api view """

    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated,
                          IsAdminUser)
    queryset = Country.objects.all()
    lookup_field = 'slug'
