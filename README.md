# Let's write an OpenSAFELY Study Together

2024 [OpenSAFELY](https://opensafely.orgg) Symposium


This repository contains example data designed to support investigation of
two Very Serious research questions:

* **Cake and/or Death**: Does consumption of cake modify the risk of mortality and if so from what causes?
* **Om Nom Nom Nom**: Explaining the temporal and spatial variation of bite wounds in England


## Codelists
Codelists you may find useful for these research questions are to be found in `/local-codelists`.

## Example data
There is a finely crafted example dataset for this coding exercise which contains more interesting
clinical phenomena than you will find in the dummy data generated by default by ehrQL.

You will need to add the `--dummy-data-file` option to your ehrQL commands to make use of it, e.g.

```sh
opensafely exec ehrql:v1 --dummy-data-file example-data
```

Including the manual dummy data override `--dummy-data-file` in your `project.yaml` action definitions is not recommended. Doing this in real study code would mean that when executed in the secure environment your action would not run on the real patient data.

## Your analysis code
R, Python, and Stata are available for your use in this Codespaces.

### R
R may be written in either Visual Studio Code or RStudio, and the `R` executable is available in the terminal. All packages that are installed in the OpenSAFELY R action image are installed locally, i.e. running `R analysis/my_script.R` in the terminal should behave similarly to `opensafely exec r:latest R analysis/my_script.R`.

We reccomend use of RStudio, which may be accessed via the Ports tab below, and clicking on the globe icon in the "Forwarded Address" column of the first row in table.


### Python
This Codespace is shipped with a Python virtual environment whose installed packages closely match those of the OpenSAFELY Python action image. This means that any code executed from Visual Studio Code, by running `python` in the terminal, or `opensafely exec python:v2 python` should behave similarly.


### Stata
It is possible to run Stata actions within this codespace via the `opensafely` commands. No futher tooling or support is provided for Stata. We do not recommend using Stata for the purposes of this exercise.
