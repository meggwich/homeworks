import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self.stdout.write(self.style.SUCCESS(f'Processing row: {row}'))
                try:
                    phone, created = Phone.objects.get_or_create(
                        id=row['id'],
                        defaults={
                            'name': row['name'],
                            'price': row['price'],
                            'image': row['image'],
                            'release_date': row['release_date'],
                            'lte_exists': row['lte_exists'] == 'True'
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully added phone {phone.name}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'Phone {phone.name} already exists'))
                except KeyError as e:
                    self.stdout.write(self.style.ERROR(f'Missing key: {e} in row: {row}'))