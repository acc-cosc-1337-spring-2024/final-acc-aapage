#write functions here, don't add input('') statements here!
def test_config():
    return True

def calculate_stats(numlist):
    lowest = min(numlist)
    highest = max(numlist)
    total = sum(numlist)
    average = total / len(numlist)

    return lowest, highest, total, average
