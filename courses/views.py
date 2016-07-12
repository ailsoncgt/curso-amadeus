# coding=utf-8

from django.shortcuts import render, get_object_or_404

from .models import Course


def index(request):
    context = {
        'courses': Course.objects.filter(is_approved=True)
    }
    return render(request, 'courses/index.html', context)


def course(request, slug):
    context = {}
    course = get_object_or_404(Course, slug=slug)
    context['course'] = course
    return render(request, 'courses/course.html', context)
