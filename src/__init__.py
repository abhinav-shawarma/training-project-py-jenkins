import sys
import getopt
from modules.usage import Usage

if __name__=="__main__":
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "cdm")
    if len(opts) == 0:
        # no options provided, displaying all info
        print(Usage.get_cpu_usage())
        print(Usage.get_disk_usage())
        print(Usage.get_memory_usage())
    for opt, arg in opts:
        if opt in ['-c']:
            print(Usage.get_cpu_usage())
        if opt in ['-d']:
            print(Usage.get_disk_usage())
        if opt in ['-m']:
            print(Usage.get_memory_usage())