/**
 * @file file.h
 * @author DargoDargonyx
 * @date 08/17/2026
 */

#ifndef FILE_H
#define FILE_H

#include "external/cJSON.h"


int file_exists(const char*);
char* read_json(const char*);
int write_json(cJSON*, const char*);


#endif // FILE_H
