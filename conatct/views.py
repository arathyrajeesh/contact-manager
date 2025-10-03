from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import Contact


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('contact_list')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
        
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('login')




@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'home.html', {'contacts': contacts})


@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})


@login_required
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'add_contact.html', {'form': form})


@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})




@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('contact_list')
    contacts = Contact.objects.all()
    return render(request, 'admin_home.html', {'contacts': contacts})


@login_required
def edit_admin(request, pk):
    if not request.user.is_superuser:
        return redirect('contact_list')
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'add_contact.html', {'form': form})


@login_required
def admin_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('contact_list')
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_dashboard')
    return render(request, 'contact_delete.html', {'contact': contact})


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
