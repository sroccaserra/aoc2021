SHELL=/bin/bash -euo pipefail

BUILD=build
SRC=src
LIB=lib

$(BUILD)/%.rom: $(SRC)/%.tal $(BUILD) $(SRC)/common.tal $(SRC)/macros.tal $(LIB)/math32.tal
	uxnasm $< $@ 2>&1 | grep -v 'Unused label'

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/%_cpp: $(SRC)/%.cpp $(SRC)/common/common.h
	g++ $< -o $@ --std=c++20

.PHONY: %_cpp
%_cpp: $(BUILD)/%_cpp
	@$< src/$*.in

.PRECIOUS: $(BUILD)/%.rom
%: $(BUILD)/%.rom
	uxncli $<

.PRECIOUS: $(BUILD)/%.rom
%w: $(BUILD)/%.rom
	uxnemu $<

.PHONY: clean
clean:
	rm -rf build/*
