import subprocess


def exec_shell(cmd: str):
    cmd = cmd.split()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = process.communicate()
    return_code = process.returncode
    return o.decode('utf-8'), e.decode('utf-8'), return_code

