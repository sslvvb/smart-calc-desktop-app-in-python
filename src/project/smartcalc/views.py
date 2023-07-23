from django.shortcuts import render
from .services import services
import logging
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import JsonResponse


# logger = logging.getLogger(__name__)


def index(request):
    """Веб-сервис, выполняющий вычисление выражения"""
    data: dict = _collect_basic_data()

    if request.method == 'POST':
        if 'equal' in request.POST:
            expression: str = request.POST.get('expression')
            x_value: str = request.POST.get('x_num')
            result: str = services.get_expression_result(expression, x_value)
            if result != "Error in expression":
                data['history'] = services.write_history(f'{expression}={result}; x={x_value}')
            # logger.info(f'{expression}={result}; x={x_value}')
            data['expression_or_result'] = result
            data['x_value'] = x_value

    return render(request, "index.html", data)


def clean_history(request):
    if request.method == 'POST':
        services.clean_history()
        # logger.info('Clean history file.')
    return HttpResponseRedirect("/")


def change_background(request):
    return _change_config(request, 'background', 'Change background')


def change_main_color(request):
    return _change_config(request, 'main_color', 'Change main accent color')


def change_font_size(request):
    return _change_config(request, 'font_size', 'Change font size')


def graph(request):
    """Веб-сервис, выполняющий отрисовку графика выражения"""
    data: dict = _collect_basic_data()
    if request.method == 'POST':
        expression = request.POST.get('expression')
        data['expression'] = expression
        data['x_min'] = request.POST.get('x_min')
        data['x_max'] = request.POST.get('x_max')
        data['y_min'] = request.POST.get('y_min')
        data['y_max'] = request.POST.get('y_max')
        result: list = services.calculate_graph_expression_result(data['expression'], data['x_min'], data['x_max'])
        if result is None:
            data['expression'] = 'Error in expression'
            # logger.warning(f'Error in expression for graph: {expression}')
        else:
            xy_values: list = [{'x': x, 'y': y} for x, y in zip(result[0], result[1])]
            data['xy_values'] = xy_values
            # logger.info(f'Print graph for: {expression}')
    return render(request, 'graph.html', data)


def about(request):
    data: dict = _collect_basic_data()
    # logger.info('Move to About page')
    return render(request, "about.html", data)


def _collect_basic_data() -> dict:
    config: dict = services.read_config()
    data: dict = {'history': services.read_history(),
                  'background': config['background'],
                  'font_size': config['font_size'],
                  'main_color': config['main_color']}
    return data


def _change_config(request, setting_name, log_message):
    if request.method == 'POST':
        setting_value = request.POST.get(setting_name)
        # if services.update_config(setting_name, setting_value):
        #     logger.info(f'{log_message} to {setting_value}')
        # else:
        #     logger.warning(f'Failed to {log_message} to {setting_value}')
    return HttpResponseRedirect("/")

def server_ready(request):
    # Perform any checks to verify the server's readiness
    # For example, check if the database is connected, caches are warmed up, etc.
    if _all_checks_pass():
        return JsonResponse({'status': 'ready'})
    else:
        return JsonResponse({'status': 'not_ready'}, status=503)  # Return a 503 status code if not ready

def _all_checks_pass():
    return True

# def page_not_found(request, exception):
#     # сюда добавить красивую страничку для 404
#     return HttpResponseNotFound("sslvvb Страница не найдена")
