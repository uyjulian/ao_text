from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2500.bin",                # FileName
        "t2500",                    # MapName
        "t2500",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -25330, 0, -250, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2500",                  # 0
        "Noewee",             # 1
        "Daimon Members",           # 2
        "Garrison members",         # 3
        "Barrel member",             # 4
        "Chiluru",                 # 5
        "Yuri",                 # 6
        "Sykes",               # 7
        "Reggie",                 # 8
        "bus",                   # 9
        "train",                   # 10
        "Special support vehicle",             # 11
        "Truck",                 # 12
        "Douglas deputy command",         # 13
        "Oliver members",           # 14
        "Jack member",           # 15
        "Alexei members",         # 16
        "Minnes",               # 17
        "bt2500",                 # 18
        "bt2500",                 # 19
        "bt2500",                 # 20
        "East Crossbell Highway",       # 21
    ))

    ATBonus("ATBonus_3B0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_470", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_454", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_458", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_45C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_464", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_468", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_490", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 0, 0, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_4B0", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_470", "MonsterBattlePostion_450", "ed7451", "ed7453", "ATBonus_3B0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4F4", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_470", "MonsterBattlePostion_450", "ed7451", "ed7453", "ATBonus_3B0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_538", 0x0022, 255, 6, 45, 3, 3, 30, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms44900.dat", "ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_450", "ed7452", "ed7453", "ATBonus_3B0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31300.itc",                   # 01
        "chr/ch20500.itc",                   # 02
        "chr/ch44100.itc",                   # 03
        "chr/ch47500.itc",                   # 04
        "chr/ch23600.itc",                   # 05
        "chr/ch41400.itc",                   # 06
        "chr/ch41500.itc",                   # 07
    ))

    DeclNpc(4294944866, 0,       4730,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294945057, 0,       4294961807, 270,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(13659,   10000,   2849,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(13859,   10000,   4294964656, 90,   261,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294931747, 0,       4294963997, 270,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294928637, 0,       4294964046, 90,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294929997, 0,       4294965877, 135,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294929046, 0,       4294962527, 45,   389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294936146, 0,       27650,   1200,    4294936146, 1000,    27650,   0x007C, 0,  18, 0x0000)
    DeclActor(4294959296, 1500,    4294929796, 1200,    4294959296, 2500,    4294929796, 0x007C, 0,  4,  0x0000)
    DeclActor(4294928926, 0,       3120,    1200,    4294928926, 2000,    3120,    0x007C, 0,  17, 0x0000)
    DeclActor(4294929406, 0,       4410,    1200,    4294929406, 2000,    4410,    0x007C, 0,  17, 0x0000)
    DeclActor(4294948316, 200,     4294955576, 1200,    4294948316, 1700,    4294955576, 0x007C, 0,  36, 0x0000)

    PlaceName(-71.0, 0.0, -8.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-5.25, 0.0, -2.5, 0x0000, 0x0052, "")
    PlaceName(-30.950000762939453, 0.0, 28.100000381469727, 0x0000, 0x0055, "")

    ChipFrameInfo(1552, 0)                                       # 0

    ScpFunction((
        "Function_0_610",          # 00, 0
        "Function_1_6C8",          # 01, 1
        "Function_2_721",          # 02, 2
        "Function_3_D7D",          # 03, 3
        "Function_4_106D",         # 04, 4
        "Function_5_11BE",         # 05, 5
        "Function_6_12AE",         # 06, 6
        "Function_7_13DB",         # 07, 7
        "Function_8_142C",         # 08, 8
        "Function_9_14C0",         # 09, 9
        "Function_10_21AE",        # 0A, 10
        "Function_11_2DA5",        # 0B, 11
        "Function_12_2EC6",        # 0C, 12
        "Function_13_2FF1",        # 0D, 13
        "Function_14_3101",        # 0E, 14
        "Function_15_3210",        # 0F, 15
        "Function_16_3C98",        # 10, 16
        "Function_17_4818",        # 11, 17
        "Function_18_4B5B",        # 12, 18
        "Function_19_4BA7",        # 13, 19
        "Function_20_4D40",        # 14, 20
        "Function_21_598F",        # 15, 21
        "Function_22_599F",        # 16, 22
        "Function_23_59B2",        # 17, 23
        "Function_24_59C5",        # 18, 24
        "Function_25_59D8",        # 19, 25
        "Function_26_59EB",        # 1A, 26
        "Function_27_6204",        # 1B, 27
        "Function_28_638B",        # 1C, 28
        "Function_29_6B3F",        # 1D, 29
        "Function_30_726C",        # 1E, 30
        "Function_31_78B5",        # 1F, 31
        "Function_32_7EFA",        # 20, 32
        "Function_33_82A0",        # 21, 33
        "Function_34_85EE",        # 22, 34
        "Function_35_9627",        # 23, 35
        "Function_36_968C",        # 24, 36
    ))


    def Function_0_610(): pass

    label("Function_0_610")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_650"),
        (1, "loc_65C"),
        (2, "loc_668"),
        (3, "loc_674"),
        (4, "loc_680"),
        (5, "loc_68C"),
        (6, "loc_698"),
        (SWITCH_DEFAULT, "loc_6A4"),
    )


    label("loc_650")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_65C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_668")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_674")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_680")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_68C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_698")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_6A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_6B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_6C7")

    Return()

    # Function_0_610 end

    def Function_1_6C8(): pass

    label("Function_1_6C8")

    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x3, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)
    Jump("loc_711")

    label("loc_705")

    ClearMapObjFlags(0x2, 0x2000000)
    ClearMapObjFlags(0x3, 0x2000000)

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_720")
    ClearMapObjFlags(0x8, 0x2000000)

    label("loc_720")

    Return()

    # Function_1_6C8 end

    def Function_2_721(): pass

    label("Function_2_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_74E")
    SetChrChipByIndex(0x8, 0x6)
    SetChrChipByIndex(0x9, 0x7)
    SetChrChipByIndex(0xA, 0x6)
    SetChrChipByIndex(0xB, 0x7)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_74E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    SetScenarioFlags(0x38, 0)

    label("loc_7DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    SetScenarioFlags(0x38, 1)

    label("loc_7F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_807")
    SetScenarioFlags(0x38, 2)

    label("loc_807")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    SetScenarioFlags(0x38, 3)

    label("loc_81D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    SetScenarioFlags(0x38, 4)

    label("loc_833")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849")
    SetScenarioFlags(0x38, 5)

    label("loc_849")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85F")
    SetScenarioFlags(0x38, 6)

    label("loc_85F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")
    SetScenarioFlags(0x38, 7)

    label("loc_875")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")
    SetScenarioFlags(0x39, 0)

    label("loc_88B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A1")
    SetScenarioFlags(0x39, 1)

    label("loc_8A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B7")
    SetScenarioFlags(0x39, 2)

    label("loc_8B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD")
    SetScenarioFlags(0x39, 3)

    label("loc_8CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E3")
    SetScenarioFlags(0x39, 4)

    label("loc_8E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F9")
    SetScenarioFlags(0x39, 5)

    label("loc_8F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    SetScenarioFlags(0x39, 6)

    label("loc_90F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    SetScenarioFlags(0x39, 7)

    label("loc_925")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    SetScenarioFlags(0x3A, 0)

    label("loc_93B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
    SetScenarioFlags(0x3A, 1)

    label("loc_951")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_967")
    SetScenarioFlags(0x3A, 2)

    label("loc_967")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D")
    SetScenarioFlags(0x3A, 3)

    label("loc_97D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    SetScenarioFlags(0x3A, 4)

    label("loc_993")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    SetScenarioFlags(0x3A, 5)

    label("loc_9A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    SetScenarioFlags(0x3A, 6)

    label("loc_9BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    SetScenarioFlags(0x3A, 7)

    label("loc_9D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB")
    SetScenarioFlags(0x3B, 0)

    label("loc_9EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A01")
    SetScenarioFlags(0x3B, 1)

    label("loc_A01")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A17")
    SetScenarioFlags(0x3B, 2)

    label("loc_A17")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2D")
    SetScenarioFlags(0x3B, 3)

    label("loc_A2D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43")
    SetScenarioFlags(0x3B, 4)

    label("loc_A43")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A59")
    SetScenarioFlags(0x3B, 5)

    label("loc_A59")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F")
    SetScenarioFlags(0x3B, 6)

    label("loc_A6F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A85")
    SetScenarioFlags(0x3B, 7)

    label("loc_A85")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9B")
    SetScenarioFlags(0x3D, 5)

    label("loc_A9B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB1")
    SetScenarioFlags(0x3D, 6)

    label("loc_AB1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC7")
    SetScenarioFlags(0x3D, 7)

    label("loc_AC7")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_BF2")

    label("loc_B02")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B25")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_BF2")

    label("loc_B25")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_BF2")

    label("loc_B48")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_BF2")

    label("loc_B6B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_BF2")

    label("loc_B8E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB1")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_BF2")

    label("loc_BB1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_BF2")

    label("loc_BD4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    SetScenarioFlags(0x3C, 7)

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3A")
    SetChrPos(0x0, -38590, 0, 1950, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 8)

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_C6D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6D")
    SetChrPos(0x0, -37890, 0, 4410, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_CBB")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9D")
    Event(0, 33)
    Jump("loc_CBB")

    label("loc_C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB8")
    Event(0, 26)
    Jump("loc_CBB")

    label("loc_CB8")

    Event(0, 7)

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CCF")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_CDE")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_CDE")
    ClearScenarioFlags(0x22, 1)
    Event(0, 27)

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D02")
    Event(0, 20)
    Jump("loc_D7C")

    label("loc_D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D34")
    Event(0, 34)
    Jump("loc_D45")

    label("loc_D34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D45")
    Event(0, 32)

    label("loc_D45")

    Jump("loc_D7C")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7C")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_D7C")

    Return()

    # Function_2_721 end

    def Function_3_D7D(): pass

    label("Function_3_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D99")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DAB")

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_DAB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E2F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xE6, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E46")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_E46")

    label("loc_E46")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECA")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    Jump("loc_EF0")

    label("loc_ECA")

    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)

    label("loc_EF0")

    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1D")
    OP_70(0x5, 0x0)
    Jump("loc_F21")

    label("loc_F1D")

    OP_70(0x5, 0x1E)

    label("loc_F21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC8")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFlags(0x6, 0x1000)
    OP_78(0x6, 0x12)
    SetChrPos(0x12, -50500, 0, 0, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    SetMapObjFlags(0xB, 0x1000)
    OP_78(0xB, 0x13)
    SetChrPos(0x13, -22290, 0, -12240, 0)
    OP_D5(0x13, 0x0, 0x0, 0x0, 0x0)

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1021")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1000")
    SetMapObjFrame(0x9, "mark00", 0x0, 0x1)
    SetMapObjFrame(0xA, "mark00", 0x0, 0x1)
    Jump("loc_101C")

    label("loc_1000")

    SetMapObjFrame(0x2, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x3, "mark00", 0x0, 0x1)

    label("loc_101C")

    Jump("loc_106C")

    label("loc_1021")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1050")
    SetMapObjFrame(0x9, "mark01", 0x0, 0x1)
    SetMapObjFrame(0xA, "mark01", 0x0, 0x1)
    Jump("loc_106C")

    label("loc_1050")

    SetMapObjFrame(0x2, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x3, "mark01", 0x0, 0x1)

    label("loc_106C")

    Return()

    # Function_3_D7D end

    def Function_4_106D(): pass

    label("Function_4_106D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116D")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('弹簧跑鞋', 1)"), scpexpr(EXPR_END)), "loc_10F6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '弹簧跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1168")

    label("loc_10F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '弹簧跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '弹簧跑鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1168")

    Jump("loc_11B2")

    label("loc_116D")

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

    label("loc_11B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_106D end

    def Function_5_11BE(): pass

    label("Function_5_11BE")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Do you want to move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City East Exit\x01",      # 0
            "Almorika Village\x01",          # 1
            "Stop (three-way street)\x01",      # 2
            "quit\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1261")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12A6")

    label("loc_1261")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1286")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12A6")

    label("loc_1286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A6")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_12A6")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_5_11BE end

    def Function_6_12AE(): pass

    label("Function_6_12AE")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_13D7")
    Fade(500)
    OP_68(-27530, 1000, 24550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(24000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -32119, 0, 25500, 90)
    SetChrPos(0x1, -32119, 0, 24000, 90)
    SetChrPos(0x2, -32119, 0, 22500, 90)
    SetChrPos(0x3, -32119, 0, 21000, 90)
    ClearChrFlags(0x10, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x10)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x10, -27000, 0, 11850, 0)
    OP_D5(0x10, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_138E():
        OP_98(0xFE, 0x0, 0x0, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_138E)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x10, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_13D7")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_6_12AE end

    def Function_7_13DB(): pass

    label("Function_7_13DB")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -31260, 0, 26050, 90)
    OP_31(0x1)
    OP_68(-31260, 1000, 26050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_7_13DB end

    def Function_8_142C(): pass

    label("Function_8_142C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1487")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_147C")
    Sound(2502, 255, 100, 0)
    Jump("loc_1482")

    label("loc_147C")

    Sound(2503, 255, 100, 0)

    label("loc_1482")

    Jump("loc_14AB")

    label("loc_1487")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14A5")
    Sound(3347, 255, 100, 0)
    Jump("loc_14AB")

    label("loc_14A5")

    Sound(3348, 255, 100, 0)

    label("loc_14AB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_142C end

    def Function_9_14C0(): pass

    label("Function_9_14C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162F")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Soldier Noe",
        (
            "O, are you …?!\x01",
            "… … you also need to catch it anymore\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Noe",
        (
            "Huh, after all we our defense army\x01",
            "I wonder what I wanted to do.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Noe",
        (
            "The unprepared guard, too,\x01",
            "Finally I was proud.\x01",
            "Even though I felt like that … ….\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Noe",
        (
            "Somehow a long long dream\x01",
            "It feels like I was being shown.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16B9")

    label("loc_162F")


    NpcTalk(
        0x8,
        "Soldier Noe",
        (
            "After all, we also defense army\x01",
            "I wonder what I wanted to do.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Noe",
        (
            "Somehow a long long dream\x01",
            "It feels like I was being shown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B9")

    Jump("loc_21AA")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A8")

    ChrTalk(
        0x8,
        (
            "Members who were hospitalized at Ursula Hospital,\x01",
            "Everyone seems to be unpredictable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… Well, they are lucky.\x01",
            "Fellows who were sacrificed in the mountain path … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am mild, but ……\x01",
            "I can not suppress my anger this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1824")

    label("loc_17A8")


    ChrTalk(
        0x8,
        (
            "I am mild, but ……\x01",
            "I can not suppress my anger this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Red constellation … this borrowing is\x01",
            "Someday, I will definitely return it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1824")

    Jump("loc_21AA")

    label("loc_1829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1919")

    ChrTalk(
        0x8,
        (
            "The accident at the West crossbell road on yesterday,\x01",
            "A considerable influence was expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If restoration is not done,\x01",
            "I was putting my side into the empire and the republic\x01",
            "I guess it was not a referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I would like to send praise to the troops I restored.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19AB")

    label("loc_1919")


    ChrTalk(
        0x8,
        (
            "If the accident was not restored,\x01",
            "I was putting my side into the empire and the republic\x01",
            "I guess it was not a referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I would like to send praise to the troops I restored.\x02",
    )

    CloseMessageWindow()

    label("loc_19AB")

    Jump("loc_21AA")

    label("loc_19B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA6")

    ChrTalk(
        0x8,
        (
            "Crossbell Autonomous province,\x01",
            "Together with the Empire and the Republic\x01",
            "We pay tax revenues of 10.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By national independence\x01",
            "If the system is abolished,\x01",
            "A considerable budget will emerge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If so, the reinforcement of the guard is\x01",
            "I wonder if it will be held first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B43")

    label("loc_1AA6")


    ChrTalk(
        0x8,
        (
            "By 10 tax revenue by independence\x01",
            "If the system to be included is abolished,\x01",
            "A considerable budget will emerge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If so, the reinforcement of the guard is\x01",
            "I wonder if it will be held first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B43")

    Jump("loc_21AA")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C31")

    ChrTalk(
        0x8,
        (
            "Crossbell Autonomous province,\x01",
            "Sandwiched between the Empire and the Republic\x01",
            "It exists in the terrain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In other words, that independence advocacy\x01",
            "In the midst of opposing partners\x01",
            "It is equal to being declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking that way,\x01",
            "The mayor also dared\x01",
            "You did it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CB6")

    label("loc_1C31")


    ChrTalk(
        0x8,
        (
            "Independent advocacy at the trade meeting is\x01",
            "In the midst of opposing partners\x01",
            "It is equal to being declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, mayor has also dreamed\x01",
            "You did it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB6")

    Jump("loc_21AA")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBF")

    ChrTalk(
        0x8,
        (
            "Terrorists in the Republic\x01",
            "I enter the crossbell …\x01",
            "There seems to be information on what kind of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is not calm as being terrorism.\x01",
            "If you want to pass your argument,\x01",
            "You should consider other ways …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… Well, well, even if I say such a thing\x01",
            "There is no choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E5F")

    label("loc_1DBF")


    ChrTalk(
        0x8,
        (
            "Terrorists in the Republic\x01",
            "I enter the crossbell …\x01",
            "There seems to be information on what kind of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For terrorist acts\x01",
            "There are things I think variously … ….\x01",
            "I have to concentrate on security for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5F")

    Jump("loc_21AA")

    label("loc_1E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F30")

    ChrTalk(
        0x8,
        (
            "This morning, President of Rock Smith\x01",
            "A white limousine passes by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With greetings and traffic restrictions,\x01",
            "I was pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To enter VIP,\x01",
            "Do not forget to take care.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FBF")

    label("loc_1F30")


    ChrTalk(
        0x8,
        (
            "This morning, President of Rock Smith\x01",
            "With greetings and traffic restrictions,\x01",
            "I was pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To enter VIP,\x01",
            "Do not forget to take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBF")

    Jump("loc_21AA")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2057")

    ChrTalk(
        0x8,
        (
            "No, thanks.\x01",
            "It was a good exercise.\x01",
            "You guys are doing a lot of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is another opportunity\x01",
            "I will ask you to make a hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AA")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2125")

    ChrTalk(
        0x8,
        (
            "I newly arrived at the Tangram gate\x01",
            "Douglas deputy commander,\x01",
            "It is quite easy-going person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If dare to say,\x01",
            "I guess everyone can depend on everyone's aniki.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… … When it comes to work\x01",
            "It will be tougher as a demon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21AA")

    label("loc_2125")


    ChrTalk(
        0x8,
        (
            "Douglas deputy commander,\x01",
            "It is quite easy-going person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If dare to say,\x01",
            "I feel like everyone can depend on everyone.\x01",
            "…… It's tough on work though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AA")

    TalkEnd(0xFE)
    Return()

    # Function_9_14C0 end

    def Function_10_21AE(): pass

    label("Function_10_21AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D0")

    NpcTalk(
        0x9,
        "Soldier Dimon",
        (
            "With the advent of that pale white tree,\x01",
            "The Republican Army for now\x01",
            "It seems to be in a posture of waitress … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Dimon",
        (
            "Now that I have lost the barrier and the \"Shinto machine\"\x01",
            "It will be a bad idea.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Dimon",
        (
            "What can protect current crossbells\x01",
            "We are the only defense forces.\x01",
            "I have to watch out strictly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2394")

    label("loc_22D0")


    NpcTalk(
        0x9,
        "Soldier Dimon",
        (
            "With the advent of that pale white tree,\x01",
            "The Republican Army for now\x01",
            "It seems to be in a posture of waitress … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Dimon",
        (
            "What can protect current crossbells\x01",
            "We are the only defense forces.\x01",
            "I have to watch out strictly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2394")

    Jump("loc_2DA1")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    ChrTalk(
        0x9,
        (
            "The reason why he could not prevent the attack of Cross Bell City,\x01",
            "We are a clear blunder of the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For Mainz occupation incident\x01",
            "The strength was cut off … …\x01",
            "Such a thing does not make an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As an organization that keeps peace of mind … …\x01",
            "Maybe it should be reviewed variously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2534")

    label("loc_24A0")


    ChrTalk(
        0x9,
        (
            "The reason why he could not prevent the attack of Cross Bell City,\x01",
            "We are a clear blunder of the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As an organization that keeps peace of mind … …\x01",
            "Maybe it should be reviewed variously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2534")

    Jump("loc_2DA1")

    label("loc_2539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25C1")

    ChrTalk(
        0x9,
        (
            "Men's haste staff earlier\x01",
            "I listened to him … …\x01",
            "It seems that female freaks are missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hmm … I wish I had nothing anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_25C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2663")

    ChrTalk(
        0x9,
        (
            "Even hasty fighters,\x01",
            "Following \"Phantom Beast\" to place various places\x01",
            "It seems to be exploring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They can not get in with us\x01",
            "It is also familiar to the backyard.\x01",
            "They are dependable people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_2663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2758")

    ChrTalk(
        0x9,
        (
            "If \"Phantom Beast\" is a foreigner\x01",
            "If there is something to hurt,\x01",
            "The two major powers will surely use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Straight to the state of tension of the border\x01",
            "More than becoming involved, never the guard as well\x01",
            "It is not a problem to overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I asked for your investigation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27B1")

    label("loc_2758")


    ChrTalk(
        0x9,
        (
            "The problem of the eidolon, never the guard as well\x01",
            "It can not be overlooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I asked for your investigation.\x02",
    )

    CloseMessageWindow()

    label("loc_27B1")

    Jump("loc_2DA1")

    label("loc_27B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_284E")

    ChrTalk(
        0x9,
        (
            "Regarding terrorists,\x01",
            "We also give our all\x01",
            "I am wary of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Through the guards'\x01",
            "That invasion must necessarily\x01",
            "I should prevent it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_284E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28D7")

    ChrTalk(
        0x9,
        (
            "President Locksmith said,\x01",
            "To the Republic as an ordinary people\x01",
            "It is said to be supported.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Actually, in fact\x01",
            "I wonder who it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_299B")

    ChrTalk(
        0x9,
        (
            "Even though there is Sergeant Noel,\x01",
            "Douglas deputy commander and so far\x01",
            "To fight a good battle … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected, a leading actor of the cult,\x01",
            "Is it called a mission support section?\x01",
            "To be honest, I got impressed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_299B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C48")

    ChrTalk(
        0x9,
        (
            "Serward Noel, thanks for your hard work!\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FGood work, Daimon.\x01",
            "Well, what's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Hmm, what is that ……\x01",
            "Sergeant not wearing the uniform of the guard,\x01",
            "I thought it was fresh somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOh, that's right.\x01",
            "Wandering around the tangram gate\x01",
            "It may be the first time … ….\x02\x03",
            "#10112FI'm sorry, a bit\x01",
            "Did not you think enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No.\x01",
            "Would it be okay ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha ~ Oh, well …\x01",
            "Noel's unfamiliar appearance\x01",
            "Have you stopped?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FHeck! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, no.\x01",
            "Never for that kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … and then I was rude.\x01",
            "Please forget, sergeant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(La, Randy Senpai.\x01",
            "It's embarrassing anymore ……)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 7)
    Jump("loc_2DA1")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D24")

    ChrTalk(
        0x9,
        (
            "…… To be honest, about the difference in costume\x01",
            "I was upset.\x01",
            "I am not satisfied with training either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was very sorry.\x01",
            "Serious, please forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Such as training,\x01",
            "Is it such a problem …? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DA1")

    label("loc_2D24")


    ChrTalk(
        0x9,
        (
            "…… To be honest, about the difference in costume\x01",
            "I was upset.\x01",
            "I am not satisfied with training either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was very sorry.\x01",
            "Serious, please forget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA1")

    TalkEnd(0xFE)
    Return()

    # Function_10_21AE end

    def Function_11_2DA5(): pass

    label("Function_11_2DA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5D")

    ChrTalk(
        0xC,
        "See them at the east exit of the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Togram gate with me\x01",
            "Because I want to go\x01",
            "Even though I brought it for escorts ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "…… To be honest, it was useless.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EC2")

    label("loc_2E5D")


    ChrTalk(
        0xC,
        (
            "Anyway, walking down the road\x01",
            "It was quite thrilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I guess I should go to Almorika village as it is.\x02",
    )

    CloseMessageWindow()

    label("loc_2EC2")

    TalkEnd(0xFE)
    Return()

    # Function_11_2DA5 end

    def Function_12_2EC6(): pass

    label("Function_12_2EC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F91")

    ChrTalk(
        0xD,
        (
            "Ha Ha……\x01",
            "When you encounter a phantom beast on the way\x01",
            "I thought what would happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "… …. Anyway, I arrived.\x01",
            "I only have to go back to the Republic ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I guess you can really go home … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FED")

    label("loc_2F91")


    ChrTalk(
        0xD,
        (
            "The work to this point\x01",
            "It's my first time of birth ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, really to the Republic\x01",
            "I wonder if I can return home …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FED")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EC6 end

    def Function_13_2FF1(): pass

    label("Function_13_2FF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AB")

    ChrTalk(
        0xE,
        (
            "Wait, see you ….\x01",
            "Even in a clear safe way\x01",
            "I was just thinking that I knew … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "No way, I ordinarily take the highway\x01",
            "What is to become a marathon fellow ……\x01",
            "I thought I was going to die … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_30FD")

    label("loc_30AB")


    ChrTalk(
        0xE,
        (
            "Wow, why are we\x01",
            "In such a way ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Crossbell\x01",
            "It's already a collage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30FD")

    TalkEnd(0xFE)
    Return()

    # Function_13_2FF1 end

    def Function_14_3101(): pass

    label("Function_14_3101")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_320C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D5")

    ChrTalk(
        0xF,
        (
            "Even though the barrier could be solved a lot,\x01",
            "I can not get a car ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "To her who came by chance\x01",
            "If you let me show you,\x01",
            "To such a tough time ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Or, even after hitchhiking\x01",
            "I should have done it ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_320C")

    label("loc_31D5")


    ChrTalk(
        0xF,
        (
            "Or, even after hitchhiking\x01",
            "I should have done it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_320C")

    TalkEnd(0xFE)
    Return()

    # Function_14_3101 end

    def Function_15_3210(): pass

    label("Function_15_3210")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331D")

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "Under the direction of the deputy commander,\x01",
            "Watch out for republic\x01",
            "I will keep on ……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "Previously, the reason why I could repel the armies of the two biggest countries\x01",
            "It was only with the power of \"Shinkansen\".\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "Next time I invade again … …\x01",
            "Perhaps, there is no way to stop it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33BB")

    label("loc_331D")


    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "I was able to repel the army before\x01",
            "It was the power of the priestess machine.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "Next time the Republican Army invades … …\x01",
            "Perhaps, there is no way to stop it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BB")

    Jump("loc_3C94")

    label("loc_33C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AA")

    ChrTalk(
        0xA,
        (
            "Having suffered tremendous damage from hunting soldiers,\x01",
            "The guard has become tattered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you are told that such people can fight again,\x01",
            "To be honest, I will want to run away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From now on, we are\x01",
            "I wonder what I should do ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_352E")

    label("loc_34AA")


    ChrTalk(
        0xA,
        (
            "If you are told that you can fight again with the hunting corps,\x01",
            "To be honest, I will want to run away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From now on, we are\x01",
            "I wonder what I should do ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352E")

    Jump("loc_3C94")

    label("loc_3533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D2")

    ChrTalk(
        0xA,
        "… …. え く っ け! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "…… Hey body for a moment\x01",
            "I guess it has cooled down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if you catch a cold\x01",
            "I wonder if I'll take a break for a bit …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3643")

    label("loc_35D2")


    ChrTalk(
        0xA,
        (
            "A little body\x01",
            "It cooled down,\x01",
            "Would you like to have a dress at the cafeteria … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In this tense state,\x01",
            "Even if you lose your physical condition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3643")

    Jump("loc_3C94")

    label("loc_3648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(
        0xA,
        (
            "Now, Tangram Hills\x01",
            "Crossbell and the Republic, which territory\x01",
            "It is in an ambiguous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Currently, the Republic possesses in fact\x01",
            "It is supposed to be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Crossbell is independent,\x01",
            "What do you mean ……\x01",
            "It seems to be frustrating for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37D5")

    label("loc_3744")


    ChrTalk(
        0xA,
        (
            "Now, Tangram Hills\x01",
            "Crossbell and the Republic, which territory\x01",
            "It is in an ambiguous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if independence is realized,\x01",
            "It seems to be frustrating for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D5")

    Jump("loc_3C94")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_393B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B8")

    ChrTalk(
        0xA,
        (
            "As the day of the referendum approaches,\x01",
            "The pressure is getting stronger day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Republicans, too, for cross-border independence\x01",
            "It seems to indicate the opposite direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To less explicit exercise and policy\x01",
            "I want to pray that it will not develop.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3936")

    label("loc_38B8")


    ChrTalk(
        0xA,
        (
            "Republicans, too, for cross-border independence\x01",
            "It seems to indicate the opposite direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To less explicit exercise and policy\x01",
            "I want to pray that it will not develop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3936")

    Jump("loc_3C94")

    label("loc_393B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A33")

    ChrTalk(
        0xA,
        (
            "Tangram Hills\x01",
            "As you can see the view is nice,\x01",
            "There are facilities for surveillance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have a flying boat or car coming\x01",
            "It should be understood soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Of course, it's not a simple story, but …\x01",
            "Do not worry, terrorists\x01",
            "I will not let you put it in absolutely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AD7")

    label("loc_3A33")


    ChrTalk(
        0xA,
        (
            "Tangram Hills\x01",
            "As you can see the view is nice,\x01",
            "There are facilities for surveillance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Of course, it's not a simple story, but …\x01",
            "Do not worry, terrorists\x01",
            "I will not let you put it in absolutely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD7")

    Jump("loc_3C94")

    label("loc_3ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B7A")

    ChrTalk(
        0xA,
        (
            "President Lock Smith 's limo,\x01",
            "Be protected by a number of escort cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As expected, the president who governs the Republic … …\x01",
            "That sight was truly spectacular.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_3B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C33")

    ChrTalk(
        0xA,
        (
            "Tangram horse spreading all over … …\x01",
            "It's a very nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Historically, on the stage of conflict many times\x01",
            "It is said that it became … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I like this scenery very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C94")

    label("loc_3C33")


    ChrTalk(
        0xA,
        (
            "Tangram horse spreading all over … …\x01",
            "It's a very nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I like this scenery very much.\x02",
    )

    CloseMessageWindow()

    label("loc_3C94")

    TalkEnd(0xFE)
    Return()

    # Function_15_3210 end

    def Function_16_3C98(): pass

    label("Function_16_3C98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8B")

    NpcTalk(
        0xB,
        "Soldier barrel",
        (
            "That unfamiliar tree ……\x01",
            "Surely from the whole crossbell\x01",
            "You should be able to see it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier barrel",
        (
            "It seems that such a sudden appearance,\x01",
            "Absolutely not ordinary.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier barrel",
        (
            "Crossbell is united\x01",
            "What will happen ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E22")

    label("loc_3D8B")


    NpcTalk(
        0xB,
        "Soldier barrel",
        (
            "Unknown trees ……\x01",
            "It seems that such a sudden appearance,\x01",
            "Absolutely not ordinary.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier barrel",
        (
            "I am in the Belgard gate\x01",
            "I wonder if Broude is okay ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E22")

    Jump("loc_4814")

    label("loc_3E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1E")

    ChrTalk(
        0xB,
        (
            "I am in the Belgard gate\x01",
            "Childhood friend Brooke\x01",
            "It seems that it was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… But, I can not rest assured.\x01",
            "What the guard lost\x01",
            "After all it's a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To be honest, now\x01",
            "I'm scared of what will happen ….\x01",
            "You only have to prepare.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F97")

    label("loc_3F1E")


    ChrTalk(
        0xB,
        (
            "What the guard lost\x01",
            "As expected after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To be honest, now\x01",
            "I'm scared of what will happen ….\x01",
            "You only have to prepare.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F97")

    Jump("loc_4814")

    label("loc_3F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408B")

    ChrTalk(
        0xB,
        (
            "Radar facilities are better today\x01",
            "It seems they are working at full capacity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As it is raining,\x01",
            "It is hard to see the sky situation with visual inspection.\x01",
            "I'm pretty handy for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although it was destroyed at the time of the trade meeting,\x01",
            "It is seriously helpful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4101")

    label("loc_408B")


    ChrTalk(
        0xB,
        (
            "Radar facilities\x01",
            "I'm pretty handy for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although it was destroyed at the time of the trade meeting,\x01",
            "It is seriously helpful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4101")

    Jump("loc_4814")

    label("loc_4106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4181")

    ChrTalk(
        0xB,
        (
            "Douglas deputy commander is friendly,\x01",
            "That is pretty cool person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I wish I could be that much …\x02",
    )

    CloseMessageWindow()
    Jump("loc_4814")

    label("loc_4181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_434B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4299")

    ChrTalk(
        0xB,
        (
            "What is a phantom beast?\x01",
            "It seems like a ghost that came out in the \"Monaster of the Moon\"\x01",
            "It seems to be incomprehensible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It would be fine just to be scared of its appearance,\x01",
            "I do not know the identity itself\x01",
            "There is an eerily horror …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even though there are times when it is to be bothered,\x01",
            "I also have to try not to lose heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4346")

    label("loc_4299")


    ChrTalk(
        0xB,
        (
            "The ghosts that previously appeared in the \"Monaster of the Moon\"\x01",
            "When I go to investigate,\x01",
            "I was falling down because of millet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even if there are things to conspire with an eidolome,\x01",
            "I also have to try not to lose heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4346")

    Jump("loc_4814")

    label("loc_434B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442D")

    ChrTalk(
        0xB,
        (
            "Police information is terrorists\x01",
            "It seems that there is a high possibility of appearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "With such dangerous people\x01",
            "I do not want to get out\x01",
            "To be honest, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, the goddess of the sky.\x01",
            "How about today's day\x01",
            "I wish for peace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44C1")

    label("loc_442D")


    ChrTalk(
        0xB,
        (
            "Terrorists are dangerous people\x01",
            "I do not want to get out\x01",
            "To be honest, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, the goddess of the sky.\x01",
            "How about today's day\x01",
            "I wish for peace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44C1")

    Jump("loc_4814")

    label("loc_44C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E8")

    ChrTalk(
        0xB,
        (
            "To welcome President 's limousine,\x01",
            "To be honest, I got nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm so lucky … ….\x01",
            "Even when saluting, something poses\x01",
            "I feel like I got strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, the president is like me.\x01",
            "I guess I did not care about one soldier … …\x01",
            "Still it was a lot of pressure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_468F")

    label("loc_45E8")


    ChrTalk(
        0xB,
        (
            "I do not want the president's limousine to be picked up\x01",
            "To be honest, I got nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, the president is like me.\x01",
            "I guess I did not care about one soldier … …\x01",
            "Still it was a lot of pressure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468F")

    Jump("loc_4814")

    label("loc_4694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477D")

    ChrTalk(
        0xB,
        (
            "At the Belgard gate in the Imperial direction,\x01",
            "There is a childhood friend as Brooke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In the meantime, from him\x01",
            "Rehabilitation training is safe\x01",
            "I heard it ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No, I was worried for a while, but …\x01",
            "I was relieved that it seemed that I could completely recover.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4814")

    label("loc_477D")


    ChrTalk(
        0xB,
        (
            "In the meantime, from the childhood friend Brode\x01",
            "Rehabilitation training is safe\x01",
            "I heard it ended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No, I was worried for a while, but …\x01",
            "I was relieved that it seemed that I could completely recover.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4814")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C98 end

    def Function_17_4818(): pass

    label("Function_17_4818")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_484A")
    SetScenarioFlags(0x31, 2)

    label("loc_484A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_488A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_487F")
    Sound(2499, 255, 100, 0)
    Jump("loc_4885")

    label("loc_487F")

    Sound(3537, 255, 100, 0)

    label("loc_4885")

    Jump("loc_4890")

    label("loc_488A")

    Sound(3344, 255, 100, 0)

    label("loc_4890")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4909")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_48E9"),
        (SWITCH_DEFAULT, "loc_48FA"),
    )


    label("loc_48E9")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4904")

    label("loc_48FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4904")

    Jump("loc_4B48")

    label("loc_4909")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_493D")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_493D")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4971"),
        (1, "loc_4A75"),
        (2, "loc_4B06"),
        (SWITCH_DEFAULT, "loc_4B3E"),
    )


    label("loc_4971")

    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49A2")
    OP_70(0x6, 0x12C)
    OP_71(0x6, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_49B2")

    label("loc_49A2")

    OP_70(0x6, 0xF0)
    OP_71(0x6, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_49B2")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A08")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A08")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A2B")
    Sound(461, 0, 100, 0)

    label("loc_4A2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A4B")
    OP_70(0x6, 0x14A)
    OP_71(0x6, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4A5B")

    label("loc_4A4B")

    OP_70(0x6, 0x10E)
    OP_71(0x6, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4A5B")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x6, "light", 0x1, 0x1)
    OP_70(0x6, 0x0)
    Jump("loc_4890")

    label("loc_4A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4AE7")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4AAA")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4AC2")

    label("loc_4AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4ABD")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4AC2")

    label("loc_4ABD")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4AC2")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B01")

    label("loc_4AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4AF7")
    OP_AF(0xFB)
    Jump("loc_4B01")

    label("loc_4AF7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B01")

    Jump("loc_4B48")

    label("loc_4B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B39")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4B2F")
    OP_AF(0xFB)
    Jump("loc_4B39")

    label("loc_4B2F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B39")

    Jump("loc_4B48")

    label("loc_4B3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B48")

    Jump("loc_4890")

    label("loc_4B4D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_17_4818 end

    def Function_18_4B5B(): pass

    label("Function_18_4B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4BA3")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The guiding bus seems to be out of service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4BA3")

    Call(0, 5)
    Return()

    # Function_18_4B5B end

    def Function_19_4BA7(): pass

    label("Function_19_4BA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -45000, 0, 11000, 0)
    SetChrPos(0x109, -45000, 0, 11000, 0)
    OP_78(0x8, 0x11)
    OP_49()
    SetChrPos(0x11, 20000, -10000, -39000, 0)
    OP_D5(0x11, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0xA3, 0x6A, 0x26, 0xE6, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    OP_68(-15000, 1500, 0, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(44000, 0)
    OP_68(-20000, -6000, -30000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac19", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-20000, -7500, -39000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(18000, 0)
    OP_68(-40000, -7500, -39000, 6000)
    MoveCamera(45, 15, 0, 6000)
    SetCameraDistance(33000, 6000)
    Sound(455, 0, 100, 0)
    ClearMapObjFlags(0x8, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_4D0D():
        OP_96(0xFE, 0xFFFE2B40, 0xFFFFD8F0, 0xFFFF67A8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4D0D)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_4BA7 end

    def Function_20_4D40(): pass

    label("Function_20_4D40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -18420, 0, 290, 270)
    SetChrPos(0x102, -17710, 0, -820, 270)
    SetChrPos(0x104, -17010, 0, 1050, 270)
    SetChrPos(0x109, -15460, 0, 420, 270)
    SetChrPos(0x105, -15120, 0, -1000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-16000, 1000, 0, 0)
    MoveCamera(34, 33, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(-28490, 1000, 340, 6000)
    BeginChrThread(0x101, 0, 0, 21)
    BeginChrThread(0x102, 0, 0, 22)
    BeginChrThread(0x104, 0, 0, 23)
    BeginChrThread(0x105, 0, 0, 24)
    BeginChrThread(0x109, 0, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4500)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#5POops ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_4EB2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4EB2)

    ChrTalk(
        0x102,
        "#00105F#12PDo you contact other departments?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F#30WYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sturdy voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhufu ….\x01",
            "You, my friend.\x02\x03",
            "I wonder who they are?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012FMr. Michelle ……\x01",
            "Well, what is wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhufu, I do not understand it with a single shot\x01",
            "You are quite clear.\x02\x03",
            "Or maybe you can make a love?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FNo, except Mr. Michelle\x01",
            "Just because the corresponding person did not think of it.\x02\x03",
            "#00000FI'm guessing that.\x01",
            "Do you mean Kea?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, that's it.\x02\x03",
            "With that child, Shizuku-chan\x01",
            "I went to play in the port area.\x02\x03",
            "I wonder if it was a zeitge?\x01",
            "Because that police dog was together\x01",
            "I think it's all right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FOh, if Zeit is with you\x01",
            "I do not need any worries.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, after all?\x02\x03",
            "I was listening to the story,\x01",
            "There are tremendous dignity everywhere.\x02\x03",
            "Truly a legendary \"god of war\"\x01",
            "There is nothing left to be told.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004FHa ha …… Truly a legendary wolf\x01",
            "I think that it is different thing.\x02\x03",
            "#00005FOh, bother to say that\x01",
            "Did you inform me?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, this is the main theme.\x02\x03",
            "Actually, Arios with you\x01",
            "They seem to want to exchange information.\x02\x03",
            "I will come back around the evening\x01",
            "I wonder if I can get some time?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FIs it evening …?\x01",
            "Would it be ok if that was it.\x02\x03",
            "To exchange information,\x01",
            "Is it about the trade meeting again?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I have it, though …\x01",
            "About \"black moon\" and \"red constellation\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F……I understand.\x02\x03",
            "#00001FOnce you have done errands\x01",
            "I will visit there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I'll be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x102,
        (
            "#00100F#12PAssociation of Zuidori\x01",
            "I heard from Mr. Michelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PDid something happen?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#00006F#5PNo, it is an offer to exchange information.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is concerned about the matter of Michelle\x01",
            "I explained to other members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#11P\"Black moon\" and \"red constellation\" ……\x02\x03",
            "#00301FIf Aosri is an Arios certainly\x01",
            "It seems to be detailed in the information outside autonomous province.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PIt may be a boat for migration.\x02\x03",
            "#10300FWell then from now\x01",
            "Will you go back to Cros Bell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PNo, Mr. Arios\x01",
            "It seems to be the evening to come back.\x02\x03",
            "Until then, I will do this errand\x01",
            "Even if it's done, it will be okay.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588E")

    ChrTalk(
        0x102,
        (
            "#00104F#12PInformation on \"Red constellation\"\x01",
            "Although it was gathered together, ….\x02\x03",
            "#00102FI have a car.\x01",
            "It looks nice to go around a lot yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_590A")

    label("loc_588E")


    ChrTalk(
        0x102,
        (
            "#00103F#12PInformation on \"Red constellation\"\x01",
            "I have not gathered so much ……\x02\x03",
            "#00100FI have a car.\x01",
            "It looks nice to try around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590A")


    ChrTalk(
        0x109,
        (
            "#10100F#11PWell then, if you do errands\x01",
            "Let's go to the east street guild.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -29000, 0, -250, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 2)
    OP_29(0xA3, 0x1, 0x6)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_20_4D40 end

    def Function_21_598F(): pass

    label("Function_21_598F")

    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_21_598F end

    def Function_22_599F(): pass

    label("Function_22_599F")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_22_599F end

    def Function_23_59B2(): pass

    label("Function_23_59B2")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_23_59B2 end

    def Function_24_59C5(): pass

    label("Function_24_59C5")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_24_59C5 end

    def Function_25_59D8(): pass

    label("Function_25_59D8")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_25_59D8 end

    def Function_26_59EB(): pass

    label("Function_26_59EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-19190, 1000, -11460, 0)
    MoveCamera(69, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15590, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x6, 0x4)
    SetCameraDistance(17960, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_68(-22700, 2480, 50, 7000)
    MoveCamera(75, 17, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(42860, 7000)
    PlaceName2(340, 200, "c_plac19", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(-46580, 2500, -1750, 4000)
    MoveCamera(48, 28, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(22180, 4000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C8F")
    Sleep(2500)
    SetChrPos(0x101, -53200, 0, 220, 90)
    SetChrPos(0x102, -54130, 0, -950, 90)
    SetChrPos(0x104, -54120, 0, 1520, 90)
    SetChrPos(0x109, -55800, 0, 1010, 90)
    SetChrPos(0x105, -56000, 0, -620, 90)

    def lambda_5B61():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B61)

    def lambda_5B7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B7B)
    Sleep(100)

    def lambda_5B8F():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B8F)

    def lambda_5BA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5BA9)
    Sleep(120)

    def lambda_5BBD():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BBD)

    def lambda_5BD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5BD7)
    Sleep(90)

    def lambda_5BEB():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BEB)

    def lambda_5C05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5C05)
    Sleep(100)

    def lambda_5C19():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C19)

    def lambda_5C33():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5C33)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Fade(500)
    OP_68(-47890, 2500, -1790, 0)
    MoveCamera(48, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16180, 0)
    OP_0D()
    Sleep(1000)
    Jump("loc_5FDF")

    label("loc_5C8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E54")
    ClearChrFlags(0x12, 0x80)
    OP_78(0x6, 0x12)
    OP_49()
    SetChrPos(0x12, -58640, 0, 540, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    OP_0D()
    OP_49()
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x0, 0x20)
    Sleep(2200)

    def lambda_5D08():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D08)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(2500)
    Sound(492, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x12, 0x1)
    SetChrPos(0x12, -37890, 0, 4410, 270)
    OP_D5(0x12, 0x0, 0x41EB0, 0x0, 0x0)
    OP_71(0x6, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x6)
    SetMapObjFlags(0x6, 0x2)
    OP_66(0x2, 0x1)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -38290, 0, 910, 180)
    SetChrPos(0x102, -36930, 0, 0, 225)
    SetChrPos(0x104, -37690, 0, -2260, 315)
    SetChrPos(0x109, -40170, 0, -730, 90)
    SetChrPos(0x105, -39670, 0, -2360, 45)
    OP_68(-38040, 800, -240, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19090, 0)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_5FDF")

    label("loc_5E54")

    ClearChrFlags(0x10, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0x10)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x10, -58640, 0, 540, 90)
    OP_D5(0x10, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_49()
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Sleep(1700)
    Sound(473, 0, 100, 0)
    Sleep(500)

    def lambda_5ECD():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5ECD)
    Sleep(1000)
    Sound(467, 0, 100, 0)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -30230, 0, 25140, 180)
    SetChrPos(0x102, -28930, 0, 24240, 270)
    SetChrPos(0x104, -29240, 0, 22400, 315)
    SetChrPos(0x105, -32100, 0, 22120, 45)
    SetChrPos(0x109, -31780, 0, 24260, 135)
    OP_68(-31080, 1300, 23140, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18570, 0)
    Sleep(1)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_5FDF")


    ChrTalk(
        0x101,
        "#00000FOk we're finally at Tangram Gate\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FTo be sure, before dispatching to the support department\x01",
            "Is that the gate that Noel was working for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, that's right\x02\x03",
            "This side is towards the Republic\x01",
            "It will be a security border gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FNow I am new to Douglas deputy commander\x01",
            "You are taking command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FDouglas's older brother ……\x01",
            "I have not seen you for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt seems to be high in urgency\x01",
            "There was also a support request … …\x02\x03",
            "I went to the second floor of the Deputy Headquarters immediately\x01",
            "Let's visit it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61B9")
    SetChrPos(0x0, -49550, 0, -310, 90)
    Jump("loc_61EE")

    label("loc_61B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61DD")
    SetChrPos(0x0, -35570, 0, 510, 90)
    Jump("loc_61EE")

    label("loc_61DD")

    SetChrPos(0x0, -30310, 0, 21020, 180)

    label("loc_61EE")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_59EB end

    def Function_27_6204(): pass

    label("Function_27_6204")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    Call(0, 28)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    Call(0, 29)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch00053.itc", 0x23)
    LoadChrToIndex("chr/ch00153.itc", 0x24)
    LoadChrToIndex("chr/ch00353.itc", 0x25)
    LoadChrToIndex("chr/ch02953.itc", 0x26)
    LoadChrToIndex("chr/ch03053.itc", 0x27)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    LoadChrToIndex("chr/ch44950.itc", 0x2F)
    Call(0, 30)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch00053.itc", 0x23)
    LoadChrToIndex("chr/ch00153.itc", 0x24)
    LoadChrToIndex("chr/ch00353.itc", 0x25)
    LoadChrToIndex("chr/ch02953.itc", 0x26)
    LoadChrToIndex("chr/ch03053.itc", 0x27)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    LoadChrToIndex("chr/ch44950.itc", 0x2F)
    LoadChrToIndex("chr/ch44953.itc", 0x30)
    Call(0, 31)
    Return()

    # Function_27_6204 end

    def Function_28_638B(): pass

    label("Function_28_638B")

    EventBegin(0x0)
    OP_68(-22750, 3100, 20090, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrSubChip(0x15, 0x0)
    OP_4B(0x15, 0xFF)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    OP_4B(0x17, 0xFF)
    SetChrPos(0x14, -16500, 0, 21500, 270)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
    SetChrPos(0x8, -19500, 0, 26000, 180)
    SetChrPos(0x9, -20500, 0, 25500, 180)
    SetChrPos(0x15, -21500, 0, 25500, 180)
    SetChrPos(0x16, -23500, 0, 26000, 180)
    SetChrPos(0x17, -22500, 0, 25500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-22750, 2100, 20090, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x14,
        (
            "#11PFrom this,\x01",
            "\"Douglas formula exercise program\"\x01",
            "Start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PEveryone ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PFive people below Daimon,\x01",
            "We are ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWe are ready too\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PGood\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PIn the battle to be done from now on,\x01",
            "Mission Support Division team's\x01",
            "Prohibit the use of Arts at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_66B2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66B2)
    Sleep(50)

    def lambda_66C2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66C2)
    Sleep(50)

    def lambda_66D2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66D2)
    Sleep(50)

    def lambda_66E2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_66E2)
    Sleep(50)

    def lambda_66F2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_66F2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FJust\x01",
            "wait a minute!\x02\x03",
            "#00001FOnly here is no arts,\x01",
            "You are too disadvantageous … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FI see, this is a rumor\x01",
            "Is it one of \"Douglas formula\"?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        "#11PExactly\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PIn this exercise program,\x01",
            "Based on various disadvantageous conditions\x01",
            "It is a test of how to fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PBy doing so,\x01",
            "The ability to respond to various situations\x01",
            "It is aimed at raising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIndeed, the name of \"demon\" is\x01",
            "That's not Date.\x02\x03",
            "#10302FGiggle\x01",
            "It has become interesting, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FFuu …\x01",
            "There seems to be no choice but to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_691A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_691A)
    Sleep(50)

    def lambda_692A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_692A)
    Sleep(50)

    def lambda_693A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_693A)
    Sleep(50)

    def lambda_694A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_694A)
    Sleep(50)

    def lambda_695A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695A)
    Sleep(300)

    ChrTalk(
        0x14,
        "#11PLet's talk later\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#4S#11PWell then ….\x01",
            "Everyone, take a stand!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Members",
        "#5P#4S#NRight!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(16200, 700)
    OP_68(-22750, 1500, 20090, 700)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2C)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00003FThe opponent is a battle pro, a security guard ……\x01",
            "Moreover, you can not use Arts?\x02\x03",
            "#00007FEveryone, do not be discouraged!\x01",
            "You should definitely find your way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5S#11PBegin!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4B0", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_638B end

    def Function_29_6B3F(): pass

    label("Function_29_6B3F")

    EventBegin(0x0)
    OP_68(-22750, 2100, 20090, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        "#11POk that's enough\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Ugh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Use of Arts\x01",
            "Even though it is forbidden ……\x01",
            "It is expected!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FWe managed to beat them\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FIn circumstances where you can not use Arts\x01",
            "I experienced it several times during battle\x01",
            "Sometimes, but …\x02\x03",
            "#00006FFrom the beginning like this time\x01",
            "I can not use it\x01",
            "It is quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FA year ago,\x01",
            "Even when Libert's power stop phenomenon\x01",
            "I wonder if it was like this …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x14,
        (
            "#11P\"Douglas formula\" The first stage\x01",
            "It seems that I could break through without doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PThen continue, the second stage …\x01",
            "Next time the war technique#4RCraft#Use of\x01",
            "You will have to battle after banning them.\x02",
        )
    )

    CloseMessageWindow()
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

    def lambda_6EE6():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EE6)
    Sleep(50)

    def lambda_6EF6():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6EF6)
    Sleep(50)

    def lambda_6F06():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F06)
    Sleep(50)

    def lambda_6F16():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F16)
    Sleep(50)

    def lambda_6F26():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F26)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00306FOi oi seriously?\x02\x03",
            "#00301FMoreover,#4RCraft#Prohibited! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#11PHey, if you were\x01",
            "It will manage to do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PI thought it was a good experience\x01",
            "Try a single, try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FDeputy commander ……\x01",
            "Millet is too much ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#4S#11PAlright, the security guard standing up!\x01",
            "Both sides put in battle attitude!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    def lambda_7079():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7079)
    Sleep(50)

    def lambda_7089():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7089)
    Sleep(50)

    def lambda_7099():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7099)
    Sleep(50)

    def lambda_70A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70A9)
    Sleep(50)

    def lambda_70B9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70B9)
    Sleep(300)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    NpcTalk(
        0x9,
        "Members",
        "#4S#NRight!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(16200, 700)
    OP_68(-22750, 1500, 20090, 700)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2C)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00003FDamn\x01",
            "War skill#4RCraft#I can not use\x01",
            "To be honest but … ….\x02\x03",
            "#00007Fsomehow,\x01",
            "Arts and normal attack\x01",
            "We will make use of it and fight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5S#11PBegin!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4F4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_29_6B3F end

    def Function_30_726C(): pass

    label("Function_30_726C")

    EventBegin(0x0)
    OP_68(-22750, 2100, 20090, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x3)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        "#11PThat's enough\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ugh, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "They're that good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FFuu …\x01",
            "It was painful indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAh……\x01",
            "War skill#4RCraft#In how much fighting\x01",
            "You know what was important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FWell, it seems that something seems to be done\x01",
            "Is not it nice?\x02\x03",
            "#00301FOK then no more complaints\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PHuh, I see.\x01",
            "Certainly it grows well\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PIf it……\x01",
            "\"Douglas formula\" to the third stage\x01",
            "Let me move it!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(-22750, 1300, 20090, 1000)
    MoveCamera(51, 19, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(16320, 1000)
    Sound(809, 0, 70, 0)
    OP_9D(0x14, 0xFFFFACE0, 0x0, 0x5DFC, 0x7D0, 0x1388)
    TurnDirection(0x14, 0x101, 500)
    Sleep(500)
    WaitChrThread(0x14, 1)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#5S#5PA security guard, stand up!\x01",
            "Transition to final training!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Members",
        "#5S#NRIGHT!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2C)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
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

    ChrTalk(
        0x102,
        "#12P#00101FThis is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell ……\x01",
            "As I was told,\x01",
            "You seem to be deceiving.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)

    ChrTalk(
        0x101,
        (
            "#12P#00003F\"Douglas of the demon\" … ….\x01",
            "The guard No. The power of 1\x01",
            "It should not be Date.\x02\x03",
            "#00007FEveryone, for a moment\x01",
            "Do not get guarded!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHa ha ha,\x01",
            "Even readers\x01",
            "It seems to be attached to the board.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P…… So, in the exercise so far\x01",
            "Is not it a total settlement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5S#5PThis me ……\x01",
            "Try to defeat it with full power!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FS-sounds good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FHere we go!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_538", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_30_726C end

    def Function_31_78B5(): pass

    label("Function_31_78B5")

    EventBegin(0x0)
    OP_68(-22750, 1500, 20090, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16320, 0)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BAD")
    OP_2C(0x6F, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x3)
    SetChrChipByIndex(0x14, 0x30)
    SetChrSubChip(0x14, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00002FW-we did it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI'm stupid\x01",
            "No way, the deputy commander …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHydrofluoric …… quite\x01",
            "well done.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#00305FAt all\x01",
            "It seems not to be effective.\x02\x03",
            "#00306FPowered by Discuz!\x01",
            "Is it tough or what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PNo this time was my loss\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PSince long ago, you have physical strength\x01",
            "I am the only acquirer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109FY-you flatter us\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FYou're humble as expected commander\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FSeriously, you were tough\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5POkay, exercises for the moment\x01",
            "This is the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x2)
    Jump("loc_7D96")

    label("loc_7BAD")

    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x24)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x3)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x3)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00003FCut …!\x01",
            "Did not reach it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FArts and fighting techniques#4RCraft#Even if there is\x01",
            "I can not win … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#12P#00301FWell, good age.\x01",
            "Do not be afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHuh, I've got a lot more\x01",
            "It is to be active.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PYou guys are pretty\x01",
            "I think I was doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FIt is a perfect defeat …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FAs expected, the guard\x01",
            "I think it is a deputy commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5POkay, exercises for the moment\x01",
            "This is the end.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    OP_0D()
    OP_29(0x6F, 0x1, 0x3)
    SetScenarioFlags(0x1, 0)

    label("loc_7D96")

    TurnDirection(0x14, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#11PGo back to your staff\x01",
            "Resume each job.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7DFF")
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_7E05")

    label("loc_7DFF")

    Sound(802, 0, 100, 0)

    label("loc_7E05")

    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    NpcTalk(
        0x9,
        "Members",
        "#4S#NYes!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x14, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#5PAlso,\x01",
            "It was a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PThere are also story talks,\x01",
            "Once in the command room\x01",
            "Shall I go back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FR-right\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x22, 0)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_78B5 end

    def Function_32_7EFA(): pass

    label("Function_32_7EFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-41990, 1000, 10, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    SetChrPos(0x101, -49500, 0, 0, 90)
    SetChrPos(0x102, -49500, 0, -1200, 90)
    SetChrPos(0x104, -49500, 0, 1200, 90)
    SetChrPos(0x109, -50500, 0, 0, 90)
    SetChrPos(0x103, -50500, 0, -1200, 90)
    SetChrPos(0x105, -50500, 0, 1200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_7FB3():
        OP_95(0x101, -42000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FB3)
    Sleep(30)

    def lambda_7FD0():
        OP_95(0x102, -42500, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FD0)
    Sleep(40)

    def lambda_7FED():
        OP_95(0x104, -42500, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7FED)
    Sleep(800)

    def lambda_800A():
        OP_95(0x109, -44100, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_800A)
    Sleep(30)

    def lambda_8027():
        OP_95(0x103, -43800, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8027)
    Sleep(10)

    def lambda_8044():
        OP_95(0x105, -43800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8044)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#00000FWell ……\x01",
            "Is the black truck come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI can not find it outdoors … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FMaybe already inside\x01",
            "I might be preparing for departure\x01",
            "I do not think so …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThat seems likely.\x01",
            "It took me a while to come … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FLet's check it in a hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWhew, let me make it in time … …\x02",
    )

    CloseMessageWindow()

    def lambda_81CE():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81CE)
    Sleep(30)

    def lambda_81EB():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81EB)
    Sleep(40)

    def lambda_8208():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8208)
    Sleep(30)

    def lambda_8225():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8225)
    Sleep(30)

    def lambda_8242():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8242)
    Sleep(10)

    def lambda_825F():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_825F)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x93, 0x1, 0x3)
    SetScenarioFlags(0x22, 1)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_7EFA end

    def Function_33_82A0(): pass

    label("Function_33_82A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-31240, 1000, 24480, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    SetChrPos(0x101, -31060, 0, 25800, 180)
    SetChrPos(0x102, -29790, 0, 24750, 270)
    SetChrPos(0x104, -29830, 0, 23100, 270)
    SetChrPos(0x109, -31200, 0, 21720, 0)
    SetChrPos(0x103, -32330, 0, 23100, 90)
    SetChrPos(0x105, -32330, 0, 24750, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FWell ……\x01",
            "Is the black truck come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI can not find it outdoors … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FMaybe already inside\x01",
            "I might be preparing for departure\x01",
            "I do not think so …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThat seems likely.\x01",
            "A bit in the waiting time of the bus\x01",
            "I took time and effort ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FLet's check it in a hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWhew, let me make it in time … …\x02",
    )

    CloseMessageWindow()

    def lambda_84B6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_84B6)
    Sleep(30)

    def lambda_84C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_84C6)
    Sleep(40)

    def lambda_84D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_84D6)
    Sleep(30)

    def lambda_84E6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_84E6)
    Sleep(30)

    def lambda_84F6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_84F6)
    Sleep(10)

    def lambda_8506():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8506)
    WaitChrThread(0x109, 2)

    def lambda_8517():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8517)
    WaitChrThread(0x104, 2)

    def lambda_8535():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8535)
    WaitChrThread(0x103, 2)

    def lambda_8553():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8553)
    WaitChrThread(0x102, 2)

    def lambda_8571():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8571)
    WaitChrThread(0x105, 2)

    def lambda_858F():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_858F)
    WaitChrThread(0x101, 2)

    def lambda_85AD():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85AD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x93, 0x1, 0x4)
    SetScenarioFlags(0x22, 1)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_82A0 end

    def Function_34_85EE(): pass

    label("Function_34_85EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x8000000)
    OP_68(-41990, 1000, 10, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    LoadChrToIndex("chr/ch45200.itc", 0x1E)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrPos(0x101, -35000, 0, 0, 0)
    SetChrPos(0x102, -35000, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Sound(459, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x1, 0x20)

    def lambda_86A7():
        OP_96(0x12, 0xFFFF5BF0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_86A7)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(492, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_71(0x6, 0x5B, 0x78, 0x1, 0x8)
    StopSound(459, 1000, 90)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThat is……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FApparently, it looks like you found it.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-24420, 1000, -11490, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    SetChrPos(0x101, -32250, 0, -8230, 135)
    SetChrPos(0x102, -31980, 0, -6900, 135)
    SetChrPos(0x103, -31690, 0, -9430, 135)
    SetChrPos(0x104, -33590, 0, -6950, 135)
    SetChrPos(0x105, -33500, 0, -5480, 135)
    SetChrPos(0x109, -33500, 0, -7110, 135)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrPos(0x18, -24460, 0, -11450, 90)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_88BC")

    ChrTalk(
        0x18,
        (
            "Powered by Translate\x01",
            "It will be safe if you come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Then I will use this medical supplies\x01",
            "You can sell it in the direction of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Medical supplies manufactured by Remiferia …\x01",
            "It will be a nice mirror.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8984")

    label("loc_88BC")


    NpcTalk(
        0x18,
        "Merchant-style man",
        (
            "Powered by Translate\x01",
            "It will be safe if you come here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Merchant-style man",
        (
            "Then I will use this medical supplies\x01",
            "You can sell it in the direction of the Republic.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Merchant-style man",
        (
            "Medical supplies manufactured by Remiferia …\x01",
            "It will be a nice mirror.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8984")


    ChrTalk(
        0x101,
        "#00007F─ ─ Do not let that happen!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(-25430, 1000, -10970, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(21210, 3000)

    def lambda_89F0():
        OP_95(0x101, -26500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89F0)

    def lambda_8A0A():
        OP_95(0x102, -26230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A0A)

    def lambda_8A24():
        OP_95(0x103, -26500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8A24)

    def lambda_8A3E():
        OP_95(0x104, -27950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8A3E)

    def lambda_8A58():
        OP_95(0x105, -27550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A58)

    def lambda_8A72():
        OP_95(0x109, -27550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A72)
    WaitChrThread(0x101, 1)

    def lambda_8A90():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A90)
    WaitChrThread(0x102, 1)

    def lambda_8AA1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8AA1)
    WaitChrThread(0x103, 1)

    def lambda_8AB2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8AB2)
    WaitChrThread(0x104, 1)

    def lambda_8AC3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8AC3)
    WaitChrThread(0x105, 1)

    def lambda_8AD4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8AD4)
    WaitChrThread(0x109, 1)

    def lambda_8AE5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8AE5)
    OP_93(0x18, 0x10E, 0x1F4)
    WaitChrThread(0x109, 2)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E2B")

    ChrTalk(
        0x18,
        "You guys ……! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMinnes ……\x01",
            "Although he was conscious,\x01",
            "It was you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FTo you, medical supplies at the airport\x01",
            "It is charged with cheating.\x02\x03",
            "#00101FI'm sorry but,\x01",
            "Even if you show the load …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "…… Hun, because I was in a hurry\x01",
            "Did you work too coarse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, indeed.\x01",
            "Compared to when I saw him in Almorika village\x01",
            "It is a sign that lacks a lot of precision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "…… you guys are here\x01",
            "Failed to work in Almorika village,\x01",
            "A woman who is wanted to arrange … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "About this\x01",
            "I have to pay for pocket money\x01",
            "The business has come up well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHat … another one\x01",
            "I wonder there are reasons for defeating.\x02\x03",
            "#00301FYou are the \"red constellation\"\x01",
            "A servant merchant or a fund raiser\x01",
            "I know that.\x02\x03",
            "Those guys are crossbells and do something like that\x01",
            "Because I got lost,\x01",
            "You probably stopped staying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "… … Huh, I will leave it to your imagination.\x02",
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x5)
    Jump("loc_9171")

    label("loc_8E2B")


    NpcTalk(
        0x18,
        "Merchant-style man",
        "Hey, are you …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWe, Crossbell Police,\x01",
            "It is a person of the affairs support department.\x02\x03",
            "I'm sorry but……\x01",
            "Name and status\x01",
            "Could you reveal it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Merchant-style man",
        (
            "Hmm … … was the police?\x01",
            "I apologize for this.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Merchant-style man",
        (
            "My name is Minnes ……\x01",
            "It is a sharp merchant from the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "From now, toward the Republic\x01",
            "It is a place to go out for trading ……\x01",
            "Is there anything I can do for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FWhew, Shiretto suddenly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FTo you, medical supplies at the airport\x01",
            "It is charged with cheating.\x02\x03",
            "#00101FI'm sorry but,\x01",
            "Even if you show the load …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Hmm, indeed for this transporter\x01",
            "I have medical supplies ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "Originally this is my baggage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Or maybe I cheated\x01",
            "Is there also evidence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FEven if you can cut off Sufa\x01",
            "I wonder if she is thinking.\x02\x03",
            "#10302FIf you confirm with Ricardo\x01",
            "I think that I can not escape to fossil.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x6)

    label("loc_9171")


    ChrTalk(
        0x103,
        (
            "#00203F…… Time is regrettable.\x01",
            "Let's forcibly take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FOh … it seems to be the only way to do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Oh, I'm scared of scary.\x01",
            "What a savage people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "If it……\x01",
            "I do not think I should flee.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sound(464, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x3C, 0x1, 0x8)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(500)

    def lambda_926A():
        OP_95(0x18, -23800, 0, -11450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_926A)
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
    WaitChrThread(0x18, 1)
    Sound(463, 0, 100, 0)

    def lambda_9324():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9324)
    OP_95(0x18, -23000, 600, -11450, 2000, 0x0)

    ChrTalk(
        0x101,
        "#00007F#11AWait a minute … …!\x02",
    )

    Sound(470, 0, 70, 0)
    OP_74(0xB, 0x3C)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x13, 1, 0, 35)
    Sleep(800)
    OP_57(0x0)
    OP_5A()

    def lambda_93BB():
        OP_95(0x101, -23500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_93BB)

    def lambda_93D5():
        OP_95(0x102, -23230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93D5)

    def lambda_93EF():
        OP_95(0x103, -23500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93EF)

    def lambda_9409():
        OP_95(0x104, -24950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9409)

    def lambda_9423():
        OP_95(0x105, -24550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9423)

    def lambda_943D():
        OP_95(0x109, -24550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_943D)
    WaitChrThread(0x109, 1)

    def lambda_945B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_945B)

    def lambda_9468():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9468)

    def lambda_9475():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9475)

    def lambda_9482():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9482)

    def lambda_948F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_948F)

    def lambda_949C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_949C)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10107FMr. Lloyd,\x01",
            "Let's follow the power guide car here as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FAh……!\x02",
    )

    CloseMessageWindow()

    def lambda_94FB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_94FB)
    Sleep(50)

    def lambda_950B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_950B)
    Sleep(50)

    def lambda_951B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_951B)
    Sleep(50)

    def lambda_952B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_952B)
    Sleep(50)

    def lambda_953B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_953B)
    Sleep(50)

    def lambda_954B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_954B)
    WaitChrThread(0x101, 1)

    def lambda_955C():
        OP_95(0x101, -32250, 0, -8230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_955C)
    WaitChrThread(0x102, 1)

    def lambda_957A():
        OP_95(0x102, -31980, 0, -6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_957A)
    WaitChrThread(0x103, 1)

    def lambda_9598():
        OP_95(0x103, -31690, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9598)
    WaitChrThread(0x104, 1)

    def lambda_95B6():
        OP_95(0x104, -33590, 0, -6950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_95B6)
    WaitChrThread(0x105, 1)

    def lambda_95D4():
        OP_95(0x105, -33500, 0, -5480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_95D4)
    WaitChrThread(0x109, 1)

    def lambda_95F2():
        OP_95(0x109, -33500, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_95F2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetScenarioFlags(0x22, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_85EE end

    def Function_35_9627(): pass

    label("Function_35_9627")

    SetChrPos(0xFE, -22290, 0, -12240, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -24290, 0, -4000)
    OP_9F(0x1, -23290, 0, -2000)
    OP_9F(0x1, -21000, 0, 0)
    OP_9F(0x1, -18290, 0, 0)
    OP_9F(0x1, 290, 0, 0)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_35_9627 end

    def Function_36_968C(): pass

    label("Function_36_968C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Republic of the Carbado border\x01",
            "\"Tangram Gate\"\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_968C end

    SaveToFile()

Try(main)
