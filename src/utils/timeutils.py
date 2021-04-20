def from_secs(secs: int):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return (h, m, s)

def from_secs_str(secs: int) -> str:
    (h, m, s) = from_secs(secs)
    result = f'{h:d}:{m:02d}:{s:02d}'
    return result

def from_secs_to_minutes(secs: int):
    m, s = divmod(secs, 60)
    return m if s < 30 else m + 1