from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import fibonacci_calculate

@api_view()
def fibonacci_calculate_view(request):
    f = fibonacci_calculate.main()
    return Response({"For fibonacci serie the value is: ": f})