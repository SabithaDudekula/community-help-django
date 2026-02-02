from django.shortcuts import render, redirect
from .models import HelpRequest
from .forms import HelpRequestForm, CustomRegisterForm

from django.contrib.auth.decorators import login_required


# Home Page - Show All Requests
def help_request_list(request):

    requests = HelpRequest.objects.all()

    return render(request, 'help_requests/help_request_list.html', {
        'requests': requests
    })


# Add New Help Request (Login Required)
@login_required
def add_help_request(request):

    if request.method == 'POST':

        form = HelpRequestForm(request.POST)

        if form.is_valid():

            # Don't save to DB yet
            help_req = form.save(commit=False)

            # Assign current user as owner
            help_req.user = request.user

            # Now save to DB
            help_req.save()

            return redirect('/')

    else:
        form = HelpRequestForm()

    return render(request, 'help_requests/add_help_request.html', {
        'form': form
    })


# User Registration
def register(request):

    if request.method == 'POST':

        form = CustomRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')

    else:
        form = CustomRegisterForm()

    return render(request, 'help_requests/register.html', {
        'form': form
    })

# Take a Help Request (I Can Help)
@login_required
def take_help_request(request, pk):

    help_req = HelpRequest.objects.get(id=pk)

    # Prevent self-help and only open requests
    if help_req.user != request.user and help_req.status == 'Open':

        help_req.helper = request.user
        help_req.status = 'In Progress'
        help_req.save()

    return redirect('/')


# Mark Request as Resolved
@login_required
def resolve_request(request, pk):

    help_req = HelpRequest.objects.get(id=pk)

    # Only owner can resolve
    if help_req.user == request.user and help_req.status == 'In Progress':

        help_req.status = 'Resolved'
        help_req.save()

    return redirect('/')


# User Dashboard
@login_required
def dashboard(request):

    my_requests = HelpRequest.objects.filter(user=request.user)

    helping_requests = HelpRequest.objects.filter(helper=request.user)

    resolved_requests = HelpRequest.objects.filter(
        user=request.user,
        status='Resolved'
    )

    return render(request, 'help_requests/dashboard.html', {
        'my_requests': my_requests,
        'helping_requests': helping_requests,
        'resolved_requests': resolved_requests,
    })
