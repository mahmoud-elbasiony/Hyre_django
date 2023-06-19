class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view is called

        if request.path == '/tenant/applicant/create' and request.method == 'POST':
            # Code specific to the desired route and HTTP method
            print("my middle ware")
            pass
        print(request.user)
        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called

        return response
