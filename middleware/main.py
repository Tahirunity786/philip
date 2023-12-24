# middleware.py
from django.contrib.auth import logout

class CustomSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Perform actions for authenticated users before the view is executed
        if request.user.is_authenticated:
            # For example, log the user in for every request
            request.user.backend = 'django.contrib.auth.backends.ModelBackend'
        
        # Custom session management logic
        # For example, set a custom session variable
        request.session['v'] = '200'
        response = self.get_response(request)
        
        # Perform actions for authenticated users after the view is executed
        if request.user.is_authenticated:
            # For example, log the user out if they are not allowed to access a specific view
            if not request.user.has_perm('employee.views'):
                logout(request)

        return response
