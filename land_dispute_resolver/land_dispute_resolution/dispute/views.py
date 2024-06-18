from django.shortcuts import render
from .models import Land, Dispute

def home(request):
    disputes = Dispute.objects.all()
    return render(request, 'dispute/home.html', {'disputes': disputes})

def land_list(request):
    lands = Land.objects.all()
    return render(request, 'dispute/land_list.html', {'lands': lands})

# Create your views here.
