{
  description = "Boehm-Berarducci encodings — multi-language devShell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachSystem [ "x86_64-linux" ] (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          name = "boehm-berarducci-dev";

          packages = [
            pkgs.stack        # Haskell (manages its own GHC via lts snapshot)
            pkgs.uv           # Python
            pkgs.jdk17        # Java (used by Maven and Scala-CLI)
            pkgs.maven        # Java build/test
            pkgs.scala-cli    # Scala
            pkgs.go           # Go
            pkgs.gnumake
          ];

          STACK_ROOT = "$HOME/.stack";
          MAVEN_OPTS = "-Duser.home=$HOME";

          shellHook = ''
            echo "boehm-berarducci dev environment ready"
            echo "Run: make test-all"
          '';
        };
      }
    );
}
