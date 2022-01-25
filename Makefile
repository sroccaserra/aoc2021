BUILD=build
SRC=src

$(BUILD)/%.rom: $(SRC)/%.tal $(BUILD) $(SRC)/common.tal $(SRC)/macros.tal
	uxnasm $< $@

$(BUILD):
	mkdir -p $(BUILD)

.PRECIOUS: $(BUILD)/%.rom
%: $(BUILD)/%.rom
	uxncli $<

.PHONY: clean
clean:
	rm -rf build/*
