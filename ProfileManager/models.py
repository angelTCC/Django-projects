from django.db import models
from django.contrib.auth.models import User  # Importing Django's built-in User model for authentication

# The Rating model represents user ratings for specific menu items
class Rating(models.Model):
    menuitem_id = models.SmallIntegerField()  # Stores the ID of the menu item being rated
    rating = models.SmallIntegerField()  # Stores the rating given by the user (e.g., 1-5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links the rating to a specific user; deletes rating if user is deleted

    def __str__(self):
        return "review"  # Returns a string representation of the model instance
