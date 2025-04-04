from django.contrib import admin
from .models import Product  # Import your model

# Register your model to see it in the admin panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'image')  # Customize displayed fields
