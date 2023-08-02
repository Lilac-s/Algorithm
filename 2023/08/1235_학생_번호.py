def calculate_min_length(student_ids):
    min_length = 0
    for idx in range(1, len(student_ids[0]) + 1):
        truncated_ids = [student_id[:idx] for student_id in student_ids]
        if len(truncated_ids) == len(set(truncated_ids)):
            min_length = idx
            break
    return min_length


if __name__ == "__main__":
    student_ids = []
    num_ids = int(input())
    for _ in range(num_ids):
        student_id = input()[::-1]
        student_ids.append(student_id)
    print(calculate_min_length(student_ids))
