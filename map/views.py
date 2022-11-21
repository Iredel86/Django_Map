from django.shortcuts import render, redirect
import folium
import geocoder
from .models import Search
from .forms import SearchForm
from django.http import HttpResponse



# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your address input is invalid')
    # Create map
    m = folium.Map(location=[19,-12],zoom_start=2)
    folium.Marker([lat, lng],tooltip='Click for more',popup=country).add_to(m)
    # HTML represantion of map objects
    m = m._repr_html_()
    context = {
        'm': m,
        'form':form,
    }
    return render(request,'index.html', context)
