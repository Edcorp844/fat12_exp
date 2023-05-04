#Created by Fros Edson
src_dir = src
build_dir = build
src_files := $(shell find $(src_dir) -name *.c)
obj_files := $(patsubst $(src_dir)/%.c, $(build_dir)/%.o, $(src_files))
CC = gcc

.PHONY: all $(obj_files) always clean img kernel

all: kernel always $(obj_files) img 

kernel: $(src_dir)/kernel/kernel.c $(build_dir)/kernel/kernel.o
	mkdir -p $(build_dir)/kernel 
	# gcc -c $(src_dir)/kernel/kernel.c $(build_dir)/kernel/kernel.o -std=gnu99 -ffreestanding - 02 -Wall -Wextra -E

$(obj_files): $(build_dir)/%o: $(src_dir)/%c
	mkdir -p $(dir $@) && \
	gcc $(patsubst $(build_dir)/%o , $(src_dir)/%c, $(src_files)) -o $@

img: always
	dd if=/dev/zero of=$(build_dir)/img bs=512 count=2880
	mkfs.fat -F 12 -n "FROST" $(build_dir)/img
	dd if=$(build_dir)/main.o of=$(build_dir)/img conv=notrunc
	mcopy -i $(build_dir)/img $(build_dir)/kernel/kernel.o "::kernel.o"
	mcopy -i $(build_dir)/img  socket.rs "::socket.rs"

always:
	mkdir -p $(build_dir)

clean:
	rm $(obj_files)
	rm $(build_dir)/img
	rm -r $(build_dir)