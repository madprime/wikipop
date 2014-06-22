from django.db import models

class WPArticle(models.Model):
    """WP article title and popularity."""
    title = models.CharField(max_length=256, unique=True)
    mdn_pop = models.DecimalField(max_digits=5, decimal_places=1)

    def __unicode__(self):
        """Return string containing title and median popularity"""
        return self.title + ", " + str(self.mdn_pop)
