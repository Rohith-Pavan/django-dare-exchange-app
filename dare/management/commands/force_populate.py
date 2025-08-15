from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dare.models import Dare, Category
from django.utils import timezone
import os


class Command(BaseCommand):
    help = 'Force populate database with sample data (for production)'

    def handle(self, *args, **options):
        self.stdout.write('Force populating database with sample data...')
        
        try:
            # Check current state
            dare_count = Dare.objects.count()
            user_count = User.objects.count()
            category_count = Category.objects.count()
            
            self.stdout.write(f'Current state: {user_count} users, {category_count} categories, {dare_count} dares')
            
            # Create admin user if doesn't exist
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@dareexchange.com',
                    'is_staff': True,
                    'is_superuser': True
                }
            )
            if created:
                admin_user.set_password('DareAdmin2024!')
                admin_user.save()
                self.stdout.write(f'✓ Created admin user: {admin_user.username}')
            else:
                self.stdout.write(f'✓ Admin user exists: {admin_user.username}')
            
            # Create demo user
            demo_user, created = User.objects.get_or_create(
                username='demo',
                defaults={'email': 'demo@dareexchange.com'}
            )
            if created:
                demo_user.set_password('DemoUser2024!')
                demo_user.save()
                self.stdout.write(f'✓ Created demo user: {demo_user.username}')
            else:
                self.stdout.write(f'✓ Demo user exists: {demo_user.username}')
            
            # Create categories
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
                    self.stdout.write(f'✓ Created category: {category.name}')
            
            # Get categories for dare assignment
            physical_cat = Category.objects.get_or_create(name='Physical Challenge')[0]
            creative_cat = Category.objects.get_or_create(name='Creative')[0]
            social_cat = Category.objects.get_or_create(name='Social')[0]
            learning_cat = Category.objects.get_or_create(name='Learning')[0]
            adventure_cat = Category.objects.get_or_create(name='Adventure')[0]
            
            # Force create sample dares (even if some exist)
            sample_dares = [
                {
                    'title': 'Complete 50 Push-ups Challenge',
                    'description': 'Do 50 push-ups in one session and record a video as proof. Show your strength and determination!',
                    'category': physical_cat,
                    'posted_by': admin_user
                },
                {
                    'title': 'Learn and Perform a New Song',
                    'description': 'Learn to play or sing a new song you\'ve never performed before and share a recording.',
                    'category': creative_cat,
                    'posted_by': demo_user
                },
                {
                    'title': 'Random Act of Kindness',
                    'description': 'Perform a genuine random act of kindness for a stranger and share the heartwarming story.',
                    'category': social_cat,
                    'posted_by': admin_user
                },
                {
                    'title': 'Master a New Recipe',
                    'description': 'Cook a complex dish you\'ve never made before and share photos of the cooking process and final result.',
                    'category': creative_cat,
                    'posted_by': demo_user
                },
                {
                    'title': 'Complete a 5K Run',
                    'description': 'Run a full 5K distance and share your time, route, and experience. Perfect for fitness enthusiasts!',
                    'category': physical_cat,
                    'posted_by': admin_user
                },
                {
                    'title': 'Create Digital Art Masterpiece',
                    'description': 'Create an original digital artwork using any software and share your creative process.',
                    'category': creative_cat,
                    'posted_by': demo_user
                },
                {
                    'title': 'Learn 10 Words in a New Language',
                    'description': 'Pick a language you don\'t know and learn 10 useful words. Record yourself using them in sentences.',
                    'category': learning_cat,
                    'posted_by': admin_user
                },
                {
                    'title': 'Explore a New Neighborhood',
                    'description': 'Visit a part of your city you\'ve never been to before and document your discoveries.',
                    'category': adventure_cat,
                    'posted_by': demo_user
                },
                {
                    'title': 'Compliment 5 Strangers',
                    'description': 'Give genuine compliments to 5 different strangers and share how it made you feel.',
                    'category': social_cat,
                    'posted_by': admin_user
                },
                {
                    'title': 'Do 100 Jumping Jacks',
                    'description': 'Complete 100 jumping jacks without stopping and record your achievement.',
                    'category': physical_cat,
                    'posted_by': demo_user
                }
            ]
            
            created_dares = 0
            for dare_data in sample_dares:
                # Check if similar dare exists
                existing = Dare.objects.filter(title=dare_data['title']).first()
                if not existing:
                    dare = Dare.objects.create(**dare_data)
                    created_dares += 1
                    self.stdout.write(f'✓ Created dare: {dare.title}')
                else:
                    self.stdout.write(f'- Dare exists: {existing.title}')
            
            # Final count
            final_dare_count = Dare.objects.count()
            final_user_count = User.objects.count()
            final_category_count = Category.objects.count()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n🎉 Database population complete!\n'
                    f'📊 Final counts: {final_user_count} users, {final_category_count} categories, {final_dare_count} dares\n'
                    f'✨ Created {created_dares} new dares this run\n'
                    f'🚀 Your Dare Exchange is ready for action!'
                )
            )
            
            # Show admin credentials for production
            if os.environ.get('RAILWAY_ENVIRONMENT'):
                self.stdout.write(
                    self.style.WARNING(
                        f'\n🔐 Admin Login Credentials:\n'
                        f'Username: admin\n'
                        f'Password: DareAdmin2024!\n'
                        f'Demo User: demo / DemoUser2024!'
                    )
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error populating database: {e}')
            )
            raise e