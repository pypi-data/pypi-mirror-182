from dataclasses import dataclass
from typing import Optional, Tuple, Union

import numpy as np
import numpy.typing as npt
import pyarrow as pa
from typing_extensions import TypedDict

# Type declaration/helpers local to this file
#
Coordinates = Tuple[Union[slice, int, npt.ArrayLike], ...]
ValueFilter = str

MatrixAxisQuery = TypedDict(
    "MatrixAxisQuery",
    {
        "obs": "AxisQuery",
        "var": "AxisQuery",
    },
)


@dataclass()
class AxisQuery:
    """
    Define a single-axis dataframe query based upon either a value filter predicate or coordinates.

    Can have value:
    * None - no query, ie, all data
    * Coordinates - a set of coordinates on the axis dataframe index (or soma_rowids if a dense dataframe)
    * A SOMA `value_filter` across columns in the axis dataframe

    Examples:
    ```
        AxisQuery()
        AxisQuery(coords=[0,1,2])
        AxisQuery(value_filter="tissue == 'lung'")
    ```
    """

    value_filter: Optional[str] = None
    coords: Optional[Coordinates] = None

    def __post_init__(self) -> None:
        # TODO: Error class
        if not (self.value_filter is None) != (self.coords is None):
            raise Exception("FilterSpec - value_filter or coords may be specified, but not both.")

        if self.value_filter is not None:
            # If a a value_filter, default to all coords
            self.coords = (slice(None),)
        else:
            if not isinstance(self.coords, tuple):
                raise Exception("FilterSpec - coords must be tuple of int, slice or numpy.array_like")
            coords = []
            for c in self.coords:
                if isinstance(c, int) or isinstance(c, slice):
                    coords.append(c)
                else:
                    coords.append(pa.array(np.array(c, dtype=np.int64)))
            self.coords = tuple(coords)

    def is_value_filter(self) -> bool:
        """Return True if this is a value filter, else False if coordinates"""
        return self.value_filter is not None
