from django.shortcuts import render
from .models import Usuarios

def home(request):
    return render(request, "usuarios/home.html")

def usuarios(request):
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    novo_usuario.save()
    
    #Exibir todos usuarios cadastrados em uma nova pagina
    
    usuarios = {
        "usuarios": Usuarios.objects.all()
    }
    #retornar os dados 
    return render(request,"usuarios/usuarios.html",usuarios)