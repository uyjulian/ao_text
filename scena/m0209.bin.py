from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0209.bin",                # FileName
        "m0209",                    # MapName
        "m0209",                    # Location
        0x00A7,                     # MapIndex
        "ed7300",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 167, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0209",                  # 0
        "Yona",                   # 1
        "Truzo Z",             # 2
        "dummy",                 # 3
        "Roberts boss",           # 4
        "SE control",                 # 5
        "bm0220",                 # 6
        "bm0220",                 # 7
    ))

    ATBonus("ATBonus_3BC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_39C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3FC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_460", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_468", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_46C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_470", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_47C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_4E0", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0220", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79101.dat", "ms79101.dat", "ms79101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3FC", "MonsterBattlePostion_45C", "ed7451", "ed7453", "ATBonus_3BC"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_49C", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bm0220", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88200.dat", 0, 0, 0, 0, 0, "ms84900.dat", 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_45C", "ed7453", "ed7453", "ATBonus_39C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50203.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch79150.itc",               # 10
        "monster/ch79151.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(102500,  250,     0,       90,   389,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       0,       0x185010E,    "BattleInfo_4E0", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 11,  -8.0,                  0.0,                   -1.0,                  400.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.09999999403953552,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.0,                   -0.0,                  0.19999998807907104,   1.0])
    DeclEvent(0x0040, 0, 6,   0.0,                   0.0,                   0.0,                   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 30,  -11.0,                 0.0,                   -2.0,                  81.0,                  [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.0,                  0.4000000059604645,    1.0])

    DeclActor(112500,  0,       204000,  1200,    112500,  1000,    204000,  0x007C, 0,  7,  0x0000)
    DeclActor(4294671796, 0,       1000,    1200,    4294671796, 1000,    1000,    0x007C, 0,  9,  0x0000)
    DeclActor(4294841296, 0,       4294962296, 1200,    4294841296, 1000,    4294962296, 0x007C, 0,  2,  0x0000)
    DeclActor(96780,   0,       4294961926, 1200,    96780,   780,     4294961926, 0x007C, 0,  3,  0x0000)
    DeclActor(4294939296, 4294959296, 4000,    1200,    4294939296, 4294960796, 4000,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_5B8",          # 00, 0
        "Function_1_6AA",          # 01, 1
        "Function_2_A17",          # 02, 2
        "Function_3_B68",          # 03, 3
        "Function_4_C2D",          # 04, 4
        "Function_5_14F9",         # 05, 5
        "Function_6_15F5",         # 06, 6
        "Function_7_1861",         # 07, 7
        "Function_8_19E6",         # 08, 8
        "Function_9_1B1A",         # 09, 9
        "Function_10_1C9F",        # 0A, 10
        "Function_11_1DD3",        # 0B, 11
        "Function_12_2CC7",        # 0C, 12
        "Function_13_2D4F",        # 0D, 13
        "Function_14_2D6B",        # 0E, 14
        "Function_15_3E18",        # 0F, 15
        "Function_16_3E31",        # 10, 16
        "Function_17_3E5D",        # 11, 17
        "Function_18_43CF",        # 12, 18
        "Function_19_441D",        # 13, 19
        "Function_20_446B",        # 14, 20
        "Function_21_44C0",        # 15, 21
        "Function_22_4515",        # 16, 22
        "Function_23_456A",        # 17, 23
        "Function_24_45BF",        # 18, 24
        "Function_25_4A6E",        # 19, 25
        "Function_26_4A8B",        # 1A, 26
        "Function_27_4AA4",        # 1B, 27
        "Function_28_4ABC",        # 1C, 28
        "Function_29_4B65",        # 1D, 29
        "Function_30_4CE1",        # 1E, 30
    ))


    def Function_0_5B8(): pass

    label("Function_0_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_5CB")
    SetChrFlags(0x8, 0x80)
    Jump("loc_613")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_613")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_624")
    ClearScenarioFlags(0x22, 0)
    Jump("loc_661")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_638")
    ClearScenarioFlags(0x22, 1)
    Event(0, 14)
    Jump("loc_661")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_652")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 24)
    Jump("loc_661")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_661")
    ClearScenarioFlags(0x22, 3)
    Event(0, 29)

    label("loc_661")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67B")
    Event(0, 17)

    label("loc_67B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692")
    Event(0, 10)

    label("loc_692")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    Event(0, 8)

    label("loc_6A9")

    Return()

    # Function_0_5B8 end

    def Function_1_6AA(): pass

    label("Function_1_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6BF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_6BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x209), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F2")

    label("loc_6DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_70A")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_722")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749")
    ClearChrFlags(0xD, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetChrFlags(0xD, 0x8000)

    label("loc_749")

    Jump("loc_758")

    label("loc_74E")

    SetChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 1, 0x80)

    label("loc_758")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    SetMapObjFrame(0x8, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x8, "Null_color2", 0x1, 0x1)
    Jump("loc_887")

    label("loc_862")

    SetMapObjFrame(0x8, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x8, "Null_color2", 0x0, 0x1)

    label("loc_887")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C5")
    SetMapObjFrame(0x7, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x7, "Null_color2", 0x1, 0x1)
    Jump("loc_8EA")

    label("loc_8C5")

    SetMapObjFrame(0x7, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x7, "Null_color2", 0x0, 0x1)

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_928")
    SetMapObjFrame(0xFF, "yo_before", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita_", 0x2, "off")
    Jump("loc_994")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_965")
    SetMapObjFrame(0xFF, "yo_before", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita_", 0x2, "on")
    Jump("loc_994")

    label("loc_965")

    SetMapObjFrame(0xFF, "yo_before", 0x1, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita_", 0x2, "on")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")
    OP_70(0xA, 0x0)
    Jump("loc_9AB")

    label("loc_9A7")

    OP_70(0xA, 0x1E)

    label("loc_9AB")

    SetMapObjFrame(0xFF, "ev_wall", 0x0, 0x1)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9D7")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x6, 0x4)

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9F1")
    OP_24(0x85)
    Sound(134, 1, 100, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_A16")

    label("loc_9F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D")
    OP_24(0x85)
    Sound(134, 1, 100, 0)
    Jump("loc_A16")

    label("loc_A0D")

    Sound(133, 1, 100, 0)
    OP_24(0x86)

    label("loc_A16")

    Return()

    # Function_1_6AA end

    def Function_2_A17(): pass

    label("Function_2_A17")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B17")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_AA0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_B12")

    label("loc_AA0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B12")

    Jump("loc_B5C")

    label("loc_B17")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_B5C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_A17 end

    def Function_3_B68(): pass

    label("Function_3_B68")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pisa's boxes are covered with easy-to-read recipes.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_C29")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C29")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Hot hot cheese pizza\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C29")

    TalkEnd(0xFF)
    Return()

    # Function_3_B68 end

    def Function_4_C2D(): pass

    label("Function_4_C2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_128E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A0")
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#02301F(Kataata, Kataataatatatach … …)\x02\x03",
            "#02310F…… Kusso, you can not do it this way! It is!\x01",
            "Then try this key … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F(Somehow it's burning … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FYona … What are you doing?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBC")
    Jump("loc_E06")

    label("loc_DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DDC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_DDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_DFC")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E06")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02305F…… Ah, it's untitled.\x02\x03",
            "#02302FNo, something a little anxious\x01",
            "I found it.\x02\x03",
            "#02306FFocus on a little\x01",
            "I am analyzing it, but ….\x01",
            "This is quite a songwriter.\x02\x03",
            "#02309FHello, Genius SE Jonna's\x01",
            "The place where blood is making noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I guess … oh well.\x02\x03",
            "#00001F… … Did Jonah see that speech?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02305FAh……\x01",
            "How about that independence?\x02\x03",
            "#02303FI tried relaying at the terminal, but ……\x01",
            "To be honest, I am not interested right now.\x02\x03",
            "#02301FAnyway, if there is no use\x01",
            "I wonder if you remove your seat?\x02\x03",
            "Now for analyzing this data\x01",
            "I want to focus.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00303F(Well ….\x01",
            "In a world full of mistakes\x01",
            "It looks like it is stuffed up. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Cheeky with Jonah's habit … …\x01",
            "I will put on moxibustion later. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Well, alright ……\x01",
            "It's bad to disturb you,\x01",
            "Would you like to come to another opportunity? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 1)
    Jump("loc_1289")

    label("loc_11A0")

    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#02301F(Kataata, Kataataatatatach … …)\x02\x03",
            "#02310FWell, in this case …\x01",
            "…… Damn it was not good after all.\x02\x03",
            "#02303FThen again with another approach ……\x01",
            "… … Dumbbell ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm completely enthusiastic … …\x01",
            "Let's say we will come on another occasion. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1289")

    Jump("loc_14F5")

    label("loc_128E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_END)), "loc_14F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1475")

    ChrTalk(
        0x8,
        (
            "#02304FAir conditioning complete, net environment is also the highest grade,\x01",
            "Furthermore, feeling isolated from this real … …\x02\x03",
            "#02302FWell, as I thought\x01",
            "The fourth control terminal is cool.\x02\x03",
            "#02309FWell, the environment of this terminal is also\x01",
            "I have to set it back to my liking ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Well, after all\x01",
            "It seemed like I helped with the unwillingness\x01",
            "I can not care less … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Well, I'm to some extent\x01",
            "It is a type that takes care of me,\x01",
            "Probably it is OK. )\x02\x03",
            "#00200F(For the manager, I will also later from me\x01",
            "Let me keep in touch. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14F5")

    label("loc_1475")


    ChrTalk(
        0x8,
        (
            "#02305F… … Huh, were you still there?\x02\x03",
            "#02306FBecause I am busy now.\x01",
            "Hey, they came home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(A, I Ratsukuru na … …)\x02",
    )

    CloseMessageWindow()

    label("loc_14F5")

    TalkEnd(0xFE)
    Return()

    # Function_4_C2D end

    def Function_5_14F9(): pass

    label("Function_5_14F9")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are devices that can recover the orbment.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15E6")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x9, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x9, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_15E6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_14F9 end

    def Function_6_15F5(): pass

    label("Function_6_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 1)), scpexpr(EXPR_END)), "loc_15FF")
    Return()

    label("loc_15FF")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Large monsters wandering around#4RIt is alright#doing.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Exterminate】\x01",      # 0
            "【quit】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_16E1"),
        (SWITCH_DEFAULT, "loc_16FA"),
    )


    label("loc_16E1")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -5000, 0, 0, 270)
    EventEnd(0x5)
    Return()

    label("loc_16FA")

    Battle("BattleInfo_4E0", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-5000, 1000, 0, 0)
    OP_90(0x0, -5000, 0, 0, 270)
    OP_90(0x1, -5000, 0, 0, 270)
    OP_90(0x2, -5000, 0, 0, 270)
    OP_90(0x3, -5000, 0, 0, 270)
    OP_90(0x4, -5000, 0, 0, 270)
    OP_90(0x5, -5000, 0, 0, 270)
    OP_90(0x6, -5000, 0, 0, 270)
    OP_90(0x7, -5000, 0, 0, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_17BC"),
        (1, "loc_17C1"),
        (SWITCH_DEFAULT, "loc_17C4"),
    )


    label("loc_17BC")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_17C1")

    OP_B9(0x0)
    Return()

    label("loc_17C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xD, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Arranged arrangements devils!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '缚魔'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('缚魔', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 1)
    OP_29(0x94, 0x4, 0x2)
    OP_29(0x94, 0x4, 0x10)
    OP_29(0x94, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_15F5 end

    def Function_7_1861(): pass

    label("Function_7_1861")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DE")
    Fade(500)
    SetChrPos(0x0, 111500, 0, 203500, 90)
    SetChrPos(0x1, 111500, 0, 204500, 90)
    SetChrPos(0x2, 110500, 0, 203500, 90)
    SetChrPos(0x3, 110500, 0, 204500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1937")
    SetChrPos(0x13E, 109500, 0, 204000, 90)

    label("loc_1937")

    OP_68(109500, 0, 204560, 0)
    MoveCamera(52, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(125000, 2000, 204560, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(7000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0200", 124, 0, 0)
    IdleLoop()

    label("loc_19DE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1861 end

    def Function_8_19E6(): pass

    label("Function_8_19E6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x64)
    Sleep(1)
    OP_68(114800, 2750, 201540, 0)
    MoveCamera(72, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26940, 0)
    OP_90(0x0, 123000, 2750, 201500, 180)
    OP_90(0x1, 122000, 2750, 201500, 180)
    OP_90(0x2, 123000, 2750, 202500, 180)
    OP_90(0x3, 122000, 2750, 202500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A97")
    SetChrPos(0x13E, 122500, 2750, 203500, 180)

    label("loc_1A97")

    Sound(145, 0, 100, 0)
    OP_68(107500, 0, 202000, 3200)
    MoveCamera(21, 45, 0, 3200)
    OP_71(0x8, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x8)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x8, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x8, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_19E6 end

    def Function_9_1B1A(): pass

    label("Function_9_1B1A")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Do you want to operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C97")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 500, 90)
    SetChrPos(0x1, -296500, 0, 1500, 90)
    SetChrPos(0x2, -297500, 0, 500, 90)
    SetChrPos(0x3, -297500, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF0")
    SetChrPos(0x13E, -298500, 0, 1000, 90)

    label("loc_1BF0")

    OP_68(-296650, 0, 650, 0)
    MoveCamera(52, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(-283000, 2000, 650, 3800)
    MoveCamera(62, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0202", 101, 0, 0)
    IdleLoop()

    label("loc_1C97")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1B1A end

    def Function_10_1C9F(): pass

    label("Function_10_1C9F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x64)
    Sleep(1)
    OP_68(-295800, 2750, -1500, 0)
    MoveCamera(72, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26940, 0)
    OP_90(0x0, -285000, 2750, -1500, 180)
    OP_90(0x1, -286000, 2750, -1500, 180)
    OP_90(0x2, -285000, 2750, -500, 180)
    OP_90(0x3, -286000, 2750, -500, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D50")
    SetChrPos(0x13E, -285500, 2750, 500, 180)

    label("loc_1D50")

    Sound(145, 0, 100, 0)
    OP_68(-300160, 0, -1500, 3200)
    MoveCamera(9, 44, 0, 3200)
    OP_71(0x7, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x7)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x7, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x7, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1C9F end

    def Function_11_1DD3(): pass

    label("Function_11_1DD3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    SoundLoad(904)
    OP_68(-12500, 900, 0, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_90(0x101, -11500, 0, -700, 90)
    OP_90(0x102, -11500, 0, 700, 90)
    OP_90(0x103, -12500, 0, -1500, 90)
    OP_90(0x104, -12500, 0, 1500, 90)
    OP_90(0x109, -13500, 0, -950, 90)
    OP_90(0x105, -13500, 0, 950, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x13E, -14500, 0, 0, 90)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    SetChrPos(0x9, 3000, 20000, 0, 270)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x96)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "ev_wall", 0x1, 0x1)
    OP_68(-7500, 900, 0, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_1F88():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F88)
    Sleep(50)

    def lambda_1FA5():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FA5)
    Sleep(50)

    def lambda_1FC2():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FC2)
    Sleep(50)

    def lambda_1FDF():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FDF)
    Sleep(50)

    def lambda_1FFC():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FFC)
    Sleep(50)

    def lambda_2019():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2019)
    Sleep(50)

    def lambda_2036():
        OP_97(0x13E, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 0, lambda_2036)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x13E, 0)
    OP_63(0x13E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13E,
        "#6P#02305FOh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(29500, 1500, 0, 4000)
    MoveCamera(42, 27, 0, 4000)
    SetCameraDistance(24500, 4000)

    def lambda_20BB():
        OP_95(0xFE, -1500, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_20BB)
    WaitChrThread(0x13E, 1)
    OP_6F(0x79)

    ChrTalk(
        0x13E,
        (
            "#02302FThat!\x01",
            "That's the \"fourth control terminal\"!\x02\x03",
            "#02309FWow, that is far too far!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-3120, 900, 170, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16149, 0)

    def lambda_2166():
        OP_97(0x101, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2166)
    Sleep(50)

    def lambda_2183():
        OP_97(0x102, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2183)
    Sleep(50)

    def lambda_21A0():
        OP_97(0x103, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_21A0)
    Sleep(50)

    def lambda_21BD():
        OP_97(0x104, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_21BD)
    Sleep(50)

    def lambda_21DA():
        OP_97(0x109, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_21DA)
    Sleep(50)

    def lambda_21F7():
        OP_97(0x105, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_21F7)
    OP_0D()
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x104,
        (
            "#00306FWhew, it was a hard time\x01",
            "Whether it is for us or not.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_224E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_224E)

    ChrTalk(
        0x109,
        (
            "#6P#10112FEhe, well well\x02\x03",
            "#10100FEven if you are not used to going along\x01",
            "Was it difficult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x01",
            "It was painful at first for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FEspecially Jonah is more than me\x01",
            "Because I am taking over care … …\x02\x03",
            "#00204FThis is so so\x01",
            "I guess I was trying hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        "#02310F#11PUgh..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PBut while I am young, I hope\x01",
            "Will not it be hard if it gets bigger?\x02\x03",
            "#10302FKimi, even pizza alone\x01",
            "She seems to like snacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FIf you do not mind, Jonah,\x01",
            "Do you go out for jogging in the morning?\x02\x03",
            "#00000FOnce a week would be good\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02311F#11POh come on leave me alone\x02\x03",
            "#02301FAnyway it's hot\x01",
            "Entering the terminal room and cooling ----\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#6P#00207F#4SJona, get over here!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(250)
    OP_68(3000, 12500, 0, 0)
    MoveCamera(90, 63, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    Sound(834, 0, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(3000, 2000, 0, 1500)
    MoveCamera(90, 25, 0, 1500)
    ClearMapObjFlags(0x0, 0x4)
    SetChrFlags(0x9, 0x1)

    def lambda_259A():
        OP_96(0xFE, 0xBB8, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_259A)
    WaitChrThread(0x9, 1)
    CancelBlur(0)
    OP_63(0x13E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_25D5():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_25D5)
    Sound(833, 0, 100, 0)
    Sound(902, 0, 100, 0)
    SetCameraDistance(19500, 1000)
    OP_82(0x0, 0x2BC, 0xBB8, 0x3E8)
    Sleep(2000)
    Fade(250)
    OP_68(-1600, 2000, 0, 0)
    MoveCamera(47, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sound(904, 2, 100, 0)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0x101, 3, 0, 12)
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2673():

        label("loc_2673")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2673")

    QueueWorkItem2(0x13E, 2, lambda_2673)

    def lambda_2685():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2685)
    WaitChrThread(0x13E, 1)
    EndChrThread(0x13E, 0x2)
    OP_64(0x13E)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        "#02307F#4S#6P#NAH!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#6P#NThis is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#6P#NI was hanging around in the B parcel\x01",
            "The deca version of the cleaning machine ……! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#6P#NNo, in such a simple thing\x01",
            "I do not think so …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#5PJona, get back!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x102, 500)

    ChrTalk(
        0x13E,
        "#02310F#12P#NR-right!\x02",
    )

    CloseMessageWindow()
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x13E, 0x10E, 0x1F4)

    def lambda_2849():
        OP_95(0xFE, -6500, 0, -2500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2849)
    WaitChrThread(0x13E, 1)
    OP_68(-1600, 2000, 0, 10000)
    MoveCamera(64, 13, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(15500, 10000)

    def lambda_2895():
        OP_95(0xFE, -9000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2895)
    WaitChrThread(0x13E, 1)

    def lambda_28B3():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_28B3)
    WaitChrThread(0x13E, 1)
    OP_64(0x13E)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(270, 90, -1, -1)
    SetChrName("PPP… Target located…")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "PPPP ……\x01",
            "Discover goals ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Primary target - Crossbell Police SSS\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Identification of target audience ……\x01",
            "Kurosuraberu police, mission support section ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#NCould it be?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#6P#NIt found out about us on the net?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10310F#6P#NFrom us on the net\x01",
            "Did you bother to specify it! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(5040, 2200, 1900, 1500)
    MoveCamera(64, 12, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(500)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(260, 70, -1, -1)
    SetChrName("PPP… Target located…")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "PPP ……\x01",
            "Danger level to be judged 3 judgment ……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's too vague for a machine\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00111F#6P#NAnyway let's be on guard!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NOn the machine\x01",
            "It's about to be over!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10107F#6P#NThat machine was…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_6F(0x79)
    OP_68(5040, 2200, 0, 1500)
    MoveCamera(90, 20, 0, 1500)
    SetCameraDistance(17500, 1500)
    Sound(576, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x136, 0x14A, 0x0, 0x0)
    Sleep(500)
    Sound(905, 0, 100, 0)
    OP_79(0x0)
    StopSound(904, 500, 100)
    OP_6F(0x79)
    Sleep(500)
    Sound(579, 2, 100, 0)
    Sound(594, 2, 100, 0)
    Sound(378, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x14A, 0x172, 0x0, 0x20)
    BlurSwitch(0x384, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(90, 13, 0, 900)
    SetCameraDistance(11500, 900)
    Sleep(900)
    StopSound(579, 300, 100)
    StopSound(594, 300, 100)
    OP_24(0x388)
    SetChrBattleFlags(0x13E, 0x8)
    Battle("BattleInfo_49C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    Call(0, 14)
    Return()

    # Function_11_1DD3 end

    def Function_12_2CC7(): pass

    label("Function_12_2CC7")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_12_2CC7 end

    def Function_13_2D4F(): pass

    label("Function_13_2D4F")

    OP_71(0x0, 0x96, 0xAA, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_13_2D4F end

    def Function_14_2D6B(): pass

    label("Function_14_2D6B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("apl/ch51770.itc", 0x2A)
    OP_68(-1900, 1000, 0, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18000, 0)
    OP_90(0x101, -3300, 0, -700, 90)
    OP_90(0x102, -3300, 0, 700, 90)
    OP_90(0x103, -4400, 0, -1500, 90)
    OP_90(0x104, -4400, 0, 1500, 90)
    OP_90(0x109, -5500, 0, -1100, 90)
    OP_90(0x105, -5500, 0, 1100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x13E, -15000, 0, 0, 90)
    SetChrPos(0xA, -4500, 0, 0, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    OP_68(-3900, 1000, 0, 2000)
    SetCameraDistance(17000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#6PThe current machine ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PWhatever you think\x01",
            "It is called illegally dumped machine\x01",
            "It is not a level …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FThe possibility of \"association\" involvement\x01",
            "It may be expensive …\x02\x03",
            "#00201FI kept Rubatse's president's office\x01",
            "It was a reaction similar to a puppet weapon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_3026():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3026)
    Sleep(50)

    def lambda_3036():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3036)
    Sleep(50)

    def lambda_3046():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3046)
    Sleep(50)

    def lambda_3056():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3056)
    Sleep(50)

    def lambda_3066():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3066)
    Sleep(50)

    def lambda_3076():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3076)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x104,
        (
            "#00306F#5PThat huge thing\x02\x03",
            "#00301FSomething better than\x01",
            "Did not you do something advanced?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308FHmm, even on the conducting net\x01",
            "It seems I was accessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAfter all \"association\"\x01",
            "Are they doing something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02304F#2P- Well, even if you think\x01",
            "There is no use, can not you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31AB():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_31AB)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-5400, 1000, 0, 2500)

    def lambda_324B():

        label("loc_324B")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_324B")

    QueueWorkItem2(0x109, 2, lambda_324B)

    def lambda_325D():

        label("loc_325D")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_325D")

    QueueWorkItem2(0x105, 2, lambda_325D)
    Sleep(50)

    def lambda_3272():

        label("loc_3272")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3272")

    QueueWorkItem2(0x103, 2, lambda_3272)

    def lambda_3284():

        label("loc_3284")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3284")

    QueueWorkItem2(0x104, 2, lambda_3284)
    Sleep(50)

    def lambda_3299():

        label("loc_3299")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3299")

    QueueWorkItem2(0x101, 2, lambda_3299)

    def lambda_32AB():

        label("loc_32AB")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_32AB")

    QueueWorkItem2(0x102, 2, lambda_32AB)
    WaitChrThread(0x13E, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x13E,
        (
            "#6P#02306FLater than that,\x01",
            "Let's hit air condition in the terminal room?\x02\x03",
            "#02302FThis Jonah-sama like the movement of the people\x01",
            "I will explore various things.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#11PYou … … Is not it sweet?\x01",
            "Is not it strong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FHuhu, what the liver is placing is\x01",
            "I certainly do.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(133, 1000, 100)
    StopBGM(0xFA0)
    WaitBGM()
    SoundLoad(134)
    SoundLoad(938)
    OP_68(100700, 4500, 0, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 100500, 0, 200, 90)
    SetChrPos(0x102, 100500, 0, -1000, 90)
    SetChrPos(0x103, 101600, 0, 1200, 180)
    SetChrPos(0x104, 100400, 0, 1700, 135)
    SetChrPos(0x109, 99300, 0, 400, 90)
    SetChrPos(0x105, 99300, 0, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x13E, 0x4)
    SetChrFlags(0x13E, 0x20)
    SetChrFlags(0x13E, 0x10)
    SetChrFlags(0x13E, 0x2)
    SetChrPos(0x13E, 102500, 250, -100, 90)
    SetChrChipByIndex(0x13E, 0x2A)
    SetChrSubChip(0x13E, 0x2)
    BeginChrThread(0x13E, 2, 0, 15)
    SetMapObjFrame(0xFF, "monita_", 0x2, "on")
    SetMapObjFrame(0xFF, "yo_before", 0x1, 0x1)
    SetMapObjFrame(0xFF, "yo_after", 0x0, 0x1)
    Sound(134, 2, 100, 0)
    Sound(938, 2, 100, 0)
    Sleep(1000)
    PlayBGM("ed7521", 0)
    Sleep(2500)
    OP_68(100700, 1500, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(102380, 1000, 220, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_24(0x3AA)
    EndChrThread(0x13E, 0x2)

    ChrTalk(
        0x13E,
        (
            "#02305F#5PFun Hun …\x01",
            "Apparently the previous machine\x01",
            "It looks like it was released one month ago.\x02\x03",
            "#02303FWirelessly connect to the power net\x01",
            "I wish the device was clogged …\x02\x03",
            "#02301FIt is called \"Novartis\"\x01",
            "The name of the administrator remains in the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FNobaltisse, that guy with the lab coat\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FApparently among the \"association\"\x01",
            "He seems to be in a considerable position.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_373D():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_373D)
    Sleep(50)

    def lambda_374D():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_374D)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#5PMaddox … …\x01",
            "It was a gruesome osan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206F…… possibly a play#2RBow#To a\x01",
            "It may have released the prototype.\x02\x03",
            "#00211FWhat, what is that?\x01",
            "It seems to be a personality that you like to love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10306FYeah. I got that feeling too\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FIt is more dangerous person than it looks\x01",
            "I do not think there is any mistake … ….\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    BeginChrThread(0x13E, 2, 0, 15)

    ChrTalk(
        0x13E,
        (
            "#02304F#5PWell, even more than\x01",
            "It seems they are not being released ……\x02\x03",
            "#02302FWith this without heart\x01",
            "That's why I am taking over!\x02\x03",
            "Well, it's near the tower\x01",
            "Line speed is faster than above\x01",
            "There are almost no restrictions … ….\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02309F#5P#4SYEAH!\x01",
            "The fourth control terminal, it's awesome!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_39F3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_39F3)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_3A30():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A30)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00012FHe's totally into it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAs I expected to draw back,\x01",
            "Is not it man-man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FJonah … … Once for the chief,\x01",
            "I'm putting in a report?\x02\x03",
            "#00211FAnd don't do that much on your own\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02304F#5POh yeah yeah\x02\x03",
            "#02302FI will be alone with you after all\x01",
            "Why are you going home soon?\x02\x03",
            "#02305F─ ─ Oops, in a place like this\x01",
            "You have a new server.\x02\x03",
            "#02309FWell, the net environment of the crossbell is also\x01",
            "I'm pretty fulfilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWhew ……\x01",
            "I guess it is already crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FWhatching\x01",
            "But it seems to be OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FYeah, the movement of \"association\"\x01",
            "I am a bit worried ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00004FWell, sometimes appearance\x01",
            "Let's go see it.\x02\x03",
            "#00000FMaybe I will not keep drawing up like this\x01",
            "I am a bit worried.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D29():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D29)
    Sleep(50)

    def lambda_3D39():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D39)
    Sleep(50)

    def lambda_3D49():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D49)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x103,
        "#5P#00202FTrue.\x02",
    )

    CloseMessageWindow()
    StopSound(938, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_37()
    EndChrThread(0x13E, 0xFF)
    SetChrChipByIndex(0x13E, 0xFF)
    SetChrSubChip(0x13E, 0x0)
    RemoveParty(0x3D, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x0, 98000, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetMapObjFrame(0xFF, "ev_wall", 0x0, 0x1)
    SetScenarioFlags(0x181, 7)
    OP_29(0xAC, 0x1, 0x9)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_14_2D6B end

    def Function_15_3E18(): pass

    label("Function_15_3E18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E30")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_15_3E18")

    label("loc_3E30")

    Return()

    # Function_15_3E18 end

    def Function_16_3E31(): pass

    label("Function_16_3E31")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E5C")
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(800)
    Jump("Function_16_3E31")

    label("loc_3E5C")

    Return()

    # Function_16_3E31 end

    def Function_17_3E5D(): pass

    label("Function_17_3E5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(29200, 900, -400, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 31000, 0, -400, 270)
    SetChrPos(0x102, 31000, 0, -400, 270)
    SetChrPos(0x103, 31000, 0, -400, 270)
    SetChrPos(0x104, 31000, 0, -400, 270)
    SetChrPos(0x109, 31000, 0, -400, 270)
    SetChrPos(0x105, 31000, 0, -400, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(28200, 900, -400, 4500)
    SetCameraDistance(18000, 4500)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x3)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 20)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 21)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 22)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(1000)
    Sound(102, 0, 100, 0)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#00005FOh that's right\x02\x03",
            "#00000FThe fellow of Jonah,\x01",
            "Direct lift leading to the exit\x01",
            "Did you say that there is something?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#12P#00202FYes, it's over there\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1100, 25500, 4000)
    MoveCamera(30, 25, 0, 4000)
    SetCameraDistance(26000, 4000)

    def lambda_40BC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40BC)
    Sleep(50)

    def lambda_40CC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_40CC)
    Sleep(50)

    def lambda_40DC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_40DC)
    Sleep(50)

    def lambda_40EC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_40EC)
    Sleep(50)

    def lambda_40FC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_40FC)
    OP_6F(0x79)
    Sleep(300)

    AnonymousTalk(
        0x103,
        (
            "#00204FApparently this place is\x01",
            "Near the base of the Orkis Tower\x01",
            "It seems to be located.\x02\x03",
            "#00202FFrom there to the lighthouse in the port area\x01",
            "There is a lift on the straight line.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#00106FOh that's fantastic\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00306FAlso, that way back through that fucking hot one\x01",
            "It is troublesome because it is troublesome.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        "#10309FEhe, true\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(28200, 900, -400, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10300F#5PEven so ……\x01",
            "I wonder if it will be around the evening already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42A4():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42A4)
    Sleep(50)

    def lambda_42B4():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42B4)
    Sleep(50)

    def lambda_42C4():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_42C4)
    Sleep(50)

    def lambda_42D4():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_42D4)
    Sleep(50)

    def lambda_42E4():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42E4)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x109,
        "#12P#10106FThat's right…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11P… then, using the lift\x01",
            "Shall we go back to the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FYep. Let's\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 28000, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 0)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_17_3E5D end

    def Function_18_43CF(): pass

    label("Function_18_43CF")


    def lambda_43D4():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43D4)

    def lambda_43EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43EE)
    WaitChrThread(0xFE, 1)

    def lambda_4403():
        OP_96(0xFE, 0x6A40, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4403)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_43CF end

    def Function_19_441D(): pass

    label("Function_19_441D")


    def lambda_4422():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4422)

    def lambda_443C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_443C)
    WaitChrThread(0xFE, 1)

    def lambda_4451():
        OP_96(0xFE, 0x6A40, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4451)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_441D end

    def Function_20_446B(): pass

    label("Function_20_446B")


    def lambda_4470():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4470)

    def lambda_448A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_448A)
    WaitChrThread(0xFE, 1)

    def lambda_449F():
        OP_95(0xFE, 28200, 0, -1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_449F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_446B end

    def Function_21_44C0(): pass

    label("Function_21_44C0")


    def lambda_44C5():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44C5)

    def lambda_44DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_44DF)
    WaitChrThread(0xFE, 1)

    def lambda_44F4():
        OP_95(0xFE, 28200, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_44C0 end

    def Function_22_4515(): pass

    label("Function_22_4515")


    def lambda_451A():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_451A)

    def lambda_4534():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4534)
    WaitChrThread(0xFE, 1)

    def lambda_4549():
        OP_95(0xFE, 29200, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4549)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_4515 end

    def Function_23_456A(): pass

    label("Function_23_456A")


    def lambda_456F():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_456F)

    def lambda_4589():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4589)
    WaitChrThread(0xFE, 1)

    def lambda_459E():
        OP_95(0xFE, 29200, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_459E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_456A end

    def Function_24_45BF(): pass

    label("Function_24_45BF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(938)
    LoadChrToIndex("apl/ch51770.itc", 0x1E)
    LoadChrToIndex("apl/ch51523.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis421.itp")
    OP_68(103460, 1000, -170, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 102500, 250, -100, 90)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 102500, 250, -100, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 15)
    ClearScenarioFlags(0x0, 2)
    Sleep(500)
    Sound(938, 2, 100, 0)
    Sleep(2000)
    PlayBGM("ed7521", 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(938, 300, 100)
    EndChrThread(0x8, 0x2)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sleep(110)
    SetChrSubChip(0x8, 0x1)
    Sleep(110)
    SetChrSubChip(0x8, 0x2)
    Sleep(110)
    SetChrSubChip(0x8, 0x1)
    Sleep(110)
    SetChrSubChip(0x8, 0x2)
    Sleep(110)
    SetChrSubChip(0x8, 0x1)
    Sleep(110)
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#5P#02306FYaaaawn!\x02\x03",
            "#02301FAhh. What time is it?\x02\x03",
            "#02305FOh it's already morning?!\x02",
        )
    )

    CloseMessageWindow()
    Sound(906, 0, 100, 0)
    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5P#02306FHa\x01",
            "It was truly hungry.\x02\x03",
            "#02300FHmm, that pizza store,\x01",
            "What time did you start doing?\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    BeginChrThread(0x8, 2, 0, 26)
    OP_68(103460, 1000, -170, 1800)
    MoveCamera(53, 28, 0, 1800)
    SetCameraDistance(13500, 1800)
    OP_6F(0x79)
    SetCameraDistance(13000, 20000)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#6P#02302FCertainly that shop, we have power net\x01",
            "I was saying to introduce the exam … …\x02\x03",
            "#02309FHehe, I just have to check it out\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#6P#02305FHuh?\x02\x03",
            "#02301F……what?\x01",
            "This garbage-like data …\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 25)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 27)
    Sleep(500)

    ChrTalk(
        0x8,
        "#6P#02310FNo this isn't data at all?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    SetScenarioFlags(0x0, 2)
    WaitChrThread(0x8, 2)
    Fade(500)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x5)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x8, 2, 0, 28)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#6P#02310F……Structure……?\x01",
            "No, far more than that … …\x02\x03",
            "#02305F….\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    SetCameraDistance(12000, 4000)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    EndChrThread(0xC, 0x1)
    StopSound(938, 1000, 100)
    StopSound(134, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x8)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        "What is this.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)
    Sound(6, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    ReplaceBGM(-1, -1)
    OP_24(0x3AA)
    OP_24(0x86)
    SetScenarioFlags(0x23, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_45BF end

    def Function_25_4A6E(): pass

    label("Function_25_4A6E")

    Sleep(2200)

    label("loc_4A71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A8A")
    Sound(836, 0, 50, 0)
    Sleep(700)
    Jump("loc_4A71")

    label("loc_4A8A")

    Return()

    # Function_25_4A6E end

    def Function_26_4A8B(): pass

    label("Function_26_4A8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AA3")
    OP_A1(0xFE, 0x5DC, 0x2, 0x3, 0x4)
    Jump("Function_26_4A8B")

    label("loc_4AA3")

    Return()

    # Function_26_4A8B end

    def Function_27_4AA4(): pass

    label("Function_27_4AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABB")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_27_4AA4")

    label("loc_4ABB")

    Return()

    # Function_27_4AA4 end

    def Function_28_4ABC(): pass

    label("Function_28_4ABC")

    OP_A1(0xFE, 0x7D0, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x7D0, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x834, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x898, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x8FC, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)
    OP_A1(0xFE, 0x960, 0x2, 0x5, 0x6)

    label("loc_4B4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B64")
    OP_A1(0xFE, 0x9C4, 0x2, 0x5, 0x6)
    Jump("loc_4B4C")

    label("loc_4B64")

    Return()

    # Function_28_4ABC end

    def Function_29_4B65(): pass

    label("Function_29_4B65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x1E)
    SoundLoad(825)
    SoundLoad(931)
    OP_68(102700, 1000, 0, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 102500, 250, -100, 90)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 102300, 0, 900, 135)
    Sound(825, 2, 100, 0)
    Sound(931, 2, 50, 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    Sleep(100)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#6P#02307FW-what the hell is this\x02\x03",
            "#02310FWhen the converted conductive energy is\x01",
            "Does it flow to the Orkis Tower! Is it?\x02",
        )
    )

    CloseMessageWindow()
    StopSound(825, 2000, 100)
    StopSound(931, 2000, 50)
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x8)
    OP_64(0xB)
    SetScenarioFlags(0x22, 1)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_4B65 end

    def Function_30_4CE1(): pass

    label("Function_30_4CE1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FOops, this is the way that came.\x02\x03",
            "#00000FBecause it's painful,\x01",
            "Let's return to the ground with a direct lift.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8310, -10, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_30_4CE1 end

    SaveToFile()

Try(main)
