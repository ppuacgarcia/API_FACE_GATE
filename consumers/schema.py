from graphql import GraphQLError
from consumers.models import MyUser
from graphene_django import DjangoObjectType
import graphene
from django.utils import timezone
from graphql_jwt.decorators import  permission_required
from utils.save_video import VideoCamera
#------------------------------- User --------------------------------

class UserType(DjangoObjectType):
    # clase user type par apoder usarlo en schema
    class Meta:
        model = MyUser
        fields = '__all__'


class CreateUserMutation(graphene.Mutation):
    # clase para crear usuario
    

    class Arguments:
        # argumentos para crear usuario
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        is_superuser = graphene.Boolean()
        is_staff = graphene.Boolean()
        is_active = graphene.Boolean()
        has_module_perms = graphene.Boolean()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        video_path = graphene.String()
        
    user = graphene.Field(UserType)
    def mutate(self, info, username, email, password, is_superuser=False, is_staff=False, is_active=True, has_module_perms=False, first_name=None, last_name=None, video_path=None):
        # funcion para crear usuario
        
        user = MyUser(
            username=username,
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            first_name=first_name,
            last_name=last_name,
            date_joined=timezone.now()
        )
        # esto es solo por si se usa el video
        camara = VideoCamera
        camara.save_video(username)

        user.set_password(password)
        user.save()
        return CreateUserMutation(user=user)

class UserQuery(object):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    
    def resolve_users(self, info, **kwargs):
        return MyUser.objects.all()
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            if id is not None:
                return MyUser.objects.get(pk=id)
            return None
        except MyUser.DoesNotExist:
            return GraphQLError('No se encontro el usuario')
        
class UserMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = CreateUserMutation.Field()
    delete_user = CreateUserMutation.Field()
            