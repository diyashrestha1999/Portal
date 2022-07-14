from .models import Client
from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
admin.site.unregister(get_user_model())
admin.site.unregister(Group)

class PersonDataAdmin(admin.ModelAdmin):
    readonly_fields=('full_name', 'last_name', 'email', 'organisation','country','domain','phone_number','gender')
    search_fields = ['organisation']
    list_display= ('full_name', 'last_name', 'email', 'organisation','country','domain','phone_number','gender')
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Client,PersonDataAdmin)
