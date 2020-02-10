from mycroft import MycroftSkill, intent_file_handler


class PomodoroTimer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('timer.pomodoro.intent')
    def handle_timer_pomodoro(self, message):
        self.speak_dialog('timer.pomodoro')


def create_skill():
    return PomodoroTimer()

