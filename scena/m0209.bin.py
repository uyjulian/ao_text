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
        "Function_3_B68",          # 03, 3
        "Function_4_C37",          # 04, 4
        "Function_5_15DB",         # 05, 5
        "Function_6_16CF",         # 06, 6
        "Function_7_193B",         # 07, 7
        "Function_8_1AB3",         # 08, 8
        "Function_9_1BE7",         # 09, 9
        "Function_10_1D5F",        # 0A, 10
        "Function_11_1E93",        # 0B, 11
        "Function_12_2E1E",        # 0C, 12
        "Function_13_2EA6",        # 0D, 13
        "Function_14_2EC2",        # 0E, 14
        "Function_15_4062",        # 0F, 15
        "Function_16_407B",        # 10, 16
        "Function_17_40A7",        # 11, 17
        "Function_18_461D",        # 12, 18
        "Function_19_466B",        # 13, 19
        "Function_20_46B9",        # 14, 20
        "Function_21_470E",        # 15, 21
        "Function_22_4763",        # 16, 22
        "Function_23_47B8",        # 17, 23
        "Function_24_480D",        # 18, 24
        "Function_25_4CB6",        # 19, 25
        "Function_26_4CD3",        # 1A, 26
        "Function_27_4CEC",        # 1B, 27
        "Function_28_4D04",        # 1C, 28
        "Function_29_4DAD",        # 1D, 29
        "Function_30_4F1F",        # 1E, 30
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
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B0E")

    Jump("loc_B5C")

    label("loc_B13")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
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
            "There's a note with a\x01",
            "simple recipe on the\x01",
            "pizza box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_C33")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C33")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Piping Hot\x01",
            "Cheese Pizza"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C33")

    TalkEnd(0xFF)
    Return()

    # Function_3_B68 end

    def Function_4_C37(): pass

    label("Function_4_C37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F8")
    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#02301F(*klak klak,\x01",
            "klakklakklakklak...*)\x02\x03",
            "#02310F...Craaap, this way's no\x01",
            "good either!! Then, it'll\x01",
            "try this key and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(He seems quite absorbed\x01",
            "in that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FJona... What are you\x01",
            "doing?\x02",
        )
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DCE")
    Jump("loc_E18")

    label("loc_DCE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DEE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E18")

    label("loc_DEE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0E")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E18")

    label("loc_E0E")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E18")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02305F...Oh, you guys, huh.\x02\x03",
            "#02302FWell, I was just looking\x01",
            "for something that's been\x01",
            "bothering me.\x02\x03",
            "#02306FI was just getting fired up\x01",
            "while doing an analysis...\x01",
            "This thing is quite tough.\x02\x03",
            "#02309FHehe. The blood of great\x01",
            "genius system engineer Jona\x01",
            "is stirring, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I see... Well, all\x01",
            "right.\x02\x03",
            "#00001F...Jona, did you see\x01",
            "that speech?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02305FHmm... That independence\x01",
            "thing you mean?\x02\x03",
            "#02303FWell, I saw it on the\x01",
            "terminal, but... Honestly,\x01",
            "I'm not interested for now.\x02\x03",
            "#02301FAt any rate, if you don't\x01",
            "need anything, could you go\x01",
            "away?\x02\x03",
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
            "#00303F(Hmm... Looks like he's\x01",
            "totally in his own\x01",
            "world.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Impertinence is Jona's\x01",
            "bad habit... I'll scold\x01",
            "him later)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(N-Now now... We shouldn't\x01",
            "get in his way. Let's come\x01",
            "again if we get the chance.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 1)
    Jump("loc_130B")

    label("loc_11F8")

    SetChrSubChip(0x8, 0x0)

    ChrTalk(
        0x8,
        (
            "#02301F(*klak klak,\x01",
            "klakklakklakklak...*)\x02\x03",
            "#02310FEeehm, in this case...\x01",
            "...Gwaah, it's really no\x01",
            "use!\x02\x03",
            "#02303FThen, I'll use a different\x01",
            "approach again...\x01",
            "...*mumble mumble*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(He's totally absorbed in\x01",
            "it... Let's come again if\x01",
            "we get another chance.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130B")

    Jump("loc_15D7")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 7)), scpexpr(EXPR_END)), "loc_15D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1554")

    ChrTalk(
        0x8,
        (
            "#02304FA top class net environment with perfect air-\x01",
            "conditioning... And furthermore, the feeling\x01",
            "of being isolated from the real world...\x02\x03",
            "#02302FHmm, the No. 4 Control Terminal is way better\x01",
            "than I thought.\x02\x03",
            "#02309FWeeell then, I'll have to remake the terminal\x01",
            "environment settings to my liking♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Hmm. I really feel\x01",
            "ashamed for helping him\x01",
            "neglect his own health...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Well, he's the type who can take\x01",
            "care of himself to a certain\x01",
            "degree, so he'll probably be fine.)\x02\x03",
            "#00200F(I'll contact Chief Roberts later\x01",
            "about this.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_15D7")

    label("loc_1554")


    ChrTalk(
        0x8,
        (
            "#02305F...Huh? You're still\x01",
            "here?\x02\x03",
            "#02306FI'm busy, you know.\x01",
            "C'mon, go home already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(H-He's making me\x01",
            "angry...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D7")

    TalkEnd(0xFE)
    Return()

    # Function_4_C37 end

    def Function_5_15DB(): pass

    label("Function_5_15DB")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an orbment charging station.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C0")
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

    label("loc_16C0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_15DB end

    def Function_6_16CF(): pass

    label("Function_6_16CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 1)), scpexpr(EXPR_END)), "loc_16D9")
    Return()

    label("loc_16D9")

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
            "A large monster is\x01",
            "wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_17B7"),
        (SWITCH_DEFAULT, "loc_17D0"),
    )


    label("loc_17B7")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -5000, 0, 0, 270)
    EventEnd(0x5)
    Return()

    label("loc_17D0")

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
        (2, "loc_1892"),
        (1, "loc_1897"),
        (SWITCH_DEFAULT, "loc_189A"),
    )


    label("loc_1892")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_1897")

    OP_B9(0x0)
    Return()

    label("loc_189A")

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
            "Wanted monster\x01",
            "exterminated!\x02",
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

    # Function_6_16CF end

    def Function_7_193B(): pass

    label("Function_7_193B")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AAB")
    Fade(500)
    SetChrPos(0x0, 111500, 0, 203500, 90)
    SetChrPos(0x1, 111500, 0, 204500, 90)
    SetChrPos(0x2, 110500, 0, 203500, 90)
    SetChrPos(0x3, 110500, 0, 204500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A04")
    SetChrPos(0x13E, 109500, 0, 204000, 90)

    label("loc_1A04")

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

    label("loc_1AAB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_193B end

    def Function_8_1AB3(): pass

    label("Function_8_1AB3")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B64")
    SetChrPos(0x13E, 122500, 2750, 203500, 180)

    label("loc_1B64")

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

    # Function_8_1AB3 end

    def Function_9_1BE7(): pass

    label("Function_9_1BE7")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control\x01",
            "panel. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D57")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 500, 90)
    SetChrPos(0x1, -296500, 0, 1500, 90)
    SetChrPos(0x2, -297500, 0, 500, 90)
    SetChrPos(0x3, -297500, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB0")
    SetChrPos(0x13E, -298500, 0, 1000, 90)

    label("loc_1CB0")

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

    label("loc_1D57")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1BE7 end

    def Function_10_1D5F(): pass

    label("Function_10_1D5F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3D)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E10")
    SetChrPos(0x13E, -285500, 2750, 500, 180)

    label("loc_1E10")

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

    # Function_10_1D5F end

    def Function_11_1E93(): pass

    label("Function_11_1E93")

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

    def lambda_2048():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2048)
    Sleep(50)

    def lambda_2065():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2065)
    Sleep(50)

    def lambda_2082():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2082)
    Sleep(50)

    def lambda_209F():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_209F)
    Sleep(50)

    def lambda_20BC():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20BC)
    Sleep(50)

    def lambda_20D9():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_20D9)
    Sleep(50)

    def lambda_20F6():
        OP_97(0x13E, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 0, lambda_20F6)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x13E, 0)
    OP_63(0x13E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13E,
        "#6P#02305FAh!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(29500, 1500, 0, 4000)
    MoveCamera(42, 27, 0, 4000)
    SetCameraDistance(24500, 4000)

    def lambda_2176():
        OP_95(0xFE, -1500, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2176)
    WaitChrThread(0x13E, 1)
    OP_6F(0x79)

    ChrTalk(
        0x13E,
        (
            "#02302FThere, there it is! It's\x01",
            "the "No. 4 Control\x01",
            "Terminal"!\x02\x03",
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

    def lambda_2230():
        OP_97(0x101, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2230)
    Sleep(50)

    def lambda_224D():
        OP_97(0x102, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_224D)
    Sleep(50)

    def lambda_226A():
        OP_97(0x103, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_226A)
    Sleep(50)

    def lambda_2287():
        OP_97(0x104, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2287)
    Sleep(50)

    def lambda_22A4():
        OP_97(0x109, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_22A4)
    Sleep(50)

    def lambda_22C1():
        OP_97(0x105, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_22C1)
    OP_0D()
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x104,
        (
            "#00306FOh man. We're the ones\x01",
            "who did all the work.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2319():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13E, 2, lambda_2319)

    ChrTalk(
        0x109,
        (
            "#6P#10112FHaha. Now, now.\x02\x03",
            "#10100FHe's not used to this,\x01",
            "so it must've been hard\x01",
            "just keeping up with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FRight... It was tough\x01",
            "for us too, at first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FIt's because Jona stays\x01",
            "indoors even more than I\x01",
            "once did...\x02\x03",
            "#00204FEven so, I don't think\x01",
            "he did too badly.\x02",
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
            "#10306F#6PIt's fine when you're young,\x01",
            "but it'll be tough when you\x01",
            "get older, you know?\x02\x03",
            "#10302FAs it is, pizza and snacks\x01",
            "are your favorite foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FJona, if you want, why\x01",
            "don't we go for a\x01",
            "morning jog?\x02\x03",
            "#00000FEven once a week would\x01",
            "be ok, you know.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02311F#11PAah, jeez, leave me alone!\x02\x03",
            "#02301FAnyway, it's hot in here, so\x01",
            "let's enter the terminal room\x01",
            "and cool down with the air con─\x02",
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

    def lambda_26D6():
        OP_96(0xFE, 0xBB8, 0x0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26D6)
    WaitChrThread(0x9, 1)
    CancelBlur(0)
    OP_63(0x13E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2711():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_2711)
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

    def lambda_27AF():

        label("loc_27AF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_27AF")

    QueueWorkItem2(0x13E, 2, lambda_27AF)

    def lambda_27C1():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_27C1)
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
        "#00010F#6P#NWhat is this thing!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#6P#NA huge version of those\x01",
            "B-Division cleanin'\x01",
            "machines?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00201F#6P#NNo, it doesn't look that\x01",
            "simple!\x02",
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

    def lambda_296B():
        OP_95(0xFE, -6500, 0, -2500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_296B)
    WaitChrThread(0x13E, 1)
    OP_68(-1600, 2000, 0, 10000)
    MoveCamera(64, 13, 0, 10000)
    OP_6E(700, 10000)
    SetCameraDistance(15500, 10000)

    def lambda_29B7():
        OP_95(0xFE, -9000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_29B7)
    WaitChrThread(0x13E, 1)

    def lambda_29D5():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_29D5)
    WaitChrThread(0x13E, 1)
    OP_64(0x13E)
    Sound(903, 0, 100, 0)
    SetMessageWindowPos(270, 90, -1, -1)
    SetChrName("Electronic Voice")

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
            "...ACCESSING NETWORK...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "TARGET GROUP IDENTIFIED...\x01",
            "CROSSBELL POLICE, SPECIAL\x01",
            "SUPPORT SECTION...\x07\x00\x02",
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
            "#10310F#6P#NDid it access the\x01",
            "network just to identify\x01",
            "us!?\x02",
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
    SetChrName("Electronic Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Beep beep beep... DANGER\x01",
            "LEVEL: 3...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ELIMINATING FOR THE TIME\x01",
            "BEING...\x07\x00\x02",
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
            "#00310F#6P#NAlthough you're a\x01",
            "machine, you're too\x01",
            "approximate!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10107F#6P#NAnyway, let's destroy\x01",
            "it!\x02",
        )
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

    # Function_11_1E93 end

    def Function_12_2E1E(): pass

    label("Function_12_2E1E")

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

    # Function_12_2E1E end

    def Function_13_2EA6(): pass

    label("Function_13_2EA6")

    OP_71(0x0, 0x96, 0xAA, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x31, 0x0, 0x20)
    Return()

    # Function_13_2EA6 end

    def Function_14_2EC2(): pass

    label("Function_14_2EC2")

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
            "#00106F#5PNo matter how you think about it,\x01",
            "it wasn't on the same level as an\x01",
            "unlawfully discarded one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FOuroboros is likely\x01",
            "involved...\x02\x03",
            "#00201FIts response was like that\x01",
            "of the one guarding the\x01",
            "Revache president's office.\x02",
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

    def lambda_319A():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_319A)
    Sleep(50)

    def lambda_31AA():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_31AA)
    Sleep(50)

    def lambda_31BA():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_31BA)
    Sleep(50)

    def lambda_31CA():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31CA)
    Sleep(50)

    def lambda_31DA():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_31DA)
    Sleep(50)

    def lambda_31EA():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_31EA)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x104,
        (
            "#00306F#5PThat warrior-like thing,\x01",
            "huh...\x02\x03",
            "#00301FWasn't this more\x01",
            "advanced stuff than that\x01",
            "one somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308FHm, it appears it also\x01",
            "accessed the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FCould Ouroboros really\x01",
            "be up to something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02304F#2P─Well, no use thinking\x01",
            "about it, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_332A():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13E, 1, lambda_332A)
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

    def lambda_33CA():

        label("loc_33CA")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_33CA")

    QueueWorkItem2(0x109, 2, lambda_33CA)

    def lambda_33DC():

        label("loc_33DC")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_33DC")

    QueueWorkItem2(0x105, 2, lambda_33DC)
    Sleep(50)

    def lambda_33F1():

        label("loc_33F1")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_33F1")

    QueueWorkItem2(0x103, 2, lambda_33F1)

    def lambda_3403():

        label("loc_3403")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3403")

    QueueWorkItem2(0x104, 2, lambda_3403)
    Sleep(50)

    def lambda_3418():

        label("loc_3418")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_3418")

    QueueWorkItem2(0x101, 2, lambda_3418)

    def lambda_342A():

        label("loc_342A")

        TurnDirection(0xFE, 0x13E, 500)
        Yield()
        Jump("loc_342A")

    QueueWorkItem2(0x102, 2, lambda_342A)
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
            "#6P#02306FMore importantly, let's go cool\x01",
            "off in the terminal room AC\x01",
            "already!\x02\x03",
            "#02302FI, the great Jona, will look up\x01",
            "all sorts of stuff about those\x01",
            "guys' activities for you.\x02",
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
            "#00006F#11PYou... I don't know if\x01",
            "you're reckless or bold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112FHaha. He's certainly got\x01",
            "guts.\x02",
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
            "#02305F#5PHm hm... It appears that\x01",
            "that machine was released a\x01",
            "month ago.\x02\x03",
            "#02303FIt's equipped with a device\x01",
            "that can wirelessly connect\x01",
            "to the orbal net...\x02\x03",
            "#02301F"Novartis" is registered as\x01",
            "its manager's name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00008FNovartis... That man in\x01",
            "a white robe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIt appears he's got\x01",
            "quite the status within\x01",
            "Ouroboros as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3904():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3904)
    Sleep(50)

    def lambda_3914():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3914)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        (
            "#00301F#5PHe was a weird old\x01",
            "man... Mad, I'd say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206F...It might have been a\x01",
            "prototype he unleashed for\x01",
            "fun.\x02\x03",
            "#00211FHow to say it... It seemed\x01",
            "like he's the kind of person\x01",
            "who enjoys such things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FYeah, I got that feeling\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FIt's certain he's more\x01",
            "dangerous that he\x01",
            "appears...\x02",
        )
    )

    CloseMessageWindow()
    Sound(938, 2, 100, 0)
    BeginChrThread(0x13E, 2, 0, 15)

    ChrTalk(
        0x13E,
        (
            "#02304F#5PWell, looks like he didn't unleash any\x01",
            "more, so...\x02\x03",
            "#02302FThat means I can stay indoors all I\x01",
            "want!\x02\x03",
            "Maaan, since it's so close to the tower,\x01",
            "not only is the line speed is crazily\x01",
            "fast, but it's got almost no limits...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x13E,
        (
            "#02309F#5P#4SYEAH! The No. 4 Control\x01",
            "Terminal is the best!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_3BEF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3BEF)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_3C2C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3C2C)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00012FSomebody's excited.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FFull of shut-in spirit,\x01",
            "isn't he...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FJona... I'm sending a\x01",
            "report to Chief Roberts,\x01",
            "ok?\x02\x03",
            "#00211FSo that you don't go too\x01",
            "crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13E,
        (
            "#02304F#5PAah, yeah, yeah.\x02\x03",
            "#02302FI'll be fine here by\x01",
            "myself, so you can go\x01",
            "leave already, you know?\x02\x03",
            "#02305F─Whoa, they made a new\x01",
            "server in a place like\x01",
            "this.\x02\x03",
            "#02309FMaaan, even Crossbell's\x01",
            "network environment is\x01",
            "quite satisfying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FOh man... Looks like he\x01",
            "already got sucked in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FHaha... However, it\x01",
            "looks like he'll be\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FYes, although Ouroboros'\x01",
            "actions worry me a\x01",
            "little...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00004FWell, let's come here to\x01",
            "check on him every now\x01",
            "and then.\x02\x03",
            "#00000FI'll worry about him if\x01",
            "he stays holed up in\x01",
            "here for too long.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F75():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F75)
    Sleep(50)

    def lambda_3F85():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F85)
    Sleep(50)

    def lambda_3F95():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3F95)
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

    # Function_14_2EC2 end

    def Function_15_4062(): pass

    label("Function_15_4062")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_407A")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_15_4062")

    label("loc_407A")

    Return()

    # Function_15_4062 end

    def Function_16_407B(): pass

    label("Function_16_407B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40A6")
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(600)
    Sound(836, 0, 100, 0)
    Sleep(800)
    Jump("Function_16_407B")

    label("loc_40A6")

    Return()

    # Function_16_407B end

    def Function_17_40A7(): pass

    label("Function_17_40A7")

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
            "#00000FDidn't Jona say that\x01",
            "there's a direct lift to\x01",
            "the exit?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#12P#00202FYes, it's that way.\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1100, 25500, 4000)
    MoveCamera(30, 25, 0, 4000)
    SetCameraDistance(26000, 4000)

    def lambda_42FE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42FE)
    Sleep(50)

    def lambda_430E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_430E)
    Sleep(50)

    def lambda_431E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_431E)
    Sleep(50)

    def lambda_432E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_432E)
    Sleep(50)

    def lambda_433E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_433E)
    OP_6F(0x79)
    Sleep(300)

    AnonymousTalk(
        0x103,
        (
            "#00204FIt seems this place is near\x01",
            "the base of Orchis Tower.\x02\x03",
            "#00202FFrom there, the lift will\x01",
            "take us straight to the\x01",
            "Waterfront Area lighthouse.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#00106F*sigh*, that's a big\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#00306FIt'd be a real pain\x01",
            "going back through that\x01",
            "damn heat again.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        "#10309FHehe. You said it.\x02",
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
            "#10300F#5PEven so... I guess it's\x01",
            "evening already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44ED():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44ED)
    Sleep(50)

    def lambda_44FD():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_44FD)
    Sleep(50)

    def lambda_450D():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_450D)
    Sleep(50)

    def lambda_451D():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_451D)
    Sleep(50)

    def lambda_452D():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_452D)
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
            "#10112F#11P...So, should we use the\x01",
            "lift and head back to\x01",
            "the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FYeah... Let's.\x02",
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

    # Function_17_40A7 end

    def Function_18_461D(): pass

    label("Function_18_461D")


    def lambda_4622():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4622)

    def lambda_463C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_463C)
    WaitChrThread(0xFE, 1)

    def lambda_4651():
        OP_96(0xFE, 0x6A40, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4651)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_461D end

    def Function_19_466B(): pass

    label("Function_19_466B")


    def lambda_4670():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4670)

    def lambda_468A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_468A)
    WaitChrThread(0xFE, 1)

    def lambda_469F():
        OP_96(0xFE, 0x6A40, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_469F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_466B end

    def Function_20_46B9(): pass

    label("Function_20_46B9")


    def lambda_46BE():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46BE)

    def lambda_46D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46D8)
    WaitChrThread(0xFE, 1)

    def lambda_46ED():
        OP_95(0xFE, 28200, 0, -1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46ED)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_20_46B9 end

    def Function_21_470E(): pass

    label("Function_21_470E")


    def lambda_4713():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4713)

    def lambda_472D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_472D)
    WaitChrThread(0xFE, 1)

    def lambda_4742():
        OP_95(0xFE, 28200, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4742)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_470E end

    def Function_22_4763(): pass

    label("Function_22_4763")


    def lambda_4768():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4768)

    def lambda_4782():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4782)
    WaitChrThread(0xFE, 1)

    def lambda_4797():
        OP_95(0xFE, 29200, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4797)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_22_4763 end

    def Function_23_47B8(): pass

    label("Function_23_47B8")


    def lambda_47BD():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFE70, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47BD)

    def lambda_47D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47D7)
    WaitChrThread(0xFE, 1)

    def lambda_47EC():
        OP_95(0xFE, 29200, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47EC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_23_47B8 end

    def Function_24_480D(): pass

    label("Function_24_480D")

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
            "#5P#02306FYaaaawn...!\x02\x03",
            "#02301FHuh, what time is it...?\x02\x03",
            "#02305F...Wait, it's already\x01",
            "morning!?\x02",
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
            "#5P#02306F*sigh*... I'm really\x01",
            "hungry.\x02\x03",
            "#02300FHmm, when did that pizza\x01",
            "shop open again?\x02",
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
            "#6P#02302FI think they said they\x01",
            "were testing an orbal\x01",
            "net service...\x02\x03",
            "#02309FHehe, let me just\x01",
            "check...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#6P#02305FWhat...?\x02\x03",
            "#02301F...What's this? Some\x01",
            "garbage data...\x02",
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
            "#6P#02310F...A structure...? No,\x01",
            "more importantly, it's\x01",
            "way too...\x02\x03",
            "#02305F...............\x02",
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
        "What the heck is this?\x02",
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

    # Function_24_480D end

    def Function_25_4CB6(): pass

    label("Function_25_4CB6")

    Sleep(2200)

    label("loc_4CB9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CD2")
    Sound(836, 0, 50, 0)
    Sleep(700)
    Jump("loc_4CB9")

    label("loc_4CD2")

    Return()

    # Function_25_4CB6 end

    def Function_26_4CD3(): pass

    label("Function_26_4CD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CEB")
    OP_A1(0xFE, 0x5DC, 0x2, 0x3, 0x4)
    Jump("Function_26_4CD3")

    label("loc_4CEB")

    Return()

    # Function_26_4CD3 end

    def Function_27_4CEC(): pass

    label("Function_27_4CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D03")
    OP_A1(0xFE, 0x7D0, 0x2, 0x2, 0x3)
    Jump("Function_27_4CEC")

    label("loc_4D03")

    Return()

    # Function_27_4CEC end

    def Function_28_4D04(): pass

    label("Function_28_4D04")

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

    label("loc_4D94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DAC")
    OP_A1(0xFE, 0x9C4, 0x2, 0x5, 0x6)
    Jump("loc_4D94")

    label("loc_4DAC")

    Return()

    # Function_28_4D04 end

    def Function_29_4DAD(): pass

    label("Function_29_4DAD")

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
            "#6P#02307FT-The heck is this!?\x02\x03",
            "#02310FConverted orbal energy\x01",
            "is flowing into Orchis\x01",
            "Tower!?\x02",
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

    # Function_29_4DAD end

    def Function_30_4F1F(): pass

    label("Function_30_4F1F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00005FWhoops, this leads back\x01",
            "to where we came from.\x02\x03",
            "#00000FSince we're here, let's\x01",
            "return to the surface\x01",
            "using the direct lift.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8310, -10, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_30_4F1F end

    SaveToFile()

Try(main)
