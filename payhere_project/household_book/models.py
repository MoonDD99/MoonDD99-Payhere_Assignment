from django.db import models
from core.models import TimeStampModel

class Book(TimeStampModel):
    user = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, verbose_name='가계부 이름')
    description = models.CharField(max_length=100, blank=True, verbose_name='가계부 설명')
    delete_flag = models.BooleanField(default=False)

    class Meta:
        db_table = 'book'


class BookRecord(TimeStampModel):
    book = models.ForeignKey('household_book.book', on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, verbose_name='사용 금액')
    description = models.CharField(max_length=30, blank=True, verbose_name='메모')
    delete_flag = models.BooleanField(default=False)

    class Meta:
        db_table = 'book_record'