from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseAdminUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import UserProfile
# Register your models here.

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model =UserProfile
        fields = ['phone_number','email','first_name','last_name','date_of_birth',
                  'county','location','bio','gender','qualifications','specialization']

class UpdateUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ['phone_number', 'email', 'first_name', 'last_name', 'date_of_birth',
                  'county', 'location', 'bio', 'gender', 'qualifications','specialization']

class UserAdmin(BaseAdminUser):
    form = UpdateUserForm
    add_form = CreateUserForm
    list_display = ['email', 'first_name', 'last_name','county', 'location',  'gender']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name',)}),
        ('Personal Information', {'fields': ('bio', 'county', 'phone_number','qualifications','specialization')}),
        ('permissions', {'fields': ('is_staff','is_active','is_superuser', 'share_email', 'is_doctor','user_permissions' )}),
        ( 'Important Info',{'fields':('last_login','date_joined')})
    )
    ''' add_fieldsets is not a standard modeladmin attribute. UserAdmin overrides get_fieldsets to use this attribute when creating a user'''

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'first_name', 'last_name', 'password1', 'password2', 'county', 'location', 'bio', 'gender', 'qualifications',)
        }),
    )
    search_fields = ('email', 'last_name', 'first_name', 'phone_number')

admin.site.register(UserProfile,UserAdmin)