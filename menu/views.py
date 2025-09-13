
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem, Category, Reservation

# Home page view
def home_view(request):
    featured = MenuItem.objects.all()[:3]  # Pick first 3 as featured
    return render(request, 'menu/home.html', {'featured': featured})

# Menu page view
def menu_view(request):
    menu_items = MenuItem.objects.select_related('category').all()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})

# About page view
def about_view(request):
    return render(request, 'menu/about.html')

# Contact page view
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        from .models import ContactMessage
        ContactMessage.objects.create(name=name, email=email, message=message_text)
        messages.success(request, f'Thank you, {name}! Your message has been received.')
        return redirect('contact')
    return render(request, 'menu/contact.html')

def book_table_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            message=message
        )
        messages.success(request, f'Thank you, {name}! Your table has been reserved. We look forward to welcoming you!')
        return redirect('book_table')
    return render(request, 'menu/book_table.html')
