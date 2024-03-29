from articles.models import Article
from utils.validation.badwords_validation import EntityBadWordsValidationService


class ArticleEntityBadWordsValidationService(EntityBadWordsValidationService):

    def publish(self) -> Article:
        self.obj.published = True
        self.obj.save()
        return self.obj
