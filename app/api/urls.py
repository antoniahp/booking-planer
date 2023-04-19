from ninja import NinjaAPI
from core.models import  BookingModel, RoomModel, PlaceModel, CityModel, CountryModel, ContinentModel
from ninja import Schema
from datetime import date
from django.db.models import Q

api = NinjaAPI(title="Traveling API", version="1.0.0")

@api.get("/booking")
def get_bookings(request):
    results = []
    for booking in BookingModel.objects.filter():
        results.append({
        "name": booking.room.name,
        "room": booking.room.id,
        "check_in": booking.check_in,
        "check_out": booking.check_out,
        "total_price": booking.total_price,
        "total_guests": booking.total_guests,
        "entitled_guest_name": booking.entitled_guest_name,
        "entitled_guest_surname": booking.entitled_guest_surname,
        "phone": booking.phone,
        "email": booking.email,

        })
    return {"get_bookings": results}


class BookingSchema(Schema):
    name: str
    room: int
    check_in: date
    check_out: date
    total_price: int
    total_guests: int
    entitled_guest_name: str
    entitled_guest_surname: str
    phone: int
    email: str


@api.post("/booking")
def post_bookings(request, booking: BookingSchema):
    db_booking, created = BookingModel.objects.get_or_create(
        name=booking.name, room=booking.room, check_in=booking.check_in, check_out=booking.check_out, total_price=booking.total_price, 
        total_guests=booking.total_guests, entitled_guest_name=booking.entitled_guest_name, entitled_guest_surname=booking.entitled_guest_surname, 
        phone=booking.phone, email=booking.email
    )
    return {
        "booking": {
            "name": db_booking.name,
            "id": db_booking.id,
            "room": db_booking.room,
            "check_in":db_booking.check_in,
            "check_out":db_booking.check_out,
            "total_price":db_booking.total_price,
            "total_guests":db_booking.total_guests,
            "entitled_guest_name":db_booking.entitled_guest_name,
            "entitled_guest_surname":db_booking.entitled_guest_surname,
            "phone":db_booking.phone,
            "email":db_booking.email,

        }
    }


@api.get("/room")
def get_rooms(request):
    results = []
    for room in RoomModel.objects.filter():
        results.append({
        "name": room.name,
        "place": room.place.name,
        "picture": room.picture.url,
        "description": room.description,
        "beds": room.beds,
        "price": room.price,
        "total_rooms": room.total_rooms,


        })
    return {"get_rooms": results}


class RoomSchema(Schema):
    name: str
    place: str
    picture: str
    description: str
    beds: int
    price: int
    total_rooms: int


@api.post("/room")
def post_rooms(request, room: RoomSchema):
    db_room, created = RoomModel.objects.get_or_create(
        name=room.name, place=room.place.name, picture=room.picture, description=room.description, beds=room.beds, price=room.price,
        total_rooms=room.total_rooms
        )
    return {
        "room": {
            "name":db_room.name,
            "place": db_room.place.name,
            "picture": db_room.picture.url,
            "description": db_room.description,
            "beds": db_room.beds,
            "price": db_room.price,
            "total_rooms": db_room.total_rooms,
        }
    }


@api.get("/place")
def get_places(request):
    results = []
    for place in PlaceModel.objects.filter():
        results.append({
        "name": place.name,
        "picture": place.picture.url,
        "description": place.description,
        "address": place.address,
        "price": place.price,
        "category": place.category,
        "stars": place.stars,
        "city": place.city.name,
        })
        
    return {"get_places": results}


class PlaceSchema(Schema):
    name: str
    picture: str
    description: str
    address: str
    price: int
    category: str
    stars: int
    city: str


@api.post("/place")
def post_places(request, place: PlaceSchema):
    db_place, created = PlaceModel.objects.get_or_create(
        name=place.name, picture=place.picture, description=place.description, address=place.address, price=place.price, 
        category=place.category, stars=place.stars, city=place.city
    )
    return {
        "place": {
            "name":db_place.name,
            "picture":db_place.picture,
            "description":db_place.description,
            "address":db_place.address,
            "price":db_place.price,
            "category":db_place.category,
            "stars":db_place.stars,
            "city":db_place.city,

        }
    }


@api.get("/city")
def get_cities(request):
    results = []
    for city in CityModel.objects.filter():
        results.append({
            "name": city.name,
            "country": city.country.name
        })
    return {"get_cities": results}


class CitySchema(Schema):
    name: str
    country: str


@api.post("/city")
def post_cities(request, city: CitySchema):
    db_city, created = CityModel.objects.get_or_create(
        name=city.name, country=city.country
    )
    return{
        "city":{
            "name":db_city.name,
            "country":db_city.country
        }
    }


@api.get("/country")
def get_countries(request):
    results = []
    for country in CountryModel.objects.filter():
        results.append({
            "name": country.name,
            "continent": country.continent.name
        })
    return {"get_countries": results}


class CounrySchema(Schema):
    name: str
    country: str


@api.post("/country")
def post_countries(request, country: CounrySchema):
    db_country, created = CountryModel.objects.get_or_create(
        name=country.name, continent=country.continent
    )
    return{
        "country":{
            "name":db_country.name,
            "continent":db_country.continent
        }
    }


@api.get("/continent")
def get_continent(request):
    results = []
    for continent in ContinentModel.objects.filter():
        results.append({
            "name": continent.name,
        })
    return {"get_continent": results}


class ContinentSchema(Schema):
    name: str


@api.post("/continent")
def post_continent(request, continent: ContinentSchema):
    db_continent, created = ContinentModel.objects.get_or_create(name=continent.name)
    return{
        "continent":{
            "name":db_continent.name,
        }
    }


