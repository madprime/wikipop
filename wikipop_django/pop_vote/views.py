# Create your views here.
from decimal import *
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import WPArticle

# More popular article must be more than (1 + MIN_SEP)-fold more popular,
# to avoid presenting pairs with nearly-equal popularity.
MIN_SEP = 0.5

class IndexView(generic.TemplateView):
    template = 'pop_vote/index.html'

    def get(self, request, *args, **kwargs):
        num_articles = WPArticle.objects.count()
        wp_page1 = WPArticle.objects.get(pk=random.randint(1,num_articles))
        wp_page2 = WPArticle.objects.get(pk=random.randint(1,num_articles))
        while (wp_page2.mdn_pop * Decimal(1.0 + MIN_SEP) > wp_page1.mdn_pop and
               wp_page1.mdn_pop * Decimal(1.0 + MIN_SEP) > wp_page2.mdn_pop):
            wp_page2 = WPArticle.objects.get(pk=random.randint(1,num_articles))

        return render(request, 'pop_vote/index.html',
                      {'wp_page1': wp_page1,
                       'wp_page2': wp_page2})

    def post(self, request, *args, **kwargs):
        wp_page1 = WPArticle.objects.get(title=request.POST['wp_page1'])
        wp_page2 = WPArticle.objects.get(title=request.POST['wp_page2'])

        is_correct = False
        if ((request.POST['pop_vote'] == request.POST['wp_page1'] and
             wp_page1.mdn_pop > wp_page2.mdn_pop) or
            (request.POST['pop_vote'] == request.POST['wp_page2'] and
             wp_page2.mdn_pop > wp_page1.mdn_pop)):
            is_correct = True

        return render(request, 'pop_vote/result.html',
                      {'wp_page1': wp_page1,
                       'wp_page2': wp_page2,
                       'is_correct': is_correct})
