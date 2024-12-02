### AOC Day 2-1 ###

# INPUT = "aoc/2024/day2/input.txt"
INPUT = "aoc/2024/day2/input.txt"


def read_lines(path):
    with open(path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def parse_reports(lines):
    reports = []
    for numbers in lines:
        reports.append([int(num) for num in numbers.split()])
    return reports


def monotonic_report(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        return True
    return False


def safe_diff(report):
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(abs(report[i] - report[i + 1]))

    return all(
        n > 0 and n <= 3 for n in diffs
    )


def safe_report(report):
    if monotonic_report(report) and safe_diff(report):
        return True
    return False


def problem_dampener(report):
    for i in range(len(report)):
        c_report = report.copy()
        c_report.pop(i)
        if safe_report(c_report):
            return True
    return False
    
reports = parse_reports(read_lines(INPUT))

results = []
for report in reports:
    results.append(problem_dampener(report))


print(sum(results))
