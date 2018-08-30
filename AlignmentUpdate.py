import requests

class AlignmentUpdate(object):

    def __init__(self):
        super().__init__()

    def removeDemandAlignment(self, token, supply_id, demand_ids):
        payload = {}
        for i in range(len(demand_ids)):
            payload[str(i)+'[vastId'] = demand_ids[i]
        header = {
            'accept': 'application/json',
            'api-version': '1',
            'authorization': 'Bearer {0}'.format(token),
            'content-type': 'application/x-www-form-urlencoded'
        }
        endpoint = 'https://api.cedato.com/api/supplies/{0}/demands/multi/detach'.format(supply_id)
        response = requests.patch(endpoint, data=payload,headers=header)
        return response
