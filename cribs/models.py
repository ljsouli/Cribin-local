# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date


# Create your models here.

class Guest(models.Model):
    email = models.EmailField()
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    address = models.CharField(max_length=254) #models.OneToOneField(Address)
    image = models.ImageField(upload_to='cribs/static/guest_pictures/', blank=True)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    min_number_of_cribmates = models.PositiveSmallIntegerField()
    max_number_of_cribmates = models.PositiveSmallIntegerField()
    min_price = models.PositiveSmallIntegerField()
    max_price = models.PositiveSmallIntegerField()
    desiredLocation = models.CharField(max_length=100) #Just the city for the moment
    lookingForACrib = models.NullBooleanField(blank=True, null=True) #Null to delete
    def __str__(self):
        return str(self.id)+" :"+self.last_name+ " "+self.first_name

class Host(models.Model):
    email = models.EmailField()
    last_name = models.CharField(max_length=50)
    fist_name = models.CharField(max_length=50)
    address = models.CharField(max_length=254) #models.OneToOneField(Address)
    image = models.ImageField(upload_to='cribs/static/host_pictures/', blank=True)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    def __str__(self):
        return str(self.id)+" :"+self.last_name+ " "+self.fist_name

class Address(models.Model):
    country = models.CharField(max_length=254)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=254)
    postal_num = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    def __str__(self):
        return str(self.street)

class Crib(models.Model):
    address = models.CharField(max_length=254) #browsed address
    complete_address = models.ForeignKey(Address, on_delete=models.CASCADE,blank=True, null=True)
    number_of_rooms = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    #image = models.ImageField(upload_to='cribs/static/cribs_pictures/', blank=True) #Pour l'instant une seul photo ,a enlever
    #A concatener avec IDCrib
    host = models.ForeignKey(Host,on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    def __str__(self):
        return "["+str(self.id)+"] :"+self.address

class Review(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    crib = models.ForeignKey(Crib, models.CASCADE)
    description = models.TextField(blank=True)
    rating = models.PositiveIntegerField(default=4) #Verifier que c'est entre 1 et 10
    def __str__(self):
        return "Rating of :"+str(self.guest) + " on : "+str(self.crib)

class CribImage(models.Model):
    image = models.ImageField(upload_to='cribs/static/crib_pictures/',blank=True)
    crib = models.ForeignKey(Crib, on_delete=models.CASCADE)
    def __str__(self):
        return " image n: " + str(self.id) 

class Room(models.Model):
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=1)
    avalaible_from = models.DateField()
    avalaible_to = models.DateField()
    avalaible = models.BooleanField()
    crib = models.ForeignKey(Crib,on_delete=models.CASCADE,blank=True, null=True)
    host = models.ForeignKey(Host,on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    def __str__(self):
        return str(self.crib.address) + ", room: " +str(self.id)

class RoomImage(models.Model):
    image = models.ImageField(blank=True,upload_to='cribs/static/room_pictures/')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    def __str__(self):
        return str(self.room)


class Rents(models.Model):
    crib_id = models.ForeignKey(Crib, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    begin_date = models.DateField()
    end_date = models.DateField()
    price = models.PositiveIntegerField(default=1)
    transaction_date = models.DateField()
    def __str__(self):
        #print str(Crib.objects.get(id=self.crib_id.id))
        return ( "Crib id :"+str(self.id)) +" Adress : "+ str(Crib.objects.get(id=self.crib_id.id)) +" Guest: "+str(Guest.objects.get(id=self.guest_id.id))
    @property
    def is_past_due(self):
        return date.today() > self.end_date

class AllCribEquipments(models.Model): #Equipments à hardcoder en DB via Admin
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='cribs/static/crib_equipments_icons/', blank=True)
    def __str__(self):
        return str(self.code)
class AllRoomEquipments(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='cribs/static/room_equipments_icons/', blank=True)
    def __str__(self):
        return str(self.code)

class CribEquipments(models.Model): #Equipment à hardcoder en DB via Admin
    crib_id = models.ForeignKey(Crib, on_delete=models.CASCADE)
    crib_equipment = models.ForeignKey(AllCribEquipments, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    def __str__(self):
        return str(" Address : "+ str(Crib.objects.get(id=self.crib_id.id))+" : "+str(self.crib_equipment) )

class RoomEquipments(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_equipment = models.ForeignKey(AllRoomEquipments, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 

class AllHobbies(models.Model): #Hobbies à hardcoder en DB via Admin
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='cribs/static/hobbies_icons/', blank=True)
    def __str__(self):
        return str(self.code)

class AllStatus(models.Model): #Status à hardcoder en DB via Admin
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    def __str__(self):
        return str(self.code)

class AllLanguages(models.Model): #Languages à hardcoder en DB via Admin
    code = models.CharField(max_length=10)
    lang = models.TextField(blank=True)
    def __str__(self):
        return str(self.code)

class GuestHobbies(models.Model):
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    hobby = models.ForeignKey(AllHobbies, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 


class GuestStatus(models.Model): 
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    status = models.ForeignKey(AllStatus, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 

class GuestLanguages(models.Model): 
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    status = models.ForeignKey(AllStatus, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 

class HostHobbies(models.Model):
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    hobby = models.ForeignKey(AllHobbies, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 

class HostStatus(models.Model): 
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE)
    status = models.ForeignKey(AllStatus, on_delete=models.CASCADE)

class HostLanguages(models.Model): 
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 
    status = models.ForeignKey(AllStatus, on_delete=models.CASCADE,blank=True, null=True) #NULL A ENLEVER! 