from django.http import HttpResponse
from django.shortcuts import render
from .models import ABC
from rest_framework.response import Response
from rest_framework import status
from .api.serializers import ABCSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def abcc(request):
    if request.method == 'GET':
        try:
            a = ABC.objects.all()
            serializer = ABCSerializer(a, many=True)  # Serialize the queryset
            return Response({"a": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"message": "Hello, world!!!"})
def home(request):
    return HttpResponse('<h1>Hello</h1>')