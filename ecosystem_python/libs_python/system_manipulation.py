# 7. Manipulação de Sistemas

# psutil (Monitoramento)
import psutil

print(psutil.cpu_percent())

# fabric (Automação remota)
from fabric import Connection

result = Connection("web.server.net").run("uptime")
