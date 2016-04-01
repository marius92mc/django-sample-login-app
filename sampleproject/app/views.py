from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import MyUser, Currency, CurrencyPair 
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/") #if login/, it appends to current URL
def home(request):
    currencies = Currency.objects.all()
    context = {
                'currencies': currencies, 
            }
    return render(request, 
                  'app/index.html', 
                  context)

TRADER = 0
CENTRAL_BANK = 1

def populate():
    user1 = MyUser(username="user1", \
                 email="a@b.com", \
                 password="password")
    user1.save()
    user2 = MyUser(username="trader", \
                   email="trader@traderion.com", \
                   password="trader", \
                   type=TRADER)
    user2.save()
    user3 = MyUser(username="cb", \
                   email="cd@traderion.com", \
                   password="cb", \
                   type=CENTRAL_BANK)
    user3.save()
    
    currency1 = Currency(name="EUR", \
                         country="Germany")
    currency1.save()
    currency2 = Currency(name="USD", \
                         country="USA")
    currency2.save()
    currency3 = Currency(name="CHF", country="Switzerland")
    currency3.save()
    currency4 = Currency(name="CAD", country="Canada")
    currency4.save()
    currency5 = Currency(name="NOK", country="Norway")
    currency5.save()
    currency6 = Currency(name="JPY", country="Japan")
    currency6.save()

