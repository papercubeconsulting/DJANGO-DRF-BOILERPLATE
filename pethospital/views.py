## Import django http utils
from django.http import FileResponse
from django.http import HttpResponseForbidden, HttpResponseNotFound

## Import pathnominator
from .utils import get_private_media_path

def private_media_access(request, path):
    access_granted = False
    user = request.user
    user_authenticated = user.is_authenticated
    if user_authenticated and user.is_staff:
        access_granted = True
    if access_granted:
        try:
            file_path = get_private_media_path(path)
            print(file_path)
            file = open(file_path, 'rb')
            response = FileResponse(file)
            return response
        except:
            return HttpResponseNotFound('El archivo solicitado no se ha encontrado')
    else:
        return HttpResponseForbidden('No se encuentra autorizado para ver este archivo')
