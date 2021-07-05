from django.contrib import admin

# Register your models here.
from hw6.models import Category, New, Law, Publication, Favourite

admin.site.register(New)
admin.site.register(Law)
admin.site.register(Publication)
admin.site.register(Favourite)
admin.site.register(Category)
