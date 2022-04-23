from django.shortcuts import render, redirect
from django.views import View
from .models import DarbuListas, DarboDuomenys

# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VisuDarbuListai(View):
    # model = DarbuListas
    template_name = 'home.html'

    def get(self, request):
        x = DarbuListas.objects.all()
        return render(request, self.template_name, {'x': x})
    
    def post(self, request, *args, **kwargs):
        new = DarbuListas(title=request.POST.get('newT'))
        new.save()
        x = DarbuListas.objects.all()
        return render(request, self.template_name, {'x': x})


########################################### automobiliai sąraše ###########################################

def list(request, id):
    isrikiuoti_duomenys = DarboDuomenys.objects.order_by('sav')
    list = DarbuListas.objects.get(id=id)
    context = {"title":"{list.title}","items": list.darboduomenys_set.all(), 'sortedsav': isrikiuoti_duomenys}
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
        context = {"title":f"{list.title}","items": list.darboduomenys_set.all(), 'sortedsav': isrikiuoti_duomenys}
    return render(request, 'darbai.html', context=context)

