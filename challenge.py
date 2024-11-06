from IPython.display import display
import pandas as pd
import datetime as dt

def open_file():
    schedule = pd.read_csv('schedule.csv')
    print('\n')
    display(schedule)
    return schedule

def close_file(schedule):
    display(schedule)
    print('\n')
    schedule.to_csv("schedule.csv", index=False)
    return

categories = {
    'w':'work',
    's':'sport and dance',
    'l':'learning',
    'f':'family & friends',
    'o':'other'
}

def event_category():
    while True:
        category_entry = input("""What is the category of the event? Type:
        (w) if it's work,
        (s) if it's sport & dance,
        (l) if it's learning,
        (f) if it's family & friends,
        (o) if it's other
        """)
        category = categories.get(category_entry.lower())
        if category is None:
            print('\nWrong input, please try again\n')
        else:
            return category

def start_past_check(event_start_entry):
    current_time = dt.datetime.now()
    if event_start_entry >= current_time:
        return event_start_entry
    else:
        while True:
            decision = input('The time you entered is in the past. Do you really want to add event in the past? Type "yes" or "no" ')
            decision = decision.lower()
            if decision == 'yes':
                return event_start_entry
            elif decision == 'no':
                event_start_entry = time_start()
                return event_start_entry
            else:
                print('\nWrong input, please try again\n')

# def time_overlap_check(event_start,duration):
#     t1 = dt.datetime.strptime(duration,"%H:%M:%S")
#     duration_timedelta = dt.timedelta(hours=t1.hour, minutes=t1.minute, seconds=t1.second)
#     event_finish = event_start + duration_timedelta
#     schedule = open_file()
#     for row in schedule:
#         old_event_start = row['event_start']
#         t2 = dt.datetime.strptime(row['duration'],"%H:%M:%S")
#         old_duration_timedelta = dt.timedelta(hours=t2.hour, minutes=t2.minute, seconds=t2.second)
#         old_event_finish = old_event_start + old_duration_timedelta
#         if old_event_start > event_finish and old_event_finish < event_start:
#             return
#         else:
#             print('There is a clash in your calendar with the below event\n')
#             print(schedule.iloc[row:row + 1, :6])
#             return

def time_start():
    date_entry = input('What is the date of the event? Enter it in YYYY-MM-DD format ')
    year, month, day = map(int, date_entry.split('-'))
    time_entry = input('What is the time of the start of the event? Enter it in HH:MM format ')
    hour, minute = map(int, time_entry.split(':'))
    event_start = dt.datetime(year, month, day, hour, minute)
    return event_start

def add_event():
    name = input('What is the name of the event? ')
    event_start_entry = time_start()
    event_start = start_past_check(event_start_entry)
    duration_minutes = int(input('What is the duration of the event? Please provide it in minutes '))
    duration = str(dt.timedelta(seconds = duration_minutes * 60))
    time_overlap_check(event_start, duration)
    category = event_category()
    comment = input('What is the comment of the event? ')
    return name, event_start, duration, category, comment

columns = {
    'n':'name',
    's':'event_start',
    'd':'duration',
    'ca':'category',
    'co':'comment'
}

def edit_value():
    while True:
        column_entry = input("""What is the name of the column that you would like to edit? Type:
        (n) if it's 'name',
        (s) if it's 'event_start',
        (d) if it's 'duration',
        (ca) if it's 'category',
        (co) if it's 'comment'
        """)
        column = columns.get(column_entry.lower())
        if (column == 'name') or (column == 'comment'):
            new_value = input('What should be the new value? ')
            return new_value, column
        elif column == 'event_start':
            new_value = time_start()
            start_past_check(new_value)
            return new_value, column
        elif column == 'duration':
            duration_minutes = int(input('What is the new duration of the event? Please provide it in minutes '))
            new_value = str(dt.timedelta(seconds = duration_minutes * 60))
            return new_value, column
        elif column == 'category':
            new_value = event_category()
            return new_value,column
        else:
            print('\nWrong input, please try again\n')

def remove_event(schedule):
    print('\n')
    row_to_remove = int(input('What is the index of the event that you would like to remove? '))
    print('\n')
    print(schedule.iloc[row_to_remove:row_to_remove +1, :6])
    print('\n')
    while True:
        decision = input('Are you sure you want to remove this event? Please type "yes" or "no" ' )
        decision = decision.lower()
        if decision == 'yes':
            schedule = schedule.drop(row_to_remove)
        elif decision == 'no':
            print('\nEvent hasn\'t been removed')
        else:
            print('\nWrong input, please try again\n')
        return schedule

def main():
    print("-----Welcome in the To Do List App!-----")
    while True:
        action = input("""What do you want to do? Type:
        (d) if you want to display schedule,
        (a) if you want to add event,
        (e) if you want to edit event,
        (r) if you want to remove event,
        (c) if you want to close the app.
        """)
        action = action.lower()
        if action =='d':
            schedule = open_file()
            schedule.to_csv("schedule.csv", index=False)
        elif action == 'a':
            schedule = open_file()
            schedule.loc[len(schedule.index)] = add_event()
            close_file(schedule)
        elif action == 'e':
            schedule = open_file()
            row = int(input('What is the index of the event that you would like to edit? '))
            new_value, column = edit_value()
            schedule.loc[row,column] = new_value
            close_file(schedule)
        elif action == 'r':
            schedule = open_file()
            schedule = remove_event(schedule)
            close_file(schedule)
        elif action == 'c':
            break
        else:
            print('\nWrong input, please try again\n')

if __name__ == "__main__":
    main()