from rest_framework import serializers

from household_book.models import Book

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['user']

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['delete_flag']