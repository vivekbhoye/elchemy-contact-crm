from django.urls import path

from .views import (home,CustomerListView,CustomerCreateView,CustomerUpdateView,CustomerDeleteView, 
    CustomerCommunicationListView,CommunicationUpdateView,CommunicationDeleteView,CommunicationCreateView,
    SendEmailView,
    )

urlpatterns = [
    # path('',home.as_view(),name='home'),
    path('customers/',CustomerListView.as_view(),name='home'),
    # path('customers/',CustomerListView.as_view(),name='customer-info'),
    path('customers/create/',CustomerCreateView.as_view(),name='customer-create'),
    path('customers/update/<int:pk>/',CustomerUpdateView.as_view(),name='customer-update'),
    path('customers/delete/<int:pk>/',CustomerDeleteView.as_view(),name='customer-delete'),
    # customer/communication/customer_id/
    path('customers/communication/<int:pk>/',CustomerCommunicationListView.as_view(),name='customer-communication'),
    # customer/communication/communication_id/
    path('customers/communication/update/<int:pk>/',CommunicationUpdateView.as_view(),name='communication-update'),
    path('customers/communication/delete/<int:pk>/',CommunicationDeleteView.as_view(),name='communication-delete'),
    path('customers/communication/create/',CommunicationCreateView.as_view(),name='communication-create'),
    path('customers/communication/sendemail/<int:pk>/',SendEmailView.as_view(),name='send-email'),

]
