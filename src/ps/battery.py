from psutil import sensors_battery
from src.utils.timeutils import from_secs_to_minutes
from math import inf

def battery():
    bat = sensors_battery()
    
    def minutes_left():
        value = from_secs_to_minutes(bat.secsleft)
        return inf if value == 0 else value

    return {
        'percent': bat.percent,
        'minutes_left': minutes_left(),
        'is_plugged': bat.power_plugged
    }