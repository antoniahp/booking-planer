from django.contrib import admin
from core.models import ContinentModel, CountryModel, CityModel, PlaceModel, RoomModel, BookingModel, TemporalBookingModel


class CountryInLine(admin.StackedInline):
    model = CountryModel
    extra = 0
    eadonly_fields = ["name"]
    can_delete = False
    show_change_link = True


class CityInLine(admin.StackedInline):
    model = CityModel
    extra = 0
    readonly_fields = ["name"]
    can_delete = False
    show_change_link = True


class PlaceInLine(admin.StackedInline):
    model = PlaceModel
    extra = 0
    readonly_fields = ["name"]
    can_delete = False
    show_change_link = True


class RoomInLine(admin.StackedInline):
    model = RoomModel
    extra = 0
    readonly_fields = ["name"]
    can_delete = False
    show_change_link = True


class BookingInLine(admin.StackedInline):
    model = BookingModel
    extra = 0
    readonly_fields = ["room"]
    can_delete = False
    show_change_link = True


class ContinentAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["name"]

    inlines = [CountryInLine]


class CountryAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    inlines = [CityInLine]


class CityAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    search_fields = ["name"]

    inlines = [PlaceInLine]

class PlaceAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    search_fields = ["name"]

    inlines = [RoomInLine]

class RoomAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    search_fields = ["name"]

    inlines = [BookingInLine]


class BookingAdmin(admin.ModelAdmin):
    search_fields = ["room__name"]
    list_filter = ["room"]






admin.site.register(ContinentModel, ContinentAdmin)
admin.site.register(CountryModel, CountryAdmin)
admin.site.register(CityModel, CityAdmin)
admin.site.register(PlaceModel, PlaceAdmin)
admin.site.register(RoomModel, RoomAdmin)
admin.site.register(BookingModel,BookingAdmin)
admin.site.register(TemporalBookingModel)



