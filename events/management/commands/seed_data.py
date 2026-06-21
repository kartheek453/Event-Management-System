from django.core.management.base import BaseCommand
from accounts.models import User
from events.models import Event


class Command(BaseCommand):
    help = "Seeds the database with a default manager account and sample event categories."

    def handle(self, *args, **options):
        manager, created = User.objects.get_or_create(
            email="manager@ems.com",
            defaults={
                "username": "manager@ems.com",
                "role": User.ROLE_MANAGER,
                "name": "Event Manager",
            },
        )
        if created:
            manager.set_password("admin123")
            manager.is_staff = True
            manager.is_superuser = True
            manager.save()
            self.stdout.write(self.style.SUCCESS("Created default manager account."))
        else:
            self.stdout.write(self.style.WARNING("Default manager account already exists."))

        sample_events = [
            {
                "title": "Wedding Decoration",
                "image": "images/events/wedding.svg",
                "description": "Elegant decoration packages for weddings with lighting, florals, and seating.",
                "price": 1999.00,
            },
            {
                "title": "Birthday Party",
                "image": "images/events/birthday.svg",
                "description": "Fun birthday themes with games, cake, and décor for every age.",
                "price": 799.00,
            },
            {
                "title": "Anniversary Celebration",
                "image": "images/events/anniversary.svg",
                "description": "Romantic anniversary setups and catering for a memorable celebration.",
                "price": 1299.00,
            },
            {
                "title": "Baby Shower",
                "image": "images/events/baby_shower.svg",
                "description": "Baby shower celebrations with custom décor, snacks, and gifts.",
                "price": 899.00,
            },
            {
                "title": "Naming Ceremony",
                "image": "images/events/naming_ceremony.svg",
                "description": "Joyous naming ceremonies with beautiful décor and refreshments.",
                "price": 999.00,
            },
            {
                "title": "Graduation Party",
                "image": "images/events/graduation.svg",
                "description": "Graduation parties with stage design, catering, and guest seating.",
                "price": 1099.00,
            },
            {
                "title": "Retirement Party",
                "image": "images/events/retirement.svg",
                "description": "Retirement events with elegant décor and appreciation ceremonies.",
                "price": 1199.00,
            },
            {
                "title": "Housewarming Ceremony",
                "image": "images/events/housewarming.svg",
                "description": "Housewarming celebrations with warm décor and welcoming themes.",
                "price": 699.00,
            },
            {
                "title": "Engagement Ceremony",
                "image": "images/events/engagement.svg",
                "description": "Engagement parties with romantic details and event coordination.",
                "price": 1499.00,
            },
            {
                "title": "Corporate Event",
                "image": "images/events/corporate_event.svg",
                "description": "Corporate events with conference setups, catering, and branding.",
                "price": 2299.00,
            },
        ]

        for event_data in sample_events:
            event, created = Event.objects.update_or_create(
                title=event_data["title"],
                defaults={
                    "image": event_data["image"],
                    "description": event_data["description"],
                    "price": event_data["price"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created event: {event.title}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Updated event: {event.title}"))
