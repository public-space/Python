import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class PomodoroApp(toga.App):
    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        self.task_input = toga.TextInput(placeholder='Enter task name...')
        self.start_button = toga.Button('Start', on_press=self.start_timer)
        self.pause_button = toga.Button('Pause', on_press=self.pause_timer)
        self.reset_button = toga.Button('Reset', on_press=self.reset_timer)
        self.timer_label = toga.Label('00:00')

        button_box = toga.Box(style=Pack(direction=ROW))
        button_box.add(self.start_button)
        button_box.add(self.pause_button)
        button_box.add(self.reset_button)

        self.main_box.add(self.task_input)
        self.main_box.add(self.timer_label)
        self.main_box.add(button_box)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(200, 150))
        self.main_window.content = self.main_box
        self.main_window.show()

    def start_timer(self, widget):
        # Implement timer start logic here
        pass

    def pause_timer(self, widget):
        # Implement timer pause logic here
        pass

    def reset_timer(self, widget):
        # Implement timer reset logic here
        pass

def main():
    pomodoro_app = PomodoroApp('Pomodoro Timer', 'org.example.pomodoro')
    return pomodoro_app

if __name__ == '__main__':
    main().main_loop()



import time

class PomodoroApp(toga.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

    def start_timer(self, widget):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.main_window.start_timer(1000, self.update_timer)

    def update_timer(self, widget):
        current_time = time.time()
        self.elapsed_time = current_time - self.start_time
        formatted_time = self.format_time(self.elapsed_time)
        self.timer_label.text = formatted_time

    def format_time(self, elapsed_time):
        minutes = int(elapsed_time / 60)
        seconds = int(elapsed_time % 60)
        return f"{minutes:02d}:{seconds:02d}"


