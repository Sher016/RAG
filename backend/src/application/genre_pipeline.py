class GenreRunner:
    def __init__(self, genre_service):
        self.genre_service = genre_service

    def execute(self, text, candidate_labels):
        return self.genre_service.run(text, candidate_labels)
