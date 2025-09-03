from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406425930',
        'name': 'Haris Azzahra Lunaaya',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)