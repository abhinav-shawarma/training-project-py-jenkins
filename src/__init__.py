import sys
import getopt
from modules.usage import Usage

usage_info = """Usage: [-c CPU Usage] [-m Memory Usage] [-d Disk Usage]"""

if __name__=="__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "cdm")
    except getopt.GetoptError:
        print("Invalid Option!")
        print(usage_info)
        exit(0)
    if len(opts) == 0:
        print("Provide an option!")
        print(usage_info)
    for opt, arg in opts:
        if opt in ['-c']:
            print(Usage.get_cpu_usage())
        if opt in ['-d']:
            print(Usage.get_disk_usage())
        if opt in ['-m']:
            print(Usage.get_memory_usage())