from django.db import models

class ChatHistory(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class OrderData(models.Model):
    user_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    order_status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
