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
            # new_u = Uzsakymai(uzsakyta=request.POST.get('uzsak'))
            checked = request.POST.getlist('checkbox')
            # pažiūrėti ar in checked yra geriausias var, gal visus id ir žiūrėti kurie checked
            print(request.POST)
            for item in Uzsakymai.objects.all():
                print(item.id)
                if str(item.id) in checked:
                    id = int(item.id)
                    list = Uzsakymai.objects.get(id=id)
                    if list:
                        print(list)
                        list.uzsakyta = True
                    list.save()
                else:
                    id = int(item.id)
                    list = Uzsakymai.objects.get(id=id)
                    list.uzsakyta = False
                    list.save()
            x = Uzsakymai.objects.all()
            return render(request, self.template_name, {'x': x})
        