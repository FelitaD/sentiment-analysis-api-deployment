import os
import requests
import time


class APITest:
    api_address = 'sentiment_analysis_api'
    api_port = 5000
    output = '''
    ============================

    request done at {endpoint}

    expected result = 200
    actual result = {status_code}

    ==>  {test_status}
    '''

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.params = {'sentence': 'Thats sucks'}

    def test_endpoint(self, *args, **kwargs):
        url = 'http://{address}:{port}/{endpoint}'.format(address=self.api_address,
                                                          port=self.api_port,
                                                          endpoint=self.endpoint)

        try:
            r = requests.post(url=url, data=self.params)
        except:
            time.sleep(10)
            r = requests.post(url=url, data=self.params)

        if r.status_code == 401 and 'Missing Authorization' in r.text:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        print(test_status)

        test_results = self.output.format(endpoint=self.endpoint,
                                          status_code=r.status_code,
                                          test_status=test_status)

        if os.environ.get('LOG') == '1':
            with open('/home/logs/api_test.log', 'a') as file:
                file.write(test_results)


if __name__ == '__main__':
    APITest(endpoint='v2/sentiment').test_endpoint(sentence='That sucks')
