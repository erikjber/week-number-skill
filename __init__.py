from mycroft import MycroftSkill, intent_file_handler


class WeekNumber(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('number.week.intent')
    def handle_number_week(self, message):
        self.speak_dialog('number.week')


def create_skill():
    return WeekNumber()

