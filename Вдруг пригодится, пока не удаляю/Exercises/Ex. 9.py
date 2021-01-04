def convert_seconds_to_dhms(raw_seconds):
    seconds = raw_seconds % 60
    raw_minutes = raw_seconds // 60

    minutes = raw_minutes % 60
    raw_hours = raw_minutes // 60

    hours = raw_hours % 24
    days = raw_hours // 24

    return ':'.join((str(days), str(hours), str(minutes), str(seconds)))


print()
