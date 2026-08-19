SRC_DIR  := src
INC_DIR  := include
BIN_DIR  := bin
DIST_DIR := dist

CC := gcc
BASE_CFLAGS := -Wall -Wextra -I$(INC_DIR) $(shell sdl2-config --cflags)
LDFLAGS := $(shell sdl2-config --libs) \
           -lSDL2_ttf -lSDL2_image -lSDL2_mixer \
           -Wl,-rpath,'$$ORIGIN/lib'

SRC := $(wildcard $(SRC_DIR)/*.c) \
	   $(wildcard $(SRC_DIR)/cli/*.c) \
	   $(wildcard $(SRC_DIR)/core/*.c) \
	   $(wildcard $(SRC_DIR)/external/*.c) \
	   $(wildcard $(SRC_DIR)/sdl/*.c) \
	   $(wildcard $(SRC_DIR)/storage/*.c) \
	   $(wildcard $(SRC_DIR)/util/*.c)

OBJ := $(patsubst $(SRC_DIR)/%.c, $(BIN_DIR)/%.o, $(SRC))

TARGET := $(DIST_DIR)/ktask

CFLAGS := $(BASE_CFLAGS) -O2 -DNDEBUG

.phony := debug release copy_libs clean run


all: $(TARGET)

$(TARGET): $(OBJ)
	@echo "Linking project..."
	@mkdir -p $(DIST_DIR)
	@$(CC) $(OBJ) -o $(TARGET) $(LDFLAGS)
	@cp -r assets $(DIST_DIR)/
	@echo "Project linked."

$(BIN_DIR)/%.o: $(SRC_DIR)/%.c
	@echo "Compiling $<"
	@mkdir -p $(dir $@)
	@$(CC) -c $< -o $@ $(CFLAGS)

debug:
	@$(MAKE) clean
	@$(MAKE) CFLAGS="$(BASE_CFLAGS) -g" all

release:
	@$(MAKE) clean
	@$(MAKE) CFLAGS="$(BASE_CFLAGS) -O2 -DNDEBUG" all
	@$(MAKE) copy_libs
	@strip $(TARGET)

copy_libs:
	@echo "Copying SDL libraries..."
	@mkdir -p $(DIST_DIR)/lib
	ldd $(TARGET) | awk `{print $$3}` | grep -E '^/' | \
	grep -vE 'libc\.so|libm\.so|ld-linux' | sort -u | \
	while read lib; do
		@cp -n $$lib $(DIST_DIR)/lib/; \
	done

clean:
	@echo "Cleaning project..."
	@rm -rf $(BIN_DIR) $(DIST_DIR)
	@echo "Project cleaned."

run: all
	@cd $(DIST_DIR) && ./ktask
