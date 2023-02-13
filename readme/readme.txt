plugin for CudaText.
it shades (dims) all lines except the current paragraph (in which 1st caret placed).
paragraphs should be separated by empty lines.
when caret is on empty line, none is shaded.

it works only for some file extensions.
to configure which file extensions are handled, call menu item
"Options / Settings-plugins / Focus Mode / Config" and edit opened config file
(restart CudaText then). you have options in [focus_mode] section:

- file_extensions: comma-separated list of file extensions.
- dim_value: dim value from 0 (no effect) to 255 (text is transparent).
             good middle value is 100..150.


author: Alexey Torgashin (CudaText)
license: MIT
