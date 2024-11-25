data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def calculate_sums(data):
    results = []
    for item in data:
        try:
            numbers = [int(x) for x in item.split(',')]
            results.append(sum(numbers))
        except ValueError:
            results.append("Не можу це зробити!")
    return results

print(calculate_sums(data))