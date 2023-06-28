from django.shortcuts import render
from .models import Task

def task_list(request):
    """
    Возвращает список задач, отфильтрованных по статусу (если задан) или все задачи.

    Args:
        request (HttpRequest): Запрос от клиента.

    Returns:
        HttpResponse: Ответ с рендером шаблона "task_list.html" и контекстом задач.

    """
    status = request.GET.get('status', '')
    tasks = Task.objects.filter(status=status) if status else Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
