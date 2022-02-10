SHELL=/bin/bash -euo pipefail

BUILD=build
SRC=src
LIB=lib

$(BUILD)/%.rom: $(SRC)/%.tal $(BUILD) $(SRC)/common.tal $(SRC)/macros.tal $(LIB)/math32.tal
	uxnasm $< $@ 2>&1 | grep -v 'Unused label'

$(BUILD):
	mkdir -p $(BUILD)

.PRECIOUS: $(BUILD)/%.rom
%: $(BUILD)/%.rom
	uxncli $<

.PRECIOUS: $(BUILD)/%.rom
%w: $(BUILD)/%.rom
	uxnemu $<

.PHONY: clean
clean:
	rm -rf build/*
