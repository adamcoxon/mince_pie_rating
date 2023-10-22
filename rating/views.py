from django.shortcuts import render, redirect
from .models import MincePie, Ratings, Questions
from statistics import mean

# TODO - Get these into a model and into the DB
likert_scale = [
    {
        "name": "a",
        "rating": 1,
        "display": "1 Rubbish: Absolutely disappointing"
    },
    {
        "name": "a",
        "rating": 2,
        "display": "2 Below Average: Needs improvement"
    },
    {
        "name": "a",
        "rating": 3,
        "display": "3 Average: Just okay, nothing special",
    },
    {
        "name": "a",
        "rating": 4,
        "display": "4 Good: Pretty satisfying",
    },
    {
        "name": "a",
        "rating": 5,
        "display": "5 Fantastic: Absolutely amazing!"
    }
]

# TODO - Get these into a model and into the DB
questions = [
    {
        "question": "What is the quality of the pastry?",
        "supporting_comment": "Are we talking buttery, crumbly or what?",
        "short_form": "pastry_quality"
    },
    {
        "question": "What is the mince meat to pastry ratio?",
        "supporting_comment": "Nice and fat or a little light?",
        "short_form": "ratio"
    },
    {
        "question": "How well does the sweetness of the pie balance with the spices?",
        "supporting_comment": "Some Supporting Comment",
        "short_form": "ratio1"
    },
    {
        "question": "How visually appealing is the mince pie?",
        "supporting_comment": "Some Supporting Comment",
        "short_form": "todo"
    },
    {
        "question": "How fresh and moist is the pastry?",
        "supporting_comment": "Some Supporting Comment",
        "short_form": "todo"
    },
    {
        "question": "How would you rate the overall flavor profile of the mince pie?",
        "supporting_comment": "Some Supporting Comment",
        "short_form": "todo"
    },
    {
        "question": "How well does the mince pie maintain its shape and structure? ",
        "supporting_comment": "Some Supporting Comment",
        "short_form": "todo"
    },
    {
        "question": "How likely are you to recommend this mince pie to others?",
        "supporting_comment": "Some Supporting Comment",
        "short_form": "todo"
    }
]


def calculate_average_score(data: dict) -> int:
    numbers = []
    for _, v in data.items():
        if v.isnumeric():
            numbers.append(int(v))
    return int(round(mean(numbers)))


def get_mince_pies() -> MincePie:
    return MincePie.objects.all()


def update_rate_pie(request):
    score = calculate_average_score(data=dict(request.POST.dict()))
    # print(f"Pie Name - {request.POST.get('pie_name')}")
    pie = MincePie.objects.filter(name=request.POST.get("pie_name")).first()
    current_rating = pie.rating
    pie.rating = int(round(mean([current_rating, score])))
    pie.times_rated = pie.times_rated + 1
    pie.save()


def price_per_pie(cost_per_box: float, amount_per_box: float):
    return cost_per_box / amount_per_box


# Views
def rate(request):
    pies = get_mince_pies()
    if request.method == "POST":
        # for k, v in request.POST.items():
        #     print(k, v)
        update_rate_pie(request=request)
        return redirect('home')
    return render(request, 'rate.html', {'pies': pies, 'likert': likert_scale, 'questions': questions})


def home(request):
    return render(request, 'index.html', {'pies': get_mince_pies()})


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == "POST":
        if request.POST['alcohol'] == 'yes':
            alcohol = True
        else:
            alcohol = False
        MincePie.objects.create(name=request.POST['name'], brand=request.POST['brand'],
                                cost=request.POST['cost'], alcohol=alcohol,
                                amount_in_box=request.POST['amount'], rating=0,
                                price_per_pie=price_per_pie(float(request.POST['cost']), float(request.POST['amount'])),
                                times_rated=0)
        return redirect('home')
    return render(request, 'register.html')
