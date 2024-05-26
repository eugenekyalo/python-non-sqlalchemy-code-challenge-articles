class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")

        self.name = name
        self.category = category
        self.articles = []  # List to store articles
        self.contributors = []  # List to store contributing authors

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an Article instance")
        self.articles.append(article)

    def add_contributor(self, author):
        if not isinstance(author, Author):
            raise TypeError("Contributor must be an Author instance")
        if author not in self.contributors:  # Check for uniqueness
            self.contributors.append(author)

    # ... other methods for Magazine (e.g., returning list of titles or authors with > 2 articles)
