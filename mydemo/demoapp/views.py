from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TodoSerializer,StudentSerializer
from .models import Todo,Student
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


# Create your views here.
def index(request):
    return HttpResponse("Hello, Globant. You're at the HSBC.")


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk=None):
    try:
        if pk:
            student = Student.objects.get(pk=pk)
        else:
            student = Student.objects.all()
    except Student.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if pk:
            student_serializer = StudentSerializer(student)
        else:
            student_serializer = StudentSerializer(student, many=True)
        return JsonResponse(student_serializer.data, safe=False)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)





