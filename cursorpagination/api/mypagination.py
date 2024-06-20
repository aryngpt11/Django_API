from rest_framework.pagination import CursorPagination

class MyPagePagination(CursorPagination):
    page_size=4
    ordering='name'