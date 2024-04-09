import graphql_jwt
import graphene
from consumers.schema import UserQuery, CreateUserMutation
class Query(UserQuery,graphene.ObjectType):
    pass

class Mutation(CreateUserMutation,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
