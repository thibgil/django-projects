from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# My Views
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months_list": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        raise Http404()

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # Reference to the URL defined in urls.py (using the prefix challenges/ in order to have the full path /challenges/<month_name>)
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()


