/**
 * @file task.c
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#include "core/task.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


static TaskGroupContainer* task_group_container = NULL;

// Tasks

int task_create(TaskGroup* task_group, const char* title) {
	if (!task_group || !title) return 0;	

	Task task;

	strncpy(task.title, title, sizeof(task.title) - 1);
    task.title[sizeof(task.title) - 1] = '\0';
    task.description[0] = '\0';

    task.status = TASK_TODO;
    task.priority = PRIORITY_MEDIUM;	
	task.date = (Date) { .day = 0, .month = 0, .year = 0 };
	
	task.id = task_group->next_id++;  
	if (task_group->task_count <= MAX_TASKS) 
		task_group->tasks[task_group->task_count++] = task;

	return 1;
}

int task_delete(TaskGroup* task_group, int task_id) {
    if (!task_group) return 0;

    for (int i = 0; i < task_group->task_count; i++) {
        if (task_group->tasks[i].id == task_id) {
            for (int j = i; j < task_group->task_count - 1; j++) {
                task_group->tasks[j] = task_group->tasks[j + 1];
            }

            task_group->task_count--;
            return 1;
        }
    }

	printf(PRINT_WARNING "Unable to find the requested task to delete\n");
	return 1;
}

Task* task_find(TaskGroup* task_group, int task_id) {
    if (!task_group) return NULL;

    for (int i = 0; i < task_group->task_count; i++) {
        if (task_group->tasks[i].id == task_id) {
            return &task_group->tasks[i];
        }
    }

    return NULL;
}

int task_set_status(Task* task, TaskStatus status) {
    if (!task) return 0;
    if (status < TASK_TODO || status > TASK_COMPLETE) return 0;

    task->status = status;
    return 1;
}

int task_set_priority(Task* task, TaskPriority priority) {
	if (task == NULL) return 0;
    if (priority < PRIORITY_LOW || priority > PRIORITY_HIGH) return 0;

    task->priority = priority;
    return 1;
}

int task_group_create(const char* title) {
	if (!task_group_container || !title) return 0;

	TaskGroup task_group;
	strncpy(task_group.title, title, sizeof(task_group.title) - 1);
    task_group.title[sizeof(task_group.title) - 1] = '\0';

	task_group.id = task_group_container->next_id++;  
	if (task_group_container->task_group_count <= MAX_GROUPS) 
		task_group_container->task_groups[task_group_container->task_group_count++] = task_group;

	return 1;
}

int task_group_delete(int task_group_id) {
    if (task_group_container == NULL) return 0;

    for (int i = 0; i < task_group_container->task_group_count; i++) {
        if (task_group_container->task_groups[i].id == task_group_id) {

            for (int j = i; j < task_group_container->task_group_count - 1; j++) {
                task_group_container->task_groups[j] = task_group_container->task_groups[j + 1];
            }

            task_group_container->task_group_count--;
            return 1;
        }
    }

	printf(PRINT_WARNING "Unable to find the requested group to delete\n");
    return 1;
}

TaskGroup* task_group_find(int group_id) {
    if (task_group_container == NULL) return NULL;

    for (int i = 0; i < task_group_container->task_group_count; i++) {
        if (task_group_container->task_groups[i].id == group_id) {
            return &task_group_container->task_groups[i];
        }
    }

    return NULL;
}

void print_all_task_groups(void) {
    if (!task_group_container) return;

    if (task_group_container->task_group_count == 0) {
        printf("No groups found.\n");
        return;
    }

    printf("----------------------------------------\n");

    for (int i = 0; i < task_group_container->task_group_count; i++) {
        const TaskGroup* task_group = &task_group_container->task_groups[i];

        printf("ID: %d\n", task_group->id);
        printf("Name: %s\n", task_group->title);
        printf("Tasks: %d\n", task_group->task_count);
        printf("----------------------------------------\n");
    }
}


// Group container

int init_task_group_container(void) {
	if (task_group_container) {
		printf(PRINT_WARNING "Attempted to initialize the group container "
				"when it has already been initialized\n");
		return 0;
	}

	task_group_container = malloc(sizeof(TaskGroupContainer));
	return 1;
}

void destroy_task_group_container(void) {
	if (!task_group_container) {
		printf(PRINT_WARNING "Attempted to destroy a null group container\n");
		return;
	}

	free(task_group_container);
	task_group_container = NULL;
}

TaskGroupContainer* get_group_container(void) { return task_group_container; }
