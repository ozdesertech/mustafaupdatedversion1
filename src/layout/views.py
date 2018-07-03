""" Views for the layout application """

from django.shortcuts import render, render_to_response, HttpResponseRedirect
from .models import ProductTbl
import django


def mustafa(request):
    prodctlist = ProductTbl.objects.all()
    """ Default view for the root """
    djangoversion = django.get_version()
    return render(request, 'layout/home.html',{'djangoversion':djangoversion,'prodctlist':prodctlist  })

def profile(request):
    return  render(request, "user/profile.html" )
