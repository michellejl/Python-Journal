from django.shortcuts import render
from django.utils import timezone
from .models import Entry

# Create your views here.


def entry_list(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'journal/entry_list.html', {'entries': entries})


def entry_detail(request, pk):
    entry = Entry.objects.get(pk=pk)
    return render(request, 'journal/entry_detail.html', {'entry': entry})
