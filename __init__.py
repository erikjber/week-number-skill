from mycroft import MycroftSkill, intent_file_handler
from isoweek import Week

class WeekNumber(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('number.week.intent')
    def handle_number_week(self, message):
        current_week = str(Week.thisweek().week)
        data = {"week":current_week}
        self.speak_dialog('number.week', data)


def create_skill():
    return WeekNumber()

