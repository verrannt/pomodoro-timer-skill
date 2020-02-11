from mycroft import MycroftSkill, intent_file_handler
from mycroft.util import play_wav
import time
from os.path import join, isfile, abspath, dirname

class PomodoroTimer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.session_length = 5 # how many study intervals in session
        self.interval_counter = 0 # counts how many study intervals have passed
        self.study_duration = 25 # study duration in minutes
        self.break_duration = 5 # break duration in minutes
        self.break_overflow = False # whether the user takes a too-long break
        self.sound_file = join(abspath(dirname(__file__)), 'timerBeep.wav')

    # 1. The start: the user tells Mycroft to start a new pomodoro session
    @intent_file_handler('session.start.intent')
    def handle_session_start(self, message):
        # 2. Start a new study timer and speak confirmation
        self.speak_dialog('session.start')
        self.start_study_timer()

    def start_study_timer(self):
        # 3. Sleep for the length of the study interval
        time.sleep(60 * self.study_duration)
        # 4. Check if end of session
        self.interval_counter += 1
        play_wav(self.sound_file)
        time.sleep(3)
        if self.interval_counter == self.session_length:
            self.end_session() # if yes, end the session
        else:
            self.take_break() # if not, take a break

    def take_break(self):
        # 5. Communicate start of break
        self.speak_dialog('break.start')
        time.sleep(60 * self.break_duration) # sleep for duration of break
        play_wav(self.sound_file)
        time.sleep(3)
        self.speak_dialog('break.end') # communicate end of break
        self.start_study_timer() # start studying again (go back to 3.)

    def end_session(self):
        # NOTE do cleaning up here for future versions
        self.speak_dialog('session.end')

    def stop(self):
        pass

    @intent_file_handler('config.set.intent')
    def handle_config_set(self, message):
        config_type = message.data.get('type')
        duration = message.data.get('duration')
        self.log.error('The function handle_config_set is not yet implemented.')
        #if config_type is 'study':
        #    self.settings['{}_duration'.format(config_type)] = duration
        #elif config_type is 'break':
        #    self.settings['{}_duration'.format(config_type)] = duration

        self.speak_dialog('config.set.success',
            {'type' : config_type, 'duration' : duration})

    @intent_file_handler('config.get.intent')
    def handle_config_get(self, message):
        config_type = message.data.get('Options')
        self.log.error('The function handle_config_get is not yet implemented.')
        #formatted_config_type = '{}_duration'.format(config_type)
        #duration = self.settings.get(formatted_config_type)
        #self.speak_dialog('config.get',
            # { 'type' : config_type, 'duration' : duration})

def create_skill():
    return PomodoroTimer()
