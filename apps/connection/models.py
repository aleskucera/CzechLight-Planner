from django.db import models
from jsonfield import JSONField

from apps.nodes.models import Device, TerminationPoint


class Connection(models.Model):
    main_path = JSONField(null=True, blank=True)
    alternative_paths = JSONField(null=True, blank=True)
    termination_points = models.ManyToManyField(TerminationPoint, related_name='termination_points')

    @property
    def name(self):
        """ Order the termination points in alphabetical order and return the name. """
        termination_points = sorted([tp.name for tp in self.termination_points.all()])
        if len(termination_points) == 0:
            return 'Without termination points'
        return ' - '.join(termination_points)

    def __str__(self):
        return f'Connection: {self.name}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.main_path == other.main_path and self.alternative_paths == other.alternative_paths

    def __hash__(self):
        return hash(self.main_path) + hash(self.alternative_paths)
