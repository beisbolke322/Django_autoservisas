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

    # def list(request, id):
    #     if request.method == "POST":
    #         print(request.POST)

    #         if request.POST.get('add'):
    #             title = request.POST.get('newT')
    #             if len(title) > 0:
    #                 DarbuListas.create(title=title)
    #             else:
    #                 print("Užduoties tekstas per trumpas")
    #             return redirect('list', id=id)
    #         elif request.POST.get('delete'):
    #             id_to_delete = request.POST.get('delete')
    #             for item in DarbuListas.all():
    #                 if str(item.id) == id_to_delete:
    #                     item.delete()
    #             return redirect('list', id=id)
    #     return render(request, 'darbai.html')


########################################### automobiliai sąraše ###########################################

def list(request, id):
    list = DarbuListas.objects.get(id=id)
    context = {"title":"{list.title}","items": list.darboduomenys_set.all() }
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
            marke = request.POST.get('newM')
            modelis = request.POST.get('newMo')
            sav = request.POST.get('newS')
            suged = request.POST.get('newSu')
            if len(marke) and len(modelis) and len(sav) and len(suged) > 0:
                list.darboduomenys_set.create(marke=marke, modelis=modelis, sav=sav, suged=suged, isCompleted=False)
            else:
                print("Užduoties tekstas per trumpas")
            return redirect('list', id=id)
        elif request.POST.get('delete'):
            id_to_delete = request.POST.get('delete')
            for item in list.darboduomenys_set.all():
                if str(item.id) == id_to_delete:
                    item.delete()
            return redirect('list', id=id)
    else:
        context = {"title":"{list.title}","items": list.darboduomenys_set.all() }
    return render(request, 'darbai.html', context=context)
