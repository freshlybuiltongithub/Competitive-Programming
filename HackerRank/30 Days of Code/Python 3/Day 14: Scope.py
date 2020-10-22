"""
Hackerrank Solution for Day 14: Scope
"""
    def __init__(self,data):
        self.data = data
        self.maximumDifference = 0

    def computeDifference(self):
        d = self.data
        l = max(d)
        mi = min(d)
        self.maximumDifference = l-mi

	# Add your code here


