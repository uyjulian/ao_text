﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1170.bin",                # FileName
        "c1170",                    # MapName
        "c1170",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1170",                  # 0
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
