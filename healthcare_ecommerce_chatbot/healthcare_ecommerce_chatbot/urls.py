from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),  # Include chatbot app URLs
    path('ecommerce/', include('ecommerce.urls')),  # Include ecommerce app URLs
]
