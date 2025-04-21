from django.contrib import admin
from django.urls import path
from tasks.views import kanban

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kanban, name='kanban'),
]