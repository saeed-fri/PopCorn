from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'PopCorn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'phase2.views.register'),
    url(r'^forget/', 'phase2.views.forget'),
    url(r'^post/','phase2.views.post'),
    url(r'^movie/', 'phase2.views.movie'),
    url(r'^user/', 'phase2.views.profile'),
    url(r'^related/', 'phase2.views.related_user'),
    url(r'^login/', 'phase2.views.sign_in'),
    url(r'^timeline/', 'phase2.views.timeline'),
]
