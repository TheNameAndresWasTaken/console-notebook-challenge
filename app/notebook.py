from datetime import datetime

class Note:
    HIGH:str="HIGH"
    MEDIUM:str="MEDIUM"
    LOW:str="LOW"
    def __init__(self, code: str,title: str, text:str, improtance:str):
        self.code: str=code
        self.title: str = title
        self.text: str = text
        self.importance: str = improtance
        self.creation_date:datetime =datetime.now()
        self.tags:list[str]=[]

    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)
    def date_creation(self):
        return f"{self.creation_date}-{self.title}"

class Notebook:
    def __init__(self):
        self.notes:list[Note]=[]
