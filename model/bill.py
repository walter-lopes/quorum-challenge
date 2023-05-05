class Bill:

    def __init__(self, id: int, title: str, sponsor_id: int):
        self.id = int(id)
        self.title = title
        self.sponsor_id = int(sponsor_id)