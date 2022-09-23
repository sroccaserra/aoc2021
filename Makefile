SHELL=/bin/bash -euo pipefail

BUILD=build
SRC=src
LIB=lib

##
# Common

$(BUILD):
	mkdir -p $(BUILD)

.PHONY: clean
clean:
	rm -rf build/*

##
# Uxntal

.PRECIOUS: $(BUILD)/%.rom
$(BUILD)/%.rom: $(SRC)/%.tal $(BUILD) $(SRC)/common.tal $(SRC)/macros.tal $(LIB)/math32.tal
	uxnasm $< $@ 2>&1 | grep -v 'Unused label'

.PHONY: %_tal
%_tal: $(BUILD)/%.rom
	uxncli $<

.PHONY: %_talw
%_talw: $(BUILD)/%.rom
	uxnemu $<

##
# C++

.PRECIOUS: $(BUILD)/%_cpp
$(BUILD)/%_cpp: $(SRC)/%.cpp $(SRC)/common/common.h
	g++ -Wall -Wpedantic -fsanitize=address,leak -std=c++20 -o $@ $<

.PHONY: %_cpp
%_cpp: $(BUILD)/%_cpp
	@$< src/$*.in

##
# Rust

.PRECIOUS: $(BUILD)/%_rs
$(BUILD)/%_rs: $(SRC)/%.rs $(SRC)/common/common.rs
	rustc -O -o $@ $<
	strip $@

.PHONY: %_rs
%_rs: $(BUILD)/%_rs
	@$< src/$*.in

##
# GNU Smalltalk

.PHONY: %_st
%_st:
	@gst --no-gc-message $(SRC)/common/common.st $(SRC)/$*.st -a $(SRC)/$*.in

##
# Java

.PRECIOUS: $(BUILD)/%.class
$(BUILD)/%.class: $(SRC)/%.java
	javac -d $(BUILD) $<

.PHONY: %_java
%_java: $(BUILD)/Day%.class
	@java --class-path=$(BUILD) Day$* src/$*.in

##
# Kotlin

.PRECIOUS: $(BUILD)/%.jar
$(BUILD)/%.jar: $(SRC)/%.kt
	kotlinc $< -d $@

.PHONY: %_kt
%_kt: $(BUILD)/%.jar
	@kotlin -classpath $(BUILD)/$*.jar _$*Kt src/$*.in
