import gc


class Achievement:
    def __init__(self, name: str, achievement_type: str, value: int, img_achieved: str, achieved: bool = False):
        self.name = name
        self.achievement_type = achievement_type
        self.value = value
        self.img_achieved = img_achieved
        self.achieved = achieved

    def check_if_achieved(self, speed_record, total_time, total_distance):

        result = 0

        if self.achievement_type == 'speed':
            result = speed_record
        elif self.achievement_type == 'distance':
            result = total_distance
        elif self.achievement_type == 'time':
            result = total_time

        if result >= self.value:
            self.achieved = True
        else:
            self.achieved = False
