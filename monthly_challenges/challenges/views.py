from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

# Dictionary of Monthly Challenges used into my functions
monthly_challenges = {
    "january": "Code in python for 30 days.",
    "february": "Code some Django apps for 30 days.",
    "march": "Learn about docker during 30 days.",
    "april": "Code in python for 30 days.",
    "may": "Code some Django apps for 30 days.",
    "june": "Learn about docker during 30 days.",
    "july": "Code in python for 30 days.",
    "august": "Code some Django apps for 30 days.",
    "september": "Learn about docker during 30 days.",
    "october": "Code in python for 30 days.",
    "november": "Code some Django apps for 30 days.",
    "december": "Learn about docker during 30 days."
}

# My Views
def index(request):
    return HttpResponse("TODO: Add tree to access all challenges per months.")

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported.")


