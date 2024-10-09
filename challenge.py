from IPython.display import display
import pandas as pd

def add_event():
    name = input('What is the name of the event? ')
    date = input('What is the date of the event? ')
    hour = input('What is the hour of the start of the event? ')
    duration = input('What is the duration of the event? ')
    category = input('What is the category of the event? ')
    comment = input('What is the comment of the event? ')
    return name, date, hour, duration, category, comment

def edit_event(schedule):
    row = int(input('What is the index of the event that you would like to edit? '))
    column = input('What is the name of the column that you would like to edit? ')
    column = column.lower()
    new_value = input('What should be the new value? ')
    schedule.loc[row,column] = new_value
    return schedule

def remove_event(schedule):
    row_to_remove = int(input('What is the index of the event that you would like to remove? '))
    print('\n')
    print(schedule.iloc[row_to_remove:row_to_remove+1,:6])
    print('\n')
    decision = input('Are you sure you want to remove this event? Please type \'y\' or \'n\' ' )
    decision = decision.lower()
    if decision == 'y':
        schedule = schedule.drop(row_to_remove)
    else:
        print('\nEvent hasn\'t been removed')
    return schedule

def main():
    while True:
        print('What do you want to do? Type:\n - a if you want to add event,\n - e if you want to edit event,\n - r if you want to remove event,\n - c if you want to close the app.')
        action = input()
        action = action.lower()
        if (action == 'a'):
            schedule = pd.read_csv("schedule.csv")
            schedule.loc[len(schedule.index)] = add_event()
            print('\n')
            display(schedule)
            print('\n')
            schedule.to_csv("schedule.csv", index=False)
        elif (action == 'e'):
            schedule = pd.read_csv("schedule.csv")
            display(schedule)
            print('\n')
            schedule = edit_event(schedule)
            print('\n')
            display(schedule)
            print('\n')
            schedule.to_csv("schedule.csv", index=False)
        elif (action == 'r'):
            schedule = pd.read_csv("schedule.csv")
            display(schedule)
            print('\n')
            schedule = remove_event(schedule)
            print('\n')
            display(schedule)
            print('\n')
            schedule.to_csv("schedule.csv", index=False)
        elif (action == 'c'):
            break
        else:
            print('\nWrong input, plese try again\n')

if __name__ == "__main__":
    main()
