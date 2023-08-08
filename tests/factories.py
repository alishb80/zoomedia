from django.contrib.auth import get_user_model
import factory
from zoomedia.userprofile.models import Follow
from faker import Faker
from django.utils import timezone
from zoomedia.userprofile.models import Profile
faker = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    
    email = factory.Iterator(["alis@gmail.com" ,"masih@gmail.com"])
    password = factory.PostGenerationMethodCall('set_password' , 'adm!n')

class FollowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Follow
    Follower = factory.SubFactory(UserFactory)
    Following = factory.SubFactory(UserFactory)

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta : 
        model = Profile
    user = factory.SubFactory(UserFactory)
    post_counts          = factory.LazyAttribute(lambda _: 0 )
    follower_count  = factory.LazyAttribute(lambda _: 0 )
    following_count    = factory.LazyAttribute(lambda _: 0 )
    bio                  = factory.LazyAttribute(lambda _: f'{faker.unique.company()}')


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda _ :f'{faker.unique.company()}')
    description = factory.LazyAttribute(lambda _ : f'{faker.unique.company()}')
    slug = factory.LazyAttribute(lambda _ : f'{faker.unique.company()}' )
    created_at           = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    updated_at           = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    author = factory.SubFactory(UserFactory)

    