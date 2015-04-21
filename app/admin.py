from django.contrib import admin

# Register your models here.

from app.models import Comic, Contact

admin.site.register(Comic)
admin.site.register(Contact)