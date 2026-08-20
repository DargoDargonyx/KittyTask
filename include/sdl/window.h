/**
 * @file window.h
 * @author DargoDargonyx
 * @date 08/19/2026
 */

#ifndef WINDOW_H
#define WINDOW_H

#include <SDL2/SDL.h>

typedef struct {
	int pixel_w;
	int pixel_h;

	SDL_Window* window;
	SDL_Renderer* renderer;
} WindowManager;

int init_window_manager(void);
void destroy_window_manager(void);
WindowManager* get_window_manager(void);

#endif // WINDOW_H
