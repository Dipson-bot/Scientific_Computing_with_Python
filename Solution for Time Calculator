def add_time(start, duration, day=None):

# declare variables
    start_hours = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1][:2])
    start_meridian = start.split(':')[1][3:]

    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])

    
# convert to 24 hr format
    if start_meridian == 'PM' and start_hours != 12 :
        start_hours += 12
    elif start_meridian == 'AM' and start_hours == 12 :
        start_hours = 0
    
# add duration hours and minutes
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes
    
# handle overflow of minutes
    if total_minutes >= 60:
      total_hours += 1
      total_minutes %= 60
# calculate days later
    days_later = total_hours // 24
    hours_later = total_hours % 24

# Convert back to 12 hour format
    if hours_later == 0 :
        hours_later = 12
        meridian = 'AM'
    elif hours_later < 12 :
        meridian = 'AM'
    elif hours_later == 12 :
        meridian = 'PM'
    else :
        hours_later  -= 12
        meridian = 'PM'

# Handle optional days of the week
    if day :
        days_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        day_index = days_of_the_week.index(day.capitalize())
        end_day_index = (day_index + days_later) % 7
        end_day = days_of_the_week[end_day_index]
    else :
        end_day = None

# format the final time
    formatted_time = f'{hours_later}:{total_minutes:02d} {meridian}'
    

    if end_day :
        formatted_time += f', {end_day}'

# Handle next day or days latter messages
    if days_later == 1 :
        formatted_time += ' (next day)'
    elif days_later > 1 :
        formatted_time += f' ({days_later} days later)'
# return the full y formatted time
    return formatted_time

add_time('11:43 PM', '24:20', 'tueSday')
Close
