import subprocess as S


txt = S.check_output(["netsh", "wlan", "show", "networks"])
print (txt.decode())

