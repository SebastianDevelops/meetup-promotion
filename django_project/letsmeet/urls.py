from django.urls import path
from . import views

urlpatterns = [
    path("letsmeet/", views.index, name="all-meetups"), # our-domain.com/letsmeet/
    path("letsmeet/<slug:letsmeet_slug>", views.meetup_details, name="meetup_detail") #our-domain.com/letsmeet/<dynamic-path-segment>
]