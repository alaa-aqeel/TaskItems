from rest_framework.pagination import PageNumberPagination
from rest_framework import response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return response.Response({
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'count': self.page.paginator.count,
            "total_page": self.page.paginator.num_pages,
            'results': data
        })