from django.contrib import admin
from .models import Settings, Collections, Sellers

# Register your models here.

admin.site.register(Settings)
admin.site.register(Collections)
admin.site.register(Sellers)
