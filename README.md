# learn-rust-by-building-ruff

## Rebuild with Python
Components:
- [ ] Tokenizer (Lexer)
- [ ] Parser

main.rs
cache.rs
check.rs
lib.rs
linter.rs
message.rs
parser.rs

## Libraries used for 1st version of ruff
The first-ever version of Ruff used the following Rust packages

fern: for logging
rayon: for parallelizing computation
clap: for cli argument parsing
serde: for serializing and deserializing data
rustpython: for parsing, uses the provided AST
colored: for adding colors to the terminal
walkdir: for walking a directory recursively
anyhow: Flexible concrete Error type built on std::error::Error

## Libraries I used for the Python verrsion
logging: std logging library
?: parallel computation
typer: cli argument parsing
?: serialising
ast: Python native ast library
rich: color terminal
os/pathlib: walking directory
?: error
pytest: write simple tests

## Rebuild with Rust

Reference:
Blog: https://compileralchemy.substack.com/p/ruff-internals-of-a-rust-backed-python
Commit:

