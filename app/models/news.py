class News:

    def __init__(self,id,author,title,description,url,urlToImage,content):
        self.id  = id
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = 'https://www.google.com/'+urlToImage
        self.url = 'vote_average'+url
        self.content = content
