from pelican import signals
from pelican.contents import Article
from stardate import StarDate

def get_stardate(generator):    
    for article in generator.articles:
        article.stardate = StarDate(article.date).getStardate()

def register():
    signals.article_generator_finalized.connect(get_stardate)
