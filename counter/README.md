# Counter

A simple experiment to explore with running a single set of code on multiple
platforms

## Features

- Installing Tailwind on Yew
- (TODO) Storage of local information work on Tauri
- (TODO) Show notification in different OS
- (TODO) Show notification in the background for Mobile OS

## Quickstart

You can install the package using the following steps

```bash
# front
cd ./frontend
cargo build
trunk build
trunk serve

# tauri
cd ./src-tauri
cargo build
cargo run
```

## Development Setup

This section covers the necessary steps to setup your environment for
development

### Prerequisite

- [asdf](https://github.com/asdf-vm/asdf) with Rust installed

### Build & Run

This can be done with the steps mentioned in the "Quickstart" section. In
addition, you can use the following command in place of `trunk serve` to have
the webpage hot reload during development

```bash
trunk watch
```
