from psutil import boot_time
from src.utils.timeutils import from_secs_str
from datetime import datetime, timezone

def boot():
    return {
        'time': datetime.fromtimestamp(int(boot_time()), timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    }