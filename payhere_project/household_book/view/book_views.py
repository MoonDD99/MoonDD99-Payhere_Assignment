from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from household_book.models import Book
from household_book.serializers import *

class BookView(APIView):
    permission_classes = [IsAuthenticated]

    #household_book 리스트 GET /books   
    def get(self, request):
        queryset = Book.objects.filter(user=request.user.id, delete_flag=request.GET.get('deleted', False))
        serializer = BookListSerializer(queryset, many=True)
        return Response(serializer.data)

    #household_book 생성 POST /books
    def post(self, request):
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Success to create householdbook'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #household_book 상세보기 GET /books/{books.id}
    #household_book 삭제 DELETE /books/{books.id}

    #household_book 수정 (title, description) PUT /books/{books.id}



