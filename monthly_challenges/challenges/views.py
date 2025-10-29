from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"""
        <h2>Monthly Challenges List:</h2>
        <ul>
            {list_items}
        </ul>
    """

    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h2>Invalid month.</h2>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # Reference to the URL defined in urls.py (using the prefix challenges/ in order to have the full path /challenges/<month_name>)
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h2>{challenge_text}</h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h2>This month is not supported.</h2>")


