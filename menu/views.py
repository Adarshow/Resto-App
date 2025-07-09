import json
from pathlib import Path
from django.shortcuts import render, redirect
from django.contrib import messages

# Helper to load menu data from JSON file
def load_menu_data():
    file_path = Path(__file__).resolve().parent / 'static/menu/menu.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Home page view
def home_view(request):
    menu_items = load_menu_data()
    featured = menu_items[:3]  # Pick first 3 as featured
    return render(request, 'menu/home.html', {'featured': featured})

# Menu page view
def menu_view(request):
    menu_items = load_menu_data()
    # Standardize category names
    for item in menu_items:
        if 'category' in item and isinstance(item['category'], str):
            item['category'] = item['category'].strip().capitalize()
    return render(request, 'menu/menu.html', {'menu_items': menu_items})

# About page view
def about_view(request):
    return render(request, 'menu/about.html')

# Contact page view
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Simulate processing: log to messages framework
        messages.success(request, f'Thank you, {name}! Your message has been received.')
        # Optionally print to console: print(name, email, message)
        return redirect('contact')
    return render(request, 'menu/contact.html')

def book_table_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # You can process/store the booking here if needed
        messages.success(request, f'Thank you, {name}! Your table has been reserved. We look forward to welcoming you!')
        return redirect('book_table')
    return render(request, 'menu/book_table.html')
