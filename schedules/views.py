from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Schedule, Comment
from .forms import ScheduleForm, GuestCommentForm, UserCommentForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def index(request):
    schedules = Schedule.objects.order_by('-pk')
    context = {
        'schedules': schedules,
    }
    return render(request, 'schedules/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('schedules:detail', schedule.pk)
    else:
        form = ScheduleForm()
    context = {
        'form': form
    }
    return render(request, 'schedules/form.html', context)

def detail(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    if request.user.is_authenticated:
        form = UserCommentForm()
    else:
        form = GuestCommentForm()
    context = {
        'schedule': schedule,
        'form' : form,
    }
    return render(request, 'schedules/detail.html', context)

@require_POST
def comment_create(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk=schedule_pk)
    if request.user.is_authenticated:
        form = UserCommentForm(request.POST)
    else:
        form = GuestCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.schedule = schedule
        if request.user.is_authenticated:
            comment.user = request.user
            comment.nickname = request.user.username
            comment.password = request.user.password
        else:
            comment.user = get_object_or_404(User, pk=2)

        comment.save()
        return redirect('schedules:detail', schedule.pk)
    else:
        return redirect('schedules:index', schedule.pk)