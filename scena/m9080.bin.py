from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9080.bin",                # FileName
        "m9080",                    # MapName
        "m9080",                    # Location
        0x00C3,                     # MapIndex
        "ed7356",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 195, 0, 2, 0, 3],
    )

    BuildStringList((
        "m9080",                  # 0
        "Tio",                    # 1
        "パズス",                 # 2
        "パズス",                 # 3
        "アストラルドミナ",       # 4
        "アストラルドミナ",       # 5
        "アストラルドミナ",       # 6
        "bm9060",                 # 7
        "bm9060",                 # 8
        "bm9060",                 # 9
        "bm9060",                 # 10
        "bm9060",                 # 11
        "bm9060",                 # 12
        "bm9060",                 # 13
        "bm9060",                 # 14
        "bm9060",                 # 15
    ))

    ATBonus("ATBonus_5D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_5E4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4FE5", 15,  15,  15,  15,  5,   5,   5)
    Sepith("Sepith_4FDD", 15,  6,   15,  6,   6,   9,   15)
    Sepith("Sepith_4FD5", 9,   15,  9,   22,  4,   10,  7)
    Sepith("Sepith_4FED", 12,  19,  14,  20,  8,   4,   5)

    MonsterBattlePostion("MonsterBattlePostion_624", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_628", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_62C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_688", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_68C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_690", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_694", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_698", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_69C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_604", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_620", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 11, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 2, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 14, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 0, 0, 180)

    # monster count: 17

    BattleInfo(
        "BattleInfo_7FC", 0x0000, 110, 6, 60, 6, 1, 30, 0, "bm9060", "Sepith_4FE5", 50, 30, 20, 0,
        (
            ("ms85301.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms85301.dat", "ms85301.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms85301.dat", "ms85301.dat", "ms85301.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_760", 0x0000, 110, 6, 60, 6, 1, 40, 0, "bm9060", "Sepith_4FDD", 50, 30, 20, 0,
        (
            ("ms79301.dat", "ms79301.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms79301.dat", "ms79301.dat", "ms79301.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6C4", 0x0010, 110, 6, 60, 6, 1, 40, 0, "bm9060", "Sepith_4FD5", 50, 30, 20, 0,
        (
            ("ms81300.dat", 0, 0, 0, 0, 0, "ms79301.dat", 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms81300.dat", "ms81300.dat", 0, 0, 0, 0, "ms79301.dat", 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms81300.dat", "ms81300.dat", "ms81300.dat", 0, 0, 0, "ms79301.dat", 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_898", 0x0000, 110, 6, 60, 6, 1, 25, 0, "bm9060", "Sepith_4FED", 40, 30, 20, 10,
        (
            ("ms78500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms78500.dat", "ms79301.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms78500.dat", "ms79301.dat", "ms79301.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms78500.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_960", 0x0C10, 255, 6, 0, 0, 3, 0, 0, "bm9060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81300.dat", "ms81300.dat", "ms81300.dat", "ms81300.dat", "ms81300.dat", "ms81300.dat", "ms79301.dat", 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9A4", 0x0C10, 255, 6, 0, 0, 3, 0, 0, "bm9060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81300.dat", "ms81300.dat", "ms81300.dat", "ms81300.dat", "ms81300.dat", "ms81300.dat", "ms79301.dat", 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9E8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms78500.dat", "ms78500.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A2C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms78500.dat", "ms78500.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A70", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms78500.dat", "ms78500.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5E4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
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
        "monster/ch81350.itc",               # 10
        "monster/ch81350.itc",               # 11
        "monster/ch79350.itc",               # 12
        "monster/ch79350.itc",               # 13
        "monster/ch85350.itc",               # 14
        "monster/ch85350.itc",               # 15
        "monster/ch78550.itc",               # 16
        "monster/ch78550.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    508,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294953296, 500,     62000,   0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(22000,   500,     30000,   0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(8000,    500,     35500,   0,    484,  0x0, 0,   22,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(4294933296, 500,     109500,  0,    484,  0x0, 0,   22,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(52000,   500,     80000,   0,    484,  0x0, 0,   22,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294945256, 43680,   0,       0x10100B6,    "BattleInfo_7FC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(32110,   45650,   4000,    0x1010101,    "BattleInfo_760", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(66940,   48610,   0,       0x10100F5,    "BattleInfo_6C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(72390,   84380,   4000,    0x1010093,    "BattleInfo_898", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(74410,   121040,  4000,    0x10100E2,    "BattleInfo_7FC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(26440,   127580,  0,       0x1010086,    "BattleInfo_760", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294926676, 140600,  0,       0x1010077,    "BattleInfo_6C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294890326, 114330,  4294963296, 0x101005C,    "BattleInfo_7FC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294897706, 59610,   4294963296, 0x101001A,    "BattleInfo_898", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294914506, 99280,   4294963296, 0x101008E,    "BattleInfo_760", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(39530,   104710,  0,       0x1010109,    "BattleInfo_6C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(92680,   100870,  4294959296, 0x1010114,    "BattleInfo_7FC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(84410,   56050,   4294963296, 0x1010013,    "BattleInfo_898", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(83720,   27930,   4294963296, 0x101014E,    "BattleInfo_760", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(49660,   28070,   4294963296, 0x1010087,    "BattleInfo_760", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(26970,   75970,   0,       0x101004E,    "BattleInfo_760", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294921056, 69420,   4000,    0x101002C,    "BattleInfo_898", 0,   22,  0xFFFF, 6,  7)

    DeclActor(4294945296, 0,       47000,   1200,    4294945296, 1000,    47000,   0x007C, 0,  4,  0x0000)
    DeclActor(82000,   4000,    126000,  1200,    82000,   5000,    126000,  0x007C, 0,  5,  0x0000)
    DeclActor(4294953296, 0,       62000,   1200,    4294953296, 1000,    62000,   0x007C, 0,  6,  0x0000)
    DeclActor(22000,   0,       30000,   1200,    22000,   1000,    30000,   0x007C, 0,  7,  0x0000)
    DeclActor(96000,   4294959296, 111000,  1200,    96000,   4294960296, 111000,  0x007C, 0,  8,  0x0000)
    DeclActor(8000,    0,       35500,   1200,    8000,    1000,    35500,   0x007C, 0,  9,  0x0000)
    DeclActor(4294933296, 0,       109500,  1200,    4294933296, 1000,    109500,  0x007C, 0,  10, 0x0000)
    DeclActor(52000,   0,       80000,   1200,    52000,   1000,    80000,   0x007C, 0,  11, 0x0000)
    DeclActor(8000,    0,       44000,   1200,    8000,    1000,    44000,   0x007C, 0,  14, 0x0000)
    DeclActor(4294931296, 0,       100000,  1200,    4294931296, 1000,    100000,  0x007C, 0,  15, 0x0000)
    DeclActor(4294931296, 0,       44000,   1200,    4294931296, 1000,    44000,   0x007C, 0,  16, 0x0000)
    DeclActor(4294950296, 0,       135000,  1200,    4294950296, 1000,    135000,  0x007C, 0,  17, 0x0000)
    DeclActor(17000,   0,       107000,  1200,    17000,   1000,    107000,  0x007C, 0,  18, 0x0000)
    DeclActor(4294950296, 0,       79000,   1200,    4294950296, 1000,    79000,   0x007C, 0,  19, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 2, 1])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_B80",          # 00, 0
        "Function_1_B9F",          # 01, 1
        "Function_2_BBE",          # 02, 2
        "Function_3_BE1",          # 03, 3
        "Function_4_2183",         # 04, 4
        "Function_5_223E",         # 05, 5
        "Function_6_238F",         # 06, 6
        "Function_7_25AA",         # 07, 7
        "Function_8_27C5",         # 08, 8
        "Function_9_2916",         # 09, 9
        "Function_10_2B31",        # 0A, 10
        "Function_11_2D4C",        # 0B, 11
        "Function_12_2F67",        # 0C, 12
        "Function_13_31EF",        # 0D, 13
        "Function_14_3342",        # 0E, 14
        "Function_15_3476",        # 0F, 15
        "Function_16_35AB",        # 10, 16
        "Function_17_36DF",        # 11, 17
        "Function_18_3945",        # 12, 18
        "Function_19_3BAB",        # 13, 19
        "Function_20_3E11",        # 14, 20
        "Function_21_4C51",        # 15, 21
        "Function_22_4CBB",        # 16, 22
        "Function_23_4D25",        # 17, 23
        "Function_24_4D8F",        # 18, 24
        "Function_25_4DF9",        # 19, 25
        "Function_26_4E63",        # 1A, 26
    ))


    def Function_0_B80(): pass

    label("Function_0_B80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_B80")

    label("loc_B9E")

    Return()

    # Function_0_B80 end

    def Function_1_B9F(): pass

    label("Function_1_B9F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBD")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_B9F")

    label("loc_BBD")

    Return()

    # Function_1_B9F end

    def Function_2_BBE(): pass

    label("Function_2_BBE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCF")
    Event(0, 12)

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE0")
    Event(0, 20)

    label("loc_BE0")

    Return()

    # Function_2_BBE end

    def Function_3_BE1(): pass

    label("Function_3_BE1")

    OP_F0(0x1, 0x320)
    OP_1B(0x6, 0x0, 0xD)
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1D10")
    SetMapObjFrame(0xFF, "obj_00", 0x0, 0x1)

    label("loc_1D10")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 7500, 0, 44000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 8500, 0, 44000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -36500, 0, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -35500, 0, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -36500, 0, 44000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -35500, 0, 44000, 4000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 1)), scpexpr(EXPR_END)), "loc_1DDC")
    OP_70(0x9, 0x3C)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    OP_65(0x8, 0x1)
    Jump("loc_1DE8")

    label("loc_1DDC")

    OP_70(0x9, 0x0)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)

    label("loc_1DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 2)), scpexpr(EXPR_END)), "loc_1E06")
    OP_70(0xA, 0x3C)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    OP_65(0x9, 0x1)
    Jump("loc_1E12")

    label("loc_1E06")

    OP_70(0xA, 0x0)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 3)), scpexpr(EXPR_END)), "loc_1E30")
    OP_70(0xB, 0x3C)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    OP_65(0xA, 0x1)
    Jump("loc_1E3C")

    label("loc_1E30")

    OP_70(0xB, 0x0)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_1E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1E72")
    SetMapObjFrame(0xFF, "CA_stop0", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x1, 0x2)
    OP_70(0xF, 0xF)
    OP_70(0x6, 0x96)
    Jump("loc_1ED0")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_1EA8")
    SetMapObjFrame(0xFF, "CA_stop0", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x0, 0x2)
    OP_70(0xF, 0xF)
    OP_70(0x6, 0x3C)
    Jump("loc_1ED0")

    label("loc_1EA8")

    SetMapObjFrame(0xFF, "CA_stop0", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x1, 0x2)
    OP_70(0xF, 0x0)
    OP_70(0x6, 0x0)

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1F06")
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x1, 0x2)
    OP_70(0x10, 0xF)
    OP_70(0x7, 0x96)
    Jump("loc_1F64")

    label("loc_1F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_1F3C")
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x0, 0x2)
    OP_70(0x10, 0xF)
    OP_70(0x7, 0x3C)
    Jump("loc_1F64")

    label("loc_1F3C")

    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x1, 0x2)
    OP_70(0x10, 0x0)
    OP_70(0x7, 0x0)

    label("loc_1F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1F9A")
    SetMapObjFrame(0xFF, "CA_stop4", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x1, 0x2)
    OP_70(0x11, 0xF)
    OP_70(0x8, 0x96)
    Jump("loc_1FF8")

    label("loc_1F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_1FD0")
    SetMapObjFrame(0xFF, "CA_stop4", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x0, 0x2)
    OP_70(0x11, 0xF)
    OP_70(0x8, 0x3C)
    Jump("loc_1FF8")

    label("loc_1FD0")

    SetMapObjFrame(0xFF, "CA_stop4", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x1, 0x2)
    OP_70(0x11, 0x0)
    OP_70(0x8, 0x0)

    label("loc_1FF8")

    SetBarrier(0x0, 0x6, 0x1, 0x0, 0, 0, 117500, 4000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 0, 0, 89500, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_2048")
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jump("loc_206A")

    label("loc_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2059")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_2059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206A")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_206A")

    SetMapObjFrame(0xFF, "CA_stop0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop3", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop4", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA_stop5", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DD")
    OP_70(0x0, 0x0)
    Jump("loc_20E1")

    label("loc_20DD")

    OP_70(0x0, 0x1E)

    label("loc_20E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F4")
    OP_70(0x1, 0x0)
    Jump("loc_20F8")

    label("loc_20F4")

    OP_70(0x1, 0x1E)

    label("loc_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210B")
    OP_70(0x2, 0x0)
    Jump("loc_210F")

    label("loc_210B")

    OP_70(0x2, 0x1E)

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2122")
    OP_70(0x3, 0x0)
    Jump("loc_2126")

    label("loc_2122")

    OP_70(0x3, 0x1E)

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2139")
    OP_70(0x4, 0x0)
    Jump("loc_213D")

    label("loc_2139")

    OP_70(0x4, 0x1E)

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2150")
    OP_70(0xC, 0x0)
    Jump("loc_2154")

    label("loc_2150")

    OP_70(0xC, 0x1E)

    label("loc_2154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2167")
    OP_70(0xD, 0x0)
    Jump("loc_216B")

    label("loc_2167")

    OP_70(0xD, 0x1E)

    label("loc_216B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217E")
    OP_70(0xE, 0x0)
    Jump("loc_2182")

    label("loc_217E")

    OP_70(0xE, 0x1E)

    label("loc_2182")

    Return()

    # Function_3_BE1 end

    def Function_4_2183(): pass

    label("Function_4_2183")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220E")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x3, 2000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I Wind Sepith x2000\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x206, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_222C")

    label("loc_220E")


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

    label("loc_222C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_2183 end

    def Function_5_223E(): pass

    label("Function_5_223E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233A")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xC5, 1)"), scpexpr(EXPR_END)), "loc_22C3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_2335")

    label("loc_22C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC5),
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

    label("loc_2335")

    Jump("loc_2383")

    label("loc_233A")

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

    label("loc_2383")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_223E end

    def Function_6_238F(): pass

    label("Function_6_238F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2560")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2492")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_23EC():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23EC)

    def lambda_2406():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2406)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_960", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2473"),
        (2, "loc_2482"),
        (1, "loc_248F"),
        (SWITCH_DEFAULT, "loc_2492"),
    )


    label("loc_2473")

    SetScenarioFlags(0x21A, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_2492")

    label("loc_2482")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_248F")

    OP_B9(0x0)
    Return()

    label("loc_2492")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x91, 1)"), scpexpr(EXPR_END)), "loc_24EB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x91),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_255B")

    label("loc_24EB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x91),
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

    label("loc_255B")

    Jump("loc_259E")

    label("loc_2560")

    FadeToDark(300, 0, 100)

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

    label("loc_259E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_238F end

    def Function_7_25AA(): pass

    label("Function_7_25AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277B")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AD")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2607():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2607)

    def lambda_2621():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2621)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_9A4", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_268E"),
        (2, "loc_269D"),
        (1, "loc_26AA"),
        (SWITCH_DEFAULT, "loc_26AD"),
    )


    label("loc_268E")

    SetScenarioFlags(0x21A, 2)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_26AD")

    label("loc_269D")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_26AA")

    OP_B9(0x0)
    Return()

    label("loc_26AD")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3F4, 1)"), scpexpr(EXPR_END)), "loc_2706")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_2776")

    label("loc_2706")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F4),
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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2776")

    Jump("loc_27B9")

    label("loc_277B")

    FadeToDark(300, 0, 100)

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

    label("loc_27B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_25AA end

    def Function_8_27C5(): pass

    label("Function_8_27C5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C1")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x58, 1)"), scpexpr(EXPR_END)), "loc_284A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x58),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_28BC")

    label("loc_284A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x58),
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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_28BC")

    Jump("loc_290A")

    label("loc_28C1")

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

    label("loc_290A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_27C5 end

    def Function_9_2916(): pass

    label("Function_9_2916")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE7")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A19")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2973():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2973)

    def lambda_298D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_298D)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_9E8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_29FA"),
        (2, "loc_2A09"),
        (1, "loc_2A16"),
        (SWITCH_DEFAULT, "loc_2A19"),
    )


    label("loc_29FA")

    SetScenarioFlags(0x21A, 3)
    OP_70(0xC, 0x1E)
    Sleep(500)
    Jump("loc_2A19")

    label("loc_2A09")

    OP_70(0xC, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2A16")

    OP_B9(0x0)
    Return()

    label("loc_2A19")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x376, 1)"), scpexpr(EXPR_END)), "loc_2A72")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x376),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x206, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_2AE2")

    label("loc_2A72")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x376),
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
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2AE2")

    Jump("loc_2B25")

    label("loc_2AE7")

    FadeToDark(300, 0, 100)

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

    label("loc_2B25")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2916 end

    def Function_10_2B31(): pass

    label("Function_10_2B31")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D02")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C34")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2B8E():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B8E)

    def lambda_2BA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2BA8)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_A2C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2C15"),
        (2, "loc_2C24"),
        (1, "loc_2C31"),
        (SWITCH_DEFAULT, "loc_2C34"),
    )


    label("loc_2C15")

    SetScenarioFlags(0x21A, 4)
    OP_70(0xD, 0x1E)
    Sleep(500)
    Jump("loc_2C34")

    label("loc_2C24")

    OP_70(0xD, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2C31")

    OP_B9(0x0)
    Return()

    label("loc_2C34")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x377, 1)"), scpexpr(EXPR_END)), "loc_2C8D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x377),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x207, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_2CFD")

    label("loc_2C8D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x377),
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
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2CFD")

    Jump("loc_2D40")

    label("loc_2D02")

    FadeToDark(300, 0, 100)

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

    label("loc_2D40")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2B31 end

    def Function_11_2D4C(): pass

    label("Function_11_2D4C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F1D")
    Sound(14, 0, 100, 0)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4F")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2DA9():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2DA9)

    def lambda_2DC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2DC3)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_A70", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2E30"),
        (2, "loc_2E3F"),
        (1, "loc_2E4C"),
        (SWITCH_DEFAULT, "loc_2E4F"),
    )


    label("loc_2E30")

    SetScenarioFlags(0x21A, 5)
    OP_70(0xE, 0x1E)
    Sleep(500)
    Jump("loc_2E4F")

    label("loc_2E3F")

    OP_70(0xE, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2E4C")

    OP_B9(0x0)
    Return()

    label("loc_2E4F")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x378, 1)"), scpexpr(EXPR_END)), "loc_2EA8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x378),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x207, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_2F18")

    label("loc_2EA8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x378),
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
    OP_71(0xE, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2F18")

    Jump("loc_2F5B")

    label("loc_2F1D")

    FadeToDark(300, 0, 100)

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

    label("loc_2F5B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_2D4C end

    def Function_12_2F67(): pass

    label("Function_12_2F67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_69(0x1, 0x0)
    OP_68(-600, 1000, -1660, 0)
    MoveCamera(38, 49, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13230, 0)
    SetChrPos(0x0, 0, 0, -3000, 0)
    SetChrPos(0x1, 0, 0, -3000, 0)
    SetChrPos(0x2, 0, 0, -3000, 0)
    SetChrPos(0x3, 0, 0, -3000, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_307B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_307B)

    def lambda_308C():
        OP_95(0xFE, -60, 0, -60, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_308C)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_30E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_30E3)

    def lambda_30F4():
        OP_95(0xFE, -1340, 0, -290, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_30F4)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3151():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_3151)

    def lambda_3162():
        OP_95(0xFE, 1210, 0, -300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3162)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_31B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_31B9)

    def lambda_31CA():
        OP_95(0xFE, -2480, 0, -850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_31CA)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_2F67 end

    def Function_13_31EF(): pass

    label("Function_13_31EF")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3248():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3248)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3293():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3293)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_32DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_32DE)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3329():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_3329)
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_13_31EF end

    def Function_14_3342(): pass

    label("Function_14_3342")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x376, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338C")
    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3475")

    label("loc_338C")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a silver gate. Use\x01",
            "the Argem Key?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346A")
    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(7690, 1000, 43860, 0)
    MoveCamera(42, 37, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13930, 0)
    OP_0D()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0x9, 0x0, 0x3C, 0x0, 0x0)
    Sleep(800)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    OP_65(0x8, 0x1)
    SetScenarioFlags(0x1B1, 1)

    label("loc_346A")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3475")

    Return()

    # Function_14_3342 end

    def Function_15_3476(): pass

    label("Function_15_3476")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x377, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C0")
    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_35AA")

    label("loc_34C0")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a golden gate. Use\x01",
            "the Goldia Key?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359F")
    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(-34980, 1000, 100140, 0)
    MoveCamera(53, 29, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16250, 0)
    OP_0D()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0xA, 0x0, 0x3C, 0x0, 0x0)
    Sleep(800)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    OP_65(0x9, 0x1)
    SetScenarioFlags(0x1B1, 2)

    label("loc_359F")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_35AA")

    Return()

    # Function_15_3476 end

    def Function_16_35AB(): pass

    label("Function_16_35AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x378, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F5")
    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_36DE")

    label("loc_35F5")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a black gate. Use\x01",
            "the Nohval Key?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D3")
    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(-38230, 1000, 45270, 0)
    MoveCamera(35, 44, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16250, 0)
    OP_0D()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0xB, 0x0, 0x3C, 0x0, 0x0)
    Sleep(800)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    OP_65(0xA, 0x1)
    SetScenarioFlags(0x1B1, 3)

    label("loc_36D3")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_36DE")

    Return()

    # Function_16_35AB end

    def Function_17_36DF(): pass

    label("Function_17_36DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3720")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever won't budge.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3939")

    label("loc_3720")

    EventBegin(0x1)
    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(-17640, 1000, 134430, 0)
    MoveCamera(12, 41, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x0, -17640, 0, 134430, 45)
    SetChrPos(0x1, -18540, 0, 135230, 45)
    SetChrPos(0x2, -18450, 0, 133490, 45)
    SetChrPos(0x3, -19380, 0, 134340, 45)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lever. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3939")
    Sound(143, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_37FA")
    ClearScenarioFlags(0x1B1, 4)
    Jump("loc_37FD")

    label("loc_37FA")

    SetScenarioFlags(0x1B1, 4)

    label("loc_37FD")

    OP_74(0xF, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_3821")
    OP_71(0xF, 0x0, 0xF, 0x0, 0x0)
    OP_79(0xF)
    Sleep(500)
    Jump("loc_3833")

    label("loc_3821")

    OP_71(0xF, 0xF, 0x3C, 0x0, 0x0)
    OP_79(0xF)
    Sleep(500)

    label("loc_3833")

    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(-2970, 1000, 129620, 0)
    MoveCamera(34, 44, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36310, 0)
    OP_0D()
    Sleep(1000)
    Sound(155, 2, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    OP_74(0x6, 0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_38C3")
    OP_71(0x6, 0x0, 0x3C, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop0", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x0, 0x2)
    Jump("loc_38EF")

    label("loc_38C3")

    OP_71(0x6, 0x3C, 0x78, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop0", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x1, 0x2)

    label("loc_38EF")

    OP_79(0x6)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3928")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_3928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3939")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_3939")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_36DF end

    def Function_18_3945(): pass

    label("Function_18_3945")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3986")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever won't budge.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3B9F")

    label("loc_3986")

    EventBegin(0x1)
    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(18330, 1000, 106050, 0)
    MoveCamera(342, 48, 0, 0)
    OP_6E(840, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x0, 17730, 0, 106210, 315)
    SetChrPos(0x1, 18760, 0, 107080, 315)
    SetChrPos(0x2, 18850, 0, 105290, 315)
    SetChrPos(0x3, 19690, 0, 106050, 315)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lever. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9F")
    Sound(143, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_3A60")
    ClearScenarioFlags(0x1B1, 5)
    Jump("loc_3A63")

    label("loc_3A60")

    SetScenarioFlags(0x1B1, 5)

    label("loc_3A63")

    OP_74(0x10, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_3A87")
    OP_71(0x10, 0x0, 0xF, 0x0, 0x0)
    OP_79(0x10)
    Sleep(500)
    Jump("loc_3A99")

    label("loc_3A87")

    OP_71(0x10, 0xF, 0x3C, 0x0, 0x0)
    OP_79(0x10)
    Sleep(500)

    label("loc_3A99")

    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(2070, 1000, 102780, 0)
    MoveCamera(326, 43, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36300, 0)
    OP_0D()
    Sleep(1000)
    Sound(155, 2, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    OP_74(0x7, 0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_3B29")
    OP_71(0x7, 0x0, 0x3C, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x0, 0x2)
    Jump("loc_3B55")

    label("loc_3B29")

    OP_71(0x7, 0x3C, 0x78, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x1, 0x2)

    label("loc_3B55")

    OP_79(0x7)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B8E")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_3B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B9F")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_3B9F")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_3945 end

    def Function_19_3BAB(): pass

    label("Function_19_3BAB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3BEC")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever won't budge.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3E05")

    label("loc_3BEC")

    EventBegin(0x1)
    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(-18000, 1000, 76890, 0)
    MoveCamera(9, 36, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x0, -17850, 0, 78240, 45)
    SetChrPos(0x1, -18740, 0, 79060, 45)
    SetChrPos(0x2, -18730, 0, 77330, 45)
    SetChrPos(0x3, -19760, 0, 78030, 45)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lever. Operate?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E05")
    Sound(143, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_3CC6")
    ClearScenarioFlags(0x1B1, 6)
    Jump("loc_3CC9")

    label("loc_3CC6")

    SetScenarioFlags(0x1B1, 6)

    label("loc_3CC9")

    OP_74(0x11, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_3CED")
    OP_71(0x11, 0x0, 0xF, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)
    Jump("loc_3CFF")

    label("loc_3CED")

    OP_71(0x11, 0xF, 0x3C, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)

    label("loc_3CFF")

    Fade(500)
    OP_69(0x2, 0x0)
    OP_68(-2180, 1000, 74430, 0)
    MoveCamera(37, 46, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36310, 0)
    OP_0D()
    Sleep(1000)
    Sound(155, 2, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xFA0)
    OP_74(0x8, 0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_3D8F")
    OP_71(0x8, 0x0, 0x3C, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop4", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x0, 0x2)
    Jump("loc_3DBB")

    label("loc_3D8F")

    OP_71(0x8, 0x3C, 0x78, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop4", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x1, 0x2)

    label("loc_3DBB")

    OP_79(0x8)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF4")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_3DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E05")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_3E05")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_3BAB end

    def Function_20_3E11(): pass

    label("Function_20_3E11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_69(0x3, 0x0)
    SoundLoad(3327)
    SoundLoad(3328)
    SoundLoad(3329)
    SetChrPos(0x101, 0, 50, -3000, 0)
    SetChrPos(0x102, 0, 50, -3000, 19)
    SetChrPos(0x103, 0, 50, -3000, 6)
    SetChrPos(0x104, 0, 50, -3000, 342)
    SetChrPos(0xF4, 0, 50, -3000, 32)
    SetChrPos(0xF5, 0, 50, -3000, 332)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x8, 0x80)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -3000, 0, -3650, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis008.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00001.itp")
    OP_68(22990, -260, 64180, 0)
    MoveCamera(32, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(52020, 0)
    OP_68(-2500, -260, 35000, 5500)
    MoveCamera(32, 24, 0, 5500)
    OP_6E(700, 5500)
    SetCameraDistance(46020, 5500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(0, 1000, 6500, 0)
    MoveCamera(358, 33, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21020, 0)
    OP_68(0, 1000, 6500, 6500)
    MoveCamera(359, 21, 0, 6500)
    OP_6E(800, 6500)
    SetCameraDistance(39340, 6500)
    Fade(500)
    Sleep(1500)
    PlaceName2(340, 200, "c_plac61", 0x0, 0)
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 21)
    Sleep(600)
    Sound(920, 0, 80, 0)
    BeginChrThread(0x102, 0, 0, 22)
    Sleep(600)
    BeginChrThread(0x104, 0, 0, 23)
    Sleep(600)
    Sound(920, 0, 80, 0)
    BeginChrThread(0x103, 0, 0, 24)
    Sleep(600)
    BeginChrThread(0xF4, 0, 0, 25)
    Sleep(600)
    Sound(920, 0, 80, 0)
    BeginChrThread(0xF5, 0, 0, 26)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(340, 1000, 3110, 0)
    MoveCamera(27, 18, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12830, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_411B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40EF")
    OP_FC(0xC)
    Jump("loc_40F2")

    label("loc_40EF")

    OP_FC(0xC)

    label("loc_40F2")


    ChrTalk(
        0x106,
        "#10712F#13P...This place is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_41BE")

    label("loc_411B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_416E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4145")
    OP_FC(0xC)
    Jump("loc_4148")

    label("loc_4145")

    OP_FC(0xC)

    label("loc_4148")


    ChrTalk(
        0x105,
        "#10405F#13PThis place is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_41BE")

    label("loc_416E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4198")
    OP_FC(0xC)
    Jump("loc_419B")

    label("loc_4198")

    OP_FC(0xC)

    label("loc_419B")


    ChrTalk(
        0x109,
        "#10113F#13PT-This place is...\x02",
    )

    CloseMessageWindow()

    label("loc_41BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4225")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41E8")
    OP_FC(0xC)
    Jump("loc_41EB")

    label("loc_41E8")

    OP_FC(0xC)

    label("loc_41EB")


    ChrTalk(
        0x10A,
        (
            "#00601F#13PThis place is MacLaine's\x01",
            "interior...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F5")

    label("loc_4225")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4288")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_424F")
    OP_FC(0xC)
    Jump("loc_4252")

    label("loc_424F")

    OP_FC(0xC)

    label("loc_4252")


    ChrTalk(
        0x109,
        (
            "#10113F#13PThis place is Arios'\x01",
            "interior...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42F5")

    label("loc_4288")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42F5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42B2")
    OP_FC(0xC)
    Jump("loc_42B5")

    label("loc_42B2")

    OP_FC(0xC)

    label("loc_42B5")


    ChrTalk(
        0x105,
        (
            "#10401F#13PThis place is the Divine\x01",
            "Blade's interior, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F5")


    ChrTalk(
        0x103,
        (
            "#00206F#12PInfinite "bindings"...\x01",
            "...There's too many of\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PArios... How much is he\x01",
            "shouldering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6P...Honestly... He's\x01",
            "burdened with too\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#11P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#11PEven the Ogre Rosso was on another\x01",
            "level, but what our current opponent\x01",
            "is shouldering is different.\x02\x03",
            "#00013FMost likely, what awaits us is a\x01",
            "battle fiercer than the one with the\x01",
            "Steel Maiden.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_44C7():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_44C7)
    Sleep(50)

    def lambda_44D7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_44D7)
    Sleep(50)

    def lambda_44E7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_44E7)
    Sleep(50)

    def lambda_44F7():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_44F7)
    Sleep(50)

    def lambda_4507():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4507)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PHowever─ We can't\x01",
            "retreat from here.\x02\x03",
            "#00001FTo get KeA back... and\x01",
            "to make the entire truth\x01",
            "clear...\x02\x03",
            "#00004FAnd... for the promise\x01",
            "with Shizuku as well.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5PLet's challenge the\x01",
            "Divine Blade's Territory\x01",
            "with everything we have!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#2P#1KYes!\x02",
    )


    ChrTalk(
        0x104,
        "#00307F#1P#1KRight!\x02",
    )

    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46C1")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_46CA")

    label("loc_46C1")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_46CA")


    ChrTalk(
        0x109,
        "#10107F#13P#1KYes!\x02",
    )


    label("loc_46E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4732")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4711")
    OP_FC(0x4)
    Sound(2417, 255, 100, 4)
    Jump("loc_471A")

    label("loc_4711")

    OP_FC(0x3)
    Sound(2417, 255, 100, 3)

    label("loc_471A")


    ChrTalk(
        0x105,
        "#10407F#13P#1KYeah!\x02",
    )


    label("loc_4732")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4782")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4762")
    OP_FC(0x4)
    Sound(4115, 255, 100, 4)
    Jump("loc_476B")

    label("loc_4762")

    OP_FC(0x3)
    Sound(4115, 255, 100, 3)

    label("loc_476B")


    ChrTalk(
        0x10A,
        "#00601F#13P#1KYes!\x02",
    )


    label("loc_4782")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47B2")
    OP_FC(0x4)
    Sound(3174, 255, 100, 4)
    Jump("loc_47BB")

    label("loc_47B2")

    OP_FC(0x3)
    Sound(3174, 255, 100, 3)

    label("loc_47BB")


    ChrTalk(
        0x106,
        "#10707F#13P#1KYes!\x02",
    )


    label("loc_47D2")

    SetMessageWindowPos(-1, 77, -1, -1)

    AnonymousTalk(
        0x8,
        "#00207F#5P#N#1KYes!\x02",
    )

    OP_57(0x1)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1650, 3680, 0)
    MoveCamera(360, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19090, 0)
    OP_68(0, 1650, 16730, 3500)
    MoveCamera(360, 10, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(19000, 3500)
    OP_93(0x101, 0x0, 0x190)
    OP_6F(0x79)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_CB(0x2, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x101,
        (
            "#40W#3327V(At last, I've\x01",
            "arrived... at that day\x01",
            "three years ago.)\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCFF)
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis228.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis009.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis010.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    OP_CC(0x1, 0x2, 0x0)
    CreatePortrait(2, 234, 0, 490, 256, 65526, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00000.itp")
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis020.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#3328V#40W(Just wait, big\x01",
            "brother.)\x02\x03",
            "#3329V(I'll shed light on the\x01",
            "darkness of that day,\x01",
            "for sure!)\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD01)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(18500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 1500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A9, 3)
    OP_E2(0x2)
    Sleep(800)
    EventEnd(0x5)
    Return()

    # Function_20_3E11 end

    def Function_21_4C51(): pass

    label("Function_21_4C51")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4C90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4C90)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_21_4C51 end

    def Function_22_4CBB(): pass

    label("Function_22_4CBB")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4CFA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4CFA)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_22_4CBB end

    def Function_23_4D25(): pass

    label("Function_23_4D25")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4D64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D64)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_23_4D25 end

    def Function_24_4D8F(): pass

    label("Function_24_4D8F")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4DCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DCE)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_4D8F end

    def Function_25_4DF9(): pass

    label("Function_25_4DF9")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4E38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E38)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_25_4DF9 end

    def Function_26_4E63(): pass

    label("Function_26_4E63")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4EA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EA2)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_26_4E63 end

    SaveToFile()

Try(main)
