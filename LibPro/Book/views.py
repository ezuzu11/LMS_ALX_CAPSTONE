from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, status, generics
from rest_framework.response import Response



# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    #CRUD OPERATION
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            book = self.get_object()
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

    
#View for Viewing and Filtering Books
class AvailableBooksListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        #Filtering by availability
        available = self.request.query_params.get('available', None)
        if available == True:
            queryset = queryset.filter(copies_available=0)

        #optional filters for title, author, or isbn
        title = self.request.query_params.get('title', None)   # icontains -->It ignors case sensitivity while searching 
        author = self.request.query_params.get('author', None)  
        isbn = self.request.query_params.get('isbn', None) # iexact --> It is expecting the exact format ---> it is case sensitive

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if isbn:
            queryset = queryset.filter(isbn__iexact=isbn)

        return queryset

    
            