.PHONY: all check build clean

all: build

check:
	./check.sh

build: check
	python -m build

clean:
	rm -rf dist/ build/ *.egg-info
