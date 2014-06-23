from django.db import models

class WPArticle(models.Model):
    """WP article title and popularity."""
    title = models.CharField(max_length=256, unique=True)
    mdn_pop = models.DecimalField(max_digits=5, decimal_places=1)

    def __unicode__(self):
        """Return string containing title and median popularity"""
        return self.title + ", " + str(self.mdn_pop)

class Vote(models.Model):
    """Record votes."""
    article1 = models.ForeignKey(WPArticle, related_name='article1')
    article2 = models.ForeignKey(WPArticle, related_name='article2')
    vote = models.ForeignKey(WPArticle, related_name='vote')
    timestamp = models.DateTimeField(auto_now_add=True)
