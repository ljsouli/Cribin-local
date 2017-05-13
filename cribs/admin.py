# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Crib
from .models import Guest
from .models import Host
from .models import Address
from .models import CribImage
from .models import Room
from .models import RoomImage
from .models import Rents
from .models import AllCribEquipments
from .models import AllHobbies
from .models import AllLanguages
from .models import AllStatus
from .models import GuestHobbies
from .models import GuestLanguages
from .models import GuestStatus
from .models import HostHobbies
from .models import HostLanguages
from .models import HostStatus
from .models import CribEquipments
from .models import Review


admin.site.register(Crib)
admin.site.register(Guest)
admin.site.register(Host)
admin.site.register(Address)
admin.site.register(CribImage)
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(Rents)
admin.site.register(AllCribEquipments)
admin.site.register(AllHobbies)
admin.site.register(AllLanguages)
admin.site.register(AllStatus)
admin.site.register(GuestHobbies)
admin.site.register(GuestLanguages)
admin.site.register(GuestStatus)
admin.site.register(HostHobbies)
admin.site.register(HostLanguages)
admin.site.register(HostStatus)
admin.site.register(CribEquipments)
admin.site.register(Review)

# Register your models here.
