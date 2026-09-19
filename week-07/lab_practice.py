def monitor_service(server, port):
    print(f"Monitoring Server: {server} on port: {port}")
monitor_service("auth-srv", 80)
monitor_service("db-master", 5432)






