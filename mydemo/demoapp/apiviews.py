from .models import Teacher
from .serializers import TeacherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TeacherDetail(APIView):
    """
    Retrieve, update or delete a teacher instance.
    """
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            teacher = self.get_object(pk)
            serializer = TeacherSerializer(teacher)
        else:
            teacher = Teacher.objects.all()
            serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        if pk:
            teacher = self.get_object(pk)
        else:
            teacher = Teacher.objects.all()
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)