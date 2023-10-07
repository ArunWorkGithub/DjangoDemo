from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinkSerializer

def drinks_list(request):
    '''
    Get all the drinks
    Serialize them 
    return JSON object of them 
    '''

    drinks = Drinks.objects.all()

    serializer = DrinkSerializer(drinks, many = True)

    return JsonResponse({'drinks': serializer.data})

