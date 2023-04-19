from django.db import models
from datetime import date
from django.core.validators import  MaxValueValidator, MinValueValidator



class ContinentModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class CountryModel(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey("ContinentModel", on_delete=models.CASCADE, related_name="countries")

    def __str__(self) -> str:
        return f"{self.name}"

class CityModel(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey("CountryModel", on_delete=models.CASCADE, related_name="cities")

    def __str__(self) -> str:
        return f"{self.name}"

class PlaceCategoryChoices(models.TextChoices):
    HOTEL = "HOTEL"
    HOSTAL = "HOSTAL"
    APARTMENT = "APARTMENT"
    MOTEL = "MOTEL"


class PlaceModel(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    description = models.TextField()
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100, choices=PlaceCategoryChoices.choices)
    stars = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    city = models.ForeignKey("CityModel", on_delete=models.CASCADE, related_name="places")
    
    def __str__(self) -> str:
        return f"{self.name}"


class RoomModel(models.Model):
    name = models.CharField(max_length=100)
    place = models.ForeignKey("PlaceModel", on_delete=models.CASCADE, related_name="rooms")
    picture = models.ImageField()
    description = models.TextField()
    beds = models.IntegerField()
    price = models.IntegerField()
    total_rooms = models.IntegerField()
    

    def __str__(self) -> str:
        return f"{self.place.name} - {self.name}"


class BookingModel(models.Model):
    room = models.ForeignKey("RoomModel", on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.IntegerField()
    total_guests = models.IntegerField()  
    entitled_guest_name = models.CharField(max_length=20)
    entitled_guest_surname = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return f" {self.room.place} - {self.room.name} "