from django.shortcuts import render, redirect
from django.views import View
from .models import Uzsakymai

# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VisiUzsakymai(View):
    model = Uzsakymai
    template_name = 'uzsakymai.html'

    def get(self, request):
        x = Uzsakymai.objects.all()
        return render(request, self.template_name, {'x': x})
    
    def post(self, request, *args, **kwargs):
        new = Uzsakymai(dalis=request.POST.get('new'))
        new.save()
        x = Uzsakymai.objects.all()
        return render(request, self.template_name, {'x': x})
        
# nereikalinga, bet netrinti
def list(request, id):
    list = Uzsakymai.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)

    if request.POST.get('add'):
        text = request.POST.get('new')
        if len(text) > 0:
            list.uzsakymai_set.create(text=text, uzsakyta=False)
        else:
            print("Detales pavadinimas per trumpas")
    else:
        context = {"title":f"{list.title}","items": list.uzsakymai_set.all() }
        return render(request, 'uzsakymai.html', context=context)
