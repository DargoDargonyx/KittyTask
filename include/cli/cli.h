/**
 * @file cli.h
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#ifndef CLI_H
#define CLI_H

int cli_run(void);

void cli_print_help(void);
void cli_list_groups(void);
void cli_create_group(void);
void cli_delete_group(void);
void cli_add_task(void);
void cli_delete_task(void);
void cli_set_status(void);

#endif // CLI_H
