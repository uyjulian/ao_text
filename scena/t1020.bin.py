from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Elise",                  # 1
        "Tourist",                # 2
        "Tourist",                # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Southwark",              # 7
        "Jeanetta",               # 8
        "Jaeger",                 # 9
        "Jaeger",                 # 10
        "Jaeger",                 # 11
        "Jaeger",                 # 12
        "Military Dog",           # 13
        "Military Dog",           # 14
        "Military Dog",           # 15
        "Military Dog",           # 16
        "KeA",                    # 17
        "Fran",                   # 18
        "Cecil",                  # 19
        "Ilya",                   # 20
        "Rixia",                  # 21
        "Sully",                  # 22
        "Mariabell",              # 23
        "SE制御",                 # 24
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
        "Function_5_E9E",          # 05, 5
        "Function_6_F72",          # 06, 6
        "Function_7_113C",         # 07, 7
        "Function_8_1376",         # 08, 8
        "Function_9_1432",         # 09, 9
        "Function_10_1546",        # 0A, 10
        "Function_11_1641",        # 0B, 11
        "Function_12_1798",        # 0C, 12
        "Function_13_1843",        # 0D, 13
        "Function_14_1AF3",        # 0E, 14
        "Function_15_1B32",        # 0F, 15
        "Function_16_1B71",        # 10, 16
        "Function_17_1BB0",        # 11, 17
        "Function_18_1BEF",        # 12, 18
        "Function_19_1C2E",        # 13, 19
        "Function_20_1C6D",        # 14, 20
        "Function_21_1CAC",        # 15, 21
        "Function_22_1D0E",        # 16, 22
        "Function_23_1D70",        # 17, 23
        "Function_24_1DD2",        # 18, 24
        "Function_25_1E34",        # 19, 25
        "Function_26_1E96",        # 1A, 26
        "Function_27_1EF8",        # 1B, 27
        "Function_28_2687",        # 1C, 28
        "Function_29_26A6",        # 1D, 29
        "Function_30_26C5",        # 1E, 30
        "Function_31_26DD",        # 1F, 31
        "Function_32_26F5",        # 20, 32
        "Function_33_271E",        # 21, 33
        "Function_34_2732",        # 22, 34
        "Function_35_275B",        # 23, 35
        "Function_36_2828",        # 24, 36
        "Function_37_284B",        # 25, 37
        "Function_38_2B3E",        # 26, 38
        "Function_39_2B5A",        # 27, 39
        "Function_40_2B76",        # 28, 40
        "Function_41_2B92",        # 29, 41
        "Function_42_2C6E",        # 2A, 42
        "Function_43_2CDA",        # 2B, 43
        "Function_44_2D46",        # 2C, 44
        "Function_45_2DF6",        # 2D, 45
        "Function_46_2EEB",        # 2E, 46
        "Function_47_2FAB",        # 2F, 47
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
    Jump("loc_E9A")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0F")

    ChrTalk(
        0x8,
        (
            "I often go to that\x01",
            "members-only jewelry\x01",
            "store over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I like it because it's a\x01",
            "quiet place tourists\x01",
            "never visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, it seems there are more\x01",
            "people there than usual today. I\x01",
            "think I'll stop by later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CAF")

    label("loc_C0F")


    ChrTalk(
        0x8,
        (
            "I often go to that\x01",
            "members-only jewelry\x01",
            "store over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, it seems there are more\x01",
            "people there than usual today. I\x01",
            "think I'll stop by later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAF")

    Jump("loc_E9A")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCC")
    Jump("loc_D44")

    label("loc_CCC")


    ChrTalk(
        0x8,
        (
            "The little girl just now\x01",
            "headed for the\x01",
            "residential area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She was adorable... I\x01",
            "wonder whose daughter\x01",
            "she is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D44")

    Jump("loc_E9A")

    label("loc_D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1D")

    ChrTalk(
        0x8,
        (
            "My husband's mansion is\x01",
            "in the residential area\x01",
            "ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We come here on vacation\x01",
            "on his days off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a relaxing place,\x01",
            "very different from the\x01",
            "bustle of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E9A")

    label("loc_E1D")


    ChrTalk(
        0x8,
        (
            "I often visit the\x01",
            "residential area ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's a relaxing place,\x01",
            "very different from the\x01",
            "bustle of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9A")

    TalkEnd(0xFE)
    Return()

    # Function_4_AEC end

    def Function_5_E9E(): pass

    label("Function_5_E9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_EAF")
    Jump("loc_F6E")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_EBD")
    Jump("loc_F6E")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_ECB")
    Jump("loc_F6E")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F6E")

    ChrTalk(
        0x9,
        (
            "Hoho, everything looks\x01",
            "delicious. I think I'll\x01",
            "come here for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since I've come to Michelam,\x01",
            "I should at least treat\x01",
            "myself to a nice meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6E")

    TalkEnd(0xFE)
    Return()

    # Function_5_E9E end

    def Function_6_F72(): pass

    label("Function_6_F72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F83")
    Jump("loc_1138")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1000")

    ChrTalk(
        0xA,
        (
            "There are so many attractions\x01",
            "to see at Michelam that it's\x01",
            "hard to choose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, I feel young\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1138")

    label("loc_1000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_112F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")

    ChrTalk(
        0xA,
        (
            "Let me see, a little\x01",
            "girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that you mention it,\x01",
            "I think I saw one walking\x01",
            "alone at the arcade...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know where she\x01",
            "went though. Sorry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_112A")

    label("loc_10BA")


    ChrTalk(
        0xA,
        (
            "I think I saw a little\x01",
            "girl walking alone at\x01",
            "the arcade...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't know where she\x01",
            "went though. Sorry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112A")

    Jump("loc_1138")

    label("loc_112F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1138")

    label("loc_1138")

    TalkEnd(0xFE)
    Return()

    # Function_6_F72 end

    def Function_7_113C(): pass

    label("Function_7_113C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_114D")
    Jump("loc_1372")

    label("loc_114D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_11B6")

    ChrTalk(
        0xB,
        (
            "Ah, wait. Why are you\x01",
            "dozing off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The fun is just\x01",
            "starting. Come on, look\x01",
            "alive!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1372")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1269")

    ChrTalk(
        0xB,
        (
            "Huh, has a little girl\x01",
            "with green hair has\x01",
            "passed by, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm. I don't think I've\x01",
            "seen her. A lot of families\x01",
            "pass through here, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12D8")

    label("loc_1269")


    ChrTalk(
        0xB,
        (
            "I'm sorry, but I haven't\x01",
            "seen your little girl\x01",
            "with green hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Why don't you try\x01",
            "looking elsewhere?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D8")

    Jump("loc_1372")

    label("loc_12DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1372")

    ChrTalk(
        0xB,
        (
            "They say Lake Beach is\x01",
            "reserved this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "How enviable. I'd like a\x01",
            "reservation myself for a nice\x01",
            "relaxing day on the beach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1372")

    TalkEnd(0xFE)
    Return()

    # Function_7_113C end

    def Function_8_1376(): pass

    label("Function_8_1376")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1387")
    Jump("loc_142E")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1395")
    Jump("loc_142E")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13A3")
    Jump("loc_142E")

    label("loc_13A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_142E")

    ChrTalk(
        0xC,
        (
            "When you come to\x01",
            "Michelam, you have to\x01",
            "visit the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The entrance fee is a\x01",
            "bit much, but it's\x01",
            "totally worth it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142E")

    TalkEnd(0xFE)
    Return()

    # Function_8_1376 end

    def Function_9_1432(): pass

    label("Function_9_1432")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1443")
    Jump("loc_1542")

    label("loc_1443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_14BD")

    ChrTalk(
        0xD,
        (
            "I tired myself out at\x01",
            "the theme park this\x01",
            "morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let me sleep for a\x01",
            "bit... *mutter\x01",
            "mutter*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1542")

    label("loc_14BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1539")

    ChrTalk(
        0xD,
        (
            "I marched around the\x01",
            "theme park this morning\x01",
            "and tired myself out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, I'd feel like\x01",
            "taking a nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1542")

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1542")

    label("loc_1542")

    TalkEnd(0xFE)
    Return()

    # Function_9_1432 end

    def Function_10_1546(): pass

    label("Function_10_1546")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1557")
    Jump("loc_163D")

    label("loc_1557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1572")
    Call(0, 11)
    Jump("loc_162F")

    label("loc_1572")


    ChrTalk(
        0xE,
        (
            "Jeanetta didn't have a good time at a\x01",
            "party recently and is feeling down.\x01",
            "And so, I boldly invited her here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Now then, I need to\x01",
            "discuss things with the\x01",
            "employees and prepare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_162F")

    Jump("loc_163D")

    label("loc_1634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_163D")

    label("loc_163D")

    TalkEnd(0xFE)
    Return()

    # Function_10_1546 end

    def Function_11_1641(): pass

    label("Function_11_1641")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        (
            "Jeanetta, should we eat\x01",
            "here tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've only read about it\x01",
            "in a magazine, but they\x01",
            "say it's quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha. I'll be looking\x01",
            "forward to it, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...That's right. I have a little\x01",
            "business to take care of, so would\x01",
            "you like to look in the other shops?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "? Yes, alright.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_11_1641 end

    def Function_12_1798(): pass

    label("Function_12_1798")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_17A9")
    Jump("loc_183F")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C4")
    Call(0, 11)
    Jump("loc_1831")

    label("loc_17C4")


    ChrTalk(
        0xF,
        (
            "We just arrived on the\x01",
            "water bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Southwark's treating me\x01",
            "today, so I'm going to\x01",
            "have lots of fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1831")

    Jump("loc_183F")

    label("loc_1836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_183F")

    label("loc_183F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1798 end

    def Function_13_1843(): pass

    label("Function_13_1843")

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

    # Function_13_1843 end

    def Function_14_1AF3(): pass

    label("Function_14_1AF3")

    SetChrPos(0xFE, 0, 0, 1000, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_14_1AF3 end

    def Function_15_1B32(): pass

    label("Function_15_1B32")

    SetChrPos(0xFE, -700, 0, -500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_15_1B32 end

    def Function_16_1B71(): pass

    label("Function_16_1B71")

    SetChrPos(0xFE, 700, 0, -500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_16_1B71 end

    def Function_17_1BB0(): pass

    label("Function_17_1BB0")

    SetChrPos(0xFE, -700, 0, -2000, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_17_1BB0 end

    def Function_18_1BEF(): pass

    label("Function_18_1BEF")

    SetChrPos(0xFE, 700, 0, -2000, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_18_1BEF end

    def Function_19_1C2E(): pass

    label("Function_19_1C2E")

    SetChrPos(0xFE, -700, 0, -3500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_19_1C2E end

    def Function_20_1C6D(): pass

    label("Function_20_1C6D")

    SetChrPos(0xFE, 700, 0, -3500, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_20_1C6D end

    def Function_21_1CAC(): pass

    label("Function_21_1CAC")

    SetChrPos(0xFE, 0, 0, -5000, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1CCD():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CCD)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_21_1CAC end

    def Function_22_1D0E(): pass

    label("Function_22_1D0E")

    SetChrPos(0xFE, -700, 0, -6500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D2F():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D2F)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_22_1D0E end

    def Function_23_1D70(): pass

    label("Function_23_1D70")

    SetChrPos(0xFE, 700, 0, -6500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1D91():
        OP_9B(0x0, 0xFE, 0x0, 0x30D4, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D91)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_23_1D70 end

    def Function_24_1DD2(): pass

    label("Function_24_1DD2")

    SetChrPos(0xFE, 0, 0, -8000, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1DF3():
        OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DF3)
    Sleep(1500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_24_1DD2 end

    def Function_25_1E34(): pass

    label("Function_25_1E34")

    SetChrPos(0xFE, -700, 0, -9500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1E55():
        OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E55)
    Sleep(2000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_25_1E34 end

    def Function_26_1E96(): pass

    label("Function_26_1E96")

    SetChrPos(0xFE, 700, 0, -9500, 0)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1EB7():
        OP_9B(0x0, 0xFE, 0x0, 0x3C8C, 0x7D0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EB7)
    Sleep(2000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    OP_9B(0x0, 0xFE, 0xFFDD, 0x2EE0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x5DC, 0x7D0, 0x1)
    Return()

    # Function_26_1E96 end

    def Function_27_1EF8(): pass

    label("Function_27_1EF8")

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

    def lambda_219D():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_219D)
    Sleep(50)

    def lambda_21B5():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_21B5)
    Sleep(50)

    def lambda_21CD():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_21CD)
    Sleep(50)

    def lambda_21E5():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_21E5)
    Sleep(50)

    def lambda_21FD():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_21FD)
    Sleep(50)

    def lambda_2215():
        OP_9B(0x0, 0x106, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2215)
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
        "Man's Voice",
        "You...!?\x02",
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
        "#5PCaptain Randolph...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PShit... The monster was\x01",
            "a diversion!?\x02",
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
        "#00312F#12PWell, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#12PI'm sorry, but you're\x01",
            "letting us through!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#12P#NAlso, Zeit 's not a\x01",
            "monster.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10,
        "#5PDamn... Get them!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x11,
        (
            "#5PBring them down will\x01",
            "full force!!\x02",
        )
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

    # Function_27_1EF8 end

    def Function_28_2687(): pass

    label("Function_28_2687")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26A5")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_28_2687")

    label("loc_26A5")

    Return()

    # Function_28_2687 end

    def Function_29_26A6(): pass

    label("Function_29_26A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26C4")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_29_26A6")

    label("loc_26C4")

    Return()

    # Function_29_26A6 end

    def Function_30_26C5(): pass

    label("Function_30_26C5")

    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_26C5 end

    def Function_31_26DD(): pass

    label("Function_31_26DD")

    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_26DD end

    def Function_32_26F5(): pass

    label("Function_32_26F5")

    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 28)
    Return()

    # Function_32_26F5 end

    def Function_33_271E(): pass

    label("Function_33_271E")

    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
    Return()

    # Function_33_271E end

    def Function_34_2732(): pass

    label("Function_34_2732")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 29)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
    Return()

    # Function_34_2732 end

    def Function_35_275B(): pass

    label("Function_35_275B")

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

    # Function_35_275B end

    def Function_36_2828(): pass

    label("Function_36_2828")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_284A")
    Sound(845, 0, 70, 0)
    Sleep(150)
    Sound(845, 0, 70, 0)
    Sleep(400)
    Jump("Function_36_2828")

    label("loc_284A")

    Return()

    # Function_36_2828 end

    def Function_37_284B(): pass

    label("Function_37_284B")

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
            "#6PHmm. That girl just now...\x01",
            "She seemed unwell. I\x01",
            "wonder if she's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Could it be...)\x02\x03",
            "#00000FExcuse me. Could she\x01",
            "have been a little girl\x01",
            "with green hair?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#6PYes, that's right,\x01",
            "but... Are you her\x01",
            "guardian or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, that's right.\x02\x03",
            "#00003FI took my eyes off her for a\x01",
            "moment and she disappeared...\x01",
            "Do you know where she went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PYes. She passed by not\x01",
            "long ago, walking toward\x01",
            "the residential area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PShe plodded along with\x01",
            "this blank expression on\x01",
            "her face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(KeA, did something\x01",
            "happen to her...?)\x02\x03",
            "#00003F(The residential area...\x01",
            "I'll go take a look.)\x02",
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

    # Function_37_284B end

    def Function_38_2B3E(): pass

    label("Function_38_2B3E")

    EventBegin(0x1)
    Call(0, 41)
    Sleep(50)
    SetChrPos(0x0, -28690, 0, 8260, 90)
    EventEnd(0x4)
    Return()

    # Function_38_2B3E end

    def Function_39_2B5A(): pass

    label("Function_39_2B5A")

    EventBegin(0x1)
    Call(0, 41)
    Sleep(50)
    SetChrPos(0x0, 28500, 0, 8080, 270)
    EventEnd(0x4)
    Return()

    # Function_39_2B5A end

    def Function_40_2B76(): pass

    label("Function_40_2B76")

    EventBegin(0x1)
    Call(0, 41)
    Sleep(50)
    SetChrPos(0x0, 100130, 0, 23700, 180)
    EventEnd(0x4)
    Return()

    # Function_40_2B76 end

    def Function_41_2B92(): pass

    label("Function_41_2B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0D")

    ChrTalk(
        0x101,
        (
            "#00000FI don't think that KeA\x01",
            "has gone far, but...\x02\x03",
            "Someone may have seen\x01",
            "her. I'll try asking\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6D")

    label("loc_2C0D")


    ChrTalk(
        0x101,
        (
            "#00000FThat woman said KeA\x01",
            "headed to the\x01",
            "residential area, right?\x02\x03",
            "...I'll go have a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6D")

    Return()

    # Function_41_2B92 end

    def Function_42_2C6E(): pass

    label("Function_42_2C6E")

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
            "It seems the residential\x01",
            "area is not accessible.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_42_2C6E end

    def Function_43_2CDA(): pass

    label("Function_43_2CDA")

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
            "It seems the Lake Beach\x01",
            "area is not accessible.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_43_2CDA end

    def Function_44_2D46(): pass

    label("Function_44_2D46")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D88")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2DEA")

    label("loc_2D88")

    Sound(807, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "It is locked. It seems\x01",
            "they're not open right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_2DEA")

    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_44_2D46 end

    def Function_45_2DF6(): pass

    label("Function_45_2DF6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F(There's not much time,\x01",
            "but... It seems we can\x01",
            "rest a little here.)\x02",
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
            "Rest a Little\x01",      # 0
            "Cancel\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E91"),
        (SWITCH_DEFAULT, "loc_2EC6"),
    )


    label("loc_2E91")

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
    Jump("loc_2ED4")

    label("loc_2EC6")

    FadeToBright(300, 0)
    Jump("loc_2ED4")

    label("loc_2ED4")

    Sleep(50)
    SetChrPos(0x0, -5150, 0, 14030, 135)
    EventEnd(0x4)
    Return()

    # Function_45_2DF6 end

    def Function_46_2EEB(): pass

    label("Function_46_2EEB")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zeit's howls and a\x01",
            "fierce shootout can be\x01",
            "heard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003FLet's leave that to\x01",
            "Zeit...\x02\x03",
            "#00001FLet's head to the guest\x01",
            "house now while we have\x01",
            "the chance!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100000, 0, 19640, 180)
    EventEnd(0x4)
    Return()

    # Function_46_2EEB end

    def Function_47_2FAB(): pass

    label("Function_47_2FAB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThe jetty is this way... Let's\x01",
            "hurry to the guest house while\x01",
            "Zeit is making a diversion for us!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -2800, 1)
    EventEnd(0x4)
    Return()

    # Function_47_2FAB end

    SaveToFile()

Try(main)
