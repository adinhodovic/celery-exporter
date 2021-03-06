# pylint: disable=protected-access
from .exporter import Exporter

prometheus_logo = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@((((((((((((((((((((((@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@((((((((((((((@@((((((((((((((((@@@@@@@@@@@@@@
@@@@@@@@@@@((((((((((((((((@@@(((((((((((((((((((@@@@@@@@@@@
@@@@@@@@(((((((((((((((((((@@@@(((((@(((((((((((((((@@@@@@@@
@@@@@@(((((((((((((((@@((((@@@@@(((@@(((((((((((((((((@@@@@@
@@@@@((((((((((((((((@@@((@@@@@@@(@@@@((((((((((((((((((@@@@
@@@(((((((((((((((((@@@@(@@@@@@@@(@@@@@((((((((((((((((((@@@
@@(((((((((((((((((@@@@@@@@@@@@@@(@@@@@@((((((((((((((((((@@
@(((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@((((((((((((((((((@
@(((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@((((((((((((((((((@
@(((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((((((
(((((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((((((
@(((((((((((@@@@((((@@@@@@@@@@@@@@@@@@@(((((@@@@((((((((((((
@((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((((@
@((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((((((@
@@((((((((((((((((((((((((((((((((((((((((((((((((((((((((@@
@@@(((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((@@@
@@@@((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((((@@@@
@@@@@@((((((((((((((((((((((((((((((((((((((((((((((((@@@@@@
@@@@@@@@((((((((((((((@@@@@@@@@@@@@@@@((((((((((((((@@@@@@@@
@@@@@@@@@@(((((((((((((@@@@@@@@@@@@@@(((((((((((((@@@@@@@@@@
@@@@@@@@@@@@@@(((((((((((#@@@@@@@@@(((((((((((&@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@((((((((((((((((((((((((@@@@@@@@@@@@@@@@@@"""

cmd_help = (
    prometheus_logo
    + """

A Prometheus exporter for Celery.

Metrics exposed:
"""
)

temp_exporter = Exporter()

for metric in temp_exporter.state_counters.values():
    cmd_help += f"""
\b
{metric._name}_total
{metric._documentation:30s}
"""
