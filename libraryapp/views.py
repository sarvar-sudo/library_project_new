from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
# Create your views here.

# Class ko'rinishida api


# Generic views lar 
# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
# class BookDestroyApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 
 
class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 
 
# APIview lar 

class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"{len(books)} ta kitob mavjud",
            "books": serializer_data
        }
        
        return Response(data)
 
 
class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": "Ma'lumotlar bazasiga kitob qo'shildi",
                "books": data}
            return Response(data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookRetrieveApiView(APIView):
        def get(self,request,pk):
            try:
                book = Book.objects.get(id=pk)
                serializer_data = BookSerializer(book).data
                
                data = {
                    'status': "Successfully",
                    "book": serializer_data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Exception:
                return Response({
                    'status' : "False",
                    'message' : 'Kitob toplimadi'
                }, status=status.HTTP_404_NOT_FOUND)


class BookDestroyApiView(APIView):
    def delete(self, request, pk):
        try:
            book = get_object_or_404(Book, id=pk)
            book.delete()
            return Response({
                'status': 'Succesfully delete',
                'message': "Kitob o'chirilidi"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': 'False',
                'message': 'Kitob topilmadi'
            }, status=status.HTTP_404_NOT_FOUND) 

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        try:
            book = get_object_or_404(Book.objects.all(), id=pk)
            data = request.data
            serializer = BookSerializer(instance=book, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                book_saved = serializer.save()
            return Response({
                'status': 'True', 'message': f"{book_saved} kitob yangilandi."
            }, status = status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': 'False',
                'message': 'Kitob topilmadi'
            }, status=status.HTTP_404_NOT_FOUND) 


 
# Funksiya ko'rinishida api 
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# from rest_framework.viewset import viewset
class BookViewsSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer