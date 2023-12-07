from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_cetagories(request): 
    if request.method == 'POST': # user post req koreche
        cetagories_form = forms.Cetagoriesform(request.POST) #user data ekhane joma hoyece
        if cetagories_form.is_valid():  #data gula valid kina check kortece
            cetagories_form.save()  # data valid tay save korece
            return redirect("add_cetagories") # sob thik thakle author er url e pathiye dibO
    else:
        cetagories_form = forms.Cetagoriesform() 
    return render(request, 'add_cetagories.html', {"form": cetagories_form})