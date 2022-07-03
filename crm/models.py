from datetime import datetime
from django.db import models
from django.urls import reverse

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    address = models.TextField()
    gst_no = models.CharField(max_length=15)
    frequency_of_automated_reminder = models.IntegerField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("home")
        # return reverse("customer-info")

    def __str__(self) -> str:
        return f'{self.full_name}'
    
class Communication(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    comm_detail = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now) 

    def __str__(self) -> str:
        return f'{self.customer} Communications {self.timestamp}'

    def get_absolute_url(self):
        return reverse('customer-communication', kwargs={'pk': self.customer.pk})

# storing sent email
class SentEmail(models.Model):
    sender = models.EmailField(default='jakeperaltab90@gmail.com')
    receiver = models.EmailField()
    subject = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.sender} to {self.receiver} subject: {self.subject}'