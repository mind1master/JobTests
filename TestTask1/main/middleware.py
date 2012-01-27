from TestTask1.main.models import Request

class RequestsMiddleware(object):
    def process_request(self, request):
    #        if (not request.status_code):
    #            st = 'no status code'
    #        else:
    #            st = request.status_code
        Request.objects.create(header=request.method + ' ' + request.path, body=request)
        return None