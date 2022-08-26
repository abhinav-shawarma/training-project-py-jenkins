import psutil

class Usage:
    def get_cpu_usage():
        perc_usage = "{0:.3f}".format(100.0 - psutil.cpu_times_percent(interval=0.4, percpu=False).idle)
        return f"CPU Usage %: {perc_usage}"

    def get_memory_usage():
        virtual_mem = psutil.virtual_memory()
        return f"""Memory Usage
Available: {virtual_mem.available >> 30}GB
Used     : {virtual_mem.used >> 30}GB
Total    : {virtual_mem.total >> 30}GB"""
        
    def get_disk_usage():
        du = psutil.disk_usage('/')
        return f"""Disk Usage
Free : {du.free >> 30}GB
Used : {du.used >> 30}GB
Total: {du.total >> 30}GB"""
