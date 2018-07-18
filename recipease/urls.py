from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('recipe.urls')),
    path('useraccount/', include('useraccount.urls')),
    path('premium/', include('premium.urls')),
    path('admin/', admin.site.urls),
]
