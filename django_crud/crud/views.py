from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    return render(request, "home.html", {})

def read(request):
    all_members = Member.objects.all()
    return render(request, "read.html", {'all': all_members})

def create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Form Has Been Submitted Successfully')
            return redirect('read')
        else:
            messages.error(request, 'There was an error in your form! Please try again.')

    form = MemberForm()
    return render(request, "create.html", {'form': form})

def update(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member updated successfully!')
            return redirect('read')
    else:
        form = MemberForm(instance=member)

    return render(request, "update.html", {'form': form, 'member': member})  # Pass member object

def delete(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.delete()
    messages.success(request, 'Member deleted successfully!')
    return redirect('read')