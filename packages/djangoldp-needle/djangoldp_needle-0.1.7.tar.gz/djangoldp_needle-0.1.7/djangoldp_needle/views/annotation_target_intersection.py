from django.core.exceptions import SuspiciousOperation
from djangoldp.serializers import LDPSerializer
from djangoldp.views import LDPViewSet
from rest_framework import serializers

from ..models import AnnotationTarget, Annotation


class AnnotationTargetIntersectionSerialier(LDPSerializer):
    intersection_total = serializers.SerializerMethodField()
    intersection_total_before = serializers.SerializerMethodField()
    intersection_total_after = serializers.SerializerMethodField()

    @property
    def with_cache(self):
        return False

    class Meta:
        fields = ['urlid', 'intersection_total', 'intersection_total_before', 'intersection_total_after']

    def get_intersection_total(self, obj):
        return obj.annotations.count() - 1

    def get_intersection_total_before(self, obj):
        return obj.annotations.filter(creation_date__lt=self.get_annotation_date()).count()

    def get_intersection_total_after(self, obj):
        return obj.annotations.filter(creation_date__gt=self.get_annotation_date()).count()

    def get_annotation_date(self):
        if 'annotation_date' not in self.context['request'].query_params:
            raise SuspiciousOperation('Invalid request')
        return self.context['request'].query_params['annotation_date']

class AnnotationTargetIntersectionViewset(LDPViewSet):
    model = AnnotationTarget
    serializer_class = AnnotationTargetIntersectionSerialier


    def get_queryset(self, *args, **kwargs):
        if 'url' not in self.request.query_params:
            raise SuspiciousOperation('Invalid request')

        url = self.request.query_params['url']

        return AnnotationTarget.objects.filter(target=url)
