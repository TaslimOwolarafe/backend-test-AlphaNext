import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "competitor_analysis.settings")

import django
django.setup()

from competitors.models import Competitor

def create_dummy_data():
    business_names = [
        "TechCorp", "HealthPlus", "EduCenter", "ShopEasy", "Foodies",
        "TravelMate", "FitnessPro", "GreenEnergy", "AutoWorld", "HomeDecor",
        "FashionHub", "PetCare", "GamingZone"
    ]
    
    business_types = [
        "Technology", "Healthcare", "Education", "E-commerce", "Food & Beverage",
        "Travel", "Fitness", "Energy", "Automotive", "Home Improvement",
        "Fashion", "Pet Services", "Entertainment"
    ]
    
    locations = [
        "New York, USA", "London, UK", "Berlin, Germany", "Tokyo, Japan", "Paris, France",
        "Toronto, Canada", "Sydney, Australia", "Dubai, UAE", "São Paulo, Brazil", "Mumbai, India",
        "Cape Town, South Africa", "Moscow, Russia", "Shanghai, China"
    ]

    for i in range(13):
        website_traffic = {
            "number_of_visitors": random.randint(50000, 200000),
            "page_views": random.randint(100000, 400000),
            "unique_visitors": random.randint(30000, 150000),
            "session_duration": f"{random.randint(2, 10)} minutes",
            "bounce_rate": f"{random.randint(20, 60)}%"
        }
        
        top_performing_pages = [
            {
                "page": "Home Page",
                "page_views": random.randint(20000, 100000),
                "unique_visitors": random.randint(15000, 80000),
                "engagement_rate": f"{random.randint(10, 40)}%",
                "average_time_on_page": f"{random.randint(1, 5)} minutes"
            },
            {
                "page": "Product Page",
                "page_views": random.randint(10000, 50000),
                "unique_visitors": random.randint(8000, 40000),
                "engagement_rate": f"{random.randint(15, 50)}%",
                "average_time_on_page": f"{random.randint(2, 6)} minutes"
            },
            {
                "page": "Blog Page",
                "page_views": random.randint(5000, 30000),
                "unique_visitors": random.randint(4000, 25000),
                "engagement_rate": f"{random.randint(5, 30)}%",
                "average_time_on_page": f"{random.randint(1, 4)} minutes"
            }
        ]
        
        competitor = Competitor(
            business_name=business_names[i],
            business_type=business_types[i],
            location=locations[i],
            website_traffic=website_traffic,
            top_performing_pages=top_performing_pages
        )
        
        competitor.save()
        print(f"Added competitor: {competitor.business_name}")

if __name__ == "__main__":
    create_dummy_data()
    print("Dummy data added successfully.")
