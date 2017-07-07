from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9002.bin",                # FileName
        "m9002",                    # MapName
        "m9002",                    # Location
        0x00BE,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 190, 0, 2, 0, 3],
    )

    BuildStringList((
        "m9002",                  # 0
        "Marybele",             # 1
        "Eidolon",                   # 2
        "Gold Statue",     # 3
        "Dark blue zone",     # 4
        "bm9010",                 # 5
        "bm9010",                 # 6
        "bm9010",                 # 7
        "bm9010",                 # 8
        "bm9010",                 # 9
        "bm9010",                 # 10
        "bm9010",                 # 11
        "bm9010",                 # 12
        "bm9010",                 # 13
    ))

    ATBonus("ATBonus_510", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_520", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_530", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_6FCF", 7,   7,   7,   7,   11,  11,  11)
    Sepith("Sepith_6FE7", 9,   9,   9,   9,   10,  10,  10)
    Sepith("Sepith_6FC7", 13,  13,  13,  13,  4,   4,   4)
    Sepith("Sepith_6FEF", 11,  23,  0,   15,  0,   0,   19)
    Sepith("Sepith_6FDF", 0,   0,   0,   0,   15,  38,  15)

    MonsterBattlePostion("MonsterBattlePostion_570", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5E4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5E8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_550", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 1, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 15, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_604", 1, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 15, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_6AC", 0x0000, 100, 6, 60, 10, 1, 40, 0, "bm9010", "Sepith_6FCF", 40, 30, 20, 10,
        (
            ("ms80900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_6FE7", 40, 30, 20, 10,
        (
            ("ms79900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
        )
    )

    BattleInfo(
        "BattleInfo_610", 0x0000, 100, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_6FC7", 50, 30, 20, 0,
        (
            ("ms85300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_6FEF", 100, 0, 0, 0,
        (
            ("ms85200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0010, 100, 6, 180, 10, 1, 5, 0, "bm9010", "Sepith_6FDF", 50, 35, 15, 0,
        (
            ("ms74200.dat", 0, 0, 0, 0, 0, "ms85200.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms74200.dat", "ms74200.dat", 0, 0, 0, 0, "ms85200.dat", 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms74200.dat", "ms74200.dat", "ms74200.dat", 0, 0, 0, "ms85200.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_A28", 0x0C10, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74200.dat", "ms74200.dat", "ms74200.dat", "ms74200.dat", "ms74200.dat", "ms74200.dat", "ms85200.dat", 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A6C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9E4", 0x0040, 255, 6, 45, 10, 1, 30, 0, "bm9010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89300.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", 0, "MonsterBattlePostion_5F0", "MonsterBattlePostion_5D0", "ed7554", "ed7453", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51735.itc",                   # 00
        "apl/ch51736.itc",                   # 01
        "apl/ch51768.itc",                   # 02
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
        "monster/ch85350.itc",               # 10
        "monster/ch85350.itc",               # 11
        "monster/ch80950.itc",               # 12
        "monster/ch80950.itc",               # 13
        "monster/ch85050.itc",               # 14
        "monster/ch85050.itc",               # 15
        "monster/ch74250.itc",               # 16
        "monster/ch74250.itc",               # 17
        "monster/ch79950.itc",               # 18
        "monster/ch79950.itc",               # 19
        "monster/ch85250.itc",               # 1A
        "monster/ch85251.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294796957, 4294942796, 4294894447, 0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(89839,   10500,   4294880536, 0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(4294844696, 4294828586, 4294942296, 0x1010137,    "BattleInfo_6AC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294813716, 4294863856, 4294942316, 0x1010092,    "BattleInfo_8D8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(4294849666, 4294877146, 4294942296, 0x10100E8,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294883086, 4294852786, 4294942296, 0x10100D8,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294874436, 4294841116, 4294942296, 0x1010024,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294908176, 4294824856, 4294942296, 0x1010124,    "BattleInfo_9A0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(75510,   4294838666, 4294942296, 0x101003B,    "BattleInfo_9A0", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(106200,  4294858146, 4294942296, 0x10100E1,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(138550,  66010,   0,       0x101009A,    "BattleInfo_610", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(117460,  60040,   10000,   0x1010098,    "BattleInfo_6AC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(128900,  4294950956, 10000,   0x1010007,    "BattleInfo_83C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(125970,  4294919266, 10000,   0x1010015,    "BattleInfo_8D8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(104070,  4294893706, 10000,   0x1010023,    "BattleInfo_9A0", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 12,  0.0,                   -148.0,                19.5,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  49.333335876464844,    -3.9000000953674316,   1.0])
    DeclEvent(0x0040, 0, 29,  -14.0,                 -127.0,                24.5,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.799999952316284,     25.399999618530273,    -4.900000095367432,    1.0])
    DeclEvent(0x0040, 0, 34,  14.0,                  -127.0,                24.5,                  6.25,                  [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.799999952316284,    25.399999618530273,    -4.900000095367432,    1.0])
    DeclEvent(0x0040, 0, 7,   125.0999984741211,     -64.55999755859375,    -0.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -15.637499809265137,   8.069999694824219,     -0.0,                  1.0])

    DeclActor(4294796956, 4294942296, 4294894446, 1200,    4294796956, 4294943296, 4294894446, 0x007C, 0,  4,  0x0000)
    DeclActor(68500,   4294942296, 4294837296, 1200,    68500,   4294943296, 4294837296, 0x007C, 0,  5,  0x0000)
    DeclActor(89840,   10000,   4294880536, 1200,    89840,   11000,   4294880536, 0x007C, 0,  6,  0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3])                          # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5
    ChipFrameInfo(1000, 0, [0])                                  # 6
    ChipFrameInfo(1000, 0, [0])                                  # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 8
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_BEC",          # 00, 0
        "Function_1_C04",          # 01, 1
        "Function_2_C23",          # 02, 2
        "Function_3_C8B",          # 03, 3
        "Function_4_18C8",         # 04, 4
        "Function_5_1ADF",         # 05, 5
        "Function_6_1C30",         # 06, 6
        "Function_7_1E47",         # 07, 7
        "Function_8_1EC0",         # 08, 8
        "Function_9_2140",         # 09, 9
        "Function_10_2299",        # 0A, 10
        "Function_11_2519",        # 0B, 11
        "Function_12_2672",        # 0C, 12
        "Function_13_3D98",        # 0D, 13
        "Function_14_3E41",        # 0E, 14
        "Function_15_3E56",        # 0F, 15
        "Function_16_3E6B",        # 10, 16
        "Function_17_3E80",        # 11, 17
        "Function_18_3E95",        # 12, 18
        "Function_19_3EAA",        # 13, 19
        "Function_20_3EBF",        # 14, 20
        "Function_21_3ED4",        # 15, 21
        "Function_22_3EF3",        # 16, 22
        "Function_23_3F08",        # 17, 23
        "Function_24_3F1D",        # 18, 24
        "Function_25_3F32",        # 19, 25
        "Function_26_3F47",        # 1A, 26
        "Function_27_3F88",        # 1B, 27
        "Function_28_3FC9",        # 1C, 28
        "Function_29_4097",        # 1D, 29
        "Function_30_4B53",        # 1E, 30
        "Function_31_4BD9",        # 1F, 31
        "Function_32_4BE4",        # 20, 32
        "Function_33_4C25",        # 21, 33
        "Function_34_4C59",        # 22, 34
        "Function_35_584E",        # 23, 35
        "Function_36_58D4",        # 24, 36
        "Function_37_58DF",        # 25, 37
        "Function_38_5920",        # 26, 38
        "Function_39_5954",        # 27, 39
        "Function_40_625A",        # 28, 40
        "Function_41_6DDF",        # 29, 41
        "Function_42_6EBF",        # 2A, 42
    ))


    def Function_0_BEC(): pass

    label("Function_0_BEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C03")
    OP_A1(0xFE, 0x3E8, 0x1, 0x0)
    Jump("Function_0_BEC")

    label("loc_C03")

    Return()

    # Function_0_BEC end

    def Function_1_C04(): pass

    label("Function_1_C04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C22")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_1_C04")

    label("loc_C22")

    Return()

    # Function_1_C04 end

    def Function_2_C23(): pass

    label("Function_2_C23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    Event(0, 8)

    label("loc_C34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C45")
    Event(0, 10)

    label("loc_C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C56")
    Event(0, 39)

    label("loc_C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    Event(0, 40)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C7B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 41)
    Jump("loc_C8A")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C8A")
    ClearScenarioFlags(0x22, 1)
    Event(0, 42)

    label("loc_C8A")

    Return()

    # Function_2_C23 end

    def Function_3_C8B(): pass

    label("Function_3_C8B")

    OP_F0(0x1, 0x320)
    OP_1B(0x8, 0x0, 0x9)
    OP_1B(0x9, 0x0, 0xB)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB1")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_CB1")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CDE")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_CDE")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0B")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_D0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D2D")
    ModifyEventFlags(0, 3, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_D96")

    label("loc_D2D")

    OP_78(0x5, 0x9)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x1)
    SetChrPos(0x9, 125100, 0, -64560, 207)
    OP_93(0x9, 0xCF, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x2, 0x0, 125100, 0, -64560, 3000, 3000, 207000)

    label("loc_D96")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_175B")
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    Jump("loc_176A")

    label("loc_175B")

    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_17AC")
    SetMapObjFrame(0xFF, "magi_00a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07a_add", 0x0, 0x1)
    ClearMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_17F3")

    label("loc_17AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_END)), "loc_17E7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D6")
    ClearMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_17E2")

    label("loc_17D6")

    SetMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x4, 0x4)

    label("loc_17E2")

    Jump("loc_17F3")

    label("loc_17E7")

    SetMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x4, 0x4)

    label("loc_17F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_END)), "loc_1835")
    SetMapObjFrame(0xFF, "magi_00b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07b_add", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_187C")

    label("loc_1835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_END)), "loc_1870")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185F")
    ClearMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_186B")

    label("loc_185F")

    SetMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x3, 0x4)

    label("loc_186B")

    Jump("loc_187C")

    label("loc_1870")

    SetMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x3, 0x4)

    label("loc_187C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188F")
    OP_70(0x0, 0x0)
    Jump("loc_1893")

    label("loc_188F")

    OP_70(0x0, 0x1E)

    label("loc_1893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A6")
    OP_70(0x1, 0x0)
    Jump("loc_18AA")

    label("loc_18A6")

    OP_70(0x1, 0x1E)

    label("loc_18AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18BD")
    OP_70(0x2, 0x0)
    Jump("loc_18C1")

    label("loc_18BD")

    OP_70(0x2, 0x1E)

    label("loc_18C1")

    Sound(112, 1, 50, 0)
    Return()

    # Function_3_C8B end

    def Function_4_18C8(): pass

    label("Function_4_18C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A99")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C7")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1925():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1925)

    def lambda_193F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_193F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_A28", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_19A8"),
        (2, "loc_19B7"),
        (1, "loc_19C4"),
        (SWITCH_DEFAULT, "loc_19C7"),
    )


    label("loc_19A8")

    SetScenarioFlags(0x218, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_19C7")

    label("loc_19B7")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_19C4")

    OP_B9(0x0)
    Return()

    label("loc_19C7")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('绝耀珠', 1)"), scpexpr(EXPR_END)), "loc_1A24")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1A94")

    label("loc_1A24")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '绝耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A94")

    Jump("loc_1AD3")

    label("loc_1A99")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1AD3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_18C8 end

    def Function_5_1ADF(): pass

    label("Function_5_1ADF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDF")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('大回复药', 1)"), scpexpr(EXPR_END)), "loc_1B68")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1BDA")

    label("loc_1B68")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '大回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1BDA")

    Jump("loc_1C24")

    label("loc_1BDF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1C24")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1ADF end

    def Function_6_1C30(): pass

    label("Function_6_1C30")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E01")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2F")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1C8D():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C8D)

    def lambda_1CA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CA7)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A monster appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_A6C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1D10"),
        (2, "loc_1D1F"),
        (1, "loc_1D2C"),
        (SWITCH_DEFAULT, "loc_1D2F"),
    )


    label("loc_1D10")

    SetScenarioFlags(0x218, 5)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1D2F")

    label("loc_1D1F")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1D2C")

    OP_B9(0x0)
    Return()

    label("loc_1D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('光耀珠', 1)"), scpexpr(EXPR_END)), "loc_1D8C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1DFC")

    label("loc_1D8C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '光耀珠'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1DFC")

    Jump("loc_1E3B")

    label("loc_1E01")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1E3B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C30 end

    def Function_7_1E47(): pass

    label("Function_7_1E47")

    Battle("BattleInfo_9E4", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8E")
    OP_90(0x0, 123300, -2590, -74250, 187)
    EventEnd(0x5)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_1EBF")

    label("loc_1E8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA1")
    Jump("loc_1EBF")

    label("loc_1EA1")

    ModifyEventFlags(0, 3, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetScenarioFlags(0x1B8, 2)
    EventEnd(0x5)

    label("loc_1EBF")

    Return()

    # Function_7_1E47 end

    def Function_8_1EC0(): pass

    label("Function_8_1EC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(11820, 26000, -128070, 0)
    MoveCamera(355, 42, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14700, 0)
    SetChrPos(0x0, 14000, 25500, -127000, 135)
    SetChrPos(0x1, 14000, 25500, -127000, 135)
    SetChrPos(0x2, 14000, 25500, -127000, 135)
    SetChrPos(0x3, 14000, 25500, -127000, 135)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_1FD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1FD0)

    def lambda_1FE1():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FE1)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2038():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2038)

    def lambda_2049():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2049)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_20A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_20A6)

    def lambda_20B7():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_20B7)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_210E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_210E)

    def lambda_211F():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_211F)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_1EC0 end

    def Function_9_2140(): pass

    label("Function_9_2140")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2199():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2199)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_21E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_21E4)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_222F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_222F)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_227A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_227A)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9050", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2140 end

    def Function_10_2299(): pass

    label("Function_10_2299")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_68(-13590, 26000, -128639, 0)
    MoveCamera(1, 46, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14700, 0)
    SetChrPos(0x0, -14000, 25500, -127000, 135)
    SetChrPos(0x1, -14000, 25500, -127000, 135)
    SetChrPos(0x2, -14000, 25500, -127000, 135)
    SetChrPos(0x3, -14000, 25500, -127000, 135)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_23A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_23A9)

    def lambda_23BA():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_23BA)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2411():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2411)

    def lambda_2422():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2422)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_247F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_247F)

    def lambda_2490():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2490)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_24E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_24E7)

    def lambda_24F8():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_24F8)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_2299 end

    def Function_11_2519(): pass

    label("Function_11_2519")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2572():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2572)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_25BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_25BD)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2608():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2608)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2653():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2653)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9060", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2519 end

    def Function_12_2672(): pass

    label("Function_12_2672")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch03700.itc", 0x1E)
    SoundLoad(3788)
    OP_69(0x3, 0x0)
    CreatePortrait(0, 65514, 0, 490, 256, 0, 0, 512, 256, 0, 0, 512, 256, 0xFFFFFF, 0x0, "bu10801.itp")
    OP_68(0, 24100, -149710, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19420, 0)
    SetChrPos(0x101, 0, 20000, -151000, 0)
    SetChrPos(0x102, 1300, 20000, -151500, 0)
    SetChrPos(0x103, 200, 20000, -152300, 0)
    SetChrPos(0x104, -1300, 20000, -152300, 0)
    SetChrPos(0xF4, -700, 20000, -153800, 0)
    SetChrPos(0xF5, 900, 20000, -153500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    FadeToBright(1000, 0)

    def lambda_2799():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2799)
    Sleep(50)

    def lambda_27B1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27B1)
    Sleep(50)

    def lambda_27C9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27C9)
    Sleep(50)

    def lambda_27E1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27E1)
    Sleep(50)

    def lambda_27F9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_27F9)
    Sleep(50)

    def lambda_2811():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_2811)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5Phere……\x02",
    )

    CloseMessageWindow()

    def lambda_28CA():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28CA)
    Sleep(50)

    def lambda_28E2():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28E2)
    Sleep(50)

    def lambda_28FA():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28FA)
    Sleep(50)

    def lambda_2912():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2912)
    Sleep(50)

    def lambda_292A():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_292A)
    Sleep(50)

    def lambda_2942():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_2942)
    OP_68(0, 26100, -126840, 6000)
    MoveCamera(23, 9, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(16970, 6000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)
    BeginChrThread(0x101, 0, 0, 14)
    BeginChrThread(0x102, 0, 0, 15)
    BeginChrThread(0x103, 0, 0, 16)
    BeginChrThread(0x104, 0, 0, 17)
    BeginChrThread(0xF4, 0, 0, 18)
    BeginChrThread(0xF5, 0, 0, 19)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_29D9():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29D9)
    Sleep(50)

    def lambda_29E9():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29E9)
    Sleep(50)

    def lambda_29F9():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_29F9)
    Sleep(50)

    def lambda_2A09():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A09)
    Sleep(50)

    def lambda_2A19():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2A19)
    Sleep(50)

    def lambda_2A29():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2A29)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00301F#6Pwhat……?\x01",
            "Even though I see the barrier\x01",
            "It is covered but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PProbably somehow\x01",
            "I think it is \"barrier\", but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PAnyway in the middle ……\x01",
            "What are the left and right things?\x02",
        )
    )

    WaitChrThread(0x102, 0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(921, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3788V#40W#35AGiggle\x01",
            "They lead to the \"realm\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
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
    Fade(500)
    OP_68(0, 26900, -131200, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10640, 0)
    OP_68(0, 28500, -129850, 4000)
    MoveCamera(358, 13, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(22230, 4000)
    BeginChrThread(0x101, 0, 0, 20)
    BeginChrThread(0x102, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0x104, 0, 0, 23)
    BeginChrThread(0xF4, 0, 0, 24)
    BeginChrThread(0xF5, 0, 0, 25)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00107F#5PBell …! Is it?\x01",
            "… … It's a bell! Is it?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_68(0, 28000, -129850, 2000)
    MoveCamera(359, 8, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(16340, 2000)
    Sleep(500)
    Sound(223, 0, 60, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 0, 27800, -126500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 3, 0, 13)
    Sleep(800)

    def lambda_2D77():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D77)
    Sleep(50)

    def lambda_2D87():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D87)
    Sleep(50)

    def lambda_2D97():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2D97)
    Sleep(50)

    def lambda_2DA7():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DA7)
    Sleep(50)

    def lambda_2DB7():
        TurnDirection(0xF4, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2DB7)
    Sleep(50)

    def lambda_2DC7():
        TurnDirection(0xF5, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2DC7)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sleep(500)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WUfufu …\x01",
            "Ellie, of course.\x02\x03",
            "── Welcome to \"Ao no Taiki\".\x02\x03",
            "Have you come\x01",
            "Ka'a would also be pleased.\x02\x03",
            "No … ──\x01",
            "Is he rather sad?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)

    ChrTalk(
        0x102,
        "#00101F#12P#NBell …… you … …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NRegardless of your intention ……\x02\x03",
            "#00001FAnyhow, we\x01",
            "I do not think he is going to hinder it, is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WYeah, this \"shinto area\" is\x01",
            "Kaoru's inner face … …\x02\x03",
            "I want you to come,\x01",
            "The appearance of the heart that I do not want to come\x01",
            "It is reflected as it is.\x02\x03",
            "In the form of a guardian that wanders around\x01",
            "It is a translation that appears.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_313F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3112")
    OP_FC(0x6)
    Jump("loc_3115")

    label("loc_3112")

    OP_FC(0xC)

    label("loc_3115")


    ChrTalk(
        0x10A,
        "#00601F#13P#NSuch a mechanism ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_31EC")

    label("loc_313F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_319A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3169")
    OP_FC(0x6)
    Jump("loc_316C")

    label("loc_3169")

    OP_FC(0xC)

    label("loc_316C")


    ChrTalk(
        0x109,
        "#10111F#13P#NThat's how it works …\x02",
    )

    CloseMessageWindow()
    Jump("loc_31EC")

    label("loc_319A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31C4")
    OP_FC(0x6)
    Jump("loc_31C7")

    label("loc_31C4")

    OP_FC(0xC)

    label("loc_31C7")


    ChrTalk(
        0x106,
        "#10712F#13P#NSuch a mechanism ……\x02",
    )

    CloseMessageWindow()

    label("loc_31EC")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3267")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3219")
    OP_FC(0x6)
    Jump("loc_321C")

    label("loc_3219")

    OP_FC(0xC)

    label("loc_321C")


    ChrTalk(
        0x105,
        (
            "#10406F#13P#NJust inside spiritual\x01",
            "Did you build a space like this …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3338")

    label("loc_3267")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32D3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3291")
    OP_FC(0x6)
    Jump("loc_3294")

    label("loc_3291")

    OP_FC(0xC)

    label("loc_3294")


    ChrTalk(
        0x106,
        (
            "#10706F#13P#NJust inside spiritual\x01",
            "Only this space ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3338")

    label("loc_32D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3338")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32FD")
    OP_FC(0x6)
    Jump("loc_3300")

    label("loc_32FD")

    OP_FC(0xC)

    label("loc_3300")


    ChrTalk(
        0x109,
        (
            "#10108F#13P#NThis is Ka'a-chan's\x01",
            "Space in mind ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3338")

    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WHuh, but it is the last party.\x02\x03",
            "To make you enjoy more,\x01",
            "We had different venues prepared.\x02\x03",
            "That's what those \"gates\" are.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
    OP_68(-10270, 25300, -123110, 0)
    MoveCamera(308, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21680, 0)
    Fade(500)
    OP_0D()

    def lambda_343B():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_343B)
    Sleep(50)

    def lambda_344B():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_344B)
    Sleep(50)

    def lambda_345B():
        OP_93(0xF4, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_345B)
    Sleep(50)

    def lambda_346B():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_346B)
    Sleep(50)

    def lambda_347B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_347B)
    Sleep(50)

    def lambda_348B():
        OP_93(0xF5, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_348B)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_68(10270, 25300, -123110, 0)
    MoveCamera(52, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21680, 0)
    Fade(500)
    OP_0D()

    def lambda_34E7():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_34E7)
    Sleep(50)

    def lambda_34F7():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34F7)
    Sleep(50)

    def lambda_3507():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3507)
    Sleep(50)

    def lambda_3517():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3517)
    Sleep(50)

    def lambda_3527():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3527)
    Sleep(50)

    def lambda_3537():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3537)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xF5, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 28000, -129850, 0)
    MoveCamera(359, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16340, 0)
    OP_0D()
    Sleep(200)

    def lambda_3596():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3596)
    Sleep(50)

    def lambda_35A6():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_35A6)
    Sleep(50)

    def lambda_35B6():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_35B6)
    Sleep(50)

    def lambda_35C6():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_35C6)
    Sleep(50)

    def lambda_35D6():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_35D6)
    Sleep(50)

    def lambda_35E6():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_35E6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00201F#6P#NAnother venue ……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NOoooi …… Well done\x01",
            "Could you stop it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WUhufu, that's easy.\x02\x03",
            "This \"god area\" is Kaoru's\x01",
            "It reflects the inside … …\x02\x03",
            "In those gates,\x01",
            "It reflects the inner face of other people\x01",
            "It leads to \"area\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
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

    ChrTalk(
        0x101,
        "#00007F#6P#NOther people …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#12P#NWell, maybe ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30WHuff, \"Edge#2RLast#\"If there is someone\x01",
            "Let's get into another venue as well.\x02\x03",
            "Now - ___ this is the guide.\x01",
            "We are waiting for you at this venue.\x02\x03",
            "You are safe,\x01",
            "I wish I could live and get there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x1, 0x800)
    Sound(223, 0, 60, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x8, 2)
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    OP_68(0, 26500, -131690, 2500)
    MoveCamera(0, 22, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(11640, 2500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00106F#11P…… Bell ………\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#5PIndeed plague is too much ……\x02\x03",
            "#00008FHowever, regardless of the central gate,\x01",
            "I can seem to be able to enter the right and left gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PThe problem is \"who\"\x01",
            "Is it after that …?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00306F#5PLet's try it for the time being.\x02\x03",
            "#00300FApparently I have someone with a relationship\x01",
            "I do not want to put it inside.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BB0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BB0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C02")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BE2")
    OP_FC(0x6)
    Jump("loc_3BE5")

    label("loc_3BE2")

    OP_FC(0xC)

    label("loc_3BE5")


    ChrTalk(
        0x105,
        "#10408F#13PYeah……\x02",
    )

    CloseMessageWindow()

    label("loc_3C02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C4A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C2C")
    OP_FC(0x6)
    Jump("loc_3C2F")

    label("loc_3C2C")

    OP_FC(0xC)

    label("loc_3C2F")


    ChrTalk(
        0x106,
        "#10708F#13P……Yes.\x02",
    )

    CloseMessageWindow()

    label("loc_3C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C74")
    OP_FC(0x6)
    Jump("loc_3C77")

    label("loc_3C74")

    OP_FC(0xC)

    label("loc_3C77")


    ChrTalk(
        0x109,
        (
            "#10101F#13PIf it seems necessary\x01",
            "The one who returned to Mercapa once\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D47")

    label("loc_3CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF7")
    OP_FC(0x6)
    Jump("loc_3CFA")

    label("loc_3CF7")

    OP_FC(0xC)

    label("loc_3CFA")


    ChrTalk(
        0x10A,
        (
            "#00601F#13PIf it is necessary\x01",
            "The one who returned to Mercapa once\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D47")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 25000, -131700, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 3)
    OP_29(0xB2, 0x1, 0x2)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_2672 end

    def Function_13_3D98(): pass

    label("Function_13_3D98")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x1F4)

    def lambda_3DA8():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DA8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x320)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x96)

    label("loc_3DE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DFA")
    Sleep(50)
    Jump("loc_3DE3")

    label("loc_3DFA")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x96)
    Sleep(300)
    Sleep(50)

    def lambda_3E10():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E10)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    Sleep(300)
    Return()

    # Function_13_3D98 end

    def Function_14_3E41(): pass

    label("Function_14_3E41")

    Sleep(100)
    OP_93(0xFE, 0x4B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xC3, 0x1F4)
    Return()

    # Function_14_3E41 end

    def Function_15_3E56(): pass

    label("Function_15_3E56")

    Sleep(200)
    OP_93(0xFE, 0x11D, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xA5, 0x1F4)
    Return()

    # Function_15_3E56 end

    def Function_16_3E6B(): pass

    label("Function_16_3E6B")

    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_16_3E6B end

    def Function_17_3E80(): pass

    label("Function_17_3E80")

    Sleep(400)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x14A, 0x1F4)
    Return()

    # Function_17_3E80 end

    def Function_18_3E95(): pass

    label("Function_18_3E95")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_18_3E95 end

    def Function_19_3EAA(): pass

    label("Function_19_3EAA")

    Sleep(600)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_19_3EAA end

    def Function_20_3EBF(): pass

    label("Function_20_3EBF")

    Sleep(500)
    OP_93(0xFE, 0xC3, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x4B, 0x1F4)
    Return()

    # Function_20_3EBF end

    def Function_21_3ED4(): pass

    label("Function_21_3ED4")

    Sleep(200)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_21_3ED4 end

    def Function_22_3EF3(): pass

    label("Function_22_3EF3")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_22_3EF3 end

    def Function_23_3F08(): pass

    label("Function_23_3F08")

    Sleep(400)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_3F08 end

    def Function_24_3F1D(): pass

    label("Function_24_3F1D")

    Sleep(650)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(450)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_24_3F1D end

    def Function_25_3F32(): pass

    label("Function_25_3F32")

    Sleep(550)
    OP_93(0xFE, 0x6E, 0x1F4)
    Sleep(550)
    OP_93(0xFE, 0xE6, 0x1F4)
    Return()

    # Function_25_3F32 end

    def Function_26_3F47(): pass

    label("Function_26_3F47")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F5F")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_3F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F73")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_3F73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F87")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3F87")

    Return()

    # Function_26_3F47 end

    def Function_27_3F88(): pass

    label("Function_27_3F88")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FA0")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_3FA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FB4")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_3FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FC8")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_3FC8")

    Return()

    # Function_27_3F88 end

    def Function_28_3FC9(): pass

    label("Function_28_3FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4028")
    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FF6")
    OP_CF(0x1, 0xF5, 0x4)
    Jump("loc_4023")

    label("loc_3FF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_400F")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_4023")

    label("loc_400F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4023")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4023")

    Jump("loc_4096")

    label("loc_4028")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_406E")
    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4055")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_4069")

    label("loc_4055")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4069")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4069")

    Jump("loc_4096")

    label("loc_406E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4096")
    OP_CF(0x1, 0xF4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4096")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4096")

    Return()

    # Function_28_3FC9 end

    def Function_29_4097(): pass

    label("Function_29_4097")

    EventBegin(0x0)
    OP_E2(0x3)
    SoundLoad(3577)
    SoundLoad(3578)
    SoundLoad(3579)
    Fade(500)
    OP_69(0x3, 0x0)
    OP_68(-12140, 25800, -128789, 0)
    MoveCamera(356, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40F3")
    Call(0, 26)
    Jump("loc_40F6")

    label("loc_40F3")

    Call(0, 28)

    label("loc_40F6")

    SetChrPos(0x101, -12000, 25800, -129000, 315)
    SetChrPos(0x102, -10750, 25800, -130250, 315)
    SetChrPos(0x103, -12200, 25000, -131200, 315)
    SetChrPos(0x104, -9800, 25000, -128800, 315)
    SetChrPos(0xF4, -10750, 25000, -131500, 315)
    SetChrPos(0xF5, -9500, 25000, -130250, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4282")
    BeginChrThread(0x101, 0, 0, 30)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4226")

    ChrTalk(
        0x101,
        (
            "#00006F#5PIs it useless?\x02\x03",
            "#00001FApparently it attacks\x01",
            "It looks like it can not be broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PAt least who is inside\x01",
            "If only I know there ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4282")

    label("loc_4226")


    ChrTalk(
        0x101,
        "#00003F#5P… … Is it the same as the right gate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PHere …\x01",
            "Who the hell are you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4282")

    OP_68(-14000, 26500, -127000, 2000)
    MoveCamera(340, 17, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(15680, 2000)
    OP_6F(0x79)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 31)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3577V#50W#40AKukuku …… Kakaka ………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3578V#50W#50A……I am……\x01",
            "My power is the strongest … ….\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3579V#50W#50AOh yeah … …\x01",
            "More than that fellow ….!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_68(-11820, 26000, -128740, 2000)
    MoveCamera(346, 20, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13300, 2000)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D7")

    ChrTalk(
        0x105,
        (
            "#10408F#12P…… Completely.\x01",
            "Why is it like me\x01",
            "Are you sticking to the heir?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_44D5():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44D5)
    Sleep(50)

    def lambda_44E5():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_44E5)
    Sleep(50)

    def lambda_44F5():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_44F5)
    Sleep(50)

    def lambda_4505():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4505)
    Sleep(50)

    def lambda_4515():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4515)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        "#00008F#5PWadi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PPick me, Lloyd.\x02\x03",
            "#10401FApparently \"he\" is\x01",
            "It seems to have decided with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P……I understood.\x02",
    )

    CloseMessageWindow()

    def lambda_45C8():
        OP_96(0xFE, 0xFFFFD508, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45C8)

    def lambda_45E2():

        label("loc_45E2")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_45E2")

    QueueWorkItem2(0x101, 2, lambda_45E2)

    def lambda_45F4():

        label("loc_45F4")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_45F4")

    QueueWorkItem2(0x102, 2, lambda_45F4)

    def lambda_4606():

        label("loc_4606")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4606")

    QueueWorkItem2(0x103, 2, lambda_4606)

    def lambda_4618():

        label("loc_4618")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4618")

    QueueWorkItem2(0x104, 2, lambda_4618)

    def lambda_462A():

        label("loc_462A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_462A")

    QueueWorkItem2(0xF5, 2, lambda_462A)
    Sleep(300)
    OP_68(-12230, 26000, -127620, 2000)
    MoveCamera(358, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_466D():
        OP_95(0xFE, -12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_466D)
    Sleep(150)

    def lambda_468A():
        OP_9B(0x1, 0xFE, 0x2D, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_468A)
    Sleep(500)

    def lambda_46A2():
        OP_96(0xFE, 0xFFFFD602, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_46A2)
    WaitChrThread(0x105, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x105, 0, 0, 32)
    WaitChrThread(0x105, 0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0x4, 0x1, 0x3E8)
    Sleep(1000)
    Sleep(500)
    BeginChrThread(0x105, 0, 0, 33)
    WaitChrThread(0x105, 0)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF5, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x4, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4780")

    ChrTalk(
        0x102,
        "#00105F#12PThe barrier disappeared …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PWith this \"area\" in place\x01",
            "Is it possible to go …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_47D2")

    label("loc_4780")


    ChrTalk(
        0x103,
        "#00201F#6P#NIt has disappeared …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#11PWith this I can not go to \"area\" …\x02",
    )

    CloseMessageWindow()

    label("loc_47D2")

    Sleep(200)
    OP_93(0x105, 0x87, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10406F#5POh … but this time\x01",
            "You will not finish playing.\x02\x03",
            "#10400FLet's face it in perfect attitude.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4943")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A1")

    ChrTalk(
        0x109,
        (
            "#10108F#12PEven if I return to Mercapa\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_493E")

    label("loc_48A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48F0")

    ChrTalk(
        0x10A,
        (
            "#00603F#12PEven if I return to Mercapa\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_493E")

    label("loc_48F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_493E")

    ChrTalk(
        0x106,
        (
            "#10708F#12PEven if I return to Mercapa\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_493E")

    Jump("loc_49CA")

    label("loc_4943")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4973")

    ChrTalk(
        0x109,
        "#10101F#12PYup……!\x02",
    )

    CloseMessageWindow()
    Jump("loc_49CA")

    label("loc_4973")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_499F")

    ChrTalk(
        0x10A,
        "#00601F#12PYes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_49CA")

    label("loc_499F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49CA")

    ChrTalk(
        0x106,
        "#10701F#12PYes……!\x02",
    )

    CloseMessageWindow()

    label("loc_49CA")

    SetScenarioFlags(0x1AA, 1)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_4B14")

    label("loc_49D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_END)), "loc_4A96")

    ChrTalk(
        0x103,
        (
            "#00205F#12PThe barriers are returning to the original …\x02\x03",
            "#00203FApparently, without Wajian\x01",
            "It does not seem to fit in this \"area\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh … … back to Mercava\x01",
            "Let's bring Wadisu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B14")

    label("loc_4A96")


    ChrTalk(
        0x103,
        (
            "#00208F#12P…… \"Who\" is there?\x01",
            "It is clearly obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh … … back to Mercava\x01",
            "Do you bring him?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B14")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -10750, 25800, -130250, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 4)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_4097 end

    def Function_30_4B53(): pass

    label("Function_30_4B53")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Return()

    # Function_30_4B53 end

    def Function_31_4BD9(): pass

    label("Function_31_4BD9")

    Sleep(800)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_4BD9 end

    def Function_32_4BE4(): pass

    label("Function_32_4BE4")

    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_32_4BE4 end

    def Function_33_4C25(): pass

    label("Function_33_4C25")

    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    Sleep(200)
    Return()

    # Function_33_4C25 end

    def Function_34_4C59(): pass

    label("Function_34_4C59")

    EventBegin(0x0)
    OP_E2(0x3)
    SoundLoad(3961)
    SoundLoad(3962)
    SoundLoad(3963)
    Fade(500)
    OP_69(0x3, 0x0)
    OP_68(12140, 25800, -128789, 0)
    MoveCamera(4, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13750, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CB5")
    Call(0, 27)
    Jump("loc_4CB8")

    label("loc_4CB5")

    Call(0, 28)

    label("loc_4CB8")

    SetChrPos(0x101, 12000, 25800, -129000, 45)
    SetChrPos(0x102, 10750, 25800, -130250, 45)
    SetChrPos(0x103, 12200, 25000, -131200, 45)
    SetChrPos(0x104, 9800, 25000, -128800, 45)
    SetChrPos(0xF4, 10750, 25000, -131500, 45)
    SetChrPos(0xF5, 9500, 25000, -130250, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E3D")
    BeginChrThread(0x101, 0, 0, 35)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE1")

    ChrTalk(
        0x101,
        (
            "#00006F#11PIs it useless?\x02\x03",
            "Apparently it attacks\x01",
            "It looks like it can not be broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAt least who is inside\x01",
            "If only I know there ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E3D")

    label("loc_4DE1")


    ChrTalk(
        0x101,
        "#00003F#11P…… Is it the same as the left gate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PHere …\x01",
            "Who the hell are you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3D")

    OP_68(14000, 26500, -127000, 2000)
    MoveCamera(20, 17, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(15680, 2000)
    OP_6F(0x79)
    Sound(921, 0, 100, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    BeginChrThread(0x101, 0, 0, 36)
    OP_C9(0x0, 0x800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3961V#40W#40AFuhu … … Ahahahaha ………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3962V#40W#38ANot yet …\x01",
            "I wonder if I still come …?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3963V#40W#38AI am having too much fun\x01",
            "I can not wait … …!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_C9(0x1, 0x80000000)
    OP_68(11820, 26000, -128740, 2000)
    MoveCamera(14, 20, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13300, 2000)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_566B")

    ChrTalk(
        0x106,
        "#10708F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PWhew …… It's me.\x02\x03",
            "#00301FMoreover, it is apparently waiting\x01",
            "It seems not to me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_50D2():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50D2)
    Sleep(50)

    def lambda_50E2():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_50E2)
    Sleep(50)

    def lambda_50F2():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_50F2)
    Sleep(50)

    def lambda_5102():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5102)
    Sleep(50)

    def lambda_5112():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5112)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#11P…… Hello, Lisa.\x02\x03",
            "#00001FIf possible we can\x01",
            "Leave it to us …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#6P─ ─ ─ No.\x02\x03",
            "#10708FIn a sense, I and she,\x01",
            "There are similar circumstances.\x02\x03",
            "I myself am going to the road ahead\x01",
            "To find out … ….\x02\x03",
            "#10701FI, once again with her,\x01",
            "You see#2RMami#Do not make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P………I understood.\x02",
    )

    CloseMessageWindow()

    def lambda_526B():
        OP_96(0xFE, 0x2AF8, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_526B)

    def lambda_5285():

        label("loc_5285")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5285")

    QueueWorkItem2(0x101, 2, lambda_5285)

    def lambda_5297():

        label("loc_5297")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5297")

    QueueWorkItem2(0x102, 2, lambda_5297)

    def lambda_52A9():

        label("loc_52A9")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_52A9")

    QueueWorkItem2(0x103, 2, lambda_52A9)

    def lambda_52BB():

        label("loc_52BB")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_52BB")

    QueueWorkItem2(0x104, 2, lambda_52BB)

    def lambda_52CD():

        label("loc_52CD")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_52CD")

    QueueWorkItem2(0xF5, 2, lambda_52CD)
    Sleep(300)
    OP_68(12230, 26000, -127620, 2000)
    MoveCamera(2, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_5310():
        OP_95(0xFE, 12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5310)
    Sleep(150)

    def lambda_532D():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_532D)
    WaitChrThread(0x106, 1)

    def lambda_5346():
        OP_96(0xFE, 0x29FE, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5346)
    WaitChrThread(0x106, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x106, 0, 0, 37)
    WaitChrThread(0x106, 0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0x3, 0x1, 0x3E8)
    Sleep(1000)
    Sleep(500)
    BeginChrThread(0x106, 0, 0, 38)
    WaitChrThread(0x106, 0)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF5, 0x2)
    ClearMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5422")

    ChrTalk(
        0x102,
        "#00105F#6PThe barrier disappeared …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PWith this \"area\" in place\x01",
            "Is it possible to go …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_5473")

    label("loc_5422")


    ChrTalk(
        0x103,
        "#00201F#6P#NIt has disappeared …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#5PWith this I can not go to \"area\" …\x02",
    )

    CloseMessageWindow()

    label("loc_5473")

    Sleep(200)
    OP_93(0x106, 0xE1, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#10703F… ….#11PThe other party is an opponent.\x02\x03",
            "#10710FTo avoid being overwhelmed unilaterally,\x01",
            "Let's face thorough attitude.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55DA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_553C")

    ChrTalk(
        0x109,
        (
            "#10106F#6PEven if I return to Mercapa\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D5")

    label("loc_553C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_558A")

    ChrTalk(
        0x10A,
        (
            "#00603F#6PEven if I return to Mercapa\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D5")

    label("loc_558A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55D5")

    ChrTalk(
        0x105,
        (
            "#10404F#6PEven if I return to Mercapa\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D5")

    Jump("loc_565E")

    label("loc_55DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5609")

    ChrTalk(
        0x109,
        "#10101F#6PYeah … …!\x02",
    )

    CloseMessageWindow()
    Jump("loc_565E")

    label("loc_5609")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5634")

    ChrTalk(
        0x10A,
        "#00601F#6PAh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_565E")

    label("loc_5634")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_565E")

    ChrTalk(
        0x105,
        "#10402F#6PYeah.\x02",
    )

    CloseMessageWindow()

    label("loc_565E")

    SetScenarioFlags(0x1AA, 2)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_580F")

    label("loc_566B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_END)), "loc_572B")

    ChrTalk(
        0x104,
        (
            "#00305F#5PBarriers are restored to the original …\x02\x03",
            "#00303FWith Lisha-chan\x01",
            "In this \"area\"\x01",
            "You can not enter it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5POh … … back to Mercava\x01",
            "Let's bring Lisha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_580F")

    label("loc_572B")


    ChrTalk(
        0x104,
        (
            "#00306F#5PWhew …… It's me.\x02\x03",
            "#00301FMoreover, it is apparently waiting\x01",
            "It seems not to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PAh……\x02\x03",
            "#00008F(Return to Mercapa \"She\"\x01",
            "I need to bring them … …)\x02\x03",
            "(Can you really bring me?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_580F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 10750, 25800, -130250, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 5)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_4C59 end

    def Function_35_584E(): pass

    label("Function_35_584E")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(2000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Return()

    # Function_35_584E end

    def Function_36_58D4(): pass

    label("Function_36_58D4")

    Sleep(800)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_36_58D4 end

    def Function_37_58DF(): pass

    label("Function_37_58DF")

    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x4E2, 0x3E8, 0x0)
    Sleep(600)
    Sound(812, 0, 100, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_37_58DF end

    def Function_38_5920(): pass

    label("Function_38_5920")

    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x3E8, 0x1)
    Sleep(200)
    Return()

    # Function_38_5920 end

    def Function_39_5954(): pass

    label("Function_39_5954")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_69(0x3, 0x0)
    OP_68(-13590, 26000, -128639, 0)
    MoveCamera(1, 46, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13700, 0)
    SetChrPos(0x101, -14000, 25500, -127000, 135)
    SetChrPos(0x102, -14000, 25500, -127000, 135)
    SetChrPos(0x103, -14000, 25500, -127000, 135)
    SetChrPos(0x104, -14000, 25500, -127000, 135)
    SetChrPos(0xF4, -14000, 25500, -127000, 135)
    SetChrPos(0xF5, -14000, 25500, -127000, 135)
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
    SetMapObjFrame(0xFF, "magi_00a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07a_add", 0x0, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    SetCameraDistance(14700, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5AEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AEA)

    def lambda_5AFB():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AFB)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5B52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5B52)

    def lambda_5B63():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B63)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5BC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5BC0)

    def lambda_5BD1():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BD1)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5C28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5C28)

    def lambda_5C39():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C39)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5C96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_5C96)

    def lambda_5CA7():
        OP_95(0xFE, -12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_5CA7)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5CFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_5CFE)

    def lambda_5D0F():
        OP_95(0xFE, -11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_5D0F)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_END)), "loc_5FB1")
    OP_29(0xB2, 0x1, 0x5)
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
    OP_68(-8500, 26200, -127000, 2500)
    MoveCamera(20, 18, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(19020, 2500)

    def lambda_5E03():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5E03)
    Sleep(50)

    def lambda_5E13():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5E13)
    Sleep(50)

    def lambda_5E23():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5E23)
    Sleep(50)

    def lambda_5E33():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5E33)
    Sleep(50)

    def lambda_5E43():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_5E43)
    Sleep(50)

    def lambda_5E53():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_5E53)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F#6P#NThe barrier is … …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NApparently two \"regions\"\x01",
            "It's because you released it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHuh, finally this\x01",
            "You started to move on.\x02\x03",
            "#10408F…… a bit before that\x01",
            "I feel like going back to the ship and taking a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PThat's right … There are reports to everyone,\x01",
            "You may return to Mercapa once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_621D")

    label("loc_5FB1")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-8500, 26200, -127000, 3000)
    MoveCamera(20, 18, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(19020, 3000)

    def lambda_6059():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6059)
    Sleep(50)

    def lambda_6069():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6069)
    Sleep(50)

    def lambda_6079():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6079)
    Sleep(50)

    def lambda_6089():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6089)
    Sleep(50)

    def lambda_6099():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6099)
    Sleep(50)

    def lambda_60A9():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_60A9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005F#6PThe barrier of the central gate ……\x01",
            "Are you getting thinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PMr. Wald's \"area\"\x01",
            "It seemed to have been released.\x02\x03",
            "#00201FPerhaps, this \"god area\" is\x01",
            "Each person's \"area\" and\x01",
            "I think that they are interlocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P#NThat means that the other\x01",
            "If I could release \"area\" …?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10400F#6PPerhaps, that perfect barrier\x01",
            "It will be to annihilate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_621D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -12000, 25500, -129300, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_39_5954 end

    def Function_40_625A(): pass

    label("Function_40_625A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "event\\ev202_00.eff")
    OP_69(0x3, 0x0)
    OP_68(11820, 26000, -128070, 0)
    MoveCamera(355, 42, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13700, 0)
    SetChrPos(0x101, 14000, 25500, -127000, 225)
    SetChrPos(0x102, 14000, 25500, -127000, 225)
    SetChrPos(0x103, 14000, 25500, -127000, 225)
    SetChrPos(0x104, 14000, 25500, -127000, 225)
    SetChrPos(0xF4, 14000, 25500, -127000, 225)
    SetChrPos(0xF5, 14000, 25500, -127000, 225)
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
    SetMapObjFrame(0xFF, "magi_00b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "magi_07b_add", 0x0, 0x1)
    ModifyEventFlags(0, 2, 0x80)
    SetCameraDistance(14700, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_663B")
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_63F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63F8)

    def lambda_6409():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6409)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6460():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6460)

    def lambda_6471():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6471)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_64CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_64CE)

    def lambda_64DF():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64DF)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6536():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6536)

    def lambda_6547():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6547)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_65A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_65A4)

    def lambda_65B5():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_65B5)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_660C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_660C)

    def lambda_661D():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_661D)
    WaitChrThread(0xF5, 1)
    Jump("loc_68BE")

    label("loc_663B")

    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6680():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6680)

    def lambda_6691():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_6691)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_66E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66E8)

    def lambda_66F9():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66F9)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6756():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6756)

    def lambda_6767():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6767)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_67BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_67BE)

    def lambda_67CF():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67CF)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_682C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_682C)

    def lambda_683D():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_683D)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6894():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6894)

    def lambda_68A5():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_68A5)
    WaitChrThread(0xF5, 1)

    label("loc_68BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_6B2E")
    OP_29(0xB2, 0x1, 0x5)
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
    OP_68(8500, 26200, -127000, 2500)
    MoveCamera(340, 18, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(19020, 2500)

    def lambda_6999():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6999)
    Sleep(50)

    def lambda_69A9():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_69A9)
    Sleep(50)

    def lambda_69B9():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_69B9)
    Sleep(50)

    def lambda_69C9():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_69C9)
    Sleep(50)

    def lambda_69D9():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_69D9)
    Sleep(50)

    def lambda_69E9():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_69E9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F#12PThe barrier is … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#NApparently two \"regions\"\x01",
            "It's because you released it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10702F#12PAt last\x01",
            "You can go ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11POh, but as expected\x01",
            "It was a tough fight …\x02\x03",
            "#00000FThere are reports to everyone,\x01",
            "You may return to Mercapa once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DA2")

    label("loc_6B2E")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(8500, 26200, -127000, 3000)
    MoveCamera(340, 18, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(19020, 3000)

    def lambda_6BD6():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6BD6)
    Sleep(50)

    def lambda_6BE6():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6BE6)
    Sleep(50)

    def lambda_6BF6():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6BF6)
    Sleep(50)

    def lambda_6C06():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6C06)
    Sleep(50)

    def lambda_6C16():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6C16)
    Sleep(50)

    def lambda_6C26():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6C26)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00005F#12PThe barrier of the central gate ……\x01",
            "Are you getting thinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P#NShirley's \"area\"\x01",
            "It seemed to have been released.\x02\x03",
            "#00201FPerhaps, this \"god area\" is\x01",
            "Each person's \"area\" and\x01",
            "I think that they are interlocked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#12PThat means that the other\x01",
            "If I could release \"area\" …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702F#12PPerhaps, that perfect barrier\x01",
            "It may be annihilated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DA2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 12000, 25500, -129300, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A8, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_625A end

    def Function_41_6DDF(): pass

    label("Function_41_6DDF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "event/ev17015.eff")
    OP_69(0x3, 0x0)
    OP_68(0, 27700, -122500, 0)
    MoveCamera(21, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17850, 0)
    SetCameraDistance(22850, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 28500, -122500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    SetMapObjFrame(0xFF, "magi_07a_add", 0x0, 0x1)
    Sleep(3000)
    StopSound(112, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9062", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_6DDF end

    def Function_42_6EBF(): pass

    label("Function_42_6EBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "event/ev17014.eff")
    OP_69(0x3, 0x0)
    OP_68(0, 27700, -122500, 0)
    MoveCamera(339, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(17850, 0)
    SetCameraDistance(22850, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 0, 28500, -122500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 50, 0)
    Sound(223, 0, 100, 0)
    SetMapObjFrame(0xFF, "magi_07b_add", 0x0, 0x1)
    Sleep(3000)
    StopSound(112, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("m9052", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_6EBF end

    SaveToFile()

Try(main)
