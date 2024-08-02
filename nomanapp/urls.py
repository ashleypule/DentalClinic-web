from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from nomanapp.views import home, contact, about, price, service, team, signup, contact_view, chatbot
from appointments.views import appointment, appointment_success
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView)

urlpatterns = [
   path('', home, name='home'),
   path('contact.html', contact, name='contact'),
   path('contact/', contact_view, name='contact'),
   path('about.html', about, name='about'),
   path('price.html', price, name='price'),
   path('service.html', service, name='service'),
   path('team.html', team, name='team'),
   path('signup/', signup, name='signup'),
   path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('book/', appointment, name='appointment'),
   path('success/', appointment_success, name='appointment_success'),
   path('chatbot.html/', chatbot, name='chatbot'),

   #Reset password urls
   path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
