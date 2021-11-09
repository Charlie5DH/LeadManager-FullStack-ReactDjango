'''
We are not creating paths statically. We will import Routers
Resource routing allows you to quickly declare all of the common routes for a given resourceful controller. 
Instead of declaring separate routes for your index... a resourceful route declares them in a single line of code.
REST framework adds support for automatic URL routing to Django, 
and provides you with a simple, quick and consistent way of wiring your view logic to a set of URLs.
'''

from rest_framework import routers, urlpatterns
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

# router.urls will give us the urls that we registered for the endpoint
urlpatterns = router.urls
