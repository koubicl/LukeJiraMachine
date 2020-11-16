import CONSTANTS


class IssueModel:
    def __init__(self, connection, stories, fix_version):
        self.connection = connection
        self.stories = stories
        self.fix_version = fix_version

    def filter_objects_to_copy(self):
        model_list = []
        for story in self.stories:
            story_fields = self.connection.issue(story)
            this_story = story_fields.fields

            fix_version = self.fix_version.split('_')[0]
            summary = "{} {}".format(str(story), this_story.summary)
            acceptation_criterias = this_story.customfield_10813
            hc_ap = this_story.customfield_10815.name

            model_list.append(
                {'project': {
                    'key': CONSTANTS.PROJECT_KEY
                },
                'fixVersions': [{
                    'name': str(fix_version)
                }],
                'summary': str(summary),
                'description': str(acceptation_criterias),
                'assignee': {
                    'name': str(hc_ap)
                },
                'reporter': {
                    'name': str(hc_ap)
                },
                'issuetype': {
                    'name': CONSTANTS.ISSUE_TYPE
                }
                })
        return model_list
