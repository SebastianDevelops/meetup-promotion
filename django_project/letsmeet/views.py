from django.shortcuts import render

from .models import meetups

# Create your views here.
def index(request):
    letsmeet = meetups.objects.all()
    return render(request, "letsmeet/index.html", {
        "letsmeet": letsmeet
    })
    
    
def meetup_details(request, letsmeet_slug):
    try:
        selected_meetup = meetups.objects.get(slug=letsmeet_slug)
        return render(request, "letsmeet/meetup-details.html", {
            "meetup_found": True,
            "meetup": selected_meetup
        })
    except Exception as exc:
        return render(request, "letsmeet/meetup-details.html", {
            "meetup_found": False
        })
          
    
