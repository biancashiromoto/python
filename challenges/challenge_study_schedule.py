def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for student_permanence in permanence_period:
        entry_time = student_permanence[0]
        out_time = student_permanence[1]
        if (
            entry_time is None or not isinstance(entry_time, int)
          ) or (
            out_time is None or not isinstance(out_time, int)
          ):
            return None
        if (int(entry_time) <= target_time <= int(out_time)):
            counter += 1
    return counter


