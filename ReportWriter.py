import csv
import os
import datetime
cwd = os.path.dirname(__file__)
os.chdir(cwd)

class ReportWriter(object):

    def __init__(self):
        super().__init__()

    def writeCSV(self, file=None, data=None):
        '''
        Writes CSV report from data, data should be in a list of dictionaries
        :param file:
        :param data:
        :return:
        '''
        currentDate = datetime.datetime.now().strftime("%Y_%m_%d")
        file = os.getcwd() + '/Cedato_Results/' +currentDate+"_"+ file
        if not os.path.exists(file):
            try:
                with open(file, 'w') as results:
                    csv_writer = csv.writer(results, delimiter=",")
                    csv_writer.writerow(data[0].keys())
                    for rows in data:
                        csv_writer.writerow(rows.values())
            except IndexError:
                print(file+" was not able to write")
        else:
            try:
                with open(file, 'a') as results:
                    csv_writer = csv.writer(results, delimiter=",")
                    for rows in data:
                        csv_writer.writerow(rows.values())
            except IndexError:
                print(file+" was not able to write")
