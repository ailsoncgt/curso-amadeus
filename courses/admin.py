# coding=utf-8

from django.contrib import admin

from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'is_approved']
    search_fields = ['name', 'slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
