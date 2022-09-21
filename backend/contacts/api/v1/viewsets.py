from rest_framework import authentication
from contacts.models import Contacts
from .serializers import ContactsSerializer
from rest_framework import viewsets


class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Contacts.objects.all()
