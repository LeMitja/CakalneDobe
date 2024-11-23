from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CakDobe
# Create your views here.
def home(request):
    return render(request, "home.html")

def databasetest(request):
    items = CakDobe.objects.all()
    return render(request, 'databasetest.html', {"CakDobe": items})

def get_chart_data(request):
    if request.method == "POST":
        body = json.loads(request.body)
        vzs_naziv = body.get("vzs_naziv")
        print(vzs_naziv)
        # Query for the most recent record for the selected vzs_naziv
        record = CakDobe.objects.filter(vzs_naziv=vzs_naziv).order_by('-recorded_date').first()
        print(record.recorded_date)
        if record:
            data = {
                "povprecna_cd_zelo_h": record.povprecna_cd_zelo_h,
                "povprecna_cd_hitro": record.povprecna_cd_hitro,
                "povprecna_cd_redno": record.povprecna_cd_redno,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "No data found"}, status=404)
        
def search_vzs(request):
    query = request.GET.get('query', '')
    results = CakDobe.objects.filter(vzs_naziv__icontains=query).values('vzs_naziv')[:500]  # Limit results to avoid excessive data
    return JsonResponse({
        'results': [{'vzs_naziv': item['vzs_naziv']} for item in results]
    })