## Overview  
This is a simulator for register machine. Register machine is a generic class of abstract machines used in a manner similar to a Turing machine. It operates on a tape of registers with a tape of commands. At the initial state, the first few registers contains the input and all other registers are set to 0, see [Input/output conventions](#IOconv) for more details.

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
<span id = "IOconv"></span>
## Supported Macros:
macro | effect
----- | :----:
asn #i #j | copy the value of register j to register i
------
## Input/output conventions:
- When the register machine starts, the k inputs are put on register 1 to k, all other registers are set to 0.
- When the register machine halts, the final value of register 1 is the result
- If the register machine failed to halt (for a certain number of runs), the result is set to infinite and the register machine will be forced to halt.
-------
## How to use:
The first argument is the register machine file (tape of commands), and then follows the inputs to the RM.
```sh
python reg_machine example_rm 10
```
------
## Function calls:
The called register machine should be declared in the form ``# function_name`` before it's called. The declaration occupies a line but won't be put in the command list. A function call will be counted as one command. The register machine can be called in the form ``function_name #register_for_output #register_for_inputs``
