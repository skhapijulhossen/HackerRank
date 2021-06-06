def breakingRecords(scores):
    # Write your code here
    high=scores[0]; low=scores[0]
    min_breaked = 0; max_breaked = 0
    for score in scores:
        if score < low:
            low = score
            min_breaked += 1
        elif score > high:
            high = score
            max_breaked += 1
        else:
            pass
    return [max_breaked ,min_breaked]