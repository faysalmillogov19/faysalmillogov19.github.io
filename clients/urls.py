from django.contrib import admin
from django.urls import path,include,re_path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'list/',views.index, name='clientList'),
    re_path(r'form/(?P<id>\d+)/',views.form, name='clientForm'),
    re_path(r'save',views.Manageclient, name='clientSave'),
    re_path(r'del/(?P<id>\d+)/',views.delete, name='clientDel'),
    re_path(r'export',views.export, name='clientexport'),
    re_path(r'/import',views.importer, name='clientimport'),
    re_path(r'/statSex',views.stat_sex, name='statSex'),
    re_path(r'/statAge',views.stat_age, name='statAge'),

]
