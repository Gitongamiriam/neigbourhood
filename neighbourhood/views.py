from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Neighbourhood,Posts,Business
from django.contrib.auth.decorators import login_required
from .forms import NewMessageForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts=Posts.show_posts()
    return render(request, 'home.html',{'posts':posts})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"business": searched_business})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_message(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewMessageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = current_user
            post.save()
        return redirect('home')
    else:
        form = NewMessageForm()
    return render(request, 'new_message.html', {"form": form})

  