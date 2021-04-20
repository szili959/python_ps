from psutil import cpu_count, cpu_freq, cpu_percent

def cpu():
    
    def freq():
        freq = cpu_freq()
        return {
            'min_GHz': freq.min / 1000,
            'max_GHz': freq.max / 1000,
            'current_GHz': freq.current / 1000
        }

    return {
        'percent': cpu_percent(),
        #'cpu_times_percent': psutil.cpu_times_percent(),
        'count_logical': cpu_count(),
        'count': cpu_count(False),
        'freq': freq()
    }