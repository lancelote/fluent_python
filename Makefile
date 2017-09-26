help:
	@echo "deps"
	@echo "    install all dependencies"
	@echo "test"
	@echo "    run all the tests"

deps:
	pip install -r requirements.txt

test:
	py.test --doctest-modules