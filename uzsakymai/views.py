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
        
def list(request, id):
    list = Uzsakymai.objects.get(id=id)
    new_u = Uzsakymai(uzsakyta=request.POST.get('uzsak'))
    checked = request.POST.getlist('checkbox')
    print(uzsakyta=request.POST.get('uzsak'))
    for item in list.uzsakymai_set.all():
        if str(item.id) in checked:
            item.uzsakyta = True
        else:
            item.uzsakyta = False
        new_u.save()
       