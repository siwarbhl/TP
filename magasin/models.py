from django.db import models
from datetime import date

# Create your models here.

#class Produit 
class Produit (models.Model):
    TYPE_CHOICES=[
                ('em','emballé'),
                ('fr','Frais'),
                ('cs','Conserve') 
                ]
    libelle = models.CharField(max_length=100)
    description=models.TextField(default='non definie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True, upload_to='media/')
 
    categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return f"({self.libelle},{self.description} ,{self.prix},{ self.type})"

#class Categorie
class Categorie (models.Model):
    TYPE_CHOICES=[
                ('Al','Alimentaire'), ('Mb','Meuble'),
                ('Sn','Sanitaire'), ('Vs','Vaisselle'),
                ('Vt','Vêtement'),('Jx','Jouets'),
                ('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')
                ]
    
    name=models.CharField(max_length=50,default='Alimentaire')
    def __str__(self) :
        return f"({self.name})"
    
# Class Fournisseur
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    logo =models.ImageField(upload_to='media/', null=True, blank=True)


# class produit non consommable
class ProduitNC (Produit):
    Duree_garantie=models.CharField(max_length=100,default=0)  
    def __str__(self) :
        return self.Duree_garantie


# class Commande
class Commande (models.Model) :
    dateCde=models.DateField(null=True, default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self) :
       return f"({self.dateCde},{self.totalCde} )"