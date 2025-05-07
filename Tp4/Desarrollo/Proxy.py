import os

class Ping:
    def execute(self, ip):
        if ip.startswith("192."):
            print(f"Haciendo ping a {ip} con control de IP (192.*)")
            os.system(f"ping -n 2 {ip}")  # en Linux usá -c
        else:
            print("Dirección IP inválida para método 'execute'. Debe comenzar con '192.'")

    def executefree(self, ip):
        print(f"Haciendo ping libre a {ip}")
        os.system(f"ping -n 2 {ip}")  # en Linux usá -c


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)


# MAIN
if __name__ == "__main__":
    proxy = PingProxy()
    print("CASO 1: IP válida con '192.'")
    proxy.execute("192.168.1.10")

    print("\nCASO 2: IP especial 192.168.0.254 → redirige a Google")
    proxy.execute("192.168.0.254")

    print("\nCASO 3: IP no válida")
    proxy.execute("10.0.0.1")
