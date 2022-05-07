from django.shortcuts import render, redirect
from django.views import View
from .models import Uzsakymai, UzsakymuListas


class VisiUzsakymai(View):
    model = Uzsakymai
    template_name = 'uzsakymai.html'

    def get(self, request):
        x = Uzsakymai.objects.all()
        return render(request, self.template_name, {'x': x})
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('submit') == 'add':
            new = Uzsakymai(dalis=request.POST.get('new'))
            new.save()
            x = Uzsakymai.objects.all()
            return render(request, self.template_name, {'x': x})
        elif request.POST.get('submit') == 'uzsak':
            print(request.POST)

            new_u = Uzsakymai(uzsakyta=request.POST.get('uzsak'))
            checked = request.POST.getlist('checkbox')
            for id in checked:
                id = int(id)
            list = Uzsakymai.objects.get(id=id)
            print(Uzsakymai.objects.all(), "+++", id)
            for item in list.objects.all():
                if str(item.id) in checked:
                    item.uzsakyta = True
                else:
                    item.uzsakyta = False
                new_u.save()
            x = Uzsakymai.objects.all()
            print(x)
            return render(request, self.template_name, {'x': x})
        