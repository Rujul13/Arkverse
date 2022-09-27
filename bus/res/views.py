from ast import Return
from django.shortcuts import render
from django.http import JsonResponse
from .models import uni
from .serializers import uniserializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def uni_list(request, format=None):
    if request.method =='GET':  
     unis = uni.objects.all()
     serializer = uniserializer(unis, many=True)
     return Response(serializer.data)
    
    if request.method =='POST': 
        serializer = uniserializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def uni_name(request,id, format=None):
    try:
        uni.objects.get(pk=id)
    except uni.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
      serializer = uniserializer(uni)
      return Response(serializer.data)
 

    elif request.method =='PUT':
        serializer = uniserializer(uni, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method =='DELETE':
        uni.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    dest1 = uni.objects.all()
    return render(request, "index.html",{dest1:dest1})