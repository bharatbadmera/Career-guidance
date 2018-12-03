from django.conf.urls import url,include
from django.contrib import admin
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ourpage/',include('ourpage.urls')),
    #url(r'^about/',views.about),
    #url(r'^$',views.homepage),
    #url(r'^Register/',views.Register),
    #url(r'^Register2/',views.Register2),
    url(r'^Resister/',include('Resister.urls')),
    url(r'^Resister2/',include('Resister2.urls')),
    url(r'^table/',include('table.urls')),

]

urlpatterns += staticfiles_urlpatterns()
