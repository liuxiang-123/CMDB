from django.db import models

class AssetServer(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=128, blank=True, default="")
    os = models.CharField(max_length=255, blank=True, default="")
    cpu_model = models.CharField(max_length=255, blank=True, default="")

    mem_total_mb = models.IntegerField(null=True, blank=True)
    mem_used_mb = models.IntegerField(null=True, blank=True)
    mem_free_mb = models.IntegerField(null=True, blank=True)

    disk_total = models.CharField(max_length=32, blank=True, default="")
    disk_used = models.CharField(max_length=32, blank=True, default="")
    disk_avail = models.CharField(max_length=32, blank=True, default="")
    disk_use_percent = models.CharField(max_length=16, blank=True, default="")

    status = models.CharField(max_length=32, blank=True, default="unknown")
    last_discovered_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "asset_server"

    def __str__(self):
        return f"{self.ip}({self.hostname})"
