def percent_cal(val_new, val_target):
    if val_new == 0 or val_target == 0:
        return 0
    percent = (val_new / val_target)
    return percent


def percentTarget(target_results, model_results):
    result_list = []

    for value in enumerate(model_results):
        index = value[0]
        model_stiffness = value[1]
        target_stiffness = target_results[index]

        percent = percent_cal(model_stiffness, target_stiffness)

        result_list.append(percent)

    stiffness_percent = zip(model_results, result_list)
    return stiffness_percent
