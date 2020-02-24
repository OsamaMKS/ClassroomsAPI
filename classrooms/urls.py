
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classesapp import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [

    path('admin/', admin.site.urls),

    path('classrooms/list/', views.ClassroomListAPIView.as_view(), name='api-classroom-list'),
    path('classrooms/detail/<int:classroom_id>/', views.ClassroomDetailAPIView.as_view(), name='api-classroom-detail'),
    path('classrooms/create/', views.ClassroomCreateAPIView.as_view(), name='api-classroom-create'),
    path('classrooms/update/<int:classroom_id>/', views.ClassroomUpdateView.as_view(), name='api-classroom-update'),
    path('classrooms/delete/<int:classroom_id>/', views.ClassroomDeleteView.as_view(), name='api-classroom-delete'),

    path('user/login/', TokenObtainPairView.as_view(), name="api-login"),
    path('user/register/', views.ClassroomCreateAPIView.as_view(), name="api-register"),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
