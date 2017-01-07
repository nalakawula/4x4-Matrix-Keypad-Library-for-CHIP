#keypad 4x4 python library for CHIP
Module python untuk CHIP $9 Computer.
Merupakan module python untuk akses Keypad Matrix 4x4 yang dipasang pada CHIP.
Module ini dibuat karena setelah brwosing ternyata library matrix keypad untuk chip belum ada.
Modul ini membutuhkan pustaka CHIP_IO dari https://github.com/xtacocorex/CHIP_IO

berikut ini wiringnya:
| Keypad        | GPIO          |
| ------------: |:--------------|
| Row 1      | XIO-P0 |
| Row 2      | XIO-P2      |
| Row 3 | XIO-P4      |
| Row 4      | XIO-P6 |
| col 1      | XIO-P1      |
| col 2 | XIO-P3      |
| col 3      | XIO-P5 |
| col 4      | XIO-P7      |

Module ini dibuat dengan referensi dari:
https://www.raspberrypi.org/forums/viewtopic.php?t=81675&p=577225
https://pypi.python.org/pypi/matrix_keypad
