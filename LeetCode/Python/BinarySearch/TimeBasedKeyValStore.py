class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        values = self.dict[key]
        left, right = 0, len(values) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            mid_timestamp, mid_value = values[mid]

            if mid_timestamp == timestamp:
                return mid_value
            elif mid_timestamp < timestamp:
                res = mid_value  # potential answer
                left = mid + 1
            else:
                right = mid - 1

        return res
