from django.db.models import fields
from rest_framework import serializers
from leads.models import Lead

'''
What is serialization? What is a Django REST serializer?
Serialization is the act of transforming an object into another data format. 
After transforming an object we can save it to a file or send it through the network.

Why serialization is necessary? 
Think of a Django model: it's a Python class. How do you render a Python class to JSON in a browser? 
With a Django REST serializer!

A serializer works the other way around too: it converts JSON to objects. This way you can:

display Django models in a browser by converting them to JSON
make CRUD request with a JSON payload to the API
'''

# Now we are turning our Lead model into a serializer
# to manage it like Json data


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        #fields = ('id', 'name', 'email', 'message')
