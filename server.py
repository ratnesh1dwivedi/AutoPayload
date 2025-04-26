import os
import shutil
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def host_payload(outfile, outformat):
    apache_dir = "/var/www/html/payloads"
    os.makedirs(apache_dir, exist_ok=True)
    src = f"{outfile}.{outformat}"
    dst = os.path.join(apache_dir, src)
    shutil.move(src, dst)

    link = f"http://{get_local_ip()}/payloads/{src}"
    print(f"[+] Payload hosted at: {link}")
