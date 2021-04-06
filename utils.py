#!/usr/bin/env python3

def calc_subtask_ids(total_num, num_tasks=2):
    """
    Split the task into sub-tasks.

    Parameters:
    -----------
    total_num: int
        Total number of the task to be split.
    num_tasks: int
        The number of sub-tasks.

    Returns:
    --------
    subtask_ids: list of list
        List of the list of ids. Eg.
        [[0, 1], [2, 3, 4]]
    """
    subtask_ids = []
    num_per_task = total_num // num_tasks
    for i in range(num_tasks):
        if i < num_tasks-1:
            ids = list(range(i*num_per_task, (i+1)*num_per_task, 1))
        else:
            ids = list(range(i*num_per_task, total_num))
        subtask_ids.append(ids)
    return subtask_ids
        
        


