from django.shortcuts import render


def indexPage(request):
    """
    Первая станица. Отображение всех комментарием.
    """
    return render(request, 'apprvc\index.html')