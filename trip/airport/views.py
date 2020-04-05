from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from airport.business.airport_errors import AirportNotFoundError, InternalError
from airport.business.airport_manager import AirportManager
from airport.models import DistanceComputeResponse
from airport.serializers import DistanceComputeResponseSerializer


class DistanceComputeView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.airport_manager = AirportManager()

    def get(self, request, first, second):
        distance = None
        first = first.upper()
        second = second.upper()
        try:
            distance = self.airport_manager.compute_distance(first, second)
            status = '200'
        except AirportNotFoundError:
            status = '400'
        except InternalError:
            status = '500'
        response = DistanceComputeResponse(first, second, distance)
        serializer = DistanceComputeResponseSerializer(response)
        return Response(status=status, data=serializer.data)


class ListAirportsView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.airport_manager = AirportManager()

    def get(self, request):
        airports = self.airport_manager.load_all()
        return Response(status='200', data=airports)
