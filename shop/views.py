from django.views import View
from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {"post": "Hello", "bikes_index": "Index"}
        return render(request, "shop/index.html", context=context)
    # We can also pass the value of the model with object_model.field as the context:


#my_favorite_frame = Frame(color='Purple', quantity=15)
#context = {'frame': my_favorite_frame}


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'frames'
    #def get_queryset(self):
    #    return Frame.objects.all

def list_bikes(request):
    greetings_to = 'Anonymous'
    bikes = models.Bike.objects.all
    return render(request, 'shop/bikes.html', {'bikes': bikes})

class BikeView(View):
    def get(self, request, pk, *args, **kwargs):
        id = self.kwargs['pk']
        bike = models.Bike.objects.filter(id=pk).first()
        return render(request, 'shop/bike.html', {'bike':bike})

#def index(request):
#    bikes_list = Bike.objects.order_by("name")
#    context = {"post": first_post, "bikes_index": bikes_list[0]}
#    return render(request, "shop/index.html", context)




#def main_page_view(request):
#    if request.method == "GET":
#        html =  "\n".join(f"<div>{candy}</div>" for candy in candies)
#        return HttpResponse(html)


#class CandyView(View):
#    def get(self, request, name, *args, **kwargs):
#        title = f"<h1>{name}</h1>"
#        html = "\n".join(f"<div>{attr}: {value}</div>" for attr, value in candies[name].items())
#       return HttpResponse(title + html)

#raise Http404  # or return HttpResponse(status=404)