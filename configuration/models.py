from django.db import models

class Configuration(models.Model):
    user_identifier = models.UUIDField()
    config = models.JSONField()
    create_date = models.DateField(auto_created=True)
    update_date = models.DateField(auto_now=True)
