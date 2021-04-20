from psutil import virtual_memory, swap_memory

from src.utils.convertutils import byte_to_mb

def memory():

    def vm():
        vm = virtual_memory()
        return {
            'total_MB': byte_to_mb(vm.total),
            'percent': vm.percent,
            'used_MB': byte_to_mb(vm.used),
            'free_MB': byte_to_mb(vm.free),
        }

    def swap():
        swap = swap_memory()
        return {
            'total_MB': byte_to_mb(swap.total),
            'percent_MB': swap.percent,
            'used_MB': byte_to_mb(swap.used),
            'free_MB': byte_to_mb(swap.free)
        }

    return {
        'vm': vm(),
        'swap': swap()
    }