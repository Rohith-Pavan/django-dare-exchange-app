from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Update user names to Indian names'
    
    def handle(self, *args, **options):
        # Mapping of current usernames to Indian names
        name_mapping = {
            'alice': 'Priya',
            'bob': 'Arjun', 
            'charlie': 'Kavya',
            'rohithpavan': 'Rohit',
            'Rohith': 'Aditya',
            'admin': 'admin'  # Keep admin as is
        }
        
        updated_count = 0
        
        for old_name, new_name in name_mapping.items():
            try:
                user = User.objects.get(username=old_name)
                user.username = new_name
                user.first_name = new_name
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully updated {old_name} to {new_name}')
                )
                updated_count += 1
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'User {old_name} not found, skipping')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nTotal users updated: {updated_count}')
        )