from django.shortcuts import render
from dj_app.models import Post
# Create your views here.
# def help(request):
#     helpdict = {'hkey':'Hello robot!'}
#     return render(request,'help.html',context=helpdict)

def help(request):
    title_list = Post.objects.order_by('text')
    date_dict = {'posts':title_list}
    return render(request,'help.html',context=date_dict)
