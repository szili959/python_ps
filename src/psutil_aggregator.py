from src.ps.cpu import cpu
from src.ps.memory import memory
from src.ps.disk import disk
from src.ps.network import network
from src.ps.battery import battery
from src.ps.boot import boot
from src.ps.users import user

def current():
    return {
        'cpu': cpu(),
        'memory': memory(),
        'disk': disk(),
        'network': network(),
        'battery': battery(),
        'boot': boot(),
        'users': user()
    }