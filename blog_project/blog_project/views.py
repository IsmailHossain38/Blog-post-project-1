from django.shortcuts import render

from Posts.models import Posts
def home(req):
    data = Posts.objects.all()
    return render(req, 'home.html' ,{"Data": data})