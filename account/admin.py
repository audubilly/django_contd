from django.contrib import admin

from .models import Owner


# Register your models here.


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phoneNumber')


admin.site.register(Owner, OwnerAdmin)
