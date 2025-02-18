from datetime import datetime

class Note:
    HIGH:str="HIGH"
    MEDIUM:str="MEDIUM"
    LOW:str="LOW"
    def __init__(self, code: str,title: str, text:str, improtance:str,creation_date: datetime, tags: list[str]):
        self.code: str=code
        self.title: str = title
        self.text: str = text
        self.importance: str = improtance
        self.creation_date:datetime =datetime.now()


