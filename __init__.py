from mycroft import MycroftSkill, intent_file_handler
import time

class PomodoroTimer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('config.set.intent')
    def handle_config_set(self, message):
        config_type = message.data.get('type')
        duration = message.data.get('duration')
        
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
