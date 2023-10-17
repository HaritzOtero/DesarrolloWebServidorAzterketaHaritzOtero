from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Etxea, Pertsona

def index(request):
    etxeak = Etxea.objects.all
    return render(request, 'index.html', {'etxeak': etxeak})

def pertsonak(request):
    pertsonak = Pertsona.objects.all
    return render(request, 'pertsonak.html', {'pertsonak': pertsonak})
# Create your views here.

def deleteEtxea(request, id):
    ezabatzekopost = Etxea.objects.get(id = id) #izenburua pasatu eta bilatu izenburu hori duen objetua
    Etxea.delete(ezabatzekopost) #ezabatu

    return HttpResponseRedirect(reverse(index))

def aldatu(request, id):
    etxeaAldatu = Etxea.objects.get(id=id) 
    pertsonak = Pertsona.objects.all()  # Agrega los paréntesis para obtener todos los autores
    return render(request, 'update.html', {'etxea': etxeaAldatu, 'pertsonak': pertsonak})

def aldatuEtxea(request, id):

        aldatzekoEtxea = Etxea.objects.get(id = id) #izenburua pasatu eta bilatu izenburu hori duen objetua
        

        izena = request.POST["izena"]
        herria = request.POST["herria"]
        pertsonaKop  = request.POST["pertsonaKop"]
        pertsona = request.POST["pertsona"]
        pertsonaberria = Pertsona.objects.get(id = pertsona)

        aldatzekoEtxea.izena = izena
        aldatzekoEtxea.herria = herria
        aldatzekoEtxea.pertsonaKop = pertsonaKop
        aldatzekoEtxea.pertsona = pertsonaberria
        aldatzekoEtxea.save()
        
        return HttpResponseRedirect(reverse(index))

def aldatuPertsona(request, id):
    pertsonaldatu = Pertsona.objects.get(id=id) 
    return render(request,'aldatuPertsona.html', {'pertsona': pertsonaldatu})

def aldatuPertsonaEtxea(request, id):
    izena = request.POST["izena"]
    gmail = request.POST["gmail"]
    nan = request.POST["nan"]
    lehengoAutorea = Pertsona.objects.get(id=id)
    lehengoAutorea.delete()
    autoreberria = Pertsona(izena = izena, gmail=gmail, nan = nan)
    autoreberria.save()

    return HttpResponseRedirect(reverse(pertsonak))

def deletePertsona(request, id):
    ezabatzekopertsona = Pertsona.objects.get(id = id) #izenburua pasatu eta bilatu izenburu hori duen objetua
    Pertsona.delete(ezabatzekopertsona) #ezabatu

    return HttpResponseRedirect(reverse(pertsonak))

def add(request):
    pertsonak = Pertsona.objects.all
    return render(request, 'add.html', {'pertsonak': pertsonak})

def addEtxea(request):
    pertsonaid = request.POST["pertsona"]
    izena = request.POST["izena"]
    herria = request.POST["herria"]
    pertsonaKop = request.POST["pertsonaKop"]
    pertsona = Pertsona.objects.get(id=pertsonaid)

    etxeberria = Etxea(izena = izena, herria=herria, pertsonaKop = pertsonaKop, pertsona = pertsona)
    etxeberria.save()

    return HttpResponseRedirect(reverse(index))

def addPertsona(request):
     return render(request, 'addPertsona.html')

def addEtxeaPertsona(request):
    izena = request.POST["izena"]
    gmail = request.POST["gmail"]
    nan = request.POST["nan"]

    pertsonaberria = Pertsona(izena = izena, gmail=gmail, nan = nan)

    pertsonaberria.save()

    return HttpResponseRedirect(reverse(pertsonak))