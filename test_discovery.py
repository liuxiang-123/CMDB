from cmdb_app.services.discovery import discover_server

res = discover_server(
    host="68.64.178.48",
    username="root",
    password="Aa.2100225612"
)

print(res)
