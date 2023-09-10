from rest_framework.pagination import PageNumberPagination


class PageNumPagination(PageNumberPagination):
    """Пагинатор для страниц."""
    page_size_query_param = 'limit'
    page_size = 6
