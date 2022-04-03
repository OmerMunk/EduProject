from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .custom_queries import *

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        all_students = Student.objects.all()
        if 'city' in request.GET:
            all_students = all_students.filter(address__icontains=request.GET['city'])
        serializer = StudentsSerializer(all_students, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def single_student(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(student)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StudentsSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tests(request):
    if request.method == 'GET':
        all_tests = Test.objects.all()
        serializer = TestsSerializer(all_tests, many=True)
        return Response(data=serializer.data)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH', 'POST'])
def single_test(request, pk):
    try:
        test = Test.objects.get(id=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TestsSerializer(test)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = TestsSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = TestsSerializer(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        answers = request.data['answers']
        answers = dict(answers)
        count = 0
        total = 0
        for q in test.questions.all():
            total += 1
            for i, j in answers.items():
                if int(q.id) == int(i):
                    if q.option1 == j:
                        count += 1

        student = Student.objects.get(id=request.data['student'])
        if student is not None:
            executed = TestExecuted.objects.create(
                student_id=student,
                test_id=Test.objects.get(id=test.id),
                correct=count,
                wrong=total - count,
                grade=(count / total) * 100
            )
            executed.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stats(request):
    if 'sort' in request.GET:
        ret = average_all_sorted()
    else:
        ret = average_all()

    return Response(ret, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stats_per_student(request, pk):
    ret = average_student(pk)
    return Response(ret, status=status.HTTP_200_OK)




