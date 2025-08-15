from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dare.models import Category, Dare
import random


class Command(BaseCommand):
    help = 'Populate the database with Indian sample data'

    def handle(self, *args, **options):
        # Create more diverse categories
        categories_data = [
            {'name': 'Physical Challenge', 'description': 'Fitness and physical activity dares'},
            {'name': 'Creative Challenge', 'description': 'Artistic and creative expression dares'},
            {'name': 'Social Challenge', 'description': 'Social interaction and community dares'},
            {'name': 'Learning Challenge', 'description': 'Educational and skill development dares'},
            {'name': 'Fun & Games', 'description': 'Entertainment and playful dares'},
            {'name': 'Food Challenge', 'description': 'Culinary adventures and food-related dares'},
            {'name': 'Travel Challenge', 'description': 'Exploration and adventure dares'},
            {'name': 'Technology Challenge', 'description': 'Digital and tech-related dares'},
            {'name': 'Cultural Challenge', 'description': 'Traditional and cultural activity dares'},
            {'name': 'Mindfulness Challenge', 'description': 'Mental wellness and meditation dares'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create Indian users
        indian_users_data = [
            {'username': 'arjun_sharma', 'email': 'arjun.sharma@example.com', 'first_name': 'Arjun', 'last_name': 'Sharma'},
            {'username': 'priya_patel', 'email': 'priya.patel@example.com', 'first_name': 'Priya', 'last_name': 'Patel'},
            {'username': 'rohit_kumar', 'email': 'rohit.kumar@example.com', 'first_name': 'Rohit', 'last_name': 'Kumar'},
            {'username': 'sneha_singh', 'email': 'sneha.singh@example.com', 'first_name': 'Sneha', 'last_name': 'Singh'},
            {'username': 'vikram_reddy', 'email': 'vikram.reddy@example.com', 'first_name': 'Vikram', 'last_name': 'Reddy'},
            {'username': 'ananya_gupta', 'email': 'ananya.gupta@example.com', 'first_name': 'Ananya', 'last_name': 'Gupta'},
            {'username': 'karthik_nair', 'email': 'karthik.nair@example.com', 'first_name': 'Karthik', 'last_name': 'Nair'},
            {'username': 'meera_joshi', 'email': 'meera.joshi@example.com', 'first_name': 'Meera', 'last_name': 'Joshi'},
            {'username': 'aditya_verma', 'email': 'aditya.verma@example.com', 'first_name': 'Aditya', 'last_name': 'Verma'},
            {'username': 'kavya_iyer', 'email': 'kavya.iyer@example.com', 'first_name': 'Kavya', 'last_name': 'Iyer'},
            {'username': 'rahul_agarwal', 'email': 'rahul.agarwal@example.com', 'first_name': 'Rahul', 'last_name': 'Agarwal'},
            {'username': 'ishita_bansal', 'email': 'ishita.bansal@example.com', 'first_name': 'Ishita', 'last_name': 'Bansal'},
            {'username': 'dev_shah', 'email': 'dev.shah@example.com', 'first_name': 'Dev', 'last_name': 'Shah'},
            {'username': 'riya_malhotra', 'email': 'riya.malhotra@example.com', 'first_name': 'Riya', 'last_name': 'Malhotra'},
            {'username': 'aryan_chopra', 'email': 'aryan.chopra@example.com', 'first_name': 'Aryan', 'last_name': 'Chopra'},
        ]
        
        for user_data in indian_users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name']
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')
        
        # Create diverse dares with Indian context
        dares_data = [
            {
                'title': 'Master 10 Yoga Asanas',
                'description': 'Learn and demonstrate 10 different yoga poses with proper form and breathing techniques.',
                'category': 'Physical Challenge',
                'posted_by': 'arjun_sharma'
            },
            {
                'title': 'Cook a Traditional Regional Dish',
                'description': 'Prepare an authentic dish from any Indian state you haven\'t tried cooking before. Share the recipe!',
                'category': 'Food Challenge',
                'posted_by': 'priya_patel'
            },
            {
                'title': 'Learn a Classical Dance Form',
                'description': 'Learn basic steps of Bharatanatyam, Kathak, or any Indian classical dance and perform for 2 minutes.',
                'category': 'Cultural Challenge',
                'posted_by': 'sneha_singh'
            },
            {
                'title': 'Visit 5 Historical Monuments',
                'description': 'Explore 5 historical sites in your city or nearby areas and share interesting facts about each.',
                'category': 'Travel Challenge',
                'posted_by': 'vikram_reddy'
            },
            {
                'title': 'Create Digital Art with Indian Motifs',
                'description': 'Design a digital artwork incorporating traditional Indian patterns, colors, or themes.',
                'category': 'Creative Challenge',
                'posted_by': 'ananya_gupta'
            },
            {
                'title': 'Learn 20 Words in a Regional Language',
                'description': 'Pick an Indian regional language different from your mother tongue and learn 20 useful phrases.',
                'category': 'Learning Challenge',
                'posted_by': 'karthik_nair'
            },
            {
                'title': 'Organize a Community Clean-up Drive',
                'description': 'Gather friends/neighbors and clean a public space in your locality. Document the before/after.',
                'category': 'Social Challenge',
                'posted_by': 'meera_joshi'
            },
            {
                'title': 'Build a Simple Mobile App',
                'description': 'Create a basic mobile app solving a local problem using any framework. Share the code!',
                'category': 'Technology Challenge',
                'posted_by': 'aditya_verma'
            },
            {
                'title': 'Practice Meditation for 21 Days',
                'description': 'Meditate for at least 15 minutes daily for 21 consecutive days. Track your progress.',
                'category': 'Mindfulness Challenge',
                'posted_by': 'kavya_iyer'
            },
            {
                'title': 'Create a Bollywood Dance Mashup',
                'description': 'Choreograph a 3-minute dance combining moves from 5 different Bollywood songs.',
                'category': 'Fun & Games',
                'posted_by': 'rahul_agarwal'
            },
            {
                'title': 'Run in a Local Marathon',
                'description': 'Participate in any local running event (5K, 10K, or half marathon) and complete it.',
                'category': 'Physical Challenge',
                'posted_by': 'ishita_bansal'
            },
            {
                'title': 'Street Food Photography Challenge',
                'description': 'Capture artistic photos of 15 different street foods from your city with their stories.',
                'category': 'Creative Challenge',
                'posted_by': 'dev_shah'
            },
            {
                'title': 'Learn to Play a Traditional Instrument',
                'description': 'Learn basics of tabla, sitar, flute, or any traditional Indian instrument. Record a 2-minute piece.',
                'category': 'Cultural Challenge',
                'posted_by': 'riya_malhotra'
            },
            {
                'title': 'Teach a Skill to 5 People',
                'description': 'Share any skill you know with 5 different people and help them learn something new.',
                'category': 'Social Challenge',
                'posted_by': 'aryan_chopra'
            },
            {
                'title': 'Try 10 Different Regional Cuisines',
                'description': 'Taste authentic dishes from 10 different Indian states. Rate and review each experience.',
                'category': 'Food Challenge',
                'posted_by': 'arjun_sharma'
            },
            {
                'title': 'Create a Travel Vlog',
                'description': 'Document a day trip to a nearby destination and create an engaging 5-minute travel vlog.',
                'category': 'Travel Challenge',
                'posted_by': 'priya_patel'
            },
            {
                'title': 'Master Mental Math Tricks',
                'description': 'Learn and demonstrate 5 different mental math techniques for quick calculations.',
                'category': 'Learning Challenge',
                'posted_by': 'rohit_kumar'
            },
            {
                'title': 'Code for a Social Cause',
                'description': 'Develop a website or app that addresses a social issue in your community.',
                'category': 'Technology Challenge',
                'posted_by': 'sneha_singh'
            },
            {
                'title': 'Practice Gratitude Journaling',
                'description': 'Write down 3 things you\'re grateful for every day for 30 days. Share insights.',
                'category': 'Mindfulness Challenge',
                'posted_by': 'vikram_reddy'
            },
            {
                'title': 'Organize a Cultural Exchange Event',
                'description': 'Host an event where people from different regions share their traditions, food, and stories.',
                'category': 'Social Challenge',
                'posted_by': 'ananya_gupta'
            },
        ]
        
        for dare_data in dares_data:
            try:
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
            except (Category.DoesNotExist, User.DoesNotExist) as e:
                self.stdout.write(f'Error creating dare {dare_data["title"]}: {e}')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with Indian sample data!'))
