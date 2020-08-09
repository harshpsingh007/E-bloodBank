from django.contrib import admin
from .models import Contact,Donor_details,Blood_DATA

# Register your models here.
admin.site.register(Contact)
admin.site.register(Donor_details)
admin.site.register(Blood_DATA)
