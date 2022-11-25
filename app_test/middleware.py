from django.utils.deprecation import MiddlewareMixin

tmp = {}


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        if 'id_user' in request.session:
            if request.session['id_user'] in tmp:
                request.session['name_user'] = tmp[request.session['id_user']]
            else:
                del request.session['id_user']
