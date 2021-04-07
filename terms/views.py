from django.shortcuts import render


def terms(request):
    """ A view to site the terms and conditions page """

    return render(request, 'terms/terms-and-conditions.html')


def privacy(request):
    """ A view to site the privacy page """

    return render(request, 'terms/privacy.html')
