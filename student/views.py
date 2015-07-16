from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render


@login_required(login_url='/accounts/login/')
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("success")
        else:
            # Return a 'disabled account' error message
            return HttpResponse("fail")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("invalid")
        
def profile(request):
	return render(request,"templates/profile.html")
	
def logout_view(request):
	logout(request)
	return redirect('/messages/')
