from psutil import users

from datetime import datetime, timezone

def user():
    started = lambda x: datetime.fromtimestamp(int(x), timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    l = lambda x: {'name': x.name, 'terminal': x.terminal, 'host': x.host, 'started': started(x.started), 'pid': x.pid}
    return [l(x) for x in users()]