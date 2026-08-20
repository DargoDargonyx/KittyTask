SRC_DIR  := src
INC_DIR  := include
BIN_DIR  := bin
DIST_DIR := dist

CC := gcc
BASE_CFLAGS := -Wall -Wextra -I$(INC_DIR) $(shell sdl2-config --cflags)
LDFLAGS := $(shell sdl2-config --libs) \
           -lSDL2_ttf \
           -lSDL2_image \
           -lSDL2_mixer \
           -Wl,-rpath,'$$ORIGIN/lib' \
		   -lm

SRC := $(wildcard $(SRC_DIR)/*.c) \
       $(wildcard $(SRC_DIR)/cli/*.c) \
       $(wildcard $(SRC_DIR)/core/*.c) \
       $(wildcard $(SRC_DIR)/external/*.c) \
       $(wildcard $(SRC_DIR)/sdl/*.c) \
       $(wildcard $(SRC_DIR)/storage/*.c) \
       $(wildcard $(SRC_DIR)/util/*.c)

.PHONY: all debug release clean run copy_libs

all: release


# --------------------------------------------------
# Development
# --------------------------------------------------

DEBUG_BIN := $(BIN_DIR)/debug
DEBUG_DIST := $(DIST_DIR)/debug

DEBUG_OBJ := $(patsubst $(SRC_DIR)/%.c, $(DEBUG_BIN)/%.o, $(SRC))

DEBUG_CFLAGS := $(BASE_CFLAGS) -g -O0 -DKTASK_DEV

debug: $(DEBUG_DIST)/ktask

$(DEBUG_DIST)/ktask: $(DEBUG_OBJ)
	@echo "Linking debug build..."
	@mkdir -p $(DEBUG_DIST)
	@$(CC) $(DEBUG_OBJ) -o $@ $(LDFLAGS)
	@echo "Debug build complete."

$(DEBUG_BIN)/%.o: $(SRC_DIR)/%.c
	@echo "Compiling $<"
	@mkdir -p $(dir $@)
	@$(CC) $(DEBUG_CFLAGS) -c $< -o $@


# --------------------------------------------------
# Release
# --------------------------------------------------

RELEASE_BIN := $(BIN_DIR)/release
RELEASE_DIST := $(DIST_DIR)/release

RELEASE_OBJ := $(patsubst $(SRC_DIR)/%.c, $(RELEASE_BIN)/%.o, $(SRC))

RELEASE_CFLAGS := $(BASE_CFLAGS) -O2 -DNDEBUG

release: $(RELEASE_DIST)/ktask

$(RELEASE_DIST)/ktask: $(RELEASE_OBJ)
	@echo "Linking release build..."
	@mkdir -p $(RELEASE_DIST)
	@$(CC) $(RELEASE_OBJ) -o $@ $(LDFLAGS)
	@cp -r assets $(RELEASE_DIST)/
	@echo "Release build complete."

$(RELEASE_BIN)/%.o: $(SRC_DIR)/%.c
	@echo "Compiling $<"
	@mkdir -p $(dir $@)
	@$(CC) $(RELEASE_CFLAGS) -c $< -o $@


# --------------------------------------------------
# Utility
# --------------------------------------------------

clean:
	@echo "Cleaning project..."
	@rm -rf $(BIN_DIR) $(DIST_DIR)
	@echo "Project cleaned."

run: debug
	@./$(DEBUG_DIST)/ktask
