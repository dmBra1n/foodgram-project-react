from api.filters import IngredientFilter, RecipeFilter
from api.mixins import ListRetrieveViewSet
from api.pagination import PageNumPagination
from api.permissions import IsAdminOrAuthorOrReadOnly
from api.serializers import (IngredientSerializer, RecipeCreateSerializer,
                             RecipeReadSerializer,
                             RecipeShortSerializer, SubscriptionSerializer,
                             TagSerializer)
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from recipes.models import Favorite, Ingredient, Recipe, ShoppingCart, Tag
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Follow, User
from api.utils import shopping_cart_file


class FollowUserView(APIView):
    """ViewSet для подписки и отписки от автора."""
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer

    def post(self, request, id):
        user = request.user
        author = get_object_or_404(User, pk=id)

        serializer = self.serializer_class(
            author,
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        Follow.objects.create(user=user, author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        user = request.user
        follow = get_object_or_404(Follow, user=user, author=id)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionsView(ListAPIView):
    """ViewSet для отображения подписок."""
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializer
    pagination_class = PageNumPagination

    def get_queryset(self):
        return User.objects.filter(author__user=self.request.user)

    def subscriptions(self, request):
        user = request.user
        queryset = User.objects.filter(follower__user=user)
        pages = self.paginate_queryset(queryset)
        serializer = SubscriptionSerializer(pages, many=True)
        return self.get_paginated_response(serializer.data)


class RecipeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Recipe."""
    queryset = Recipe.objects.all()
    permission_classes = (IsAdminOrAuthorOrReadOnly,)
    filterset_class = RecipeFilter
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PageNumPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return RecipeCreateSerializer
        return RecipeReadSerializer

    @staticmethod
    def add_remove_recipe(request, model, pk):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        if request.method == 'POST':
            if model.objects.filter(user=user, recipe=recipe).exists():
                return Response(
                    {'errors': 'Рецепт уже добавлен'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            model.objects.create(user=user, recipe=recipe)
            serializer = RecipeShortSerializer(
                recipe, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            if not model.objects.filter(user=user).exists():
                return Response(
                    {'errors': 'Рецепта нет в списке'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            obj = get_object_or_404(
                model, user=user, recipe=recipe
            )
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True,
            methods=['POST', 'DELETE'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        return self.add_remove_recipe(request, Favorite, pk)

    @action(detail=True,
            methods=['POST', 'DELETE'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk=None):
        return self.add_remove_recipe(request, ShoppingCart, pk)

    @action(detail=False,
            methods=['GET'],
            permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        return shopping_cart_file(request)


class TagViewSet(ListRetrieveViewSet):
    """ViewSet для модели Tag"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(ListRetrieveViewSet):
    """ViewSet для модели Ingredient"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filterset_class = IngredientFilter
    pagination_class = None
