/**
 * @file task.h
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#ifndef TASK_H
#define TASK_H

#include "util/helper.h"


#define MAX_TASKS 1000
#define MAX_GROUPS 100

// Tasks
typedef enum {
	TASK_TODO,
	TASK_IN_PROGRESS,
	TASK_COMPLETE
} TaskStatus;

typedef enum {
	PRIORITY_LOW,
	PRIORITY_MEDIUM,
	PRIORITY_HIGH
} TaskPriority;

typedef struct {
	int id;
	char title[128];
	char description[1024];
	Date date;

	TaskStatus status;
	TaskPriority priority;
} Task;

typedef struct {
	int id;
	char title[128];

	Task tasks[1000];
	int task_count;
	int next_id;
} TaskGroup;

int task_create(TaskGroup*, const char*);
int task_delete(TaskGroup*, int);
Task* task_find(TaskGroup*, int);

int task_set_status(Task*, TaskStatus);
int task_set_priority(Task*, TaskPriority);

int task_group_create(const char*);
int task_group_delete(int);
TaskGroup* task_group_find(int);
void print_all_task_groups(void);

// Group container
typedef struct {
	TaskGroup task_groups[MAX_GROUPS];
	int task_group_count;
	int next_id;
} TaskGroupContainer;

int init_task_group_container(void);
void destroy_task_group_container(void);
TaskGroupContainer* get_task_group_container(void);


#endif // TASK_H
