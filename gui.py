import PySimpleGUI as sg
import track_mouse
from draw_pixels import *
import threading

sg.theme('Topanga')

track_btn = sg.Button('Start tracking')
tracked_txt = sg.Text('Tracked: 0', size=(15,1))
layout = [  [track_btn, tracked_txt],
            [sg.Button('Draw stuff')],
            [sg.Button('Quit')] ]

# Create the Window
window = sg.Window('Simple Mouse Tracker', layout, size=(300, 200))

tracking_mouse = False
mouse_tracker = track_mouse.MouseTracker()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event in (None, 'Quit'):	# if user closes window or clicks cancel
        if tracking_mouse:
            tracking_mouse = False
            mouse_tracker.terminate()
            mouse_tracker.thread.join()
        break

    elif event in ('Start tracking'):
        if not tracking_mouse:
            tracking_mouse = True
            track_btn.Update("Stop tracking")
            mouse_tracker = track_mouse.MouseTracker()
            tracked_txt.update("Tracked: Tracking")
            mouse_tracker.thread.start()
        else:
            tracking_mouse = False
            track_btn.Update("Start tracking")
            tracked_txt.update("Tracked: " + str(mouse_tracker.tracked))
            mouse_tracker.terminate()
            mouse_tracker.thread.join()

    elif event in ('Draw stuff'):
        file_path = sg.PopupGetFile(
                "Select a valid .tracked file.",
                title="File to draw",
                file_types=(("Tracked","*.tracked"),))

        if file_path != '' and file_path != None:
            draw(file_path)

window.close()
