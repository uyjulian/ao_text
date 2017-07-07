from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1020.bin",                # FileName
        "t1020",                    # MapName
        "t1020",                    # Location
        0x0095,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1020",                  # 0
        "Elise",               # 1
        "tourist",                 # 2
        "tourist",                 # 3
        "tourist",                 # 4
        "tourist",                 # 5
        "tourist",                 # 6
        "Southwark",               # 7
        "Janetta",             # 8
        "A hunter",                   # 9
        "A hunter",                   # 10
        "A hunter",                   # 11
        "A hunter",                   # 12
        "Military dog",                 # 13
        "Military dog",                 # 14
        "Military dog",                 # 15
        "Military dog",                 # 16
        "Keya",                 # 17
        "Franc",                 # 18
        "Cecil",                 # 19
        "Ilia",                 # 20
        "Lisha",               # 21
        "Shuri",                 # 22
        "Marybele",             # 23
        "SE control",                 # 24
        "bt1020",                 # 25
    ))

    ATBonus("ATBonus_504", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_5C4", 7, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 9, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 5, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 11, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_5E4", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42001.dat", "ms42001.dat", "ms41902.dat", "ms41902.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_5A4", "ed7540", "ed7453", "ATBonus_504"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51706.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch33200.itc",                   # 02
        "chr/ch21600.itc",                   # 03
        "chr/ch20100.itc",                   # 04
        "chr/ch34300.itc",                   # 05
        "chr/ch34302.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch26702.itc",                   # 08
        "chr/ch22000.itc",                   # 09
        "chr/ch26600.itc",                   # 0A
    ))

    DeclNpc(4294942387, 0,       5570,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(98650,   0,       2349,    315,  389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       500,     0,    385,  0x0, 0,   4,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(96000,   100,     20399,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(100000,  0,       21000,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(96000,   100,     19600,   90,   453,  0x0, 0,   8,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(98349,   0,       2000,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(99000,   0,       2700,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  7.5,                   8.5,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.5,                  -0.8500000238418579,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 46,  100.16000366210938,    23.280000686645508,    -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -10.016000747680664,   -7.760000228881836,    0.20000000298023224,   1.0])

    DeclActor(4294938256, 0,       8010,    1200,    4294938256, 1500,    8010,    0x007C, 0,  42, 0x0000)
    DeclActor(28550,   0,       7990,    1200,    28550,   1500,    7990,    0x007C, 0,  43, 0x0000)
    DeclActor(96820,   0,       4294967266, 1200,    96820,   1500,    4294967266, 0x007C, 0,  44, 0x0000)
    DeclActor(4294948296, 0,       11820,   1200,    4294948296, 1500,    11820,   0x007C, 0,  44, 0x0000)
    DeclActor(19000,   0,       11760,   1200,    19000,   1500,    11760,   0x007C, 0,  44, 0x0000)

    ChipFrameInfo(1768, 0)                                       # 0

    ScpFunction((
        "Function_0_6E8",          # 00, 0
        "Function_1_7A0",          # 01, 1
        "Function_2_7CB",          # 02, 2
        "Function_3_937",          # 03, 3
        "Function_4_AEC",          # 04, 4
        "Function_5_E4E",          # 05, 5
        "Function_6_F08",          # 06, 6
        "Function_7_10CF",         # 07, 7
        "Function_8_12C8",         # 08, 8
        "Function_9_1380",         # 09, 9
        "Function_10_148E",        # 0A, 10
        "Function_11_1561",        # 0B, 11
        "Function_12_16A5",        # 0C, 12
        "Function_13_1766",        # 0D, 13
        "Function_14_1A16",        # 0E, 14
        "Function_15_1A55",        # 0F, 15
        "Function_16_1A94",        # 10, 16
        "Function_17_1AD3",        # 11, 17
        "Function_18_1B12",        # 12, 18
        "Function_19_1B51",        # 13, 19
        "Function_20_1B90",        # 14, 20
        "Function_21_1BCF",        # 15, 21
        "Function_22_1C31",        # 16, 22
        "Function_23_1C93",        # 17, 23
        "Function_24_1CF5",        # 18, 24
        "Function_25_1D57",        # 19, 25
        "Function_26_1DB9",        # 1A, 26
        "Function_27_1E1B",        # 1B, 27
        "Function_28_258A",        # 1C, 28
        "Function_29_25A9",        # 1D, 29
        "Function_30_25C8",        # 1E, 30
        "Function_31_25E0",        # 1F, 31
        "Function_32_25F8",        # 20, 32
        "Function_33_2621",        # 21, 33
        "Function_34_2635",        # 22, 34
        "Function_35_265E",        # 23, 35
        "Function_36_272B",        # 24, 36
        "Function_37_274E",        # 25, 37
        "Function_38_2A14",        # 26, 38
        "Function_39_2A30",        # 27, 39
        "Function_40_2A4C",        # 28, 40
        "Function_41_2A68",        # 29, 41
        "Function_42_2B47",        # 2A, 42
        "Function_43_2BA5",        # 2B, 43
        "Function_44_2C0A",        # 2C, 44
        "Function_45_2CC0",        # 2D, 45
        "Function_46_2DAE",        # 2E, 46
        "Function_47_2E58",        # 2F, 47
    ))


    def Function_0_6E8(): pass

    label("Function_0_6E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_728"),
        (1, "loc_734"),
        (2, "loc_740"),
        (3, "loc_74C"),
        (4, "loc_758"),
        (5, "loc_764"),
        (6, "loc_770"),
        (SWITCH_DEFAULT, "loc_77C"),
    )


    label("loc_728")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_734")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_740")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_74C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_758")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_764")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_770")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_77C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_788")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_79F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_788")

    label("loc_79F")

    Return()

    # Function_0_6E8 end

    def Function_1_7A0(): pass

    label("Function_1_7A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CA")
    OP_94(0xFE, 0xFFFFF542, 0x60E, 0xABE, 0xFFFFFE3E, 0x3E8)
    Sleep(300)
    Jump("Function_1_7A0")

    label("loc_7CA")

    Return()

    # Function_1_7A0 end

    def Function_2_7CB(): pass

    label("Function_2_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_7DE")
    SetChrFlags(0x8, 0x80)
    Jump("loc_905")

    label("loc_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_7EC")
    Jump("loc_905")

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7FA")
    Jump("loc_905")

    label("loc_7FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_808")
    Jump("loc_905")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_863")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_905")

    label("loc_863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8C0")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BB")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_8BB")

    Jump("loc_905")

    label("loc_8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_8CE")
    Jump("loc_905")

    label("loc_8CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8FC")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 26870, 0, 10210, 180)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_905")

    label("loc_8FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_905")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_919")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)
    Jump("loc_936")

    label("loc_919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_936")
    ClearScenarioFlags(0x22, 1)
    SetChrPos(0x0, 28500, 0, 8080, 270)

    label("loc_936")

    Return()

    # Function_2_7CB end

    def Function_3_937(): pass

    label("Function_3_937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_949")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_949")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_961")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_974")
    OP_1B(0x5, 0x0, 0x2D)

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A0")
    OP_1B(0x1, 0x0, 0x26)
    OP_1B(0x6, 0x0, 0x27)
    OP_1B(0x9, 0x0, 0x28)
    Jump("loc_9AA")

    label("loc_9A0")

    OP_1B(0x6, 0x0, 0x27)
    OP_1B(0x9, 0x0, 0x28)

    label("loc_9AA")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_A24")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_A0C")
    SetMapObjFlags(0x6, 0x4)
    OP_65(0x1, 0x1)

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A24")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)

    label("loc_A24")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A41")
    ModifyEventFlags(1, 1, 0x80)
    OP_1B(0x0, 0x0, 0x2F)

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A52")
    Call(0, 35)

    label("loc_A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA1")
    SoundDistance(0x6E, 0x16382, 0x0, 0x6CC0, 0x11170, 0xC350, 0x64, 0x0)
    Jump("loc_AEB")

    label("loc_AA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEB")
    Sound(110, 1, 10, 0)

    label("loc_AEB")

    Return()

    # Function_3_937 end

    def Function_4_AEC(): pass

    label("Function_4_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B03")
    Call(0, 37)
    Return()

    label("loc_B03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B14")
    Jump("loc_E4A")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA")

    ChrTalk(
        0x8,
        (
            "There is a membership jewelry shop there\x01",
            "I often go there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "いつもはtouristも入ってこない\x01",
            "It is my favorite in a quiet place ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today is somewhat better than usual\x01",
            "I guess there are many people, I wonder if I should try it later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C62")

    label("loc_BEA")


    ChrTalk(
        0x8,
        (
            "There is a membership jewelry shop there\x01",
            "I often go there ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today is somewhat better than usual\x01",
            "I guess there are many people, I wonder if I should try it later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62")

    Jump("loc_E4A")

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7F")
    Jump("loc_CF5")

    label("loc_C7F")


    ChrTalk(
        0x8,
        (
            "If you are a girl the day ago\x01",
            "It seems like I went to the villa area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was a very lovely girl ….\x01",
            "I wonder if it is a senior daughter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF5")

    Jump("loc_E4A")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")

    ChrTalk(
        0x8,
        (
            "In the villa ground this far\x01",
            "There is a mansion of my master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When work is off, so\x01",
            "It comes to a vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Unlike the noisy crossbell city\x01",
            "It's a very calming place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E4A")

    label("loc_DD0")


    ChrTalk(
        0x8,
        (
            "私はIn the villa ground this far\x01",
            "It is often visited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Unlike the noisy crossbell city\x01",
            "It's a very calming place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A")

    TalkEnd(0xFE)
    Return()

    # Function_4_AEC end

    def Function_5_E4E(): pass

    label("Function_5_E4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E5F")
    Jump("loc_F04")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_E6D")
    Jump("loc_F04")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_E7B")
    Jump("loc_F04")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F04")

    ChrTalk(
        0x9,
        (
            "Ho, everyone seems delicious.\x01",
            "I'm going to have lunch here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I came to the Michelin with great pains,\x01",
            "Lavish luxury as much as a meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F04")

    TalkEnd(0xFE)
    Return()

    # Function_5_E4E end

    def Function_6_F08(): pass

    label("Function_6_F08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F19")
    Jump("loc_10CB")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_FA8")

    ChrTalk(
        0xA,
        (
            "Michelam is,\x01",
            "There are so many places to go around\x01",
            "It is a wonderful thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hehe, somehow feeling\x01",
            "I feel like I am getting young.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CB")

    label("loc_FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104B")

    ChrTalk(
        0xA,
        "Okay, girls?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Speaking of Arcade\x01",
            "Like I saw him walking alone ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do not know the destination in detail.\x01",
            "Sorry, hey.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10BD")

    label("loc_104B")


    ChrTalk(
        0xA,
        (
            "Girls arcade\x01",
            "Like I saw him walking alone ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I do not know the destination in detail.\x01",
            "Sorry, hey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BD")

    Jump("loc_10CB")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_10CB")

    label("loc_10CB")

    TalkEnd(0xFE)
    Return()

    # Function_6_F08 end

    def Function_7_10CF(): pass

    label("Function_7_10CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10E0")
    Jump("loc_12C4")

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_115A")

    ChrTalk(
        0xB,
        (
            "Oh, hey.\x01",
            "What are you doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm still looking forward to it.\x01",
            "Hey, let's do it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C4")

    label("loc_115A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1243")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(
        0xB,
        (
            "Eh, a green hair girl\x01",
            "Did not I go through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I guess I have not seen it.\x01",
            "Even if it comes with families it passes well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_123E")

    label("loc_11EB")


    ChrTalk(
        0xB,
        (
            "I'm sorry but green hair\x01",
            "I have not seen a girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Why do not you look for other places?\x02",
    )

    CloseMessageWindow()

    label("loc_123E")

    Jump("loc_12C4")

    label("loc_1243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_12C4")

    ChrTalk(
        0xB,
        (
            "Today in the morning,\x01",
            "Lake beach is a charter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm jealous,\x01",
            "I would like to spend time relaxing with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C4")

    TalkEnd(0xFE)
    Return()

    # Function_7_10CF end

    def Function_8_12C8(): pass

    label("Function_8_12C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_12D9")
    Jump("loc_137C")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_12E7")
    Jump("loc_137C")

    label("loc_12E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12F5")
    Jump("loc_137C")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_137C")

    ChrTalk(
        0xC,
        (
            "To say Michelam,\x01",
            "After all I hope to play at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The entrance fee is good,\x01",
            "I think its value is absolute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137C")

    TalkEnd(0xFE)
    Return()

    # Function_8_12C8 end

    def Function_9_1380(): pass

    label("Function_9_1380")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1391")
    Jump("loc_148A")

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(
        0xD,
        (
            "In the morning's theme park play\x01",
            "I'm tired …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please let me sleep for a moment.\x01",
            "Mumboppy …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148A")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1481")

    ChrTalk(
        0xD,
        (
            "All morning with her\x01",
            "Walking around the theme park,\x01",
            "I am completely tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I feel like taking a nap.\x02",
    )

    CloseMessageWindow()
    Jump("loc_148A")

    label("loc_1481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_148A")

    label("loc_148A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1380 end

    def Function_10_148E(): pass

    label("Function_10_148E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_149F")
    Jump("loc_155D")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BA")
    Call(0, 11)
    Jump("loc_154F")

    label("loc_14BA")


    ChrTalk(
        0xE,
        (
            "最近、Janettaちゃんが\x01",
            "Because I fell down on mismatch\x01",
            "I tried inviting my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, consult a store person\x01",
            "I have to get ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154F")

    Jump("loc_155D")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_155D")

    label("loc_155D")

    TalkEnd(0xFE)
    Return()

    # Function_10_148E end

    def Function_11_1561(): pass

    label("Function_11_1561")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        (
            "それじゃあJanettaちゃん、\x01",
            "Shall we eat here tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I read it in a magazine,\x01",
            "It seems pretty tasty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Well, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Huhu, I will expect it ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "… … That's right, I have a bit of business\x01",
            "Janettaちゃんは他のお店でも\x01",
            "I wonder if you can see it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Is it? Well, that's fine ~.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_11_1561 end

    def Function_12_16A5(): pass

    label("Function_12_16A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_16B6")
    Jump("loc_1762")

    label("loc_16B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D1")
    Call(0, 11)
    Jump("loc_1754")

    label("loc_16D1")


    ChrTalk(
        0xF,
        (
            "By a water bus a while ago\x01",
            "I have just arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "今日はSouthwarkさんが\x01",
            "It is said that they will write to us,\x01",
            "I am enjoying it very much!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1754")

    Jump("loc_1762")

    label("loc_1759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1762")

    label("loc_1762")

    TalkEnd(0xFE)
    Return()

    # Function_12_16A5 end

    def Function_13_1766(): pass

    label("Function_13_1766")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x20)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0x18, 0, 0, 0, 0)
    SetChrPos(0x19, 0, 0, 0, 0)
    SetChrPos(0x1B, 0, 0, 0, 0)
    SetChrPos(0x1A, 0, 0, 0, 0)
    SetChrPos(0x1C, 0, 0, 0, 0)
    SetChrPos(0x1D, 0, 0, 0, 0)
    SetChrPos(0x1E, 0, 0, 0, 0)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x1C, 0x4)
    ClearChrFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x4)
    OP_68(0, 2400, 0, 0)
    MoveCamera(325, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    Sound(107, 0, 100, 0)
    Sleep(300)
    FadeToBright(1000, 0)
    MoveCamera(325, 12, 0, 7000)
    BeginChrThread(0x1E, 3, 0, 14)
    BeginChrThread(0x1B, 3, 0, 15)
    BeginChrThread(0x1A, 3, 0, 16)
    BeginChrThread(0x19, 3, 0, 17)
    BeginChrThread(0x1C, 3, 0, 19)
    BeginChrThread(0x1D, 3, 0, 20)
    BeginChrThread(0x18, 3, 0, 21)
    BeginChrThread(0x102, 3, 0, 22)
    BeginChrThread(0x103, 3, 0, 23)
    BeginChrThread(0x109, 3, 0, 18)
    BeginChrThread(0x105, 3, 0, 26)
    BeginChrThread(0x101, 3, 0, 24)
    BeginChrThread(0x104, 3, 0, 25)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x3)
    SetScenarioFlags(0x22, 0)
    NewScene("t1050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1766 end

    def Function_14_1A16(): pass

    label("Function_14_1A16")

    SetChrPos(0xFE, 0, 0, 1000, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_14_1A16 end

    def Function_15_1A55(): pass

    label("Function_15_1A55")

    SetChrPos(0xFE, -700, 0, -500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_15_1A55 end

    def Function_16_1A94(): pass

    label("Function_16_1A94")

    SetChrPos(0xFE, 700, 0, -500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_16_1A94 end

    def Function_17_1AD3(): pass

    label("Function_17_1AD3")

    SetChrPos(0xFE, -700, 0, -2000, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_17_1AD3 end

    def Function_18_1B12(): pass

    label("Function_18_1B12")

    SetChrPos(0xFE, 700, 0, -2000, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_18_1B12 end

    def Function_19_1B51(): pass

    label("Function_19_1B51")

    SetChrPos(0xFE, -700, 0, -3500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_19_1B51 end

    def Function_20_1B90(): pass

    label("Function_20_1B90")

    SetChrPos(0xFE, 700, 0, -3500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_20_1B90 end

    def Function_21_1BCF(): pass

    label("Function_21_1BCF")

    SetChrPos(0xFE, 0, 0, -5000, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1BF0():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BF0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_21_1BCF end

    def Function_22_1C31(): pass

    label("Function_22_1C31")

    SetChrPos(0xFE, -700, 0, -6500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C52():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C52)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_22_1C31 end

    def Function_23_1C93(): pass

    label("Function_23_1C93")

    SetChrPos(0xFE, 700, 0, -6500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1CB4():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CB4)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_23_1C93 end

    def Function_24_1CF5(): pass

    label("Function_24_1CF5")

    SetChrPos(0xFE, 0, 0, -8000, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D16():
        OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D16)
    Sleep(1500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_24_1CF5 end

    def Function_25_1D57(): pass

    label("Function_25_1D57")

    SetChrPos(0xFE, -700, 0, -9500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D78():
        OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D78)
    Sleep(2000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_25_1D57 end

    def Function_26_1DB9(): pass

    label("Function_26_1DB9")

    SetChrPos(0xFE, 700, 0, -9500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DDA():
        OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DDA)
    Sleep(2000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_26_1DB9 end

    def Function_27_1E1B(): pass

    label("Function_27_1E1B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch41950.itc", 0x24)
    LoadChrToIndex("chr/ch41951.itc", 0x25)
    LoadChrToIndex("chr/ch41952.itc", 0x26)
    LoadChrToIndex("chr/ch42050.itc", 0x27)
    LoadChrToIndex("chr/ch42051.itc", 0x28)
    LoadChrToIndex("monster/ch82050.itc", 0x29)
    LoadChrToIndex("monster/ch82051.itc", 0x2A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 10000, 0, 7400, 270)
    SetChrPos(0x104, 10000, 0, 8600, 270)
    SetChrPos(0x103, 11500, 0, 7400, 270)
    SetChrPos(0x105, 11500, 0, 8600, 270)
    SetChrPos(0x109, 11100, 0, 6400, 270)
    SetChrPos(0x106, 10550, 0, 9600, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x10, 0x28)
    SetChrChipByIndex(0x11, 0x28)
    SetChrChipByIndex(0x12, 0x25)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x14, 0x2A)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrChipByIndex(0x16, 0x2A)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 29)
    BeginChrThread(0x15, 0, 0, 29)
    BeginChrThread(0x16, 0, 0, 29)
    BeginChrThread(0x17, 0, 0, 29)
    SetChrPos(0x10, -15000, 0, 8700, 90)
    SetChrPos(0x11, -15000, 0, 7300, 90)
    SetChrPos(0x12, -16000, 0, 10000, 90)
    SetChrPos(0x13, -16000, 0, 6000, 90)
    SetChrPos(0x14, -18500, 0, 9000, 90)
    SetChrPos(0x15, -18500, 0, 7000, 90)
    SetChrPos(0x16, -21500, 0, 10000, 90)
    SetChrPos(0x17, -21500, 0, 6000, 90)
    OP_68(8000, 1300, 8000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(6000, 1300, 8000, 2500)

    def lambda_20C0():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20C0)
    Sleep(50)

    def lambda_20D8():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_20D8)
    Sleep(50)

    def lambda_20F0():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_20F0)
    Sleep(50)

    def lambda_2108():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2108)
    Sleep(50)

    def lambda_2120():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2120)
    Sleep(50)

    def lambda_2138():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2138)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x10,
        "Voice of a man",
        "You guys …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 31)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 31)
    Sleep(50)
    BeginChrThread(0x14, 3, 0, 32)
    BeginChrThread(0x1F, 1, 0, 36)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x15, 3, 0, 32)
    BeginChrThread(0x13, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x16, 3, 0, 32)
    Sleep(50)
    BeginChrThread(0x17, 3, 0, 32)
    Fade(1000)
    OP_68(-10000, 1300, 8000, 0)
    OP_68(4000, 1300, 8000, 3500)
    MoveCamera(315, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 50, 0)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    EndChrThread(0x1F, 0x1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x10,
        "#5PCaptain Randolph … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PDamn\x01",
            "Is the person of the ceremonial sun? Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(250)

    ChrTalk(
        0x104,
        "#00312F#12PWell, that kind of thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PIt's bad, but let's get through!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12P#NAnd Zeit is\x01",
            "It is not a gift.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10,
        "#5PCut … … please!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x11,
        "#5PGet it all out!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13000, 500)
    SetChrChipByIndex(0x10, 0x28)
    BeginChrThread(0x10, 3, 0, 33)
    Sleep(10)
    BeginChrThread(0x14, 3, 0, 34)
    SetChrChipByIndex(0x11, 0x28)
    BeginChrThread(0x11, 3, 0, 33)
    Sleep(10)
    BeginChrThread(0x15, 3, 0, 34)
    SetChrChipByIndex(0x12, 0x25)
    BeginChrThread(0x12, 3, 0, 33)
    Sleep(10)
    BeginChrThread(0x16, 3, 0, 34)
    SetChrChipByIndex(0x13, 0x25)
    BeginChrThread(0x13, 3, 0, 33)
    Sleep(10)
    BeginChrThread(0x17, 3, 0, 34)
    Sleep(60)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(250)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x15, 0x3)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    Battle("BattleInfo_5E4", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    Call(0, 35)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x0, 7500, 0, 8000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 6)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_1E1B end

    def Function_28_258A(): pass

    label("Function_28_258A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25A8")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_28_258A")

    label("loc_25A8")

    Return()

    # Function_28_258A end

    def Function_29_25A9(): pass

    label("Function_29_25A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25C7")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_29_25A9")

    label("loc_25C7")

    Return()

    # Function_29_25A9 end

    def Function_30_25C8(): pass

    label("Function_30_25C8")

    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_25C8 end

    def Function_31_25E0(): pass

    label("Function_31_25E0")

    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_25E0 end

    def Function_32_25F8(): pass

    label("Function_32_25F8")

    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 28)
    Return()

    # Function_32_25F8 end

    def Function_33_2621(): pass

    label("Function_33_2621")

    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
    Return()

    # Function_33_2621 end

    def Function_34_2635(): pass

    label("Function_34_2635")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 29)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
    Return()

    # Function_34_2635 end

    def Function_35_265E(): pass

    label("Function_35_265E")

    SetChrChipByIndex(0x10, 0x0)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, 2600, 0, 7500, 0)
    SetChrChipByIndex(0x11, 0x0)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x1)
    SetChrPos(0x11, 650, 0, 10150, 45)
    SetChrChipByIndex(0x12, 0x0)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x1)
    SetChrPos(0x12, -2280, 0, 6930, 90)
    SetChrChipByIndex(0x13, 0x0)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x13, 0x1)
    SetChrPos(0x13, 350, 0, 4200, 135)
    Return()

    # Function_35_265E end

    def Function_36_272B(): pass

    label("Function_36_272B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_274D")
    Sound(845, 0, 70, 0)
    Sleep(150)
    Sound(845, 0, 70, 0)
    Sleep(400)
    Jump("Function_36_272B")

    label("loc_274D")

    Return()

    # Function_36_272B end

    def Function_37_274E(): pass

    label("Function_37_274E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-23640, 1700, 5050, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16390, 0)
    SetChrPos(0x101, -24950, 0, 7130, 180)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#6PWell, child earlier ……\x01",
            "Somehow I was not energetic\x01",
            "I wonder if it is OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Maybe … …)\x02\x03",
            "#00000FExcuse me.\x01",
            "Maybe the child,\x01",
            "With green hair girls?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#6PWell, yes, but … …\x01",
            "Are you, a guardian of that child or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, that's right.\x02\x03",
            "#00003FIf I take my eyes off a bit\x01",
            "It's gone now … ….\x01",
            "Do you know where you went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes, just past here\x01",
            "I walked to the villa area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWhile dazzling,\x01",
            "I was walking with the tea ceremony but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F（Keya、何かあったのか……？）\x02\x03",
            "#00003F(Villa Regional Surface ……\x01",
            "Why do not you go for a moment. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_1B(0x1, 0xFF, 0xFFFF)
    SetScenarioFlags(0x15A, 6)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x5A, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24950, 0, 7130, 180)
    EventEnd(0x5)
    Return()

    # Function_37_274E end

    def Function_38_2A14(): pass

    label("Function_38_2A14")

    EventBegin(0x1)
    Call(0, 41)
    Sleep(50)
    SetChrPos(0x0, -28690, 0, 8260, 90)
    EventEnd(0x4)
    Return()

    # Function_38_2A14 end

    def Function_39_2A30(): pass

    label("Function_39_2A30")

    EventBegin(0x1)
    Call(0, 41)
    Sleep(50)
    SetChrPos(0x0, 28500, 0, 8080, 270)
    EventEnd(0x4)
    Return()

    # Function_39_2A30 end

    def Function_40_2A4C(): pass

    label("Function_40_2A4C")

    EventBegin(0x1)
    Call(0, 41)
    Sleep(50)
    SetChrPos(0x0, 100130, 0, 23700, 180)
    EventEnd(0x4)
    Return()

    # Function_40_2A4C end

    def Function_41_2A68(): pass

    label("Function_41_2A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEE")

    ChrTalk(
        0x101,
        (
            "#00000FKeyaはそんな遠くへは\x01",
            "I think that I have not gone ……\x02\x03",
            "Someone may be watching.\x01",
            "I guess I'll try to listen a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B46")

    label("loc_2AEE")


    ChrTalk(
        0x101,
        (
            "#00000FKeyaは別荘地方面に\x01",
            "It was a story about going.\x02\x03",
            "…… Do you go looking for something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B46")

    Return()

    # Function_41_2A68 end

    def Function_42_2B47(): pass

    label("Function_42_2B47")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "The villa regional side seems to be blockade.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_42_2B47 end

    def Function_43_2BA5(): pass

    label("Function_43_2BA5")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "It seems that the direction to Lake beach is blocked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_43_2BA5 end

    def Function_44_2C0A(): pass

    label("Function_44_2C0A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C51")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2CB4")

    label("loc_2C51")

    Sound(807, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "It is locked.\x01",
            "It seems that business is currently suspended.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_2CB4")

    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_44_2C0A end

    def Function_45_2CC0(): pass

    label("Function_45_2CC0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F(I can not take the time ……\x01",
            "Here it seems to be a little rest. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Have a little rest\x01",      # 0
            "quit\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D54"),
        (SWITCH_DEFAULT, "loc_2D89"),
    )


    label("loc_2D54")

    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_2D97")

    label("loc_2D89")

    FadeToBright(300, 0)
    Jump("loc_2D97")

    label("loc_2D97")

    Sleep(50)
    SetChrPos(0x0, -5150, 0, 14030, 135)
    EventEnd(0x4)
    Return()

    # Function_45_2CC0 end

    def Function_46_2DAE(): pass

    label("Function_46_2DAE")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With the roar of Zeit\x01",
            "I hear heavy shooting sounds.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003FLet's over there over to Zeit … …\x02\x03",
            "#00001FWe are in the midst of now\x01",
            "We will head towards Guest House.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100000, 0, 19640, 180)
    EventEnd(0x4)
    Return()

    # Function_46_2DAE end

    def Function_47_2E58(): pass

    label("Function_47_2E58")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThis is a dockland … …\x01",
            "While Zeit is going through\x01",
            "Hurry up and head for guesthouse!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -2800, 1)
    EventEnd(0x4)
    Return()

    # Function_47_2E58 end

    SaveToFile()

Try(main)
