import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from spots.models import FishingSpot, ParkingLot


class Command(BaseCommand):
    help = '釣り場・駐車場データをCSVから一括登録する'

    def add_arguments(self, parser):
        parser.add_argument('spots_csv', type=str)
        parser.add_argument('parking_csv', type=str)

    def handle(self, *args, **options):
        spot_map = {}

        with open(options['spots_csv'], encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                spot, _ = FishingSpot.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'prefecture': row['prefecture'],
                        'city': row['city'],
                        'address': row['address'],
                        'location': Point(float(row['lng']), float(row['lat'])),
                        'water_type': row['water_type'],
                        'description': row.get('description', ''),
                    }
                )
                spot_map[row['name']] = spot
        self.stdout.write(self.style.SUCCESS(f'釣り場 {len(spot_map)} 件登録'))

        count = 0
        with open(options['parking_csv'], encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                spot = spot_map.get(row['spot_name']) or FishingSpot.objects.get(name=row['spot_name'])
                ParkingLot.objects.update_or_create(
                    spot=spot, name=row['name'],
                    defaults={
                        'motorcycle_allowed': row['motorcycle_allowed'].lower() == 'true',
                        'capacity': row.get('capacity') or None,
                        'is_free': row['is_free'].lower() == 'true',
                        'fee_note': row.get('fee_note', ''),
                        'distance_to_spot_m': row.get('distance_to_spot_m') or None,
                        'note': row.get('note', ''),
                    }
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'駐車場 {count} 件登録'))