from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Noｱl",                  # 1
        "Wazy",                   # 2
        "Yin",                    # 3
        "ボート",                 # 4
        "SE制御",                 # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
    ))

    ATBonus("ATBonus_3C4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_434D", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_433D", 8,   8,   6,   6,   6,   8,   6)
    Sepith("Sepith_4355", 4,   2,   10,  4,   8,   2,   10)

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
        "BattleInfo_530", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_434D", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_433D", 50, 25, 25, 0,
        (
            ("ms78200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms78200.dat", "ms78200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms78200.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5CC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_4355", 40, 30, 20, 0,
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
        "Function_8_15DF",         # 08, 8
        "Function_9_18DB",         # 09, 9
        "Function_10_1B40",        # 0A, 10
        "Function_11_1C07",        # 0B, 11
        "Function_12_1F44",        # 0C, 12
        "Function_13_1F5C",        # 0D, 13
        "Function_14_1F74",        # 0E, 14
        "Function_15_1F8C",        # 0F, 15
        "Function_16_1FA4",        # 10, 16
        "Function_17_1FBC",        # 11, 17
        "Function_18_2007",        # 12, 18
        "Function_19_2052",        # 13, 19
        "Function_20_20B5",        # 14, 20
        "Function_21_2118",        # 15, 21
        "Function_22_216C",        # 16, 22
        "Function_23_426B",        # 17, 23
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117F")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1B9, 1)"), scpexpr(EXPR_END)), "loc_1108")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_117A")

    label("loc_1108")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_117A")

    Jump("loc_11C8")

    label("loc_117F")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D0")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1259")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_12CB")

    label("loc_1259")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12CB")

    Jump("loc_1319")

    label("loc_12D0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1421")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64A, 1)"), scpexpr(EXPR_END)), "loc_13AA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_141C")

    label("loc_13AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64A),
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_141C")

    Jump("loc_146A")

    label("loc_1421")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AF")
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
            "#56I Earth Sepith  x80\x01\x07\x02",
            "#57I Water Sepith  x80\x01\x07\x02",
            "#58I Fire Sepith   x80\x01\x07\x02",
            "#59I Wind Sepith   x80\x01\x07\x02",
            "#60I Time Sepith   x80\x01\x07\x02",
            "#61I Space Sepith  x80\x01\x07\x02",
            "#62I Mirage Sepith x80\x01\x07\x00",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F2, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_15CD")

    label("loc_15AF")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is empty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_15CD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1476 end

    def Function_8_15DF(): pass

    label("Function_8_15DF")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                 # 0
            "Switch Wazy Out\x01",      # 1
            "Cancel\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CE")

    ChrTalk(
        0x105,
        (
            "#10300FThen, take care of the\x01",
            "rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10100FYes, leave it to me!\x02",
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
    Jump("loc_18D2")

    label("loc_16CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E2")
    Jump("loc_18D2")

    label("loc_16E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1816")

    ChrTalk(
        0x8,
        (
            "#10103FThe place where Joachim Gｸnther\x01",
            "was harvesting Gnosis\x01",
            "ingredients...\x02\x03",
            "#10108FWhat could've happened to Ling\x01",
            "and Eolia in a place like this,\x01",
            "I wonder...?\x02\x03",
            "#10101FIt also appears there's a great\x01",
            "danger of Cryptids showing up.\x01",
            "Everyone, please be careful!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18D2")

    label("loc_1816")


    ChrTalk(
        0x8,
        (
            "#10108FWhat could've happened to Ling\x01",
            "and Eolia in a place like this,\x01",
            "I wonder...?\x02\x03",
            "#10101FIt also appears there's a great\x01",
            "danger of Cryptids showing up.\x01",
            "Everyone, please be careful!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D2")

    Jump("loc_15EC")

    label("loc_18D7")

    TalkEnd(0xFE)
    Return()

    # Function_8_15DF end

    def Function_9_18DB(): pass

    label("Function_9_18DB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                  # 0
            "Switch Noｱl Out\x01",      # 1
            "Cancel\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C4")

    ChrTalk(
        0x109,
        (
            "#10100FWazy, I leave the rest\x01",
            "to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10300FHehe, roger.\x02",
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
    Jump("loc_1B37")

    label("loc_19C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D8")
    Jump("loc_1B37")

    label("loc_19D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B37")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACB")

    ChrTalk(
        0x9,
        (
            "#10303FSo all this Pleroma Grass\x01",
            "was blooming in a place\x01",
            "like this, eh?\x02\x03",
            "#10302FI wonder if... the\x01",
            "flowers are the source of\x01",
            "all this mist around us?\x02\x03",
            "#10304FAnyway, we should proceed\x01",
            "carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B37")

    label("loc_1ACB")


    ChrTalk(
        0x9,
        (
            "#10302FI wonder if this mist is\x01",
            "due to the Pleroma\x01",
            "Grass.\x02\x03",
            "#10304FAnyway, we should\x01",
            "proceed carefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B37")

    Jump("loc_18E8")

    label("loc_1B3C")

    TalkEnd(0xFE)
    Return()

    # Function_9_18DB end

    def Function_10_1B40(): pass

    label("Function_10_1B40")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
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
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C02")
    OP_E2(0x2)
    MiniGame(0x6, 0x6, 0x328C, 0xFFFFFE0C, 0xFFFFE322, 0xB4, 0x3836, 0xFFFFFE0C, 0xFFFFC7E8)

    label("loc_1C02")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1B40 end

    def Function_11_1C07(): pass

    label("Function_11_1C07")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C39")
    SetScenarioFlags(0x31, 2)

    label("loc_1C39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1C79")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C6E")
    Sound(2499, 255, 100, 0)
    Jump("loc_1C74")

    label("loc_1C6E")

    Sound(3537, 255, 100, 0)

    label("loc_1C74")

    Jump("loc_1C7F")

    label("loc_1C79")

    Sound(3344, 255, 100, 0)

    label("loc_1C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1CF4")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CD4"),
        (SWITCH_DEFAULT, "loc_1CE5"),
    )


    label("loc_1CD4")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CEF")

    label("loc_1CE5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CEF")

    Jump("loc_1F31")

    label("loc_1CF4")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1D26")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_1D26")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D5A"),
        (1, "loc_1E5E"),
        (2, "loc_1EEF"),
        (SWITCH_DEFAULT, "loc_1F27"),
    )


    label("loc_1D5A")

    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_74(0x7, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D8B")
    OP_70(0x7, 0x12C)
    OP_71(0x7, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_1D9B")

    label("loc_1D8B")

    OP_70(0x7, 0xF0)
    OP_71(0x7, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_1D9B")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DF1")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E14")
    Sound(461, 0, 100, 0)

    label("loc_1E14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E34")
    OP_70(0x7, 0x14A)
    OP_71(0x7, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_1E44")

    label("loc_1E34")

    OP_70(0x7, 0x10E)
    OP_71(0x7, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_1E44")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x7, "light", 0x1, 0x1)
    OP_70(0x7, 0x0)
    Jump("loc_1C7F")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1ED0")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_1E93")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1EAB")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1EA6")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1EAB")

    label("loc_1EA6")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1EAB")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EEA")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1EE0")
    OP_AF(0xFB)
    Jump("loc_1EEA")

    label("loc_1EE0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EEA")

    Jump("loc_1F31")

    label("loc_1EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F08")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F22")

    label("loc_1F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1F18")
    OP_AF(0xFB)
    Jump("loc_1F22")

    label("loc_1F18")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F22")

    Jump("loc_1F31")

    label("loc_1F27")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F31")

    Jump("loc_1C7F")

    label("loc_1F36")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_11_1C07 end

    def Function_12_1F44(): pass

    label("Function_12_1F44")

    OP_9C(0xFE, 0xFFFFAC04, 0x0, 0xFFFFAC04, 0x32, 0x3)
    Return()

    # Function_12_1F44 end

    def Function_13_1F5C(): pass

    label("Function_13_1F5C")

    OP_9C(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x32, 0x5)
    Return()

    # Function_13_1F5C end

    def Function_14_1F74(): pass

    label("Function_14_1F74")

    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x32, 0xA)
    Return()

    # Function_14_1F74 end

    def Function_15_1F8C(): pass

    label("Function_15_1F8C")

    OP_9C(0xFE, 0xFFFFEE6C, 0x0, 0x0, 0x32, 0xA)
    Return()

    # Function_15_1F8C end

    def Function_16_1FA4(): pass

    label("Function_16_1FA4")

    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x32, 0xA)
    Return()

    # Function_16_1FA4 end

    def Function_17_1FBC(): pass

    label("Function_17_1FBC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2006")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_17_1FBC")

    label("loc_2006")

    Return()

    # Function_17_1FBC end

    def Function_18_2007(): pass

    label("Function_18_2007")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2051")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -750, -5000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("Function_18_2007")

    label("loc_2051")

    Return()

    # Function_18_2007 end

    def Function_19_2052(): pass

    label("Function_19_2052")

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

    # Function_19_2052 end

    def Function_20_20B5(): pass

    label("Function_20_20B5")

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

    # Function_20_20B5 end

    def Function_21_2118(): pass

    label("Function_21_2118")

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

    # Function_21_2118 end

    def Function_22_216C(): pass

    label("Function_22_216C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2208")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis263.itp")
    Jump("loc_2234")

    label("loc_2208")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis264.itp")

    label("loc_2234")

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

    def lambda_2421():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2421)

    def lambda_242E():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_242E)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 14)
    BeginChrThread(0x109, 1, 0, 14)
    WaitChrThread(0xB, 1)

    def lambda_244F():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_244F)

    def lambda_245C():
        OP_93(0xFE, 0x13B, 0xC8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_245C)
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

    def lambda_24E2():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24E2)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 16)
    BeginChrThread(0x109, 1, 0, 16)
    Sleep(300)

    def lambda_2502():
        OP_9B(0x1, 0xFE, 0x159, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2502)
    Sleep(200)
    EndChrThread(0x109, 0x3)
    Sleep(200)

    def lambda_2521():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2521)
    WaitChrThread(0x105, 2)
    Sleep(400)
    WaitChrThread(0xB, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x21)
    BeginChrThread(0x104, 1, 0, 19)
    Sleep(200)

    def lambda_2556():
        OP_9B(0x1, 0xFE, 0x1E, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2556)
    Sleep(200)
    WaitChrThread(0x105, 2)
    SetChrChipByIndex(0x105, 0x23)
    BeginChrThread(0x105, 1, 0, 19)
    WaitChrThread(0x104, 1)

    def lambda_2580():
        OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2580)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x103, 1)

    def lambda_259D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_259D)
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

    def lambda_269C():
        OP_9B(0x0, 0xFE, 0x0, 0x1450, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_269C)

    def lambda_26B1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26B1)

    def lambda_26C6():
        OP_9B(0x0, 0xFE, 0xB, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26C6)

    def lambda_26DB():
        OP_9B(0x0, 0xFE, 0x5, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26DB)

    def lambda_26F0():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26F0)
    Sleep(850)
    SetChrChipByIndex(0x109, 0x22)
    BeginChrThread(0x109, 1, 0, 20)
    WaitChrThread(0x109, 1)

    def lambda_2716():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2716)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(150)

    def lambda_2736():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2736)
    Sleep(250)

    def lambda_2746():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2746)
    WaitChrThread(0x109, 2)

    def lambda_2757():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2757)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    Sleep(250)

    ChrTalk(
        0x101,
        "#00007F#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#5PT-That looks like the\x01",
            "boat Ling and Eolia came\x01",
            "here on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10310F#11P...No way... To think\x01",
            "things turned out like\x01",
            "this...\x02",
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

    def lambda_29E2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29E2)
    Sleep(100)

    def lambda_29FA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29FA)
    Sleep(100)

    def lambda_2A12():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A12)
    Sleep(50)

    def lambda_2A2A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A2A)
    Sleep(50)

    def lambda_2A42():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A42)
    Sleep(100)

    def lambda_2A5A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A5A)
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
            "#00301F#12PHey now... Are we havin'\x01",
            "a dream...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PIt really seems like\x01",
            "we're inside a fairy\x01",
            "tale...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PU-Unbelievable...\x02\x03",
            "#00201FIt looks like the\x01",
            "composition of space itself\x01",
            "is different from reality...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00010F#6PPleroma Grass... Since\x01",
            "when has there been this\x01",
            "much of it here?\x02\x03",
            "#00003FBut, that's right... What\x01",
            "Joachim was harvesting as\x01",
            "a Gnosis ingredient was─\x02",
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
        "Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#N#5PWell if you think about\x01",
            "it, this must be the\x01",
            "place.\x07\x00\x02",
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

    def lambda_2DC4():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DC4)

    def lambda_2DD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2DD9)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105F#6PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#6PY-You're that...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#5PYin... Why are you\x01",
            "here!?\x02",
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
            "That's my line.\x02\x03",
            "The shadows of the Snake and the\x01",
            "demonization of the delinquents'\x01",
            "leader...\x02\x03",
            "Azure flowers starting to bloom all\x01",
            "over the place and the appearance\x01",
            "of mysterious Cryptids...\x02\x03",
            "To think I'd run into you all as I\x01",
            "was following those signs...\x07\x00\x02",
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
        "#10305F#6PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PYou mean you guessed that\x01",
            "this place was suspicious\x01",
            "and came to investigate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11PPrecisely.\x02\x03",
            "#00702FHmm, it appears your\x01",
            "situation is a bit\x01",
            "different, correct?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#6PY-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PCircumstances being what\x01",
            "they are, allow me to\x01",
            "explain...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained the events\x01",
            "since Ling and Eolia\x01",
            "went missing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P─I see, so that boat\x01",
            "belongs to the bracers.\x02\x03",
            "#00702FHehe, I see... That being\x01",
            "the case, it appears I'm\x01",
            "getting close to the core.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PThe core...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PWhy the azure flowers─ Why Pleroma Grass\x01",
            "has begun to bloom all over Crossbell\x01",
            "and Cryptids have begun to appear...\x02\x03",
            "#10301F"What meaning does that have" for\x01",
            "Crossbell. That's the "core" isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11PHehe, precisely.\x02\x03",
            "#00700FThis is a part of my\x01",
            "contract with Heiyue as\x01",
            "well.\x02\x03",
            "I'll leave the bracers\x01",
            "to you and go on ahe─\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P─No.\x02\x03",
            "#00000FYin... Why don't you\x01",
            "come with us?\x02",
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

    def lambda_342D():

        label("loc_342D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_342D")

    QueueWorkItem2(0x102, 2, lambda_342D)
    Sleep(100)

    def lambda_3442():

        label("loc_3442")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3442")

    QueueWorkItem2(0x104, 2, lambda_3442)
    Sleep(100)

    def lambda_3457():

        label("loc_3457")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3457")

    QueueWorkItem2(0x103, 2, lambda_3457)
    Sleep(50)

    def lambda_346C():

        label("loc_346C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_346C")

    QueueWorkItem2(0x109, 2, lambda_346C)
    Sleep(50)

    def lambda_3481():

        label("loc_3481")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3481")

    QueueWorkItem2(0x105, 2, lambda_3481)
    Sleep(200)

    ChrTalk(
        0x109,
        "#10111F#6PLloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305F#6PHey now, you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#12P*sigh", I had a feeling\x01",
            "you'd say something like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PJust as I predicted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PMan. In times like these, I\x01",
            "want to say you're a little\x01",
            "too flexible or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2629, 255, 100, 0)
    Sleep(500)

    def lambda_35AD():

        label("loc_35AD")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_35AD")

    QueueWorkItem2(0x102, 2, lambda_35AD)
    Sleep(100)

    def lambda_35C2():

        label("loc_35C2")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_35C2")

    QueueWorkItem2(0x104, 2, lambda_35C2)
    Sleep(150)

    def lambda_35D7():

        label("loc_35D7")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_35D7")

    QueueWorkItem2(0x103, 2, lambda_35D7)
    Sleep(100)

    def lambda_35EC():

        label("loc_35EC")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_35EC")

    QueueWorkItem2(0x109, 2, lambda_35EC)
    Sleep(50)

    def lambda_3601():

        label("loc_3601")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_3601")

    QueueWorkItem2(0x105, 2, lambda_3601)
    Sleep(200)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P...Bannings. Aren't you\x01",
            "misunderstanding\x01",
            "something?\x02\x03",
            "Our positions differ to\x01",
            "begin with, and so do\x01",
            "our interests.\x02\x03",
            "Unlike that time at the\x01",
            "hospital, cooperating\x01",
            "with you would bring me─\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PNothing─ That's what you were going\x01",
            "to say, right?\x02\x03",
            "#00001FLing and Eolia are so skilled as to\x01",
            "have almost reached A-rank.\x02\x03",
            "When they join forces, the skills\x01",
            "they possess would even be match for\x01",
            "Arios.\x02\x03",
            "#00006FIf there's danger great enough to\x01",
            "cut off their contact with the\x01",
            "outside world waiting for us here...\x02\x03",
            "#00013FCan you really say you'll be fine by\x01",
            "yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P............\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#5PWell, it is an emergency\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#6PIf Ling and Eolia are\x01",
            "safe, you might be able\x01",
            "to learn something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PEven from the standpoint of\x01",
            "efficiency, you should be\x01",
            "able to cooperate with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P...Hehe...\x02\x03",
            "The "Special Support Section"... It\x01",
            "appears you've taken quite a lot of\x01",
            "inspiration from your leader, eh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112F#6PP-Perhaps?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6PWell, I can't deny it\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#5P...It was slightly\x01",
            "unintentional, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3A85():

        label("loc_3A85")

        OP_93(0xFE, 0x159, 0x1F4)
        Yield()
        Jump("loc_3A85")

    QueueWorkItem2(0x101, 2, lambda_3A85)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00011F#5PHey, why is all of this\x01",
            "my fault?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#6PHehe... This is one of\x01",
            "your virtues too, isn't\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B27():

        label("loc_3B27")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_3B27")

    QueueWorkItem2(0x101, 2, lambda_3B27)
    Sleep(100)
    Sleep(250)

    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P─Very well. We'll\x01",
            "temporarily join forces\x01",
            "once again.\x02\x03",
            "#00700FHowever, when the Divine\x01",
            "Blade of Wind catches up\x01",
            "with us, I'll leave.\x02\x03",
            "Is that all right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYeah, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PBut with this many, our\x01",
            "maneuverability going to\x01",
            "be limited.\x02\x03",
            "#00301FWe'll be helpless if\x01",
            "monsters attack.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C88():

        label("loc_3C88")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3C88")

    QueueWorkItem2(0x101, 2, lambda_3C88)
    Sleep(50)

    def lambda_3C9D():

        label("loc_3C9D")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3C9D")

    QueueWorkItem2(0x102, 2, lambda_3C9D)
    Sleep(50)

    def lambda_3CB2():

        label("loc_3CB2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3CB2")

    QueueWorkItem2(0x103, 2, lambda_3CB2)
    Sleep(50)

    def lambda_3CC7():

        label("loc_3CC7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3CC7")

    QueueWorkItem2(0x109, 2, lambda_3CC7)
    Sleep(50)

    def lambda_3CDC():

        label("loc_3CDC")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3CDC")

    QueueWorkItem2(0x105, 2, lambda_3CDC)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#10103F#12PThen, maybe we should\x01",
            "leave someone here\x01",
            "alone.\x02\x03",
            "#10101FWe may need someone to\x01",
            "watch the boat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PWell why not? They could get\x01",
            "in touch with the Divine Blade\x01",
            "of Wind when he arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PGot it. Let me think\x01",
            "about the formation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-2600, 1500, 2120, 3000)
    MoveCamera(182, 16, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(18630, 3000)

    def lambda_3E2F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E2F)
    Sleep(50)

    def lambda_3E3F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E3F)
    Sleep(50)

    def lambda_3E4F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3E4F)
    Sleep(50)

    def lambda_3E5F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E5F)
    Sleep(50)

    def lambda_3E6F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3E6F)
    Sleep(50)

    def lambda_3E7F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3E7F)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F73")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    FadeToDark(0, 0, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F#1P(I still haven't repaid\x01",
            "them for the move they\x01",
            "taught me...)\x02\x03",
            "#00013F(I must find Ling and\x01",
            "Eolia at all costs and\x01",
            "confirm their safety!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Jump("loc_4053")

    label("loc_3F73")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    FadeToDark(0, 0, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F#1P(It was harsh in the\x01",
            "beginning, but recently we've\x01",
            "built a good relationship...)\x02\x03",
            "#00001F(I must find them at all\x01",
            "costs and confirm their\x01",
            "safety!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    label("loc_4053")

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
            "#1KWho will you leave\x01",
            "behind?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Wazy]\x01",       # 0
            "[Noｱl]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_40CC"),
        (0, "loc_40E4"),
        (SWITCH_DEFAULT, "loc_40FC"),
    )


    label("loc_40CC")

    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    Jump("loc_40FC")

    label("loc_40E4")

    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    Jump("loc_40FC")

    label("loc_40FC")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41D7")
    Jump("loc_41DC")

    label("loc_41D7")

    OP_29(0x80, 0x4, 0x40)

    label("loc_41DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41ED")
    Jump("loc_41F2")

    label("loc_41ED")

    OP_29(0x83, 0x4, 0x40)

    label("loc_41F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4203")
    Jump("loc_4208")

    label("loc_4203")

    OP_29(0x88, 0x4, 0x40)

    label("loc_4208")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4219")
    Jump("loc_421E")

    label("loc_4219")

    OP_29(0x8B, 0x4, 0x40)

    label("loc_421E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_422F")
    Jump("loc_4234")

    label("loc_422F")

    OP_29(0x8C, 0x4, 0x40)

    label("loc_4234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4245")
    Jump("loc_424A")

    label("loc_4245")

    OP_29(0x8D, 0x4, 0x40)

    label("loc_424A")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_66(0x6, 0x1)
    OP_24(0x1E3)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_216C end

    def Function_23_426B(): pass

    label("Function_23_426B")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A small boat is docked here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4312")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4312")

    ChrTalk(
        0x101,
        (
            "#00001FThis is the boat those\x01",
            "two used.\x02\x03",
            "...Anyway, let's hurry\x01",
            "further inside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4312")

    EventEnd(0x3)
    Return()

    # Function_23_426B end

    SaveToFile()

Try(main)
