from django.core.management.base import BaseCommand
from dare.models import Dare, DareCompletion, DareRating

class Command(BaseCommand):
    help = 'Reset all dares to original fresh state'
    
    def handle(self, *args, **options):
        # Delete all completions and ratings
        completions_deleted = DareCompletion.objects.all().delete()[0]
        ratings_deleted = DareRating.objects.all().delete()[0]
        
        # Reset all dares to available status and clear accepted_by field
        dares_updated = Dare.objects.update(status='available', accepted_by=None)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully reset {dares_updated} dares to fresh state')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Deleted {completions_deleted} completions and {ratings_deleted} ratings')
        )
        self.stdout.write(
            self.style.SUCCESS('All dares are now available for acceptance!')
        )