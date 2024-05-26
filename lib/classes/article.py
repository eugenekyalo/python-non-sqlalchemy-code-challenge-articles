class Article:
    def __init__(self, title, topic_area):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Article title must be a string between 5 and 50 characters")
        if not isinstance(topic_area, str) or len(topic_area) == 0:
            raise ValueError("Article topic area must be a non-empty string")

        self._title = title
        self._topic_area = topic_area

    @property
    def title(self):
        return self._title

    @property
    def topic_area(self):
        return self._topic_area

# Test case (assuming you have a way to create an Article object)
article = Article("How to wear a tutu with style", "Fashion")
assert article.title == "How to wear a tutu with style"  # Fixed assertion
