from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from household_book.models import BookRecord
from household_book.serializers import *

class BookRecordView(APIView):
    permission_classes = [IsAuthenticated]

    #book_recod 리스트 GET /books/{books.id}/records
    def get(self, request, book_id):
        queryset = BookRecord.objects.filter(book=book_id,delete_flag=request.GET.get('deleted', False))
        serializers = BookRecordSerializer(queryset, many=True)
        return Response(serializers.data)

    #household_book_recod 생성 POST /household-books/{house-books.id}/records
    def post(self, request, book_id):
        serializer = BookRecordCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Success to create householdbook Record'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRecordDetailView(APIView):
    permission_classes = [IsAuthenticated]

    #household_book_recod 상세보기 GET /books/{books.id}/records/{record.id}
    def get(self, request, book_id, record_id):
        book_record = get_object_or_404(BookRecord,pk=record_id,book_id=book_id, delete_flag=False)
        serializer = BookRecordSerializer(book_record)
        return Response(serializer.data)
    
    # household_book_recod 수정 (amount, description) PATCH /books/{books.id}/records/{record.id}    
    def patch(self, request, book_id, record_id):
        book_record = get_object_or_404(BookRecord,pk=record_id,book_id=book_id,delete_flag=False)

        serializer = BookRecordSerializer(instance=book_record, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #household_book_recod 삭제 DELETE /books/{book.id}/records/{record.id}
    def delete(self, request, book_id, record_id):
        book_record = get_object_or_404(BookRecord,pk=record_id,book_id=book_id,delete_flag=False)

        book_record.delete_flag = True
        serializer = BookRecordSerializer(instance = book_record, data=book_record.__dict__)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'success': 'success to delete Household Book Record'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #household_book_recod 복제 POST /books/{book.id}/records/{record.id}
    def post(self, request, book_id, record_id):
        book_record = get_object_or_404(BookRecord,pk=record_id,book_id=book_id,delete_flag=False)
        
        book_record.pk = None
        serializer = BookRecordSerializer(instance=book_record, data=book_record.__dict__)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Success to duplicate householdbook Record'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#household_book_recod 복제 POST /household-books/{house-books.id}/records/{record.id}