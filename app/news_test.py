import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News(123,'Russia invades Ukrain','The rescent updates on the russians attack on the ukrain soil',
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.themoscowtimes.com%2F2022%2F02%2F25%2Frussia-attacks-ukraine-as-its-happening-a76553&psig=AOvVaw2ogZrO2fp7kGGBhYF8e8zP&ust=1646141820099000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIiNqajCovYCFQAAAAAdAAAAABAD',
        8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()