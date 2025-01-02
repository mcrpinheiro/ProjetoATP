import FreeSimpleGUI as sg

# Define the layout
layout = [
    [sg.Text(
        "This is a dynamically resizable text. Resize the window to see the effect.",
        key="TEXT",
        size=(50, 1),
        expand_x=True,
        expand_y=True,
        justification="center",
    )],
    [sg.Multiline(
        "This multiline box will wrap text and expand as the window resizes.",
        size=(50, 10),
        expand_x=True,
        expand_y=True,
        key="MULTILINE",
        no_scrollbar=True,
        disabled=True,  # Set to True if you don't want user editing
    )],
    [sg.Button("Exit")],
]

# Create the window
window = sg.Window(
    "Resizable Text Example",
    layout,
    resizable=True,
    finalize=True  # Required for resizing to take effect
)

# Enable dynamic resizing for text and multiline elements
window["TEXT"].expand(expand_x=True, expand_y=False)
window["MULTILINE"].expand(expand_x=True, expand_y=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close()
