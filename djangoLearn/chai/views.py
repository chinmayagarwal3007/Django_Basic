from django.shortcuts import render
from .models import ChaiVarity,ChaiReview,Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    print(chais)
    return render(request, 'chai/all_chai.html', {'chais':chais})
def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    review = ChaiReview.objects.filter(chai = chai)
    print(chai, review)
    return render(request, "chai/chai_detail.html", {'chai':chai, 'review':review})
def chai_store(request):
    stores = None
    form = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties = chai_varity)
    else:
        form = ChaiVarityForm()
    return render(request, "chai/chai_stores.html", {'stores':stores, "form":form})