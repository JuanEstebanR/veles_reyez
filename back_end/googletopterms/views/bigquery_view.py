from ..utils.user_utils import user_authenticated
from rest_framework import generics, status
from rest_framework.response import Response
from ..googleapi.querybuilder import (top_25_terms_and_rising,
                                      top_25_international_terms_and_rising,
                                      top_international_terms)
import json

class Top25TermsAPIView(generics.ListAPIView):
    def post(self, request):
        """
        Return a list of the top 25 terms
        Based on the interval and table name
        From U.S.
        """
        try:
            data = request.data["body"]
            interval = data["interval"]
            limit = data["limit"]
            table_name = data["table_name"]
            print(interval, table_name)
            raw_query, data = top_25_terms_and_rising(table_name, interval, limit)
            return Response(data, content_type='application/json', status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class InternationalTopTermsAPIView(generics.ListAPIView):
    def post(self, request):
        try:
            data = request.data["body"]
            interval = data["interval"]
            table_name = data["table_name"]
            country_name = data["country_name"]
            limit = data["limit"]
            print(interval, table_name, country_name)
            raw_query, data = top_25_international_terms_and_rising(table_name,
                                                                    country_name,
                                                                    interval,
                                                                    limit)
            return Response(data, content_type="application/json" ,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class InternationalTopOneTermsAPIView(generics.ListAPIView):
    def post(self, request):
        try:
            data = request.data["body"]
            interval = data["interval"]
            limit = data["limit"]
            raw_query, data = top_international_terms(interval, limit)
            return Response(data, content_type="application/json",
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

