import psutil
from tabulate import tabulate


def list_processes():
    """Display a list of currently running processes."""
    process_list = []

    for proc in psutil.process_iter(attrs=["pid", "name", "username"]):
        try:
            # Add process details to the list
            process_list.append(proc.info)
        except psutil.NoSuchProcess:
            pass

    # Format and print the process list
    print(tabulate(process_list, headers="keys", tablefmt="fancy_grid"))


if __name__ == "__main__":
    print("Currently Running Processes:\n")
    list_processes()
