class Reminder:
    def __init__(self, name):
        self.name = name

    def remind(self):
        return f"{self.name}! {self.reminder}!"
    
    def remind_me_to(self, reminder):
        self.reminder = reminder

reminder = Reminder("Kay")

reminder.remind_me_to("Walk the dog")

print(reminder.remind())
# Should print: "Kay! Walk the dog!"