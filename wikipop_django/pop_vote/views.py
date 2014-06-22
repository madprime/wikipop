# Create your views here.
from decimal import *
import random
from django.http import HttpResponse
from django.shortcuts import render
from .models import WPArticle

# More popular article must be more than (1 + MIN_SEP)-fold more popular,
# to avoid presenting pairs with nearly-equal popularity.
MIN_SEP = 0.5

def index(request):
    wp_articles = WPArticle.objects.all()
    wp_page1 = random.choice(wp_articles)
    wp_page2 = random.choice(wp_articles)
    while (wp_page2.mdn_pop * Decimal(1.0 + MIN_SEP) > wp_page1.mdn_pop and
           wp_page1.mdn_pop * Decimal(1.0 + MIN_SEP) > wp_page2.mdn_pop):
        wp_page2 = random.choice(wp_articles)
        
    return render(request, 'pop_vote/index.html',
                  {'wp_page1': wp_page1,
                   'wp_page2': wp_page2})
