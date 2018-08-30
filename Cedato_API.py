'''
Written by Andrew Ravn
Last Updated: 23AUG2018
'''

from time import sleep
import pandas as pd
from cedato.Authenticate import Authenticate as auth
from cedato.Reports import Reports as rpt
from cedato.AlignmentUpdate import AlignmentUpdate as aln
from cedato.Filter import Filter as flt
from cedato.ReportWriter import ReportWriter as rw
import os, datetime
from cedato.TimeStampCreation import Timestamp_Maker as tstmp
cwd = os.path.dirname(__file__)
os.chdir(cwd)

def main():
    currentDate = datetime.datetime.now().strftime("%Y_%m_%d")
    endDate = tstmp().convertToTimestamp(datetime.date.today() - datetime.timedelta(1))
    startDate = tstmp().convertToTimestamp(datetime.date.today() - datetime.timedelta(3))
    token = auth().authentication()
    supply_ids = rpt().all_supply_report(token, startDate, endDate)
    '''
    supply_type = 0 - HTML player
    supply_type = 1 - Vast
    supply_type = 2 - CedatoX
    '''
    html_ids = []
    vast_ids = []
    cx_ids = []

    for rows in supply_ids:
        if rows['supply_type'] is '0':
            html_ids.append(rows['supply_id'])
        elif rows['supply_type'] is '1':
            vast_ids.append(rows['supply_id'])
        elif rows['supply_type'] is '2':
            cx_ids.append(rows['supply_id'])
        else:
            print("Supply id " + rows['supply_id'] + "has unknown supply_type id of " + rows['supply_type'])

    supply_ids = [html_ids, vast_ids, cx_ids]
    c = 0
    for rows in supply_ids:
        segment = [rows[x:x+8] for x in range(0,len(rows),8)]
        for seg in segment:
            sleep(2)
            row = ','.join(str(id) for id in seg)
            demand_data = rpt().supply_by_demand(token, row, startDate, endDate)
            rw().writeCSV("supply_type_"+str(c)+"_DemandReport.csv", demand_data)
            unique_supp_id = []
            for rows in demand_data:
                if not any(rows['supply_id'] == x for x in unique_supp_id):
                    unique_supp_id.append(rows['supply_id'])
            for ids in unique_supp_id:
                slice_data = []
                for rows in demand_data:
                    if rows['supply_id'] == ids:
                        slice_data.append(rows)
                filtered_data = flt().slice_n_dice(slice_data)
                filtered_report = os.getcwd() + '/Cedato_Results/supply_type_'+str(c)+"_DemandReport_filtered"+currentDate+".csv"
                if not os.path.exists(filtered_report):
                    filtered_data.to_csv(path_or_buf=filtered_report, index=False, mode='a', header=True)
                else:
                    filtered_data.to_csv(path_or_buf=filtered_report, index=False, mode='a', header=False)

        c+=1
        aln().removeDemandAlignment(token, rows['supply_id'], removeIds)

if __name__ == '__main__':
    main()
    print("Done")
