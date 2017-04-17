# binder.py
Simple script to bind two executables

## Usage
`python3 binder.py exec1 exec2`

## Description
binder.py generates a source file (in Go and C) ready to be compiled for the target plateform (for windows 64 bits from linux : `env GOOS=windows GOARCH=amd64 go build binded.out.go`).

The executable `binded.out` creates 2 files, writes the original executables and runs them.

## Misc
For testing purpose, a Go source file is provided in the `test` folder, this program creates a file named "test[pid]" (where '[pid]' is pid of the process) in the working directory.
Compile using `go build test.go`, test the script running `python3 binder.py test/test test/test && ./binded`
