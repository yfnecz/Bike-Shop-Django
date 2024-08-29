from django.views import View
from django.shortcuts import render

# Create your views here.
title = "John Doe's blog"
first_post = {
    "text": "My first post",
    "theme": "Easy talk",
    "comments": [
        "My congratulations!!",
        "Looking forward to the second one",
    ],
}


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {"post": first_post, "bikes_index": title}
        return render(request, "bikeshop/index.html", context=context)


#We can also pass the value of the model with object_model.field as the context:
#from .models import Blogs
#def index(request):
#    latest_blogs_list = Blogs.objects.order_by("-publication_date")[:5]
#    context = {"latest_post_list": latest_post_list}
#    return render(request, "blog/index.html", context)