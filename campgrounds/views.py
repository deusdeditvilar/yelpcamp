from django.shortcuts import render

# Create your views here.

def add(request):
    return render(request,'campgrounds/add.html')

def ind(request):
    return render(request,'campgrounds/individual.html')

def comment(request):
    return render(request,'campgrounds/comment.html')