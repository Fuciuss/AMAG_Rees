import numpy as np
from pathlib import Path
from functools import partial
from matplotlib import pyplot as plt


class VehicleData:
    def __init__(
        # init with data file
        self,
        data_input: str or Path,
    ):
        self.data = np.load(data_input)
        self.segments = self._parse(self.data)

    def _parse(self, data: np.ndarray) -> dict[id, np.ndarray]:
        segments = {}
        unique_ids = set(self.data[:, 1])
        for uid in unique_ids:
            uid_data = data[data[:, 1] == uid]
            # Select just the lat and lon
            tuples = [(row[2], row[3]) for row in uid_data]
            segments[uid] = tuples
        return segments

    def by_id(self, id: int) -> int:
        return self.segments[id]

    def filter(self, function: callable):
        filtered_segments = []
        for segment in self.segments.values():
            if function(segment):
                filtered_segments.append(segment)
        return filtered_segments

    def plot(self, segments):
        for segment in segments:
            segment = np.array(segment)
            x, y = segment[:, 0], segment[:, 1]
            plt.plot(x, y)

        plt.show()
        return plt


