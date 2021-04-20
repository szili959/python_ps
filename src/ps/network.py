from psutil import net_io_counters, net_if_addrs, net_if_stats

from src.utils.convertutils import byte_to_mb

def network():
    
    def io():
        io_counters = net_io_counters()
        return {
            'MBs_sent': byte_to_mb(io_counters.bytes_sent),
            'MBs_received': byte_to_mb(io_counters.bytes_recv),
            'packets_sent_k': io_counters.packets_sent / 1000,
            'packets_received_k': io_counters.packets_recv / 1000,
            'error_in': io_counters.errin,
            'error_out': io_counters.errout
        }

    def addrs():
        if_addrs = net_if_addrs()
        l = lambda x: {'family': x.family, 'address': x.address, 'netmask': x.netmask, 'broadcast': x.broadcast}
        return {k : [l(x) for x in v] for (k,v) in if_addrs.items()}

    def stats():
        if_stats = net_if_stats()
        l = lambda x: {'isup': x.isup, 'duplex': x.duplex, 'speed': x.speed, 'mtu': x.mtu}
        return {k : l(v)  for (k,v) in if_stats.items()}

    return {
        'io': io(),
        #'addrs': addrs(),
        #'stats': stats()
    }