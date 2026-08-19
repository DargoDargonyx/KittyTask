/**
 * @file cli.c
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#include "cli/cli.h"
#include "core/task.h"

#include <stdio.h>
#include <string.h>

int cli_run(void) {
	char input[256];
	printf(PRINT_INFO "Kitty Task => Type 'help' for commands.\n");

	int result;
	while (1) {
		printf(PRINT_KITTY);
		if (fgets(input, sizeof(input), stdin) == NULL) {
			result = 1;
			break;
		}
		input[strcspn(input, "\n")] = '\0';
		
		if (strcmp(input, "exit") == 0 
				|| strcmp(input, "quit") == 0
				|| strcmp(input, "q") == 0) {
			
			result = 0;
			break;
		}

		if (strcmp(input, "") == 0) continue;

		if (strcmp(input, "help") == 0)					cli_print_help();
		else if (strcmp(input, "groups") == 0)			cli_list_groups();
		else if (strcmp(input, "group add") == 0)		cli_create_group();
		else if (strcmp(input, "group delete") == 0)	cli_delete_group();
		else if (strcmp(input, "task add") == 0)		cli_add_task();
		else if (strcmp(input, "task delete") == 0)		cli_delete_task();
		else if (strcmp(input, "task status") == 0)		cli_set_status();
		else printf("Unknown command: %s\n", input);
	}

	return result;
}

void cli_print_help(void) {
    printf(PRINT_INFO "Commands:\n");
    printf("   <help>              Show this help message\n");
    printf("   <groups>            List task groups\n");
    printf("   <group add>         Create a group\n");
    printf("   <group delete>      Delete a group\n");
    printf("   <task add>          Create a task\n");
    printf("   <task delete>       Delete a task\n");
    printf("   <task status>       Change task status\n");
    printf("   <task priority>     Change task priority\n");
    printf("   <save>              Save tasks\n");
    printf("   <load>              Load tasks\n");
    printf("   <exit>              Exit the program\n");
}

void cli_list_groups(void) {
    TaskGroupContainer* container = get_task_group_container();
    if (!container) {
        printf("Container unavailable.\n");
        return;
    }

    if (container->task_group_count == 0) {
        printf("No groups.\n");
        return;
    }

    printf(PRINT_INFO "Groups:\n");

    for (int i = 0;
         i < container->task_group_count;
         i++) {

        TaskGroup* group = &container->task_groups[i];
        printf("  [%d] %s (%d tasks)\n", group->id, group->title, group->task_count);
    }
}

void cli_create_group(void) {
    char title[128];
    printf("Group title: ");

    if (fgets(title, sizeof(title), stdin) == NULL) return;
    title[strcspn(title, "\n")] = '\0';

    if (title[0] == '\0') {
        printf("Group title cannot be empty.\n");
        return;
    }

    TaskGroupContainer* container = get_task_group_container();
    if (!container) return;

    if (!task_group_create(title)) {
        printf("Could not create group.\n");
        return;
    }
    printf("Group created.\n");
}

void cli_delete_group(void) {
    int id;
    printf("Group ID: ");

    if (scanf("%d", &id) != 1) {
        printf("Invalid group ID.\n");

        while (getchar() != '\n');
        return;
    }

    while (getchar() != '\n');

    TaskGroupContainer* container = get_task_group_container();

    if (!container) return;

    if (task_group_delete(id)) printf("Group %d deleted.\n", id);
    else printf("Group %d not found.\n", id);
}

void cli_add_task(void) {
    int group_id;
    char title[128];
    printf("Group ID: ");
    if (scanf("%d", &group_id) != 1) {
        printf("Invalid group ID.\n");

        while (getchar() != '\n');
        return;
    }

    while (getchar() != '\n');
    TaskGroupContainer* container = get_task_group_container();
    if (!container) return;

    TaskGroup* group = task_group_find(group_id);
    if (!group) {
        printf("Group %d not found.\n", group_id);
        return;
    }

    printf("Task title: ");
    if (fgets(title, sizeof(title), stdin) == NULL) return;
    title[strcspn(title, "\n")] = '\0';

    if (title[0] == '\0') {
        printf("Task title cannot be empty.\n");
        return;
    }
    if (!task_create(group, title)) {
        printf("Could not create task.\n");
        return;
    }
    printf("Task created in group %d.\n", group_id);
}

void cli_delete_task(void) {
    int group_id;
    int task_id;
    printf("Group ID: ");
    if (scanf("%d", &group_id) != 1) {
        printf("Invalid group ID.\n");
        while (getchar() != '\n');
        return;
    }

    printf("Task ID: ");
    if (scanf("%d", &task_id) != 1) {
        printf("Invalid task ID.\n");
        while (getchar() != '\n');
        return;
    }

    while (getchar() != '\n');
    TaskGroupContainer *container = get_task_group_container();
    if (!container) return;

    TaskGroup* group = task_group_find(group_id);
    if (!group) {
        printf("Group %d not found.\n", group_id);
        return;
    }

    if (task_delete(group, task_id)) printf("Task %d deleted.\n", task_id);
    else printf("Task %d not found.\n", task_id);
}

void cli_set_status(void) {
    int group_id;
    int task_id;
    int status;

    printf("Group ID: ");
    if (scanf("%d", &group_id) != 1) {
        printf("Invalid group ID.\n");
        while (getchar() != '\n');
        return;
    }

    printf("Task ID: ");
    if (scanf("%d", &task_id) != 1) {
        printf("Invalid task ID.\n");
        while (getchar() != '\n');
        return;
    }

    printf("Status (0=TODO, 1=IN_PROGRESS, 2=DONE): ");

    if (scanf("%d", &status) != 1) {
        printf("Invalid status.\n");
        while (getchar() != '\n');
        return;
    }

    while (getchar() != '\n');
    TaskGroupContainer* container = get_task_group_container();
    if (!container) return;

    TaskGroup* group = task_group_find(group_id);
    if (!group) {
        printf("Group not found.\n");
        return;
    }

    Task* task = task_find(group, task_id);
    if (!task) {
        printf("Task not found.\n");
        return;
    }

    if (!task_set_status(task, status)) {
        printf("Invalid status.\n");
        return;
    }
    printf("Task status updated.\n");
}
