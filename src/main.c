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
    if (!init_task_group_container()) {
		printf(PRINT_ERROR "Failed to initialize task group container.\n");
		return 1;
	}

	if (!storage_init()) {
        printf(PRINT_ERROR "Failed to initialize storage.\n");
        return 1;
    }

    if (!storage_load()) {
        printf(PRINT_ERROR "Failed to load task data.\n");
        return 1;
    }

    int result;

    if (argc == 1) {
        result = cli_run();
    } else {
        result = cli_command(argc, argv);
    }

    if (!storage_save()) {
        printf(PRINT_ERROR "Failed to save task data.\n");
        return 1;
    }

    return result;
}
