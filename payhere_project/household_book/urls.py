from django.urls import path, include

from household_book.view.book_views import BookView

urlpatterns = [
    path('',BookView.as_view())
]