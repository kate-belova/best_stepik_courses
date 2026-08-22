from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from courses.forms import CourseFilterForm
from courses.models import Course


def courses_list(request):
    form = CourseFilterForm(request.GET)
    courses = Course.objects.all()

    if form.is_valid():
        if form.cleaned_data["min_price"] is not None:
            courses = courses.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"] is not None:
            courses = courses.filter(price__lte=form.cleaned_data["max_price"])

        price_type = form.cleaned_data["price_type"]

        if price_type == "free":
            courses = courses.filter(is_free=True)
        elif price_type == "paid":
            courses = courses.filter(is_free=False)

        if form.cleaned_data["query"]:
            queries = [
                item.strip()
                for item in form.cleaned_data["query"].split(",")
                if item.strip()
            ]

            category_filter = Q()
            for query in queries:
                category_filter |= Q(categories__name__istartswith=query)

            courses = courses.filter(category_filter).distinct()

        if form.cleaned_data["ordering"]:
            courses = courses.order_by(form.cleaned_data["ordering"])

    return render(
        request, "courses/courses_list.html", {"courses": courses, "form": form}
    )


def course_detail(request, course_slug):
    course = get_object_or_404(
        Course,
        slug=course_slug,
    )
    return render(
        request,
        "courses/course_detail.html",
        {"course": course},
    )
