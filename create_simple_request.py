import json
import requests
from requests.auth import HTTPBasicAuth
from base.config import Config


class JiraSDCreateSimpleRequest(object):
    """
    Jira: Create simple Service Desk Request (summary field only)
    - no approvers

    ---
    https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/

    Basic user:password is deprecated

    => for auth: use:    user:api_token

    In Jira Software, a new ticket is an 'issue', in Jira Service Desk it is a 'request'
    """

    def __init__(self):
        self.config = None
        self.auth = None

        self.jira_host = None
        self.jira_user = None
        self.jira_api_token = None

        self.jira_rum_service_desk_id = None
        self.jira_rum_request_type_id = None
        self.jira_user_api_token = None

    def init(self):
        self.config = Config()
        self.config.init()
        self.read_params()

        # print('init(): self.jira_user: ' + self.jira_user)
        # print('init(): self.jira_api_token: ' + self.jira_api_token)
        self.auth = HTTPBasicAuth(self.jira_user, self.jira_api_token)

    def read_params(self):
        self.jira_host = self.config.get_value('JIRA', 'JIRA_HOST')
        self.jira_user = self.config.get_value('JIRA', 'JIRA_USER')
        self.jira_api_token = self.config.get_value('JIRA', 'JIRA_API_TOKEN')
        self.jira_rum_service_desk_id = self.config.get_value('JIRA', 'JIRA_RUM_SERVICE_DESK_ID')
        self.jira_rum_request_type_id = self.config.get_value('JIRA', 'JIRA_RUM_REQUEST_TYPE_ID')
        print('jira_host: ' + self.jira_host)
        print('jira_rum_service_desk_id: ' + self.jira_rum_service_desk_id)
        print('jira_rum_request_type_id: ' + self.jira_rum_request_type_id)

        self.jira_user_api_token = self.jira_user + ':' + self.jira_api_token
        # print('self.jira_user_api_token: ' + self.jira_user_api_token)

    def get_headers(self):
        # content_type = 'text/html;charset=utf-8'
        accept_content_type = 'application/json'
        headers = {
            'User-Agent': 'python-requests',
            'Content-Type': accept_content_type,
            'Accept': accept_content_type
        }
        return headers

    def create_basic_request(self):
        """
        Submit a request to Jira Service Desk
        """
        url = self.jira_host + '/rest/servicedeskapi/request'

        # https://community.atlassian.com/t5/Jira-questions/How-to-create-a-
        # ticket-via-service-desk-api/qaq-p/1075512
        data = {
            "serviceDeskId": self.jira_rum_service_desk_id,
            "requestTypeId": self.jira_rum_request_type_id,
            "requestFieldValues": {
                "summary": "JSD issue created via Python REST API",
            }
        }
        # "description": "<description>"
        # "raiseOnBehalfOf": "sergey@google.com"

        headers = self.get_headers()
        r = requests.post(url, auth=self.auth, headers=headers, data=json.dumps(data))
        print(r.text)

    def main(self):
        self.init()  # read and inspect Jira ID's needed for JSON payload
        self.create_basic_request()


if __name__ == '__main__':
    this_class = 'JiraSDCreateSimpleRequest'
    c = None
    try:
        c = JiraSDCreateSimpleRequest()
        c.main()
    except Exception as e__main:
        print('Exception:', e__main, flush=True)
    finally:
        pass
