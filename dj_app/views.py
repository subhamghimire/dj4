from django.shortcuts import render

# Create your views here.
def help(request):
    helpdict = {'hkey':'Hello robot!'}
    return render(request,'help.html',context=helpdict)
