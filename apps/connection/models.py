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


class Channel(models.Model):
    lower_frequency = models.FloatField()
    upper_frequency = models.FloatField()

    def is_in_conflict(self, other):
        """ Check if the current channel is in conflict with another channel.

        Parameters:
            other (Channel): The other channel.

        Returns:
            bool: True if the current channel is in conflict with the other channel, False otherwise.
        """

        return self.lower_frequency <= other.lower_frequency <= self.upper_frequency or \
            self.lower_frequency <= other.upper_frequency <= self.upper_frequency or \
            other.lower_frequency <= self.lower_frequency <= other.upper_frequency or \
            other.lower_frequency <= self.upper_frequency <= other.upper_frequency

    def __str__(self):
        return f'{self.lower_frequency} - {self.upper_frequency}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.lower_frequency == other.lower_frequency and self.upper_frequency == other.upper_frequency

    def __hash__(self):
        return hash(self.lower_frequency) + hash(self.upper_frequency)
