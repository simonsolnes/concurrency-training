# Makefile for building demo applications.
# by Brian Fraser

# Edit this file to compile extra C files into their own programs.

CROSS_TOOL = 
CC_CPP = $(CROSS_TOOL)g++
CC_C = $(CROSS_TOOL)gcc

CFLAGS = -Wall -g -std=c99 -Werror -pthread

all: clean many

.PHONY: one
one:
	$(CC_C) $(CFLAGS) sum_on_thread.c -o sum_on_thread

.PHONY: many
many:
	$(CC_C) $(CFLAGS) sum_on_many_threads.c -o sum_on_many_threads

clean:
	rm -f sum_on_thread sum_on_many_threads
