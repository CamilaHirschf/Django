from django.http import HttpResponse

@app.route('/', methods=['GET'])
def hello(request):
 return HttpResponse("Hello World")
