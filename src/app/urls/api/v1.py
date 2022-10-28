from django.urls import include, path

urlpatterns = [
    path('v1/books/', include('books.urls')),
]
