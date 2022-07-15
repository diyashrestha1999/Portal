
from django.http import HttpResponseRedirect
from .models import Client
from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
admin.site.unregister(get_user_model())
admin.site.unregister(Group)

class MyModelAdmin(admin.ModelAdmin):
    ...
    def change_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser:
            extra_context = extra_context or {}
            extra_context['readonly'] = True

        return super(MyModelAdmin, self).change_view(request, object_id, extra_context=extra_context)

class PersonDataAdmin(admin.ModelAdmin):
    readonly_fields=('full_name', 'last_name', 'email', 'organisation','organisation_size','date','country','domain','phone_number','gender','is_approved')
    search_fields = ['organisation']
    list_display= ('full_name', 'email', 'organisation','date','domain','phone_number')
    def has_add_permission(self, request, obj=None):
        return False

    def changeform_view(self,request,object_id=None,from_url='',extra_context=None):
        extra_context=extra_context or {}
        extra_context['show_save_and_continue']=False
        extra_context['show_save']=False
        return super(PersonDataAdmin,self).changeform_view(request,object_id,extra_context=extra_context)

# class ClientAdmin(admin.ModelAdmin):
#     ...
#     change_form_template = "entities/villain_changeform.html"


#     def response_change(self, request, obj):
#         if "approve_client" in request.POST:
         
#             # self.message_user(request, "This villain is now unique")
#             return HttpResponseRedirect("/admin/client/client/")
#         return super().response_change(request, obj)

   
admin.site.register(Client,PersonDataAdmin)
# admin.site.register(ClientAdmin)


