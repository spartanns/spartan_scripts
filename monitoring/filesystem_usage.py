import os


def check_filesystem_usage(path):
    usage = os.statvfs(path)
    total = usage.f_frsize * usage.f_blocks
    free = usage.f_frsize * usage.f_bfree
    used = total - free
    percent_used = (used / total) * 100
    print(f"Filesystem usage for {path}: {percent_used:.2f}%")


check_filesystem_usage("/")  # Check root filesystem
