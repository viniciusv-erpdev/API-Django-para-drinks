from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def drink_list(request, format=None):
    """
    GET: lista todos os drinks
    POST: cria novo drink (aceita imagem via multipart/form-data)
    """
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def drink_detail(request, id, format=None):
    """
    GET: retorna um drink
    PUT: atualiza (aceita imagem via multipart/form-data)
    DELETE: deleta
    """
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data, partial=False, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@ensure_csrf_cookie
def test_page(request):
    return render(request, 'drinks/test.html')