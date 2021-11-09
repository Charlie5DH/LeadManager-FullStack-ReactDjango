from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Create our Lead viewset. This allows to create a complete CRUD
# without having to specify methods for the functionalities


class LeadViewSet(viewsets.ModelViewSet):

    # get all the leads
    queryset = Lead.objects.all()

    # first allow all
    permission_classes = [
        permissions.AllowAny
    ]

    # specify a serializer class
    serializer_class = LeadSerializer
