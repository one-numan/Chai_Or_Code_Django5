from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.


def all_chai(request):
    chais = ChaiVarity.objects.all()
    context = {
        'chais': chais
    }
    return render(request, 'chai/all_chai.html', context=context)


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    print('Function Calling')
    return render(request, 'chai/chai_detail.html', {'chai': chai})
