class Skyline:
    def get_skyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2
        left = self.get_skyline(buildings[:mid])
        right = self.get_skyline(buildings[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        h1, h2 = 0, 0
        i, j = 0, 0
        result = []

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                h1 = left[i][1]
                corner = left[i][0]
                i += 1
            elif right[j][0] < left[i][0]:
                h2 = right[j][1]
                corner = right[j][0]
                j += 1
            else:
                h1 = left[i][1]
                h2 = right[j][1]
                corner = right[j][0]
                i += 1
                j += 1
            if self.is_valid(result, max(h1, h2)):
                result.append([corner, max(h1, h2)])
        result.extend(right[j:])
        result.extend(left[i:])
        return result

    def is_valid(self, result, new_height):
        return not result or result[-1][1] != new_height

if __name__ == "__main__":
    output = Skyline()
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(output.get_skyline(buildings))
