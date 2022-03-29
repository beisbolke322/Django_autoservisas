from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import DarbuListas, DarboDuomenys

# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VisuDarbuListai(ListView):
    model = DarbuListas
    template_name = 'home.html'

    def get_queryset(self):
        return DarbuListas.objects.all()

def list(request, id):
    list = DarbuListas.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)

    if request.POST.get('save'):
        checked = request.POST.getlist('checkbox')
        for item in list.darboduomenys_set.all():
            if str(item.id) in checked:
                item.isCompleted = True
            else:
                item.isCompleted = False
            item.save()
    elif request.POST.get('add'):
        text = request.POST.get('new')
        if len(text) > 3:
            list.darboduomenys_set.create(text=text, isCompleted=False)
        else:
            print("Užduoties tekstas per trumpas")
    elif request.POST.get('delete'):
        id_to_delete = request.POST.get('delete')
        for item in list.darboduomenys_set.all():
            if str(item.id) == id_to_delete:
                item.delete()
        return redirect('list', id=id)
    else:
        context = {"title":f"{list.title}","items": list.darboduomenys_set.all() }
        return render(request, 'darbai.html', context=context)
