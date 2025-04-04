import json
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(["POST"])
@permission_classes([IsAuthenticated])  # ✅ Require authentication
def create_product(request):
    parser_classes = (MultiPartParser, FormParser)  # ✅ Allow file uploads

    name = request.data.get("name")
    description = request.data.get("description", "")
    price = request.data.get("price")
    image = request.FILES.get("image")  # ✅ Get uploaded image

    if not name or price is None:
        return JsonResponse(
            {"error": "Missing required fields"},
            status=status.HTTP_400_BAD_REQUEST
        )

    product = Product.objects.create(name=name, description=description, price=price, image=image)

    return JsonResponse(
        {"message": "Product created successfully", "id": product.id,
         "image_url": product.image.url if product.image else None},
        status=status.HTTP_201_CREATED
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated])  # ✅ Require authentication
def list_products(request):
    products = Product.objects.all().values("id", "name", "description", "price", "created_at")
    return JsonResponse(list(products), safe=False, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])  # ✅ Require authentication
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # ✅ Simplified query

    data = request.data  # ✅ Use DRF request parsing
    product.name = data.get("name", product.name)
    product.description = data.get("description", product.description)
    product.price = data.get("price", product.price)
    product.save()

    return JsonResponse(
        {"message": "Product updated successfully"},
        status=status.HTTP_200_OK
    )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])  # ✅ Require authentication
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # ✅ Simplified query
    product.delete()

    return JsonResponse(
        {"message": "Product deleted successfully"},
        status=status.HTTP_200_OK
    )
