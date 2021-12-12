from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import fibonacci_calculate

@api_view()
def hello_world(request):
    f = fibonacci_calculate.main()
    return Response({"For fibonacci serie the value is: ": f})