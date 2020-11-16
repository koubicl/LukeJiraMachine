JIRA_SERVER = 'https://jira.homecredit.net/jira'
LUKE_JQL = "issuetype = Story AND fixVersion in ({},{}) AND Status != Closed AND Status != suspended AND sprint = \"{}\" ORDER BY key ASC"
ISSUE_TYPE = "Test"
PROJECT_KEY = "TECS"
TEST = False