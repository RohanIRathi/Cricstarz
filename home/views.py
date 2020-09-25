from django.shortcuts import redirect, render
from .forms import CreateForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created!')
            return redirect('login')
        else:
            messages.error(request, f'Ther was an error in your form!')
            return render(request, 'registration/register.html', {'form':form})
    else:
        form = CreateForm()
        
        args = {'form': form}
        return render(request, 'registration/register.html', args)