from django.shortcuts import render, redirect
from django.views import View
from .models import DarbuListas, DarboDuomenys
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VisuDarbuListai(View,LoginRequiredMixin):
    template_name = 'home.html'

    def get(self, request):
        x = DarbuListas.objects.filter(user=self.request.user)
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

def ppong(request):
    return render(request, 'ping_pong.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(request.POST)
        if form.is_valid():
            print('veikia')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                print('veikia')
                return redirect('uzsakymai/')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Jūs sėkmingai atsijungėte.") 
	return redirect("uzsakymai")