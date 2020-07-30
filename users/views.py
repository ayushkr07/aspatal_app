from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
import string
import random
from django.contrib import messages

def register(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            user=form.save()
            f_name=user.first_name
            l_name=user.last_name
            name=f_name+' '+l_name
            UserProfile.objects.create(name=name,user=user)
            messages.success(request,f'Account created for {f_name}')
            return redirect('aspatal_app:home')
    else:
        form = UserCreateForm()
    return render(request,'users/register.html',{'form':form})

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required(login_url='/login/')
def CreateUserProfile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            password = User.objects.make_random_password()
            username = profile.name.split()[0] + id_generator()
            user = User.objects.create(username=username, registeras="P")
            user.set_password(password)
            user.save_base(raw=True)
            profile.user = user
            profile.save()
            return redirect('aspatal_app:r_dashboard')
    form = ProfileUpdateForm()
    return render(request, 'users/profile_create.html', {'form': form})


@login_required(login_url='/login/')
def UpdatedUserProfile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'user':user})


@login_required(login_url='/login/')
def UpdatedUserProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('aspatal_app:r_dashboard')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'user':user})


@login_required(login_url='/login/')
def UpdatedDocProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('aspatal_app:hr_dashboard')
    else:
        form = DoctorProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form, 'user':user})


@login_required(login_url='/login/')
def DeleteUserProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        user.delete()
        return redirect('aspatal_app:r_dashboard')
    else:
        return render(request, 'users/profile_delete.html', {'user':user})


@login_required(login_url='/login/')
def DeleteDocProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        user.delete()
        return redirect('aspatal_app:hr_dashboard')
    else:
        return render(request, 'user_profile/profile_doc_delete.html', {'user':user})