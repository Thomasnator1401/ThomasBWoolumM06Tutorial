from django.shortcuts import render
from .models import MyModel

def my_view(request):
    my_data = MyModel.objects.all()  # Fetch data from your model
    return render(request, 'my_template.html', {'data': my_data})
