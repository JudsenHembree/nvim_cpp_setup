.PHONY: all clean make_dir run copy_compile_commands build
TARGET = setup
all: clean make_dir build copy_compile_commands

clean:
	rm -rf build

make_dir:
	mkdir -p build

run:
	@./build/$(TARGET)

build:
	cd build && cmake .. && make

copy_compile_commands:
	cp build/compile_commands.json .
