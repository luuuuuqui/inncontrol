class Teste:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.get_name()}
    
    def from_row(self, row):
        self.set_name(row['name'])