from rest_framework.pagination import BasePagination
from rest_framework.response import Response


class PostPageNumberPagination(BasePagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': None,
            'previous': None,
            'results': data
        })

    def paginate_queryset(self, queryset, request, view=None):
        self.count = queryset.count()
        offset = self.get_offset(request)

        if offset > self.count:
            return []
        return list(queryset[offset:])

    def get_offset(self, request):
        try:
            offset = int(request.query_params.get('offset', 0))
        except ValueError:
            offset = 0
        return offset

    def get_page_number(self, request, paginator):
        return 1
