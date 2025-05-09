class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed
        }
