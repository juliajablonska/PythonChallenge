from IPython.display import display
import pandas as pd
import datetime as dt

def open_file():
    schedule = pd.read_csv('schedule.csv')
    print('\n')
    display(schedule)
    print('\n')
    return schedule

def close_file(schedule):
    display(schedule)
    print('\n')
    schedule.to_csv("schedule.csv", index=False)
    return

def add_event():
    name = input('What is the name of the event? ')
    date_entry = input('What is the date of the event? Enter it in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    time_entry = input('What is the time of the start of the event? Enter it in HH:MM format')
    hour, minute = map(int, time_entry.split(':'))
    event_start = dt.datetime(year, month, day, hour, minute)
    duration_minutes = int(input('What is the duration of the event? Please provide it in minutes '))
    duration = str(dt.timedelta(seconds=duration_minutes*60))
    category = input('What is the category of the event? ')
    comment = input('What is the comment of the event? ')
    return name, event_start, duration, category, comment

def edit_event(row,column):   
    column = column.lower()
    if (column == 'name') or (column == 'category') or (column == 'comment'):
        new_value = input('What should be the new value? ')
    elif (column == 'event_start'):
        date_entry = input('What is the new date of the event? Enter it in YYYY-MM-DD format')
        year, month, day = map(int, date_entry.split('-'))
        time_entry = input('What is the new time of the start of the event? Enter it in HH:MM format')
        hour, minute = map(int, time_entry.split(':'))
        new_value = dt.datetime(year, month, day, hour, minute)
    elif (column == 'duration'):
        duration_minutes = int(input('What is the new duration of the event? Please provide it in minutes '))
        new_value = str(dt.timedelta(seconds=duration_minutes*60))
    else: 
        print('\nWrong input, plese try again\n')    
    return new_value

def remove_event(row_to_remove):    
    print('\n')
    print(schedule.iloc[row_to_remove:row_to_remove+1,:6])
    print('\n')
    decision = input('Are you sure you want to remove this event? Please type \'y\' or \'n\' ' )
    decision = decision.lower()
    if decision == 'y':
        schedule = schedule.drop(row_to_remove)
    else:
        print('\nEvent hasn\'t been removed')
    return

print("-----Welcome in the To Do List App!-----")

def main():
    while True:    
        action = input("""What do you want to do? Type:
        (d) if you want to display schedule,
        (a) if you want to add event,
        (e) if you want to edit event,
        (r) if you want to remove event,
        (c) if you want to close the app.
        
        """)
        action = action.lower()       
        if (action =='d'):
            schedule = open_file()
            schedule.to_csv("schedule.csv", index=False)
        elif (action == 'a'):
            schedule = open_file()
            schedule.loc[len(schedule.index)] = add_event() 
            close_file(schedule)
        elif (action == 'e'):
            schedule = open_file()
            row = int(input('What is the index of the event that you would like to edit? '))
            column = input('What is the name of the column that you would like to edit? ')
            new_value = edit_event(row,column)
            schedule.loc[row,column] = new_value
            close_file(schedule)
        elif (action == 'r'):
            schedule = open_file()
            row_to_remove = int(input('What is the index of the event that you would like to remove? '))
            schedule = remove_event(row_to_remove)
            close_file(schedule)
        elif (action == 'c'):           
            break
        else:
            print('\nWrong input, plese try again\n')

if __name__ == "__main__":
    main()