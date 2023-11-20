from ..utils.user_utils import user_authenticated
from rest_framework import generics, status
from rest_framework.response import Response
from ..googleapi.querybuilder import (top_25_terms_and_rising,
                                      top_25_international_terms_and_rising,
                                      top_international_terms)


class Top25TermsAPIView(generics.ListAPIView):
    def post(self, request):
        """
        Return a list of the top 25 terms
        Based on the interval and table name
        From U.S.
        """
        try:
            interval = request.data['interval']
            table_name = request.data['table_name']
            raw_query, data = top_25_terms_and_rising(table_name, interval)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class InternationalTopTermsAPIView(generics.ListAPIView):
    def post(self, request):
        try:
            interval = request.data['interval']
            table_name = request.data['table_name']
            country_name = request.data['country_name']
            raw_query, data = top_25_international_terms_and_rising(table_name,
                                                                    country_name,
                                                                    interval)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class InternationalTopOneTermsAPIView(generics.ListAPIView):
    def post(self, request):
        try:
            interval = request.data['interval']
            raw_query, data = top_international_terms(interval)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

