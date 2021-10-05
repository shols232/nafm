from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main/home.html", {})


class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main/about.html", {})


class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "main/contact.html", {})
