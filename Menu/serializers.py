from rest_framework import serializers
from .models import Plan, Subscription, Video, QBank, Test,SavedVideo

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '_all_'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '_all_'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '_all_'

class QBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QBank
        fields = '_all_'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '_all_'

class SavedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedVideo
        fields = '_all_'