from psutil import disk_partitions, disk_usage

from src.utils.convertutils import byte_to_gb

def disk():
    
    def partitions():
        l = lambda x: {'device': x.device, 'mountpoint': x.mountpoint, 'fstype': x.fstype}
        return [l(x) for x in disk_partitions()]

    def usage():
        usage = disk_usage('/')
        return {
            'total_GB': byte_to_gb(usage.total),
            'percent': usage.percent,
            'used_GB': byte_to_gb(usage.used),
            'free_GB': byte_to_gb(usage.free)
        }

    return {
        'partitions': partitions(),
        'usage': usage()
    }