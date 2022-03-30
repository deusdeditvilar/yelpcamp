from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from campgrounds.models import Campground
from campgrounds.filters import CampgroundFilter


def landing(request):
    return render(request,'dashboard/landing.html')

def home(request):
    if request.GET:

        filters = request.GET.copy()
        queryset = Campground.objects.all()

        filtro = CampgroundFilter(filters, queryset=queryset)
    filtro = CampgroundFilter(request.GET, queryset=Campground.objects.all())

    return render(request, 'dashboard/home.html', {'filter': filtro,'camps':filtro.qs})


class SignUpView(FormView):
    template_name = 'account/auth.html'
    form_class = SignUpForm
    success_url = '/home/'

    def form_valid(self, form):     
        self.object = form.save(commit=False)
        form.instance.user = self.request.user
        self.object.save()
        user = self.object
        login(self.request, user)
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context.update({'login': False, 'btntext': 'Create an account'})
        return context

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account:home'))
        data = { 'form': LoginForm(),'login': True, 'btntext': 'Login' }
        return render(request, 'account/auth.html', data)
    
    def post(self, request):
        form = LoginForm(data=request.POST)
        next = request.GET.get("next")
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password and authenticate(username=username, password=password):
                user = User.objects.get(Q(username__iexact=username))
                login(request, user)
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse('account:home'))
        
        data = { 
            'form': form,
            'error': 'Username or Password incorrect',
            'login': True, 
            'btntext': 'Login'
        }
        return render(request, 'account/auth.html', data)