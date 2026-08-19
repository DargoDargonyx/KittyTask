/**
 * @file command.h
 * @author DargoDargonyx
 * @date 08/19/2026
 */

#ifndef COMMAND_H
#define COMMAND_H

int cli_command(int, char**);

// Group commmands
int group_command(int, char**);
int group_add_cmd(int, char**);
int group_delete_cmd(int, char**);

// Task commands
int task_command(int, char**);
int task_add_cmd(int, char**);
int task_delete_cmd(int, char**);
int task_status_cmd(int, char**);
int task_priority_cmd(int, char**);

#endif // COMMAND_H
