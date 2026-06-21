from django.shortcuts import get_object_or_404, render
from accounts.decorators import client_required
from .models import Event


EVENT_SERVICES = {
    "Wedding Decoration": [
        "Stage decor and lighting",
        "Floral arrangements",
        "Seating and aisle setup",
        "Catering coordination",
    ],
    "Birthday Party": [
        "Theme decoration",
        "Party games and music",
        "Cake and catering support",
        "Balloon and table styling",
    ],
    "Anniversary Celebration": [
        "Romantic lighting",
        "Couple photo display",
        "Floral décor",
        "Fine dining setup",
    ],
    "Baby Shower": [
        "Custom décor and favors",
        "Snacks and desserts",
        "Games and seating",
        "Gift table setup",
    ],
    "Naming Ceremony": [
        "Ceremony decor",
        "Family seating",
        "Refreshments",
        "Photography coverage",
    ],
    "Graduation Party": [
        "Stage setup",
        "Graduation theme décor",
        "Catering and refreshments",
        "Photo booth",
    ],
    "Retirement Party": [
        "Elegant décor",
        "Award presentation setup",
        "Catering arrangements",
        "Guest seating",
    ],
    "Housewarming Ceremony": [
        "Welcome décor",
        "House tour setup",
        "Guest refreshments",
        "Warm seating areas",
    ],
    "Engagement Ceremony": [
        "Romantic décor",
        "Floral accents",
        "Catering coordination",
        "Photography",
    ],
    "Corporate Event": [
        "Conference setup",
        "Branding and signage",
        "Audio/visual support",
        "Refreshments",
    ],
}


@client_required
def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})


@client_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    services = EVENT_SERVICES.get(event.title, [
        "Event planning",
        "Decoration",
        "Catering support",
        "Entertainment coordination",
    ])
    return render(request, "events/event_detail.html", {"event": event, "services": services})
