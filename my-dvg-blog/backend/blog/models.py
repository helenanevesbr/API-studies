from django.db import models
from django.conf import settings


class Profile(models.Model):
    '''
    Defines a new Django model named Profile
    '''
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        # One-to-one relationship with the authenticated user model
        # Therefore, each Profile can be associated with one user, and each user can have one Profile
        on_delete = models.PROTECT,
        # Django will prevent the deletion of the associated user if a Profile exists for that user.
    )
    website = models.URLField(blank = True)
    # URL field can be left blank
    bio = models.CharField(max_length=240, blank=True)
    # character field can also be left blank

    def __str__(self):
        return self.user.get_username()
    # __str__ : dunder method that returns a string representation of an object
    # In the context of Django, it's used to represent a model object as a string.
    # The get_username() method is a standard method of Django's User model, which returns the username of the user.
    # So, for example, if you have a Profile object associated with a User whose username is 'john_doe', when you call print() on this Profile object, the output will be 'john_doe'.
    # For example: 
    # profile = Profile.objects.get(id=1)  # Assume this profile belongs to the user 'john_doe'
    # print(profile)  # This will output: john_doe
    # __str__ will make the Profile objects appear in a more human-friendly manner on the admin site

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # field will be set to the current date/time when an object is first created (i.e., when it's added to the database). The date/time is automatically set when you create a new object, hence the name auto_now_add.
    # After the object is created, the date_created field won't change when you update the object. If you want the field to update to the current date/time every time the object is saved, you would use auto_now=True instead of auto_now_add=True.
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    # You won’t accidentally delete an author who still has posts on the blog
    # Because if you try to delete a Profile object that is referenced by at least one other object (for example, a blog post in the 'Post' model), Django will raise a ProtectedError.
    # ForeignKey is a type of field in Django that creates a many-to-one relationship.
    # That means that an author can write many posts, but each post has only one author.
    tags = models.ManyToManyField(Tag, blank=True)
    # The ManyToManyField relationship to Tag allows you to associate a post with zero or more tags. Each tag can be associated to many posts.