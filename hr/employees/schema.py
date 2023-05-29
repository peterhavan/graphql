import graphene

from graphene_django.types import DjangoObjectType

from hr.employees.models import Category, Employee


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_employees = graphene.List(EmployeeType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_employees(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Employee.objects.select_related('category').all()