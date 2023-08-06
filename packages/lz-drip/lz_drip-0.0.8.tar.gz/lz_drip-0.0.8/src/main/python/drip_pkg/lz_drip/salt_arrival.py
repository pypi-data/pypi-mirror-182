"""Define the SaltArrival class"""

from typing import List, Tuple

from drip import Dropper
from .bundle import find_bundles, Bundle
from .file_utils import read_config, select_source, select_destination, select_nosalt, select_threshold


class SaltArrival(Dropper):
    """
    This class provides the concrete implementation use by a Feeder
    instance to copy SPADE bundles from one directory into an area
    organized by their canonical path values.
    """

    def __init__(self, config_file: str, section: str):
        """
        Creates an instance of this class.

        :param source: the Path to the source directory
        :param destination: the Path to the destination directory
        """
        config = read_config(config_file, section)

        self.__src = select_source(config)
        self.__dst = select_destination(config)
        self.__nosalt = select_nosalt(config)
        self.__threshold = select_threshold(config)

    def assess_condition(self) -> Tuple[int, str]:
        """
        Assess whether a drip should be executed or not.

        :return maximum number if items that can be dropped and
        explanation of any limitations.
        """
        return self.__threshold, ""

    def drop(self, item):
        """
        "Drops" the supplied item, i.e. acts on that item.
        """
        item.move_to_canonical(self.__dst)

    def fill_cache(self) -> List[Bundle]:
        """
        Fills internal list of bundles to be moved.
        """
        bundles = find_bundles(self.__src)
        for bundle in bundles:
            if self.test_nosalt(bundle):
                bundle.move(self.__nosalt)
        return find_bundles(self.__src)

    def test_nosalt(self, bundle: Bundle) -> bool:
        return True
