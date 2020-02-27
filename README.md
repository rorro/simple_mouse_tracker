# Simple Mouse Tracker
![Simple Mouse Tracker logo](icon.png)

A simple program to track mouse movements.

## Getting started
- Use Linux
- Use Python 3+
- Install following dependencies:
  - tkinter
  - PIL
  - System Hotkey
- Download or clone the project
- Run the program using `python gui.py`

## Features
- Record mouse movements
- Draw recorded mouse path using PIL

## Config
Default config `.simplemousetracker` will be created in `~` if none exists.
```
# The keybinding for starting/stopping the mouse tracking.
# Valid modifiers: control, shift, super (windows key), alt.
# Read more about valid bindings at https://github.com/timeyyy/system_hotkey
start_tracking=control-s

# Where to save the tracked files. Leave blank to save in same folder as
# the script. The path should be absolute.
# If folder doesn't exist, nothing will be saved.
save_folder=
```
