from django.db import models
from django.db.models.fields import TextField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class ClientopinionModel(models.Model):    
    name                                = models.CharField(max_length=40,verbose_name = "Client name",blank=True)
    company                             = models.CharField(max_length=40,verbose_name = "Şirket",blank=True)
    title                               = models.CharField(max_length=40,verbose_name = "Başlık",blank=True)
    decription                          = models.TextField(max_length=400,verbose_name="Açıklama")
    image                               = models.ImageField(verbose_name='client  "148x148"',blank=False, null=True)


    def __str__(self):
        return '%s %s' % (self.title,self.id)

    
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/dictionary/detail/{str}/".format(str=self.slug)
        except:
            return "/dictionary/detail/{str}/".format(str=self.title.lower().replace('-',' '))

    class Meta:
        ordering = ['id']
        verbose_name = 'Yorum'
        verbose_name_plural = 'yorumlar'



class TeamModel(models.Model):    
    title                           = models.CharField(max_length=40,verbose_name = "İsim",blank=True)
    small                           = models.CharField(max_length=40,verbose_name = "light text",blank=True)    
    image                           = models.ImageField(verbose_name='ana resim "476x595"',blank=False, null=True)



    def __str__(self):
        return '%s %s' % (self.title,self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


        
class ClientsModel(models.Model):    
    title                           = models.CharField(max_length=40,verbose_name = "İsim",blank=True) 
    image                           = models.ImageField(verbose_name='ana resim "225x110"',blank=False, null=True)



    def __str__(self):
        return '%s %s' % (self.title,self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

        

class PortfolioCatModel(models.Model):    
    title                           = models.CharField(max_length=40,verbose_name = "İsim",blank=True) 
    slug                            = models.SlugField(blank=True, null=True,verbose_name='uzantı',max_length=500)


    def __str__(self):
        return '%s %s' % (self.title,self.id)

    def save(self, *args, **kwargs):

        slug =  slugify(self.title)
        self.slug = slug

        return super(PortfolioCatModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']
        verbose_name = 'portfolyo kategöri'
        verbose_name_plural = 'portfolyo kategöriler'


class PortfolioModel(models.Model):    
    portfolyo                       = models.ForeignKey(PortfolioCatModel, related_name='portfoliocatmodelinline', on_delete=models.CASCADE,blank=True, null=True)
    title                           = models.CharField(max_length=40,verbose_name = "İsim",blank=True)
    small                           = models.CharField(max_length=40,verbose_name = "light text",blank=True)    
    image                           = models.ImageField(verbose_name='ana resim ',blank=False, null=True)



    def __str__(self):
        return '%s %s' % (self.title,self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'portfolyo'
        verbose_name_plural = 'portfolyolar'