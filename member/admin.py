from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(state)

class GuildAdmin(admin.ModelAdmin):
    list_display = ['guild','Update']
    readonly_fields = ['Timestamp', 'Update']
    search_fields = ['guild']

admin.site.register(guild,GuildAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display=['Nickname','Identity','Update']
    readonly_fields=['Timestamp','Update']
    search_fields = ['Nickname','Identity','Update']

admin.site.register(Member,MemberAdmin)

class CharaterAdmin(admin.ModelAdmin):
    list_display = ['Name', 'account', 'Update']
    readonly_fields = ['Timestamp', 'Update']
    search_fields = ['Id','Product_Name', 'Count']

admin.site.register(Character,CharaterAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['publisher', 'Product_Name','Price','Count', 'Update']
    readonly_fields = ['Timestamp', 'Update']
    search_fields = ['Id','Product_Name']

admin.site.register(Order,OrderAdmin)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ['Provider', 'Order_Id', 'Update']
    readonly_fields = ['Timestamp', 'Update']
    search_fields = ['Order_Id','Character_name', ]

admin.site.register(Provider_details,ProviderAdmin)

class Makeitem_Admin(admin.ModelAdmin):
    list_display = ['Name', 'Inner']
    readonly_fields = ['Timestamp', 'Update']
    search_fields = ['Name','Inner' ]

admin.site.register(Plate_shoes,Makeitem_Admin)
admin.site.register(Plate_armor,Makeitem_Admin)
admin.site.register(Plate_helmet,Makeitem_Admin)
admin.site.register(Sword,Makeitem_Admin)
admin.site.register(Axe,Makeitem_Admin)
admin.site.register(Mace,Makeitem_Admin)
admin.site.register(Gloves,Makeitem_Admin)
admin.site.register(Crossbow,Makeitem_Admin)
admin.site.register(Shield,Makeitem_Admin)