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
        "Function_5_11BF",         # 05, 5
        "Function_6_12C2",         # 06, 6
        "Function_7_13EF",         # 07, 7
        "Function_8_1440",         # 08, 8
        "Function_9_14D4",         # 09, 9
        "Function_10_2441",        # 0A, 10
        "Function_11_32A1",        # 0B, 11
        "Function_12_33DE",        # 0C, 12
        "Function_13_357B",        # 0D, 13
        "Function_14_36B3",        # 0E, 14
        "Function_15_37F3",        # 0F, 15
        "Function_16_44A3",        # 10, 16
        "Function_17_525F",        # 11, 17
        "Function_18_5598",        # 12, 18
        "Function_19_55EC",        # 13, 19
        "Function_20_5785",        # 14, 20
        "Function_21_6553",        # 15, 21
        "Function_22_6563",        # 16, 22
        "Function_23_6576",        # 17, 23
        "Function_24_6589",        # 18, 24
        "Function_25_659C",        # 19, 25
        "Function_26_65AF",        # 1A, 26
        "Function_27_6E63",        # 1B, 27
        "Function_28_6FEA",        # 1C, 28
        "Function_29_7870",        # 1D, 29
        "Function_30_8010",        # 1E, 30
        "Function_31_86AF",        # 1F, 31
        "Function_32_8D8B",        # 20, 32
        "Function_33_9148",        # 21, 33
        "Function_34_94AF",        # 22, 34
        "Function_35_A648",        # 23, 35
        "Function_36_A6AD",        # 24, 36
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1164")

    Jump("loc_11B3")

    label("loc_1169")

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

    label("loc_11B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_106D end

    def Function_5_11BF(): pass

    label("Function_5_11BF")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City East Entrance\x01",      # 0
            "Tangram Gate\x01",                      # 1
            "Bus Stop (Fork in the Road)\x01",       # 2
            "Quit\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1275")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12BA")

    label("loc_1275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129A")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12BA")

    label("loc_129A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BA")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_12BA")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_5_11BF end

    def Function_6_12C2(): pass

    label("Function_6_12C2")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_13EB")
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

    def lambda_13A2():
        OP_98(0xFE, 0x0, 0x0, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13A2)
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

    label("loc_13EB")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_6_12C2 end

    def Function_7_13EF(): pass

    label("Function_7_13EF")

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

    # Function_7_13EF end

    def Function_8_1440(): pass

    label("Function_8_1440")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1490")
    Sound(2502, 255, 100, 0)
    Jump("loc_1496")

    label("loc_1490")

    Sound(2503, 255, 100, 0)

    label("loc_1496")

    Jump("loc_14BF")

    label("loc_149B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14B9")
    Sound(3347, 255, 100, 0)
    Jump("loc_14BF")

    label("loc_14B9")

    Sound(3348, 255, 100, 0)

    label("loc_14BF")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1440 end

    def Function_9_14D4(): pass

    label("Function_9_14D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1658")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Soldier Nowe",
        (
            "Y-You guys...!\x01",
            "...Wait, there was no more\x01",
            "need to arrest you, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Nowe",
        (
            "*sigh*, in the end, we State\x01",
            "Guard didn't do anything.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Nowe",
        (
            "Even the unappreciated CGF\x01",
            "finally had its pride.\x01",
            "I was feeling that, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Nowe",
        (
            "Somehow it's like they made \x01",
            "me see a long, long dream...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16ED")

    label("loc_1658")


    NpcTalk(
        0x8,
        "Soldier Nowe",
        (
            "*sigh*, in the end, we State\x01",
            "Guard didn't do anything.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Nowe",
        (
            "Somehow it's like they made \x01",
            "me see a long, long dream...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16ED")

    Jump("loc_243D")

    label("loc_16F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180F")

    ChrTalk(
        0x8,
        (
            "The conditions of all the members hospitalised\x01",
            "at St. Ursula seem to be unpredictable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Man, they were luckier than...\x01",
            "The comrades who died on the mountain path...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm normally moderate, however...\x01",
            "Just this time, I can't control my anger.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18A9")

    label("loc_180F")


    ChrTalk(
        0x8,
        (
            "I'm normally moderate, however...\x01",
            "Just this time, I can't control my anger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Red Constellation... One day,\x01",
            "we'll pay you back for this for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A9")

    Jump("loc_243D")

    label("loc_18AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CD")

    ChrTalk(
        0x8,
        (
            "Yesterday West Crossbell Highway accident\x01",
            "was expected to have quite an effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they hadn't finished the repairs,\x01",
            "it's likely the Empire and Republic\x01",
            "would've meddled with the local referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I want to praise the unit that did the repairs.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A8A")

    label("loc_19CD")


    ChrTalk(
        0x8,
        (
            "If the accident repairs hadn't been finished,\x01",
            "it's likely that the Empire and Republic\x01",
            "would've meddled with the local referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I want to praise the unit that did the repairs.\x02",
    )

    CloseMessageWindow()

    label("loc_1A8A")

    Jump("loc_243D")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA6")

    ChrTalk(
        0x8,
        (
            "The autonomous state of Crossbell\x01",
            "pays 10% of revenues to the\x01",
            "Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If the system was abolished\x01",
            "by the national independence,\x01",
            "the budget would rise a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that happened, I wonder if they\x01",
            "would strengthen the CGF first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C61")

    label("loc_1BA6")


    ChrTalk(
        0x8,
        (
            "If the system where we pay 10% revenues\x01",
            "were crushed by the independence,\x01",
            "the budget would rise a lot, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that happened, I wonder if they\x01",
            "would strengthen the CGF first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C61")

    Jump("loc_243D")

    label("loc_1C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(
        0x8,
        (
            "The autonomous state of Crossbell\x01",
            "exists in a geographic terrain caught\x01",
            "in between the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In other words, that independence proposal\x01",
            "is equal to have declared a confrontation\x01",
            "in the midst of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking about it,\x01",
            "the mayor did a\x01",
            "drastic thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E3A")

    label("loc_1D99")


    ChrTalk(
        0x8,
        (
            "The independence proposal at the Trade\x01",
            "Conference was equal to have declared\x01",
            "a confrontation in the midst of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, the mayor\x01",
            "did a drastic thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3A")

    Jump("loc_243D")

    label("loc_1E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F70")

    ChrTalk(
        0x8,
        (
            "Republican terrorists\x01",
            "are entering Crossbell...\x01",
            "It seems there's intel like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Terrorism isn't anything calm.\x01",
            "If they want to carry their own opinions,\x01",
            "they should think more about other methods...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Wait, even if I say something\x01",
            "like this, there's no point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2030")

    label("loc_1F70")


    ChrTalk(
        0x8,
        (
            "Republican terrorists\x01",
            "are entering Crossbell...\x01",
            "It seems there's intel like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As for terrorist acts,\x01",
            "I can think about many things, but...\x01",
            "For now, we have to focus on security.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2030")

    Jump("loc_243D")

    label("loc_2035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2123")

    ChrTalk(
        0x8,
        (
            "This morning, President Rocksmith's\x01",
            "white limousine passed through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've been quite busy with the\x01",
            "reception and traffic control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We really need to pay attention\x01",
            "when a VIP enters the state.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21DE")

    label("loc_2123")


    ChrTalk(
        0x8,
        (
            "Due to the reception of President Rocksmith's \x01",
            "limousine and the traffic control,\x01",
            "we were pretty busy this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We really need to pay attention\x01",
            "when a VIP enters the state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DE")

    Jump("loc_243D")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_243D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2289")

    ChrTalk(
        0x8,
        (
            "Maaan, thanks to you,\x01",
            "it was a nice practice.\x01",
            "You're quite good too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If chance permits it again,\x01",
            "let's have another sparring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243D")

    label("loc_2289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238B")

    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas who\x01",
            "was newly appointed to Tangram\x01",
            "is a pretty sociable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd dare to say as an example that he's\x01",
            "like the big bro everyone can count on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Although when it comes\x01",
            "to work, he's extremely strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_243D")

    label("loc_238B")


    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas\x01",
            "is a pretty sociable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd dare to say as an example that he's\x01",
            "like the big bro everyone can count on.\x01",
            "...Although he's strict on the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243D")

    TalkEnd(0xFE)
    Return()

    # Function_9_14D4 end

    def Function_10_2441(): pass

    label("Function_10_2441")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AC")

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Due to the appearance of that azure\x01",
            "pale tree, the Republican Army seems\x01",
            "to be on a wait-and-see attitude for now, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Now that we've lost the barrier and the "Aions",\x01",
            "we must be on guard.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Only us State Guard can\x01",
            "defend Crossbell now.\x01",
            "We have to be on a strict lookout.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_269F")

    label("loc_25AC")


    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Due to the appearance of that azure\x01",
            "pale tree, the Republican Army seems\x01",
            "to be on a wait-and-see attitude for now, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Daimon",
        (
            "Only us State Guard can\x01",
            "defend Crossbell now.\x01",
            "We have to be on a strict lookout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269F")

    Jump("loc_329D")

    label("loc_26A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FA")

    ChrTalk(
        0x9,
        (
            "Not having being able to defend against the\x01",
            "attack to Crossbell was our CGF obvious failure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Due to the Mainz occupation incident,\x01",
            "our war potential was reduced, but...\x01",
            "Such a thing is nothing more than an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As an organization that maintains public order...\x01",
            "Maybe we should revise many things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B7")

    label("loc_27FA")


    ChrTalk(
        0x9,
        (
            "Not having being able to defend against the\x01",
            "attack to Crossbell was our CGF obvious failure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As an organization that maintains public order...\x01",
            "Maybe we should revise many things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B7")

    Jump("loc_329D")

    label("loc_28BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_295C")

    ChrTalk(
        0x9,
        (
            "Just before, a male Bracer\x01",
            "was inquiring around...\x01",
            "It seems female Bracers have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hm...I hope nothing has happened to them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_295C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A06")

    ChrTalk(
        0x9,
        (
            "The Bracers too seem to be\x01",
            "searching in many places\x01",
            "running after a "Cryptid".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, they know well\x01",
            "the backwood areas\x01",
            "where we can't enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_2A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2F")

    ChrTalk(
        0x9,
        (
            "If it happens that a "Cryptid"\x01",
            "were to hurt a foreigner, the two\x01",
            "major powers would use that for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it's straightly tied with the\x01",
            "national borders state of tension too,\x01",
            "it's a problem the CGF can't overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We're counting on you for the search.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B9E")

    label("loc_2B2F")


    ChrTalk(
        0x9,
        (
            "The Cryptids problem is something\x01",
            "even the CGF can't overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We're counting on you for the search.\x02",
    )

    CloseMessageWindow()

    label("loc_2B9E")

    Jump("loc_329D")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2C46")

    ChrTalk(
        0x9,
        (
            "Regarding the terrorists,\x01",
            "we too are guarding with\x01",
            "all our resources.\x02",
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
    Jump("loc_329D")

    label("loc_2C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2CF8")

    ChrTalk(
        0x9,
        (
            "President Rocksmith is said to\x01",
            "be supported by the Republican\x01",
            "citizens as the common people faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Really, I wonder what sort\x01",
            "of man is he in practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_2CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_329D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E03")

    ChrTalk(
        0x9,
        (
            "You had Sergeant Noｱl with you, but\x01",
            "to think you could fight such a good \x01",
            "fight against Vice Commander Douglas...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As expected from the Cult incident centre\x01",
            "figure, the Special Support Section, I guess?\x01",
            "Honestly, you did very well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_2E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3119")

    ChrTalk(
        0x9,
        (
            "Master Sergeant Noｱl, thank you for your hard work!\x01",
            "............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThank you too, Mr. Daimon.\x01",
            "...Ehm, is something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Hm, how to say it...\x01",
            "I was thinking that was somehow refreshing seeing\x01",
            "the Master Sergeant not wearing the CGF uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FAh, now that I think about it, it could \x01",
            "be the first time I'm going around \x01",
            "Tangram Gate in this outfit...\x02\x03",
            "#10112FI'm sorry, maybe I was\x01",
            "a bit inconsiderate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "N-No.\x01",
            "I think it's very nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAh aah, then....\x01",
            "You fluttered because of Noｱl in an \x01",
            "outfit you're not used to see her in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FEh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "N-No, that's not that.\x01",
            "Absolutely not that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...P-Pardon me.\x01",
            "Please forget it, Master Sergeant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(D-Damn you, senior Randy.\x01",
            "It's embarrassing, jeez...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 7)
    Jump("loc_329D")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3208")

    ChrTalk(
        0x9,
        (
            "...Honestly, I was too shaken\x01",
            "just by different garments.\x01",
            "I'm lacking in training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm extremely sorry.\x01",
            "Master Sergeant, please forget it.\x02",
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
    Jump("loc_329D")

    label("loc_3208")


    ChrTalk(
        0x9,
        (
            "...Honestly, I was too shaken\x01",
            "just by different garments.\x01",
            "I'm lacking in training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm extremely sorry.\x01",
            "Master Sergeant, please forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329D")

    TalkEnd(0xFE)
    Return()

    # Function_10_2441 end

    def Function_11_32A1(): pass

    label("Function_11_32A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3374")

    ChrTalk(
        0xC,
        "I met these people at the city east exit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since they said they wanted to go \x01",
            "to Tangram Gate, I took them\x01",
            "along as bodyguards, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Honestly, they were useless.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33DA")

    label("loc_3374")


    ChrTalk(
        0xC,
        (
            "Even so, walking on the\x01",
            "highway was quite thrilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Maybe I'll go to Armorica Village now.\x02",
    )

    CloseMessageWindow()

    label("loc_33DA")

    TalkEnd(0xFE)
    Return()

    # Function_11_32A1 end

    def Function_12_33DE(): pass

    label("Function_12_33DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F5")

    ChrTalk(
        0xD,
        (
            "*pant, pant*...\x01",
            "When we encountered a Cryptid on the way,\x01",
            "I didn't know what would've happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I-In any case, we managed to get here.\x01",
            "What remains is only to go back to the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "W-We'll be able to go back, right...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3577")

    label("loc_34F5")


    ChrTalk(
        0xD,
        (
            "I had never been treated like\x01",
            "this since I was born...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I-I wonder if we'll be really able\x01",
            "to go back to the Republic...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3577")

    TalkEnd(0xFE)
    Return()

    # Function_12_33DE end

    def Function_13_357B(): pass

    label("Function_13_357B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_36AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365B")

    ChrTalk(
        0xE,
        (
            "*hanf, hanf*...\x01",
            "A-Although it's a safe road for sure,\x01",
            "I took it for granted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Who could've thought to get stuck with\x01",
            "doing a marathon on the highway...\x01",
            "I-I thought I was gonna die...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_36AF")

    label("loc_365B")


    ChrTalk(
        0xE,
        (
            "Uuh, why did this\x01",
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

    label("loc_36AF")

    TalkEnd(0xFE)
    Return()

    # Function_13_357B end

    def Function_14_36B3(): pass

    label("Function_14_36B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B6")

    ChrTalk(
        0xF,
        (
            "Although the barrier dissolved,\x01",
            "we didn't have a car, you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "After we were guided here by\x01",
            "a girl we met by coincidence,\x01",
            "now there's this bothersome stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "A-As expected, hitch-hiking\x01",
            "would've been better...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_37EF")

    label("loc_37B6")


    ChrTalk(
        0xF,
        (
            "A-As expected, hitch-hiking\x01",
            "would've been better...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EF")

    TalkEnd(0xFE)
    Return()

    # Function_14_36B3 end

    def Function_15_37F3(): pass

    label("Function_15_37F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3963")

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "As per the Vice Commander's orders,\x01",
            "vigilance of the Republic region\x01",
            "still goes on, however...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "It was because we had the "Aions" power that we\x01",
            "could repel the two major powers' armies before.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "The next time they'll come to invade...\x01",
            "We probably won't be able to stop them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A2C")

    label("loc_3963")


    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "Because we had the "Aions" power\x01",
            "we could repel the army before.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Soldier Garrison",
        (
            "The next time they Republican Army comes to invade...\x01",
            "We probably won't be able to stop it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A2C")

    Jump("loc_449F")

    label("loc_3A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2C")

    ChrTalk(
        0xA,
        (
            "Because we received heavy damage from\x01",
            "the jaeger corps, the CGF has crumbled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If I was told to fight again against those guys,\x01",
            "honestly, I'd end up running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder how we should \x01",
            "proceed from now on...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BBB")

    label("loc_3B2C")


    ChrTalk(
        0xA,
        (
            "If I was told to fight again against jaeger corps,\x01",
            "honestly, I'd end up running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder how we should \x01",
            "proceed from now on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BBB")

    Jump("loc_449F")

    label("loc_3BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6F")

    ChrTalk(
        0xA,
        "......*atchooo*!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...I guess my body has\x01",
            "chilled down a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It wouldn't be good if I got a cold.\x01",
            "Maybe I should rest a little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D1D")

    label("loc_3C6F")


    ChrTalk(
        0xA,
        (
            "My body has chilled down a \x01",
            "little so I guess I'll go take a \x01",
            "short rest at the mess hall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In this state of tension, getting\x01",
            "your health ruined wouldn't be good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1D")

    Jump("loc_449F")

    label("loc_3D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3B")

    ChrTalk(
        0xA,
        (
            "At present, it's ambiguous whether\x01",
            "Tangram Hill is Crossbell or\x01",
            "Republic territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As a matter of fact, nowadays it's\x01",
            "Republic possession, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If Crossbell were to become\x01",
            "independent, it seems that the\x01",
            "dispute would go on for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EF6")

    label("loc_3E3B")


    ChrTalk(
        0xA,
        (
            "At present, it's ambiguous whether\x01",
            "Tangram Hill is Crossbell or\x01",
            "Republic territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even though the independence was realized,\x01",
            "it seems that the dispute will go on for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EF6")

    Jump("loc_449F")

    label("loc_3EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4023")

    ChrTalk(
        0xA,
        (
            "As the local referendum day gets closer, even\x01",
            "the pressure becomes stronger day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that the Republic citizens are showing\x01",
            "dissenting opinions about the Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I pray they not grow into open\x01",
            "movements and policies too much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40D3")

    label("loc_4023")


    ChrTalk(
        0xA,
        (
            "It seems that the Republic citizens are showing\x01",
            "dissenting opinions about the Crossbell independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I pray they not grow into open\x01",
            "movements and policies too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D3")

    Jump("loc_449F")

    label("loc_40D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4201")

    ChrTalk(
        0xA,
        (
            "As you can see, Tangram Hill \x01",
            "commands a fine view and\x01",
            "also has monitoring facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We can immediately know if there're\x01",
            "airships or vehicles coming from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Of course, it's not so easy, but...\x01",
            "Don't worry, we'll never allow\x01",
            "the entry of terrorists.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42BE")

    label("loc_4201")


    ChrTalk(
        0xA,
        (
            "As you can see, Tangram Hill \x01",
            "commands a fine view and\x01",
            "also has monitoring facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Of course, it's not so easy, but...\x01",
            "Don't worry, we'll never allow\x01",
            "the entry of terrorists.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BE")

    Jump("loc_449F")

    label("loc_42C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_437B")

    ChrTalk(
        0xA,
        (
            "President Rocksmith's limousine is\x01",
            "guarded by many escort vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As expected from the President who governs\x01",
            "the Republic...that scene was truly a spectacle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_449F")

    label("loc_437B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_449F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443E")

    ChrTalk(
        0xA,
        (
            "Tangram Hill spreading all around...\x01",
            "It's a very nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Historically, it's said it was the\x01",
            "stage of many a battle, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I quite love this scenery.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_449F")

    label("loc_443E")


    ChrTalk(
        0xA,
        (
            "Tangram Hill spreading all around...\x01",
            "It's a very nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I quite love this scenery.\x02",
    )

    CloseMessageWindow()

    label("loc_449F")

    TalkEnd(0xFE)
    Return()

    # Function_15_37F3 end

    def Function_16_44A3(): pass

    label("Function_16_44A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BD")

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "That mysterious tree...\x01",
            "I'm sure it can be seen from\x01",
            "everywhere in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "Such a thing appearing all of a sudden...\x01",
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
    Jump("loc_4670")

    label("loc_45BD")


    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "A mysterious tree...\x01",
            "Such a thing appearing all of a sudden...\x01",
            "That's not normal at all.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Burrell",
        (
            "I wonder if Broude at\x01",
            "Bellguard Gate is fine...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4670")

    Jump("loc_525B")

    label("loc_4675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4839")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A1")

    ChrTalk(
        0xB,
        (
            "It seems that Broude, my\x01",
            "childhood friend who is at\x01",
            "Bellguard Gate, was fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Still, I can't feel at ease.\x01",
            "What the CGF has lost\x01",
            "is really huge, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Frankly speaking, I'm scared about\x01",
            "what will happen from now on, but...\x01",
            "I can only prepare myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4834")

    label("loc_47A1")


    ChrTalk(
        0xB,
        (
            "What the CGF has\x01",
            "lost is really huge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Frankly speaking, I'm scared about\x01",
            "what will happen from now on, but...\x01",
            "I can only prepare myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4834")

    Jump("loc_525B")

    label("loc_4839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496E")

    ChrTalk(
        0xB,
        (
            "Today, it seems that the radar\x01",
            "facility is operating at full power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When it rains, it's difficult to tell\x01",
            "the sky condition by eyesight.\x01",
            "Quite handy for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was broken at the time of the Trade Conference,\x01",
            "but it's properly serving its purpose now, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A10")

    label("loc_496E")


    ChrTalk(
        0xB,
        (
            "The radar facility is quite\x01",
            "handy for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was broken at the time of the Trade Conference,\x01",
            "but it's properly serving its purpose now, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A10")

    Jump("loc_525B")

    label("loc_4A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4AA8")

    ChrTalk(
        0xB,
        (
            "Vice Commander Douglas is sociable and,\x01",
            "despite the appearances, a pretty cool man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "If only I too could become like him...\x02",
    )

    CloseMessageWindow()
    Jump("loc_525B")

    label("loc_4AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0F")

    ChrTalk(
        0xB,
        (
            "Those Cryptids look like those\x01",
            "mysterious things similar to spirits that\x01",
            "previously appeared at the "Temple of Moon".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It would be ok if only their outward appearance\x01",
            "was scary, but not knowing their real nature\x01",
            "has got an eerie terror to it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I'd ever bump into one of those,\x01",
            "I must not lose consciousness again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CCA")

    label("loc_4C0F")


    ChrTalk(
        0xB,
        (
            "When we went to investigate spirits that\x01",
            "appeared at the "Temple of Moon" before,\x01",
            "I collapsed in a flurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If I'd ever bump into a Cryptid,\x01",
            "I must not lose consciousness again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CCA")

    Jump("loc_525B")

    label("loc_4CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DBC")

    ChrTalk(
        0xB,
        (
            "According to police intel, it's likely\x01",
            "that terrorists could show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Honestly, I don't want to\x01",
            "face such dangerous guys.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Aah, venerable Goddess of the Sky.\x01",
            "May this very day end peacefully...\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E4D")

    label("loc_4DBC")


    ChrTalk(
        0xB,
        (
            "Honestly, I don't want to\x01",
            "face dangerous guys\x01",
            "like terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Aah, venerable Goddess of the Sky.\x01",
            "May this very day end peacefully...\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E4D")

    Jump("loc_525B")

    label("loc_4E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_505C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA1")

    ChrTalk(
        0xB,
        (
            "Honestly, I was tense ushering in\x01",
            "the President's limousine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm someone who feels nervous easily...\x01",
            "Even when I saluted, I have a feeling\x01",
            "I did some kind of strange pose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, His Grace the President will probably\x01",
            "not bother with a private like me, but...\x01",
            "Even so, it was a lot of pressure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5057")

    label("loc_4FA1")


    ChrTalk(
        0xB,
        (
            "I was tense ushering in\x01",
            "the President's limousine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, His Grace the President will probably\x01",
            "not bother with a private like me, but...\x01",
            "Even so, it was a lot of pressure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5057")

    Jump("loc_525B")

    label("loc_505C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_525B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5181")

    ChrTalk(
        0xB,
        (
            "I have a childhood friend called Broude\x01",
            "at the Empire region of Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The other day I heard he\x01",
            "finished rehabilitation\x01",
            "training without problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Man, I was temporarily worried, but...\x01",
            "I felt relieved since it seems he completely recovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_525B")

    label("loc_5181")


    ChrTalk(
        0xB,
        (
            "The other day I heard from my childhood\x01",
            "friend Broude that he finished rehabilitation\x01",
            "training without problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Man, I was temporarily worried, but...\x01",
            "I felt relieved since it seems he completely recovered.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525B")

    TalkEnd(0xFE)
    Return()

    # Function_16_44A3 end

    def Function_17_525F(): pass

    label("Function_17_525F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5291")
    SetScenarioFlags(0x31, 2)

    label("loc_5291")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_52D1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52C6")
    Sound(2499, 255, 100, 0)
    Jump("loc_52CC")

    label("loc_52C6")

    Sound(3537, 255, 100, 0)

    label("loc_52CC")

    Jump("loc_52D7")

    label("loc_52D1")

    Sound(3344, 255, 100, 0)

    label("loc_52D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_558A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_534A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_532A"),
        (SWITCH_DEFAULT, "loc_533B"),
    )


    label("loc_532A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_5345")

    label("loc_533B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5345")

    Jump("loc_5585")

    label("loc_534A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_537C")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_537C")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_53AE"),
        (1, "loc_54B2"),
        (2, "loc_5543"),
        (SWITCH_DEFAULT, "loc_557B"),
    )


    label("loc_53AE")

    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53DF")
    OP_70(0x6, 0x12C)
    OP_71(0x6, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_53EF")

    label("loc_53DF")

    OP_70(0x6, 0xF0)
    OP_71(0x6, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_53EF")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5445")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5445")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5468")
    Sound(461, 0, 100, 0)

    label("loc_5468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5488")
    OP_70(0x6, 0x14A)
    OP_71(0x6, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_5498")

    label("loc_5488")

    OP_70(0x6, 0x10E)
    OP_71(0x6, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_5498")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x6, "light", 0x1, 0x1)
    OP_70(0x6, 0x0)
    Jump("loc_52D7")

    label("loc_54B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5524")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_54E7")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_54FF")

    label("loc_54E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_54FA")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_54FF")

    label("loc_54FA")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_54FF")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_553E")

    label("loc_5524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5534")
    OP_AF(0xFB)
    Jump("loc_553E")

    label("loc_5534")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_553E")

    Jump("loc_5585")

    label("loc_5543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_555C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5576")

    label("loc_555C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_556C")
    OP_AF(0xFB)
    Jump("loc_5576")

    label("loc_556C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5576")

    Jump("loc_5585")

    label("loc_557B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5585")

    Jump("loc_52D7")

    label("loc_558A")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_17_525F end

    def Function_18_5598(): pass

    label("Function_18_5598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_55E8")
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

    label("loc_55E8")

    Call(0, 5)
    Return()

    # Function_18_5598 end

    def Function_19_55EC(): pass

    label("Function_19_55EC")

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

    def lambda_5752():
        OP_96(0xFE, 0xFFFE2B40, 0xFFFFD8F0, 0xFFFF67A8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5752)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_55EC end

    def Function_20_5785(): pass

    label("Function_20_5785")

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
        "#00005F#5POh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_58F2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_58F2)

    ChrTalk(
        0x102,
        "#00105F#12PMaybe a call from another post?\x02",
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
            "#00000F#30WYes, Special Support Section,\x01",
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
            "Uhuhu...\x01",
            "It's me, me.\x02\x03",
            "Can you tell who I am?\x02",
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
            "#00012FMr. Michel...\x01",
            "Ehhm, is something wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhuhu, getting it right immediately...\x01",
            "Aren't you quite skillful?\x02\x03",
            "Or could it be none other than love?\x02",
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
            "#00006FNo, it's just that there's no other than you \x01",
            "Mr. Michel who could I've thought of.\x02\x03",
            "#00000FCould it be about KeA\x01",
            "who came there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, that's right.\x02\x03",
            "That child went to play at the\x01",
            "Waterfront Area with Shizuku.\x02\x03",
            "Zeit...I think he's called?\x01",
            "Since they're together with that\x01",
            "police dog, I think they're fine.\x02",
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
            "#00002FYeah, if Zeit is with them, I think\x01",
            "there's nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "My, really?\x02\x03",
            "I heard stories about him,\x01",
            "he looks very dignified.\x02\x03",
            "Not for nothing it's said to be\x01",
            "a legendary "Divine Wolf", eh?\x02",
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
            "#00004FHa ha...as you'd expect, I think a\x01",
            "legendary wolf would be different.\x02\x03",
            "#00005FAh, did you call on purpose\x01",
            "to inform us about this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, I'll tell you the main point now.\x02\x03",
            "Actually, it seems that Arios wants\x01",
            "to exchange information with you.\x02\x03",
            "He'll be back by evening, so\x01",
            "could you somehow have time?\x02",
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
            "#00000FEvening...?\x01",
            "I think it's fine.\x02\x03",
            "About the information exchange, does\x01",
            "he mean about the Trade Conference?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That too, but also...regarding the\x01",
            ""Heiyue" and the "Red Constellation".\x02",
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
            "#00003F...Understood.\x02\x03",
            "#00001FWhen we finish our business,\x01",
            "we'll come over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All right, we'll be waiting.\x07\x00\x02",
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
            "#00100F#12PIt seemed from Mr. Michel\x01",
            "of the Bracer Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PSomething happened?\x02",
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
        "#00006F#5PNo, it was an information exchange offer.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained to the other\x01",
            "members what Michel wanted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#11P"Heiyue" and the "Red Constellation"...?\x02\x03",
            "#00301FIt's true that someone like ol' man Arios could\x01",
            "be well informed about the autonomous state too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PUh uh, we could bite at the chance.\x02\x03",
            "#10300FSo then, should we go\x01",
            "back to Crossbell now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PNo, it seems that Mr. Arios\x01",
            "will be back in the evening.\x02\x03",
            "Until then, it should be fine\x01",
            "to finish our business.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_640C")

    ChrTalk(
        0x102,
        (
            "#00104F#12PWe could gather some information\x01",
            "about the "Red Constellation", but...\x02\x03",
            "#00102FSince we have a car, it seems it would\x01",
            "be better to go around some more places.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64BF")

    label("loc_640C")


    ChrTalk(
        0x102,
        (
            "#00103F#12PWe haven't gathered that much information\x01",
            "about the "Red Constellation"...\x02\x03",
            "#00100FSince we have a car, it seems it would\x01",
            "be better to go around some more places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64BF")


    ChrTalk(
        0x109,
        (
            "#10100F#11PThen, let's go to the Guild in East\x01",
            "Street after we finish our business.\x02",
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

    # Function_20_5785 end

    def Function_21_6553(): pass

    label("Function_21_6553")

    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_21_6553 end

    def Function_22_6563(): pass

    label("Function_22_6563")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_22_6563 end

    def Function_23_6576(): pass

    label("Function_23_6576")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_23_6576 end

    def Function_24_6589(): pass

    label("Function_24_6589")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_24_6589 end

    def Function_25_659C(): pass

    label("Function_25_659C")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_25_659C end

    def Function_26_65AF(): pass

    label("Function_26_65AF")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6853")
    Sleep(2500)
    SetChrPos(0x101, -53200, 0, 220, 90)
    SetChrPos(0x102, -54130, 0, -950, 90)
    SetChrPos(0x104, -54120, 0, 1520, 90)
    SetChrPos(0x109, -55800, 0, 1010, 90)
    SetChrPos(0x105, -56000, 0, -620, 90)

    def lambda_6725():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6725)

    def lambda_673F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_673F)
    Sleep(100)

    def lambda_6753():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6753)

    def lambda_676D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_676D)
    Sleep(120)

    def lambda_6781():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6781)

    def lambda_679B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_679B)
    Sleep(90)

    def lambda_67AF():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67AF)

    def lambda_67C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_67C9)
    Sleep(100)

    def lambda_67DD():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_67DD)

    def lambda_67F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_67F7)
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
    Jump("loc_6BA3")

    label("loc_6853")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A18")
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

    def lambda_68CC():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_68CC)
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
    Jump("loc_6BA3")

    label("loc_6A18")

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

    def lambda_6A91():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6A91)
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

    label("loc_6BA3")


    ChrTalk(
        0x101,
        "#00000FWell, we've arrived at Tangram Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIf I'm not mistaking it, it's the gate\x01",
            "where you were on service before being\x01",
            "assigned to the SSS, right, Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, that's right.\x02\x03",
            "This part is the national border gate\x01",
            "that guards the Republic region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAt present, the new Vice Commander\x01",
            "Douglas took its direction, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBig bro Douglas, huh...?\x01",
            "It's been a long time since I've met him too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe also have a support request that\x01",
            "seems to be highly urgent, so...\x02\x03",
            "Should we go visit the Vice Commander\x01",
            "room at 2F immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E18")
    SetChrPos(0x0, -49550, 0, -310, 90)
    Jump("loc_6E4D")

    label("loc_6E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E3C")
    SetChrPos(0x0, -35570, 0, 510, 90)
    Jump("loc_6E4D")

    label("loc_6E3C")

    SetChrPos(0x0, -30310, 0, 21020, 180)

    label("loc_6E4D")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_65AF end

    def Function_27_6E63(): pass

    label("Function_27_6E63")

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

    # Function_27_6E63 end

    def Function_28_6FEA(): pass

    label("Function_28_6FEA")

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
            "#11PThen, we'll now start the\x01",
            ""Douglas-style Training Program".\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PBoth parties are ready, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PMember Daimon and other four have\x01",
            "finished their preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FSame for the Special Support Section.\x02",
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
            "#11PFurthermore, in the fight that's going\x01",
            "to take place now, the use of Arts by\x01",
            "the SSS team is completely forbidden.\x02",
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

    def lambda_7360():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7360)
    Sleep(50)

    def lambda_7370():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7370)
    Sleep(50)

    def lambda_7380():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7380)
    Sleep(50)

    def lambda_7390():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7390)
    Sleep(50)

    def lambda_73A0():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_73A0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00005FW-...\x01",
            "Please, wait a moment!\x02\x03",
            "#00001FIsn't it too much of a disadvantage\x01",
            "if only we can't use Arts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FI see, so this is one of the \x01",
            "rumored "Douglas-styles", huh?\x02",
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
            "#11PThis training program is something\x01",
            "to test how to fight in many types\x01",
            "of disadvantaged conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PBy doing that, the purpose\x01",
            "is to increase the strength to\x01",
            "cope with many situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FI see, the "ogre" nickname for his\x01",
            "extreme methods isn't for show.\x02\x03",
            "#10302FHu hu...\x01",
            "Things have become interesting, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106F*sigh*...\x01",
            "It seems it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_761C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_761C)
    Sleep(50)

    def lambda_762C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_762C)
    Sleep(50)

    def lambda_763C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_763C)
    Sleep(50)

    def lambda_764C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_764C)
    Sleep(50)

    def lambda_765C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_765C)
    Sleep(300)

    ChrTalk(
        0x14,
        "#11PHave you finished talking?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#4S#11PThen...\x01",
            "Everyone, in position!\x02",
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
            "#12P#00003FThe opponents are fighting pros, CGF members...\x01",
            "And furthermore, we can't use Arts, eh?\x02\x03",
            "#00007FEveryone, don't let your guard down!\x01",
            "We'll absolutely find a way out for sure!\x02",
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
        "#5S#11P...Begin!!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4B0", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_6FEA end

    def Function_29_7870(): pass

    label("Function_29_7870")

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
        "#11PAlright, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Not bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Although you're forbidden\x01",
            "to use Arts...\x01",
            "You're very good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FIt seems we did it somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FI personally experienced not\x01",
            "being able to use Arts while\x01",
            "in battle, however...\x02\x03",
            "#00006FNot being able to use them\x01",
            "since the beginning like\x01",
            "now is quite hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FMaybe it felt like this at the time of\x01",
            "the Liberl orbal shutdown phenomenon\x01",
            "a little over one year ago...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x14,
        (
            "#11PIt seems you managed to safely get\x01",
            "through step 1 of the "Douglas-style".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PThen, continuing with step 2...\x01",
            "This time, I'll have you fight\x01",
            "with Crafts usage prohibited.\x02",
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

    def lambda_7C54():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C54)
    Sleep(50)

    def lambda_7C64():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C64)
    Sleep(50)

    def lambda_7C74():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C74)
    Sleep(50)

    def lambda_7C84():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C84)
    Sleep(50)

    def lambda_7C94():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C94)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00306FHey hey, there's more!?\x02\x03",
            "#00301FAnd Crafts are prohibited!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#11PWhat, if it's you guys\x01",
            "you'll manage somehow, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PI think it'll be good experience,\x01",
            "so come on, give it a try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FVice Commander...\x01",
            "You're too strict...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x14,
        (
            "#4S#11PAlright, CGF members, stand up!\x01",
            "Both parties, be ready for battle!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    def lambda_7E13():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E13)
    Sleep(50)

    def lambda_7E23():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E23)
    Sleep(50)

    def lambda_7E33():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E33)
    Sleep(50)

    def lambda_7E43():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E43)
    Sleep(50)

    def lambda_7E53():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E53)
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
            "#12P#00003FKh...\x01",
            "Honestly, not being able to\x01",
            "use Crafts will be tough, but...\x02\x03",
            "#00007FSomehow, we'll fight\x01",
            "using Arts freely and\x01",
            "normal attacks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101F...Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5S#11P...Begin!!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4F4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_29_7870 end

    def Function_30_8010(): pass

    label("Function_30_8010")

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
        "#11PUhm, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*bwaa*, for real...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "To think they could do so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F*phew*...\x01",
            "It was tough as expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah...\x01",
            "I understood how much important\x01",
            "are Crafts in battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FWell, we got it through in a\x01",
            "way or another, so it's ok.\x02\x03",
            "#00301FWhat do you say, no complaints, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PHu hu, I see.\x01",
            "It really seems you've\x01",
            "grown up well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PIn that case...\x01",
            "Let's move to step 3 of\x01",
            "the "Douglas-style"!\x02",
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
            "#5S#5PCGF members, stand up!\x01",
            "We switch over to the final training!\x02",
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
            "#12P#10302FHmph...\x01",
            "Like the stories I've heard,\x01",
            "you seem proficient, eh?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)

    ChrTalk(
        0x101,
        (
            "#12P#00003F"Douglas the Ogre"...\x01",
            "The CGF No.1 for skills\x01",
            "should be the real deal.\x02\x03",
            "#00007FEveryone, don't let your guard\x01",
            "down even for an instant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHah hah ha, it seems\x01",
            "you're quite used to your\x01",
            "position as a leader, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P...Then, let's take to a conclusion\x01",
            "all the training until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5S#5PUse all your might and...\x01",
            "Try to defeat me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FEh, fine by me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FHere I go!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_538", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_30_8010 end

    def Function_31_86AF(): pass

    label("Function_31_86AF")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89D6")
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
        "#12P#00002FW-We did it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI-Impossible...\x01",
            "To think that the Vice Commander has...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHmph...\x01",
            "You're quite good, eh?\x02",
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
            "#12P#00305F...I seems he didn't\x01",
            "feel that at all.\x02\x03",
            "#00306FTch, as tough as\x01",
            "always I'd say.\x02",
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
            "#5PSince the past, stamina was the one\x01",
            "and only redeeming feature I had.\x02",
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
        "#12P#10106FAs expected from the Vice Commander.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10306FOh boy, hats off to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PWell, with this, the training\x01",
            "is over for the time being.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x2)
    Jump("loc_8BFC")

    label("loc_89D6")

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
            "#12P#00003FKh...!\x01",
            "We couldn't do it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#N#00106FEven if we had Arts and Crafts,\x01",
            "we couldn't win...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#12P#00301FTch, no longer young\x01",
            "and yet full of vigour...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHu hu, I've still got a lot\x01",
            "more of active duty to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PI think you too did quite\x01",
            "your best, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FA complete defeat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FI guess it was to be expected from\x01",
            "the CGF Vice Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PWell, with this, the training\x01",
            "is over for the time being.\x02",
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

    label("loc_8BFC")

    TurnDirection(0x14, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#11PAll members, return to your positions\x01",
            "and resume your individual jobs.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8C78")
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_8C7E")

    label("loc_8C78")

    Sound(802, 0, 100, 0)

    label("loc_8C7E")

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
            "#5PYou too, thank you\x01",
            "for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PStanding around here talking\x01",
            "wouldn't be good, so let's go\x01",
            "back to my office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FY-Yes.\x02",
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

    # Function_31_86AF end

    def Function_32_8D8B(): pass

    label("Function_32_8D8B")

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

    def lambda_8E44():
        OP_95(0x101, -42000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E44)
    Sleep(30)

    def lambda_8E61():
        OP_95(0x102, -42500, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E61)
    Sleep(40)

    def lambda_8E7E():
        OP_95(0x104, -42500, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E7E)
    Sleep(800)

    def lambda_8E9B():
        OP_95(0x109, -44100, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E9B)
    Sleep(30)

    def lambda_8EB8():
        OP_95(0x103, -43800, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8EB8)
    Sleep(10)

    def lambda_8ED5():
        OP_95(0x105, -43800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8ED5)
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
            "#00000FWell then...\x01",
            "Has the black truck arrived...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI don't see it outdoors, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt could be that it's already\x01",
            "inside doing the departure\x01",
            "formalities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt seems likely.\x01",
            "Although it's here, it should take some time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FL-Let's go to confirm it fast!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FOh boy, I hope we've made it in time...\x02",
    )

    CloseMessageWindow()

    def lambda_9076():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9076)
    Sleep(30)

    def lambda_9093():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9093)
    Sleep(40)

    def lambda_90B0():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90B0)
    Sleep(30)

    def lambda_90CD():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_90CD)
    Sleep(30)

    def lambda_90EA():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_90EA)
    Sleep(10)

    def lambda_9107():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9107)
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

    # Function_32_8D8B end

    def Function_33_9148(): pass

    label("Function_33_9148")

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
            "#00000FWell then...\x01",
            "Has the black truck arrived...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI don't see it outdoors, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt could be that it's already\x01",
            "inside doing the departure\x01",
            "formalities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt seems likely.\x01",
            "It took us some time due to\x01",
            "waiting for the bus, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FL-Let's go to confirm it fast!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FOh boy, I hope we've made it in time...\x02",
    )

    CloseMessageWindow()

    def lambda_9377():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9377)
    Sleep(30)

    def lambda_9387():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9387)
    Sleep(40)

    def lambda_9397():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9397)
    Sleep(30)

    def lambda_93A7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93A7)
    Sleep(30)

    def lambda_93B7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93B7)
    Sleep(10)

    def lambda_93C7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_93C7)
    WaitChrThread(0x109, 2)

    def lambda_93D8():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_93D8)
    WaitChrThread(0x104, 2)

    def lambda_93F6():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_93F6)
    WaitChrThread(0x103, 2)

    def lambda_9414():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9414)
    WaitChrThread(0x102, 2)

    def lambda_9432():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9432)
    WaitChrThread(0x105, 2)

    def lambda_9450():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9450)
    WaitChrThread(0x101, 2)

    def lambda_946E():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_946E)
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

    # Function_33_9148 end

    def Function_34_94AF(): pass

    label("Function_34_94AF")

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

    def lambda_9568():
        OP_96(0x12, 0xFFFF5BF0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9568)
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
        "#00101FIt seems we've found him.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97A2")

    ChrTalk(
        0x18,
        (
            "Eh eh...\x01",
            "Now that I've arrived here, I can rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "What remains is to wholesale the medical\x01",
            "goods in the Republic region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Remiferia made medical goods...\x01",
            "They should turn into a pretty mira...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98AE")

    label("loc_97A2")


    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "Eh eh...\x01",
            "Now that I've arrived here, I can rest easy.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "What remains is to wholesale the medical\x01",
            "goods in the Republic region.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "Remiferia made medical goods...\x01",
            "They should turn into a pretty mira...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98AE")


    ChrTalk(
        0x101,
        "#00007F──We won't allow you!\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(-25430, 1000, -10970, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(21210, 3000)

    def lambda_991D():
        OP_95(0x101, -26500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_991D)

    def lambda_9937():
        OP_95(0x102, -26230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9937)

    def lambda_9951():
        OP_95(0x103, -26500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9951)

    def lambda_996B():
        OP_95(0x104, -27950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_996B)

    def lambda_9985():
        OP_95(0x105, -27550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9985)

    def lambda_999F():
        OP_95(0x109, -27550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_999F)
    WaitChrThread(0x101, 1)

    def lambda_99BD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_99BD)
    WaitChrThread(0x102, 1)

    def lambda_99CE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_99CE)
    WaitChrThread(0x103, 1)

    def lambda_99DF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_99DF)
    WaitChrThread(0x104, 1)

    def lambda_99F0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_99F0)
    WaitChrThread(0x105, 1)

    def lambda_9A01():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9A01)
    WaitChrThread(0x109, 1)

    def lambda_9A12():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9A12)
    OP_93(0x18, 0x10E, 0x1F4)
    WaitChrThread(0x109, 2)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9DA6")

    ChrTalk(
        0x18,
        "You...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FMinneth...\x01",
            "We had some suspects,\x01",
            "but it was really you, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYou're suspected to have cheated out\x01",
            "medical goods at the airport.\x02\x03",
            "#00101FWe're very sorry, but could you\x01",
            "show us your baggages...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "...Hmph, because I was in a hurry\x01",
            "I did too rough a job, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, indeed.\x01",
            "Compared to when we met at Armorica Village,\x01",
            "you did quite a lackluster trick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "...Because of you, my job at\x01",
            "Armorica Village was a failure\x01",
            "and I even ended up on a wanted list...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "If I didn't earn at least\x01",
            "this pocket money, my\x01",
            "business would go bust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHah! You should've got\x01",
            "another bigger reason.\x02\x03",
            "#00301FWe know that you're\x01",
            "purveying and raising funds\x01",
            "for the "Red Constellation".\x02\x03",
            "Because those guys ended up\x01",
            "doing such a thing in Crossbell,\x01",
            "you can't remain here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "...Hu hu, I'll leave that to your imagination.\x02",
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x5)
    Jump("loc_A186")

    label("loc_9DA6")


    NpcTalk(
        0x18,
        "Trader-looking Man",
        "Oh, and you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWe're from the Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "I'm terribly sorry, but could\x01",
            "you disclose your name\x01",
            "and occupation?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "Hm...police officers, eh?\x01",
            "Excuse my rudeness.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Trader-looking Man",
        (
            "My name is Minneth...\x01",
            "I am a humble trader of Imperial origins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "I am about to depart for a\x01",
            "business in the Republic...\x01",
            "Do you need something from me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FOh boy, doin' as if nothing happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYou're suspected to have cheated out\x01",
            "medical goods at the airport.\x02\x03",
            "#00101FWe're very sorry, but could you\x01",
            "show us your baggages...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Hm, it is true that I have medical\x01",
            "goods stocked in this truck, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "These baggages are mine from the start.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Furthermore, do you have proof\x01",
            "that I cheated out them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, I think he thinks he\x01",
            "can feign ignorance.\x02\x03",
            "#10302FAlthough I think that if we confirmed\x01",
            "with Mr. Ricardo he wouldn't really\x01",
            "be able to talk his way out.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x6)

    label("loc_A186")


    ChrTalk(
        0x103,
        (
            "#00203F...Time is precious.\x01",
            "Let's perform a compulsory arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah...it seems it's our only option.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Ooh, scary, scary.\x01",
            "What a group of savages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "If that's the case...\x01",
            "It seems I can only run away.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sound(464, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x3C, 0x1, 0x8)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(500)

    def lambda_A290():
        OP_95(0x18, -23800, 0, -11450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A290)
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

    def lambda_A34A():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A34A)
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

    def lambda_A3DB():
        OP_95(0x101, -23500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3DB)

    def lambda_A3F5():
        OP_95(0x102, -23230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3F5)

    def lambda_A40F():
        OP_95(0x103, -23500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A40F)

    def lambda_A429():
        OP_95(0x104, -24950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A429)

    def lambda_A443():
        OP_95(0x105, -24550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A443)

    def lambda_A45D():
        OP_95(0x109, -24550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A45D)
    WaitChrThread(0x109, 1)

    def lambda_A47B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A47B)

    def lambda_A488():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A488)

    def lambda_A495():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A495)

    def lambda_A4A2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A4A2)

    def lambda_A4AF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A4AF)

    def lambda_A4BC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A4BC)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10107FMr. Lloyd, let's chase\x01",
            "him with our orbal car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah...!\x02",
    )

    CloseMessageWindow()

    def lambda_A51C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A51C)
    Sleep(50)

    def lambda_A52C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A52C)
    Sleep(50)

    def lambda_A53C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A53C)
    Sleep(50)

    def lambda_A54C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A54C)
    Sleep(50)

    def lambda_A55C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A55C)
    Sleep(50)

    def lambda_A56C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A56C)
    WaitChrThread(0x101, 1)

    def lambda_A57D():
        OP_95(0x101, -32250, 0, -8230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A57D)
    WaitChrThread(0x102, 1)

    def lambda_A59B():
        OP_95(0x102, -31980, 0, -6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A59B)
    WaitChrThread(0x103, 1)

    def lambda_A5B9():
        OP_95(0x103, -31690, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A5B9)
    WaitChrThread(0x104, 1)

    def lambda_A5D7():
        OP_95(0x104, -33590, 0, -6950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A5D7)
    WaitChrThread(0x105, 1)

    def lambda_A5F5():
        OP_95(0x105, -33500, 0, -5480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A5F5)
    WaitChrThread(0x109, 1)

    def lambda_A613():
        OP_95(0x109, -33500, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A613)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetScenarioFlags(0x22, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_94AF end

    def Function_35_A648(): pass

    label("Function_35_A648")

    SetChrPos(0xFE, -22290, 0, -12240, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -24290, 0, -4000)
    OP_9F(0x1, -23290, 0, -2000)
    OP_9F(0x1, -21000, 0, 0)
    OP_9F(0x1, -18290, 0, 0)
    OP_9F(0x1, 290, 0, 0)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_35_A648 end

    def Function_36_A6AD(): pass

    label("Function_36_A6AD")

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
            "                   [Tangram Gate]\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_A6AD end

    SaveToFile()

Try(main)
