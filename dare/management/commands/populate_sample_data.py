from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dare.models import Category, Dare


class Command(BaseCommand):
    help = 'Populate the database with sample categories and dares'

    def handle(self, *args, **options):
        # Create sample categories
        categories_data = [
            {'name': 'Physical Challenge', 'description': 'Dares involving physical activities'},
            {'name': 'Creative Challenge', 'description': 'Artistic and creative dares'},
            {'name': 'Social Challenge', 'description': 'Dares involving social interactions'},
            {'name': 'Learning Challenge', 'description': 'Educational and skill-building dares'},
            {'name': 'Fun & Games', 'description': 'Light-hearted and entertaining dares'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create sample users if they don't exist
        users_data = [
            {'username': 'alice', 'email': 'alice@example.com'},
            {'username': 'bob', 'email': 'bob@example.com'},
            {'username': 'charlie', 'email': 'charlie@example.com'},
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email']}
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')
        
        # Create sample dares
        dares_data = [
            {
                'title': 'Run 5K in under 30 minutes',
                'description': 'Complete a 5-kilometer run in less than 30 minutes and share your time!',
                'category': 'Physical Challenge',
                'posted_by': 'alice'
            },
            {
                'title': 'Draw a portrait of a stranger',
                'description': 'Approach a stranger (politely) and ask to draw their portrait. Share the artwork!',
                'category': 'Creative Challenge',
                'posted_by': 'bob'
            },
            {
                'title': 'Learn 10 words in a new language',
                'description': 'Pick a language you\'ve never studied and learn 10 useful words. Record yourself saying them!',
                'category': 'Learning Challenge',
                'posted_by': 'charlie'
            },
            {
                'title': 'Compliment 5 strangers today',
                'description': 'Give genuine compliments to 5 different strangers and spread some positivity!',
                'category': 'Social Challenge',
                'posted_by': 'alice'
            },
            {
                'title': 'Create a 30-second dance video',
                'description': 'Choreograph and film a 30-second dance to your favorite song!',
                'category': 'Fun & Games',
                'posted_by': 'bob'
            },
        ]
        
        for dare_data in dares_data:
            category = Category.objects.get(name=dare_data['category'])
            posted_by = User.objects.get(username=dare_data['posted_by'])
            
            dare, created = Dare.objects.get_or_create(
                title=dare_data['title'],
                defaults={
                    'description': dare_data['description'],
                    'category': category,
                    'posted_by': posted_by
                }
            )
            if created:
                self.stdout.write(f'Created dare: {dare.title}')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated sample data!'))