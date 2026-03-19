# boehm-berarducci

Implementations of [Boehm-Berarducci encodings](https://okmij.org/ftp/tagless-final/course/Boehm-Berarducci.html) for elementary algebraic data types across multiple programming languages.

Boehm-Berarducci encoding is the typed lambda calculus analogue of Church encoding: algebraic data types (Maybe, Either, Pair, Free, …) are represented purely as higher-order functions, with no constructors or pattern matching — only function application. This makes it a fun lens for comparing how different type systems express the same idea.

## Types implemented

| Type    | Haskell | Python | Java | Scala | Go |
|---------|:-------:|:------:|:----:|:-----:|:--:|
| Maybe   | ✓       | ✓      | ✓    | ✓     | ✓  |
| Either  | ✓       | ✓      | ✓    | ✓     |    |
| Pair    | ✓       |        |      |       |    |
| Free    | ✓       | ✓      |      |       |    |

## Running the tests

### Prerequisites

All toolchains are managed via [Nix](https://nixos.org/). Install it with the [Determinate Systems installer](https://determinate.systems/nix-installer):

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

### Enter the dev shell

```bash
nix develop
```

This drops you into a shell with `stack`, `uv`, `maven`, `scala-cli`, and `go` all available at pinned versions.

### Run all test suites

```bash
make test-all
```

### Run individual suites

```bash
make test-haskell   # Haskell  — stack test
make test-python    # Python   — uv run pytest
make test-java      # Java     — mvn test
make test-scala     # Scala    — scala-cli test
make test-go        # Go       — go test ./...
```

### One-liner (without entering the shell first)

```bash
nix develop --command make test-all
```

## Language notes

- **Haskell** — uses `RankNTypes` to express the universal quantification directly in the type; the most natural encoding
- **Python** — uses closures and operator overloading (`>>`, `&`, `*`) to approximate monadic syntax
- **Java** — uses anonymous inner classes and generics to simulate higher-rank polymorphism
- **Scala** — uses traits and Scala 3 syntax; run via Scala-CLI with no separate build file
- **Go** — uses `interface{}` to approximate parametric polymorphism (pre-generics style)
