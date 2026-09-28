from django.contrib import admin
from django.urls import path

from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import StaticViewSitemap

from .views import home, robots_txt
from contacts.views import contact


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [

    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("contact/", contact, name="contact"),

    path("robots.txt", robots_txt, name="robots_txt"),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),
]