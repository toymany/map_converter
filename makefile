stage_tsv := $(wildcard tsv/*.tsv)
stage_cs := $(patsubst tsv/%.tsv, cs/%.cs, $(stage_tsv))

all: $(stage_cs)  converter.py


SUFFIXES: .txt .tsv

cs/%.cs : tsv/%.tsv
	python converter.py $<


.PHONY: clean
clean:
	rm -f cs/*.cs

