def add_time(start, duration, day=None):
    # Split start time into components
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Convert start hour to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Split duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate the new hour and minute
    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute = end_minute % 60
    
    end_hour = start_hour + duration_hour + extra_hour
    days_later = end_hour // 24
    end_hour = end_hour % 24
    
    # Determine AM or PM for the end time
    if end_hour >= 12:
        period = 'PM'
        if end_hour > 12:
            end_hour -= 12
    else:
        period = 'AM'
        if end_hour == 0:
            end_hour = 12
    
    # Build the new time string
    new_time = f"{end_hour}:{end_minute:02d} {period}"
    
    # Calculate the new day of the week if given
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(day.capitalize())
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        new_time += f", {end_day}"
    
    # Add information about days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time
