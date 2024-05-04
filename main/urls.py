from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('next', views.next, name='next'),
    path('detail/', views.detail, name='detail'),
    path('question/', views.question_view, name='question'),
    path('detail/<int:pk>/', views.PageDetailView.as_view(), name='page-detail'),
    path('detail/<int:pk>/update', views.PageUpdateView.as_view(), name='page-update'),
    path('detail/<int:pk>/delete', views.PageDeleteView.as_view(), name='page-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
