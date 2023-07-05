from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import UserCreationForm
from .forms import LoginForm
from .forms import QandaForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            student_id = form.cleaned_data.get('student_id')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(student_id=student_id, password=raw_password)
            login(request, user)

            return redirect('main')
        
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def log_out(request):
    logout(request)
    
    return redirect(reverse("main"))

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("main")
    
    def form_valid(self, form):
        student_id = form.cleaned_data.get('student_id')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, student_id=student_id, password=password)
        
        if user is not None:
            login(self.request, user)
            
        return super().form_valid(form)

def QandaView(request):
    if request.method =='POST':
        form = QandaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QandaForm()
    return render(request, 'qanda.html', {'form':form})
