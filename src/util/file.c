/**
 * @file file.c
 * @author DargoDargonyx
 * @date 08/17/2026
 */

#include "util/file.h"
#include "util/helper.h"
#include "external/cJSON.h"

#include <stdio.h>
#include <stdlib.h>


int file_exists(const char* filename) {
	FILE* file = fopen(filename, "r");

	if (file != NULL) {
		fclose(file);
		return 1;
	}
	return 0;
}

char* read_json(const char* filename) {
	FILE* file = fopen(filename, "rb");
	if (!file) {
		printf(PRINT_ERROR "Could not open file {%s}\n", filename);
		return NULL;
	}

	fseek(file, 0, SEEK_END);
	long size = ftell(file);
	rewind(file);

	char* buffer = malloc(size + 1);
	if (!buffer) goto end;

	size_t bytes_read = fread(buffer, 1, size, file);
	buffer[bytes_read] = '\0';
end:
	fclose(file);
	return buffer;
}

int write_json(cJSON* json, const char* filename) {
	FILE* file = fopen(filename, "w");

	char* json_string = cJSON_Print(json);

	if (json_string == NULL) {
		printf(PRINT_ERROR "Could not write an empty json object to a file\n");
		return 1;
	}

	if (file == NULL) {
		printf(PRINT_ERROR "Could not write to the file {%s}\n", filename);
		free(json_string);
		return 1;
	}

	fputs(json_string, file);
	fclose(file);

	free(json_string);
	return 0;
}
