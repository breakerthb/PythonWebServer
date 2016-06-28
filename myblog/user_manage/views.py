from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from user_manage.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def userlist(request):
    userlist = User.objects.all()
    return render(request, 'userlist.html', {'userlist' : userlist})
    
from forms import LoginForm

def userdel(request):
    id1 = request.GET.get('id', 0)
    
    User.objects.get(id = id1).delete()
    return HttpResponse("Delete success...")
    
def useradd(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            name1 = form.cleaned_data['name']
            pw1 = form.cleaned_data['pw']
            User.objects.create(name=name1, pw=pw1)
            HttpResponse('<script>alert("Add Succeed");history.back();</script>')
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm()
    return render(request, 'useradd.html', {'form': form})
  
def usersearch(request):
    return render(request, 'usersearch.html')
    
def searchret(request):
    name1 = request.GET.get('name', '')
    userlist = User.objects.filter(name = name1)
    return render(request, 'userlist.html', {'userlist' : userlist, 'title': 'Search Result'})
    
    

