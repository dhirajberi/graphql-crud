import graphene
from graphene_django import DjangoObjectType
from crudapp.models import Test

class TestType(DjangoObjectType):
    class Meta:
        model = Test
        fields=("id", "name")

class Query(graphene.ObjectType):
    all_names = graphene.List(TestType)

    def resolve_all_names(root, info):
        # We can easily optimize query count in the resolve method
        return Test.objects.all()
 
class TestCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)
 
    test = graphene.Field(TestType)
 
    @classmethod
    def mutate(cls,root,info,name):
        test = Test(name = name)
        test.save()
        return TestCreate(test = test)
 
class TestUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID() 
        name = graphene.String(required = True)
 
    test = graphene.Field(TestType)
 
    @classmethod
    def mutate(cls,root,info,name,id):
        test = Test.objects.get(id = id)
        test.name = name
        test.save()
        return TestUpdate(test = test)
 
class TestDelete(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
 
    test=graphene.Field(TestType)
 
    @classmethod
    def mutate(cls,root,info,id):
        test=Test.objects.get(id=id)
        test.delete()
        return
 
class Mutation(graphene.ObjectType):
    create_test=TestCreate.Field()
    update_test=TestUpdate.Field()
    delete_test=TestDelete.Field()
 
schema=graphene.Schema(mutation=Mutation, query=Query)