import json
import requests
from base.config import Config


class Jira(object):
    """
    Jira: Create Issue
    https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/
    """

    def __init__(self):
        self.config = None

    def init(self):
        self.config = Config()
        self.config.init()
        self.read_params()

    def read_params(self):
        self.jira_host = self.config.get_value('JIRA', 'JIRA_HOST')
        self.jira_user = self.config.get_value('JIRA', 'JIRA_USER')
        self.jira_api_token = self.config.get_value('JIRA', 'JIRA_API_TOKEN')
        self.jira_user_api_token = self.jira_user + ':' + self.jira_api_token
        self.jira_rum_prj_key = self.config.get_value('JIRA', 'JIRA_RUM_PRJ_KEY')
        print('jira_host: ' + self.jira_host)

        # JIRA_PASSWORD
        # JIRA_API_TOKEN    # Base64
        # JIRA_ADMIN_API_KEY =
        # JIRA_ORG_ID =

    def createmeta(self):
        # url = self.jira_host + '/rest/api/2/issue/createmeta'
        # url = self.jira_host + '/rest/api/3/issue/createmeta'
        url = self.jira_host + '/rest/api/latest/issue/createmeta'
        headers = self.get_headers()
        r = requests.get(url, headers=headers)
        print(r.text)

    def get_headers(self):
        # content_type = 'text/html;charset=utf-8'
        accept_content_type = 'application/json'
        headers = {
            'User-Agent': 'python-requests',
            'Authorization': 'Basic ' + self.jira_user_api_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        return headers

    def submitRumServiceRequest(self):
        pass

    def submit_basic(self):
        request_type_id = 43
        # service_desk_id = "RPDP"
        # https://procore-test.atlassian.net/jira/servicedesk/projects/RPDP/queues/custom/43/RPDP-5"
        # url = "https://procore-test.atlassian.net/rest/servicedeskapi/request"
        url = "https://procore-test.atlassian.net/rest/api/2/issue"

        # "serviceDeskId": service_desk_id,

        # "requestTypeId": request_type_id,
        # data = {
        #     "requestFieldValues": {
        #         "summary": "Service request raised via service REST API",
        #         "description": "<description>",
        #         "issuetype": {"id": "43"},
        #         "project": {"key": "RPDP"}
        #     }
        # }

        # https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples
        # what is id of 'rum-request' and 'basic'?
        # how to get?
        data = {
            "fields": {"project": {"key": "RPDP"},
                       "summary": "created by api",
                       "description": "created by api",
                       "issuetype": {"id": "10008"}
                       }
        }

        headers = self.get_headers()
        r = requests.post(url, headers=headers, data=json.dumps(data))
        print(r.text)

    def main(self):
        self.init()  # read and inspect Jira ID's needed for JSON payload
        # self.meta()
        # self.submit_basic()
        # self.submit()


if __name__ == '__main__':
    this_class = 'Jira'
    c = None
    try:
        c = Jira()
        c.main()
    except Exception as e__main:
        print('Exception:', e__main, flush=True)
    finally:
        pass
