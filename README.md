## This is a simulator for register machine
------
## Commands of register machine:
command | effect
-------- | :--------:
z #i | set register i to be 0
s #i | increase register i by 1
j #i #j #k | if register i and j are the same, jump to the k<sub>th</sub> command

Registers and commands are on different tapes in RM model.  
Each command occupies a line.

------
## Input/output conventions:
- When starting a register machine, the k inputs are put on register 1 to k, all other registers are set to 0.
- When the register machine halts, the final value of register 1 is the result
- If the register machine failed to halt (for a certain number of runs), then the result is infinite
-------
## How to use:
The first argument is the register machine file, and then follows the inputs to the RM.
```sh
python reg_machine example_rm 10
```
------
## Macros:
macro | effect
----- | :----:
asn #i #j | copy the value of register j to register i
------
## Function calls:
The called register machine should be declared in the form ``# function_name`` before it's called. The declaration occupies a line but won't be put in the command list. The register machine can be called in the form ``function_name #register_for_output #register_for_inputs``
