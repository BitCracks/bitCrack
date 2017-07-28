from datetime import datetime

def timeConvert(unix_timestamp):
    utc_time = datetime.utcfromtimestamp(unix_timestamp)
 #   return utc_time.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")
    return utc_time.strftime("%Y-%m-%d %H:%M:%S")
