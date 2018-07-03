"""urlconf for the layout application"""

from django.conf.urls import url
from layout.views import mustafa


urlpatterns =[
    url(r'^$', mustafa),


]
