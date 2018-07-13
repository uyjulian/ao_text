from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Jona",                   # 1
        "トルゾーＺ",             # 2
        "Dummy",                  # 3
        "Chief Roberts",          # 4
        "SE制御",                 # 5
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
        "Function_3_B69",          # 03, 3
        "Function_4_C4C",          # 04, 4
        "Function_5_1646",         # 05, 5
        "Function_6_173C",         # 06, 6
        "Function_7_19A6",         # 07, 7
        "Function_8_1B25",         # 08, 8
        "Function_9_1C59",         # 09, 9
        "Function_10_1DD8",        # 0A, 10
        "Function_11_1F0C",        # 0B, 11
        "Function_12_2EFA",        # 0C, 12
        "Function_13_2F82",        # 0D, 13
        "Function_14_2F9E",        # 0E, 14
        "Function_15_41B8",        # 0F, 15
        "Function_16_41D1",        # 10, 16
        "Function_17_41FD",        # 11, 17
        "Function_18_47AE",        # 12, 18
        "Function_19_47FC",        # 13, 19
        "Function_20_484A",        # 14, 20
        "Function_21_489F",        # 15, 21
        "Function_22_48F4",        # 16, 22
        "Function_23_4949",        # 17, 23
        "Function_24_499E",        # 18, 24
        "Function_25_4E73",        # 19, 25
        "Function_26_4E90",        # 1A, 26
        "Function_27_4EA9",        # 1B, 27
        "Function_28_4EC1",        # 1C, 28
        "Function_29_4F6A",        # 1D, 29
        "Function_30_50DF",        # 1E, 30
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B13")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_A9C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FC, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_B0E")

    label("loc_A9C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B0E")

    Jump("loc_B5D")

    label("loc_B13")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_B5D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_A17 end

    def Function_3_B69(): pass

    label("Function_3_B69")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Affixed on the pizza box, there is\x01",
            "a memo with written a simple recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_C48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Piping Hot Cheese Pizza"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C48")

    TalkEnd(0xFF)
    Return()

    # Function_3_B69 end

    def Function_4_C4C(): pass

    label("Function_4_C4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_134D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1239")
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#02301F(*klak klak, klakklakklakklak...*)\x02\x03",
            "#02310F...Craaap, it's no use like this too!!\x01",
            "Then, what if I try this key...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F(Somehow, he's putting his heart into it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FJona...what are you doing?\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DEA")
    Jump("loc_E34")

    label("loc_DEA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E0A")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E34")

    label("loc_E0A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2A")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E34")

    label("loc_E2A")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E34")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02305F...Oh, it's you guys.\x02\x03",
            "#02302FWell, I'm looking for something\x01",
            "that's been bothering me a little.\x02\x03",
            "#02306FI was just running an analysis\x01",
            "when being caught up in it...\x01",
            "This is quite the ruffian.\x02\x03",
            "#02309FEh eh, the blood of the great genius system\x01",
            "engineer Jona is stirring, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I see...well, all right.\x02\x03",
            "#00001F...Jona, did you see that speech?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02305FHmm...\x01",
            "That independence thing you mean?\x02\x03",
            "#02303FWell, I saw the relay with the terminal, but...\x01",
            "Honestly, I'm not interested for now.\x02\x03",
            "#02301FAt any rate, if you don't need anything,\x01",
            "could you go away?\x02\x03",
            "I wanna focus on analyzing\x01",
            "this data now.\x02",
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
            "#00303F(Uhhm...\x01",
            "It looks like he's totally\x01",
            "into that other world.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Conceitedness is Jona's bad habit...\x01",
            "I will chastise him later.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(N-Now now...\x01",
            "It's bad getting in his way, so\x01",
            "Let's come again on another chance.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 1)
    Jump("loc_1348")

    label("loc_1239")

    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#02301F(*klak klak, klakklakklakklak...*)\x02\x03",
            "#02310FEeehm, in this case...\x01",
            "...Gwaah, it's really no use!\x02\x03",
            "#02303FThen, I'll use a different approach again...\x01",
            "...*mumble mumble*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(He's completely absorbed in it...\x01",
            "Let's come again on another chance.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1348")

    Jump("loc_1642")

    label("loc_134D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_END)), "loc_1642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BB")

    ChrTalk(
        0x8,
        (
            "#02304FA top class net environment with perfect\x01",
            "air-conditioning... And furthermore, the feeling\x01",
            "of being isolated from the real world...\x02\x03",
            "#02302FUhhm, the No. 4 Control Terminal\x01",
            "is way better than I thought.\x02\x03",
            "#02309FWeeell then, I'll have to remake the settings of\x01",
            "this terminal environment according to my likings♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Uhhm, I really feel ashamed\x01",
            "since it appears I have helped\x01",
            "him to neglect his health...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Well, he is the type who can take\x01",
            "care of himself to a certain level,\x01",
            "so he will probably be fine.)\x02\x03",
            "#00200F(I will contact Chief Roberts\x01",
            "later about this.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1642")

    label("loc_15BB")


    ChrTalk(
        0x8,
        (
            "#02305F...Hmm, are you still there?\x02\x03",
            "#02306FI'm busy now, you know.\x01",
            "C'mon, c'mon, go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(H-He's getting me mad...)\x02",
    )

    CloseMessageWindow()

    label("loc_1642")

    TalkEnd(0xFE)
    Return()

    # Function_4_C4C end

    def Function_5_1646(): pass

    label("Function_5_1646")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172D")
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

    label("loc_172D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_1646 end

    def Function_6_173C(): pass

    label("Function_6_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 1)), scpexpr(EXPR_END)), "loc_1746")
    Return()

    label("loc_1746")

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
            "A large monster is wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Quit]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1822"),
        (SWITCH_DEFAULT, "loc_183B"),
    )


    label("loc_1822")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -5000, 0, 0, 270)
    EventEnd(0x5)
    Return()

    label("loc_183B")

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
        (2, "loc_18FD"),
        (1, "loc_1902"),
        (SWITCH_DEFAULT, "loc_1905"),
    )


    label("loc_18FD")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_1902")

    OP_B9(0x0)
    Return()

    label("loc_1905")

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
            "Wanted Monster exterminated!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0xBC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xBC, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 1)
    OP_29(0x94, 0x4, 0x2)
    OP_29(0x94, 0x4, 0x10)
    OP_29(0x94, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_6_173C end

    def Function_7_19A6(): pass

    label("Function_7_19A6")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1D")
    Fade(500)
    SetChrPos(0x0, 111500, 0, 203500, 90)
    SetChrPos(0x1, 111500, 0, 204500, 90)
    SetChrPos(0x2, 110500, 0, 203500, 90)
    SetChrPos(0x3, 110500, 0, 204500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A76")
    SetChrPos(0x13E, 109500, 0, 204000, 90)

    label("loc_1A76")

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

    label("loc_1B1D")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_19A6 end

    def Function_8_1B25(): pass

    label("Function_8_1B25")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD6")
    SetChrPos(0x13E, 122500, 2750, 203500, 180)

    label("loc_1BD6")

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

    # Function_8_1B25 end

    def Function_9_1C59(): pass

    label("Function_9_1C59")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lift control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD0")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 500, 90)
    SetChrPos(0x1, -296500, 0, 1500, 90)
    SetChrPos(0x2, -297500, 0, 500, 90)
    SetChrPos(0x3, -297500, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D29")
    SetChrPos(0x13E, -298500, 0, 1000, 90)

    label("loc_1D29")

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

    label("loc_1DD0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1C59 end

    def Function_10_1DD8(): pass

    label("Function_10_1DD8")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E89")
    SetChrPos(0x13E, -285500, 2750, 500, 180)

    label("loc_1E89")

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

    # Function_10_1DD8 end

    def Function_11_1F0C(): pass

    label("Function_11_1F0C")

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

    def lambda_20C1():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20C1)
    Sleep(50)

    def lambda_20DE():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_20DE)
    Sleep(50)

    def lambda_20FB():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_20FB)
    Sleep(50)

    def lambda_2118():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2118)
    Sleep(50)

    def lambda_2135():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2135)
    Sleep(50)

    def lambda_2152():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2152)
    Sleep(50)

    def lambda_216F():
        OP_97(0x13E, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 0, lambda_216F)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x13E, 0)
    OP_63(0x13E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13E,
        "#6P#02305FAh...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(29500, 1500, 0, 4000)
    MoveCamera(42, 27, 0, 4000)
    SetCameraDistance(24500, 4000)

    def lambda_21F2():
        OP_95(0xFE, -1500, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_21F2)
    WaitChrThread(0x13E, 1)
    OP_6F(0x79)

    ChrTalk(
        0x13E,
        (
            "#02302FThat, that!\x01",
            "That's the "No. 4 Control Terminal" over there!\x02\x03",
            "#02309F*siiigh*, it was so far!\x02",
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

    def lambda_22B1():
        OP_97(0x101, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22B1)
    Sleep(50)

    def lambda_22CE():
        OP_97(0x102, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22CE)
    Sleep(50)

    def lambda_22EB():
        OP_97(0x103, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_22EB)
    Sleep(50)

    def lambda_2308():
        OP_97(0x104, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2308)
    Sleep(50)

    def lambda_2325():
        OP_97(0x109, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2325)
    Sleep(50)

    def lambda_2342():
        OP_97(0x105, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2342)
    OP_0D()
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x104,
        (
            "#00306FOh man, and when\x01",
            "WE did all the work.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2393():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_2393)

    ChrTalk(
        0x109,
        (
            "#6P#10112FUh uh, now now.\x02\x03",
            "#10100FSince he's not used to it, even just following\x01",
            "us must've been hard for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FRight...\x01",
            "It was tough for us too the first times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FIn particular, Jona stays indoor\x01",
            "more than the past me...\x02\x03",
            "#00204FSo, I think he\x01",
            "did not too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        "#02310F#11PMgrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PStill, until you're young it could\x01",
            "be fine, but when you'll become an\x01",
            "adult it could be bad, right?\x02\x03",
            "#10302FIn addition, it seems you like\x01",
            "pizza and snacks, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FJona, if you want, why don't\x01",
            "we jog together in the morning?\x02\x03",
            "#00000FEven once a week would be ok, you know.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02311F#11PAah, jeez, leave me alone!\x02\x03",
            "#02301FAt any rate, it's hot here, so let's enter the\x01",
            "terminal room and cool down with the air con──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#6P#00207F#4SJona, over here!\x02",
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

    def lambda_2774():
        OP_96(0xFE, 0xBB8, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2774)
    WaitChrThread(0x9, 1)
    CancelBlur(0)
    OP_63(0x13E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_27AF():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_27AF)
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

    def lambda_284D():

        label("loc_284D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_284D")

    QueueWorkItem2(0x13E, 2, lambda_284D)

    def lambda_285F():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_285F)
    WaitChrThread(0x13E, 1)
    EndChrThread(0x13E, 0x2)
    OP_64(0x13E)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        "#02307F#4S#6P#NW-Whaaaat!?\x02",
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
        "#00010F#6P#NWhat's this thing...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#6P#NA huge version of those cleanin' machines\x01",
            "that were loiterin' around the B-Division?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#6P#NNo, it doesn't look like\x01",
            "such a simple thing...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#5PJona, stay back!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13E, 0x102, 500)

    ChrTalk(
        0x13E,
        "#02310F#12P#NG-Got it...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x13E, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x13E, 0x10E, 0x1F4)

    def lambda_2A3A():
        OP_95(0xFE, -6500, 0, -2500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2A3A)
    WaitChrThread(0x13E, 1)
    OP_68(-1600, 2000, 0, 10000)
    MoveCamera(64, 13, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(15500, 10000)

    def lambda_2A86():
        OP_95(0xFE, -9000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2A86)
    WaitChrThread(0x13E, 1)

    def lambda_2AA4():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2AA4)
    WaitChrThread(0x13E, 1)
    OP_64(0x13E)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(270, 90, -1, -1)
    SetChrName("Electronic Sound")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Beep beep beep beep...\x01",
            "TARGETS ACQUIRED...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...ACCESSING THE NETWORK...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "TARGET GROUP IDENTIFIED...\x01",
            "CROSSBELL POLICE, SPECIAL SUPPORT SECTION...\x07\x00\x02",
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
        "#00011F#6P#NW-What the!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#6P#N...Impossible...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10310F#6P#NDid he identify us accessing\x01",
            "the network on its own!?\x02",
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
    SetChrName("Electronic Sound")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Beep beep beep...\x01",
            "LEVEL OF DANGER: 3...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "REMOVING FOR THE TIME BEING...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00111F#6P#NF-For the time being...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NAlthough you're a machine,\x01",
            "you're too approximate!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10107F#6P#NIn any case, let's repel it!\x02",
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

    # Function_11_1F0C end

    def Function_12_2EFA(): pass

    label("Function_12_2EFA")

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

    # Function_12_2EFA end

    def Function_13_2F82(): pass

    label("Function_13_2F82")

    OP_71(0x0, 0x96, 0xAA, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_13_2F82 end

    def Function_14_2F9E(): pass

    label("Function_14_2F9E")

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
        "#00013F#6PThat machine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PI-It didn't appear to be on\x01",
            "the level of an unlawfully\x01",
            "dumped machine at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FThe "Society" involvement\x01",
            "could be very possible...\x02\x03",
            "#00201FIt reacted like the archaism that was\x01",
            "guarding the Revache's President office.\x02",
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

    def lambda_327A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_327A)
    Sleep(50)

    def lambda_328A():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_328A)
    Sleep(50)

    def lambda_329A():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_329A)
    Sleep(50)

    def lambda_32AA():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_32AA)
    Sleep(50)

    def lambda_32BA():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_32BA)
    Sleep(50)

    def lambda_32CA():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_32CA)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x104,
        (
            "#00306F#5PThat warrior-like thing, huh...?\x02\x03",
            "#00301FWasn't this one somehow doin' more \x01",
            "advanced stuff than that one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308FHm, it also appears it was\x01",
            "accessing the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FCould the "Society" really\x01",
            "be up to something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02304F#2P──Well, no use in thinking\x01",
            "about it, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3424():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_3424)
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

    def lambda_34C4():

        label("loc_34C4")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_34C4")

    QueueWorkItem2(0x109, 2, lambda_34C4)

    def lambda_34D6():

        label("loc_34D6")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_34D6")

    QueueWorkItem2(0x105, 2, lambda_34D6)
    Sleep(50)

    def lambda_34EB():

        label("loc_34EB")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_34EB")

    QueueWorkItem2(0x103, 2, lambda_34EB)

    def lambda_34FD():

        label("loc_34FD")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_34FD")

    QueueWorkItem2(0x104, 2, lambda_34FD)
    Sleep(50)

    def lambda_3512():

        label("loc_3512")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3512")

    QueueWorkItem2(0x101, 2, lambda_3512)

    def lambda_3524():

        label("loc_3524")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3524")

    QueueWorkItem2(0x102, 2, lambda_3524)
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
            "#6P#02306FMore importantly, let's go to cool\x01",
            "in the terminal room AC already!\x02\x03",
            "#02302FThe great Jona will search for you various\x01",
            "stuff about those guys' activities.\x02",
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
            "#00006F#11PListen...I don't know if you're\x01",
            "happy-go-lucky or bold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FUh uh, it's true he seems\x01",
            "to have guts.\x02",
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
            "#02305F#5PHm hm...\x01",
            "It appears that that machine\x01",
            "was released one month ago.\x02\x03",
            "#02303FIt seems it's equipped with a device that\x01",
            "can link to the orbal net wirelessly...\x02\x03",
            "#02301F"Novartis" remains as the\x01",
            "name of its manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FNovartis...that man in a white robe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIt appears he's got quite the\x01",
            "status among the "Society" too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A09():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A09)
    Sleep(50)

    def lambda_3A19():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3A19)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#5PIt was a weird old man...\x01",
            "Mad, I'd say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206F...He could have released a\x01",
            "test prototype just for sport.\x02\x03",
            "#00211FYou know, he seemed to have a personality\x01",
            "that really likes to do things like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10306FYeah, he really looked like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FWithout a doubt he was more a dangerous\x01",
            "person that what meets the eye...\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    BeginChrThread(0x13E, 2, 0, 15)

    ChrTalk(
        0x13E,
        (
            "#02304F#5PWell, it appears there weren't\x01",
            "released more than that, so...\x02\x03",
            "#02302FIt means that now I can stay\x01",
            "indoor without reserve!\x02\x03",
            "Maaan, since it's close to the tower,\x01",
            "not only the line speed is crazily fast,\x01",
            "but it's got almost no limits too...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02309F#5P#4SYEAH!\x01",
            "The No. 4 Control Terminal is the best!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_3D29():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3D29)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_3D66():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3D66)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00012FHe's in high spirits, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FHe's fully brimmin' with\x01",
            "a shut-in spirit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FJona...send a report to\x01",
            "Chief Roberts, will you?\x02\x03",
            "#00211FYou shouldn't do too much what you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02304F#5PAah, yeah, yeah.\x02\x03",
            "#02302FI'll be fine alone here, so you\x01",
            "can go away at once, you know?\x02\x03",
            "#02305F──Whoa, they made a new\x01",
            "server in such a place.\x02\x03",
            "#02309FMaaan, even the Crossbell network\x01",
            "environment is quite satisfying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FOh boy...\x01",
            "It looks like he's already absorbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FUh uh...\x01",
            "However, it looks like he'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FYes, although the "Society"\x01",
            "movements worry me a little...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00004FWell, let's come every now and\x01",
            "then to see how he's doing.\x02\x03",
            "#00000FI'm a little worried if he keeps\x01",
            "staying holed up in here like this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_40CB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_40CB)
    Sleep(50)

    def lambda_40DB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_40DB)
    Sleep(50)

    def lambda_40EB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_40EB)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x103,
        "#5P#00202FRight.\x02",
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

    # Function_14_2F9E end

    def Function_15_41B8(): pass

    label("Function_15_41B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41D0")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_15_41B8")

    label("loc_41D0")

    Return()

    # Function_15_41B8 end

    def Function_16_41D1(): pass

    label("Function_16_41D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41FC")
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(800)
    Jump("Function_16_41D1")

    label("loc_41FC")

    Return()

    # Function_16_41D1 end

    def Function_17_41FD(): pass

    label("Function_17_41FD")

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
            "#11P#00005FBy the way....\x02\x03",
            "#00000FDidn't Jona say that \x01",
            "there's a direct lift that \x01",
            "connects to the exit?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#12P#00202FYes, it is that way.\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1100, 25500, 4000)
    MoveCamera(30, 25, 0, 4000)
    SetCameraDistance(26000, 4000)

    def lambda_4465():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4465)
    Sleep(50)

    def lambda_4475():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4475)
    Sleep(50)

    def lambda_4485():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4485)
    Sleep(50)

    def lambda_4495():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4495)
    Sleep(50)

    def lambda_44A5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_44A5)
    OP_6F(0x79)
    Sleep(300)

    AnonymousTalk(
        0x103,
        (
            "#00204FIt seems that this place is\x01",
            "located in the environs at\x01",
            "the Orchis Tower base.\x02\x03",
            "#00202FFrom there, the lift should come out\x01",
            "straightly to the Waterfront Area lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#00106F*sigh*, that would really help us.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00306FIt'd be really a bother going back\x01",
            "through all that friggin' heat again.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        "#10309FHu hu, really.\x02",
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
            "#10300F#5PEven so...\x01",
            "I guess it's evening already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4681():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4681)
    Sleep(50)

    def lambda_4691():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4691)
    Sleep(50)

    def lambda_46A1():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_46A1)
    Sleep(50)

    def lambda_46B1():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_46B1)
    Sleep(50)

    def lambda_46C1():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_46C1)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x109,
        "#12P#10106FYes, you're right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10112F#11P...So, should we use the lift\x01",
            "and go back to the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FYeah...let's.\x02",
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

    # Function_17_41FD end

    def Function_18_47AE(): pass

    label("Function_18_47AE")


    def lambda_47B3():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47B3)

    def lambda_47CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47CD)
    WaitChrThread(0xFE, 1)

    def lambda_47E2():
        OP_96(0xFE, 0x6A40, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47E2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_47AE end

    def Function_19_47FC(): pass

    label("Function_19_47FC")


    def lambda_4801():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4801)

    def lambda_481B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_481B)
    WaitChrThread(0xFE, 1)

    def lambda_4830():
        OP_96(0xFE, 0x6A40, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4830)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_47FC end

    def Function_20_484A(): pass

    label("Function_20_484A")


    def lambda_484F():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_484F)

    def lambda_4869():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4869)
    WaitChrThread(0xFE, 1)

    def lambda_487E():
        OP_95(0xFE, 28200, 0, -1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_487E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_484A end

    def Function_21_489F(): pass

    label("Function_21_489F")


    def lambda_48A4():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48A4)

    def lambda_48BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48BE)
    WaitChrThread(0xFE, 1)

    def lambda_48D3():
        OP_95(0xFE, 28200, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48D3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_489F end

    def Function_22_48F4(): pass

    label("Function_22_48F4")


    def lambda_48F9():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48F9)

    def lambda_4913():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4913)
    WaitChrThread(0xFE, 1)

    def lambda_4928():
        OP_95(0xFE, 29200, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4928)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_48F4 end

    def Function_23_4949(): pass

    label("Function_23_4949")


    def lambda_494E():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_494E)

    def lambda_4968():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4968)
    WaitChrThread(0xFE, 1)

    def lambda_497D():
        OP_95(0xFE, 29200, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_497D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_4949 end

    def Function_24_499E(): pass

    label("Function_24_499E")

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
            "#5P#02306FHmmm...!\x02\x03",
            "#02301FOh, what time is it...?\x02\x03",
            "#02305F...Wait, it's already morning!?\x02",
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
            "#5P#02306F*sigh*...\x01",
            "I'm really hungry.\x02\x03",
            "#02300FHmm, what hours did that\x01",
            "pizza shop do again?\x02",
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
            "#6P#02302FIf I remember correctly they said they were\x01",
            "testing to introduce the orbal net...\x02\x03",
            "#02309FEh eh, I'll check in a moment...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#6P#02305FWhat...?\x02\x03",
            "#02301F...What's this?\x01",
            "Some garbage-like data...\x02",
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
        "#6P#02310FNo, it's not data?\x02",
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
            "#6P#02310F...A structure...?\x01",
            "No, more importantly, it's way too...\x02\x03",
            "#02305F........................\x02",
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
        "What the heck is thiiis?\x02",
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

    # Function_24_499E end

    def Function_25_4E73(): pass

    label("Function_25_4E73")

    Sleep(2200)

    label("loc_4E76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E8F")
    Sound(836, 0, 50, 0)
    Sleep(700)
    Jump("loc_4E76")

    label("loc_4E8F")

    Return()

    # Function_25_4E73 end

    def Function_26_4E90(): pass

    label("Function_26_4E90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EA8")
    OP_A1(0xFE, 0x5DC, 0x2, 0x3, 0x4)
    Jump("Function_26_4E90")

    label("loc_4EA8")

    Return()

    # Function_26_4E90 end

    def Function_27_4EA9(): pass

    label("Function_27_4EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC0")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_27_4EA9")

    label("loc_4EC0")

    Return()

    # Function_27_4EA9 end

    def Function_28_4EC1(): pass

    label("Function_28_4EC1")

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

    label("loc_4F51")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F69")
    OP_A1(0xFE, 0x9C4, 0x2, 0x5, 0x6)
    Jump("loc_4F51")

    label("loc_4F69")

    Return()

    # Function_28_4EC1 end

    def Function_29_4F6A(): pass

    label("Function_29_4F6A")

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
            "#6P#02307FT-The heck is this...!?\x02\x03",
            "#02310FConverted orbal energy is\x01",
            "flowing into Orchis Tower!?\x02",
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

    # Function_29_4F6A end

    def Function_30_50DF(): pass

    label("Function_30_50DF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FOops, this lead to where we came.\x02\x03",
            "#00000FSince we're here, let's go back to\x01",
            "the surface using the direct lift.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8310, -10, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_30_50DF end

    SaveToFile()

Try(main)
