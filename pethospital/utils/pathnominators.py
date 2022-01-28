# Django import
from django.conf import settings

# file path issue
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#filefield
def get_profile_photo_path(instance, filename):
    print(instance)
    return 'private/staff/{0}/profile/photo/{1}'.format(instance.user.id,filename)

def get_private_media_path(media_path):
    file_path = settings.BASE_DIR / 'data/private/' / media_path
    return file_path