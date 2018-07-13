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

    Sepith("Sepith_509E", 15,  15,  15,  15,  5,   5,   5)
    Sepith("Sepith_5096", 15,  6,   15,  6,   6,   9,   15)
    Sepith("Sepith_508E", 9,   15,  9,   22,  4,   10,  7)
    Sepith("Sepith_50A6", 12,  19,  14,  20,  8,   4,   5)

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
        "BattleInfo_7FC", 0x0000, 110, 6, 60, 6, 1, 30, 0, "bm9060", "Sepith_509E", 50, 30, 20, 0,
        (
            ("ms85301.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms85301.dat", "ms85301.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms85301.dat", "ms85301.dat", "ms85301.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_760", 0x0000, 110, 6, 60, 6, 1, 40, 0, "bm9060", "Sepith_5096", 50, 30, 20, 0,
        (
            ("ms79301.dat", "ms79301.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms79301.dat", "ms79301.dat", "ms79301.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms79301.dat", "ms79301.dat", "ms79301.dat", "ms79301.dat", 0, 0, 0, 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6C4", 0x0010, 110, 6, 60, 6, 1, 40, 0, "bm9060", "Sepith_508E", 50, 30, 20, 0,
        (
            ("ms81300.dat", 0, 0, 0, 0, 0, "ms79301.dat", 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms81300.dat", "ms81300.dat", 0, 0, 0, 0, "ms79301.dat", 0, "MonsterBattlePostion_604", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            ("ms81300.dat", "ms81300.dat", "ms81300.dat", 0, 0, 0, "ms79301.dat", 0, "MonsterBattlePostion_624", "MonsterBattlePostion_684", "ed7452", "ed7453", "ATBonus_5D4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_898", 0x0000, 110, 6, 60, 6, 1, 25, 0, "bm9060", "Sepith_50A6", 40, 30, 20, 10,
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
        "Function_6_2390",         # 06, 6
        "Function_7_25AC",         # 07, 7
        "Function_8_27C8",         # 08, 8
        "Function_9_291A",         # 09, 9
        "Function_10_2B36",        # 0A, 10
        "Function_11_2D52",        # 0B, 11
        "Function_12_2F6E",        # 0C, 12
        "Function_13_31F6",        # 0D, 13
        "Function_14_3349",        # 0E, 14
        "Function_15_3489",        # 0F, 15
        "Function_16_35CA",        # 10, 16
        "Function_17_370A",        # 11, 17
        "Function_18_398C",        # 12, 18
        "Function_19_3C0E",        # 13, 19
        "Function_20_3E90",        # 14, 20
        "Function_21_4D0A",        # 15, 21
        "Function_22_4D74",        # 16, 22
        "Function_23_4DDE",        # 17, 23
        "Function_24_4E48",        # 18, 24
        "Function_25_4EB2",        # 19, 25
        "Function_26_4F1C",        # 1A, 26
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
            "#59IWind Sepith x2000\x01\x07\x00",
            " obtained.\x02",
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2335")

    Jump("loc_2384")

    label("loc_233A")

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

    label("loc_2384")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_223E end

    def Function_6_2390(): pass

    label("Function_6_2390")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2561")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2493")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_23ED():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_23ED)

    def lambda_2407():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2407)
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
        (0, "loc_2474"),
        (2, "loc_2483"),
        (1, "loc_2490"),
        (SWITCH_DEFAULT, "loc_2493"),
    )


    label("loc_2474")

    SetScenarioFlags(0x21A, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_2493")

    label("loc_2483")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2490")

    OP_B9(0x0)
    Return()

    label("loc_2493")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x91, 1)"), scpexpr(EXPR_END)), "loc_24EC")
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
    Jump("loc_255C")

    label("loc_24EC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x91),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_255C")

    Jump("loc_25A0")

    label("loc_2561")

    FadeToDark(300, 0, 100)

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

    label("loc_25A0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_2390 end

    def Function_7_25AC(): pass

    label("Function_7_25AC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277D")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AF")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2609():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2609)

    def lambda_2623():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2623)
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
        (0, "loc_2690"),
        (2, "loc_269F"),
        (1, "loc_26AC"),
        (SWITCH_DEFAULT, "loc_26AF"),
    )


    label("loc_2690")

    SetScenarioFlags(0x21A, 2)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_26AF")

    label("loc_269F")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_26AC")

    OP_B9(0x0)
    Return()

    label("loc_26AF")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3F4, 1)"), scpexpr(EXPR_END)), "loc_2708")
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
    Jump("loc_2778")

    label("loc_2708")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2778")

    Jump("loc_27BC")

    label("loc_277D")

    FadeToDark(300, 0, 100)

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

    label("loc_27BC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_25AC end

    def Function_8_27C8(): pass

    label("Function_8_27C8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C4")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x58, 1)"), scpexpr(EXPR_END)), "loc_284D")
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
    Jump("loc_28BF")

    label("loc_284D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x58),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_28BF")

    Jump("loc_290E")

    label("loc_28C4")

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

    label("loc_290E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_27C8 end

    def Function_9_291A(): pass

    label("Function_9_291A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEB")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1D")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2977():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2977)

    def lambda_2991():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2991)
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
        (0, "loc_29FE"),
        (2, "loc_2A0D"),
        (1, "loc_2A1A"),
        (SWITCH_DEFAULT, "loc_2A1D"),
    )


    label("loc_29FE")

    SetScenarioFlags(0x21A, 3)
    OP_70(0xC, 0x1E)
    Sleep(500)
    Jump("loc_2A1D")

    label("loc_2A0D")

    OP_70(0xC, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2A1A")

    OP_B9(0x0)
    Return()

    label("loc_2A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x376, 1)"), scpexpr(EXPR_END)), "loc_2A76")
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
    Jump("loc_2AE6")

    label("loc_2A76")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x376),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2AE6")

    Jump("loc_2B2A")

    label("loc_2AEB")

    FadeToDark(300, 0, 100)

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

    label("loc_2B2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_291A end

    def Function_10_2B36(): pass

    label("Function_10_2B36")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D07")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C39")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2B93():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B93)

    def lambda_2BAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2BAD)
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
        (0, "loc_2C1A"),
        (2, "loc_2C29"),
        (1, "loc_2C36"),
        (SWITCH_DEFAULT, "loc_2C39"),
    )


    label("loc_2C1A")

    SetScenarioFlags(0x21A, 4)
    OP_70(0xD, 0x1E)
    Sleep(500)
    Jump("loc_2C39")

    label("loc_2C29")

    OP_70(0xD, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2C36")

    OP_B9(0x0)
    Return()

    label("loc_2C39")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x377, 1)"), scpexpr(EXPR_END)), "loc_2C92")
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
    Jump("loc_2D02")

    label("loc_2C92")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x377),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2D02")

    Jump("loc_2D46")

    label("loc_2D07")

    FadeToDark(300, 0, 100)

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

    label("loc_2D46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2B36 end

    def Function_11_2D52(): pass

    label("Function_11_2D52")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F23")
    Sound(14, 0, 100, 0)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E55")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2DAF():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2DAF)

    def lambda_2DC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2DC9)
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
        (0, "loc_2E36"),
        (2, "loc_2E45"),
        (1, "loc_2E52"),
        (SWITCH_DEFAULT, "loc_2E55"),
    )


    label("loc_2E36")

    SetScenarioFlags(0x21A, 5)
    OP_70(0xE, 0x1E)
    Sleep(500)
    Jump("loc_2E55")

    label("loc_2E45")

    OP_70(0xE, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2E52")

    OP_B9(0x0)
    Return()

    label("loc_2E55")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x378, 1)"), scpexpr(EXPR_END)), "loc_2EAE")
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
    Jump("loc_2F1E")

    label("loc_2EAE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x378),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xE, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2F1E")

    Jump("loc_2F62")

    label("loc_2F23")

    FadeToDark(300, 0, 100)

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

    label("loc_2F62")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_2D52 end

    def Function_12_2F6E(): pass

    label("Function_12_2F6E")

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

    def lambda_3082():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3082)

    def lambda_3093():
        OP_95(0xFE, -60, 0, -60, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3093)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_30EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_30EA)

    def lambda_30FB():
        OP_95(0xFE, -1340, 0, -290, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_30FB)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3158():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_3158)

    def lambda_3169():
        OP_95(0xFE, 1210, 0, -300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3169)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_31C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_31C0)

    def lambda_31D1():
        OP_95(0xFE, -2480, 0, -850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_31D1)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_2F6E end

    def Function_13_31F6(): pass

    label("Function_13_31F6")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_324F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_324F)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_329A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_329A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_32E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_32E5)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3330():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_3330)
    Sleep(1000)
    NewScene("m9008", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_13_31F6 end

    def Function_14_3349(): pass

    label("Function_14_3349")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x376, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3393")
    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3488")

    label("loc_3393")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a silver-colored gate.\x01",
            "Use the Argem Key?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347D")
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

    label("loc_347D")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3488")

    Return()

    # Function_14_3349 end

    def Function_15_3489(): pass

    label("Function_15_3489")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x377, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D3")
    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_35C9")

    label("loc_34D3")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a golden-colored gate.\x01",
            "Use the Goldia Key?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35BE")
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

    label("loc_35BE")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_35C9")

    Return()

    # Function_15_3489 end

    def Function_16_35CA(): pass

    label("Function_16_35CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x378, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3614")
    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3709")

    label("loc_3614")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a black-colored gate.\x01",
            "Use the Nohval Key?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36FE")
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

    label("loc_36FE")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_3709")

    Return()

    # Function_16_35CA end

    def Function_17_370A(): pass

    label("Function_17_370A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3760")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears the lever does not move anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3980")

    label("loc_3760")

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
            "There is a lever.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3980")
    Sound(143, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_3841")
    ClearScenarioFlags(0x1B1, 4)
    Jump("loc_3844")

    label("loc_3841")

    SetScenarioFlags(0x1B1, 4)

    label("loc_3844")

    OP_74(0xF, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_3868")
    OP_71(0xF, 0x0, 0xF, 0x0, 0x0)
    OP_79(0xF)
    Sleep(500)
    Jump("loc_387A")

    label("loc_3868")

    OP_71(0xF, 0xF, 0x3C, 0x0, 0x0)
    OP_79(0xF)
    Sleep(500)

    label("loc_387A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_END)), "loc_390A")
    OP_71(0x6, 0x0, 0x3C, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop0", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x0, 0x2)
    Jump("loc_3936")

    label("loc_390A")

    OP_71(0x6, 0x3C, 0x78, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop0", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop1", 0x1, 0x2)

    label("loc_3936")

    OP_79(0x6)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_396F")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_396F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3980")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_3980")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_370A end

    def Function_18_398C(): pass

    label("Function_18_398C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_39E2")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears the lever does not move anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3C02")

    label("loc_39E2")

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
            "There is a lever.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C02")
    Sound(143, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_3AC3")
    ClearScenarioFlags(0x1B1, 5)
    Jump("loc_3AC6")

    label("loc_3AC3")

    SetScenarioFlags(0x1B1, 5)

    label("loc_3AC6")

    OP_74(0x10, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_3AEA")
    OP_71(0x10, 0x0, 0xF, 0x0, 0x0)
    OP_79(0x10)
    Sleep(500)
    Jump("loc_3AFC")

    label("loc_3AEA")

    OP_71(0x10, 0xF, 0x3C, 0x0, 0x0)
    OP_79(0x10)
    Sleep(500)

    label("loc_3AFC")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_END)), "loc_3B8C")
    OP_71(0x7, 0x0, 0x3C, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x0, 0x2)
    Jump("loc_3BB8")

    label("loc_3B8C")

    OP_71(0x7, 0x3C, 0x78, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop3", 0x1, 0x2)

    label("loc_3BB8")

    OP_79(0x7)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BF1")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_3BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C02")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_3C02")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_398C end

    def Function_19_3C0E(): pass

    label("Function_19_3C0E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3C64")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears the lever does not move anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3E84")

    label("loc_3C64")

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
            "There is a lever.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E84")
    Sound(143, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_3D45")
    ClearScenarioFlags(0x1B1, 6)
    Jump("loc_3D48")

    label("loc_3D45")

    SetScenarioFlags(0x1B1, 6)

    label("loc_3D48")

    OP_74(0x11, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_3D6C")
    OP_71(0x11, 0x0, 0xF, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)
    Jump("loc_3D7E")

    label("loc_3D6C")

    OP_71(0x11, 0xF, 0x3C, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)

    label("loc_3D7E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_END)), "loc_3E0E")
    OP_71(0x8, 0x0, 0x3C, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop4", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x0, 0x2)
    Jump("loc_3E3A")

    label("loc_3E0E")

    OP_71(0x8, 0x3C, 0x78, 0x0, 0x0)
    SetMapObjFrame(0xFF, "CA_stop4", 0x0, 0x2)
    SetMapObjFrame(0xFF, "CA_stop5", 0x1, 0x2)

    label("loc_3E3A")

    OP_79(0x8)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E73")
    SetBarrier(0x2, 0x6, 0x1)

    label("loc_3E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E84")
    SetBarrier(0x2, 0x7, 0x1)

    label("loc_3E84")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_3C0E end

    def Function_20_3E90(): pass

    label("Function_20_3E90")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4198")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_416E")
    OP_FC(0xC)
    Jump("loc_4171")

    label("loc_416E")

    OP_FC(0xC)

    label("loc_4171")


    ChrTalk(
        0x106,
        "#10712F#13P...Where're we...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_4198")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41C2")
    OP_FC(0xC)
    Jump("loc_41C5")

    label("loc_41C2")

    OP_FC(0xC)

    label("loc_41C5")


    ChrTalk(
        0x105,
        "#10405F#13PWhere're we...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4237")

    label("loc_41E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4237")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4213")
    OP_FC(0xC)
    Jump("loc_4216")

    label("loc_4213")

    OP_FC(0xC)

    label("loc_4216")


    ChrTalk(
        0x109,
        "#10113F#13PW-Where're we...\x02",
    )

    CloseMessageWindow()

    label("loc_4237")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_429E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4261")
    OP_FC(0xC)
    Jump("loc_4264")

    label("loc_4261")

    OP_FC(0xC)

    label("loc_4264")


    ChrTalk(
        0x10A,
        "#00601F#13PThis place is MacLaine's interior...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4376")

    label("loc_429E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4305")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42C8")
    OP_FC(0xC)
    Jump("loc_42CB")

    label("loc_42C8")

    OP_FC(0xC)

    label("loc_42CB")


    ChrTalk(
        0x109,
        "#10113F#13PThis place is Mr. Arios' interior...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4376")

    label("loc_4305")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4376")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_432F")
    OP_FC(0xC)
    Jump("loc_4332")

    label("loc_432F")

    OP_FC(0xC)

    label("loc_4332")


    ChrTalk(
        0x105,
        "#10401F#13PThis place is the "Divine Blade"'s interior, eh...?\x02",
    )

    CloseMessageWindow()

    label("loc_4376")


    ChrTalk(
        0x103,
        (
            "#00206F#12PInfinite "binds"...\x01",
            "...Seem too much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PThat person...\x01",
            "How many things is he shouldering...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6P...Honestly...\x01",
            "He's taken too much upon himself...\x02",
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
            "#00006F#11PEven the "Red Ogre" was on a\x01",
            "different scale, but what our current\x01",
            "opponent is shouldering is different.\x02\x03",
            "#00013FProbably...what's awaiting us is a fiercer \x01",
            "battle than the one with the "Steel Maiden".\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_4555():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4555)
    Sleep(50)

    def lambda_4565():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4565)
    Sleep(50)

    def lambda_4575():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4575)
    Sleep(50)

    def lambda_4585():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_4585)
    Sleep(50)

    def lambda_4595():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4595)
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
            "#00003F#5PHowever── we can't\x01",
            "retreat from here.\x02\x03",
            "#00001FEven in order to get KeA back...\x01",
            "And to make the entire truth clear...\x02\x03",
            "#00004FAnd also...\x01",
            "For the promise with Shizuku too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#5PLet's challenge the Divine Blade's\x01",
            ""territory" with all we've got...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#00107F#2P#1KYes...!\x02",
    )


    ChrTalk(
        0x104,
        "#00307F#1P#1KYeah...!\x02",
    )

    Sound(2153, 255, 90, 0)
    Sound(2343, 255, 100, 1)
    Sound(2249, 255, 100, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4788")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4765")
    OP_FC(0x4)
    Sound(2478, 255, 100, 4)
    Jump("loc_476E")

    label("loc_4765")

    OP_FC(0x3)
    Sound(2478, 255, 100, 3)

    label("loc_476E")


    ChrTalk(
        0x109,
        "#10107F#13P#1KYes...!\x02",
    )


    label("loc_4788")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47DC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47B8")
    OP_FC(0x4)
    Sound(2417, 255, 100, 4)
    Jump("loc_47C1")

    label("loc_47B8")

    OP_FC(0x3)
    Sound(2417, 255, 100, 3)

    label("loc_47C1")


    ChrTalk(
        0x105,
        "#10407F#13P#1KYeah...!\x02",
    )


    label("loc_47DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_482E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_480C")
    OP_FC(0x4)
    Sound(4115, 255, 100, 4)
    Jump("loc_4815")

    label("loc_480C")

    OP_FC(0x3)
    Sound(4115, 255, 100, 3)

    label("loc_4815")


    ChrTalk(
        0x10A,
        "#00601F#13P#1KHm...!\x02",
    )


    label("loc_482E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4881")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_485E")
    OP_FC(0x4)
    Sound(3174, 255, 100, 4)
    Jump("loc_4867")

    label("loc_485E")

    OP_FC(0x3)
    Sound(3174, 255, 100, 3)

    label("loc_4867")


    ChrTalk(
        0x106,
        "#10707F#13P#1KYes...!\x02",
    )


    label("loc_4881")

    SetMessageWindowPos(-1, 77, -1, -1)

    AnonymousTalk(
        0x8,
        "#00207F#5P#N#1KYes...!\x02",
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
            "#40W#3327V(At last, I've arrived...\x01",
            "To that day of three years ago.)\x02",
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
            "#3328V#40W(Just wait...big brother.)\x02\x03",
            "#3329V(I'll shed light on the darkness\x01",
            "of that day, for sure...!)\x02",
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

    # Function_20_3E90 end

    def Function_21_4D0A(): pass

    label("Function_21_4D0A")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4D49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D49)
    OP_9B(0x0, 0xFE, 0x0, 0x128E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_21_4D0A end

    def Function_22_4D74(): pass

    label("Function_22_4D74")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4DB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DB3)
    OP_9B(0x0, 0xFE, 0x0, 0x10FE, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x155, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_22_4D74 end

    def Function_23_4DDE(): pass

    label("Function_23_4DDE")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4E1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E1D)
    OP_9B(0x0, 0xFE, 0x0, 0x1036, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x12, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_23_4DDE end

    def Function_24_4E48(): pass

    label("Function_24_4E48")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4E87():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E87)
    OP_9B(0x0, 0xFE, 0x0, 0xD48, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x162, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_24_4E48 end

    def Function_25_4EB2(): pass

    label("Function_25_4EB2")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4EF1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EF1)
    OP_9B(0x0, 0xFE, 0x0, 0xC4E, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x148, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_25_4EB2 end

    def Function_26_4F1C(): pass

    label("Function_26_4F1C")

    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4F5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F5B)
    OP_9B(0x0, 0xFE, 0x0, 0xB22, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1C, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_26_4F1C end

    SaveToFile()

Try(main)
