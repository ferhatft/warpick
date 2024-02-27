from django.shortcuts import render

# Create your views here.
from .models import ClientopinionModel,TeamModel,ClientsModel,PortfolioCatModel,PortfolioModel

def anasayfa(request):
    clientsmodel        = ClientsModel.objects.all()
    teammodel           = TeamModel.objects.all()
    clien_opinion       = ClientopinionModel.objects.all()
            
    context = {
        'clien_opinion':clien_opinion,
        'clientsmodel':clientsmodel,
        'teammodel':teammodel,
    }
    return render(request, "index.html", context)



def neyapıyoruz(request):
    
    clien_opinion = ClientopinionModel.objects.all()
    
   
    
    context = {
        'clien_opinion' :clien_opinion,
    }
    return render(request, "neyapıyoruz.html", context)

    
def bizkimiz(request):
    
    clien_opinion = ClientopinionModel.objects.all()
    
   
    
    context = {
        'clien_opinion' :clien_opinion,
    }
    return render(request, "bizkimiz.html", context)


def portfolyo(request):
    portfolyocat    = PortfolioCatModel.objects.all()
    portfolyo       = PortfolioModel.objects.all()
    
   
    
    context = {
        'portfolyocat' :portfolyocat,
        'portfolyo' :portfolyo,
    }
    return render(request, "portfolyo.html", context)