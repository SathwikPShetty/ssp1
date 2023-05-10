from django.shortcuts import render, HttpResponse
from datetime import datetime
from team.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context={
    #     'variable':"THIS IS SENT"
    # }
    return render(request,'index.html');
def team(request):
    return render(request,'team.html');

def profile_submit(request):
    if request.method == 'POST':
        form_data = request.POST
        profile = Profile(
            first_name=form_data['first_name'],
            middle_name=form_data['middle_name'],
            last_name=form_data['last_name'],
            linkedin=form_data['linkedin'],
            instagram=form_data['instagram'],
            github=form_data['github'],
            profile_pic=request.FILES.get('profile_pic')
        )
        profile.save()
        return redirect('profile_success')  # Redirect to a success page

    return render(request, 'profile_form.html')
