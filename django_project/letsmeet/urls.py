from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="all-meetups"), # our-domain.com/letsmeet/
    path("<slug:letsmeet_slug>/success", views.confirm_registration, name = "confirm-registration"),
    path("<slug:letsmeet_slug>", views.meetup_details, name="meetup_detail") #our-domain.com/letsmeet/<dynamic-path-segment>
]