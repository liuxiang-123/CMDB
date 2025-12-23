from django.db import models

class AssetServer(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=128)
    os = models.CharField(max_length=255)
    cpu_model = models.CharField(max_length=255)

    mem_total_mb = models.IntegerField()
    mem_used_mb = models.IntegerField()
    mem_free_mb = models.IntegerField()

    disk_total = models.CharField(max_length=32)
    disk_used = models.CharField(max_length=32)
    disk_avail = models.CharField(max_length=32)
    disk_use_percent = models.CharField(max_length=16)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip}({self.hostname})"

# Create your models here.
