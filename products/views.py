# products/views.py
from django.http import HttpResponse

def product_list(request):
    return HttpResponse("This is a placeholder for the product list.")

