from django.db import models

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# Many to one relationship
# Many entries can be associated to one Topic
class Entry(models.Model):
    """Something specific learned about a topic"""

    #Reference to other record in database
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Extra information for managing the Entry model as "entries" (in plural)
    class Meta:
        verbose_name_plural = 'entries'
    
    # Which information to show when it refers to individual entries
    def __str__(self):
        """Return a string representation of the model. """
        return f"{self.text[:50]}..."