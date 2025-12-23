import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from cmdb_app.services.discovery import discover_server, save_discovery_to_db
from cmdb_app.models import AssetServer

ip = "68.64.178.48"

res = discover_server(host=ip, username="root", password="Aa.2100225612")
print(res)

if res.get("success"):
    obj = save_discovery_to_db(ip, res["data_structured"])
    print("Saved:", obj)

print("DB count:", AssetServer.objects.count())
