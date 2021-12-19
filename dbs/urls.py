from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',view.index,name='index'),
    path('',include('project.urls')),
    path('/admin',views.admin,name='admin')
    # path('results/',view.results,name='results'),
    # path('results2/',view.results2,name='results2')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)