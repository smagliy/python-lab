from django.shortcuts import render
from .models import TableHello
from .forms import TableHelloForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = TableHelloForm(request.POST)
        if form.is_valid():
            messages.info(request, f'Привіт {form.save()}')
            #form.save()
        else:
            messages.warning(request, f"Вже бачилися!!!")

    form = TableHelloForm()
    data = {
        'form': form
    }
    return render(request, 'main/index.html', data)


def table(request):
    table_hello = TableHello.objects.all()
    return render(request, 'main/table.html', {'table_hello': table_hello})
