from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import Profile


@login_required
def dashboard(request):
    register_date = request.user.date_joined
    messages.success(request, f"Hi, {request.user.username} You’ve been with us since: {register_date.strftime('%a %d %b %Y, %I:%M%p')}.")
    messages.warning(request, f"Last failed attempt to login is {request.user.profile.last_failed_attempt.strftime('%a %d %b %Y, %I:%M%p')}")
    return render(request, 'dashboard/dashboard.html', {'title': 'dashboard'})
