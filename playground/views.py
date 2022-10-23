from django.shortcuts import render


def get_uvod(request):
    return render(request, 'playground/uvod.html')


def get_projekt_logotvorba_vaclavovice(request):
    return render(request, 'playground/projekt-logotvorba-vaclavovice.html')


def get_kontakt(request):
    return render(request, 'playground/kontakt.html')




