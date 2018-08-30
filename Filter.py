import pandas as pd
import math, datetime
from cedato.ReportWriter import ReportWriter as rw
class Filter(object):

    def __int__(self):
        super().__init__()

    def slice_n_dice(self, data):

        currentDate = datetime.datetime.now().strftime("%Y_%m_%d")
        df = pd.DataFrame(data)
        revenue_10per = df['revenue'].astype(float).sum()/10
        # supply_rpr = revenue / df['adRequest'].astype(float).sum() * 1000
        df['RPR'] = df['revenue'].astype(float) / df['adRequest'].astype(float) * 1000
        df_nofill = df[(df.impressions.astype(int) == 0)]
        df_filtered = df[(df.impressions.astype(int) > 0)]
        df_filtered = df_filtered.sort_values(by=['RPR'], ascending=False).reset_index(drop=True)
        bottom_10 = math.ceil(len(df_filtered)/10)
        df_filtered = df_filtered.tail(bottom_10).sort_values(by=['revenue'], ascending=True).reset_index(drop=True)
        revenue_filtered = df_filtered['revenue'].astype(float).sum()
        try:
           if not df_filtered.empty:
               while revenue_filtered > revenue_10per:
                   df_filtered = df_filtered.drop(index=0).reset_index(drop=True)
                   revenue_filtered = df_filtered['revenue'].astype(float).sum()
        except ValueError:
            print("Supply Id " + str(data[0]['supply_id']) + " is not performing well, look into pausing")
            rw().writeCSV("poorPerformingSupply_"+ currentDate + ".csv",data)
        df_filtered = pd.concat([df_filtered, df_nofill]).reset_index(drop=True)
        df_filtered = df_filtered[['supply_id',
                                'supply_name',
                                'supply_type','RPM',
                                'active',
                                'adRequest',
                                'ad_starts',
                                'cost',
                                'created',
                                'vastId',
                                'demand_name',
                                'demand_type',
                                'impressions',
                                'is_mobile_app',
                                'is_mobile_web',
                                'loaded',
                                'loaded_percent',
                                'revenue',
                                'updated',
                                'RPR']]
        return df_filtered
