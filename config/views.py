from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://boubacar-dev.onrender.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")