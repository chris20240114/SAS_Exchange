from django.contrib import admin
from .models import Seller
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#admin.site.register(Seller)

class AccountInline(admin.StackedInline):
    model = Seller
    can_delete = False
    verbose_name_plural = 'Sellers'
    
class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )
    
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)