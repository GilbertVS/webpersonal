from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Título")
    description = models.TextField(
                            verbose_name="Descripción")
    image = models.ImageField(upload_to="projects",
            verbose_name="Imagen")
    link = models.URLField(null=True, blank=True,
                               verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyecto"
        ordering = ["-created"] 
    
    def __str__(self):
        return self.title
        
        
class Curssos(models.Model):
    codi_curs = models.CharField(max_length=8,
                                 verbose_name="codi")
    nom = models.CharField(max_length=20,
                           verbose_name="curs")
    estat = models.IntegerField(verbose_name="estat")
    data_inici = models.DateField(auto_now_add=True,
                                  verbose_name="Data d'inici")
    data_fi = models.DateField(auto_now=True,
                               verbose_name="Data final")
    hores = models.IntegerField(verbose_name="hores")
    class Meta:
        verbose_name = "curssos"
        verbose_name_plural = "curssos"
    
    def __str__(self):
        return self.nom 

class Inscripcions(models.Model):
    codi_curs = models.ForeignKey(Curssos, on_delete=models.CASCADE)
    ordre = models.IntegerField(verbose_name="ordre")
    nom = models.CharField(max_length=20,
                           verbose_name="nom")
    cognoms = models.CharField(max_length=40,
                           verbose_name="cognoms")  
    dni = models.CharField(max_length=9,
                           verbose_name="dni")
    telefon = models.IntegerField(verbose_name="telefon")
    correu = models.CharField(max_length=20,
                                  verbose_name="correu")
    sexe = models.CharField(max_length=10,
                               verbose_name="sexe")
    edat = models.IntegerField(verbose_name="edat")
    class Meta:
        verbose_name = "incripciones"
        verbose_name_plural = "incripciones"
    
    def __str__(self):
        return self.codi_curs        

        