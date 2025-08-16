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
            
            # Create demo users with Indian names
            demo_users = [
                {'username': 'admin', 'email': 'admin@dareexchange.com', 'is_staff': True, 'is_superuser': True},
                {'username': 'arjun', 'email': 'arjun@example.com'},
                {'username': 'priya', 'email': 'priya@example.com'},
                {'username': 'rohit', 'email': 'rohit@example.com'},
                {'username': 'sneha', 'email': 'sneha@example.com'},
                {'username': 'vikram', 'email': 'vikram@example.com'},
                {'username': 'ananya', 'email': 'ananya@example.com'},
                {'username': 'karan', 'email': 'karan@example.com'},
                {'username': 'meera', 'email': 'meera@example.com'},
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
            
            # Create sample dares with Indian cultural context
            sample_dares = [
                {
                    'title': 'Master 108 Surya Namaskars',
                    'description': 'Complete 108 Surya Namaskars (Sun Salutations) in one session. A traditional yoga challenge that tests endurance and devotion!',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Learn a Classical Indian Raga',
                    'description': 'Learn to sing or play a classical Indian raga you\'ve never performed before. Share a recording of your performance.',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Feed 50 Street Animals',
                    'description': 'Prepare food and feed 50 street dogs or cats in your area. Document this act of compassion and share the experience.',
                    'category': created_categories[2],  # Social
                },
                {
                    'title': 'Cook Authentic Biryani from Scratch',
                    'description': 'Master the art of making authentic Hyderabadi or Lucknowi biryani from scratch. Share the cooking process and final result!',
                    'category': created_categories[5],  # Food
                },
                {
                    'title': 'Complete a 10K Morning Run',
                    'description': 'Wake up at 5 AM and complete a 10K run before sunrise. Capture the beautiful morning views and your achievement!',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Create Rangoli Art',
                    'description': 'Design and create a beautiful rangoli pattern using traditional or modern techniques. Share your colorful creation!',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Learn Sanskrit Shlokas',
                    'description': 'Memorize and recite 5 Sanskrit shlokas with proper pronunciation. Share a video of your recitation.',
                    'category': created_categories[3],  # Learning
                },
                {
                    'title': 'Build an Indian Language App',
                    'description': 'Create a simple mobile or web app that teaches basic words in any Indian regional language.',
                    'category': created_categories[6],  # Technology
                },
                {
                    'title': 'Visit 5 Historical Monuments',
                    'description': 'Explore 5 historical monuments in your city or nearby areas. Document their history and significance.',
                    'category': created_categories[4],  # Adventure
                },
                {
                    'title': 'Teach a Skill to 10 People',
                    'description': 'Share any skill you know with 10 different people for free. Document the teaching sessions and their reactions.',
                    'category': created_categories[2],  # Social
                },
                {
                    'title': 'Master 50 Bhangra Moves',
                    'description': 'Learn and perform 50 different Bhangra dance moves. Create an energetic dance video showcasing your skills!',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Write a Bollywood Script',
                    'description': 'Write a complete short film script in Bollywood style with drama, romance, and action. Share your creative story!',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Master Regional Indian Cuisine',
                    'description': 'Cook authentic dishes from 5 different Indian states you\'ve never tried before. Document the culinary journey!',
                    'category': created_categories[5],  # Food
                },
                {
                    'title': 'Code in an Indian Language',
                    'description': 'Write a program with variable names and comments in Hindi, Tamil, or any Indian language. Share your unique code!',
                    'category': created_categories[6],  # Technology
                },
                {
                    'title': 'Trek to a Temple',
                    'description': 'Plan and complete a trek to a hilltop temple or spiritual place. Share the spiritual and physical journey.',
                    'category': created_categories[4],  # Adventure
                },
                {
                    'title': 'Organize a Community Cleanup',
                    'description': 'Organize and lead a community cleanup drive in your neighborhood. Get at least 20 people to participate.',
                    'category': created_categories[2],  # Social
                },
                {
                    'title': 'Learn Traditional Indian Martial Arts',
                    'description': 'Learn basic moves of Kalaripayattu, Gatka, or any traditional Indian martial art. Demonstrate your skills!',
                    'category': created_categories[0],  # Physical Challenge
                },
                {
                    'title': 'Create Indian Folk Art',
                    'description': 'Learn and create artwork in Madhubani, Warli, or any traditional Indian folk art style. Share your masterpiece!',
                    'category': created_categories[1],  # Creative
                },
                {
                    'title': 'Master Indian Street Food',
                    'description': 'Learn to make 10 different Indian street foods like pani puri, vada pav, dosa, etc. Host a street food party!',
                    'category': created_categories[5],  # Food
                },
                {
                    'title': 'Explore Indian Philosophy',
                    'description': 'Read and understand concepts from Bhagavad Gita, Upanishads, or any Indian philosophical text. Share your insights!',
                    'category': created_categories[3],  # Learning
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
                            completed_by=acceptor,
                            proof_text=f"I completed this dare! It was {random.choice(['amazing', 'challenging', 'fun', 'rewarding'])}.")
                        
                        # Sometimes add ratings
                        if random.random() < 0.7:  # 70% chance of rating
                            rating = DareRating.objects.create(
                                dare=dare,
                                rated_by=acceptor,
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
                    f'   Users: arjun, priya, rohit, sneha, vikram, ananya, karan, meera / demopass123'
                )
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error populating database: {e}')
            )
            raise e