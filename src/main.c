/**
 * @file main.c
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#include "storage/file.h"
#include "cli/cli.h"
#include "cli/command.h"

#include <stdio.h>


int main(int argc, char** argv) {
	init_task_group_container();
	TaskGroupContainer* container = get_task_group_container();

	if (!container) {
		printf(PRINT_ERROR "Failed to initialize task manager.\n");
		return 1;
	}

	if (file_exists(TASK_DATA_PATH)) {
		if (!group_container_load(TASK_DATA_PATH)) {
			printf(PRINT_ERROR "Failed to load %s.\n", TASK_DATA_PATH);
			return 1;
		}
	}

	int result;
	if (argc == 1) result = cli_run();
	else result = cli_command(argc, argv);

	if (!group_container_save(TASK_DATA_PATH)) {
		printf(PRINT_ERROR "Failed to save %s.\n", TASK_DATA_PATH);
		return 1;
	}

	return result;
}
