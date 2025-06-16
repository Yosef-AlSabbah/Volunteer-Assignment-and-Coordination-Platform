from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials'

    def handle(self, *args, **options):
        email = 'admin@admin.com'
        password = 'admin'
        
        # Check if the superuser already exists
        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Superuser with email {email} already exists.'))
            return
            
        User.objects.create_superuser(
            email=email,
            username='admin',  # Include username if your User model requires it
            password=password
        )
        
        self.stdout.write(self.style.SUCCESS(f'Superuser with email {email} created successfully!'))
