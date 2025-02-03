# learn-rust-by-building-ruff

## The First version of Rust
These are the main files included in the first version of Rust - that power only two specific rules. While it cannot be used in a meaningful way, it provides an easy way to understand how `ruff` (or generally other linter) works without getting into all the details that are not so important for education.

- main.rs
- cache.rs
- check.rs
- lib.rs
- linter.rs
- message.rs
- parser.rs

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
typer: cli argument parsing
ast: Python native ast library
rich: color terminal
os/pathlib: walking directory
pytest: write simple tests

## Next Step
- Implement Cache
- Implement parallel processing
- Reimplement in Rust

Reference:
Blog: https://compileralchemy.substack.com/p/ruff-internals-of-a-rust-backed-python
Commit:

