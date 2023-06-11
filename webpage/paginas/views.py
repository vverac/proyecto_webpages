from django.shortcuts import render

# Create your views here.
def index_estatico(request):
  return render(request, 'paginas/landing.html')