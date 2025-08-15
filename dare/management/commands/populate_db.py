from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dare.models import Dare, Category
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample data...')
        
        # Create sample users if they don't exist
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(f'Created admin user: {admin_user.username}')
        
        demo_user, created = User.objects.get_or_create(
            username='demo',
            defaults={'email': 'demo@example.com'}
        )
        if created:
            demo_user.set_password('demo123')
            demo_user.save()
            self.stdout.write(f'Created demo user: {demo_user.username}')
        
        # Create sample categories
        categories_data = [
            {'name': 'Physical Challenge', 'description': 'Physical activities and sports challenges'},
            {'name': 'Creative', 'description': 'Art, music, and creative challenges'},
            {'name': 'Social', 'description': 'Social interaction and community challenges'},
            {'name': 'Learning', 'description': 'Educational and skill-building challenges'},
            {'name': 'Adventure', 'description': 'Outdoor and adventure challenges'}
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create sample dares if database is empty
        if Dare.objects.count() == 0:
            sample_dares = [
                {
                    'title': 'Do 50 Push-ups',
                    'description': 'Complete 50 push-ups in one session and record a video as proof.',
                    'difficulty': 'medium',
                    'points': 50,
                    'posted_by': admin_user
                },
                {
                    'title': 'Learn a New Song',
                    'description': 'Learn to play or sing a new song and share a recording.',
                    'difficulty': 'medium',
                    'points': 75,
                    'posted_by': demo_user
                },
                {
                    'title': 'Random Act of Kindness',
                    'description': 'Perform a random act of kindness for a stranger and share the story.',
                    'difficulty': 'easy',
                    'points': 30,
                    'posted_by': admin_user
                },
                {
                    'title': 'Cook a New Recipe',
                    'description': 'Try cooking a dish you\'ve never made before and share photos.',
                    'difficulty': 'easy',
                    'points': 40,
                    'posted_by': demo_user
                },
                {
                    'title': 'Run 5K',
                    'description': 'Complete a 5K run and share your time and route.',
                    'difficulty': 'hard',
                    'points': 100,
                    'posted_by': admin_user
                }
            ]
            
            for dare_data in sample_dares:
                dare = Dare.objects.create(**dare_data)
                self.stdout.write(f'Created dare: {dare.title}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Database populated successfully! '
                f'Users: {User.objects.count()}, '
                f'Categories: {Category.objects.count()}, '
                f'Dares: {Dare.objects.count()}'
            )
        )