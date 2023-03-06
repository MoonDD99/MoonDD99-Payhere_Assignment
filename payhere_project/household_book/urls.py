from django.urls import path, include

from household_book.view.book_views import BookView
from household_book.view.book_record_views import BookRecordView, BookRecordDetailView

urlpatterns = [
    path('',BookView.as_view()),
    path('<int:book_id>',BookView.as_view()),
    path('<int:book_id>/records',BookRecordView.as_view()),
    path('<int:book_id>/records/<int:record_id>',BookRecordDetailView.as_view())
]