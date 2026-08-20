/**
 * @file widget.h
 * @author DargoDargonyx
 * @date 08/19/2026
 */

#ifndef WIDGET_H
#define WIDGET_H

#include <SDL2/SDL.h>


// General widgets
typedef enum {
	BUTTON
} WidgetType;

typedef struct {
	WidgetType type;

	SDL_Rect sdl_rect;
	SDL_Texture* sdl_texture;
} Widget;

SDL_Texture* create_rounded_rect_texture(SDL_Renderer*, int, int, 
		int, SDL_Color, SDL_Color);

// Buttons
typedef enum {
	BTN_IDLE,
	BTN_HOVER,
	BTN_PRESSED
} ButtonState;

typedef struct {
	Widget base;
	ButtonState action_state;
	SDL_Texture* hover_sdl_texture;

	char* txt;

	SDL_Color bg_color;
	SDL_Color fg_color;
	SDL_Color border_color;
	int radius;
} Button;

SDL_Surface* createRoundedSurface(int, int, int, SDL_Color, SDL_Color);
SDL_Texture* createButtonTexture(SDL_Renderer*, int, int, int, SDL_Color, SDL_Color);
Button* createButton(SDL_Renderer*, int, int, int, int, int);
void updateButton(Button*, int, int, int);
void destroy_button(Button*);


#endif // WIDGET_H
