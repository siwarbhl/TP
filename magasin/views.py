from django.shortcuts import redirect, render , get_object_or_404
from .models import Produit
from .models import Fournisseur
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def index(request):
        products=Produit.objects.all()
        return render(request,'magasin/Produits/mesProduits.html',{'products':products})


def ListFournisseur(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/Fournisseurs/fournisseur.html', context)

def nouveauFournisseur(request):
    if request.method == "POST" :
         form = FournisseurForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              nouvFournisseur=Fournisseur.objects.all()
              return render(request,'magasin/Fournisseurs/fournisseur.html',{'nouvFournisseur':nouvFournisseur})
    else : 
            form = FournisseurForm() #créer formulaire vide 
            nouvFournisseur=Fournisseur.objects.all()
            return render(request,'magasin/Fournisseurs/create-fournisseur.html',{'form':form,'nouvFournisseur':nouvFournisseur})


def update_Fournisseur(request, fk):
    fournisseur = get_object_or_404(Fournisseur, id=fk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES, instance=fournisseur)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            frns = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['logo']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                frns.logo= nouvelle_image
            # Sauvegarder le produit
            frns.save()
            return redirect('fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
        return render(request, 'magasin/Fournisseurs/update-fournisseur.html', {'form': form})


def delete_Fournisseur(request, fk):
    fournisseur = get_object_or_404(Fournisseur, id=fk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseurs')
    return render(request,'magasin/Fournisseurs/delete-fournisseur.html', {'fournisseur': fournisseur})

def detail_Fournisseur(request, for_id):
    fournisseur = get_object_or_404(Fournisseur, id=for_id)
    context = {'fournisseur': fournisseur}
    return render(request, 'magasin/Fournisseurs/detail-fournisseur.html', context)


def Catalogue(request):
        products= Produit.objects.all()
        context={'products':products}
        return render( request,'magasin/Produits/mesProduits.html',context )

def nouveauProduct(request):
    if request.method == "POST" :
         form = ProduitForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              nouvProduct=Produit.objects.all()
              return render(request,'magasin/Produits/mesProduits.html',{'nouvProduct':nouvProduct})
    else : 
            form = ProduitForm() #créer formulaire vide 
            nouvProduct=Fournisseur.objects.all()
            return render(request,'magasin/Produits/create-produit.html',{'form':form,'nouvProduct':nouvProduct})


def update_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            produit = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['img']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                produit.img = nouvelle_image
            # Sauvegarder le produit
            produit.save()
            return redirect('Catalogue')
    else:
        form = ProduitForm(instance=product)
        return render(request, 'magasin/Produits/update-produit.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Catalogue')
    return render(request, 'magasin/Produits/delete-produit.html', {'product': product})

def detail_product(request, product_id):
    produit = get_object_or_404(Produit, id=product_id)
    context = {'produit': produit}
    return render(request, 'magasin/Produits/detail-produit.html', context)



def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('home')
     else :
          form = UserCreationForm()
     return render(request,'magasin/registration/register.html',{'form' : form})


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("Catalogue")
    context = {'form':form}
    return render(request, 'magasin/registration/login.html', context=context)


def logout(request):  
    auth.logout(request)
    return redirect("login")


class ChangePasswordView(PasswordChangeView):
    template_name = 'magasin/registration/change_password.html'
    success_url = reverse_lazy('home')



