"""Provide utilities to help using the lz_drip package"""

import os
from pathlib import Path

from drip import utils as drip_utils

_CONFIG_STRINGS = ["source", "destination", "nosalt"]
_SOURCE_INDEX = 0
_DESTINATION_INDEX = _SOURCE_INDEX + 1
_NOSALT_INDEX = _DESTINATION_INDEX + 1
_CONFIG_INTEGERS = ["threshold"]
_THRESHOLD_INDEX = 0

_SOURCE_ENVAR = "FILE_DRIP_SOURCE"
_DESTINATION_ENVAR = "FILE_DRIP_DESTINATION"
_NOSALT_ENVAR = "FILE_DRIP_NOSALT"
_THRESHOLD_ENVAR = "FILE_DRIP_THRESHOLD"
_DEFAULT_THRESHOLD = 8


def read_config(config_file, section) -> drip_utils.Configs:
    """
    Reads the supplied configuration ini

    :param config_file: the path to the file containing the configuration information.
    :param section: the section within the file containing the configuration for this instance.
    """
    return drip_utils.read_config(
        config_file, section, integers=_CONFIG_INTEGERS, strings=_CONFIG_STRINGS
    )


def select_source(config) -> Path:
    """
    Returns the Path to the selected bundles source
    """
    if _SOURCE_ENVAR in os.environ:
        drip_source = os.environ[_SOURCE_ENVAR]
    else:
        drip_source = str(config[_CONFIG_STRINGS[_SOURCE_INDEX]])
    if None is drip_source:
        raise ValueError(
            "source must be defined in configuration file,"
            + " or envar "
            + _SOURCE_ENVAR
            + " set"
        )
    source = Path(drip_source)
    if not source.exists():
        raise ValueError(f"{source.resolve()} does not exist!")
    return source


def select_destination(config) -> Path:
    """
    Returns the Path to the selected bundles destination
    """
    if _DESTINATION_ENVAR in os.environ:
        drip_destination = os.environ[_DESTINATION_ENVAR]
    else:
        drip_destination = str(config[_CONFIG_STRINGS[_DESTINATION_INDEX]])
    if None is drip_destination:
        raise ValueError(
            "destination must be defined in configuration file,"
            + " or envar "
            + _DESTINATION_ENVAR
            + " set"
        )
    destination = Path(drip_destination)
    if not destination.exists():
        raise ValueError(f"{destination.resolve()} does not exist!")
    if not destination.is_dir():
        raise ValueError(f"{destination.resolve()} is not a directory")
    return destination


def select_nosalt(config) -> Path:
    """
    Returns the Path to the salt destination for non-salt bundles
    """
    if _NOSALT_ENVAR in os.environ:
        drip_nosalt = os.environ[_NOSALT_ENVAR]
    else:
        drip_nosalt = str(config[_CONFIG_STRINGS[_NOSALT_INDEX]])
    if None is drip_nosalt:
        raise ValueError(
            "nosalt must be defined in configuration file,"
            + " or envar "
            + _NOSALT_ENVAR
            + " set"
        )
    nosalt = Path(drip_nosalt)
    if not nosalt.exists():
        raise ValueError(f"{nosalt.resolve()} does not exist!")
    if not nosalt.is_dir():
        raise ValueError(f"{nosalt.resolve()} is not a directory")
    return nosalt


def select_threshold(config) -> int:
    """
    Returns the Path to the selected file threshold
    """
    if _THRESHOLD_ENVAR in os.environ:
        drip_threshold = os.getenv(_THRESHOLD_ENVAR)
    else:
        threshold: int = int(config[_CONFIG_INTEGERS[_THRESHOLD_INDEX]])
        if None is threshold:
            return _DEFAULT_THRESHOLD
        return threshold
    return int(drip_threshold)
