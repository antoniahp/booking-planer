from django.shortcuts import render
import requests
from django.shortcuts import redirect
from django.urls import reverse

def home(request):
    if request.method == "POST":
        city_id = request.POST.get("city")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        print(request.POST)
        return redirect(reverse("city", kwargs={"city_id":city_id})+ f"?check_in={check_in}&check_out={check_out}")
    response = requests.get(url="http://localhost:8000/api/city")
    response.raise_for_status()

    cities = response.json()["cities"]
    context = {
        "cities": cities
        
    }
    return render(request, "home.html", context)


def places_list(request, city_id: int):
    check_in = request.GET.get("check_in")
    check_out = request.GET.get("check_out")
    response = requests.get(url=f"http://localhost:8000/api/availability/city/{city_id}?check_in={check_in}&check_out={check_out}")
    response.raise_for_status()

    context = {
        "places": response.json(),
        "check_in": check_in,
        "check_out": check_out,
        
    }
    return render(request, "places_list.html", context)


def base(request):
    context = {}
    return render(request, "base.html", context)

def place(request, place_id: int):
    check_in = request.GET.get("check_in")
    check_out = request.GET.get("check_out")
    response = requests.get(url=f"http://localhost:8000/api/availability/places/{place_id}?check_in={check_in}&check_out={check_out}")
    response.raise_for_status()

    rooms = response.json()["rooms"]
    place = response.json()["place"]

    context = {
        "rooms": rooms,
        "place": place,
        "stars": "⭐" * place["stars"],
        "check_in": check_in,
        "check_out": check_out,

    }
    return render(request, "place.html", context)


def pay_page(request, place_id: int):
    if request.method == "POST":
        place_id = request.POST.get("place")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        print(request.POST)
        return redirect(reverse("place", kwargs={"place_id":place_id})+ f"?check_in={check_in}&check_out={check_out}")

    response = requests.get(url="http://localhost:8000/api/booking")
    response.raise_for_status()
    bookings = response.json()["bookings"]

    context = {
        "bookings": bookings
    }
    return render(request, "pay_page.html", context)
