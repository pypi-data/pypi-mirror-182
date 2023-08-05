import uuid
from .node import Construct

class Element(Construct):
    def __init__(self, model, name):
        super().__init__(model, name)
        self.name = name
        self.uuid = uuid.uuid4()