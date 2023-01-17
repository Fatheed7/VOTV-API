from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response(
        {
            "message": "Welcome to the VOTV API.",
            "message2": "Valid Routes are:",
            "routes": [
                "cards/",
                "cards/<Card ID>/",
                "keywords/",
                "keywords/<Keyword ID>/",
                "artifacts/",
                "artifacts/<Artifact ID>/",
                "spells/",
                "spells/<Spell ID>/",
            ],
        }
    )