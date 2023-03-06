from rest_framework import serializers

from household_book.models import Book, BookRecord

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['user']

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['delete_flag']

class BookRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecord
        exclude = ['book']

class BookRecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRecord
        exclude = ['delete_flag']

class BookRecordDeleteSerializer(serializers.ModelSerializer):
    def delete(self, instance):
        instance.delete_flag = True
        instance.save()
        return instance

    class Meta:
        model = BookRecord
        exclude = '__all__'
        
        