from django.views import View
from django.shortcuts import render
from django.views import generic
from .models import Frame


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {"post": first_post, "bikes_index": title}
        return render(request, "shop/index.html", context=context)
    # We can also pass the value of the model with object_model.field as the context:


my_favorite_frame = Frame(color='Purple', quantity=15)
context = {'frame': my_favorite_frame}


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'frames'


#def get_queryset(self):
#    return Frame.


#def index(request):
#    bikes_list = Bike.objects.order_by("name")
#    context = {"post": first_post, "bikes_index": bikes_list[0]}
#    return render(request, "shop/index.html", context)
