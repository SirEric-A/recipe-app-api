from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipe import serializers


class BaseRecipeAttrViewset(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    '''base viewset for user owed recipe attributes'''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        '''return objects for the current authenticated user only'''
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        '''create a new objects '''
        serializer.save(user=self.request.user)


# class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
class TagViewSet(BaseRecipeAttrViewset):
    '''manage tags inthe database'''
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewset):
    '''manage Ingredients in the database'''
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
# # class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
# class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                  mixins.CreateModelMixin):
#     '''manage tags inthe database'''
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Tag.objects.all()
#     serializer_class = serializers.TagSerializer

#     def get_queryset(self):
#         '''return objects for the current authenticated user only'''
#         return self.queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self, serializer):
#         '''create a new tag'''
#         serializer.save(user=self.request.user)


# class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
#                         mixins.CreateModelMixin):
#     '''manage Ingredients in the database'''
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Ingredient.objects.all()
#     serializer_class = serializers.IngredientSerializer

#     def get_queryset(self):
#         '''return objects for the current authenticated user only'''
#         return self.queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self, serializer):
#         '''create a new tag'''
#         serializer.save(user=self.request.user)
