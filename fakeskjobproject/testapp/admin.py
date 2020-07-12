from django.contrib import admin
from testapp.models import punejobs,hydjobs,mumbaijobs,banglorejobs


# Register your models here.
class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class mumbaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class banglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(punejobs,punejobsAdmin)
admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(mumbaijobs,mumbaijobsAdmin)
admin.site.register(banglorejobs,banglorejobsAdmin)
