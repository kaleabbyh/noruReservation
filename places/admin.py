from django.contrib import admin

from .models import *

admin.site.register(Customer)


admin.site.register(city)
admin.site.register(place_type)
admin.site.register(place)
admin.site.register(room_category)
admin.site.register(room)
admin.site.register(guest)
admin.site.register(reservation)
admin.site.register(reserved_room)
admin.site.register(review)
