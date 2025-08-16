from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dare.models import Dare, Category, DareCompletion, DareRating
from django.utils import timezone
import random


class Command(BaseCommand):
    help = 'Populate database with sample data for Render deployment'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Populating Render database with sample data...')
        
        try:
            # Create categories
            categories_data = [
                {'name': 'Physical Challenge', 'description': 'Physical activities and sports challenges'},
                {'name': 'Creative', 'description': 'Art, music, and creative challenges'},
                {'name': 'Social', 'description': 'Social interaction and community challenges'},
                {'name': 'Learning', 'description': 'Educational and skill-building challenges'},
                {'name': 'Adventure', 'description': 'Outdoor and adventure challenges'},
                {'name': 'Food', 'description': 'Cooking and food-related challenges'},
                {'name': 'Technology', 'description': 'Tech and coding challenges'},
            ]
            
            created_categories = []
            for cat_data in categories_data:
                category, created = Category.objects.get_or_create(
                    name=cat_data['name'],
                    defaults={'description': cat_data['description']}
                )
                created_categories.append(category)
                if created:
                    self.stdout.write(f'✅ Created category: {category.name}')
            
            # Create demo users
            demo_users = [
                {'username': 'admin', 'email': 'admin@dareexchange.com', 'is_staff': True, 'is_superuser': True},
                {'username': 'alice', 'email': 'alice@example.com'},
                {'username': 'bob', 'email': 'bob@example.com'},
                {'username': 'charlie', 'email': 'charlie@example.com'},
                {'username': 'diana', 'email': 'diana@example.com'},
            ]
            
            created_users = []
            for user_data in demo_users:
                user, created = User.objects.get_or_create(
                    username=user_data['username'],
                    defaults={
                        'email': user_data['email'],
                        'is_staff': user_data.get('is_staff', False),
                        'is_superuser': user_data.get('is_superuser', False)
                    }
                )
                if created:
                    user.set_password('demopass123')
                    user.save()
                    self.stdout.write(f'✅ Created user: {user.username}')
                created_users.append(user)
            
            # Create sample dares
            sample_dares = [
                {
                    'title': 'Complete 50 Push-ups Challenge',
                    'description': 'Do 50 push-ups in one session and record a video as proof. Show your strength and determination!',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Learn and Perform a New Song',
                    'description': 'Learn to play or sing a new song you\'ve never performed before and share a recording.',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Random Act of Kindness',
                    'description': 'Perform a genuine random act of kindness for a stranger and share the heartwarming story.',
                    'category': created_categories[2],  # Social
                },
                {
                    'title': 'Master a New Recipe',
                    'description': 'Cook a complex dish you\'ve never made before and share photos of the cooking process and final result.',
                    'category': created_categories[5],  # Food
                },
                {
                    'title': 'Complete a 5K Run',
                    'description': 'Run a full 5K distance and share your time, route, and experience. Perfect for fitness enthusiasts!',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Create Digital Art Masterpiece',
                    'description': 'Create an original digital artwork using any software and share your creative process.',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Learn 10 Words in a New Language',
                    'description': 'Pick a language you don\'t know and learn 10 useful words. Record yourself using them in sentences.',
                    'category': created_categories[3],  # Learning
                },
                {
                    'title': 'Build a Simple Web App',
                    'description': 'Create a basic web application using any framework and deploy it online.',
                    'category': created_categories[6],  # Technology
                },
                {
                    'title': 'Explore a New Neighborhood',
                    'description': 'Visit a part of your city you\'ve never been to before and document your discoveries.',
                    'category': created_categories[4],  # Adventure
                },
                {
                    'title': 'Compliment 5 Strangers',
                    'description': 'Give genuine compliments to 5 different strangers and share how it made you feel.',
                    'category': created_categories[2],  # Social
                },
                {
                    'title': 'Do 100 Jumping Jacks',
                    'description': 'Complete 100 jumping jacks without stopping and record your achievement.',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Write a Short Story',
                    'description': 'Write a creative short story of at least 500 words and share it with the community.',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Try a New Cuisine',
                    'description': 'Visit a restaurant serving cuisine you\'ve never tried before and document the experience.',
                    'category': created_categories[5],  # Food
                },
                {
                    'title': 'Solve a Coding Challenge',
                    'description': 'Complete a challenging programming problem on any coding platform and share your solution.',
                    'category': created_categories[6],  # Technology
                },
                {
                    'title': 'Hike a New Trail',
                    'description': 'Find and hike a trail you\'ve never been on before. Share photos and your experience.',
                    'category': created_categories[4],  # Adventure
                },
            ]
            
            created_dares = 0
            for i, dare_data in enumerate(sample_dares):
                # Assign random creator from demo users
                creator = random.choice(created_users)
                
                dare, created = Dare.objects.get_or_create(
                    title=dare_data['title'],
                    defaults={
                        'description': dare_data['description'],
                        'category': dare_data['category'],
                        'creator': creator,
                    }
                )
                
                if created:
                    created_dares += 1
                    self.stdout.write(f'✅ Created dare: {dare.title}')
                    
                    # Randomly accept some dares by other users
                    if random.random() < 0.3:  # 30% chance
                        acceptor = random.choice([u for u in created_users if u != creator])
                        completion = DareCompletion.objects.create(
                            dare=dare,
                            user=acceptor,
                            proof_text=f"I completed this dare! It was {random.choice(['amazing', 'challenging', 'fun', 'rewarding'])}.")
                        
                        # Sometimes add ratings
                        if random.random() < 0.7:  # 70% chance of rating
                            rating = DareRating.objects.create(
                                dare=dare,
                                user=acceptor,
                                rating=random.randint(3, 5),
                                comment=f"Great dare! {random.choice(['Loved it!', 'Would recommend!', 'Super fun!', 'Challenging but worth it!'])}"
                            )
            
            # Final count
            final_dare_count = Dare.objects.count()
            final_user_count = User.objects.count()
            final_category_count = Category.objects.count()
            final_completion_count = DareCompletion.objects.count()
            final_rating_count = DareRating.objects.count()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'\n🎉 Database population complete!\n'
                    f'📊 Final counts:\n'
                    f'   👥 Users: {final_user_count}\n'
                    f'   📂 Categories: {final_category_count}\n'
                    f'   🎯 Dares: {final_dare_count}\n'
                    f'   ✅ Completions: {final_completion_count}\n'
                    f'   ⭐ Ratings: {final_rating_count}\n'
                    f'✨ Created {created_dares} new dares this run\n'
                    f'🚀 Your Dare Exchange is ready for action!\n\n'
                    f'🔐 Demo Login Credentials:\n'
                    f'   Admin: admin / demopass123\n'
                    f'   Users: alice, bob, charlie, diana / demopass123'
                )
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error populating database: {e}')
            )
            raise e