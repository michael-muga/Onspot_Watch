import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News(123,'rusev','Russia invades Ukrain','The rescent updates on the russians attack on the ukrain soil',
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.themoscowtimes.com%2F2022%2F02%2F25%2Frussia-attacks-ukraine-as-its-happening-a76553&psig=AOvVaw2ogZrO2fp7kGGBhYF8e8zP&ust=1646141820099000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIiNqajCovYCFQAAAAAdAAAAABAD',
        'https://www.themoscowtimes.com/2022/02/27/us-asks-americans-in-russia-to-consider-leaving-now-a76638','Russian President Vladimir Putin has launched a full-scale invasion of Ukraine, forcing residents to flee for their lives and leaving hundreds dead.')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()