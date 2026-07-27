from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from django.contrib import admin
from .models import FishingSpot, ParkingLot
# Register your models here.

# GISModelAdmin を使うと、
# 管理画面の location フィールドが地図上でクリックして緯度経度を入力できるUIになります
# (Django 5.0以降の推奨クラス。旧OSMGeoAdminは非推奨)。
class ParkingLotInline(admin.TabularInline):
    model = ParkingLot
    extra = 1


@admin.register(FishingSpot)
class FishingSpotAdmin(GISModelAdmin):
    list_display = ('name', 'prefecture', 'city', 'water_type')
    list_filter = ('prefecture', 'water_type')
    search_fields = ('name', 'city')
    inlines = [ParkingLotInline]


@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display = ('name', 'spot', 'motorcycle_allowed', 'capacity', 'is_free')
    list_filter = ('motorcycle_allowed', 'is_free')