from datetime import datetime
from time import mktime

class Timestamp_Maker(object):

    def __int__(self):
        super().__init__()

    def convertToTimestamp(self, date):
        '''
        Converts date to Unix Timestamp
        :param date:
        :return:
        '''
        date = str(date.strftime("%d/%m/%Y"))
        timestamp = mktime(datetime.strptime(date, "%d/%m/%Y").timetuple())
        return timestamp
