from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("django-sortedm2m").version
except DistributionNotFound:
    # package is not installed
    __version__ = None
