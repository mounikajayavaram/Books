from django.shortcuts import render
from .serializers import*
from .models import*
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#read
@api_view(['GET'])
def Booklist(request):
    booksobj=BooksModel.objects.all()
    serializer= BookSerializer(booksobj,many=True)
    return Response(serializer.data)

    #create
    #reead
@api_view(['POST'])
def post_book(request):
    booksobj=BooksModel.objects.all()
    serializer= BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

#update
@api_view(['POST'])
def update_book(request,id):
    booksobj=BooksModel.objects.get(id=id)
    serializer= BookSerializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def delete_book(request,id):
    booksobj=BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response("book is created")                      