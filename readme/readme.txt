plugin for CudaText.
it shades (dims) all lines except the current paragraph (in which 1st caret placed).
paragraphs should be separated by empty lines.

it works only for some lexers.
to configure which lexers are handled, call menuitem "Plugins/ Focus Mode/ Config" and edit opened config file. you have options there in [op] section:

- lexers: comma-separated list of lexers for which plugin works
- dim_value: this is dim value from 0 (no effect) to 255 (text is transparent). good middle value is 100..150.


author: Alexey T (CudaText)
license: MIT
