/**
 * @file file.h
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#ifndef FILE_H
#define FILE_H

#include "external/cJSON.h"
#include "core/task.h"


int file_exists(const char*);
char* read_json(const char*);
int write_json(cJSON*, const char*);

//Storage
int storage_init(void);
int storage_load(void);
int storage_save(void);

// Tasks
cJSON* task_to_json(const Task*);
int task_from_json(const cJSON*, Task*);

// Task groups
cJSON* task_group_to_json(const TaskGroup*);
int task_group_from_json(const cJSON*, TaskGroup*);

// Task group container
cJSON* task_group_container_to_json(void);
int task_group_container_from_json(void);
int group_container_save(const char*);
int group_container_load(const char*);


#endif // FILE_H
