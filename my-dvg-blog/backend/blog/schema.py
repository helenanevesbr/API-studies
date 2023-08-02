from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from blog import models

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
    # The Meta class is a special keyword in Django and related packages (such as graphene-django), and it cannot be named anything else.
    # In the context of graphene-django, the Meta class inside a DjangoObjectType class is used to associate the DjangoObjectType with a Django model.
    # DjangoObjectType is a special class that maps a Django model to a GraphQL object type, which can then be used in your GraphQL schema.

    # get_user_model() is used and not models.Profile. Why is that?
    # Django has a built-in user model for handling users. This user model is used for authentication, and it contains fields like username, email, password, etc.
    # My custom Profile model is designed to hold extra information about users that isn't included in the user model. The user model handles authentication, and the profile model handles extra user information.

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag
    # The Meta classes inside UserType, AuthorType etc specify which models these DjangoObjectTypes should be based on.

class Query(graphene.ObjectType):
    '''
    This class will bring together all the type classes you created, and you'll add methods to it to indicate the ways in which your models can be queried.
    '''

    all_posts = graphene.List(PostType)
    #graphene.List if the query will return multiple items.
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    #graphene.Field if it should return a single item.
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    post_by_author = graphene.List(PostType, username=graphene.String())
    post_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        '''
        For each of these attributes (all_posts, author_by_username, etc), you'll also create a method to resolve the query.
        The method for each resolver must start with resolve_, and the rest of the name should match the corresponding attribute.
        '''

        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )
        #You resolve a query by taking the information supplied in the query and returning the appropriate Django queryset in response.

schema = graphene.Schema(query=Query)
# graphene.Schema is a class provided by the Graphene library.
# An instance of Schema represents a GraphQL schema, which describes the types of data that clients can query and the operations (queries and mutations) that clients can perform
# query=Query is setting the root query object for the schema. In my case, Query is a graphene.ObjectType that I've defined with a field for every type of query that clients can make.
# When a client sends a query, the fields of Query define what data the client can request.