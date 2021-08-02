from django.core.exceptions import RequestAborted
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView


class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = "contact_list"
    

    def get_queryset(self):

        contacts = Contact.objects.all()
        return contacts

class ContactCreateView(CreateView):
    model = Contact
    # template_name = 'crudapp/create.html'

    def post(self, request):
        # breakpoint()
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        form = ContactForm()

        return render(request, 'crudapp/create.html', {'form': form})

class ContactDetailView(DetailView):
    model = Contact
    form_class = ContactForm
    template_name = 'crudapp/create.html'

    def get(self, request):
        return render(request, self.template_name, {"form":self.form_class})
            





    def edit(request, pk, template_name='crudapp/edit.html'):
        contact = get_object_or_404(Contact, pk=pk)

        form = ContactForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, template_name, {'form': form})

    def delete(request, pk, template_name='crudapp/confirm_delete.html'):
        contact = get_object_or_404(Contact, pk=pk)
        if request.method=='POST':
            contact.delete()
            return redirect('index')
        return render(request, template_name, {'object': contact})