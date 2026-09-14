.PHONY: all clean

all: report.txt

stats.txt: stats.py data.csv
	python stats.py

report.txt: build_report.py stats.txt report.md
	python build_report.py

clean:
	rm -f stats.txt report.txt
