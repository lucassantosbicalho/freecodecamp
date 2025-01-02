def next_list_element(list, element_start, increment):
    map = {list[i]: list[(i + int(increment)) % len(list)] for i in range(len(list))}
    return map[element_start]

def convert_formatted_time_to_minutes(str_time):
    # It must be on format 'HH:MM [AM|PM]'
    time = str_time.split()[0] 
    period = str_time.split()[1] if len(str_time.split()) > 1 else False
    h = time.split(':')[0] 
    m = time.split(':')[1] 
    minutes = (int(h) * 60) + int(m)
    if period == 'PM':
        minutes += 720
    return (minutes)

def get_days_added(amount):
    cycle = amount // 1440
    rest = amount - (cycle * 1440)
    return [cycle, rest]

def convert_min_to_ampm_format(hour):
    h = int(hour) // 60
    m = (int(hour) - (h * 60))
    f = f'{h}:{m:02d} AM'
    if h == 0:
        f = f'12:{m:02d} AM'
    elif h == 12:
        f = f'{h}:{m:02d} PM'
    elif h > 12:
        f = f'{h - 12}:{m:02d} PM'
    return f

def add_time(start, duration, day = None):
    # Convert the time in string format to minutes. Do some calculations. And convert it back to string format
    new_time = None
    label = ''
    day = day.capitalize() if day else ''

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    minutes_amount_from_start = convert_formatted_time_to_minutes(start) 
    minutes_amount_from_duration = convert_formatted_time_to_minutes(duration)
    amount = minutes_amount_from_start + minutes_amount_from_duration
    days_added, minutes_on_last_day_iteration = get_days_added(amount)
    
    if day and days_added > 1:
        label = f', {next_list_element(days, day, days_added)} ({days_added} days later)'
    elif day and days_added == 1:
        label = f', {next_list_element(days, day, days_added)} (next day)'
    elif day and days_added == 0:
        label = f', {day}'
    elif not day and days_added > 1:
        label = f' ({days_added} days later)'
    elif not day and days_added == 1:
        label = ' (next day)'

    new_time = convert_min_to_ampm_format(minutes_on_last_day_iteration)
    
    return f'{new_time}{label}'

if __name__ == '__main__':

    print(add_time('3:00 PM', '3:10'))
    # Returns: 6:10 PM

    print(add_time('11:30 AM', '2:32', 'Monday'))
    # Returns: 2:02 PM, Monday

    print(add_time('11:43 AM', '00:20'))
    # Returns: 12:03 PM

    print(add_time('10:10 PM', '3:30'))
    # Returns: 1:40 AM (next day)

    print(add_time('11:43 PM', '24:20', 'tueSday'))
    # Returns: 12:03 AM, Thursday (2 days later)

    print(add_time('6:30 PM', '205:12'))
    # Returns: 7:42 AM (9 days later)

    print(add_time('2:59 AM', '24:00'))
    # Returns: 2:59 AM (next day)

    print(add_time('2:59 AM', '24:00', 'saturDay'))
    # Returns: 2:59 AM, Sunday (next day)