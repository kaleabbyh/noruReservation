import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# new model structure
class city(models.Model):
    city_name = models.CharField(max_length=200, null=False)
    ts_created = models.DateTimeField(auto_now_add=True)
    city_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.city_name


#place type
class place_type(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    place_type_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.name
    

# place model
class place(models.Model):
    place_type = models.ForeignKey(place_type, blank=True, null=True, on_delete=models.CASCADE)
    place_address = models.ForeignKey(city, on_delete = models.CASCADE)
    place_name = models.CharField(max_length=200)
    about_place = models.TextField(max_length=2000,null=True,blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    ts_created = models.DateTimeField(auto_now_add=True)
    place_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    place_image = models.ImageField(null=True, blank=True)
    

    @property
    def place_imageURL(self):
        try:
            url = self.place_image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ['-vote_ratio','vote_total']
        
    def __str__(self):
        return self.place_name

class room_category(models.Model):
    room_category_name = models.CharField(max_length=200)
    ts_created = models.DateTimeField(auto_now_add=True)
    room_category_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return self.room_category_name


class room(models.Model):
    place = models.ForeignKey(place, on_delete=models.CASCADE, null=True)
    room_category = models.ForeignKey(
        room_category, on_delete=models.CASCADE, null=True)
    room_number = models.IntegerField()
    room_name = models.CharField(max_length=200, null=False)
    room_added_date=models.DateTimeField(auto_now_add=True)
    room_updated_date=models.DateTimeField(auto_now=True)
    room_description = models.TextField()
    room_price = models.FloatField()
    ts_created = models.DateTimeField(auto_now_add=True)
    room_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    room_image = models.ImageField(null=True, blank=True)
    class Meta:
        ordering = ['-room_added_date','-room_updated_date']
    def __str__(self):
        return self.room_name

    @property
    def room_imageURL(self):
        try:
            url = self.room_image.url
        except:
            url = ''
        return url

class guest(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=200, null=True)
    guest_email = models.EmailField(max_length=200)
    guest_phone=models.CharField(max_length=200)
    ts_created = models.DateTimeField(auto_now_add=True)
    guest_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    guest_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.guest_name

    @property
    def guest_imageURL(self):
        try:
            url = self.guest_image.url
        except:
            url = ''
        return url


class reservation(models.Model):
    guest = models.ForeignKey(
        guest, on_delete=models.SET_NULL, null=True, blank=True)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    complete = models.BooleanField(default=False)
    reservation_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.id)



class reserved_room(models.Model):
    room = models.ForeignKey(room, on_delete=models.SET_NULL, null=True)
    reservation = models.ForeignKey(
        reservation, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    reserved_room_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    




#place Review and comment
class review(models.Model):
    STAR_COUNT = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    # owner = 
    place = models.ForeignKey(place, on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    value = models.IntegerField(choices=STAR_COUNT)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.value)

