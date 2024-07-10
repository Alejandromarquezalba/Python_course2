from django.shortcuts import render
from .forms import *
from Applic.models import *

def Home(request):

    content1 = Client.objects.all()
    content2 =  Market.objects.all()
    content3 = Worker.objects.all()
    content = {
                'content1':content1,
                'content2':content2,
                'content3':content3
               }
    
    return render(
        request, 
        'Applic/index.html', content)


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

def Form (request):
    if request.method== 'POST':
        form = classForm(request.POST)
        if form.is_valid():
            data_money = form.cleaned_data.get('money'),
            data_product = form.cleaned_data.get('product')
            form_save = Client(money=data_money, product=data_product)
            form_save.save()
            
            return render(request, 'Applic/Form.html')
    else:
        form = classForm()
    
    return render(request, 'Applic/Form.html', {'form':form})


def Form2 (request):
    if request.method== 'POST':
        form2 = classForm2(request.POST)
        if form2.is_valid():
            data_money2 = form2.cleaned_data.get('money'),
            data_client = form2.cleaned_data.get('client')
            form_save = Market(money=data_money2, client=data_client)
            form_save.save()
            
            return render(request, 'Applic/Form.html')
    else:
        form2 = classForm2()
    
    return render(request, 'Applic/Form.html', {'form':form2})


def Form3 (request):
    if request.method== 'POST':
        form3 = classForm3(request.POST)
        if form3.is_valid():
            data_pay = form3.cleaned_data.get('pay'),
            data_hours = form3.cleaned_data.get('hours')
            form_save = Worker(pay=data_pay, hours=data_hours)
            form_save.save()
            
            return render(request, 'Applic/Form.html')
    else:
        form3 = classForm3()
    
    return render(request, 'Applic/Form.html', {'form':form3})


def Search (request):
    return render(request, 'Applic/search.html')

def Find(request):
    query = request.GET.get('search_term', '')    
    clients = Client.objects.filter(money__icontains=query) | Client.objects.filter(product__icontains=query)
    markets = Market.objects.filter(money__icontains=query) | Market.objects.filter(client__icontains=query)
    workers = Worker.objects.filter(pay__icontains=query) | Worker.objects.filter(hours__icontains=query)
    context = {
               'content1':clients,
               'content2':markets,
               'content3':workers,
               'query':query
              }
    
    return render(request, 'Applic/index.html', context)
    
