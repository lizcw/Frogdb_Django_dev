from django.conf.urls import url
from django.contrib.auth.views import login
from . import views, reports

app_name = 'frogs'
urlpatterns = [
    ##Using generic views instead
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.loginfrogdb, name='loginform'),
    url(r'^logout/$', views.logoutfrogdb, name='logout'),
    url(r'^permit/create/$',
        views.PermitCreate.as_view(), name="permit_create"),
    url(r'^permit/(?P<pk>\d+)/$',
        views.PermitDetail.as_view(), name="permit_detail"),
    url(r'^permit/(?P<pk>\d+)/update/$',
        views.PermitUpdate.as_view(), name="permit_update"),
    url(r'^permit/(?P<pk>\d+)/delete/$',
        views.PermitDelete.as_view(), name="permit_delete"),
    url(r'^permit/list/$',
        views.PermitList.as_view(), name='permit_list'),
    url(r'^frog/list/$',
        views.FrogList.as_view(), name='frog_list'),
    url(r'^frog/list/(?P<shipmentid>\w+)/$',
        views.FrogList.as_view(), name='frog_list_byshipment'),
    url(r'^frog/create/$',
        views.FrogCreate.as_view(), name="frog_create"),
    url(r'^frog/(?P<pk>\d+)/$',
        views.FrogDetail.as_view(), name="frog_detail"),
    url(r'^frog/(?P<pk>\d+)/update/$',
        views.FrogUpdate.as_view(), name="frog_update"),
    url(r'^frog/(?P<pk>\d+)/delete/$',
        views.FrogDelete.as_view(), name="frog_delete"),
    url(r'^frog/(?P<pk>\d+)/death/$',
        views.FrogDeath.as_view(), name="frog_death"),
    url(r'^frog/(?P<pk>\d+)/disposal/$',
        views.FrogDisposal.as_view(), name="frog_disposal"),
    url(r'^frog/upload/(?P<frogid>\w+)/$',
        views.FrogAttachment.as_view(), name="frog_upload"),
    url(r'^frog/bulkcreate/(?P<shipmentid>\d+)/$',
        views.FrogBulkCreate.as_view(), name="bulkfrog_create"),
    url(r'^frog/bulkdelete/(?P<shipmentid>\d+)/$',
        views.FrogBulkDelete.as_view(), name="bulkfrog_delete"),
    url(r'^frog/bulkdisposal/$',
        views.FrogBulkDisposal.as_view(), name="frog_bulkdisposal"),
    url(r'^operation/summary/(?P<species>\w+(?:\.\w+)?)?/$',
        views.OperationSummary.as_view(), name='operation_summary'),
    url(r'^operation/create/(?P<frogid>\w+)/$',
        views.OperationCreate.as_view(), name="operation_create"),
    url(r'^operation/(?P<pk>\d+)/update/$',
        views.OperationUpdate.as_view(), name="operation_update"),
    url(r'^operation/(?P<pk>\d+)/delete/$',
        views.OperationDelete.as_view(), name="operation_delete"),
    url(r'^transfer/list/$',
        views.TransferList.as_view(), name='transfer_list'),
    url(r'^transfer/list/(?P<operationid>\w+)/$',
        views.TransferList.as_view(), name='transfer_list_byop'),
    url(r'^transfer/create/(?P<operationid>\w+)/$',
        views.TransferCreate.as_view(), name="transfer_create"),
    url(r'^transfer/(?P<pk>\d+)/$',
        views.TransferDetail.as_view(), name="transfer_detail"),
    url(r'^transfer/(?P<pk>\d+)/update/$',
        views.TransferUpdate.as_view(), name="transfer_update"),
    url(r'^transfer/(?P<pk>\d+)/delete/$',
        views.TransferDelete.as_view(), name="transfer_delete"),
    url(r'^experiment/list/$',
        views.ExperimentList.as_view(), name='experiment_list'),
    url(r'^experiment/list/(?P<transferid>\w+)/$',
        views.ExperimentList.as_view(), name='experiment_list_bytransfer'),
    url(r'^experiment/create/(?P<transferid>\w+)/$',
        views.ExperimentCreate.as_view(), name="experiment_create"),
    url(r'^experiment/(?P<pk>\d+)/$',
        views.ExperimentDetail.as_view(), name="experiment_detail"),
    url(r'^experiment/(?P<pk>\d+)/update/$',
        views.ExperimentUpdate.as_view(), name="experiment_update"),
    url(r'^experiment/(?P<pk>\d+)/delete/$',
        views.ExperimentDelete.as_view(), name="experiment_delete"),
    url(r'^experiment/(?P<pk>\d+)/disposal/$',
        views.ExperimentDisposal.as_view(), name="experiment_disposal"),
    url(r'^experiment/(?P<pk>\d+)/autoclave/$',
        views.ExperimentAutoclave.as_view(), name="experiment_autoclave"),
    url(r'^disposal/list/$',
        views.DisposalList.as_view(), name="disposal_list"),
    url(r'report/$', reports.some_view, name="test_report"),
    ]
