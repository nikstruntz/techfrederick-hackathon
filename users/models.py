from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Creating the model for a profile
class Profile(models.Model):

    # Linking to a User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Image for the user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Returning the name of the user when referenced
    def __str__(self):
        return f'{self.user.username} Profile'

    # Saving an image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image
        img = Image.open(self.image.path)

        # Resize image to a thumbnail
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)