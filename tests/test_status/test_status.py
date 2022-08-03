import os
import requests
import time


class APITest:
    api_address = 'sentiment_analysis_api'
    api_port = 5000
    output = '''
    ============================
        {test_type} test
    ============================

    request done at {endpoint}

    expected result = 200
    actual result = {status_code}

    ==>  {test_status}
    '''

    def __init__(self, endpoint, test_type):
        self.endpoint = endpoint
        self.test_type = test_type

    def test_endpoint(self, *args, **kwargs):
        url = 'http://{address}:{port}/{endpoint}'.format(address=self.api_address,
                                                          port=self.api_port,
                                                          endpoint=self.endpoint)

        try:
            r = requests.get(url=url)
        except:
            time.sleep(10)
            r = requests.get(url=url)

        test_status = self.test_condition(r, *args, **kwargs)

        test_results = self.output.format(endpoint=self.endpoint,
                                          test_type=self.test_type,
                                          status_code=r.status_code,
                                          test_status=test_status)

        if os.environ.get('LOG') == '1':
            with open('/home/logs/api_test.log', 'a') as file:
                file.write(test_results)

    def test_condition(self, request, *args, **kwargs):
        if request.status_code == 200:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        print(test_status)
        return test_status


if __name__ == '__main__':
    APITest('status', 'S').test_endpoint()