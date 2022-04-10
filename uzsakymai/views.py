from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import UzsakymuListas, Uzsakymai

# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VisiUzsakymai(ListView):
    model = Uzsakymai
    template_name = 'uzsakymai.html'

    def get_queryset(self):
        return Uzsakymai.objects.all()

def list(request, id):
    list = Uzsakymai.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)

    if request.POST.get('add'):
        text = request.POST.get('new')
        if len(text) > 3:
            list.uzsakymai_set.create(text=text, isCompleted=False)
        else:
            print("Detales pavadinimas per trumpas")
    else:
        context = {"title":f"{list.title}","items": list.uzsakymai_set.all() }
        return render(request, 'uzsakymai.html', context=context)
