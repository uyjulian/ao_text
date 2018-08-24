from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9005.bin",                # FileName
        "m9005",                    # MapName
        "m9005",                    # Location
        0x00BF,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 191, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9005",                  # 0
        "Cryptid",                # 1
        "ヘカトンケイル",         # 2
        "ヘカトンケイル",         # 3
        "bm9010",                 # 4
        "bm9010",                 # 5
        "bm9010",                 # 6
        "bm9010",                 # 7
        "bm9010",                 # 8
        "bm9010",                 # 9
        "bm9010",                 # 10
        "bm9010",                 # 11
    ))

    ATBonus("ATBonus_564", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_574", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_46C6", 12,  23,  0,   16,  0,   0,   20)
    Sepith("Sepith_46B6", 8,   8,   18,  8,   2,   8,   16)
    Sepith("Sepith_46BE", 8,   4,   4,   16,  15,  17,  4)
    Sepith("Sepith_46A6", 14,  14,  14,  14,  4,   9,   6)
    Sepith("Sepith_46AE", 9,   9,   9,   9,   13,  13,  13)

    MonsterBattlePostion("MonsterBattlePostion_5B4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_618", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_61C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_620", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_624", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_628", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_62C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_594", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 1, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 15, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 1, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 15, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 0, 0, 180)

    # monster count: 20

    BattleInfo(
        "BattleInfo_8F0", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_46C6", 100, 0, 0, 0,
        (
            ("ms85201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 105, 6, 60, 10, 1, 40, 0, "bm9010", "Sepith_46B6", 40, 35, 25, 0,
        (
            ("ms87900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms87900.dat", "ms87900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms87900.dat", "ms87900.dat", "ms87900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_828", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_46BE", 40, 30, 20, 10,
        (
            ("ms85700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85700.dat", "ms85700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85700.dat", "ms85700.dat", "ms85700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_654", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_46A6", 40, 35, 25, 0,
        (
            ("ms85400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85400.dat", "ms85700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms85400.dat", "ms85700.dat", "ms85700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6F0", 0x0000, 105, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_46AE", 40, 35, 25, 0,
        (
            ("ms81100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms81100.dat", "ms81100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_594", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            ("ms81100.dat", "ms81100.dat", "ms81100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_564"),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_978", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81100.dat", "ms85700.dat", "ms81100.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_574"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9BC", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms81100.dat", "ms85700.dat", "ms81100.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "MonsterBattlePostion_5B4", "MonsterBattlePostion_614", "ed7452", "ed7453", "ATBonus_574"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_934", 0x0040, 255, 6, 45, 10, 1, 30, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89301.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", "ms85700.dat", 0, "MonsterBattlePostion_634", "MonsterBattlePostion_614", "ed7554", "ed7453", "ATBonus_574"),
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
        "monster/ch85450.itc",               # 10
        "monster/ch85450.itc",               # 11
        "monster/ch81150.itc",               # 12
        "monster/ch81151.itc",               # 13
        "monster/ch87950.itc",               # 14
        "monster/ch87951.itc",               # 15
        "monster/ch85750.itc",               # 16
        "monster/ch85751.itc",               # 17
        "monster/ch85250.itc",               # 18
        "monster/ch85251.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(68459,   30500,   4294953817, 0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(56000,   30500,   100000,  0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(31750,   4294905316, 30000,   0x10100D1,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(48570,   4294927056, 30020,   0x1010081,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(55920,   4294916226, 30030,   0x101013D,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294864116, 4294879016, 25000,   0x1010168,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294849016, 4294918456, 25520,   0x101009C,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294839376, 1890,    25500,   0x10100B4,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294882256, 4294966506, 25500,   0x1010107,    "BattleInfo_654", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294903676, 4294951606, 25000,   0x101013A,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294904806, 23830,   25000,   0x10100B7,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294921376, 48720,   25050,   0x10100E1,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(4294958726, 62070,   25020,   0x101000C,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(22610,   71520,   25020,   0x101010E,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(34590,   50000,   25000,   0x1010137,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(79910,   84020,   30020,   0x101010E,    "BattleInfo_654", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(80100,   62070,   30020,   0x1010011,    "BattleInfo_6F0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(103300,  39430,   30000,   0x1010111,    "BattleInfo_78C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(108520,  7040,    30000,   0x1010168,    "BattleInfo_828", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(103990,  4294946036, 30000,   0x1010009,    "BattleInfo_8F0", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(98580,   4294907016, 30020,   0x1010168,    "BattleInfo_654", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(70180,   4294881686, 30000,   0x101005A,    "BattleInfo_6F0", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 13,  -44.5,                 -97.0,                 44.5,                  81.0,                  [0.2730506658554077,   0.09559610486030579,   -0.0,                  0.0,                   -0.19119220972061157,  0.13652533292770386,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -6.394889831542969,    17.496984481811523,    -8.90000057220459,     1.0])
    DeclEvent(0x0040, 0, 6,   31.079999923706055,    -106.05000305175781,   34.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -3.884999990463257,    13.256250381469727,    -8.5,                  1.0])

    DeclActor(68460,   30000,   4294953816, 1200,    68460,   31000,   4294953816, 0x007C, 0,  3,  0x0000)
    DeclActor(56000,   30000,   100000,  1200,    56000,   31000,   100000,  0x007C, 0,  4,  0x0000)
    DeclActor(4294945296, 25000,   69500,   1200,    4294945296, 26000,   69500,   0x007C, 0,  5,  0x0000)
    DeclActor(0,       35000,   4294857296, 1200,    0,       35000,   4294857296, 0x007C, 0,  9,  0x0000)
    DeclActor(0,       30250,   4294911296, 1200,    0,       30250,   4294911296, 0x007C, 0,  11, 0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 4
    ChipFrameInfo(899, 0, [0, 1, 2, 3, 4])                       # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9

    ScpFunction((
        "Function_0_AE0",          # 00, 0
        "Function_1_AFC",          # 01, 1
        "Function_2_B75",          # 02, 2
        "Function_3_1D6F",         # 03, 3
        "Function_4_1F8A",         # 04, 4
        "Function_5_21A6",         # 05, 5
        "Function_6_22F7",         # 06, 6
        "Function_7_2370",         # 07, 7
        "Function_8_25F0",         # 08, 8
        "Function_9_2743",         # 09, 9
        "Function_10_286F",        # 0A, 10
        "Function_11_2958",        # 0B, 11
        "Function_12_2A85",        # 0C, 12
        "Function_13_2B6E",        # 0D, 13
        "Function_14_3ACB",        # 0E, 14
        "Function_15_3ADB",        # 0F, 15
        "Function_16_3AEE",        # 10, 16
        "Function_17_3B1F",        # 11, 17
        "Function_18_3B32",        # 12, 18
        "Function_19_3B45",        # 13, 19
        "Function_20_3B67",        # 14, 20
        "Function_21_3C08",        # 15, 21
        "Function_22_3C1D",        # 16, 22
        "Function_23_3C5E",        # 17, 23
        "Function_24_3C80",        # 18, 24
        "Function_25_3D65",        # 19, 25
    ))


    def Function_0_AE0(): pass

    label("Function_0_AE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFB")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_AE0")

    label("loc_AFB")

    Return()

    # Function_0_AE0 end

    def Function_1_AFC(): pass

    label("Function_1_AFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D")
    Event(0, 7)

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1E")
    Event(0, 25)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B2D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)

    label("loc_B2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5A")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_B74")

    label("loc_B5A")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B74")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_B74")

    Return()

    # Function_1_AFC end

    def Function_2_B75(): pass

    label("Function_2_B75")

    OP_F0(0x1, 0x320)
    OP_1B(0x5, 0x0, 0x8)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B9A")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_B9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBC")
    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_C25")

    label("loc_BBC")

    OP_78(0x7, 0x8)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x1)
    SetChrPos(0x8, 31080, 35000, -106050, 67)
    OP_93(0x8, 0x43, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 31080, 34000, -106050, 3000, 3000, 90000)

    label("loc_C25")

    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x4, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x1000)
    OP_10(0x7, 0x0)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 3)), scpexpr(EXPR_END)), "loc_1CA3")
    ClearMapObjFlags(0x2, 0x4)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x1000)
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    Jump("loc_1CC4")

    label("loc_1CA3")

    SetMapObjFlags(0x2, 0x4)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x1000)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)

    label("loc_1CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 6)), scpexpr(EXPR_END)), "loc_1CD9")
    ClearMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x6, 0x4)

    label("loc_1CD9")

    SetMapObjFrame(0xFF, "CA_stop2", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_1D02")
    SetMapObjFrame(0xFF, "CA_stop2", 0x1, 0x2)

    label("loc_1D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D23")
    SetMapObjFrame(0xFF, "magi_07c_add", 0x0, 0x1)

    label("loc_1D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D36")
    OP_70(0x3, 0x0)
    Jump("loc_1D3A")

    label("loc_1D36")

    OP_70(0x3, 0x1E)

    label("loc_1D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4D")
    OP_70(0x4, 0x0)
    Jump("loc_1D51")

    label("loc_1D4D")

    OP_70(0x4, 0x1E)

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D64")
    OP_70(0x5, 0x0)
    Jump("loc_1D68")

    label("loc_1D64")

    OP_70(0x5, 0x1E)

    label("loc_1D68")

    Sound(112, 1, 100, 0)
    Return()

    # Function_2_B75 end

    def Function_3_1D6F(): pass

    label("Function_3_1D6F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F40")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E72")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1DCC():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DCC)

    def lambda_1DE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1DE6)
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
    Battle("BattleInfo_978", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1E53"),
        (2, "loc_1E62"),
        (1, "loc_1E6F"),
        (SWITCH_DEFAULT, "loc_1E72"),
    )


    label("loc_1E53")

    SetScenarioFlags(0x219, 3)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_1E72")

    label("loc_1E62")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1E6F")

    OP_B9(0x0)
    Return()

    label("loc_1E72")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x656, 1)"), scpexpr(EXPR_END)), "loc_1ECB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x656),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x201, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1F3B")

    label("loc_1ECB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x656),
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

    label("loc_1F3B")

    Jump("loc_1F7E")

    label("loc_1F40")

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

    label("loc_1F7E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1D6F end

    def Function_4_1F8A(): pass

    label("Function_4_1F8A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215C")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208D")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1FE7():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FE7)

    def lambda_2001():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2001)
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
    Battle("BattleInfo_9BC", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_206E"),
        (2, "loc_207D"),
        (1, "loc_208A"),
        (SWITCH_DEFAULT, "loc_208D"),
    )


    label("loc_206E")

    SetScenarioFlags(0x219, 4)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_208D")

    label("loc_207D")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_208A")

    OP_B9(0x0)
    Return()

    label("loc_208D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41C, 1)"), scpexpr(EXPR_END)), "loc_20E6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x202, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_2157")

    label("loc_20E6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(0x4),
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

    label("loc_2157")

    Jump("loc_219A")

    label("loc_215C")

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

    label("loc_219A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1F8A end

    def Function_5_21A6(): pass

    label("Function_5_21A6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A2")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_222B")
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
    SetScenarioFlags(0x202, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_229D")

    label("loc_222B")

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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_229D")

    Jump("loc_22EB")

    label("loc_22A2")

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

    label("loc_22EB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_21A6 end

    def Function_6_22F7(): pass

    label("Function_6_22F7")

    Battle("BattleInfo_934", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233E")
    OP_90(0x0, 38360, 34570, -103390, 66)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_236F")

    label("loc_233E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2351")
    Jump("loc_236F")

    label("loc_2351")

    ModifyEventFlags(0, 1, 0x80)
    SetMapObjFlags(0x7, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetScenarioFlags(0x1B8, 3)
    EventEnd(0x5)

    label("loc_236F")

    Return()

    # Function_6_22F7 end

    def Function_7_2370(): pass

    label("Function_7_2370")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_68(-54730, 46000, -89080, 0)
    MoveCamera(31, 51, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13870, 0)
    SetChrPos(0x0, -54250, 45500, -86750, 165)
    SetChrPos(0x1, -54250, 45500, -86750, 165)
    SetChrPos(0x2, -54250, 45500, -86750, 165)
    SetChrPos(0x3, -54250, 45500, -86750, 165)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2480():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2480)

    def lambda_2491():
        OP_95(0xFE, -53260, 45000, -91480, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2491)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_24E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_24E8)

    def lambda_24F9():
        OP_95(0xFE, -54540, 45000, -91510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_24F9)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2556():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2556)

    def lambda_2567():
        OP_95(0xFE, -51990, 45000, -90960, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2567)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_25BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_25BE)

    def lambda_25CF():
        OP_95(0xFE, -55840, 45000, -91280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_25CF)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_7_2370 end

    def Function_8_25F0(): pass

    label("Function_8_25F0")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event/evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2649():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2649)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2694():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2694)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_26DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_26DF)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_272A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_272A)
    Sleep(1000)
    NewScene("m9070", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_25F0 end

    def Function_9_2743(): pass

    label("Function_9_2743")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift. Use it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2867")
    Fade(500)
    SetChrPos(0x0, 0, 35000, -111000, 180)
    SetChrPos(0x1, -1000, 35000, -110000, 180)
    SetChrPos(0x2, 1000, 35000, -110000, 180)
    SetChrPos(0x3, 0, 35000, -109000, 180)
    OP_68(0, 35000, -111000, 0)
    MoveCamera(341, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(29410, 0)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x3C, 0x5A, 0x0, 0x0)
    OP_68(0, 15000, -108000, 4000)
    MoveCamera(5, 55, 0, 4000)
    Sleep(1800)
    StopSound(832, 500, 100)
    StopSound(112, 500, 100)
    SetScenarioFlags(0x1B0, 2)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9004", 0, 0, 0)
    IdleLoop()

    label("loc_2867")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_2743 end

    def Function_10_286F(): pass

    label("Function_10_286F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x1, 0x5A)
    Sleep(1)
    OP_68(0, 35000, -111000, 0)
    MoveCamera(6, 57, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(22000, 0)
    OP_90(0x0, 0, 35000, -111000, 0)
    OP_90(0x1, -1000, 35000, -110000, 0)
    OP_90(0x2, 1000, 35000, -110000, 0)
    OP_90(0x3, 0, 35000, -109000, 0)
    Sound(832, 2, 100, 0)
    OP_68(0, 40000, -114000, 3000)
    MoveCamera(0, 40, 0, 3000)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x5A, 0x78, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0x1)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_286F end

    def Function_11_2958(): pass

    label("Function_11_2958")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift. Use it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7D")
    Fade(500)
    OP_69(0x0, 0x0)
    SetChrPos(0x0, 0, 30250, -57000, 180)
    SetChrPos(0x1, -1000, 30250, -56000, 180)
    SetChrPos(0x2, 1000, 30250, -56000, 180)
    SetChrPos(0x3, 0, 30250, -55000, 180)
    OP_68(0, 31250, -56000, 0)
    MoveCamera(16, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20650, 0)
    OP_0D()
    Sleep(500)
    Sound(832, 2, 100, 0)
    Sound(935, 0, 70, 0)
    OP_74(0x2, 0xF)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    OP_68(0, 35000, -56000, 4000)
    MoveCamera(5, 35, 0, 4000)
    Sleep(1800)
    StopSound(832, 500, 100)
    StopSound(112, 500, 100)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9007", 0, 0, 0)
    IdleLoop()

    label("loc_2A7D")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_2958 end

    def Function_12_2A85(): pass

    label("Function_12_2A85")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x2, 0x1E)
    Sleep(1)
    OP_68(80, 35090, -57000, 0)
    MoveCamera(346, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19850, 0)
    OP_90(0x0, 0, 46000, -57000, 180)
    OP_90(0x1, -1000, 46000, -56000, 180)
    OP_90(0x2, 1000, 46000, -56000, 180)
    OP_90(0x3, 0, 46000, -55000, 180)
    Sound(832, 2, 100, 0)
    OP_68(0, 31250, -56000, 3000)
    MoveCamera(0, 35, 0, 3000)
    OP_74(0x2, 0xF)
    OP_71(0x2, 0x1E, 0x3C, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(2000)
    OP_24(0x340)
    Sound(149, 0, 60, 0)
    Sleep(1400)
    Sleep(500)
    OP_79(0x2)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_2A85 end

    def Function_13_2B6E(): pass

    label("Function_13_2B6E")

    SetMapFlags(0x80)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    FadeToBright(0, -1)
    OP_E2(0x3)
    SoundLoad(3840)
    SoundLoad(3841)
    SoundLoad(3842)
    SoundLoad(3843)
    SoundLoad(3844)
    SoundLoad(3845)
    SoundLoad(3846)
    OP_69(0x0, 0x0)
    LoadChrToIndex("apl/ch51741.itc", 0x1E)
    LoadChrToIndex("apl/ch51768.itc", 0x1F)
    SetChrPos(0x101, -46490, 45000, -96480, 305)
    SetChrPos(0x102, -45190, 45430, -95980, 305)
    SetChrPos(0x103, -45390, 45500, -96980, 305)
    SetChrPos(0x104, -46090, 45500, -98480, 305)
    SetChrPos(0xF4, -43890, 45500, -96980, 305)
    SetChrPos(0xF5, -44490, 45500, -98780, 305)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-44890, 45600, -96900, 0)
    MoveCamera(348, 41, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17450, 0)
    Sleep(500)
    OP_68(-53480, 45300, -89160, 4500)
    MoveCamera(346, 25, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(17450, 4500)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 0, 0, 14)
    BeginChrThread(0x102, 0, 0, 15)
    BeginChrThread(0x103, 0, 0, 16)
    BeginChrThread(0x104, 0, 0, 17)
    BeginChrThread(0xF4, 0, 0, 18)
    BeginChrThread(0xF5, 0, 0, 19)
    OP_0D()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_68(-53480, 45800, -89160, 1500)
    MoveCamera(346, 21, 0, 1500)
    OP_6E(800, 1500)
    SetCameraDistance(16750, 1500)

    def lambda_2D0E():
        OP_93(0x101, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D0E)
    Sleep(50)

    def lambda_2D1E():
        OP_93(0x102, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D1E)
    Sleep(50)

    def lambda_2D2E():
        OP_93(0x103, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2D2E)
    Sleep(50)

    def lambda_2D3E():
        OP_93(0x104, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2D3E)
    Sleep(50)

    def lambda_2D4E():
        OP_93(0xF4, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2D4E)
    Sleep(50)

    def lambda_2D5E():
        OP_93(0xF5, 0x14F, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2D5E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00013F#6PThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12P...A new "gate".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12PThere's a Magical\x01",
            "Barrier here as well...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    BeginChrThread(0x101, 0, 0, 20)
    WaitChrThread(0x101, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PIt's no use... It's not\x01",
            "reacting to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-53960, 46200, -86710, 2000)
    MoveCamera(346, 13, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    Sound(921, 0, 100, 0)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3840V#40W#20A...Hehe...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3841V#40W#38AIt seems you've beaten\x01",
            "Shirley and the boy, eh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x159, 0x1F4)

    ChrTalk(
        0x104,
        "#00307F#6P#NYou!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005F#6PCan you tell what we're\x01",
            "doing here!?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3842V#40W#32AHehe, quite clearly.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3843V#40W#35ACome now─ Randolph, put\x01",
            "your hand there...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3844V#40W#30AWe're going to settle\x01",
            "everything.\x07\x00\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_24(0xF04)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)

    ChrTalk(
        0x104,
        "#00311F#6P#N...Hah, fine by me.\x02",
    )

    CloseMessageWindow()

    def lambda_312C():
        OP_96(0xFE, 0xFFFF2B1C, 0xAFC8, 0xFFFE9A94, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_312C)

    def lambda_3146():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3146)

    def lambda_3153():

        label("loc_3153")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3153")

    QueueWorkItem2(0x102, 2, lambda_3153)

    def lambda_3165():

        label("loc_3165")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3165")

    QueueWorkItem2(0x103, 2, lambda_3165)

    def lambda_3177():

        label("loc_3177")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3177")

    QueueWorkItem2(0xF4, 2, lambda_3177)

    def lambda_3189():

        label("loc_3189")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3189")

    QueueWorkItem2(0xF5, 2, lambda_3189)
    Sleep(300)
    OP_68(-54120, 46300, -86290, 2000)
    MoveCamera(346, 13, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(17500, 2000)
    BeginChrThread(0x104, 0, 0, 21)
    Sleep(300)
    WaitChrThread(0x101, 2)

    def lambda_31D9():

        label("loc_31D9")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_31D9")

    QueueWorkItem2(0x101, 2, lambda_31D9)
    WaitChrThread(0x104, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x104, 0, 0, 22)
    WaitChrThread(0x104, 0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0x6, 0x1, 0x3E8)
    Sleep(2000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    BeginChrThread(0x104, 0, 0, 23)
    WaitChrThread(0x104, 0)
    ClearMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x6, 0x4)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3845V#40W#52AHeh... Then, let's start\x01",
            "the "battle".\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3846V#40W#42ACast away doubts and\x01",
            "reluctance and come\x01",
            "charge at me now!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_24(0xF06)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_C9(0x1, 0x800)
    OP_68(-53550, 46000, -88660, 3500)
    MoveCamera(346, 18, 0, 3500)
    OP_6E(800, 3500)
    SetCameraDistance(16750, 3500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00306F#5P...Jeez, like father\x01",
            "like daughter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12P#NRandy...\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P...I was expecting this,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah... Honestly, he's too\x01",
            "difficult an opponent.\x02\x03",
            "#00008FConsidering the overwhelming power\x01",
            "he showed in front of IBC... our\x01",
            "chances of winning are slim.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_357B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_351B")
    OP_FC(0xC)
    Jump("loc_351E")

    label("loc_351B")

    OP_FC(0xFFFA)

    label("loc_351E")


    ChrTalk(
        0x109,
        (
            "#10108F#13P...You're right... Our\x01",
            "degrees of combat experience\x01",
            "are too different.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3669")

    label("loc_357B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35A5")
    OP_FC(0xC)
    Jump("loc_35A8")

    label("loc_35A5")

    OP_FC(0xFFFA)

    label("loc_35A8")


    ChrTalk(
        0x105,
        (
            "#10408F#13PIndeed... Our degrees of\x01",
            "combat experience are\x01",
            "too different.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_3669")

    label("loc_35FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3669")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3626")
    OP_FC(0xC)
    Jump("loc_3629")

    label("loc_3626")

    OP_FC(0xFFFA)

    label("loc_3629")


    ChrTalk(
        0x106,
        (
            "#10708F#13PThe Ogre Rosso... I'd\x01",
            "heard the rumors, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3669")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3693")
    OP_FC(0xC)
    Jump("loc_3696")

    label("loc_3693")

    OP_FC(0xFFFA)

    label("loc_3696")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PHe's really the leader\x01",
            "of Zemuria strongest\x01",
            "jaeger corps, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_37DB")

    label("loc_36EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_375D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3715")
    OP_FC(0xC)
    Jump("loc_3718")

    label("loc_3715")

    OP_FC(0xFFFA)

    label("loc_3718")


    ChrTalk(
        0x106,
        (
            "#10703F#13PThe Ogre Rosso... I'd\x01",
            "heard the rumors, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_37DB")

    label("loc_375D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37DB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3787")
    OP_FC(0xC)
    Jump("loc_378A")

    label("loc_3787")

    OP_FC(0xFFFA)

    label("loc_378A")


    ChrTalk(
        0x105,
        (
            "#10406F#13PHe's really the leader\x01",
            "of Zemuria's strongest\x01",
            "jaeger corps, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_37DB")


    ChrTalk(
        0x104,
        (
            "#00303F#5PStill, until I─ I mean,\x01",
            "until we get through\x01",
            "him, we can't advance.\x02\x03",
            "#00308FAnd to settle what I\x01",
            "couldn't two years ago\x01",
            "as well...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xA0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#5PI beg of you─ Lend me\x01",
            "your aid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYeah, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#NThat goes without\x01",
            "saying.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00109F#12P*giggle*... Naturally.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3966")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3947")
    OP_FC(0xC)
    Jump("loc_394A")

    label("loc_3947")

    OP_FC(0xFFFA)

    label("loc_394A")


    ChrTalk(
        0x109,
        "#10100F#13PI'll help!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3966")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3990")
    OP_FC(0xC)
    Jump("loc_3993")

    label("loc_3990")

    OP_FC(0xFFFA)

    label("loc_3993")


    ChrTalk(
        0x105,
        (
            "#10402F#13PHehe, if you're fine\x01",
            "with my modest\x01",
            "abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_39D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39FD")
    OP_FC(0xC)
    Jump("loc_3A00")

    label("loc_39FD")

    OP_FC(0xFFFA)

    label("loc_3A00")


    ChrTalk(
        0x10A,
        "#00604F#13PHmph... Very well.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3A24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A4E")
    OP_FC(0xC)
    Jump("loc_3A51")

    label("loc_3A4E")

    OP_FC(0xFFFA)

    label("loc_3A51")


    ChrTalk(
        0x106,
        (
            "#10702F#13PPlease, allow me to\x01",
            "assist you.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3A82")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, -52940, 45100, -91520, 340)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 6)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_2B6E end

    def Function_14_3ACB(): pass

    label("Function_14_3ACB")

    OP_9B(0x0, 0xFE, 0x5, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_14_3ACB end

    def Function_15_3ADB(): pass

    label("Function_15_3ADB")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x5, 0x1C20, 0x7D0, 0x0)
    Return()

    # Function_15_3ADB end

    def Function_16_3AEE(): pass

    label("Function_16_3AEE")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x5, 0xB54, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x163, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x163, 0x7D0, 0x7D0, 0x0)
    Return()

    # Function_16_3AEE end

    def Function_17_3B1F(): pass

    label("Function_17_3B1F")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x5, 0x2198, 0x7D0, 0x0)
    Return()

    # Function_17_3B1F end

    def Function_18_3B32(): pass

    label("Function_18_3B32")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x5, 0x1D4C, 0x7D0, 0x0)
    Return()

    # Function_18_3B32 end

    def Function_19_3B45(): pass

    label("Function_19_3B45")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0x5, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15A, 0x11C6, 0x7D0, 0x0)
    Return()

    # Function_19_3B45 end

    def Function_20_3B67(): pass

    label("Function_20_3B67")

    OP_95(0xFE, -53580, 45500, -89410, 2000, 0x0)
    OP_93(0xFE, 0x159, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Return()

    # Function_20_3B67 end

    def Function_21_3C08(): pass

    label("Function_21_3C08")

    OP_95(0xFE, -53580, 45500, -89410, 2000, 0x0)
    Return()

    # Function_21_3C08 end

    def Function_22_3C1D(): pass

    label("Function_22_3C1D")

    OP_93(0xFE, 0x159, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_22_3C1D end

    def Function_23_3C5E(): pass

    label("Function_23_3C5E")

    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    Return()

    # Function_23_3C5E end

    def Function_24_3C80(): pass

    label("Function_24_3C80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x2, "event/ev17017.eff")
    OP_69(0x0, 0x0)
    OP_68(-61000, 46900, -105500, 0)
    MoveCamera(30, 16, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17850, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22850, 5000)
    OP_0D()
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -62600, 47500, -108215, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    Sleep(300)
    SetMapObjFrame(0xFF, "magi_07c_add", 0x0, 0x1)
    Sleep(3000)
    StopSound(112, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9072", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3C80 end

    def Function_25_3D65(): pass

    label("Function_25_3D65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event/ev202_00.eff")
    OP_69(0x0, 0x0)
    OP_68(-54730, 46000, -89080, 0)
    MoveCamera(31, 42, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13700, 0)
    SetChrPos(0x101, -54250, 45500, -86750, 165)
    SetChrPos(0x102, -54250, 45500, -86750, 165)
    SetChrPos(0x103, -54250, 45500, -86750, 165)
    SetChrPos(0x104, -54250, 45500, -86750, 165)
    SetChrPos(0xF4, -54250, 45500, -86750, 165)
    SetChrPos(0xF5, -54250, 45500, -86750, 165)
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
    SetMapObjFrame(0xFF, "magi_07c_add", 0x0, 0x1)
    SetCameraDistance(14700, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3EE2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EE2)

    def lambda_3EF3():
        OP_95(0xFE, -53260, 45000, -91480, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EF3)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3F4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F4A)

    def lambda_3F5B():
        OP_95(0xFE, -54540, 45000, -91510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F5B)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_3FB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3FB8)

    def lambda_3FC9():
        OP_95(0xFE, -51990, 45000, -90960, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FC9)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_4020():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4020)

    def lambda_4031():
        OP_95(0xFE, -55840, 45000, -91280, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4031)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_408E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_408E)

    def lambda_409F():
        OP_95(0xFE, -54850, 45600, -90050, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_409F)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_40F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_40F6)

    def lambda_4107():
        OP_95(0xFE, -53270, 45600, -89890, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_4107)
    WaitChrThread(0xF5, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_419A():
        OP_93(0x101, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_419A)
    Sleep(50)

    def lambda_41AA():
        OP_93(0x102, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41AA)
    Sleep(50)

    def lambda_41BA():
        OP_93(0x103, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41BA)
    Sleep(50)

    def lambda_41CA():
        OP_93(0x104, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_41CA)
    Sleep(50)

    def lambda_41DA():
        OP_93(0xF4, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_41DA)
    Sleep(50)

    def lambda_41EA():
        OP_93(0xF5, 0xD2, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_41EA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_68(-55500, 47000, -99000, 3000)
    MoveCamera(19, 8, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(24100, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#11PThe Magical Barrier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PIt seems like they get\x01",
            "unlocked when each\x01",
            "Territory is released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PAlright... Now we can\x01",
            "move on.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4309")
    OP_FC(0x5)
    Jump("loc_430C")

    label("loc_4309")

    OP_FC(0xB)

    label("loc_430C")


    ChrTalk(
        0x109,
        (
            "#10106F#13PBut as expected, it was\x01",
            "a hard fight...\x02\x03",
            "#10100FIt might be nice to\x01",
            "return to the Merkabah\x01",
            "temporarily and rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PRight... Let's go back\x01",
            "and report at the same\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45D7")

    label("loc_43D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4400")
    OP_FC(0x5)
    Jump("loc_4403")

    label("loc_4400")

    OP_FC(0xB)

    label("loc_4403")


    ChrTalk(
        0x105,
        (
            "#10406F#13PPhew... But as expected,\x01",
            "it was a hard fight...\x02\x03",
            "#10400FIt might be nice to\x01",
            "return to the Merkabah\x01",
            "temporarily and rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PRight... Let's go back\x01",
            "and report at the same\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45D7")

    label("loc_44D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44FF")
    OP_FC(0x5)
    Jump("loc_4502")

    label("loc_44FF")

    OP_FC(0xB)

    label("loc_4502")


    ChrTalk(
        0x10A,
        (
            "#00606F#13PHowever, we were forced\x01",
            "to exhaustion as well...\x02\x03",
            "#00600FIt might be a good idea\x01",
            "to return to the Merkabah\x01",
            "temporarily and rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PRight... Let's go back\x01",
            "and report at the same\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45D7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -54000, 45200, -91100, 165)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A9, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_3D65 end

    SaveToFile()

Try(main)
