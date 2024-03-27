from django.shortcuts import render,HttpResponseRedirect

# Create your views here.





def home(request):
    return render(request,"index.html")


from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

def homemail(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        recipient_email = settings.DEFAULT_FROM_EMAIL
        try:
            send_mail(
                'New Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                [recipient_email],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
           # Print the error to the console for debugging
            return JsonResponse({'success': False})

    
