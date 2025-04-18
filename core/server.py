import os

def host_payload(outfile, outformat):
    print(f"[+] Hosting payload at http://0.0.0.0:8080/{outfile}.{outformat}")
    os.system(f"python3 -m http.server 8080")
