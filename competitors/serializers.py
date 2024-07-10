from rest_framework import serializers
from .models import Competitor


class WebsiteTrafficSerializer(serializers.Serializer):
    number_of_visitors = serializers.IntegerField()
    page_views = serializers.IntegerField()
    unique_visitors = serializers.IntegerField()
    session_duration = serializers.CharField()
    bounce_rate = serializers.CharField()

class TopPerformingPageSerializer(serializers.Serializer):
    page = serializers.CharField()
    page_views = serializers.IntegerField()
    unique_visitors = serializers.IntegerField()
    engagement_rate = serializers.CharField()
    average_time_on_page = serializers.CharField()

class CompetitorSerializer(serializers.ModelSerializer):
    website_traffic = WebsiteTrafficSerializer()
    top_performing_pages = TopPerformingPageSerializer(many=True)

    class Meta:
        model = Competitor
        fields = ['business_name', 'business_type', 'location', 'website_traffic', 'top_performing_pages']
