from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact

# show all contact
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

# add contact in user
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

# edit contact in user
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'add_contact.html', {'form': form})


# delete contact in user
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})


# show contact in admin
def admin_Dashboard(request):
    contacts = Contact.objects.all()
    return render(request,'admin_home.html',{'contacts': contacts})

# add contact in admin
def admin_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('admin_dashboard')
    return render(request, 'contact_delete.html', {'contact': contact})


# edit contact in admin
def edit_admin(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'add_contact.html', {'form': form})

