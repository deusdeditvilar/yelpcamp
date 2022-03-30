from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse


class AddCampground(LoginRequiredMixin, FormView):
    template_name = 'campgrounds/add.html'
    form_class = CampgroundForm
    success_url = '/home/'
    login_url = '/login/'

    def form_valid(self, form):
        form.save(commit=False)
        user = self.request.user
        form.instance.user_id = user.id
        form.save()
        return super().form_valid(form)

def campground(request,pk):
    camp = get_object_or_404(Campground,pk=pk)
    comments = Comment.objects.filter(campground_id=pk).order_by("-id")[:3]
    return render(request, 'campgrounds/individual.html', {"camp": camp,'comments':comments})


@login_required
def comment(request,pk):
    camp = get_object_or_404(Campground,pk=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.instance
            comment.campground = camp
            comment.user = user
            comment.created_at = timezone.now()
            form.save()
            return HttpResponseRedirect('/campgrounds/individual/'+str(pk))
        else:
            return render(request,'campgrounds/comment.html',{'form':form})
    form = CommentForm()
    return render(request,'campgrounds/comment.html',{'form':form})