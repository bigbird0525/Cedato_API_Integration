import requests
from ast import literal_eval


class Reports(object):

    def __init__(self):
        super().__init__()

    def all_supply_report(self, token,startDate,endDate):
        '''
        Returns Unique Supply Id/Names/Type
        :param token:
        :return:
        '''
        payload = {}
        header = {
            'accept': 'application/json',
            'api-version': '1',
            'authorization': 'Bearer {0}'.format(token)
        }
        report_url = 'https://api.cedato.com/api/reports/supplies/extended?start={0}&end={1}&limit=1000'.format(startDate,endDate)
        response = requests.get(report_url, data=payload, headers=header)
        data = literal_eval(response.text)['data']['supplies']
        formatted_supply_data = []
        for rows in data:
            keys = ['supply_id', 'supply_name','supply_type']
            temp = {}
            for key in keys:
                temp[key] = rows[key]
            formatted_supply_data.append(temp)
        return formatted_supply_data

    def supply_by_demand(self, token, supply_id,startDate,endDate):
        '''
        Notes about response:
        adRequest = Ad Responses
        loaded = close to Ad Starts, but not quite the same
        :param token:
        :param supply_id:
        :return:
        '''
        payload = {}
        header = {
            'accept': 'application/json',
            'api-version': '1',
            'authorization': 'Bearer {0}'.format(token)
        }
        report_url = 'https://api.cedato.com/api/reports/supplies/extended?supply_id={0}&startDate={1}&endDate={2}&&group_by=demand_id&limit=100000'.format(supply_id,startDate,endDate)
        response = requests.get(report_url, data=payload, headers=header)
        data = literal_eval(response.text)['data']['supplies']
        return data
