/**
 * @file file.c
 * @author DargoDargonyx
 * @date 08/18/2026
 */

#include "storage/file.h"
#include "util/helper.h"
#include "external/cJSON.h"
#include "core/task.h"

#include <stdio.h>
#include <stdlib.h>


// Generic

int file_exists(const char* filename) {
	if (!filename) return 0;
	FILE* file = fopen(filename, "r");

	if (file != NULL) {
		fclose(file);
		return 1;
	}
	return 0;
}

char* read_json(const char* filename) {
    if (filename == NULL) return NULL;
    FILE* file = fopen(filename, "rb");

    if (!file) {
        printf(PRINT_ERROR "Could not open file {%s}\n", filename);
        return NULL;
    }

    if (fseek(file, 0, SEEK_END) != 0) {
        fclose(file);
        return NULL;
    }

    long size = ftell(file);
    if (size < 0) {
        fclose(file);
        return NULL;
    }
    rewind(file);

    char* buffer = malloc((size_t) size + 1);
    if (!buffer) {
        fclose(file);
        return NULL;
    }

    size_t bytes_read = fread(buffer, 1, (size_t) size, file);
    if (bytes_read != (size_t) size && ferror(file)) {
        free(buffer);
        fclose(file);
        return NULL;
    }
    buffer[bytes_read] = '\0';
    
	fclose(file);
    return buffer;
}

int write_json(cJSON* json, const char* filename) {
	FILE* file = fopen(filename, "w");

	char* json_str = cJSON_Print(json);
	if (json_str == NULL) return 0;

	if (file == NULL) {
		printf(PRINT_ERROR "Could not write to the file {%s}\n", filename);
		free(json_str);
		return 1;
	}

	fputs(json_str, file);
	fclose(file);

	free(json_str);
	return 0;
}

// Tasks

cJSON* task_to_json(const Task* task) {
    if (!task) return NULL;

    cJSON *json = cJSON_CreateObject();
    if (!json) return NULL;

    cJSON_AddNumberToObject(json, "id", task->id);
    cJSON_AddStringToObject(json, "title", task->title);
    cJSON_AddStringToObject(json, "description", task->description);
    cJSON_AddNumberToObject(json, "status", task->status);
    cJSON_AddNumberToObject(json, "priority", task->priority);

    return json;
}

int task_from_json(const cJSON* json, Task* task) {
    if (!json || !task) return 0;

    const cJSON* id = cJSON_GetObjectItemCaseSensitive(json, "id");
    const cJSON* title = cJSON_GetObjectItemCaseSensitive(json, "title");
    const cJSON* description = cJSON_GetObjectItemCaseSensitive(json, "description");
    const cJSON* status = cJSON_GetObjectItemCaseSensitive(json, "status");
    const cJSON* priority = cJSON_GetObjectItemCaseSensitive(json, "priority");

    if (!cJSON_IsNumber(id) ||
        !cJSON_IsString(title) ||
        !cJSON_IsString(description) ||
        !cJSON_IsNumber(status) ||
        !cJSON_IsNumber(priority)) {
        return 0;
    }

    task->id = id->valueint;

    snprintf(task->title, sizeof(task->title), "%s", title->valuestring);
    snprintf(task->description, sizeof(task->description), "%s", description->valuestring);

    task->status = status->valueint;
    task->priority = priority->valueint;

    return 1;
}

// Task groups

cJSON* task_group_to_json(const TaskGroup* group) {
    if (!group) return NULL;

    cJSON* json = cJSON_CreateObject();
    if (!json) return NULL;

    cJSON_AddNumberToObject(json, "id", group->id);
    cJSON_AddStringToObject(json, "title", group->title);

    cJSON* tasks = cJSON_CreateArray();
    if (!tasks) {
        cJSON_Delete(json);
        return NULL;
    }
    cJSON_AddItemToObject(json, "tasks", tasks);

    for (int i = 0; i < group->task_count; i++) {
        cJSON* task_json = task_to_json(&group->tasks[i]);
        if (!task_json) {
            cJSON_Delete(json);
            return NULL;
        }
        cJSON_AddItemToArray(tasks, task_json);
    }

    return json;
}

int task_group_from_json(const cJSON* json, TaskGroup* group) {
    if (json == NULL || group == NULL) return 0;

    const cJSON* id = cJSON_GetObjectItemCaseSensitive(json, "id");
    const cJSON* title = cJSON_GetObjectItemCaseSensitive(json, "title");
    const cJSON* tasks = cJSON_GetObjectItemCaseSensitive(json, "tasks");

    if (!cJSON_IsNumber(id) ||
        !cJSON_IsString(title) ||
        !cJSON_IsArray(tasks)) {
        return 0;
    }

    group->id = id->valueint;

    snprintf(group->title, sizeof(group->title), "%s", title->valuestring);

    int task_count = cJSON_GetArraySize(tasks);
    group->task_count = 0;

    for (int i = 0; i < task_count; i++) {
        const cJSON* task_json = cJSON_GetArrayItem(tasks, i);

        if (!task_from_json(task_json, &group->tasks[i])) return 0;
        group->task_count++;
    }

    return 1;
}

// Task group container

cJSON* group_container_to_json(void) {
    TaskGroupContainer* task_group_container = get_task_group_container();
	if (!task_group_container) return NULL;

    cJSON* json = cJSON_CreateObject();
    if (!json) return NULL;

    cJSON_AddNumberToObject(json, "next_id", task_group_container->next_id);

    cJSON* groups = cJSON_CreateArray();
    if (!groups) {
        cJSON_Delete(json);
        return NULL;
    }

    cJSON_AddItemToObject(json, "groups", groups);
    for (int i = 0; i < task_group_container->task_group_count; i++) {
        cJSON* group_json = task_group_to_json(&task_group_container->task_groups[i]);
        if (!group_json) {
            cJSON_Delete(json);
            return NULL;
        }
        cJSON_AddItemToArray(groups, group_json);
    }

    return json;
}

int group_container_from_json(const cJSON* json) {
    TaskGroupContainer* task_group_container = get_task_group_container();
	if (!json || !task_group_container) return 0;

    const cJSON* next_id = cJSON_GetObjectItemCaseSensitive(json, "next_id");
    const cJSON* groups = cJSON_GetObjectItemCaseSensitive(json, "groups");

    if (!cJSON_IsNumber(next_id) || !cJSON_IsArray(groups)) return 0;

    int group_count = cJSON_GetArraySize(groups);
    if (group_count > MAX_GROUPS) return 0;

    task_group_container->task_group_count = 0;
    task_group_container->next_id = next_id->valueint;

    for (int i = 0; i < group_count; i++) {
        const cJSON* group_json = cJSON_GetArrayItem(groups, i);
        if (!task_group_from_json(group_json, &task_group_container->task_groups[i])) 
			return 0;
        task_group_container->task_group_count++;
    }

    return 1;
}

int group_container_save(const char* filename) {
	TaskGroupContainer* task_group_container = get_task_group_container();
    if (!task_group_container || !filename) return 0;

    cJSON* json = group_container_to_json();
    if (json == NULL) return 0;

    int result = write_json(json, filename);
    cJSON_Delete(json);
    return result == 0;
}

int group_container_load(const char* filename) {
    TaskGroupContainer* task_group_container = get_task_group_container();
	if (!task_group_container || !filename) return 0;

    char* text = read_json(filename);
    if (!text) return 0;
    
	cJSON* json = cJSON_Parse(text);
    free(text);
    if (!json) return 0;

    int result = group_container_from_json(json);
    cJSON_Delete(json);
    return result;
}
