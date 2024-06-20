from rest_framework.pagination import LimitOffsetPagination

class MyPagePagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='ml'
    offset_query_param='off'
    max_limit=6