from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Pricing, Jobs





class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone", "email", "message", "time")

class PricingAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", "lname", "cname", "phone", "email", "checks", "message", "time")

class JobsAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone", "email", "role", "message", "time", "show_cv_url")
    
    def show_cv_url(self, obj):
         return format_html("<a href='{url}'>{url}</a>", url=obj.cv)
    show_cv_url.short_description = "CV"


# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Jobs, JobsAdmin)
