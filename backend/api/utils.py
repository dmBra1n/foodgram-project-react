from django.db.models import Sum
from django.http import HttpResponse

from recipes.models import RecipeIngredient


def shopping_cart_file(request):
    ingredients = (
        RecipeIngredient.objects.filter(
            recipe__shopping_cart__user=request.user
        )
        .values('ingredient__name', 'ingredient__measurement_unit')
        .annotate(amount=Sum('amount'))
    )
    message = '\n'.join(
        f"• {ingredient.get('ingredient__name')}"
        f" ({ingredient.get('ingredient__measurement_unit')})"
        f" — {ingredient.get('amount')}"
        for ingredient in ingredients
    )

    headers = {
        'Content-Disposition': 'attachment; filename=shopping_cart.txt'
    }
    return HttpResponse(
        message, content_type='text/plain; charset=UTF-8', headers=headers
    )
