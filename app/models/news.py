class News:

    def __init__(self,id,title,overview,coverPhoto,vote_average,vote_count):
        self.id  = id
        self.title = title
        self.overview = overview
        self.coverPhoto = 'https://www.google.com/'+coverPhoto
        self.vote_avarage = vote_average
        self.vote_count = vote_count
