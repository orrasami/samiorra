from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Foto, Galeria


def index(request):
    if request.method == 'POST':
        username = request.POST["usuario"].upper()
        password = request.POST["password"]

        print(f"Usuario: {username} - Senha: {password}")

        if username == 'SAMI' and password == '0048':
            request.session['username'] = username
        else:
            messages.error(request, 'Dados Incorretos')
    context = {
        'fotos': Foto.objects.all().order_by('ordem'),
        'usuario_logado': request.session.get('username', None),
    }
    return render(request, 'index.html', context)


def galeria(request, pk):
    nome = pk
    galeria = Galeria.objects.get(galeria=nome)

    context = {
        'fotos': Foto.objects.all().order_by('ordem'),
        'galeria_id': galeria.pk,
        'galeria_nome': galeria.galeria,
        'usuario_logado': request.session.get('username', None),
    }
    return render(request, 'galeria.html', context)


def galeriarestrita(request, pk):
    nome = pk
    usuario_logado = request.session.get('username', None)
    if usuario_logado != None:
        usuario_logado = usuario_logado.upper()
    if usuario_logado == 'SAMI':
        galeria = Galeria.objects.get(galeria=nome)

        context = {
            'fotos': Foto.objects.all().order_by('ordem'),
            'galeria_id': galeria.pk,
            'galeria_nome': galeria.galeria,
            'usuario_logado': request.session.get('username', None),
        }
        return render(request, 'galeria-restrita.html', context)
    else:
        return redirect('index')


def logout(request):
    request.session['username'] = None
    return redirect('index')


def login(request):
    if request.method == 'POST':
        username = request.POST["usuario"].upper()
        password = request.POST["password"]
        if username == 'SAMI' and password == '0048':
            request.session['username'] = username
            return redirect('index')
        else:
            messages.error(request, 'Dados Incorretos')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def restrito(request):
    usuario_logado = request.session.get('username', None)
    if usuario_logado != None:
        usuario_logado = usuario_logado.upper()
    if usuario_logado == 'SAMI':
        context = {
            'fotos': Foto.objects.all().order_by('ordem'),
            'usuario_logado': request.session.get('username', 'SAMI'),
        }
        return render(request, 'restrito.html', context)
    else:
        return redirect('index')

