import math
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer(widget):
    start_button.enabled = True
    timer.cancel()
    timer_text.text = "00:00"
    title_label.text = "Timer"
    check_marks.text = ""
    global reps
    reps = 0

def start_timer(widget):
    start_button.enabled = False
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.text = "Long Break"
        title_label.style.color = '#0000FF'
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.text = "Short Break"
        title_label.style.color = '#00FF00'
    else:
        count_down(work_sec)
        title_label.text = "Work"
        title_label.style.color = '#FF0000'

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    timer_text.text = f"{count_min}:{count_sec}"
    if count > 0:
        global timer
        timer = toga.Timer(1.0, count_down, count - 1)
        timer.start()
    else:
        start_timer(None)
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.text = marks

def build(app):
    # Set up styles
    box_style = Pack(direction=COLUMN, padding=10)
    button_style = Pack(padding=(5, 10))

    # Create the UI components
    title_label = toga.Label("Timer", style=Pack(font_size=50))
    timer_text = toga.Label("00:00", style=Pack(font_size=35, font_weight='bold'))
    start_button = toga.Button("Start", on_press=start_timer, style=button_style)
    reset_button = toga.Button("Reset", on_press=reset_timer, style=button_style)
    check_marks = toga.Label("", style=Pack(font_size=25, font_weight='bold'))

    # Load the image for the tomato
    image_path = "tomato.png"
    tomato_img = toga.Image(image_path)
    canvas = toga.ImageView(image=tomato_img, style=Pack(width=200, height=224))

    # Create boxes to hold the UI components
    title_box = toga.Box(children=[title_label], style=Pack(alignment='center'))
    timer_box = toga.Box(children=[canvas, timer_text], style=Pack(alignment='center'))
    buttons_box = toga.Box(children=[start_button, reset_button], style=Pack(alignment='center'))
    marks_box = toga.Box(children=[check_marks], style=Pack(alignment='center'))

    # Create the main box to hold all the other boxes
    main_box = toga.Box(style=box_style)
    main_box.add(title_box)
    main_box.add(timer_box)
    main_box.add(buttons_box)
    main_box.add(marks_box)

        # Create the main window
    main_window = toga.MainWindow(title="Pomodoro Timer Application", size=(400, 400))
    main_window.content = main_box
    main_window.show()

def main():
    return toga.App("Pomodoro Timer", "com.example.pomodoro", startup=build)

if __name__ == '__main__':
    app = main()
    app.main_loop()
