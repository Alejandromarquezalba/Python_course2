from django.shortcuts import render, redirect
from .forms import *
from Applic.models import *

def Home(request):

    content1 = Client.objects.all()
    content2 =  Market.objects.all()
    content3 = Worker.objects.all()
    content = {
                'content1':content1,
                'content2':content2,
                'content3':content3,
                'query':''
               }
    
    return render(request, 'Applic/index.html', content)


#def Home2(request):
#    content2 = {'market': Market.objects.all()}
#    return render(request, 'Applic/index.html', content2)
#def Home3(request):
#    content3 = {'worker': Worker.objects.all()}
#    return render(request, 'Applic/index.html', content3)


def Acerca(request):
    return render(request, 'Applic/acerca.html')
    
def Contacto(request):
    return render(request, 'Applic/contacto.html')

def Form(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        market_form = MarketForm(request.POST)
        worker_form = WorkerForm(request.POST)
        
        if client_form.is_valid():
            Client.objects.create(**client_form.cleaned_data)
            return redirect('home')
        elif market_form.is_valid():
            Market.objects.create(**market_form.cleaned_data)
            return redirect('home')
        elif worker_form.is_valid():
            Worker.objects.create(**worker_form.cleaned_data)
            return redirect('home')
    else:
        client_form = ClientForm()
        market_form = MarketForm()
        worker_form = WorkerForm()
    
    return render(request, 'Applic/form.html', {
        'form': client_form,
        'form2': market_form,
        'form3': worker_form
    })


def Search (request):
    return render(request, 'Applic/search.html')

def Find(request):
    query = request.GET.get('search_term', '')
    clients = Client.objects.filter(money__icontains=query) | Client.objects.filter(product__icontains=query)
    markets = Market.objects.filter(money__icontains=query) | Market.objects.filter(client__icontains=query)
    workers = Worker.objects.filter(pay__icontains=query) | Worker.objects.filter(hours__icontains=query)
    
    context = {
        'clients': clients,
        'markets': markets,
        'workers': workers,
        'query': query
    }

    return render(request, 'Applic/index.html', context)
    
