﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "temp.bin",                # FileName
        "a0000",                    # MapName
        "a0000",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "temp",                   # 0
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

    Return()

    # Function_1_9D end

    SaveToFile()

Try(main)
