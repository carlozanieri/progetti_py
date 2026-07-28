from django.shortcuts import get_object_or_404, render
from .models import Menuweb
from .models import Entries
from .models import Slider
#from Connect import Connect

def index(request):
   
    entries = Entries.objects.filter(slug='sanpiero')
    menuweb = Menuweb.objects.filter(livello=2)
    submenu = Menuweb.objects.filter(livello=3)
    slider = Slider.objects.all()[:]
    #slider = Connect.slider("", "mugello")
    context = {"entries": entries, "menuweb": menuweb, "submenu": submenu, "slider": slider}
   
    return render(request, "beb/index.html", context)


def detail(request, author_id):
    entries = get_object_or_404(Entries, pk=author_id)
    menuweb = Menuweb.objects.filter(livello=2)[:]
    context = {"entries": entries, "menuweb": menuweb}
    return render(request, "beb/detail.html", context)


def slide(request):
    luogo = request.GET.get('luogo')
    #slider = Slider.objects.all()[:]
    slider = Slider.objects.filter(codice='mugello')[:]
    #slider = Connect.slider("", "mugello")
    context = {"slider": slider, 'luogo': luogo}
    return render(request, "beb/nivo.html", context)


def menu(request):
        
    menuweb = Menuweb.objects.filter(livello=2)
    submenu = Menuweb.objects.filter(livello=3)
    context = {"menuweb": menuweb, "submenu": submenu}
    return render(request, "beb/menu5.html", context)

