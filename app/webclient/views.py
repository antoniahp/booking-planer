from django.shortcuts import render

def home(request):
    context = {}
    return render(request, "home.html", context)


def places_list(request):
    context = {}
    return render(request, "places_list.html", context)


def base(request):
    context = {}
    return render(request, "base.html", context)

def place(request):
    context = {}
    return render(request, "place.html", context)


def pay_page(request):
    if request.method == "POST":
        print(request.POST.get("address"))
    context = {}
    return render(request, "pay_page.html", context)
