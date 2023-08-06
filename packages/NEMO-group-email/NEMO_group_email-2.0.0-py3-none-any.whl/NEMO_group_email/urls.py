from django.conf.urls import url

from NEMO_group_email.views import email

urlpatterns = [
    url(r"^email_broadcast/$", email.email_broadcast, name="email_broadcast"),
    url(
        r"^email_broadcast/(?P<audience>tool|area|account|project|user|group)/$",
        email.email_broadcast,
        name="email_broadcast",
    ),
]
