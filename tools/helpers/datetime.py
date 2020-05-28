from datetime import datetime, timezone, timedelta

def local_time() -> datetime:
    tz = timezone(timedelta(hours=+8))

    return datetime.now(tz)
