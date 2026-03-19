.PHONY: test-all test-haskell test-python test-java test-scala test-go clean help

test-all: test-haskell test-python test-java test-scala test-go
	@echo ""
	@echo "All test suites passed."

test-haskell:
	@echo "==> Haskell (stack test)"
	cd haskell && stack test

test-python:
	@echo "==> Python (uv run pytest)"
	cd python && uv run pytest tests/ -v

test-java:
	@echo "==> Java (mvn test)"
	cd java && mvn test

test-scala:
	@echo "==> Scala (scala-cli test)"
	scala-cli test scala/

test-go:
	@echo "==> Go (go test)"
	cd go && go test ./...

clean:
	cd haskell && stack clean
	cd python && rm -rf .venv __pycache__ .pytest_cache
	cd java && mvn clean
	scala-cli clean scala/
	cd go && go clean

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "  test-all       Run all five test suites"
	@echo "  test-haskell   Run haskell/: stack test"
	@echo "  test-python    Run python/: uv run pytest"
	@echo "  test-java      Run java/: mvn test"
	@echo "  test-scala     Run scala/: scala-cli test"
	@echo "  test-go        Run go/: go test ./..."
	@echo "  clean          Clean all build artifacts"
	@echo ""
	@echo "Recommended entry point: nix develop --command make test-all"
