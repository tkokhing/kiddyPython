hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

end_time_mins = mins + dura
hour_counter = (hour + (end_time_mins//60) - 24)
day_counter = 1
if (hour + (end_time_mins//60))<24:
    if end_time_mins >= 60 and end_time_mins <=120:
        hour += 1
        end_time_mins -=60
    else:
        hour += (end_time_mins//60)
        end_time_mins %=60
    print('Expected end time is: ',hour, ':',end_time_mins,' Hrs')
else:
    while (hour_counter > 24):
        hour_counter -=24
        day_counter +=1
    
    if end_time_mins >= 60 and end_time_mins <=120:
        hour += 1
        end_time_mins -=60
    else:
        hour = hour_counter
        end_time_mins %=60

    print('Expected end time is the',day_counter,'day(s) later at: ',hour, ':',end_time_mins,' Hrs')

    # if end_time_mins >= 60 and end_time_mins <=120:
    #     hour += 1
    #     end_time_mins -=60
    # else:
    #     hour = (hour + (end_time_mins//60) - 24)
    #     end_time_mins %=60
    # print('Expected end time is the next day: ',hour, ':',end_time_mins,' Hrs')