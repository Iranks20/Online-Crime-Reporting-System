from django.urls import path, include
from django.contrib import admin
from comment.views import CreateComment
from comment.views import HomePage, CommentPage
from home.views import criminal_directory
from home.views import upload_evidence
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from police.views import person_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', TemplateView.as_view(template_name="about.html"), name="about"),
    path('contact', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('police/', include('police.urls')),
    path('anonymous/', include('home.url_anonymous')),
    path('citizen/', include('citizen.urls')),
    path('comment/ajax/create', CreateComment, name="create_comment"),
    path('comment/', CommentPage, name="comment"),
    path('criminal_directory/', criminal_directory, name="criminal_directory"),
    path('evidence/<int:id>/upload', upload_evidence, name="upload_anonymous_evidence"),
    path('person_detail/<str:id>/', person_detail_view, name='person_detail'),
    path('', HomePage, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
