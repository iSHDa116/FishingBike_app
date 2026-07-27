from django.contrib.gis.db import models


class FishingSpot(models.Model):
    PREFECTURE_CHOICES = [
        ('kanagawa', '神奈川県'),
        ('tokyo', '東京都'),
    ]
    WATER_TYPE_CHOICES = [
        ('sea', '海'),
        ('river', '河川'),
        ('lake', '湖'),
    ]

    name = models.CharField('釣り場名', max_length=100)
    prefecture = models.CharField(
        '都道府県', max_length=20,
        choices=PREFECTURE_CHOICES, default='kanagawa', db_index=True
    )
    city = models.CharField('市区町村', max_length=50)
    address = models.CharField('住所', max_length=200)
    location = models.PointField('位置情報', geography=True)
    water_type = models.CharField(
        '種別', max_length=10,
        choices=WATER_TYPE_CHOICES, db_index=True
    )
    description = models.TextField('説明', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '釣り場'
        verbose_name_plural = '釣り場'
        ordering = ['name']

    def __str__(self):
        return self.name


class ParkingLot(models.Model):
    spot = models.ForeignKey(
        FishingSpot, related_name='parking_lots',
        on_delete=models.CASCADE, verbose_name='釣り場'
    )
    name = models.CharField('駐車場名', max_length=100)
    location = models.PointField('位置情報', geography=True, null=True, blank=True)
    motorcycle_allowed = models.BooleanField('バイク駐車可否', db_index=True)
    capacity = models.PositiveIntegerField('バイク駐車可能台数', null=True, blank=True)
    is_free = models.BooleanField('無料', default=True)
    fee_note = models.CharField('料金備考', max_length=200, blank=True)
    distance_to_spot_m = models.PositiveIntegerField('釣り場までの距離(m)', null=True, blank=True)
    note = models.TextField('備考(規制情報など)', blank=True)

    class Meta:
        verbose_name = '駐車場'
        verbose_name_plural = '駐車場'

    def __str__(self):
        return f'{self.name}({self.spot.name})'