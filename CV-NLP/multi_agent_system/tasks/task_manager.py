class TaskManager:
    def parse_task(self, task_description):
        # Analyze task description and determine the roles required
        roles = []
        if 'research' in task_description.lower():
            roles.append('Researcher')
        if 'write' in task_description.lower():
            roles.append('Writer')
        if 'edit' in task_description.lower() or len(roles) > 1:
            roles.append('Editor')
        return roles
