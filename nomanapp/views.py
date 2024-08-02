from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'home.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def price(request):
    return render(request, 'price.html', {})

def service(request):
    return render(request, 'service.html', {})

def team(request):
    return render(request, 'team.html', {})

from . import forms
def contact_view(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(subject, message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, (email))
            return render(request, 'contact_success.html')
    return render(request, 'contact.html', {'form': form})


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_thank_you_email(user):
    subject = 'Thank You for Registering with DentCare'
    html_message = render_to_string('thank_you_registration.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = 'pule_baloyi@outlook.com'
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_thank_you_email(instance)

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from django.shortcuts import render

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


def chatbot(request):
    return render(request, 'chatbot.html',{})

