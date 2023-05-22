from django.db import models


class Client(models.Model):
    phone_number = models.CharField(max_length=12, unique=True)
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)


class Dispatch(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message = models.TextField()
    client_filter_operator_code = models.CharField(max_length=10)
    client_filter_tag = models.CharField(max_length=100)


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)