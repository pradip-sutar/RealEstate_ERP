from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import ProductDetails, RaiseCost, ProductCost
from .serializers import ProductDetailsSerializer, RaiseCostSerializer, ProductCostSerializer

# 1. Product Details API View
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def product_details_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id',None)
        if subproject_id:
            product_detail = ProductDetails.objects.filter(subproject_id=subproject_id)
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
def raise_cost_handler(request):
    if request.method == 'GET':
        subproject_id = request.query_params.get('subproject_id',None)
        if subproject_id:
            raise_cost = RaiseCost.objects.filter(subproject_id=subproject_id)
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
def product_cost_handler(request, pk=None):
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
