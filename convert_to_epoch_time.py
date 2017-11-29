# =============================================================================
# SaltStack utils File
#
# NAME: _utils/convert_to_epoch_time.py
# WRITTEN BY: Alek Tant of SmartAlek Solutions
# DATE  : 2016.07.11
#
# PURPOSE: Convert Salt Event Times into Epoch Times
#


from __future__ import absolute_import
from calendar import timegm
from time import strptime


def __virtual__():
    return "convert_to_epoch_time"


def convert_to_epoch_time(salt_event_time):
    '''
    Convert Salt Event Times into Epoch times.
    '''
    date_time = salt_event_time.split('.')[0]
    pattern = '%Y-%m-%dT%H:%M:%S'
    epoch_time = int(timegm(strptime(date_time, pattern)))
    return epoch_time
