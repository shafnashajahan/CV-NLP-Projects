from .researcher import ResearcherAgent
from .writer import WriterAgent
from .editor import EditorAgent

class WorkerFactory:
    def create_worker(self, role):
        if role == 'Researcher':
            return ResearcherAgent()
        elif role == 'Writer':
            return WriterAgent()
        elif role == 'Editor':
            return EditorAgent()
        else:
            raise ValueError(f"No such role: {role}")
