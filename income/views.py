from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Income

def index(request):
    incomes_list = Income.objects.all().order_by('date')
    paginator = Paginator(incomes_list, 10)  # Show 10 records per page
    page_number = request.GET.get('page')
    incomes = paginator.get_page(page_number)
    return render(request, 'income/index.html', {'incomes': incomes})