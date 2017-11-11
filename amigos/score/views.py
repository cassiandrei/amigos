from django.shortcuts import render
from  accounts.models import Match


# Create your views here.
@login_required
def list_friends(request):
    matches = Match.objects.calc_points(user=request.user)
    return render(request, 'score/list_friends.html', {'matches': matches})
