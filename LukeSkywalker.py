import click
from ConnectionEntity import JiraConnection
from IssueModel import IssueModel
from StoryHandler import StoryHandler
import CONSTANTS


@click.command()
@click.option('--username', help='Jira user', prompt=True,
              required=True)
@click.option('--password', help='Jira user', prompt=True, hide_input=True,
              required=True)
@click.option('--fix_version', help='Jira user', prompt=True,
              required=True)
@click.option('--sprint', help='Jira user', prompt=True,
              required=True)
def run(username, password, fix_version, sprint):
    jira_connection = JiraConnection(username, password).get_connection()
    jql = create_appropriate_jql(fix_version, sprint)
    stories = StoryHandler(jira_connection, jql).find_stories()
    model_list = IssueModel(jira_connection, stories).filter_objects_to_copy()
    create_new_tecs(jira_connection, model_list)


def create_new_tecs(jira_connection, model_list):
    for model in model_list:
        issue = jira_connection.create_issue(project=model['project'], fixVersions=model['fixVersions'],
                                             summary=model['summary'], description=model['description'],
                                             assignee=model['assignee'], issuetype=model['issuetype'],
                                             reporter=model['reporter'])
        print(issue.key)


def create_appropriate_jql(fix_version, sprint):
    return CONSTANTS.LUKE_JQL.format(fix_version, sprint)


if __name__ == '__main__':
    run()
