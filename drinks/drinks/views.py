# seu_app/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Drink
from .serializers import DrinkSerializer

# =========================
# Página HTML de teste
# =========================
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def test_page(request):
    """
    Renderiza a página HTML que consome a API de drinks.
    """
    return render(request, 'drinks/test.html')


# =========================
# API: lista e criação
# =========================
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        # parser para lidar com arquivos
        parser_classes = [MultiPartParser, FormParser]
        serializer = DrinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# API: detalhe, atualização e deleção
# =========================
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
