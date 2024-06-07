import os
from django.contrib.auth.models import User
from django.http import JsonResponse
from registeration.models import Referrals
from registeration.send_email import send_registeration_email
from django.contrib.auth.decorators import login_required
from Compass.utils import write_file
from django.conf import settings


def new_user(request):
    try:
        user = User.objects.create_user(username=request.POST.get('username'),
                                        email=request.POST.get('email'),
                                        password=request.POST.get('password'),
                                        first_name=request.POST.get('first_name'),
                                        last_name=request.POST.get('last_name')
                                        )
        try:
            referrer = request.POST.get('referral')
            if referrer != '':
                referrer = User.objects.get(id=referrer)
                Referrals.objects.create(user=user, referrer=referrer)
        except Exception:
            return JsonResponse({'message': 'Invalid Referral ID'}, status=500)
        if not user:
            return JsonResponse({'message': 'User already exists!'}, status=500)
        send_registeration_email(user)
        return JsonResponse({'message': 'User Created!'}, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Something went wrong!'}, status=500)


@login_required
def add_user_photo(request):
    user = request.user
    photos_path = os.path.join(settings.BASE_DIR,
                               'static',
                               'user_photos',
                               str(user.id),
                               'profile_photo')
    uploaded_photo = request.FILES.get('photo')
    photo_name = uploaded_photo.name.split('.')
    photo_name = "profile_pic." + photo_name[1]
    write_file(uploaded_photo, photos_path, photo_name)
    return JsonResponse({'message': 'Success!'}, status=200)


@login_required
def get_profile_data(request):
    referral_id = request.user.id
    count = Referrals.objects.filter(referrer=request.user).count()
    first_name = request.user.first_name
    last_name = request.user.last_name
    rel_path = os.path.join('static',
                            'user_photos',
                            str(request.user.id),
                            'profile_photo')
    photos_path = os.path.join(settings.BASE_DIR, rel_path)
    if os.path.exists(photos_path):
        photo = os.listdir(photos_path)[0]
    
    return JsonResponse({'referral_id': referral_id,
                         'count': count,
                         'first_name': first_name,
                         'last_name': last_name,
                         'photo': os.path.join(rel_path, photo)
                         }, status=200)