from django.shortcuts import render
from math import pi

def index(request):
    area = None
    volume = None
    form_data = {}
    project_description = """
    веб-приложение предоставляет возможность пользователям вводить значения длины, ширины и высоты фундамента и получать рассчитанный объем бетонной смеси.
    """

    if request.method == 'POST':
        length = float(request.POST.get('length', 0))
        width = float(request.POST.get('width', 0))
        height = float(request.POST.get('height', 0))

        form_data['length'] = length
        form_data['width'] = width
        form_data['height'] = height

        if 'calculate_area' in request.POST:
            # Расчет площади пола
            area = length * width
        elif 'calculate_volume' in request.POST:
            # Расчет объема бетонной смеси
            volume = length * width * height
    
    context = {
        "title": "Рассчет объема бетонной смеси",
        "subtitle": "Производственная практика (практика в ИТ-сфере)",
        "description": project_description,
        "area": area,
        "volume": volume,
        "form_data": form_data,
        "developer_info": {
            "name": "Коваленко А.А.",
            "university": "Росдистант",
            "year": "2025"
        }
    }
    return render(request, "index.html", context)