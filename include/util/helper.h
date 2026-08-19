/**
 * @file helper.h
 * @author DargoDargonyx
 * @date 08/17/2026
 */

#ifndef HELPER_H
#define HELPER_H

#include "util/ansi.h"


// Time formats
typedef struct {
	int day;
	int month;
	int year;
} Date;

// Helper ANSI print output macros
#define PRINT_ERROR ANSI_BOLD ANSI_RED "[ERROR] " ANSI_RESET
#define PRINT_WARNING ANSI_BOLD ANSI_YELLOW "[WARNING] " ANSI_RESET
#define PRINT_INFO ANSI_BOLD ANSI_CYAN "[INFO] " ANSI_RESET


#endif // HELPER_H
