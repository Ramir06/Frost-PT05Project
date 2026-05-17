from django.shortcuts import render
from django.http import JsonResponse
from .models import IceCream


def index(request):
    # Получаем все мороженые для бегущей строки
    all_ice_creams = list(IceCream.objects.all())

    # Разделяем на два ряда для бегущей строки
    mid_point = len(all_ice_creams) // 2
    marquee_ice_creams = all_ice_creams[:mid_point] if mid_point > 0 else all_ice_creams
    marquee_ice_creams_reverse = all_ice_creams[mid_point:] if mid_point > 0 else all_ice_creams

    # Получаем сезонные вкусы
    spring_ice_cream = IceCream.objects.filter(season='spring').first()
    summer_ice_cream = IceCream.objects.filter(season='summer').first()
    autumn_ice_cream = IceCream.objects.filter(season='autumn').first()
    winter_ice_cream = IceCream.objects.filter(season='winter').first()

    context = {
        'marquee_ice_creams': marquee_ice_creams,
        'marquee_ice_creams_reverse': marquee_ice_creams_reverse,
        'spring_ice_cream': spring_ice_cream,
        'summer_ice_cream': summer_ice_cream,
        'autumn_ice_cream': autumn_ice_cream,
        'winter_ice_cream': winter_ice_cream,
    }

    return render(request, 'ice_shop/index.html', context)


def get_ice_creams_api(request):
    ice_creams = IceCream.objects.values(
        'id', 'title', 'description', 'price', 'flavor_type',
        'is_popular', 'is_new', 'is_vegan', 'is_seasonal', 'season',
    )
    return JsonResponse(list(ice_creams), safe=False)