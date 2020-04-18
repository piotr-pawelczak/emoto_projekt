from django.shortcuts import render


speed_record = 120
time = 24
distance = 100


def stats(request):
    context = {
        'speed': speed_record,
        'time': time,
        'distance': distance
    }
    return render(request, 'stats/stats.html', context)
