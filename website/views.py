from django.shortcuts import render, redirect
from django.http import JsonResponse
from website.models import Auction

def index(request):
    return render(request, 'website/index.html')

def search(request):
    search = request.POST['search-input']
    pk=search
    results = Auction.objects.filter(description__icontains=search)
    print(results)
    return render(request,'website/search.html', {
        'results' : results,
    })