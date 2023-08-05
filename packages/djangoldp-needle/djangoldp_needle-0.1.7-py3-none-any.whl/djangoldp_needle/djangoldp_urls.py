from django.conf.urls import url
from .models import Annotation, Tag, AnnotationTarget, NeedleActivity
from .views import AnnotationViewset, AnnotationTargetViewset, TagViewset, AnnotationTargetIntersectionViewset

urlpatterns = [
    url(r'^annotations/', AnnotationViewset.urls(model_prefix="annotation", model=Annotation)),
    url(r'^annotationtargets/', AnnotationTargetViewset.urls(model_prefix="annotationtarget", model=AnnotationTarget)),
    url(r'^annotationtargetsintersection', AnnotationTargetIntersectionViewset.as_view({'get': 'list'}, model=AnnotationTarget)),
    url(r'^users/(?P<slug>[\w\-\.]+)/yarn/', AnnotationViewset.urls(model_prefix="yarn", model=Annotation)),
    url(r'^users/(?P<slug>[\w\-\.]+)/tags', TagViewset.urls(model_prefix="tags", model=Tag)),
]
