/**
 * @file widget.c
 * @author DargoDargonyx
 * @date 08/19/2026
 */

#include "sdl/widget.h"

#include <SDL2/SDL.h>
#include <math.h>


#define SUPERSAMPLE 4

SDL_Surface* createRoundedSurface(int width, int height, int radius, 
		SDL_Color fill, SDL_Color border) {

	int sw = width * SUPERSAMPLE;
	int sh = height * SUPERSAMPLE;
	int sr = radius * SUPERSAMPLE;

	SDL_Surface* surface = SDL_CreateRGBSurfaceWithFormat(
		0,
		sw,
		sh,
		32,
		SDL_PIXELFORMAT_RGBA32
	);

	if (!surface) return NULL;

	SDL_LockSurface(surface);

	Uint32* pixels = (Uint32*) surface->pixels;
	int pitch = surface->pitch / 4;

	for (int y = 0; y < sh; y++) {
		for (int x = 0; x < sw; x++) {
			float px = x + 0.5f;
			float py = y + 0.5f;
			float cx = px;
			float cy = py;

			if (px < sr) cx = sr;
			else if (px > sw - sr) cx = sw - sr;

			if (py < sr) cy = sr;
			else if (py > sh - sr) cy = sh - sr;

			float dx = px - cx;
			float dy = py - cy;

			float distance = sqrtf(dx * dx + dy * dy);
			float edge = 0.5f * SUPERSAMPLE;
			float alpha = 1.0f;

			if (distance > sr - edge) alpha = (sr + edge - distance) / (2.0f * edge);

			if (alpha < 0.0f) alpha = 0.0f;
			if (alpha > 1.0f) alpha = 1.0f;

			float borderWidth = 1.0f * SUPERSAMPLE;
			int isBorder = distance >= sr - borderWidth;

			SDL_Color color;
			if (isBorder) color = border;
			else color = fill;

			Uint8 finalAlpha = (Uint8) (color.a * alpha);
			Uint32 pixel = SDL_MapRGBA(
				surface->format,
				color.r,
				color.g,
				color.b,
				finalAlpha
			);

			pixels[y * pitch + x] = pixel;
		}
	}

	SDL_UnlockSurface(surface);
	return surface;
}

SDL_Texture* createButtonTexture(SDL_Renderer* renderer, int width, int height, 
		int radius, SDL_Color fill, SDL_Color border) {
    
	SDL_Surface* surface = createRoundedSurface(
		width,
		height,
		radius,
		fill,
		border
	);
	if (!surface) return NULL;

	SDL_Texture* texture = SDL_CreateTextureFromSurface(renderer, surface);
	SDL_FreeSurface(surface);
	if (!texture) return NULL;
	SDL_SetTextureBlendMode(texture, SDL_BLENDMODE_BLEND);

	return texture;
}

Button* createButton(SDL_Renderer* renderer, int w, int h, int x, int y, int r) {
	Button* btn = malloc(sizeof(Button));

	btn->base.sdl_rect.x = x;
	btn->base.sdl_rect.y = y;
	btn->base.sdl_rect.w = w;
	btn->base.sdl_rect.h = h;
	btn->action_state = BTN_IDLE;

	SDL_Color normalFill = { .r = 255, .g = 255, .b = 255, .a = 25 };
	SDL_Color normalBorder = { .r = 255, .g = 255, .b = 255, .a = 90 };
	SDL_Color hoverFill = { .r = 255, .g = 255, .b = 255, .a = 50 };
	SDL_Color hoverBorder = { .r = 255, .g = 255, .b = 255, .a = 165 };

	btn->base.sdl_texture = createButtonTexture(
		renderer,
		w,
		h,
		r,
		normalFill,
		normalBorder
	);

	btn->hover_sdl_texture = createButtonTexture(
		renderer,
		w,
		h,
		r,
		hoverFill,
		hoverBorder
	);


	if (!btn->base.sdl_texture || !btn->hover_sdl_texture) return NULL;
	return btn;
}

void updateButton(Button* btn, int mouse_x, int mouse_y, int mouse_clicked) {
	SDL_Point point = { .x = mouse_x, .y = mouse_y };

	if (!SDL_PointInRect(&point, &btn->base.sdl_rect)) {
		btn->action_state = BTN_IDLE;
	} else {
		if (mouse_clicked) btn->action_state = BTN_PRESSED;
		else btn->action_state = BTN_HOVER;
	}
}
