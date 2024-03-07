from django.contrib import admin
from django.urls import path
from rest_framework import routers
from Ifood.views import UserView ,  LoginUserView, RegisterUserView

"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'labs', LabViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'reservation', ReservationViewSet)
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('user/<int:id>', UserView.as_view(), name='user')
]

#urlpatterns += router.urls