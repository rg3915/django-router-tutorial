from apps.core.custom_router import router
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import PersonForm
from .mixins import SearchMixin
from .models import Person


@router.path()
def person_list(request):
    template_name = 'crm/person_list.html'
    object_list = Person.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(email__icontains=search)
        )

    context = {'object_list': object_list}
    return render(request, template_name, context)


@router.path()
def person_detail(request, pk):
    template_name = 'crm/person_detail.html'
    obj = Person.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


@router.path()
def person_create(request):
    template_name = 'crm/person_form.html'
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('crm:person_list')

    context = {'form': form}
    return render(request, template_name, context)


@router.path()
def person_update(request, pk):
    template_name = 'crm/person_form.html'
    instance = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('crm:person_list')

    context = {'form': form}
    return render(request, template_name, context)


@router.path()
def person_delete(request, pk):
    template_name = 'crm/person_confirm_delete.html'
    obj = Person.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('crm:person_list')

    context = {'object': obj}
    return render(request, template_name, context)


@router.path()
class PersonListView(SearchMixin, ListView):
    model = Person
    paginate_by = 10


@router.path()
class PersonDetailView(DetailView):
    model = Person


@router.path()
class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm


@router.path()
class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm


@router.path()
class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('crm:person_list')


@router.path()
def person_export_csv(request):
    return HttpResponse('export-person')


@router.path('person/export/csv/')
def person_export_csv2(request):
    return HttpResponse('export-person')


@router.path('person/export/excel/')
def person_export_excel(request):
    return HttpResponse('export-person')
