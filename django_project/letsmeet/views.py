from django.shortcuts import render, redirect

from .models import meetups, Participant

from .forms import RegistrationForm

# Create your views here.
def index(request):
    letsmeet = meetups.objects.all()
    return render(request, "letsmeet/index.html", {
        "letsmeet": letsmeet
    })
    
    
def meetup_details(request, letsmeet_slug):
    try:
        selected_meetup = meetups.objects.get(slug=letsmeet_slug)

        
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data["email"]
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect("confirm-registration", letsmeet_slug = letsmeet_slug)
                
        return render(request, "letsmeet/meetup-details.html", {
                "meetup_found": True,
                "meetup": selected_meetup,
                "form": registration_form
            })
                    
    except Exception as exc:
        return render(request, "letsmeet/meetup-details.html", {
        "meetup_found": False
        })
        
def confirm_registration(request, letsmeet_slug):
    meetup = meetups.objects.get(slug = letsmeet_slug)
    return render(request, "letsmeet/registration-success.html", {
        "organizer_email": meetup.organizer_email
    })
          
    
