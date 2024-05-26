class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []  # List to store associated articles

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an Article instance")
        self.articles.append(article)

    # ... other methods for Author (e.g., returning list of topics)
