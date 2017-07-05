﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9099.bin",                # FileName
        "m9099",                    # MapName
        "m9099",                    # Location
        0x00BF,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 191, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9099",                  # 0
    ))

    ChipFrameInfo(156, 0)                                        # 0

    ScpFunction((
        "Function_0_9C",           # 00, 0
        "Function_1_9D",           # 01, 1
    ))


    def Function_0_9C(): pass

    label("Function_0_9C")

    Return()

    # Function_0_9C end

    def Function_1_9D(): pass

    label("Function_1_9D")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_9D end

    SaveToFile()

Try(main)
