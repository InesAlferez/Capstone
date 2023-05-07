from django.shortcuts import render, redirect
from .models import AuthUser
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = AuthUser(
                password=form.cleaned_data['password'],
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['name'].split()[0],
                last_name=form.cleaned_data['name'].split()[1],
                pet_name=form.cleaned_data['pet_name'],                                
                email=form.cleaned_data['email'],
                is_staff=False
            )
            user.save()
            return redirect('PatientHomePage/patienthome/')
    else: 
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

