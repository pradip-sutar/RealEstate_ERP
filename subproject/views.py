from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# View for Product Detail
@api_view(['GET', 'POST'])
def product_detail_view(request):
    if request.method == 'GET':
        products = ProductDetail.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for Raise Cost
@api_view(['GET', 'POST'])
def raise_cost_view(request):
    if request.method == 'GET':
        raise_costs = RaiseCost.objects.all()
        serializer = RaiseCostSerializer(raise_costs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RaiseCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for Product Cost
@api_view(['GET', 'POST'])
def product_cost_view(request):
    if request.method == 'GET':
        product_costs = ProductCost.objects.all()
        serializer = ProductCostSerializer(product_costs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View for Product Cost_1
@api_view(['GET', 'POST'])
def product_cost_view(request):
    if request.method == 'GET':
        products = ProductCost_1.objects.all()
        serializer = ProductCostSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for Amenity Cost
@api_view(['GET', 'POST'])
def amenity_cost_view(request):
    if request.method == 'GET':
        amenities = AmenityCost.objects.all()
        serializer = AmenityCostSerializer(amenities, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AmenityCostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
