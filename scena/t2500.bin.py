from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Nowe",                   # 1
        "Daimon",                 # 2
        "Garrison",               # 3
        "Burrell ",               # 4
        "Chiruru",                # 5
        "Yuri",                   # 6
        "Sykes",                  # 7
        "Reggie",                 # 8
        "バス",                   # 9
        "列車",                   # 10
        "Special Support Vehicle",# 11
        "Transport",              # 12
        "Vice Commander Douglas", # 13
        "Oliver ",                # 14
        "Jack ",                  # 15
        "Alexei",                 # 16
        "Minneth",                # 17
        "bt2500",                 # 18
        "bt2500",                 # 19
        "bt2500",                 # 20
        "East Crossbell Highway", # 21
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
        "Function_6_12C4",         # 06, 6
        "Function_7_13F1",         # 07, 7
        "Function_8_1442",         # 08, 8
        "Function_9_14D6",         # 09, 9
        "Function_10_236F",        # 0A, 10
        "Function_11_31D1",        # 0B, 11
        "Function_12_330F",        # 0C, 12
        "Function_13_34B1",        # 0D, 13
        "Function_14_35D9",        # 0E, 14
        "Function_15_3719",        # 0F, 15
        "Function_16_43B0",        # 10, 16
        "Function_17_50CA",        # 11, 17
        "Function_18_5407",        # 12, 18
        "Function_19_545B",        # 13, 19
        "Function_20_55F4",        # 14, 20
        "Function_21_63A9",        # 15, 21
        "Function_22_63B9",        # 16, 22
        "Function_23_63CC",        # 17, 23
        "Function_24_63DF",        # 18, 24
        "Function_25_63F2",        # 19, 25
        "Function_26_6405",        # 1A, 26
        "Function_27_6C65",        # 1B, 27
        "Function_28_6DEC",        # 1C, 28
        "Function_29_75D5",        # 1D, 29
        "Function_30_7D37",        # 1E, 30
        "Function_31_83A0",        # 1F, 31
        "Function_32_8A59",        # 20, 32
        "Function_33_8E26",        # 21, 33
        "Function_34_9192",        # 22, 34
        "Function_35_A28C",        # 23, 35
        "Function_36_A2F1",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1169")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x646, 1)"), scpexpr(EXPR_END)), "loc_10F2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1164")

    label("loc_10F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x646),
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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1164")

    Jump("loc_11B2")

    label("loc_1169")

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
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City East Entrance\x01",      # 0
            "Armorica Village\x01",                  # 1
            "Bus Stop (Fork in the Road)\x01",       # 2
            "Cancel\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1277")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12BC")

    label("loc_1277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129C")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12BC")

    label("loc_129C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BC")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_12BC")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_5_11BE end

    def Function_6_12C4(): pass

    label("Function_6_12C4")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_13ED")
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

    def lambda_13A4():
        OP_98(0xFE, 0x0, 0x0, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13A4)
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

    label("loc_13ED")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_6_12C4 end

    def Function_7_13F1(): pass

    label("Function_7_13F1")

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

    # Function_7_13F1 end

    def Function_8_1442(): pass

    label("Function_8_1442")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_149D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1492")
    Sound(2502, 255, 100, 0)
    Jump("loc_1498")

    label("loc_1492")

    Sound(2503, 255, 100, 0)

    label("loc_1498")

    Jump("loc_14C1")

    label("loc_149D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14BB")
    Sound(3347, 255, 100, 0)
    Jump("loc_14C1")

    label("loc_14BB")

    Sound(3348, 255, 100, 0)

    label("loc_14C1")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1442 end

    def Function_9_14D6(): pass

    label("Function_9_14D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1651")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Solider Nowe",
        (
            "Y-You guys are...!? ...Wait,\x01",
            "there's no need to arrest\x01",
            "you any longer, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Solider Nowe",
        (
            "*sigh*, in the end, we\x01",
            "State Guard didn't do\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Solider Nowe",
        (
            "Even the unappreciated CGF\x01",
            "finally had its pride. I\x01",
            "had that feeling, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Solider Nowe",
        (
            "I feel like I had a\x01",
            "long, long dream...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D4")

    label("loc_1651")


    NpcTalk(
        0x8,
        "Solider Nowe",
        (
            "*sigh*, in the end, we\x01",
            "State Guard didn't do\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Solider Nowe",
        (
            "I feel like I had a\x01",
            "long, long dream...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D4")

    Jump("loc_236B")

    label("loc_16D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_186E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E1")

    ChrTalk(
        0x8,
        (
            "The condition of the\x01",
            "members hospitalised at St.\x01",
            "Ursula seem unpredictable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Man, they were luckier\x01",
            "than... our comrades who\x01",
            "died on the mountain path...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm normally calm.\x01",
            "However... I can't control\x01",
            "my anger this time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1869")

    label("loc_17E1")


    ChrTalk(
        0x8,
        (
            "I'm normally calm.\x01",
            "However... I can't control\x01",
            "my anger this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Red Constellation... I\x01",
            "swear, they'll pay for\x01",
            "this one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1869")

    Jump("loc_236B")

    label("loc_186E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1991")

    ChrTalk(
        0x8,
        (
            "Yesterday's accident near West\x01",
            "Crossbell Highway was expected\x01",
            "to have a large impact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they hadn't completed the repairs,\x01",
            "the Empire and Republic would have\x01",
            "likely meddled with the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to praise the\x01",
            "unit that completed the\x01",
            "repairs.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A47")

    label("loc_1991")


    ChrTalk(
        0x8,
        (
            "If the accident repairs hadn't been\x01",
            "completed, the Empire and Republic would\x01",
            "have likely meddled with the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to praise the\x01",
            "unit that completed the\x01",
            "repairs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A47")

    Jump("loc_236B")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B52")

    ChrTalk(
        0x8,
        (
            "Crossbell State pays 10%\x01",
            "of revenues to the\x01",
            "Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If the system was abolished\x01",
            "by state independence, the\x01",
            "budget would rise a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that happened, I wonder\x01",
            "if they would prioritize\x01",
            "strengthening the CGF.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C11")

    label("loc_1B52")


    ChrTalk(
        0x8,
        (
            "If the system where we pay 10%\x01",
            "revenues were crushed by independence,\x01",
            "the budget would rise a lot, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that happened, I wonder\x01",
            "if they would prioritize\x01",
            "strengthening the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C11")

    Jump("loc_236B")

    label("loc_1C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0x8,
        (
            "The State of Crossbell is\x01",
            "situated geographically between\x01",
            "the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In other words, the independence\x01",
            "proposal is tantamount to\x01",
            "confronting both of them head-on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you think about it,\x01",
            "what the mayor did was\x01",
            "bold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DBF")

    label("loc_1D24")


    ChrTalk(
        0x8,
        (
            "The independence proposal at the trade\x01",
            "conference was equal to declaring a\x01",
            "confrontation against both of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, what the mayor did\x01",
            "was bold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBF")

    Jump("loc_236B")

    label("loc_1DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDF")

    ChrTalk(
        0x8,
        (
            "Republican terrorists are\x01",
            "entering Crossbell...\x01",
            "We've received such intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Terrorism isn't anything calm. If\x01",
            "they want to spread their ideas, they\x01",
            "should think about other methods...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Wait, even if I say\x01",
            "stuff like this, there's\x01",
            "no point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F95")

    label("loc_1EDF")


    ChrTalk(
        0x8,
        (
            "Republican terrorists are\x01",
            "entering Crossbell...\x01",
            "We've received such intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As for terrorist acts, I can think\x01",
            "of many things, but... For now, we\x01",
            "have to focus on security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F95")

    Jump("loc_236B")

    label("loc_1F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2084")

    ChrTalk(
        0x8,
        (
            "This morning, President\x01",
            "Rocksmith's white limousine\x01",
            "passed through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been quite busy\x01",
            "with reception and\x01",
            "traffic control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We really need to pay\x01",
            "attention when a VIP\x01",
            "enters the state.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2134")

    label("loc_2084")


    ChrTalk(
        0x8,
        (
            "We were pretty busy with receiving\x01",
            "President Rocksmith's limousine and\x01",
            "the traffic control this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We really need to pay\x01",
            "attention when a VIP\x01",
            "enters the state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2134")

    Jump("loc_236B")

    label("loc_2139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_236B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_21E9")

    ChrTalk(
        0x8,
        (
            "Maaan, thanks to you, it was\x01",
            "a nice practice. You guys\x01",
            "are pretty good, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there's a chance,\x01",
            "let's have another match\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236B")

    label("loc_21E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CF")

    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas,\x01",
            "newly appointed to Tangram,\x01",
            "is a pretty sociable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I dare say he's like a\x01",
            "big brother everyone can\x01",
            "count on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Although when it\x01",
            "comes to work, he's\x01",
            "extremely strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_236B")

    label("loc_22CF")


    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas\x01",
            "is a pretty sociable\x01",
            "person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I dare say he's like a big brother\x01",
            "everyone can count on. ...Although\x01",
            "he's strict on the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236B")

    TalkEnd(0xFE)
    Return()

    # Function_9_14D6 end

    def Function_10_236F(): pass

    label("Function_10_236F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D5")

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Due to the appearance of that pale blue\x01",
            "tree, the Republican Army seems to have\x01",
            "taken wait-and-see position for now, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Now that we've lost the\x01",
            "barrier and Aions, we\x01",
            "must be on guard.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Only we State Guard can\x01",
            "defend Crossbell now. We have\x01",
            "to keep a strict lookout.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25C9")

    label("loc_24D5")


    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Due to the appearance of that pale blue\x01",
            "tree, the Republican Army seems to have\x01",
            "taken wait-and-see position for now, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Only we State Guard can\x01",
            "defend Crossbell now. We have\x01",
            "to keep a strict lookout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C9")

    Jump("loc_31CD")

    label("loc_25CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272C")

    ChrTalk(
        0x9,
        (
            "Not being able to defend against\x01",
            "the attack on Crossbell was an\x01",
            "obvious failure of the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Due to the Mainz occupation, our battle\x01",
            "strength was reduced, but... Something\x01",
            "like that is nothing more than an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As an organization that maintains\x01",
            "security... there may be a lot of\x01",
            "things we need to rethink.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F1")

    label("loc_272C")


    ChrTalk(
        0x9,
        (
            "Not being able to defend against\x01",
            "the attack on Crossbell was an\x01",
            "obvious failure of the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As an organization that maintains\x01",
            "security... there may be a lot of\x01",
            "things we need to rethink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F1")

    Jump("loc_31CD")

    label("loc_27F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(
        0x9,
        (
            "A male bracer was asking around\x01",
            "here earlier... It seems some\x01",
            "female bracers have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... I hope nothing\x01",
            "has happened to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CD")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_294D")

    ChrTalk(
        0x9,
        (
            "The bracers seem to be\x01",
            "searching various places going\x01",
            "after the Cryptids themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, they know the\x01",
            "backwoods areas, and\x01",
            "even we can't go there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CD")

    label("loc_294D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ACC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A57")

    ChrTalk(
        0x9,
        (
            "If a Cryptid were to hurt a\x01",
            "foreigner, the major powers would\x01",
            "use that against us for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it's tied to the border\x01",
            "tensions as well, it's a\x01",
            "problem the CGF can't overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're counting on you\x01",
            "for the investigation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AC7")

    label("loc_2A57")


    ChrTalk(
        0x9,
        (
            "The Cryptid problem is\x01",
            "something the CGF can't\x01",
            "overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're counting on you\x01",
            "for the investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC7")

    Jump("loc_31CD")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B78")

    ChrTalk(
        0x9,
        (
            "Regarding the terrorists, we\x01",
            "are guarding against them\x01",
            "with all our resources.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On the honor of the CGF,\x01",
            "we absolutely must\x01",
            "prevent an infiltration.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CD")

    label("loc_2B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(
        0x9,
        (
            "President Rocksmith is said to be\x01",
            "supported by the Republican citizens\x01",
            "under the populist faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Really, I wonder what\x01",
            "sort of man he is in\x01",
            "practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CD")

    label("loc_2C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_31CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D39")

    ChrTalk(
        0x9,
        (
            "Although you had Sergeant Noｱl with you,\x01",
            "to think you could fight such a good\x01",
            "fight against Vice Commander Douglas...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected the Special Support Section\x01",
            "at the center of the cult incident, I\x01",
            "guess? Honestly, you guys did very well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31CD")

    label("loc_2D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3029")

    ChrTalk(
        0x9,
        (
            "Sergeant Major Noｱl,\x01",
            "thank you for your hard\x01",
            "work! ......\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThank you too, Daimon.\x01",
            "...Umm, is something the\x01",
            "matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Hm, how to say it... I was thinking that\x01",
            "was somehow refreshing seeing the Sergeant\x01",
            "Major not wearing the CGF uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FAh, now that I think about it,\x01",
            "it might be my first visit to\x01",
            "Tangram Gate in this outfit...\x02\x03",
            "#10112FSorry, maybe I was a bit\x01",
            "inconsiderate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "N-No. I think it's very\x01",
            "nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha, then.... You're flustered\x01",
            "because Noｱl's in an outfit\x01",
            "you're not used to seeing her in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FHuuuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "N-No, that's not that.\x01",
            "Absolutely not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...P-Pardon me. Please\x01",
            "forget it, Sergeant\x01",
            "Major.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(D-Damn you, Randy.\x01",
            "That's embarrassing,\x01",
            "jeez...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 7)
    Jump("loc_31CD")

    label("loc_3029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3128")

    ChrTalk(
        0x9,
        (
            "...To be honest, I was caught off\x01",
            "guard by you not being in uniform.\x01",
            "Man, I'm not trained for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm extremely sorry.\x01",
            "Sergeant Major, please\x01",
            "forget it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Is "training" the\x01",
            "problem here...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31CD")

    label("loc_3128")


    ChrTalk(
        0x9,
        (
            "...To be honest, I was caught off\x01",
            "guard by you not being in uniform.\x01",
            "Man, I'm not trained for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm extremely sorry.\x01",
            "Sergeant Major, please\x01",
            "forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31CD")

    TalkEnd(0xFE)
    Return()

    # Function_10_236F end

    def Function_11_31D1(): pass

    label("Function_11_31D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_330B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A5")

    ChrTalk(
        0xC,
        (
            "I met these people at\x01",
            "the city's east exit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since they said they wanted to\x01",
            "go to Tangram Gate, I took them\x01",
            "along as bodyguards, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Honestly, they were\x01",
            "useless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_330B")

    label("loc_32A5")


    ChrTalk(
        0xC,
        (
            "Even so, walking on the\x01",
            "highway was quite\x01",
            "thrilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Maybe I'll go to\x01",
            "Armorica Village now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330B")

    TalkEnd(0xFE)
    Return()

    # Function_11_31D1 end

    def Function_12_330F(): pass

    label("Function_12_330F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3425")

    ChrTalk(
        0xD,
        (
            "*pant, pant*... When we encountered\x01",
            "a Cryptid on the way, I didn't know\x01",
            "what was going to happen, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I-In any case, we managed\x01",
            "make it here. All that's left is\x01",
            "to head back to the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "W-We'll be able to\x01",
            "return, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_34AD")

    label("loc_3425")


    ChrTalk(
        0xD,
        (
            "I've never been treated\x01",
            "like this since the day\x01",
            "I was born...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I-I wonder if we'll be\x01",
            "really able to return to\x01",
            "the Republic...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34AD")

    TalkEnd(0xFE)
    Return()

    # Function_12_330F end

    def Function_13_34B1(): pass

    label("Function_13_34B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_35D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357B")

    ChrTalk(
        0xE,
        (
            "*pant, pant*... I\x01",
            "thought surely this road\x01",
            "was safe, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Who would've thought we'd get stuck\x01",
            "doing a marathon on the highway...\x01",
            "I-I thought I was gonna die...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_35D5")

    label("loc_357B")


    ChrTalk(
        0xE,
        (
            "Ooh, why'd this have to\x01",
            "happen to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've had enough of\x01",
            "Crossbell already...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D5")

    TalkEnd(0xFE)
    Return()

    # Function_13_34B1 end

    def Function_14_35D9(): pass

    label("Function_14_35D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DD")

    ChrTalk(
        0xF,
        (
            "Even though the barrier\x01",
            "dissolved, we don't have\x01",
            "a car, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "After we were guided here by a\x01",
            "girl we met by coincidence, now\x01",
            "there's this bothersome stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "A-As expected,\x01",
            "hitchhiking would've\x01",
            "been better...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3715")

    label("loc_36DD")


    ChrTalk(
        0xF,
        (
            "A-As expected,\x01",
            "hitchhiking would've\x01",
            "been better...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3715")

    TalkEnd(0xFE)
    Return()

    # Function_14_35D9 end

    def Function_15_3719(): pass

    label("Function_15_3719")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_395F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3880")

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "Per the vice commander's orders,\x01",
            "we're continuing to secure the\x01",
            "Republican border....\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "However, it was because we had\x01",
            "power of the Aions that we repelled\x01",
            "the major powers' armies before.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "The next time they come to\x01",
            "invade... we probably won't\x01",
            "be able to stop them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_395A")

    label("loc_3880")


    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "It was because we had the\x01",
            "power of the Aions that we\x01",
            "repelled the armies before.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "The next time the Republican Army\x01",
            "comes to invade... We probably\x01",
            "won't be able to stop them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395A")

    Jump("loc_43AC")

    label("loc_395F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A50")

    ChrTalk(
        0xA,
        (
            "Because we received heavy\x01",
            "damage from the jaeger\x01",
            "corps, the CGF has crumbled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I was told to fight those\x01",
            "guys again, I'd honestly end\x01",
            "up running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder how we should\x01",
            "proceed from now on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3ADA")

    label("loc_3A50")


    ChrTalk(
        0xA,
        (
            "If I was told to fight that\x01",
            "jaeger corps again, I'd\x01",
            "honestly end up running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder how we should\x01",
            "proceed from now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADA")

    Jump("loc_43AC")

    label("loc_3ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7F")

    ChrTalk(
        0xA,
        "......*atchooo*!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I guess I'm a little\x01",
            "chilly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It won't be good if I\x01",
            "catch a cold. Maybe I\x01",
            "should rest a little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C1A")

    label("loc_3B7F")


    ChrTalk(
        0xA,
        (
            "I'm a little chilly so I\x01",
            "guess I'll go take a short\x01",
            "break at the mess hall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In this state of tension,\x01",
            "having your health ruined\x01",
            "won't be good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1A")

    Jump("loc_43AC")

    label("loc_3C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D23")

    ChrTalk(
        0xA,
        (
            "At present, it's ambiguous\x01",
            "whether Tangram Hill is\x01",
            "Crossbell or Republic territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Republic has\x01",
            "possession at present,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If Crossbell were to become\x01",
            "independent, it seems the\x01",
            "dispute would go on for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DD2")

    label("loc_3D23")


    ChrTalk(
        0xA,
        (
            "At present, it's ambiguous\x01",
            "whether Tangram Hill is\x01",
            "Crossbell or Republic territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even if independence was\x01",
            "realized, it seems the dispute\x01",
            "would go on for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD2")

    Jump("loc_43AC")

    label("loc_3DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE9")

    ChrTalk(
        0xA,
        (
            "As the day of the referendum\x01",
            "gets closer, the pressure\x01",
            "gets stronger day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems the Republican citizens\x01",
            "have a dissenting opinion of\x01",
            "Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I pray that their actions\x01",
            "and policies don't grow\x01",
            "too audacious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F8A")

    label("loc_3EE9")


    ChrTalk(
        0xA,
        (
            "It seems the Republican citizens\x01",
            "have a dissenting opinion of\x01",
            "Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I pray that their actions\x01",
            "and policies don't grow\x01",
            "too audacious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8A")

    Jump("loc_43AC")

    label("loc_3F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_418B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40BE")

    ChrTalk(
        0xA,
        (
            "As you can see, the view is\x01",
            "great from Tangram Hill, and we\x01",
            "also have monitoring facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If vehicles or aircraft\x01",
            "are coming from there,\x01",
            "we'll know immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It won't be so easy, of course,\x01",
            "but... Don't worry, we'll never\x01",
            "allow terrorists to get through.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4186")

    label("loc_40BE")


    ChrTalk(
        0xA,
        (
            "As you can see, the view is\x01",
            "great from Tangram Hill, and we\x01",
            "also have monitoring facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It won't be so easy, of course,\x01",
            "but... Don't worry, we'll never\x01",
            "allow terrorists to get through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4186")

    Jump("loc_43AC")

    label("loc_418B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4243")

    ChrTalk(
        0xA,
        (
            "President Rocksmith's\x01",
            "limousine is guarded by\x01",
            "many escort vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As expected from the President\x01",
            "who governs the Republic... The\x01",
            "scene was truly a spectacle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43AC")

    label("loc_4243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4335")

    ChrTalk(
        0xA,
        (
            "Tangram Hill spreading out\x01",
            "before you in all directions...\x01",
            "It's a very nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Historically, it's said to have\x01",
            "been the stage upon which many\x01",
            "battles were fought, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I quite love this\x01",
            "scenery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43AC")

    label("loc_4335")


    ChrTalk(
        0xA,
        (
            "Tangram Hill spreading out\x01",
            "before you in all directions...\x01",
            "It's a very nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I quite love this\x01",
            "scenery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AC")

    TalkEnd(0xFE)
    Return()

    # Function_15_3719 end

    def Function_16_43B0(): pass

    label("Function_16_43B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_458B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44D1")

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "That mysterious tree... I'm\x01",
            "sure it can be seen from\x01",
            "everywhere in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "Something like that\x01",
            "appearing all of a sudden...\x01",
            "That's not normal at all.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "What will become of\x01",
            "Crossbell, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4586")

    label("loc_44D1")


    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "A mysterious tree... Such a thing\x01",
            "appearing all of a sudden...\x01",
            "That's not normal at all.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "I wonder how Broude at\x01",
            "Bellguard Gate is\x01",
            "doing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4586")

    Jump("loc_50C6")

    label("loc_458B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_472C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469B")

    ChrTalk(
        0xB,
        (
            "It seems Broude, my\x01",
            "childhood friend at\x01",
            "Bellguard Gate, was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Still, I can't rest\x01",
            "easy. The CGF's losses\x01",
            "are great, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly speaking, I'm afraid of\x01",
            "what's going to happen, but...\x01",
            "All I can do is prepare myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4727")

    label("loc_469B")


    ChrTalk(
        0xB,
        (
            "The CGF's losses are\x01",
            "indeed huge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly speaking, I'm afraid of\x01",
            "what's going to happen, but...\x01",
            "All I can do is prepare myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4727")

    Jump("loc_50C6")

    label("loc_472C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4848")

    ChrTalk(
        0xB,
        (
            "I heard the radar\x01",
            "facility is operating at\x01",
            "full power today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's hard to keep an eye on\x01",
            "the sky when it rains. It's\x01",
            "quite handy for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was destroyed during the trade\x01",
            "conference, but it's serving its\x01",
            "purpose properly now, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48E5")

    label("loc_4848")


    ChrTalk(
        0xB,
        (
            "The radar facility is\x01",
            "quite handy for\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was destroyed during the trade\x01",
            "conference, but it's serving its\x01",
            "purpose properly now, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E5")

    Jump("loc_50C6")

    label("loc_48EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_496F")

    ChrTalk(
        0xB,
        (
            "Vice Commander Douglas is sociable\x01",
            "and, despite appearances, is a\x01",
            "pretty cool man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I could be like\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50C6")

    label("loc_496F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AA7")

    ChrTalk(
        0xB,
        (
            "Those cryptids look like those\x01",
            "mysterious spirit-like beings that\x01",
            "appeared before at the Temple of Moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It would be ok if only their\x01",
            "appearance was scary, but not knowing\x01",
            "their origins is oddly terrifying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I ever bump into one,\x01",
            "I mustn't lose\x01",
            "consciousness again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B61")

    label("loc_4AA7")


    ChrTalk(
        0xB,
        (
            "When we went to investigate the\x01",
            "spirits that appeared at the Temple of\x01",
            "Moon before, I fainted and collapsed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I ever bump into a\x01",
            "cryptid, I mustn't lose\x01",
            "consciousness again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B61")

    Jump("loc_50C6")

    label("loc_4B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C41")

    ChrTalk(
        0xB,
        (
            "According to police\x01",
            "intel, it's likely that\x01",
            "terrorists could show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, I don't want\x01",
            "to face such dangerous\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, Goddess of the Sky.\x01",
            "May this day end\x01",
            "peacefully...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CC1")

    label("loc_4C41")


    ChrTalk(
        0xB,
        (
            "Honestly, I don't want\x01",
            "to face dangerous guys\x01",
            "like terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, Goddess of the Sky.\x01",
            "May this day end\x01",
            "peacefully...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CC1")

    Jump("loc_50C6")

    label("loc_4CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0D")

    ChrTalk(
        0xB,
        (
            "Honestly, welcoming the\x01",
            "President's limousine\x01",
            "was nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm someone who gets nervous easily...\x01",
            "Even when I saluted, I have a feeling\x01",
            "I made some kind of strange pose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, the President probably won't\x01",
            "bother with a private like me, but...\x01",
            "Even so, it was a lot of pressure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EBB")

    label("loc_4E0D")


    ChrTalk(
        0xB,
        (
            "Welcoming the\x01",
            "President's limousine\x01",
            "was nerve-wracking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, the President probably won't\x01",
            "bother with a private like me, but...\x01",
            "Even so, it was a lot of pressure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBB")

    Jump("loc_50C6")

    label("loc_4EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF9")

    ChrTalk(
        0xB,
        (
            "My childhood friend Broude is\x01",
            "stationed at Bellguard Gate, which\x01",
            "guards the border with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I heard he finished\x01",
            "rehabilitation training without\x01",
            "difficulty the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was worried about him for a\x01",
            "while, but... I feel relieved\x01",
            "since he's completely recovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50C6")

    label("loc_4FF9")


    ChrTalk(
        0xB,
        (
            "I heard my childhood friend Broude\x01",
            "finished rehabilitation training\x01",
            "without difficulty the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was worried about him for a\x01",
            "while, but... I feel relieved\x01",
            "since he's completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C6")

    TalkEnd(0xFE)
    Return()

    # Function_16_43B0 end

    def Function_17_50CA(): pass

    label("Function_17_50CA")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50FC")
    SetScenarioFlags(0x31, 2)

    label("loc_50FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_513C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5131")
    Sound(2499, 255, 100, 0)
    Jump("loc_5137")

    label("loc_5131")

    Sound(3537, 255, 100, 0)

    label("loc_5137")

    Jump("loc_5142")

    label("loc_513C")

    Sound(3344, 255, 100, 0)

    label("loc_5142")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_51B7")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5197"),
        (SWITCH_DEFAULT, "loc_51A8"),
    )


    label("loc_5197")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_51B2")

    label("loc_51A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51B2")

    Jump("loc_53F4")

    label("loc_51B7")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_51E9")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_51E9")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_521D"),
        (1, "loc_5321"),
        (2, "loc_53B2"),
        (SWITCH_DEFAULT, "loc_53EA"),
    )


    label("loc_521D")

    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_524E")
    OP_70(0x6, 0x12C)
    OP_71(0x6, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_525E")

    label("loc_524E")

    OP_70(0x6, 0xF0)
    OP_71(0x6, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_525E")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52B4")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D7")
    Sound(461, 0, 100, 0)

    label("loc_52D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52F7")
    OP_70(0x6, 0x14A)
    OP_71(0x6, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_5307")

    label("loc_52F7")

    OP_70(0x6, 0x10E)
    OP_71(0x6, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_5307")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x6, "light", 0x1, 0x1)
    OP_70(0x6, 0x0)
    Jump("loc_5142")

    label("loc_5321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5393")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5356")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_536E")

    label("loc_5356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5369")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_536E")

    label("loc_5369")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_536E")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53AD")

    label("loc_5393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_53A3")
    OP_AF(0xFB)
    Jump("loc_53AD")

    label("loc_53A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53AD")

    Jump("loc_53F4")

    label("loc_53B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_53E5")

    label("loc_53CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_53DB")
    OP_AF(0xFB)
    Jump("loc_53E5")

    label("loc_53DB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E5")

    Jump("loc_53F4")

    label("loc_53EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53F4")

    Jump("loc_5142")

    label("loc_53F9")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_17_50CA end

    def Function_18_5407(): pass

    label("Function_18_5407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5457")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_5457")

    Call(0, 5)
    Return()

    # Function_18_5407 end

    def Function_19_545B(): pass

    label("Function_19_545B")

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

    def lambda_55C1():
        OP_96(0xFE, 0xFFFE2B40, 0xFFFFD8F0, 0xFFFF67A8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_55C1)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_545B end

    def Function_20_55F4(): pass

    label("Function_20_55F4")

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
        "#00005F#5PWhoops...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_5765():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5765)

    ChrTalk(
        0x102,
        (
            "#00105F#12PA call from another\x01",
            "department?\x02",
        )
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
            "#00000F#30WSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Husky Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehehe...... Hey\x01",
            "darling, it's me.\x02\x03",
            "Do you know who I am?\x02",
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
            "#00012FMichel... Um, what's up?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ahaha. You got me in one\x01",
            "shot! So skillful, you.\x02\x03",
            "Or was it love that led\x01",
            "you to my identity?\x02",
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
            "#00006FNo, it's just that you\x01",
            "were the only logical\x01",
            "choice to think of.\x02\x03",
            "#00000FBy any chance, is KeA\x01",
            "visiting you at the\x01",
            "Guild?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, about that.\x02\x03",
            "That child actually went to\x01",
            "Waterfront Area to play with\x01",
            "Shizuku.\x02\x03",
            "Zeit... I think he's called? They're\x01",
            "traveling together with that police\x01",
            "dog, so I think they'll be fine.\x02",
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
            "#00002FYeah, if they're with\x01",
            "Zeit, there shouldn't be\x01",
            "anything to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, really?\x02\x03",
            "I've heard about him, he\x01",
            "has such a strong\x01",
            "presence.\x02\x03",
            "As expected of the\x01",
            "legendary Divine Wolf,\x01",
            "wouldn't you say?\x02",
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
            "#00004FHaha... I think a\x01",
            "legendary wolf would be\x01",
            "quite different.\x02\x03",
            "#00005FSo, is this all you\x01",
            "wanted to tell us with\x01",
            "your call?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, no, let me get to the\x01",
            "point.\x02\x03",
            "Actually, it sounds like\x01",
            "Arios wants to exchange\x01",
            "information with you guys.\x02\x03",
            "He'll be back by this\x01",
            "evening, so could you make\x01",
            "some time for him?\x02",
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
            "#00000FThis evening...? That\x01",
            "should be fine.\x02\x03",
            "About the information\x01",
            "exchange, it's about the\x01",
            "trade conference, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That's correct, but it's\x01",
            "also... more about Heiyue\x01",
            "and Red Constellation.\x02",
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
            "#00003F...Got it.\x02\x03",
            "#00001FWhen we're finished with\x01",
            "our tasks, we'll make\x01",
            "sure to stop by.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Michel's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Great, I'll be waiting\x01",
            "for you.\x07\x00\x02",
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
            "#00100F#12PWas that Michel from the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PSomethin' come up?\x02",
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
        (
            "#00006F#5PNo, they want to\x01",
            "exchange information\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained Michel's\x01",
            "request to the other\x01",
            "members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#11PHeiyue and Red Constellation?\x02\x03",
            "#00301FIt's true that someone like ol'\x01",
            "Arios could be well informed\x01",
            "about matters out of state too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHehe, this could end up\x01",
            "helping us.\x02\x03",
            "#10300FSo, are we heading back\x01",
            "to Crossbell City now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PNo, Arios won't be back\x01",
            "until this evening.\x02\x03",
            "We should try to finish\x01",
            "up our requests before\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6252")

    ChrTalk(
        0x102,
        (
            "#00104F#12PWe gathered some basic\x01",
            "information about Red\x01",
            "Constellation, but...\x02\x03",
            "#00102FSince we have a car, it\x01",
            "might be best to visit\x01",
            "some other places too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62FD")

    label("loc_6252")


    ChrTalk(
        0x102,
        (
            "#00103F#12PWe haven't gathered that\x01",
            "much information about\x01",
            "Red Constellation, but...\x02\x03",
            "#00100FSince we have a car, it\x01",
            "might be best to visit\x01",
            "several different places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62FD")


    ChrTalk(
        0x109,
        (
            "#10100F#11PAlright, once we've finished our\x01",
            "business, let's head to the guild\x01",
            "branch office on East Street.\x02",
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

    # Function_20_55F4 end

    def Function_21_63A9(): pass

    label("Function_21_63A9")

    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_21_63A9 end

    def Function_22_63B9(): pass

    label("Function_22_63B9")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_22_63B9 end

    def Function_23_63CC(): pass

    label("Function_23_63CC")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_23_63CC end

    def Function_24_63DF(): pass

    label("Function_24_63DF")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_24_63DF end

    def Function_25_63F2(): pass

    label("Function_25_63F2")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_25_63F2 end

    def Function_26_6405(): pass

    label("Function_26_6405")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A9")
    Sleep(2500)
    SetChrPos(0x101, -53200, 0, 220, 90)
    SetChrPos(0x102, -54130, 0, -950, 90)
    SetChrPos(0x104, -54120, 0, 1520, 90)
    SetChrPos(0x109, -55800, 0, 1010, 90)
    SetChrPos(0x105, -56000, 0, -620, 90)

    def lambda_657B():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_657B)

    def lambda_6595():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6595)
    Sleep(100)

    def lambda_65A9():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65A9)

    def lambda_65C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65C3)
    Sleep(120)

    def lambda_65D7():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_65D7)

    def lambda_65F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_65F1)
    Sleep(90)

    def lambda_6605():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6605)

    def lambda_661F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_661F)
    Sleep(100)

    def lambda_6633():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6633)

    def lambda_664D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_664D)
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
    Jump("loc_69F9")

    label("loc_66A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686E")
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

    def lambda_6722():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6722)
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
    Jump("loc_69F9")

    label("loc_686E")

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

    def lambda_68E7():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_68E7)
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

    label("loc_69F9")


    ChrTalk(
        0x101,
        (
            "#00000FAlright, we've arrived\x01",
            "at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThis is where you were\x01",
            "stationed before your temporary\x01",
            "assignment with us, right Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, that's right.\x02\x03",
            "This border gate guards\x01",
            "Crossbell's border with\x01",
            "the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FCommander Douglas, the\x01",
            "new CGF vice commander,\x01",
            "has taken command, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FMr. Douglas, huh...\x01",
            "Haven't seen him in a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThere's that urgent\x01",
            "support request too...\x02\x03",
            "Let's pay a visit to the\x01",
            "Vice Commander's room on\x01",
            "2F.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1A")
    SetChrPos(0x0, -49550, 0, -310, 90)
    Jump("loc_6C4F")

    label("loc_6C1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C3E")
    SetChrPos(0x0, -35570, 0, 510, 90)
    Jump("loc_6C4F")

    label("loc_6C3E")

    SetChrPos(0x0, -30310, 0, 21020, 180)

    label("loc_6C4F")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_6405 end

    def Function_27_6C65(): pass

    label("Function_27_6C65")

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

    # Function_27_6C65 end

    def Function_28_6DEC(): pass

    label("Function_28_6DEC")

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
            "#11PThen, we'll now begin\x01",
            "the Douglas Method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PIs everyone ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PSquad leader Daimon and\x01",
            "company, ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSame for the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PGood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PAlso, in the battle that's about to\x01",
            "take place, use of arts by the Support\x01",
            "Section is strictly prohibited.\x02",
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

    def lambda_7124():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7124)
    Sleep(50)

    def lambda_7134():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7134)
    Sleep(50)

    def lambda_7144():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7144)
    Sleep(50)

    def lambda_7154():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7154)
    Sleep(50)

    def lambda_7164():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7164)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FW-Wait a minute!\x02\x03",
            "#00001FIt'll be too much of a\x01",
            "disadvantage if only we\x01",
            "can't use arts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FI see, so this is part\x01",
            "of the rumored Douglas\x01",
            "Method, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        "#11PPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PThis training program is to\x01",
            "test how you'll fight given\x01",
            "various disadvantages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PThe objective is to raise\x01",
            "your ability to deal with\x01",
            "various situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FI see. That "Demon"\x01",
            "nickname isn't just for\x01",
            "show.\x02\x03",
            "#10302FHehe... Things have\x01",
            "gotten interesting, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106F*sigh*... It seems we\x01",
            "have no choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_739D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_739D)
    Sleep(50)

    def lambda_73AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_73AD)
    Sleep(50)

    def lambda_73BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_73BD)
    Sleep(50)

    def lambda_73CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_73CD)
    Sleep(50)

    def lambda_73DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_73DD)
    Sleep(300)

    ChrTalk(
        0x14,
        "#11PAre you done talking?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#4S#11PThen... Everyone, in\x01",
            "position!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Troops",
        "#5P#4S#NSir!!\x02",
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
            "#12P#00003FOur opponents are CGF\x01",
            "members- combat pros. And we\x01",
            "can't use arts, either, huh.\x02\x03",
            "#00007FEveryone, don't let your\x01",
            "guard down! We'll find a way\x01",
            "out of this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FR-Roger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5S#11PBegin!!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4B0", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_6DEC end

    def Function_29_75D5(): pass

    label("Function_29_75D5")

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
        "#11PAlright, that's enough!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Ow... They got us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Even though you couldn't\x01",
            "use arts... You guys are\x01",
            "good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FLooks like we managed to\x01",
            "beat them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThere have been a few\x01",
            "times when we couldn't\x01",
            "use arts in battle...\x02\x03",
            "#00006FBut not being able to\x01",
            "use them from the start\x01",
            "like this was tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FI wonder if the orbal shutdown\x01",
            "phenomenon in Liberl a year\x01",
            "ago went something like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x14,
        (
            "#11PSo you've cleared stage\x01",
            "1 of the Douglas Method.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PContinuing to stage 2...\x01",
            "You'll fight with craft\x01",
            "use strictly prohibited.\x02",
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

    def lambda_7981():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7981)
    Sleep(50)

    def lambda_7991():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7991)
    Sleep(50)

    def lambda_79A1():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79A1)
    Sleep(50)

    def lambda_79B1():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79B1)
    Sleep(50)

    def lambda_79C1():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_79C1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00306FWhoa, there's more!?\x02\x03",
            "#00301FAnd crafts are\x01",
            "prohibited!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#11PDon't give me that. If\x01",
            "it's you guys, you'll\x01",
            "manage somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PIt'll be a good\x01",
            "experience for you. Come\x01",
            "on, give it a try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FVice Commander... You're\x01",
            "too strict...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#4S#11PAlright! CGF members in\x01",
            "formation! Teams,\x01",
            "prepare for battle!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    def lambda_7B3F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B3F)
    Sleep(50)

    def lambda_7B4F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B4F)
    Sleep(50)

    def lambda_7B5F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B5F)
    Sleep(50)

    def lambda_7B6F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B6F)
    Sleep(50)

    def lambda_7B7F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B7F)
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
        "Troops",
        "#4S#NSir!!\x02",
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
            "#12P#00003FUgh. Honestly, not being\x01",
            "able to use crafts will\x01",
            "be really tough, but...\x02\x03",
            "#00007FSomehow, we'll fight\x01",
            "using arts and normal\x01",
            "attacks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5S#11PBegin!!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4F4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_29_75D5 end

    def Function_30_7D37(): pass

    label("Function_30_7D37")

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
        "#11PYes, that's enough!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ugh, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "No way, they're that\x01",
            "good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FPhew! That sure was\x01",
            "tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah... I understand\x01",
            "just how important\x01",
            "crafts are in battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FWell, we got through it,\x01",
            "so it's all good.\x02\x03",
            "#00301FHow 'bout that? You've\x01",
            "got no complaints,\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PHaha, I see. You have\x01",
            "certainly grown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PIn that case... We move\x01",
            "to the 3rd stage of the\x01",
            "Douglas Method!\x02",
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
            "#5S#5POn your feet, CGF! This\x01",
            "is the final training!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Troops",
        "#5S#NSir!\x02",
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
        "#12P#00101FThat's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHmph... He seems\x01",
            "skilled, just like I've\x01",
            "heard.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)

    ChrTalk(
        0x101,
        (
            "#12P#00003FDemon Douglas... As the\x01",
            "CGF's strongest, his title\x01",
            "isn't just for show.\x02\x03",
            "#00007FEveryone, don't let your\x01",
            "guard down even for an\x01",
            "instant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHahaha, it seems you're\x01",
            "quite used to your\x01",
            "position as leader, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P...Then, this is the\x01",
            "conclusion of today's\x01",
            "training, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5S#5PUse all your might\x01",
            "and... Try to defeat me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FHeh, fine by me!\x02",
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

    # Function_30_7D37 end

    def Function_31_83A0(): pass

    label("Function_31_83A0")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D3")
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
        "#12P#00002FW-We did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI-Impossible... To think\x01",
            "that the Vice Commander\x01",
            "has...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHmph... You're quite\x01",
            "good, eh?\x02",
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
            "#12P#00305F...Looks like he didn't\x01",
            "feel that at all.\x02\x03",
            "#00306FTch, tough as always,\x01",
            "I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PNo, I felt it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PIt's just, stamina has been my\x01",
            "one and only strong point for\x01",
            "as long as I can remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109FH-How modest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FThat was impressive,\x01",
            "Vice Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FOh man. Hats off to you,\x01",
            "sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PVery well then. That's\x01",
            "all for today's\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x2)
    Jump("loc_88E8")

    label("loc_86D3")

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
            "#12P#00003FUgh! We couldn't do it,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FTo think we couldn't win\x01",
            "even with arts and\x01",
            "crafts...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#12P#00301FTch. He's got a lot of\x01",
            "energy for a man his\x01",
            "age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHehe. I've got a lot\x01",
            "more active duty service\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PAlthough I think you all\x01",
            "did your best, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FWiped out, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FThat's the CGF's Vice\x01",
            "Commander for you, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PVery well then. That's\x01",
            "all for today's\x01",
            "training.\x02",
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

    label("loc_88E8")

    TurnDirection(0x14, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#11PAll members, return to\x01",
            "your posts and resume\x01",
            "your duties.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8957")
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_895D")

    label("loc_8957")

    Sound(802, 0, 100, 0)

    label("loc_895D")

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
        "Troops",
        "#4S#NSir!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x14, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#5PYou guys too. Good work\x01",
            "out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PRather than stand here\x01",
            "and talk, let's return\x01",
            "to my office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FY-Yes, sir.\x02",
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

    # Function_31_83A0 end

    def Function_32_8A59(): pass

    label("Function_32_8A59")

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

    def lambda_8B12():
        OP_95(0x101, -42000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B12)
    Sleep(30)

    def lambda_8B2F():
        OP_95(0x102, -42500, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B2F)
    Sleep(40)

    def lambda_8B4C():
        OP_95(0x104, -42500, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8B4C)
    Sleep(800)

    def lambda_8B69():
        OP_95(0x109, -44100, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8B69)
    Sleep(30)

    def lambda_8B86():
        OP_95(0x103, -43800, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8B86)
    Sleep(10)

    def lambda_8BA3():
        OP_95(0x105, -43800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8BA3)
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
            "#00000FWell then... I wonder if\x01",
            "the black transport\x01",
            "arrived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI don't see it outdoors,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt could already be\x01",
            "inside going through\x01",
            "customs procedures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThat seems likely. Although\x01",
            "it came, it took us quite a\x01",
            "bit of time to get here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FL-Let's go confirm it\x01",
            "quick!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh man. I hope we've\x01",
            "made it in time...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D54():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D54)
    Sleep(30)

    def lambda_8D71():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D71)
    Sleep(40)

    def lambda_8D8E():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8D8E)
    Sleep(30)

    def lambda_8DAB():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8DAB)
    Sleep(30)

    def lambda_8DC8():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8DC8)
    Sleep(10)

    def lambda_8DE5():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8DE5)
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

    # Function_32_8A59 end

    def Function_33_8E26(): pass

    label("Function_33_8E26")

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
            "#00000FWell then... I wonder if\x01",
            "the black transport\x01",
            "arrived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI don't see it outdoors,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt could already be\x01",
            "inside going through\x01",
            "customs procedures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThat seems likely. It took\x01",
            "us quite a bit of time for\x01",
            "the bus to arrive, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FL-Let's go confirm it\x01",
            "quick!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh man. I hope we've\x01",
            "made it in time...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_905A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_905A)
    Sleep(30)

    def lambda_906A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_906A)
    Sleep(40)

    def lambda_907A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_907A)
    Sleep(30)

    def lambda_908A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_908A)
    Sleep(30)

    def lambda_909A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_909A)
    Sleep(10)

    def lambda_90AA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_90AA)
    WaitChrThread(0x109, 2)

    def lambda_90BB():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_90BB)
    WaitChrThread(0x104, 2)

    def lambda_90D9():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90D9)
    WaitChrThread(0x103, 2)

    def lambda_90F7():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_90F7)
    WaitChrThread(0x102, 2)

    def lambda_9115():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9115)
    WaitChrThread(0x105, 2)

    def lambda_9133():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9133)
    WaitChrThread(0x101, 2)

    def lambda_9151():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9151)
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

    # Function_33_8E26 end

    def Function_34_9192(): pass

    label("Function_34_9192")

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

    def lambda_924B():
        OP_96(0x12, 0xFFFF5BF0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_924B)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(492, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_71(0x6, 0x5B, 0x78, 0x1, 0x8)
    StopSound(459, 1000, 90)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThat's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FLooks like we found him.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_947E")

    ChrTalk(
        0x18,
        (
            "Hehe... Now that I've\x01",
            "arrived here, I can rest\x01",
            "easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "All that's left is to\x01",
            "unload these medical\x01",
            "supplies in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Remiferian medical\x01",
            "goods... They should fetch\x01",
            "a fair bit of mira...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9584")

    label("loc_947E")


    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "Hehe... Now that I've\x01",
            "arrived here, I can rest\x01",
            "easy.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "All that's left is to\x01",
            "unload these medical\x01",
            "supplies in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "Remiferian medical\x01",
            "goods... They should fetch\x01",
            "a fair bit of mira...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9584")


    ChrTalk(
        0x101,
        "#00007F─We won't let you!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(-25430, 1000, -10970, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(21210, 3000)

    def lambda_95EF():
        OP_95(0x101, -26500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95EF)

    def lambda_9609():
        OP_95(0x102, -26230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9609)

    def lambda_9623():
        OP_95(0x103, -26500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9623)

    def lambda_963D():
        OP_95(0x104, -27950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_963D)

    def lambda_9657():
        OP_95(0x105, -27550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9657)

    def lambda_9671():
        OP_95(0x109, -27550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9671)
    WaitChrThread(0x101, 1)

    def lambda_968F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_968F)
    WaitChrThread(0x102, 1)

    def lambda_96A0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_96A0)
    WaitChrThread(0x103, 1)

    def lambda_96B1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_96B1)
    WaitChrThread(0x104, 1)

    def lambda_96C2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_96C2)
    WaitChrThread(0x105, 1)

    def lambda_96D3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_96D3)
    WaitChrThread(0x109, 1)

    def lambda_96E4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_96E4)
    OP_93(0x18, 0x10E, 0x1F4)
    WaitChrThread(0x109, 2)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9A39")

    ChrTalk(
        0x18,
        "You guys!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMinneth... I had a\x01",
            "feeling, but it really\x01",
            "was you, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYou're suspected of\x01",
            "theft of medical goods\x01",
            "at the airport.\x02\x03",
            "#00101FWe're very sorry, but\x01",
            "could you show us your\x01",
            "cargo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "...Hmph, I did too rough\x01",
            "a job because I was in\x01",
            "hurry, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, indeed. Compared to when\x01",
            "we met at Armorica Village,\x01",
            "your technique is lacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "...Because of you bastards, my\x01",
            "job at Armorica Village failed\x01",
            "and I'm even a wanted man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "If I didn't earn at least\x01",
            "this pocket money, my\x01",
            "business would be doomed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHah! There's a bigger\x01",
            "reason, isn't there.\x02\x03",
            "#00301FWe know you're a supplier\x01",
            "or fundraiser for Red\x01",
            "Constellation.\x02\x03",
            "Because they did what they\x01",
            "did here in Crossbell, you\x01",
            "can't stay here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "...Hehe, I'll leave that\x01",
            "to your imagination.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x5)
    Jump("loc_9DD7")

    label("loc_9A39")


    NpcTalk(
        0x18,
        "Trader-looking Man",
        "Oh, and you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FCrossbell Police, Special\x01",
            "Support Section.\x02\x03",
            "We're terribly sorry, but\x01",
            "could you tell us your\x01",
            "name and occupation?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "Hmm... Police officers,\x01",
            "huh? Excuse my rudeness.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "My name is Minneth... I\x01",
            "am a humble trader of\x01",
            "Imperial origin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "I am about to depart for\x01",
            "business in the Republic... Do\x01",
            "you need something from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh man, actin' as if\x01",
            "nothin' happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYou're suspected of\x01",
            "theft of medical goods\x01",
            "at the airport.\x02\x03",
            "#00101FWe're very sorry, but\x01",
            "could you show us your\x01",
            "cargo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Hmm. I do indeed have\x01",
            "medical goods stocked in\x01",
            "this transport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "However, this cargo was\x01",
            "mine from the start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "I wonder if you have any\x01",
            "proof that I stole them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe, he thinks he can play\x01",
            "innocent.\x02\x03",
            "#10302FIf we check with Ricardo, I\x01",
            "don't think you'd be able to\x01",
            "talk your way out of this one.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x6)

    label("loc_9DD7")


    ChrTalk(
        0x103,
        (
            "#00203F...Time is short. Let's\x01",
            "take him away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... Seems like\x01",
            "that's our only option.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Ohh, scary, scary. What\x01",
            "a group of savages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "If that's the case... I\x01",
            "have no choice but to\x01",
            "run, do I.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sound(464, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x3C, 0x1, 0x8)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(500)

    def lambda_9EDA():
        OP_95(0x18, -23800, 0, -11450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9EDA)
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

    def lambda_9F94():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9F94)
    OP_95(0x18, -23000, 600, -11450, 2000, 0x0)

    ChrTalk(
        0x101,
        "#00007F#11AW-Wait...!\x02",
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

    def lambda_A025():
        OP_95(0x101, -23500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A025)

    def lambda_A03F():
        OP_95(0x102, -23230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A03F)

    def lambda_A059():
        OP_95(0x103, -23500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A059)

    def lambda_A073():
        OP_95(0x104, -24950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A073)

    def lambda_A08D():
        OP_95(0x105, -24550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A08D)

    def lambda_A0A7():
        OP_95(0x109, -24550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A0A7)
    WaitChrThread(0x109, 1)

    def lambda_A0C5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A0C5)

    def lambda_A0D2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A0D2)

    def lambda_A0DF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A0DF)

    def lambda_A0EC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A0EC)

    def lambda_A0F9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A0F9)

    def lambda_A106():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A106)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10107FLloyd, let's chase him\x01",
            "with our orbal car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRight!\x02",
    )

    CloseMessageWindow()

    def lambda_A160():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A160)
    Sleep(50)

    def lambda_A170():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A170)
    Sleep(50)

    def lambda_A180():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A180)
    Sleep(50)

    def lambda_A190():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A190)
    Sleep(50)

    def lambda_A1A0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A1A0)
    Sleep(50)

    def lambda_A1B0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A1B0)
    WaitChrThread(0x101, 1)

    def lambda_A1C1():
        OP_95(0x101, -32250, 0, -8230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1C1)
    WaitChrThread(0x102, 1)

    def lambda_A1DF():
        OP_95(0x102, -31980, 0, -6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1DF)
    WaitChrThread(0x103, 1)

    def lambda_A1FD():
        OP_95(0x103, -31690, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A1FD)
    WaitChrThread(0x104, 1)

    def lambda_A21B():
        OP_95(0x104, -33590, 0, -6950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A21B)
    WaitChrThread(0x105, 1)

    def lambda_A239():
        OP_95(0x105, -33500, 0, -5480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A239)
    WaitChrThread(0x109, 1)

    def lambda_A257():
        OP_95(0x109, -33500, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A257)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetScenarioFlags(0x22, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_9192 end

    def Function_35_A28C(): pass

    label("Function_35_A28C")

    SetChrPos(0xFE, -22290, 0, -12240, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -24290, 0, -4000)
    OP_9F(0x1, -23290, 0, -2000)
    OP_9F(0x1, -21000, 0, 0)
    OP_9F(0x1, -18290, 0, 0)
    OP_9F(0x1, 290, 0, 0)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_35_A28C end

    def Function_36_A2F1(): pass

    label("Function_36_A2F1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Calvard Republic Region National Border\x01",
            "                   Tangram Gate\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_A2F1 end

    SaveToFile()

Try(main)
