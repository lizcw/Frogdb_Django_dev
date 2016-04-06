from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.utils import timezone
from .models import Permit, Frog, Operation
from .forms import PermitForm, FrogForm, FrogDeathForm, FrogDisposalForm,OperationForm, LoginForm

## Index page
class IndexView(generic.ListView):
    template_name = 'frogs/index.html'
    context_object_name = 'shipment_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Permit.objects.order_by('-arrival_date')[:5]

## Home page - Landing page on login
class HomeView(generic.ListView):
    template_name = 'frogs/home.html'
    context_object_name = 'shipment_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Permit.objects.order_by('-arrival_date')[:5]
## Login
def logoutfrogdb(request):
    logout(request)
    return redirect('/frogs')
    # Redirect to a success page.

def loginfrogdb(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print('DEBUG: user=', user)
    message = None
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            message = 'Your account has been disabled. Please contact admin.'
    else:
        # Return an 'invalid login' error message.
        message = 'Login credentials are invalid. Please try again'
    return render(request, "frogs/home.html", {'errors': message, 'user': user})

#### PERMITS/SHIPMENTS
class PermitList(generic.ListView):
    template_name = 'frogs/shipmentlist.html'
    context_object_name = 'shipment_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Permit.objects.order_by('-arrival_date')

class PermitDetail(generic.DetailView):
    model = Permit
    context_object_name = 'shipment'
    template_name = 'frogs/shipmentview.html'


class PermitCreate(generic.CreateView):
    model = Permit
    template_name = 'frogs/permitcreate.html'
    form_class = PermitForm
    success_url = reverse_lazy('frogs:permit_list')

class PermitUpdate(generic.UpdateView):
    model = Permit
    form_class = PermitForm
    template_name = 'frogs/permitcreate.html'
    success_url = reverse_lazy('frogs:permit_list')

class PermitDelete(generic.DeleteView):
    model = Permit
    success_url = reverse_lazy("frogs:permit_list")


########## FROGS ############################################
class FrogList(generic.ListView):
    template_name = 'frogs/froglist.html'
    context_object_name = 'frogs'

    def get_queryset(self):
        return Frog.objects.order_by('-frogid')

class FrogDetail(generic.DetailView):
    model = Frog
    context_object_name = 'frog'
    template_name = 'frogs/frogview.html'

class FrogCreate(generic.CreateView):
    model = Frog
    template_name = 'frogs/frogcreate.html'
    form_class = FrogForm

    def get_success_url(self):
        return reverse('frogs:frog_detail', args=[self.object.id])

class FrogUpdate(generic.UpdateView):
    model = Frog
    form_class = FrogForm
    template_name = 'frogs/frogcreate.html'

    def get_success_url(self):
        return reverse('frogs:frog_detail', args=[self.object.id])

class FrogDelete(generic.DeleteView):
    model = Frog
    success_url = reverse_lazy("frogs:frog_list")

class FrogDeath(generic.UpdateView):
    model = Frog
    form_class = FrogDeathForm
    context_object_name = 'frog'
    template_name = 'frogs/frogdeath.html'

    def get_success_url(self):
        return reverse('frogs:frog_detail', args=[self.object.id])

class FrogDisposal(generic.UpdateView):
    model = Frog
    form_class = FrogDisposalForm
    context_object_name = 'frog'
    template_name = 'frogs/frogdisposal.html'

    def get_success_url(self):
        return reverse('frogs:frog_detail', args=[self.object.id])

########## OPERATIONS ############################################
class OperationSummary(generic.ListView):
    template_name = 'frogs/operationsummary.html'
    context_object_name = 'summaries'

    def get_queryset(self):
        #Get Operations first
        ops = Operation.objects.all().values_list('frogid')
        print('DEBUG: ops=', ops)
        #TODO Add species filter
        return Frog.objects.filter(id__in=ops).order_by('-frogid')

class OperationDetail(generic.DetailView):
    model = Operation
    context_object_name = 'operation'
    template_name = 'frogs/operationview.html'


## 1. Set frogid then 2. Increment opnum
## TODO: Limits: 6 operations and 6 mths apart
class OperationCreate(generic.CreateView):
    model = Operation
    template_name = 'frogs/operationcreate.html'
    form_class = OperationForm

    def get_success_url(self):
        frog = Frog.objects.filter(frogid=self.object.frogid)
        return reverse('frogs:frog_detail', args=[frog[0].id])


    def get_initial(self):
        fid = self.kwargs.get('frogid')
        print('DEBUG: pk frogid=', fid)
        frog = Frog.objects.get(pk=fid)
        print('DEBUG: frogid=', frog.frogid)
        ## next opnum
        opnum = 1 #default
        if (frog.operation_set.all()):
            opnum = frog.operation_set.count() + 1
        return {'frogid': frog, 'opnum': opnum}


class OperationUpdate(generic.UpdateView):
    model = Operation
    form_class = OperationForm
    template_name = 'frogs/operationcreate.html'

    def get_success_url(self):
        frogid = self.object.frogid
        frog = Frog.objects.filter(frogid=frogid)
        fid = frog[0].id
        print('DEBUG: frogid=', fid )
        return reverse('frogs:frog_detail', args=[fid])


class OperationDelete(generic.DeleteView):
    model = Operation

    def get_success_url(self):
        frog = Frog.objects.filter(frogid=self.object.frogid)
        return reverse('frogs:frog_detail', args=[frog[0].id])