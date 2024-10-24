from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import *
from .serializers import *

# 1. Product Details API View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def product_details_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id',None)
        if subproject_id:
            product_details = ProductDetails.objects.filter(subproject_id=subproject_id)
        else:
            product_details = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(product_details, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        product_id = request.query_params.get('product_id',None)
        product_detail = ProductDetails.objects.get(code=product_id)
        serializer = ProductDetailsSerializer(product_detail, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product_id = request.query_params.get('product_id',None)
        product_detail = ProductDetails.objects.get(code=product_id)
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 2. Raise Cost API View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def raise_cost_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id',None)
        if subproject_id:
            raise_costs = RaiseCost.objects.filter(subproject_id=subproject_id)
        else:
            raise_costs = RaiseCost.objects.all()
        serializer = RaiseCostSerializer(raise_costs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RaiseCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        raise_id = request.query_params.get('raise_id',None)
        raise_cost = RaiseCost.objects.get(id=raise_id)
        serializer = RaiseCostSerializer(raise_cost, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        raise_id = request.query_params.get('raise_id',None)
        raise_cost = RaiseCost.objects.get(id=raise_id)
        raise_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 3. Product Cost API View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def product_cost_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id',None)
        if subproject_id:
            product_cost = ProductCost.objects.filter(subproject_id=subproject_id)
        else:
            product_costs = ProductCost.objects.all()
        serializer = ProductCostSerializer(product_costs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        cost_id = request.query_params.get('cost_id',None)
        product_cost = ProductCost.objects.get(pk=cost_id)
        serializer = ProductCostSerializer(product_cost, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cost_id = request.query_params.get('cost_id',None)
        product_cost = ProductCost.objects.get(pk=cost_id)
        product_cost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def product_inventories_handler(request):
    if request.method == 'GET':
        # Fetch based on subproject_id query parameter
        subproject_id = request.query_params.get('subproject_id', None)
        if subproject_id:
            inventories = ProductInventories.objects.filter(subproject_id=subproject_id)
        else:
            return Response({"error": "Subproject ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ProductInventoriesSerializer(inventories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new product inventory entry
        serializer = ProductInventoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        inventory_id = request.query_params.get('inventory_id',None)
        if not inventory_id:
            return Response({"error": "Product Inventory ID is required for updating"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            inventory = ProductInventories.objects.get(pk=inventory_id)
        except ProductInventories.DoesNotExist:
            return Response({"error": "Product Inventory not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductInventoriesSerializer(inventory, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventory_id = request.query_params.get('inventory_id',None)
        if not inventory_id:
            return Response({"error": "Product Inventory ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            inventory = ProductInventories.objects.get(pk=inventory_id)
        except ProductInventories.DoesNotExist:
            return Response({"error": "Product Inventory not found"}, status=status.HTTP_404_NOT_FOUND)

        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Sub Product Images API View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def sub_product_images_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id', None)
        if subproject_id:
            sub_images = SubProductImages.objects.filter(subproject_id=subproject_id)
        else:
            return Response({"error": "Subproject ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SubProductImagesSerializer(sub_images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubProductImagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        image_id = request.query_params.get('image_id',None)
        if not image_id:
            return Response({"error": "Sub Product Image ID is required for updating"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            sub_image = SubProductImages.objects.get(pk=image_id)
        except SubProductImages.DoesNotExist:
            return Response({"error": "Sub Product Image not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SubProductImagesSerializer(sub_image, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        image_id = request.query_params.get('image_id',None)
        if not image_id:
            return Response({"error": "Sub Product Image ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            sub_image = SubProductImages.objects.get(pk=image_id)
        except SubProductImages.DoesNotExist:
            return Response({"error": "Sub Product Image not found"}, status=status.HTTP_404_NOT_FOUND)

        sub_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Payment Slab API View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@transaction.atomic
def payment_slab_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id', None)
        if subproject_id:
            slabs = PaymentSlab.objects.filter(subproject_id=subproject_id)
        else:
            return Response({"error": "Subproject ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PaymentSlabSerializer(slabs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentSlabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        slab_id = request.query_params.get('slab_id',None)
        if not slab_id:
            return Response({"error": "Payment Slab ID is required for updating"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            slab = PaymentSlab.objects.get(pk=slab_id)
        except PaymentSlab.DoesNotExist:
            return Response({"error": "Payment Slab not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaymentSlabSerializer(slab, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        slab_id = request.query_params.get('slab_id',None)
        if not slab_id:
            return Response({"error": "Payment Slab ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            slab = PaymentSlab.objects.get(pk=slab_id)
        except PaymentSlab.DoesNotExist:
            return Response({"error": "Payment Slab not found"}, status=status.HTTP_404_NOT_FOUND)

        slab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
