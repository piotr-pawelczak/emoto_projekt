from django.shortcuts import render
import achievements.achievements_class as ac

ach1 = ac.Achievement('Snail', 'speed', 50, 'speed50.png')
ach2 = ac.Achievement('Beginning of the ride', 'speed', 70, 'speed70.png')
ach3 = ac.Achievement('First 100', 'speed', 100, 'speed100.png')
ach4 = ac.Achievement('Cheetah', 'speed', 150, 'speed150.png')
ach5 = ac.Achievement('Demon of speed', 'speed', 200, 'speed200.png')

ach6 = ac.Achievement('Walk', 'distance', 100, 'distance100.png')
ach7 = ac.Achievement('Adept', 'distance', 200, 'distance200.png')
ach8 = ac.Achievement('Travel', 'distance', 300, 'distance300.png')
ach9 = ac.Achievement('Marathon', 'distance', 500, 'distance500.png')
ach10 = ac.Achievement('Globetrotter', 'distance', 1000, 'distance1000.png')

ach11 = ac.Achievement('First steps', 'time', 10, 'time10.png')
ach12 = ac.Achievement('1 day on ride', 'time', 24, 'time24.png')
ach13 = ac.Achievement('2 days trip', 'time', 48, 'time48.png')
ach14 = ac.Achievement('Veteran', 'time', 100, 'time100.png')

achievement_list = [
    ach1, ach2, ach3, ach4, ach5,
    ach6, ach7, ach8, ach9, ach10,
    ach11, ach12, ach13, ach14
]

for elem in achievement_list:
    elem.img_achieved = 'achievements/images/' + elem.img_achieved

speed = 120
time = 24
distance = 100


def home(request):
    for achievement in achievement_list:
        achievement.check_if_achieved(speed, time, distance)

    achieved_list = [x for x in achievement_list if x.achieved is True]
    no_achieved = [x for x in achievement_list if x.achieved is False]

    context = {
        'achievements': achievement_list,
        'achieved_list': achieved_list,
        'no_achieved': no_achieved
    }

    return render(request, 'achievements/home.html', context)


def achieved(request):
    for achievement in achievement_list:
        achievement.check_if_achieved(speed, time, distance)

    achieved_list = [x for x in achievement_list if x.achieved is True]
    no_achieved = [x for x in achievement_list if x.achieved is False]

    context = {
        'achievements': achievement_list,
        'achieved_list': achieved_list,
        'no_achieved': no_achieved
    }

    return render(request, 'achievements/achieved.html', context)


def not_achieved(request):
    for achievement in achievement_list:
        achievement.check_if_achieved(speed, time, distance)

    achieved_list = [x for x in achievement_list if x.achieved is True]
    no_achieved = [x for x in achievement_list if x.achieved is False]

    context = {
        'achievements': achievement_list,
        'achieved_list': achieved_list,
        'no_achieved': no_achieved
    }

    return render(request, 'achievements/not_achieved.html', context)


