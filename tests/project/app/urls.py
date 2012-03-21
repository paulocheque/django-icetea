from django.conf.urls.defaults import *
from icetea.resource import Resource
from handlers import ClientHandler, AccountHandler, ContactHandler

client_handler = Resource(ClientHandler)
account_handler = Resource(AccountHandler)
contact_handler = Resource(ContactHandler)

urlpatterns = patterns('',
    url(r'^clients/$', client_handler),
    url(r'^clients/(?P<id>\d+)/$', client_handler),
    url(r'^accounts/$', account_handler),
    url(r'^accounts/(?P<id>\d+)/$', account_handler),
    url(r'^contacts/$', contact_handler),
    url(r'^contacts/(?P<id>\d+)/$', contact_handler),
)
