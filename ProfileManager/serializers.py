from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator  # Ensures unique combinations of fields
from .models import Rating  # Importing the Rating model
from django.contrib.auth.models import User  # Importing Django's built-in User model for authentication

# RatingSerializer for serializing and deserializing the Rating model instances
class RatingSerializer(serializers.ModelSerializer):
    # Customizing the 'user' field to automatically assign the currently authenticated user
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # All User instances can be linked to the rating
        default=serializers.CurrentUserDefault()  # Default to the current authenticated user
    )

    class Meta:
        model = Rating  # The model to serialize
        fields = ['user', 'menuitem_id', 'rating']  # Fields to include in the serialized data
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),  # Ensure no duplicate user-menuitem_id combinations
                fields=['user', 'menuitem_id']  # The combination of user and menuitem_id must be unique
            )
        ]
        extra_kwargs = {
            'rating': {
                'max_value': 5,  # Maximum allowed rating value
                'min_value': 0,  # Minimum allowed rating value
            }
        }
