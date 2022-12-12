from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Items
from .serializers import ItemsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request,"index.html",{})
# Create your views here.
@api_view(['GET','POST'])
def item_list(request):
 if request.method == 'GET':
    items = Items.objects.all()
    serilaizer = ItemsSerializer(items, many = True)
    return Response(serilaizer.data)
 if request.method == 'POST':
        serilaizer = ItemsSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
def item_detail(request,id):
    try:
        item=Items.objects.get(pk=id)
    except Items.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =ItemsSerializer(item)
        return Response(serializer.data)
    elif request.method == 'POST':
       serilaizer = ItemsSerializer(item,data=request.data)
       if serilaizer.is_valid():
          serilaizer.save()
          return Response(serializer.data) 
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

