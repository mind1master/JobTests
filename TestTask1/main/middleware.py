from TestTask1.main.models import Request
class RequestsMiddleware(object):
    def process_request(self, request):
        Request.objects.create(header=request)
        return None