﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4200.bin",                # FileName
        "m4200",                    # MapName
        "m4200",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4200",                  # 0
        "Noel",                 # 1
        "Waji",                   # 2
        "Silver",                     # 3
        "boat",                 # 4
        "SE control",                 # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
    ))

    ATBonus("ATBonus_3C4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_4145", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_4135", 8,   8,   6,   6,   6,   8,   6)
    Sepith("Sepith_414D", 4,   2,   10,  4,   8,   2,   10)

    MonsterBattlePostion("MonsterBattlePostion_414", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_47C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_480", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_484", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_488", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_48C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_530", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_4145", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_4135", 50, 25, 25, 0,
        (
            ("ms78200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms78200.dat", "ms78200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms78200.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5CC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_414D", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch02900.itc",                   # 00
        "chr/ch03000.itc",                   # 01
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
        "monster/ch78250.itc",               # 10
        "monster/ch78251.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch83350.itc",               # 16
        "monster/ch83351.itc",               # 17
        "monster/ch86850.itc",               # 18
        "monster/ch86850.itc",               # 19
    ))

    DeclNpc(16000,   0,       31000,   225,  389,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(16000,   0,       31000,   225,  389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294946466, 12140,   4294966806, 0x1010087,    "BattleInfo_530", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(6310,    4294935416, 0,       0x1010141,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294959046, 4294922486, 0,       0x1010154,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294934476, 4294921006, 0,       0x1010154,    "BattleInfo_530", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(21150,   4294924626, 4294966796, 0x10100D1,    "BattleInfo_5CC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294943876, 4294894146, 0,       0x1010065,    "BattleInfo_5CC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(4294959816, 4294881066, 0,       0x101013B,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294941166, 4294868966, 4294967286, 0x1010098,    "BattleInfo_530", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(4294955646, 4294851916, 4294967286, 0x101014C,    "BattleInfo_5CC", 0,   24,  0xFFFF, 4,  5)

    DeclActor(4294945296, 4294966796, 19000,   1200,    4294945296, 500,     19000,   0x007C, 0,  4,  0x0000)
    DeclActor(4294960296, 0,       4294918796, 1200,    4294960296, 1000,    4294918796, 0x007C, 0,  5,  0x0000)
    DeclActor(22000,   500,     4294931296, 1200,    22000,   1500,    4294931296, 0x007C, 0,  6,  0x0000)
    DeclActor(4294940296, 0,       4294873296, 1200,    4294940296, 1000,    4294873296, 0x007C, 0,  7,  0x0000)
    DeclActor(4294960516, 0,       32820,   1200,    4294960516, 2000,    32820,   0x007C, 0,  11, 0x0000)
    DeclActor(13100,   4294966796, 4294959986, 1200,    14390,   4294966796, 4294952936, 0x007C, 0,  10, 0x0000)
    DeclActor(5410,    0,       44030,   3200,    5410,    0,       44030,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_7C0",          # 01, 1
        "Function_2_852",          # 02, 2
        "Function_3_104E",         # 03, 3
        "Function_4_1083",         # 04, 4
        "Function_5_11D4",         # 05, 5
        "Function_6_1325",         # 06, 6
        "Function_7_1476",         # 07, 7
        "Function_8_15DD",         # 08, 8
        "Function_9_1888",         # 09, 9
        "Function_10_1AEE",        # 0A, 10
        "Function_11_1BC2",        # 0B, 11
        "Function_12_1F05",        # 0C, 12
        "Function_13_1F1D",        # 0D, 13
        "Function_14_1F35",        # 0E, 14
        "Function_15_1F4D",        # 0F, 15
        "Function_16_1F65",        # 10, 16
        "Function_17_1F7D",        # 11, 17
        "Function_18_1FC8",        # 12, 18
        "Function_19_2013",        # 13, 19
        "Function_20_2076",        # 14, 20
        "Function_21_20D9",        # 15, 21
        "Function_22_212D",        # 16, 22
        "Function_23_4067",        # 17, 23
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_748"),
        (1, "loc_754"),
        (2, "loc_760"),
        (3, "loc_76C"),
        (4, "loc_778"),
        (5, "loc_784"),
        (6, "loc_790"),
        (SWITCH_DEFAULT, "loc_79C"),
    )


    label("loc_748")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_754")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_760")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_76C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_778")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_784")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_790")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_79C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_7A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_7BF")

    Return()

    # Function_0_710 end

    def Function_1_7C0(): pass

    label("Function_1_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D1")
    Call(0, 3)

    label("loc_7D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_808")
    ClearScenarioFlags(0x22, 0)
    OP_78(0x5, 0xB)
    SetChrPos(0xB, 21000, -500, 29720, 225)
    OP_D5(0xB, 0x0, 0x36EE8, 0x0, 0x0)
    Event(0, 22)

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81E")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_851")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    SetChrPos(0x0, -6780, 0, 32820, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_851")

    Return()

    # Function_1_7C0 end

    def Function_2_852(): pass

    label("Function_2_852")

    SetMapObjFlags(0x4, 0x4)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86E")
    OP_66(0x6, 0x1)

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_889")
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_889")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 14390, -500, -14360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    MiniGame(0x2F, 0xFFFFFFFF, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFE")
    OP_70(0x0, 0x0)
    Jump("loc_1002")

    label("loc_FFE")

    OP_70(0x0, 0x1E)

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1015")
    OP_70(0x1, 0x0)
    Jump("loc_1019")

    label("loc_1015")

    OP_70(0x1, 0x1E)

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102C")
    OP_70(0x2, 0x0)
    Jump("loc_1030")

    label("loc_102C")

    OP_70(0x2, 0x1E)

    label("loc_1030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1043")
    OP_70(0x3, 0x0)
    Jump("loc_1047")

    label("loc_1043")

    OP_70(0x3, 0x1E)

    label("loc_1047")

    Sound(123, 1, 80, 0)
    Return()

    # Function_2_852 end

    def Function_3_104E(): pass

    label("Function_3_104E")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_106D")
    ClearChrFlags(0x8, 0x80)

    label("loc_106D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_1082")
    ClearChrFlags(0x9, 0x80)

    label("loc_1082")

    Return()

    # Function_3_104E end

    def Function_4_1083(): pass

    label("Function_4_1083")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1183")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('不可思议盒饭『仰天』', 1)"), scpexpr(EXPR_END)), "loc_110C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '不可思议盒饭『仰天』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_117E")

    label("loc_110C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '不可思议盒饭『仰天』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '不可思议盒饭『仰天』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_117E")

    Jump("loc_11C8")

    label("loc_1183")

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

    label("loc_11C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1083 end

    def Function_5_11D4(): pass

    label("Function_5_11D4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D4")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_125D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_12CF")

    label("loc_125D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12CF")

    Jump("loc_1319")

    label("loc_12D4")

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

    label("loc_1319")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_11D4 end

    def Function_6_1325(): pass

    label("Function_6_1325")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1425")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('檀木树脂靴', 1)"), scpexpr(EXPR_END)), "loc_13AE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '檀木树脂靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1420")

    label("loc_13AE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '檀木树脂靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '檀木树脂靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1420")

    Jump("loc_146A")

    label("loc_1425")

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

    label("loc_146A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1325 end

    def Function_7_1476(): pass

    label("Function_7_1476")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A6")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the Earth × 80\x01\x07\x02",
            "#57IWater sepis × 80\x01\x07\x02",
            "#58IFire sepis × 80\x01\x07\x02",
            "#59IWind sepice × 80\x01\x07\x02",
            "#60ITime sepis × 80\x01\x07\x02",
            "#61IEmpty Sepis × 80\x01\x07\x02",
            "#62IThe phantom sepis × 80\x01\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F2, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_15CB")

    label("loc_15A6")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_15CB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1476 end

    def Function_8_15DD(): pass

    label("Function_8_15DD")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1884")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",            # 0
            "Replace with Wadi\x01",      # 1
            "quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C3")

    ChrTalk(
        0x105,
        "#10300FWell then, I will ask you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10100FYes, leave it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    OP_37()
    Call(0, 3)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_187F")

    label("loc_16C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D7")
    Jump("loc_187F")

    label("loc_16D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E4")

    ChrTalk(
        0x8,
        (
            "#10103FJoachim Gunter\x01",
            "Gnostic raw materials\x01",
            "Where they were collecting ……\x02\x03",
            "#10108FIn such a place, to Eoria\x01",
            "What on earth was that … ….\x02\x03",
            "#10101FThere is also the danger that \"Phantom beast\" will appear\x01",
            "It is highly likely.\x01",
            "Everyone, please be careful!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_187F")

    label("loc_17E4")


    ChrTalk(
        0x8,
        (
            "#10108FIn such a place, to Eoria\x01",
            "What on earth was that … ….\x02\x03",
            "#10101FThere is also the danger that \"Phantom beast\" will appear\x01",
            "It is highly likely.\x01",
            "Everyone, please be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187F")

    Jump("loc_15EA")

    label("loc_1884")

    TalkEnd(0xFE)
    Return()

    # Function_8_15DD end

    def Function_9_1888(): pass

    label("Function_9_1888")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1895")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AEA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",              # 0
            "To replace Noel\x01",      # 1
            "quit\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1970")

    ChrTalk(
        0x109,
        "#10100FWaji, I left it to you later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10300FHuh, I understand.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    OP_37()
    Call(0, 3)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1AE5")

    label("loc_1970")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1984")
    Jump("loc_1AE5")

    label("loc_1984")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A67")

    ChrTalk(
        0x9,
        (
            "#10303FIn such a place \"Praroma Grass\"\x01",
            "It was blooming in the end.\x02\x03",
            "#10302FInexplicable fog that wraps around,\x01",
            "Is it because of this flower …?\x02\x03",
            "#10304FIn any case, if forward\x01",
            "You should go cautiously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AE5")

    label("loc_1A67")


    ChrTalk(
        0x9,
        (
            "#10302FInexplicable fog that wraps around,\x01",
            "Is it because of \"Pleroma grass\"?\x02\x03",
            "#10304FIn any case, if forward\x01",
            "You should go cautiously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE5")

    Jump("loc_1895")

    label("loc_1AEA")

    TalkEnd(0xFE)
    Return()

    # Function_9_1888 end

    def Function_10_1AEE(): pass

    label("Function_10_1AEE")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
    )

    CloseMessageWindow()
    OP_68(14080, 500, -10820, 1500)
    MoveCamera(53, 46, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(16290, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBD")
    OP_E2(0x2)
    MiniGame(0x6, 0x6, 0x328C, 0xFFFFFE0C, 0xFFFFE322, 0xB4, 0x3836, 0xFFFFFE0C, 0xFFFFC7E8)

    label("loc_1BBD")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1AEE end

    def Function_11_1BC2(): pass

    label("Function_11_1BC2")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF4")
    SetScenarioFlags(0x31, 2)

    label("loc_1BF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1C34")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C29")
    Sound(2499, 255, 100, 0)
    Jump("loc_1C2F")

    label("loc_1C29")

    Sound(3537, 255, 100, 0)

    label("loc_1C2F")

    Jump("loc_1C3A")

    label("loc_1C34")

    Sound(3344, 255, 100, 0)

    label("loc_1C3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1CB3")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C93"),
        (SWITCH_DEFAULT, "loc_1CA4"),
    )


    label("loc_1C93")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CAE")

    label("loc_1CA4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CAE")

    Jump("loc_1EF2")

    label("loc_1CB3")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1CE7")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_1CE7")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D1B"),
        (1, "loc_1E1F"),
        (2, "loc_1EB0"),
        (SWITCH_DEFAULT, "loc_1EE8"),
    )


    label("loc_1D1B")

    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_74(0x7, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D4C")
    OP_70(0x7, 0x12C)
    OP_71(0x7, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_1D5C")

    label("loc_1D4C")

    OP_70(0x7, 0xF0)
    OP_71(0x7, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_1D5C")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DB2")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD5")
    Sound(461, 0, 100, 0)

    label("loc_1DD5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF5")
    OP_70(0x7, 0x14A)
    OP_71(0x7, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_1E05")

    label("loc_1DF5")

    OP_70(0x7, 0x10E)
    OP_71(0x7, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_1E05")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x7, "light", 0x1, 0x1)
    OP_70(0x7, 0x0)
    Jump("loc_1C3A")

    label("loc_1E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1E91")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_1E54")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1E6C")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1E67")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1E6C")

    label("loc_1E67")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1E6C")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EAB")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1EA1")
    OP_AF(0xFB)
    Jump("loc_1EAB")

    label("loc_1EA1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EAB")

    Jump("loc_1EF2")

    label("loc_1EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EE3")

    label("loc_1EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1ED9")
    OP_AF(0xFB)
    Jump("loc_1EE3")

    label("loc_1ED9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE3")

    Jump("loc_1EF2")

    label("loc_1EE8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EF2")

    Jump("loc_1C3A")

    label("loc_1EF7")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_11_1BC2 end

    def Function_12_1F05(): pass

    label("Function_12_1F05")

    OP_9C(0xFE, 0xFFFFAC04, 0x0, 0xFFFFAC04, 0x32, 0x3)
    Return()

    # Function_12_1F05 end

    def Function_13_1F1D(): pass

    label("Function_13_1F1D")

    OP_9C(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x32, 0x5)
    Return()

    # Function_13_1F1D end

    def Function_14_1F35(): pass

    label("Function_14_1F35")

    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x32, 0xA)
    Return()

    # Function_14_1F35 end

    def Function_15_1F4D(): pass

    label("Function_15_1F4D")

    OP_9C(0xFE, 0xFFFFEE6C, 0x0, 0x0, 0x32, 0xA)
    Return()

    # Function_15_1F4D end

    def Function_16_1F65(): pass

    label("Function_16_1F65")

    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x32, 0xA)
    Return()

    # Function_16_1F65 end

    def Function_17_1F7D(): pass

    label("Function_17_1F7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FC7")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_17_1F7D")

    label("loc_1FC7")

    Return()

    # Function_17_1F7D end

    def Function_18_1FC8(): pass

    label("Function_18_1FC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2012")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -750, -5000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("Function_18_1FC8")

    label("loc_2012")

    Return()

    # Function_18_1FC8 end

    def Function_19_2013(): pass

    label("Function_19_2013")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xFFFFF542, 0x0, 0x5DC, 0xFA, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(39, 0, 80, 0)
    Sound(30, 0, 50, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_19_2013 end

    def Function_20_2076(): pass

    label("Function_20_2076")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0xFA, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(39, 0, 80, 0)
    Sound(30, 0, 50, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_20_2076 end

    def Function_21_20D9(): pass

    label("Function_21_20D9")

    Sound(483, 2, 50, 0)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Sleep(200)
    OP_25(0x1E3, 0x64)
    Sleep(2000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sleep(2500)
    Sound(484, 0, 50, 0)
    Sleep(500)
    Sound(477, 0, 60, 0)
    Sleep(6500)
    Sound(478, 0, 40, 0)
    Return()

    # Function_21_20D9 end

    def Function_22_212D(): pass

    label("Function_22_212D")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    LoadChrToIndex("chr/ch00201.itc", 0x20)
    LoadChrToIndex("chr/ch00301.itc", 0x21)
    LoadChrToIndex("chr/ch02901.itc", 0x22)
    LoadChrToIndex("chr/ch03001.itc", 0x23)
    LoadEffect(0x0, "event/ev315_00.eff")
    LoadEffect(0x1, "event/ev202_00.eff")
    SoundLoad(483)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_21C9")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis263.itp")
    Jump("loc_21F5")

    label("loc_21C9")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis264.itp")

    label("loc_21F5")

    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00700.itp")
    SetChrPos(0xB, 57000, -500, 59720, 225)
    SetChrPos(0x101, 56350, -150, 57870, 225)
    SetChrPos(0x109, 55800, -150, 58520, 225)
    SetChrPos(0x102, 55150, -150, 59270, 270)
    SetChrPos(0x105, 57400, 280, 61720, 270)
    SetChrPos(0x103, 56900, 280, 59620, 225)
    SetChrPos(0x104, 58300, 280, 59620, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x4)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0x104, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    ClearChrFlags(0x102, 0x1)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 10000, 0, 20000, 45)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0x90, 0xB0, 0xC0, 0x0, 0x0)
    OP_11(0xA0, 0xB8, 0xD0, 0x1, 0x28, 0x0)
    OP_68(52530, 1000, 55230, 0)
    MoveCamera(29, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(26420, 0)
    BeginChrThread(0xC, 1, 0, 21)
    FadeToBright(1000, 0)
    OP_68(25540, 1000, 30950, 7000)
    BeginChrThread(0xB, 1, 0, 12)
    BeginChrThread(0x109, 1, 0, 12)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(1500)
    MoveCamera(329, 20, 0, 3500)
    OP_6E(650, 3500)
    SetCameraDistance(26420, 3500)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1194)
    OP_11(0xB4, 0xE6, 0xFA, 0x19, 0x5A, 0x157C)
    Sleep(1000)
    EndChrThread(0x109, 0x3)
    BeginChrThread(0x109, 3, 0, 18)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 13)
    BeginChrThread(0x109, 1, 0, 13)
    Sleep(1000)

    def lambda_23E2():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23E2)

    def lambda_23EF():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_23EF)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 14)
    BeginChrThread(0x109, 1, 0, 14)
    WaitChrThread(0xB, 1)

    def lambda_2410():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2410)

    def lambda_241D():
        OP_93(0xFE, 0x13B, 0xC8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_241D)
    SetChrFlags(0x102, 0x1)
    BeginChrThread(0xB, 1, 0, 15)
    BeginChrThread(0x109, 1, 0, 15)
    SetChrSubChip(0x109, 0x2)
    OP_68(21520, 1000, 29780, 0)
    MoveCamera(282, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(24330, 0)
    Fade(500)
    OP_68(21520, 1000, 29780, 2000)
    MoveCamera(291, 23, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(19110, 2000)
    Sleep(1000)

    def lambda_24A3():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24A3)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 16)
    BeginChrThread(0x109, 1, 0, 16)
    Sleep(300)

    def lambda_24C3():
        OP_9B(0x1, 0xFE, 0x159, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24C3)
    Sleep(200)
    EndChrThread(0x109, 0x3)
    Sleep(200)

    def lambda_24E2():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_24E2)
    WaitChrThread(0x105, 2)
    Sleep(400)
    WaitChrThread(0xB, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x21)
    BeginChrThread(0x104, 1, 0, 19)
    Sleep(200)

    def lambda_2517():
        OP_9B(0x1, 0xFE, 0x1E, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2517)
    Sleep(200)
    WaitChrThread(0x105, 2)
    SetChrChipByIndex(0x105, 0x23)
    BeginChrThread(0x105, 1, 0, 19)
    WaitChrThread(0x104, 1)

    def lambda_2541():
        OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2541)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x103, 1)

    def lambda_255E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_255E)
    WaitChrThread(0x103, 2)
    SetChrChipByIndex(0x103, 0x20)
    BeginChrThread(0x103, 1, 0, 19)
    Sleep(300)
    WaitChrThread(0x103, 1)
    SetChrPos(0x105, 14800, 0, 26800, 180)
    SetChrPos(0x103, 13500, 0, 28800, 180)
    SetChrPos(0x101, 12300, 0, 27000, 180)
    SetChrPos(0x102, 17000, 0, 32500, 225)
    SetChrPos(0x104, 12750, 0, 29500, 225)
    SetChrPos(0x109, 20500, 400, 30700, 225)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrBattleFlags(0x101, 0x20)
    ClearChrBattleFlags(0x102, 0x20)
    ClearChrBattleFlags(0x109, 0x20)
    ClearChrBattleFlags(0x103, 0x20)
    ClearChrBattleFlags(0x104, 0x20)
    ClearChrBattleFlags(0x105, 0x20)
    SetChrChipByIndex(0x109, 0x0)
    SetChrSubChip(0x109, 0x0)
    OP_68(13480, 1000, 28250, 0)
    MoveCamera(12, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20690, 0)
    Fade(500)

    def lambda_265D():
        OP_9B(0x0, 0xFE, 0x0, 0x1450, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_265D)

    def lambda_2672():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2672)

    def lambda_2687():
        OP_9B(0x0, 0xFE, 0xB, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2687)

    def lambda_269C():
        OP_9B(0x0, 0xFE, 0x5, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_269C)

    def lambda_26B1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26B1)
    Sleep(850)
    SetChrChipByIndex(0x109, 0x22)
    BeginChrThread(0x109, 1, 0, 20)
    WaitChrThread(0x109, 1)

    def lambda_26D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_26D7)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(150)

    def lambda_26F7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_26F7)
    Sleep(250)

    def lambda_2707():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2707)
    WaitChrThread(0x109, 2)

    def lambda_2718():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2718)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    Sleep(250)

    ChrTalk(
        0x101,
        "#00007F#5PT-This is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PWell, there are things,\x01",
            "Lin's came on board\x01",
            "It looks like a boat, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10310F#11P…… No way … …\x01",
            "I do not think that it is supposed to be such a thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(11980, 1000, 24000, 0)
    MoveCamera(197, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16030, 0)
    OP_68(-6620, 1000, -43200, 9000)
    MoveCamera(228, 27, 0, 9000)
    OP_6E(650, 9000)
    SetCameraDistance(27620, 9000)
    SetChrPos(0x101, 8930, 0, 17730, 180)
    SetChrPos(0x102, 7930, 0, 18730, 180)
    SetChrPos(0x103, 10030, 0, 18430, 180)
    SetChrPos(0x109, 8530, 0, 19830, 180)
    SetChrPos(0x104, 9730, 0, 20530, 180)
    SetChrPos(0x105, 10730, 0, 19530, 180)
    SetChrPos(0xA, 750, 0, 10500, 45)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-7670, 1000, -44840, 0)
    MoveCamera(37, 36, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(41480, 0)
    OP_68(4910, 1000, 14450, 10000)
    MoveCamera(76, 35, 0, 10000)
    OP_6E(550, 10000)
    SetCameraDistance(27520, 10000)
    SetChrPos(0x101, 8930, 0, 17730, 225)
    SetChrPos(0x102, 7930, 0, 18730, 225)
    SetChrPos(0x103, 10030, 0, 18430, 225)
    SetChrPos(0x109, 8530, 0, 19830, 225)
    SetChrPos(0x104, 9730, 0, 20530, 225)
    SetChrPos(0x105, 10730, 0, 19530, 225)
    Sleep(3000)
    PlaceName2(340, 200, "c_plac51", 0x0, 0)

    def lambda_29AA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29AA)
    Sleep(100)

    def lambda_29C2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29C2)
    Sleep(100)

    def lambda_29DA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29DA)
    Sleep(50)

    def lambda_29F2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_29F2)
    Sleep(50)

    def lambda_2A0A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A0A)
    Sleep(100)

    def lambda_2A22():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A22)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Sleep(750)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(4460, 1000, 14170, 0)
    MoveCamera(224, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#12PCome on … …\x01",
            "Are we watching even a dream …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PIt's like a fairy tale\x01",
            "It seems there are … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PU-unbelievable\x02\x03",
            "#00201FIt is as if the structure of the space itself\x01",
            "It seems to be different from reality … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PPrelimma grass … From when\x01",
            "Were they breeding so much?\x02\x03",
            "#00003FBut, I see …\x01",
            "Joachim makes the raw material of Gnostic\x01",
            "I was collecting ──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2628, 255, 100, 0)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(
        0xA,
        "voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#N#5PWell, consider this place\x01",
            "There is no mistake.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
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
    OP_68(4260, 1000, 13700, 2000)
    MoveCamera(166, 18, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(13900, 2000)
    PlayEffect(0x1, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(341, 0, 100, 0)
    ClearChrFlags(0xA, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2D54():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2D54)

    def lambda_2D69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2D69)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105F#6PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PF-from that time..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5P\"Silver#2RIn#\"… ….\x01",
            "How come you! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sound(2627, 255, 100, 0)
    Sleep(500)

    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "That would be my line\x02\x03",
            "With the shadow of the \"snake\"\x01",
            "Demolition of bad leaders … …\x02\x03",
            "Blue flowers that started to bloom in various places\x01",
            "The emergence of a magical \"eidolon\" …\x02\x03",
            "If you follow the signs of them\x01",
            "What do you mean to come across you …?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x105,
        "#10305F#6PHmm\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PSort of\x01",
            "Staring at this place as doubtful\x01",
            "Did you take the trouble to step in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11PExactly\x02\x03",
            "#00702FHmm, if you are\x01",
            "It seems that circumstances are somewhat different?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PR-right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PBecause it is this case\x01",
            "I will explain the circumstances … ….\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Phosphorus and aeolia\x01",
            "I explained the circumstances when I was missing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P─ ─ I see, that boat is\x01",
            "Was it a thief's stuff?\x02\x03",
            "#00702FPowered by chance, …\x01",
            "I like this person, apparently at the core\x01",
            "It seems that it is getting close.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PCore…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PWhy the blue flower - \"Preloma grass\"\x01",
            "Beginning to bloom all over the crossbell,\x01",
            "\"Phantom beast\" started to appear ……\x02\x03",
            "#10301FIt is a crossbell\x01",
            "\"What meaning do you have?\"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11PHmm. Exactly\x02\x03",
            "#00700FThis is also\x01",
            "It is a contract with \"Black moon\".\x02\x03",
            "The prisoners to you\x01",
            "Leave it aside, I will go ahead - ─\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PNo.\x02\x03",
            "#00000F\"Silver\"……\x01",
            "Will not you go with me here as well?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3333():

        label("loc_3333")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3333")

    QueueWorkItem2(0x102, 2, lambda_3333)
    Sleep(100)

    def lambda_3348():

        label("loc_3348")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3348")

    QueueWorkItem2(0x104, 2, lambda_3348)
    Sleep(100)

    def lambda_335D():

        label("loc_335D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_335D")

    QueueWorkItem2(0x103, 2, lambda_335D)
    Sleep(50)

    def lambda_3372():

        label("loc_3372")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3372")

    QueueWorkItem2(0x109, 2, lambda_3372)
    Sleep(50)

    def lambda_3387():

        label("loc_3387")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3387")

    QueueWorkItem2(0x105, 2, lambda_3387)
    Sleep(200)

    ChrTalk(
        0x109,
        "#10111F#6PL-Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6POi oi really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#12PHuh, somehow like that\x01",
            "I felt like to say that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PIt was just as I predicted\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PJust like this time\x01",
            "Is it too flexible or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2629, 255, 100, 0)
    Sleep(500)

    def lambda_34A3():

        label("loc_34A3")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_34A3")

    QueueWorkItem2(0x102, 2, lambda_34A3)
    Sleep(100)

    def lambda_34B8():

        label("loc_34B8")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_34B8")

    QueueWorkItem2(0x104, 2, lambda_34B8)
    Sleep(150)

    def lambda_34CD():

        label("loc_34CD")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_34CD")

    QueueWorkItem2(0x103, 2, lambda_34CD)
    Sleep(100)

    def lambda_34E2():

        label("loc_34E2")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_34E2")

    QueueWorkItem2(0x109, 2, lambda_34E2)
    Sleep(50)

    def lambda_34F7():

        label("loc_34F7")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_34F7")

    QueueWorkItem2(0x105, 2, lambda_34F7)
    Sleep(200)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P…… Bannings.\x01",
            "What are you misunderstanding?\x02\x03",
            "In the first place, you and me\x01",
            "Different stands will have different interests.\x02\x03",
            "Unlike at the time of hospital,\x01",
            "Benefits to cooperate with you - ─\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PNothing. That's what you're going to say?\x02\x03",
            "#00001FLin and Aoria are\x01",
            "It is a great army to reach Class A.\x02\x03",
            "With 2 people together,\x01",
            "It is comparable to that Arios\x01",
            "I saw that I had a good skill.\x02\x03",
            "#00006FThe two of them disappear\x01",
            "If danger awaits … …\x02\x03",
            "#00013FEven if you truly alone\x01",
            "Can we assert that we are all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P…\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F#5PWell, it is an emergency situation\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#6PIf Lin's were safe\x01",
            "You can also get the information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PIf efficiency focuses to the last\x01",
            "Certainly we can cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11PHa\x02\x03",
            "\"Special Affairs Support Division\" … …\x01",
            "Apparently to the leaders\x01",
            "You seem to be inspired?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112F#6PI-I wonder\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#6PWell we can't deny that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#5PI'm a bit reluctant\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_38AE():

        label("loc_38AE")

        OP_93(0xFE, 0x159, 0x1F4)
        Yield()
        Jump("loc_38AE")

    QueueWorkItem2(0x101, 2, lambda_38AE)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00011F#5PNo, so why did I blame you\x01",
            "I doubt whether it is going … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PAhah\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#6PGiggle\x01",
            "I guess this is also a virtue.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_395B():

        label("loc_395B")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_395B")

    QueueWorkItem2(0x101, 2, lambda_395B)
    Sleep(100)
    Sleep(250)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P── It will be good.\x01",
            "This time#4RThis time#Let's accompany temporarily.\x02\x03",
            "#00700FBut \"wind sword of heaven\"\x01",
            "I keep going after catching up.\x02\x03",
            "Is that fine?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, got it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PBut with this number of people\x01",
            "As expected, there is no small turning.\x02\x03",
            "#00301FWhen attacked by a devil, something\x01",
            "It is likely to be stuck.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A9E():

        label("loc_3A9E")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3A9E")

    QueueWorkItem2(0x101, 2, lambda_3A9E)
    Sleep(50)

    def lambda_3AB3():

        label("loc_3AB3")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3AB3")

    QueueWorkItem2(0x102, 2, lambda_3AB3)
    Sleep(50)

    def lambda_3AC8():

        label("loc_3AC8")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3AC8")

    QueueWorkItem2(0x103, 2, lambda_3AC8)
    Sleep(50)

    def lambda_3ADD():

        label("loc_3ADD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3ADD")

    QueueWorkItem2(0x109, 2, lambda_3ADD)
    Sleep(50)

    def lambda_3AF2():

        label("loc_3AF2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3AF2")

    QueueWorkItem2(0x105, 2, lambda_3AF2)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#10103F#12PThen, someone else here\x01",
            "You may as well leave it.\x02\x03",
            "#10101FBoat guards also\x01",
            "It may be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PWhy not?\x01",
            "For the time when the \"Wind Sword Saint\" came.\x01",
            "It is likely to be a liaison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PGot it. Let's think of who to leave\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-2600, 1500, 2120, 3000)
    MoveCamera(182, 16, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(18630, 3000)

    def lambda_3C31():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C31)
    Sleep(50)

    def lambda_3C41():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C41)
    Sleep(50)

    def lambda_3C51():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C51)
    Sleep(50)

    def lambda_3C61():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3C61)
    Sleep(50)

    def lambda_3C71():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3C71)
    Sleep(50)

    def lambda_3C81():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3C81)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D74")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    FadeToDark(0, 0, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F#1P(I borrowed that technique I taught you\x01",
            "I have not returned it properly yet ……)\x02\x03",
            "#00013F(Anyway, find Lynn's sisters\x01",
            "I have to check my safety …! )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Jump("loc_3E45")

    label("loc_3D74")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    FadeToDark(0, 0, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F#1P(I was cautious around the beginning\x01",
            "Recently I was building a good relationship … …)\x02\x03",
            "#00001F(Anyway, find them\x01",
            "I have to confirm safety …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    label("loc_3E45")

    Sleep(1000)
    OP_32(0xFF, 0xF9, 0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho will be left as a waiting member?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Wadi】\x01",        # 0
            "[Noel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3EC8"),
        (0, "loc_3EE0"),
        (SWITCH_DEFAULT, "loc_3EF8"),
    )


    label("loc_3EC8")

    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    Jump("loc_3EF8")

    label("loc_3EE0")

    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    Jump("loc_3EF8")

    label("loc_3EF8")

    AddParty(0x5, 0xFF, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_49()
    OP_32(0x5, 0x0, 0x49)
    OP_32(0x5, 0x5, 0xC8)
    OP_42(0x5, 0x460, 0xFF)
    OP_42(0x5, 0x5E8, 0xFF)
    OP_42(0x5, 0x649, 0xFF)
    OP_42(0x5, 0x4A, 0x3)
    OP_42(0x5, 0x22, 0x4)
    RemoveCraft(0x5, 0xFFFF)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x5, 0x81, 0x1)
    OP_38(0x5, 0x82, 0x1)
    OP_38(0x5, 0x83, 0x1)
    OP_38(0x5, 0x84, 0x2)
    OP_38(0x5, 0x85, 0x2)
    OP_38(0x5, 0x86, 0x1)
    OP_42(0x5, 0xE7, 0x0)
    OP_42(0x5, 0xBA, 0x1)
    OP_42(0x5, 0x9E, 0x2)
    OP_42(0x5, 0x6D, 0x3)
    OP_42(0x5, 0x76, 0x4)
    OP_42(0x5, 0x69, 0x5)
    OP_42(0x5, 0x90, 0x6)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0xCC)
    AddCraft(0x5, 0x131)
    SetChrChipPat(0x5, 0x6, 0x131)
    AddCraft(0x5, 0x16D)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 11000, 0, 26000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x165, 2)
    OP_29(0xA9, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3FD3")
    Jump("loc_3FD8")

    label("loc_3FD3")

    OP_29(0x80, 0x4, 0x40)

    label("loc_3FD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3FE9")
    Jump("loc_3FEE")

    label("loc_3FE9")

    OP_29(0x83, 0x4, 0x40)

    label("loc_3FEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3FFF")
    Jump("loc_4004")

    label("loc_3FFF")

    OP_29(0x88, 0x4, 0x40)

    label("loc_4004")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4015")
    Jump("loc_401A")

    label("loc_4015")

    OP_29(0x8B, 0x4, 0x40)

    label("loc_401A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_402B")
    Jump("loc_4030")

    label("loc_402B")

    OP_29(0x8C, 0x4, 0x40)

    label("loc_4030")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4041")
    Jump("loc_4046")

    label("loc_4041")

    OP_29(0x8D, 0x4, 0x40)

    label("loc_4046")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_66(0x6, 0x1)
    OP_24(0x1E3)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_212D end

    def Function_23_4067(): pass

    label("Function_23_4067")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A small boat is parked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410A")

    ChrTalk(
        0x101,
        (
            "#00001FThis is a boat that two people used.\x02\x03",
            "- Anyhow, let's hurry and head back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_410A")

    EventEnd(0x3)
    Return()

    # Function_23_4067 end

    SaveToFile()

Try(main)
