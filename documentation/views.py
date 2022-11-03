from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
  
# simple serializer for student
class StudentForm(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
  
# simple endpoint to take the serializer data
class Student(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(request_body=StudentForm)
    def post(self, request):
        serializer = StudentForm(data=request.data)
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
