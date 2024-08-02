from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AppointmentForm

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})


def appointment_success(request):
    return render(request, 'appointment_success.html')
