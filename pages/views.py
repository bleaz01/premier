from django.shortcuts import render

from .forms import ContactForm

from django.http import Http404

from pages.models import Article


# def index(resqest):
 #    context ={'titre':"salut les copains",'nom': "Frank"}
  #   return render(resqest,"pages/index.html",context)
#
# def page2(resqest):
#     context ={'age':18}
#     return render(resqest,"pages/page2.html",context)
#
# def page3(resqest):
#     context ={'maliste':['franck', 'jeason', 'marie', 'lola']}
#     return render(resqest,"pages/page3.html",context)


def accueil(request):
    """affiche tous les article de notre blog"""
    articles = Article.objects.all()
    return render(request,'pages/page2.html',{'derniers_articles': articles})


def lire(request,id):
    try:
        article =Article.objects.get(id=id)
    except Article.DoesNotExist:
            raise Http404

    return render(request, 'pages/lire.html',{'article':article})




def contact(request):
    form= ContactForm(request.POST or None)
    if form.is_valid():
        sujet=form.cleaned_date['sujet']
        message=form.cleaned_data['message']
        envoyeur=form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']



        envoi =True

    return render(request,'pages/contact.html', locals())
