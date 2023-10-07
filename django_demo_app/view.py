from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_drinks_list(request, format = None):
    '''
    Get all the drinks
    Serialize them 
    return JSON object of them 
    '''

    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many = True)

    '''
    To send the JsonRespone with non dictionary object
    we need to disable the safe option in JsonResponse class
    "In order to allow non-dict objects to be serialized set the safe parameter to False."
    '''
    # return JsonResponse(serializer.data, safe=False)
    # return JsonResponse({'drinks': serializer.data})

    return Response(data=serializer.data)

@api_view(['POST'])
def insert_drink(request, format = None):
    serializer = DrinkSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format = None):
    
    try:
        drink = Drink.objects.get(pk = id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        serializer = DrinkSerializer(drink)
        return Response(data=serializer.data)
    
    elif(request.method == 'PUT'):
        serializer = DrinkSerializer(drink, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif(request.method == 'DELETE'):
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)