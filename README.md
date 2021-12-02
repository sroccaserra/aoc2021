# aoc2021

## Learnings

- Python can now pattern match:
    - Structural Pattern Matching: Tutorial ~ <https://www.python.org/dev/peps/pep-0636/>
## How it started

```shell
$ stack new aoc2021
$ cd aoc2021
$ rm -r app
$ rm -r test
$ rm -r Changelog.md
```

In package.yaml:
- Remove "executables" section
- Remove "tests" section
- add hspec dependency (LTS) and -W ghc-option in "library" section

```shell
$ stack setup
$ stack build
```

Then write a Spec.hs file in src, and try to run it with:
```shell
$ stack runhaskell -- src/Spec.hs
```

Note: for this simple project, I want all the code in the src directory.
