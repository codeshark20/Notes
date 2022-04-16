import json
import os
import time
import sys

template = json.dumps({"Notes": {"Tasks": ["Empty","Empty"],"Reminders": ["Empty","Empty"],"Notes": ["Empty","Empty"]}})

#Imports module 'click' if not found

try:
    import click
except ModuleNotFoundError:
    confirm = input("The module click is not found. Import click? (Y/N)")
    if confirm != "N":
        os.system('cmd /c "py -m pip install click"')
        print("If import was not compleed, please install the following package manually: 'click'.")
    if confirm == "N":
        sys.exit()

#Opens and reads data file

try:
    data = open('data.json', 'r')
    file = json.load(data)
    root = file['Notes']
    note = root['Notes']
    task = root['Tasks']
    reminder = root['Reminders']
    print(note, task, reminder)
    time.sleep(0.8)
    click.clear()
except OSError:
    open('data.json', 'x')
  
    # Using a JSON string
    with open('data.json', 'w') as outfile:
        outfile.write(template)


#Defines functions for display

def notes():
    runtime = -1

    try:
      print('Notes:')
      while True:
        runtime = runtime + 1
        notes = note[runtime]
        print(notes)
    except:
      None
    finally:
      time.sleep(1)

def tasks():

    runtime = -1

    try:
      print('Tasks:')
      while True:
        runtime = runtime + 1
        tasks = task[runtime]
        print(tasks)
    except:
      None
    finally:
      time.sleep(1)

def reminders():

    runtime = -1

    try:
      print('Reminders:')
      while True:
        runtime = runtime + 1
        reminders = reminder[runtime]
        print(reminders)
    except:
      None
    finally:
      time.sleep(1)

def clear(time):
    time.sleep(time)
    click.clear()

