# Import re
import re
# Import validation error
from django.core.exceptions import ValidationError

# django validators issue (https://docs.djangoproject.com/en/4.0/ref/validators/)
def validate_document_number(self):
    document_type = self.document_type
    document_number = self.document_number
    if document_type:
        veredict = False
        if document_type.id == 1:
            veredict = re.match(r'^[0-9]{8}$', document_number)
            print(veredict)
        if document_type.id == 2:
            veredict = re.match(r'^[0-9]{12}$', document_number)
        if document_type.id == 3:
            veredict = re.match(r'^[0-9]{11}$', document_number)
        if veredict == None:
            raise ValidationError("El número de documento ingresado no es válido para el tipo de documento seleccionado")
    else:
        raise ValidationError("Para validar el número de documento se requiere seleccionar el tipo de documento")
