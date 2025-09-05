import tkinter as tk
import winsound

# 🔊 Signal funksiyasi
def play_sound():
    duration = 500  # ms
    freq = 1000     # Hz
    winsound.Beep(freq, duration)

# ⏱ Vaqtni formatlash
def format_time(seconds: int) -> str:
    minutes = seconds // 60
    sec = seconds % 60
    return f"{minutes:02}:{sec:02}"

# 📋 Task manager
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.selected_task = None

    def add_task(self, name, planned_pomodoros):
        task = {"name": name, "planned": planned_pomodoros, "done": 0}
        self.tasks.append(task)
        self.selected_task = task  # avtomatik tanlash

    def mark_pomodoro_done(self):
        if self.selected_task:
            self.selected_task["done"] += 1

    def get_tasks(self):
        return self.tasks

# ⏳ Pomodoro taymeri
class PomodoroTimer:
    def __init__(self, root, update_callback, finish_callback):
        self.root = root
        self.update_callback = update_callback
        self.finish_callback = finish_callback

        self.work_time = 25 * 60
        self.break_time = 5 * 60
        self.time_left = self.work_time
        self.is_work = True
        self.is_running = False
        self.timer_id = None

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def stop(self):
        if self.is_running and self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.is_running = False

    def reset(self):
        self.stop()
        self.time_left = self.work_time if self.is_work else self.break_time
        self.update_callback(format_time(self.time_left))

    def countdown(self):
        if self.time_left > 0:
            self.update_callback(format_time(self.time_left))
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.countdown)
        else:
            play_sound()
            self.finish_callback(self.is_work)
            self.switch_mode()

    def switch_mode(self):
        self.is_work = not self.is_work
        self.time_left = self.work_time if self.is_work else self.break_time
        self.update_callback(format_time(self.time_left))
        self.is_running = False

# 🖥 Asosiy ilova GUI
class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("500x700")
        self.root.config(bg="#e6f7ff")

        self.task_manager = TaskManager()
        self.timer = PomodoroTimer(root, self.update_timer_display, self.session_finished)

        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 36, "bold"),
                                    fg="red", bg="#e6f7ff")
        self.timer_label.pack(pady=30)

        self.start_button = tk.Button(root, text="Start", command=self.timer.start,
                                      bg="#4CAF50", fg="white", width=10, font=("Arial", 12))
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.timer.stop,
                                     bg="#f44336", fg="white", width=10, font=("Arial", 12))
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.timer.reset,
                                      bg="#2196F3", fg="white", width=10, font=("Arial", 12))
        self.reset_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=6)
        self.task_listbox.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task,
                                         bg="#FF9800", fg="white", width=10, font=("Arial", 12))
        self.add_task_button.pack(pady=5)

        self.help_label = tk.Label(
            root,
            text=(
                "📌 Foydalanish tartibi:\n"
                "1. Avval vazifani 'Add Task' orqali qo‘shing.\n"
                "2. 'Start' tugmasini bosib ish sessiyasini boshlang (25 min).\n"
                "3. Vaqt tugaganda qisqa dam olish (5 min) avtomatik boshlanadi.\n"
                "4. Har safar tugagach, vazifaga bitta pomidorka qo‘shiladi.\n"
                "✅ Shu tariqa vazifalaringizni samarali tugatib boring!"
            ),
            font=("Arial", 10),
            fg="black",
            bg="#e6f7ff",
            justify="left",
            wraplength=350
        )
        self.help_label.pack(pady=15)

        self.author_label = tk.Label(
            root, text="Jamshidbek Isroilov\n t.me/jamshidbekisroilov2000", font=("Arial", 15, "italic"),
            fg="red", bg="#e6f7ff"
        )
        self.author_label.pack(side="bottom", pady=10)

    def update_timer_display(self, time_text):
        color = "red" if self.timer.is_work else "green"
        self.timer_label.config(text=time_text, fg=color)

    def session_finished(self, was_work):
        if was_work:
            self.task_manager.mark_pomodoro_done()
        self.update_task_list()

    def add_task(self):
        self.task_manager.add_task("New Task", 1)
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(
                tk.END, f"{task['name']} ({task['done']}/{task['planned']})"
            )

# 🚀 Ilovani ishga tushirish
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
