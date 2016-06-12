from django.shortcuts import render

from user_manage.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def userlist(request):
    userlist = User.objects.all()
    return render(request, 'userlist.html', {'userlist' : userlist})
