BUILD=build
SRC=src

$(BUILD)/%.rom: $(SRC)/%.tal $(BUILD)
	uxnasm $< $@ 2>&1 | grep -v 'Unused label'

$(BUILD):
	mkdir -p $(BUILD)

.PRECIOUS: $(BUILD)/%.rom
%: $(BUILD)/%.rom
	uxncli $<

.PHONY: clean
clean:
	rm -rf build/*
