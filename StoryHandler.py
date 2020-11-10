class StoryHandler:
    def __init__(self, connection, jql):
        self.connection = connection
        self.jql = jql

    def find_stories(self):
        return self.connection.search_issues(jql_str=self.jql)
