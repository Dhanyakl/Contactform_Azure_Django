from django.shortcuts import render,redirect
from .forms import Contactforms


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Contactforms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Contactforms()

    return render(request, 'index.html', {'form': form})
