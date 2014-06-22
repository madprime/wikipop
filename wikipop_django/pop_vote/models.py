from django.db import models

class WPArticle(models.Model):
    """WP article title and popularity."""
    title = models.CharField(max_length=256)
    median_popularity = models.IntegerField()

    def __unicode__(self):
        """Return string containing title and median popularity"""
        return self.title + ", " + str(self.median_popularity)
