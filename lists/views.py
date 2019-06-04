from django.shortcuts import render, redirect
from lists.models import Item
#from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # renders home.html template
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/') # always redirect a POST

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
