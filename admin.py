from django.contrib import admin
from.models import *

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)


class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("title","picture")

admin.site.register(tblgallery,tblgalleryAdmin)


class tblcategoryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture")
admin.site.register(tblcategory,tblcategoryAdmin)

class tblproductAdmin(admin.ModelAdmin):
    list_display=("id","title","product_info","product_category","price","discounted_price","weight","picture","posted_date")
admin.site.register(tblproduct,tblproductAdmin)

class tblregisterAdmin(admin.ModelAdmin):
    list_display=("name","email","password","address","pincode","landmark","mobile","regdate","picture")
admin.site.register(tblregister,tblregisterAdmin)


class tblcartAdmin(admin.ModelAdmin):
    list_display=("id","userid","pid","product_picture","product_name","product_price","product_info","discounted_price","total_price","product_weight","product_quantity","added_date")
admin.site.register(tblcart,tblcartAdmin)


class tblorderAdmin(admin.ModelAdmin):
    list_display=("id","userid","pid","product_picture","product_name","product_price","product_info","discounted_price","total_price","product_weight","product_quantity","added_date","status")
admin.site.register(tblorder,tblorderAdmin)