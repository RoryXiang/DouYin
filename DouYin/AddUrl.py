import json
import time
import requests
import redis
from DouYin.DouyinFun import *
import schedule


class AddRedisUrl(object):
    def __init__(self, host='127.0.0.1', port='6379'):
        """连接redis数据库"""
        self.db = redis.StrictRedis(host=host, port=port, decode_responses=True, db=2)

    def add_redis(self):
        data = self.db.lrange('group:start_urls', 0, -1)
        if len(data) > 0:
           pass

        elif len(data) <= 0:
            request_url = 'http://127.0.0.1:8000/distribution/?distribution_server_name={}'.format('服务器1')
            data = requests.get(request_url)
            json_data = json.loads(data.text)

            if json_data['status'] == 0:
                distribution_last = json_data['data']['distribution_last']
                distribution_new = json_data['data']['distribution_new']
                distribution_header = json_data['data']['distribution_header']
                STUB = ""
                for i in range(distribution_last, distribution_new):
                    group_id = int(str(distribution_header) + '00000000000') + i
                    url = 'https://api3-normal-c-lf.amemv.com/aweme/v1/im/group/share/?version_code=10.3.0&js_sdk_version=1.55.0.3&app_name=aweme&vid=C2E5976F-BC7C-43F3-BEAA-46E14DF616C7&app_version=10.3.0&device_id=3764332570087559&channel=App%20Store&mcc_mnc=46006&aid=1128&screen_width=750&openudid=0d1ae40e0147a7793ea10082d9a9469c76080f8e&cdid=48EC7C60-896E-408F-8F76-D5D25A36E490&os_api=18&ac=WIFI&os_version=13.6.1&device_platform=iphone&build_number=103020&iid=2163444591899117&device_type=iPhone8,1&is_vcd=1&idfa=F1B0785A-18C1-4060-A63F-B82A3D020F3A&share_type=2&share_scene=12&group_id={}'.format(group_id)
                    cookies = 'd_ticket=5e30d08544e274f5c93d465e538386d35c277; odin_tt=73d7b7252b3114086297f00069d4b04c903ce78c58e6556a8a39143ebd247bd4fd0b4713b93f8126486519f72d27ad40eca5f3cc9cafb9014748f8bdde624503; sid_guard=471898e77b406a017c3acc5f5c27c8f3%7C1596176557%7C5184000%7CTue%2C+29-Sep-2020+06%3A22%3A37+GMT; uid_tt=e09eab304609eb8addb844d4e73fec05; sid_tt=471898e77b406a017c3acc5f5c27c8f3; sessionid=471898e77b406a017c3acc5f5c27c8f3; passport_csrf_token=4ba8109d55c7c9679e9f6630ad6a2feb; install_id=2427318944677447; ttreq=1$fc39d9c472c8c1ef3ffcf05559825698f269b47b'
                    params = url[url.index('?') + 1:]
                    s = getXGon(params, STUB, cookies)
                    ts = str(time.time()).split(".")[0]
                    gorgon = get_gorgon(ts, strToByte(s))

                    request_data = {'url': url, 'ts': ts, 'gorgon': gorgon, 'group_id': group_id}
                    self.db.lpush('group:start_urls', json.dumps(request_data))

            elif json_data['status'] == 1:
                print('没有更多的了')


def run():
    obj = AddRedisUrl()
    obj.add_redis()


schedule.every(20).minutes.do(run)

while True:
    schedule.run_pending()


