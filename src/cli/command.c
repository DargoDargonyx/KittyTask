/**
 * @file command.c
 * @author DargoDargonyx
 * @date 08/19/2026
 */

#include "cli/command.h"
#include "cli/cli.h"
#include "util/helper.h"
#include "core/task.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>


int cli_command(int argc, char** argv) {
    if (strcmp(argv[1], "help") == 0) {
        cli_print_help();
        return 0;
    }
    if (strcmp(argv[1], "groups") == 0) {
        cli_list_groups();
        return 0;
    }
    
	if (strcmp(argv[1], "group") == 0) return group_command(argc, argv);
    if (strcmp(argv[1], "task") == 0) return task_command(argc, argv);

    printf(PRINT_ERROR "Unknown command: %s\n", argv[1]);
    return 1;
}

// Group commands

int group_command(int argc, char** argv) {
    if (argc < 3) {
        printf(PRINT_ERROR "Usage: ktask group <command>\n");
        return 1;
    }

    if (strcmp(argv[2], "add") == 0) return group_add_cmd(argc, argv);
    if (strcmp(argv[2], "delete") == 0) return group_delete_cmd(argc, argv);

    printf(PRINT_ERROR "Unknown group command: %s\n", argv[2]);
    return 1;
}

int group_add_cmd(int argc, char** argv) {
    if (argc != 4) {
        printf(PRINT_ERROR "Usage: ktask group add <title>\n");
        return 1;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return 1;

    if (!task_group_create(argv[3])) {
        printf(PRINT_ERROR "Failed to create group.\n");
        return 1;
    }

    printf(PRINT_KITTY "Group created: %s\n", argv[3]);
    return 0;
}

int group_delete_cmd(int argc, char** argv) {
    if (argc != 4) {
        printf(PRINT_ERROR "Usage: ktask group delete <id>\n");
        return 1;
    }
    char* end;
    
	long id = strtol(argv[3], &end, 10);
    if (*end != '\0' || id < 0 || id > INT_MAX) {
        printf("Invalid group ID: %s\n", argv[3]);
        return 1;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return 1;

    if (!task_group_delete((int) id)) {
        printf(PRINT_ERROR "Group %d not found.\n", (int) id);
        return 1;
    }

    printf(PRINT_KITTY "Group %d deleted.\n", (int) id);
    return 0;
}

// Task commands

int task_command(int argc, char** argv) {
    if (argc < 3) {
        printf(PRINT_ERROR "Usage: ktask task <command>\n");
        return 1;
    }

    if (strcmp(argv[2], "add") == 0) return task_add_cmd(argc, argv);
    if (strcmp(argv[2], "delete") == 0) return task_delete_cmd(argc, argv);
    if (strcmp(argv[2], "status") == 0) return task_status_cmd(argc, argv);
    if (strcmp(argv[2], "priority") == 0) return task_priority_cmd(argc, argv);

    printf(PRINT_ERROR "Unknown task command: %s\n", argv[2]);
    return 1;
}

int task_add_cmd(int argc, char** argv) {
    if (argc != 5) {
        printf(PRINT_ERROR "Usage: ktask task add <group_id> <title>\n");
        return 1;
    }
    char* end;
    
	long group_id = strtol(argv[3], &end, 10);
    if (*end != '\0' || group_id < 0 || group_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid group ID: %s\n", argv[3]);
        return 1;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return 1;

    TaskGroup* group = task_group_find((int) group_id);
    if (!group) {
        printf(PRINT_ERROR "Group %d not found.\n", (int) group_id);
        return 1;
    }

    if (!task_create(group, argv[4])) {
        printf(PRINT_ERROR "Failed to create task.\n");
        return 1;
    }

    printf(PRINT_KITTY "Task created in group %d.\n", (int) group_id);
    return 0;
}

int task_delete_cmd(int argc, char** argv) {
    if (argc != 5) {
        printf(PRINT_ERROR "Usage: ktask task delete <group_id> <task_id>\n");
        return 1;
    }
    char* end;
    
	long group_id = strtol(argv[3], &end, 10);
    if (*end != '\0' || group_id < 0 || group_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid group ID: %s\n", argv[3]);
        return 1;
    }

    long task_id = strtol(argv[4], &end, 10);
    if (*end != '\0' || task_id < 0 || task_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid task ID: %s\n", argv[4]);
        return 1;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return 1;

    TaskGroup* group = task_group_find((int) group_id);
    if (!group) {
        printf(PRINT_ERROR "Group %d not found.\n", (int) group_id);
        return 1;
    }

    if (!task_delete(group, (int) task_id)) {
        printf(PRINT_ERROR "Task %d not found.\n", (int) task_id);
        return 1;
    }

    printf(PRINT_KITTY "Task %d deleted.\n", (int) task_id);
    return 0;
}

int task_status_cmd(int argc, char** argv) {
    if (argc != 6) {
        printf(PRINT_ERROR "Usage: taskmgr task status <group_id> <task_id> <status>\n");
        printf(PRINT_INFO "Status: todo, progress, done\n");
        return 1;
    }
    char* end;

    long group_id = strtol(argv[3], &end, 10);
    if (*end != '\0' || group_id < 0 || group_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid group ID.\n");
        return 1;
    }

    long task_id = strtol(argv[4], &end, 10);
    if (*end != '\0' || task_id < 0 || task_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid task ID.\n");
        return 1;
    }

    TaskStatus status;
    if (strcmp(argv[5], "todo") == 0) {
        status = TASK_TODO;
    } else if (strcmp(argv[5], "progress") == 0) {
        status = TASK_IN_PROGRESS;
    } else if (strcmp(argv[5], "done") == 0) {
        status = TASK_COMPLETE;
    } else {
        printf("Invalid status: %s\n", argv[5]);
        return 1;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return 1;

    TaskGroup* group = task_group_find((int) group_id);
    if (!group) {
        printf(PRINT_ERROR "Group %d not found.\n", (int) group_id);
        return 1;
    }

    Task* task = task_find(group, (int) task_id);
    if (!task) {
        printf(PRINT_ERROR "Task %d not found.\n", (int) task_id);
        return 1;
    }

    if (!task_set_status(task, status)) {
        printf(PRINT_ERROR "Failed to set task status.\n");
        return 1;
    }

    printf(PRINT_KITTY "Task %d status updated.\n", (int) task_id);
    return 0;
}

int task_priority_cmd(int argc, char** argv) {
    if (argc != 6) {
        printf(PRINT_ERROR "Usage: taskmgr task priority <group_id> <task_id> <priority>\n");
        printf(PRINT_INFO "Priority: low, medium, high\n");
        return 1;
    }
    char* end;

    long group_id = strtol(argv[3], &end, 10);
    if (*end != '\0' || group_id < 0 || group_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid group ID.\n");
        return 1;
    }

    long task_id = strtol(argv[4], &end, 10);
    if (*end != '\0' || task_id < 0 || task_id > INT_MAX) {
        printf(PRINT_ERROR "Invalid task ID.\n");
        return 1;
    }

    TaskPriority priority;
    if (strcmp(argv[5], "low") == 0) {
        priority = PRIORITY_LOW;
    } else if (strcmp(argv[5], "medium") == 0) {
        priority = PRIORITY_MEDIUM;
    } else if (strcmp(argv[5], "high") == 0) {
        priority = PRIORITY_HIGH;
    } else {
        printf(PRINT_ERROR "Invalid priority: %s\n", argv[5]);
        return 1;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return 1;

    TaskGroup* group = task_group_find((int) group_id);
    if (!group) {
        printf(PRINT_ERROR "Group %d not found.\n", (int) group_id);
        return 1;
    }

    Task* task = task_find(group, (int) task_id);
    if (!task) {
        printf(PRINT_ERROR "Task %d not found.\n", (int) task_id);
        return 1;
    }

    if (!task_set_priority(task, priority)) {
        printf(PRINT_ERROR "Failed to set task priority.\n");
        return 1;
    }

    printf(PRINT_KITTY "Task %d priority updated.\n", (int) task_id);
    return 0;
}
