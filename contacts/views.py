from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ContactMessage


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(
            request,
            "Votre message a bien été envoyé. Merci pour votre contact !"
        )

        return redirect("/#contact")

    return redirect("/#contact")