# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Crib
from .models import CribImage
from .models import Room
from .models import RoomImage
from .models import Rents
from .models import Guest
from .models import Host
from .models import Address
from .models import CribEquipments
from .models import AllCribEquipments
from .models import GuestHobbies
from .models import AllHobbies
from .models import Review
from datetime import timedelta

# Create your views here.

#Piste mettre une variable globale pour le Crib courant
cribs = list(Crib.objects.filter(address__startswith="Av")) #list that will contain all the cribs corresponding to my preferences
crib = cribs[0]
currentCrib = -1

def browse(request):
    """
    cribs = Crib.objects.all() #Recuperer du profil de l'utilisateur
    latest_cribs = cribs.order_by('-number_of_rooms')[:5] #Ajouter système de matching ici
    context = {'latest_cribs' : latest_cribs}
    return render(request, 'cribs/browse.html', context)
    """
    #Merger Browse et nextCrib
    addresses = list(Address.objects.filter(city="Brussels"))
    global cribs
    cribs=list()
    for address in addresses:
       cribs.append(list(Crib.objects.filter(complete_address=address))[0])
    global crib
    crib = cribs.pop()
    global currentCrib
    currentCrib = crib.id

    #Recuperation du context de la page
    cribImages = CribImage.objects.filter(crib=currentCrib)
    rents = list(Rents.objects.filter(crib_id=currentCrib)) #rents for current crib
    guestsList = list()
    cribHobbies = list()
    listHobbies = list()
    for rent in rents:
        if not rent.is_past_due:
            currentGuest = Guest.objects.get(id=rent.guest_id.id)
            guestsList.append(currentGuest)#

    for guest in guestsList:
        currentGuestHobbies = GuestHobbies.objects.filter(guest_id=guest)
        for currentGuestHobby in currentGuestHobbies:
            cribHobbies.append(list(GuestHobbies.objects.filter(hobby=currentGuestHobby.hobby))[0])
    for cribHobby in cribHobbies:
        currentHobby = AllHobbies.objects.get(code=cribHobby.hobby)
        if currentHobby not in listHobbies:
            listHobbies.append(currentHobby)
       
    host_id = crib.host.id
    host = Host.objects.get(id=host_id)
    rooms = Room.objects.filter(crib=currentCrib)
    roomImages = RoomImage.objects.filter(room=rooms)
    cribEquipments = CribEquipments.objects.filter(crib_id=currentCrib)
    cribEquipmentImages = list()
    for cribEquip in cribEquipments:
        equip = AllCribEquipments.objects.get(code=cribEquip.crib_equipment)
        cribEquipmentImages.append(equip)

    reviews = list(Review.objects.filter(crib=currentCrib))


    context = {'crib_images' : cribImages, 'crib': crib, 'guests_list': guestsList,
               'host': host, 'room_images' : roomImages, 'crib_equipments': cribEquipments,
                'equipments_images': cribEquipmentImages,'crib_hobbies' : listHobbies, 'reviews' : reviews}
    #
    return render(request, 'cribs/browse.html', context)

def nextCrib(request):
    #currentCrib = cribs[0].id #Freeze at the last one
    print "LENGTH CRIBS"
    print len(cribs)
    if(len(cribs)>=1):
        global crib
        crib = cribs.pop()
        global currentCrib
        currentCrib = crib.id

     #Recuperation du context de la page
    cribImages = CribImage.objects.filter(crib=currentCrib)
    rents = list(Rents.objects.filter(crib_id=currentCrib)) #rents for current crib
    guestsList = list()
    cribHobbies = list()
    listHobbies = list()
    temp = ""
    for rent in rents:
        if not rent.is_past_due:
            currentGuest = Guest.objects.get(id=rent.guest_id.id)
            guestsList.append(currentGuest)#

    for guest in guestsList:
        currentGuestHobbies = GuestHobbies.objects.filter(guest_id=guest)
        for currentGuestHobby in currentGuestHobbies:
            cribHobbies.append(list(GuestHobbies.objects.filter(hobby=currentGuestHobby.hobby))[0])
    for cribHobby in cribHobbies:
        currentHobby = AllHobbies.objects.get(code=cribHobby.hobby)
        if currentHobby not in listHobbies:
            listHobbies.append(currentHobby)
       
    host_id = crib.host.id
    host = Host.objects.get(id=host_id)
    rooms = Room.objects.filter(crib=currentCrib)
    roomImages = RoomImage.objects.filter(room=rooms)
    cribEquipments = CribEquipments.objects.filter(crib_id=currentCrib)
    cribEquipmentImages = list()
    for cribEquip in cribEquipments:
        equip = AllCribEquipments.objects.get(code=cribEquip.crib_equipment)
        cribEquipmentImages.append(equip)

    context = {'crib_images' : cribImages, 'crib': crib, 'guests_list': guestsList,
               'host': host, 'room_images' : roomImages, 'crib_equipments': cribEquipments,
                'equipments_images': cribEquipmentImages,'crib_hobbies' : listHobbies}
    #
    return render(request, 'cribs/browse.html', context)



def subscribe(request):
    form = GuestForm(request.POST or None)
    if form.is_valid():
        a=1
        #Traitement des données ici
    return render(request,'cribs/subscribe.html',locals())

def home(request):
    return render(request,'cribs/home.html',locals())




def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)