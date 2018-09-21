from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from . import models


def user_list(request):
    all_users = models.DjangoUser.objects.all()
    paginator = Paginator(all_users, 10)

    page = request.GET.get('page', 1)
    users = paginator.get_page(page)
    return render(request, 'contents/user_list.html', {'users': users})


def company_list(request):
    all_companies = models.Company.objects.all()
    paginator = Paginator(all_companies, 10)

    page = request.GET.get('page', 1)
    companies = paginator.get_page(page)
    return render(request, 'contents/company_list.html', {'companies': companies})


def community_list(request):
    all_communities = models.Community.objects.all()
    paginator = Paginator(all_communities, 10)

    page = request.GET.get('page', 1)
    communities = paginator.get_page(page)
    return render(request, 'contents/community_list.html', {'communities': communities})


def project_list(request):
    all_projects = models.Project.objects.all()
    paginator = Paginator(all_projects, 10)

    page = request.GET.get('page', 1)
    projects = paginator.get_page(page)
    return render(request, 'contents/project_list.html', {'projects': projects})


def blog_list(request):
    all_blogs = models.Blog.objects.all()
    paginator = Paginator(all_blogs, 10)

    page = request.GET.get('page', 1)
    blogs = paginator.get_page(page)
    return render(request, 'contents/blog_list.html', {'blogs': blogs})
