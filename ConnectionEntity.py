from jira import JIRA
import CONSTANTS


class JiraConnection:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_connection(self):
        options = {'server': CONSTANTS.JIRA_SERVER}
        return JIRA(options, basic_auth=(self.username, self.password))
