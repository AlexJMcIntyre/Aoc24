file = open("2_real.txt")
reports = file.readlines()


def check_seq(seq):
    if seq[1] > seq[0]:
        asc = 1  # the sequence is ascending
    else:
        asc = 0  # the sequence is descending

    for f_level in range(len(seq)-1):
        first = int(seq[f_level])
        second = int(seq[f_level+1])
        if first > second and asc == 1:
            return False
        elif first < second and asc == 0:
            return False
        elif not 1 <= abs(first-second) <= 3:
            return False
    # all shifts passed without error, return 0:
    return True


safe = 0
for report in reports:
    report = report.strip().split()

    if check_seq(report):
        # passes without any issues
        safe += 1
    else:
        for level in range(len(report)):
            report_check = report.copy()
            report_check.pop(level)
            if check_seq(report_check):
                safe += 1
                break

print(safe)
