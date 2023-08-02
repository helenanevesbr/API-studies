from django.contrib import admin
from blog.models import Profile, Post, Tag

# The Django administration site (or "admin site") is a powerful feature of Django that provides a ready-to-use web-based interface for managing the content of your database, including creating, updating, and deleting records.

# When you register a model class with the admin site, Django automatically provides a default form interface for that model that you can use to manipulate objects of the model.

# To register a model with the admin site, you use decorator admin.register(), and pass in the model class that you want to register.

@admin.register(Profile) # This makes Profile appear in the Django admin site, and allows you to add, change, and delete instances of this model using the admin interface.
class ProfileAdmin(admin.ModelAdmin):
    # The decorator lets you register the model at the same time as you define a custom admin class (a subclass of admin.ModelAdmin). This class allows you to customize the admin interface for the model.
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

# Django automatically associates the Profile and Tag models with their respective ModelAdmins because you're using the @admin.register() decorator.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    list_filter = (
        "published",
        "publish_date",
    )

    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    search_fields = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    prepopulated_fields = {
        "slug":(
            "title",
            "subtitle",
        )
    }

    date_hierarchy = "publish_date"
    save_on_top = True

    # list_display, list_filter, etc. are not arbitrary names; they are predefined options in Django's ModelAdmin class. These options are used to control how the Django admin site displays the model's data.