from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactForm
from .serializer import ContactFormSerializer

class index(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
    
class ContactFormView(APIView):
    def post(self, requets):
        data = requets.data
        serializer = ContactFormSerializer(data=data)
        fname = data.get('fname')
        lname = data.get('lname')
        email = data.get('email')
        phone = data.get('phone')
        consultation_type = data.get('consultation_type') 
        service_intrest = data.get('service_intrest')
        pacakage_intrest = data.get('pacakage_intrest')
        preferred_date = data.get('preferred_date')
        preferred_time = data.get('preferred_time')
        message = data.get('message')
        if serializer.is_valid():
            serializer.save()
            subject = 'New Contact Form Submission'
            message = f'You have received a new message from {fname} {lname}.\n\n' \
                      f'Email: {email}\n' \
                      f'Phone: {phone}\n' \
                      f'Consultation Type: {consultation_type}\n' \
                      f'Service Interest: {service_intrest}\n' \
                      f'Package Interest: {pacakage_intrest}\n' \
                      f'Preferred Date: {preferred_date}\n' \
                      f'Preferred Time: {preferred_time}\n\n' \
                      f'Message:\n{message}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            subject1 = 'thanks for your submission'
            message1 = f'Thanks for your submission {fname} {lname}.\n\n' \
                      f'We have received your message and will get back to you shortly.'
            send_mail(subject1, message1, settings.EMAIL_HOST_USER, [email])
            return Response({"message": "Form submitted successfully!"})
        else:
            errors = serializer.errors
            return Response({"message": "Form submission failed!", "errors": errors})