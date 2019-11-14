from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm


def index(request):
    return(render(request))


def rejestruj(request):
    if request.method == 'POST':
        pass
    else:
        form=UserCreationForm()
        kontekst = {'form': form}
    return(render(request, 'users/register.html', kontekst))
