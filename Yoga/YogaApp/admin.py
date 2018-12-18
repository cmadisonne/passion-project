from django.contrib import admin

# Register your models here.
from .models import Contact, Events, Requests

admin.site.register(Contact)
admin.site.register(Events)
admin.site.register(Requests)

