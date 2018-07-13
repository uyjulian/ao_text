﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3110.bin",                # FileName
        "e3110",                    # MapName
        "e3110",                    # Location
        0x0000,                     # MapIndex
        "ed7515",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3110",                  # 0
        "Lovely Girl",            # 1
        "White Falcon",           # 2
        "Female Officer",         # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(248, 0)                                        # 0

    ScpFunction((
        "Function_0_F8",           # 00, 0
        "Function_1_108",          # 01, 1
        "Function_2_109",          # 02, 2
        "Function_3_4CE",          # 03, 3
    ))


    def Function_0_F8(): pass

    label("Function_0_F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_107")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_107")

    Return()

    # Function_0_F8 end

    def Function_1_108(): pass

    label("Function_1_108")

    Return()

    # Function_1_108 end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(447)
    SoundLoad(448)
    LoadEffect(0x0, "event\\ev304_00.eff")
    LoadEffect(0x1, "event\\ev304_01.eff")
    LoadEffect(0x2, "event\\ev304_02.eff")
    LoadEffect(0x3, "event\\ev304_03.eff")
    LoadEffect(0x4, "event\\ev304_04.eff")
    LoadEffect(0x5, "event\\ev304_05.eff")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 15700, 0, 0)
    MoveCamera(312, -21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80350, 0)
    FadeToBright(500, 0)
    SetCameraDistance(90850, 9000)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_271")
    SetMessageWindowPos(40, 230, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00102FBeautiful...\x02\x03",
            "If I remember correctly, they fire\x01",
            "them up every night at Michelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_464")

    label("loc_271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_2F0")
    SetMessageWindowPos(40, 230, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00202F...They are beautiful.\x02\x03",
            "If I remember correctly, they fire\x01",
            "them up every night at Michelam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_464")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_36B")
    SetMessageWindowPos(40, 230, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00309FHa ha, "bravooo"...that's it, right?\x02\x03",
            "They fire 'em up every\x01",
            "night at Michelam, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_464")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_3F0")
    SetMessageWindowPos(40, 230, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10102FEh eh, they're beautiful.\x02\x03",
            "If I remember correctly, they fire\x01",
            "them up every night at Michelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_464")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_464")
    SetMessageWindowPos(40, 230, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10302FHu hu, quite splendid.\x02\x03",
            "It's a spectacle you can see\x01",
            "here every night, am I right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_464")

    SetMessageWindowPos(280, 230, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00002FHa ha, we could see them\x01",
            "with a nice timing, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t103B", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_109 end

    def Function_3_4CE(): pass

    label("Function_3_4CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64F")
    Sleep(300)
    Sound(447, 0, 100, 0)
    Sleep(700)
    PlayEffect(0x5, 0x0, 0xFF, 0x0, 0, 20000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, -5000, 15000, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, 10000, 12000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sound(448, 0, 100, 0)
    Sleep(900)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 10000, 12000, 7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0x5, 0xFF, 0x0, -5000, 15000, -7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x4, 0x4, 0xFF, 0x0, 0, 18000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_3_4CE")

    label("loc_64F")

    Return()

    # Function_3_4CE end

    SaveToFile()

Try(main)
