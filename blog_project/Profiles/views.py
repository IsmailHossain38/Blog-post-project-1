from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profiles(request):
    if request.method == 'POST':
        profile_forms = forms.Profileform(request.POST)
        if profile_forms.is_valid():
            profile_forms.save()
            return redirect('add_author')
    else:
        profile_forms = forms.Profileform()
        
    return render(request,'add_profiles.html' , {'form':profile_forms})