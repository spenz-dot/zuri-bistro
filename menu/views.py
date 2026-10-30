from django.db.models import Prefetch
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Category, MenuItem


def menu_page(request):
    available = MenuItem.objects.filter(available=True)
    categories = Category.objects.prefetch_related(
        Prefetch("menuitem_set", queryset=available, to_attr="items")
    )
    return render(request, "menu/menu.html", {"categories": categories})


def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/reserve/?sent=1")
    else:
        form = ReservationForm()
    return render(request, "menu/reserve.html", {"form": form})


def home(request):
    return render(request, "menu/home.html")
