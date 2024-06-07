from django.contrib.auth.models import User
from django.http import JsonResponse
from registeration.models import Referrals
from registeration.send_email import send_registeration_email
from django.contrib.auth.decorators import login_required

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
def get_referral_count(request):
    count = Referrals.objects.filter(referrer=request.user).count()
    return JsonResponse({'message': count}, status=200)

@login_required
def get_referral_id(request):
    return JsonResponse({'message': request.user.id}, status=200)
