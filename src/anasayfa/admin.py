from django.contrib import admin

from .models import ClientopinionModel,TeamModel,ClientsModel,PortfolioCatModel,PortfolioModel


# Register your models here.

admin.site.register(ClientopinionModel)
admin.site.register(TeamModel)
admin.site.register(ClientsModel)
admin.site.register(PortfolioCatModel)
admin.site.register(PortfolioModel)
