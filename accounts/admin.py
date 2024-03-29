from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Referral
# Register your models here.
class AccountAdmin(UserAdmin):
    # gives the columns to be displayed in admin panel for Accounts
    list_display = ('email', 'first_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    # # makes password readonly fields
    fieldsets = ()

class ReferralAdmin(UserAdmin):
    # gives the columns to be displayed in admin panel for Accounts
    list_display = ('account_id', 'ref_code', 'used', 'created')
    ordering = ('-created',)
    
    filter_horizontal = ()
    list_filter = ()

# to show up in admin panel
admin.site.register(Account, AccountAdmin)
admin.site.register(Referral, ReferralAdmin)


