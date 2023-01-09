import math
import colorama


# Print iterations progress
def progress_bar (progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    if progress == total:
        print(colorama.Fore.BLUE + f"\r{bar}| {percent:.2f}%\n")
    else:
        print(color + f"\r{bar}| {percent:.2f}%", end = "\r")


numbers = [x * 5 for x in range(2000, 3000)]
results = []
# A List of Items

# Initial call to print 0% progress
progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers), colorama.Fore.YELLOW)

print(colorama.Fore.RESET)


