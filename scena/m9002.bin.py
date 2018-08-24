from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Mariabell",              # 1
        "Cryptid",                # 2
        "Gold Statue",            # 3
        "Dark Blue Zone",         # 4
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

    Sepith("Sepith_72AB", 7,   7,   7,   7,   11,  11,  11)
    Sepith("Sepith_72C3", 9,   9,   9,   9,   10,  10,  10)
    Sepith("Sepith_72A3", 13,  13,  13,  13,  4,   4,   4)
    Sepith("Sepith_72CB", 11,  23,  0,   15,  0,   0,   19)
    Sepith("Sepith_72BB", 0,   0,   0,   0,   15,  38,  15)

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
        "BattleInfo_6AC", 0x0000, 100, 6, 60, 10, 1, 40, 0, "bm9010", "Sepith_72AB", 40, 30, 20, 10,
        (
            ("ms80900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_72C3", 40, 30, 20, 10,
        (
            ("ms79900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
        )
    )

    BattleInfo(
        "BattleInfo_610", 0x0000, 100, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_72A3", 50, 30, 20, 0,
        (
            ("ms85300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_72CB", 100, 0, 0, 0,
        (
            ("ms85200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0010, 100, 6, 180, 10, 1, 5, 0, "bm9010", "Sepith_72BB", 50, 35, 15, 0,
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
        "Function_5_1AE3",         # 05, 5
        "Function_6_1C34",         # 06, 6
        "Function_7_1E4F",         # 07, 7
        "Function_8_1EC8",         # 08, 8
        "Function_9_2148",         # 09, 9
        "Function_10_22A1",        # 0A, 10
        "Function_11_2521",        # 0B, 11
        "Function_12_267A",        # 0C, 12
        "Function_13_3EC8",        # 0D, 13
        "Function_14_3F71",        # 0E, 14
        "Function_15_3F86",        # 0F, 15
        "Function_16_3F9B",        # 10, 16
        "Function_17_3FB0",        # 11, 17
        "Function_18_3FC5",        # 12, 18
        "Function_19_3FDA",        # 13, 19
        "Function_20_3FEF",        # 14, 20
        "Function_21_4004",        # 15, 21
        "Function_22_4023",        # 16, 22
        "Function_23_4038",        # 17, 23
        "Function_24_404D",        # 18, 24
        "Function_25_4062",        # 19, 25
        "Function_26_4077",        # 1A, 26
        "Function_27_40B8",        # 1B, 27
        "Function_28_40F9",        # 1C, 28
        "Function_29_41C7",        # 1D, 29
        "Function_30_4D0F",        # 1E, 30
        "Function_31_4D95",        # 1F, 31
        "Function_32_4DA0",        # 20, 32
        "Function_33_4DE1",        # 21, 33
        "Function_34_4E15",        # 22, 34
        "Function_35_5A6E",        # 23, 35
        "Function_36_5AF4",        # 24, 36
        "Function_37_5AFF",        # 25, 37
        "Function_38_5B40",        # 26, 38
        "Function_39_5B74",        # 27, 39
        "Function_40_64E5",        # 28, 40
        "Function_41_70BB",        # 29, 41
        "Function_42_719B",        # 2A, 42
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CB")
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
            "Monsters appeared!\x07\x00\x02",
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
        (0, "loc_19AC"),
        (2, "loc_19BB"),
        (1, "loc_19C8"),
        (SWITCH_DEFAULT, "loc_19CB"),
    )


    label("loc_19AC")

    SetScenarioFlags(0x218, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_19CB")

    label("loc_19BB")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_19C8")

    OP_B9(0x0)
    Return()

    label("loc_19CB")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8E, 1)"), scpexpr(EXPR_END)), "loc_1A24")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
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

    label("loc_1A94")

    Jump("loc_1AD7")

    label("loc_1A99")

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

    label("loc_1AD7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_18C8 end

    def Function_5_1AE3(): pass

    label("Function_5_1AE3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDF")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1B68")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
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

    label("loc_1BDA")

    Jump("loc_1C28")

    label("loc_1BDF")

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

    label("loc_1C28")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1AE3 end

    def Function_6_1C34(): pass

    label("Function_6_1C34")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E05")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D37")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1C91():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C91)

    def lambda_1CAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CAB)
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
    Battle("BattleInfo_A6C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1D18"),
        (2, "loc_1D27"),
        (1, "loc_1D34"),
        (SWITCH_DEFAULT, "loc_1D37"),
    )


    label("loc_1D18")

    SetScenarioFlags(0x218, 5)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1D37")

    label("loc_1D27")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1D34")

    OP_B9(0x0)
    Return()

    label("loc_1D37")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7F, 1)"), scpexpr(EXPR_END)), "loc_1D90")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x200, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1E00")

    label("loc_1D90")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
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

    label("loc_1E00")

    Jump("loc_1E43")

    label("loc_1E05")

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

    label("loc_1E43")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C34 end

    def Function_7_1E4F(): pass

    label("Function_7_1E4F")

    Battle("BattleInfo_9E4", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E96")
    OP_90(0x0, 123300, -2590, -74250, 187)
    EventEnd(0x5)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_1EC7")

    label("loc_1E96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA9")
    Jump("loc_1EC7")

    label("loc_1EA9")

    ModifyEventFlags(0, 3, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetScenarioFlags(0x1B8, 2)
    EventEnd(0x5)

    label("loc_1EC7")

    Return()

    # Function_7_1E4F end

    def Function_8_1EC8(): pass

    label("Function_8_1EC8")

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

    def lambda_1FD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1FD8)

    def lambda_1FE9():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FE9)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2040():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2040)

    def lambda_2051():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2051)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_20AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_20AE)

    def lambda_20BF():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_20BF)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2116():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2116)

    def lambda_2127():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2127)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_1EC8 end

    def Function_9_2148(): pass

    label("Function_9_2148")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_21A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_21A1)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_21EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_21EC)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2237)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2282():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2282)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9050", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2148 end

    def Function_10_22A1(): pass

    label("Function_10_22A1")

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

    def lambda_23B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_23B1)

    def lambda_23C2():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_23C2)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2419():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2419)

    def lambda_242A():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_242A)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2487():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2487)

    def lambda_2498():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2498)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_24EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_24EF)

    def lambda_2500():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2500)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_22A1 end

    def Function_11_2521(): pass

    label("Function_11_2521")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_257A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_257A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_25C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_25C5)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2610():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2610)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_265B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_265B)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9060", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2521 end

    def Function_12_267A(): pass

    label("Function_12_267A")

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

    def lambda_27A1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27A1)
    Sleep(50)

    def lambda_27B9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27B9)
    Sleep(50)

    def lambda_27D1():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27D1)
    Sleep(50)

    def lambda_27E9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27E9)
    Sleep(50)

    def lambda_2801():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_2801)
    Sleep(50)

    def lambda_2819():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_2819)
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
        "#00005F#5PWhat is this place...\x02",
    )

    CloseMessageWindow()

    def lambda_28DD():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28DD)
    Sleep(50)

    def lambda_28F5():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28F5)
    Sleep(50)

    def lambda_290D():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_290D)
    Sleep(50)

    def lambda_2925():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2925)
    Sleep(50)

    def lambda_293D():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_293D)
    Sleep(50)

    def lambda_2955():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_2955)
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

    def lambda_29EC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29EC)
    Sleep(50)

    def lambda_29FC():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29FC)
    Sleep(50)

    def lambda_2A0C():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A0C)
    Sleep(50)

    def lambda_2A1C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A1C)
    Sleep(50)

    def lambda_2A2C():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2A2C)
    Sleep(50)

    def lambda_2A3C():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2A3C)
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
            "#00301F#6PThe heck...? It seems\x01",
            "it's covered by something\x01",
            "like a barrier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PIt is probably a kind of\x01",
            "Magical Barrier, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PSetting aside the central part...\x01",
            "I wonder what those things on the\x01",
            "left and right sides of it are.\x02",
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
            "#3788V#40W#35AHuhu... Those are known\x01",
            "as Territories.\x07\x00\x02",
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
            "#00107F#5PBell...!? ...Bell, is\x01",
            "that you!?\x02",
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

    def lambda_2DCD():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DCD)
    Sleep(50)

    def lambda_2DDD():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2DDD)
    Sleep(50)

    def lambda_2DED():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DED)
    Sleep(50)

    def lambda_2DFD():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DFD)
    Sleep(50)

    def lambda_2E0D():
        TurnDirection(0xF4, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2E0D)
    Sleep(50)

    def lambda_2E1D():
        TurnDirection(0xF5, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2E1D)
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
            "#30WUhuhu... Of course, Elie.\x02\x03",
            "─Welcome to the Azure Tree.\x02\x03",
            "KeA will be glad that you have\x01",
            "come as well.\x02\x03",
            "No─ Huhu, rather, will she be sad,\x01",
            "perhaps?\x07\x00\x02",
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
        "#00101F#12P#NBell... You...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NPutting aside your\x01",
            "goals...\x02\x03",
            "#00001FIt seems you have no\x01",
            "intention of stopping us\x01",
            "at all, right?\x02",
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
            "#30WCorrect. This Sanctuary is KeA's very\x01",
            "own interior...\x02\x03",
            "Her desires of wanting you to come and\x01",
            "not wanting you to come are reflected\x01",
            "here, just as they are in her mind.\x02\x03",
            "They appear in the form of the\x01",
            "guardians you see wandering around.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3184")
    OP_FC(0x6)
    Jump("loc_3187")

    label("loc_3184")

    OP_FC(0xC)

    label("loc_3187")


    ChrTalk(
        0x10A,
        "#00601F#13P#NSuch a structure is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3265")

    label("loc_31B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_320F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31DF")
    OP_FC(0x6)
    Jump("loc_31E2")

    label("loc_31DF")

    OP_FC(0xC)

    label("loc_31E2")


    ChrTalk(
        0x109,
        "#10111F#13P#NS-Such a structure...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3265")

    label("loc_320F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3265")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3239")
    OP_FC(0x6)
    Jump("loc_323C")

    label("loc_3239")

    OP_FC(0xC)

    label("loc_323C")


    ChrTalk(
        0x106,
        "#10712F#13P#NSuch a structure is...\x02",
    )

    CloseMessageWindow()

    label("loc_3265")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3292")
    OP_FC(0x6)
    Jump("loc_3295")

    label("loc_3292")

    OP_FC(0xC)

    label("loc_3295")


    ChrTalk(
        0x105,
        (
            "#10406F#13P#NSo it's because this place\x01",
            "is inside her mind that\x01",
            "there's so much space, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E9")

    label("loc_32FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_337D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3324")
    OP_FC(0x6)
    Jump("loc_3327")

    label("loc_3324")

    OP_FC(0xC)

    label("loc_3327")


    ChrTalk(
        0x106,
        (
            "#10706F#13P#NThere's this much space\x01",
            "because it's the inside\x01",
            "of her mind...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E9")

    label("loc_337D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33A7")
    OP_FC(0x6)
    Jump("loc_33AA")

    label("loc_33A7")

    OP_FC(0xC)

    label("loc_33AA")


    ChrTalk(
        0x109,
        (
            "#10108F#13P#NThis is a space at the\x01",
            "core of KeA's mind...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E9")

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
            "#30WHuhu. However, this is\x01",
            "the last banquet.\x02\x03",
            "For much more fun, I\x01",
            "prepared different\x01",
            "grounds.\x02\x03",
            "And those─ They are\x01",
            "their "gates".\x07\x00\x02",
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

    def lambda_34F0():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_34F0)
    Sleep(50)

    def lambda_3500():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3500)
    Sleep(50)

    def lambda_3510():
        OP_93(0xF4, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3510)
    Sleep(50)

    def lambda_3520():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3520)
    Sleep(50)

    def lambda_3530():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3530)
    Sleep(50)

    def lambda_3540():
        OP_93(0xF5, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3540)
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

    def lambda_359C():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_359C)
    Sleep(50)

    def lambda_35AC():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35AC)
    Sleep(50)

    def lambda_35BC():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_35BC)
    Sleep(50)

    def lambda_35CC():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_35CC)
    Sleep(50)

    def lambda_35DC():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_35DC)
    Sleep(50)

    def lambda_35EC():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_35EC)
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

    def lambda_364B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_364B)
    Sleep(50)

    def lambda_365B():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_365B)
    Sleep(50)

    def lambda_366B():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_366B)
    Sleep(50)

    def lambda_367B():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_367B)
    Sleep(50)

    def lambda_368B():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_368B)
    Sleep(50)

    def lambda_369B():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_369B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00201F#6P#NDifferent grounds...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NHey now... Can't you\x01",
            "stop playin' yer games?\x02",
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
            "#30WUhuhu, it's quite simple.\x02\x03",
            "Just as this Sanctuary\x01",
            "reacts to KeA's inner\x01",
            "self...\x02\x03",
            "Those gates are linked to\x01",
            "Territories that react to\x01",
            "other people's inner selves.\x07\x00\x02",
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
        "#00007F#6P#NOther people...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00101F#12P#NC-Could you mean...\x02",
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
            "#30WHuhu. If you have people with a\x01",
            "connection to them...\x02\x03",
            "Well then everyone. My guidance\x01",
            "ends here. I will be waiting for\x01",
            "you at the main grounds.\x02\x03",
            "Provided you manage to reach them\x01",
            "safely and alive, that is.\x07\x00\x02",
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
        "#00106F#11P...Bell...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#5PReally, this goes beyond a simple\x01",
            "joke...\x02\x03",
            "#00008FHowever, setting aside the central\x01",
            "gate, it seems we can enter the\x01",
            "gates on the left and right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PThe problem is "who" is\x01",
            "beyond them...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00306F#5PWell for now, let's give them a\x01",
            "try.\x02\x03",
            "#00300FIt seems like we won't be able\x01",
            "to enter unless we have someone\x01",
            "related to the person inside.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CEF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CEF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D3D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D21")
    OP_FC(0x6)
    Jump("loc_3D24")

    label("loc_3D21")

    OP_FC(0xC)

    label("loc_3D24")


    ChrTalk(
        0x105,
        "#10408F#13PRight...\x02",
    )

    CloseMessageWindow()

    label("loc_3D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D82")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D67")
    OP_FC(0x6)
    Jump("loc_3D6A")

    label("loc_3D67")

    OP_FC(0xC)

    label("loc_3D6A")


    ChrTalk(
        0x106,
        "#10708F#13P...Yes.\x02",
    )

    CloseMessageWindow()

    label("loc_3D82")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DAC")
    OP_FC(0x6)
    Jump("loc_3DAF")

    label("loc_3DAC")

    OP_FC(0xC)

    label("loc_3DAF")


    ChrTalk(
        0x109,
        (
            "#10101F#13PIf we need to, it might\x01",
            "be best to return to the\x01",
            "Merkabah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E77")

    label("loc_3DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E77")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E29")
    OP_FC(0x6)
    Jump("loc_3E2C")

    label("loc_3E29")

    OP_FC(0xC)

    label("loc_3E2C")


    ChrTalk(
        0x10A,
        (
            "#00601F#13PIf we need to, it might\x01",
            "be best to return to the\x01",
            "Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E77")

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

    # Function_12_267A end

    def Function_13_3EC8(): pass

    label("Function_13_3EC8")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x1F4)

    def lambda_3ED8():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3ED8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x320)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x96)

    label("loc_3F13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2A")
    Sleep(50)
    Jump("loc_3F13")

    label("loc_3F2A")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x96)
    Sleep(300)
    Sleep(50)

    def lambda_3F40():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F40)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    Sleep(300)
    Return()

    # Function_13_3EC8 end

    def Function_14_3F71(): pass

    label("Function_14_3F71")

    Sleep(100)
    OP_93(0xFE, 0x4B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xC3, 0x1F4)
    Return()

    # Function_14_3F71 end

    def Function_15_3F86(): pass

    label("Function_15_3F86")

    Sleep(200)
    OP_93(0xFE, 0x11D, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xA5, 0x1F4)
    Return()

    # Function_15_3F86 end

    def Function_16_3F9B(): pass

    label("Function_16_3F9B")

    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_16_3F9B end

    def Function_17_3FB0(): pass

    label("Function_17_3FB0")

    Sleep(400)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x14A, 0x1F4)
    Return()

    # Function_17_3FB0 end

    def Function_18_3FC5(): pass

    label("Function_18_3FC5")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_18_3FC5 end

    def Function_19_3FDA(): pass

    label("Function_19_3FDA")

    Sleep(600)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_19_3FDA end

    def Function_20_3FEF(): pass

    label("Function_20_3FEF")

    Sleep(500)
    OP_93(0xFE, 0xC3, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x4B, 0x1F4)
    Return()

    # Function_20_3FEF end

    def Function_21_4004(): pass

    label("Function_21_4004")

    Sleep(200)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_21_4004 end

    def Function_22_4023(): pass

    label("Function_22_4023")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_22_4023 end

    def Function_23_4038(): pass

    label("Function_23_4038")

    Sleep(400)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_4038 end

    def Function_24_404D(): pass

    label("Function_24_404D")

    Sleep(650)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(450)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_24_404D end

    def Function_25_4062(): pass

    label("Function_25_4062")

    Sleep(550)
    OP_93(0xFE, 0x6E, 0x1F4)
    Sleep(550)
    OP_93(0xFE, 0xE6, 0x1F4)
    Return()

    # Function_25_4062 end

    def Function_26_4077(): pass

    label("Function_26_4077")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_408F")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_408F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40A3")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_40A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40B7")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_40B7")

    Return()

    # Function_26_4077 end

    def Function_27_40B8(): pass

    label("Function_27_40B8")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40D0")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_40D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40E4")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_40E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40F8")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_40F8")

    Return()

    # Function_27_40B8 end

    def Function_28_40F9(): pass

    label("Function_28_40F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4158")
    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4126")
    OP_CF(0x1, 0xF5, 0x4)
    Jump("loc_4153")

    label("loc_4126")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_413F")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_4153")

    label("loc_413F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4153")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4153")

    Jump("loc_41C6")

    label("loc_4158")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_419E")
    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4185")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_4199")

    label("loc_4185")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4199")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4199")

    Jump("loc_41C6")

    label("loc_419E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41C6")
    OP_CF(0x1, 0xF4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41C6")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_41C6")

    Return()

    # Function_28_40F9 end

    def Function_29_41C7(): pass

    label("Function_29_41C7")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4223")
    Call(0, 26)
    Jump("loc_4226")

    label("loc_4223")

    Call(0, 28)

    label("loc_4226")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D3")
    BeginChrThread(0x101, 0, 0, 30)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4368")

    ChrTalk(
        0x101,
        (
            "#00006F#5P...It's no use, it\x01",
            "looks.\x02\x03",
            "#00001FEven if we were to\x01",
            "strike it, it wouldn't\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PIf only we could figure\x01",
            "out who's inside...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D3")

    label("loc_4368")


    ChrTalk(
        0x101,
        (
            "#00003F#5P...It's the same as the\x01",
            "gate on the right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PI wonder... Who could be\x01",
            "inside?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D3")

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
            "#3577V#50W#40AHeh heh... Gwahaha...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3578V#50W#50A...I... My power is the\x01",
            "greatest...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3579V#50W#50AYeah, that's right...\x01",
            "Even greater than that\x01",
            "bastard's!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B74")

    ChrTalk(
        0x105,
        (
            "#10408F#12P...Honestly. Why does he\x01",
            "have to be particular\x01",
            "about a blockhead like me?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_463C():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_463C)
    Sleep(50)

    def lambda_464C():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_464C)
    Sleep(50)

    def lambda_465C():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_465C)
    Sleep(50)

    def lambda_466C():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_466C)
    Sleep(50)

    def lambda_467C():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_467C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        "#00008F#5PWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PMove aside, Lloyd.\x02\x03",
            "#10401FIt looks like "he" wants\x01",
            "to settle things with\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...I understand.\x02",
    )

    CloseMessageWindow()

    def lambda_4735():
        OP_96(0xFE, 0xFFFFD508, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4735)

    def lambda_474F():

        label("loc_474F")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_474F")

    QueueWorkItem2(0x101, 2, lambda_474F)

    def lambda_4761():

        label("loc_4761")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4761")

    QueueWorkItem2(0x102, 2, lambda_4761)

    def lambda_4773():

        label("loc_4773")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4773")

    QueueWorkItem2(0x103, 2, lambda_4773)

    def lambda_4785():

        label("loc_4785")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4785")

    QueueWorkItem2(0x104, 2, lambda_4785)

    def lambda_4797():

        label("loc_4797")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4797")

    QueueWorkItem2(0xF5, 2, lambda_4797)
    Sleep(300)
    OP_68(-12230, 26000, -127620, 2000)
    MoveCamera(358, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_47DA():
        OP_95(0xFE, -12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47DA)
    Sleep(150)

    def lambda_47F7():
        OP_9B(0x1, 0xFE, 0x2D, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47F7)
    Sleep(500)

    def lambda_480F():
        OP_96(0xFE, 0xFFFFD602, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_480F)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48FB")

    ChrTalk(
        0x102,
        (
            "#00105F#12PThe barrier\x01",
            "disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PNow we can go to that\x01",
            "Territory's grounds,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_4950")

    label("loc_48FB")


    ChrTalk(
        0x103,
        "#00201F#6P#NIt vanished...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#11PNow we can go to the\x01",
            "Territory...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4950")

    Sleep(200)
    OP_93(0x105, 0x87, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10406F#5PYeah... However, it\x01",
            "won't end in a game of\x01",
            "fun this time.\x02\x03",
            "#10400FShall we make sure we're\x01",
            "ready to face him?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AEE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A3F")

    ChrTalk(
        0x109,
        (
            "#10108F#12PIt might also do us some\x01",
            "good to return to the\x01",
            "Merkabah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE9")

    label("loc_4A3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A95")

    ChrTalk(
        0x10A,
        (
            "#00603F#12PIt might even be good to\x01",
            "return to the Merkabah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE9")

    label("loc_4A95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AE9")

    ChrTalk(
        0x106,
        (
            "#10708F#12PIt might also do us good\x01",
            "to return to the\x01",
            "Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AE9")

    Jump("loc_4B67")

    label("loc_4AEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B18")

    ChrTalk(
        0x109,
        "#10101F#12PYes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B67")

    label("loc_4B18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B42")

    ChrTalk(
        0x10A,
        "#00601F#12PMmm.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B67")

    label("loc_4B42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B67")

    ChrTalk(
        0x106,
        "#10701F#12PYes!\x02",
    )

    CloseMessageWindow()

    label("loc_4B67")

    SetScenarioFlags(0x1AA, 1)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_4CD0")

    label("loc_4B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_END)), "loc_4C48")

    ChrTalk(
        0x103,
        (
            "#00205F#12PThe barrier went back to\x01",
            "how it was...\x02\x03",
            "#00203FIt looks like we can't\x01",
            "enter this Territory\x01",
            "without Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah... Let's return to\x01",
            "the Merkabah and bring\x01",
            "Wazy with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD0")

    label("loc_4C48")


    ChrTalk(
        0x103,
        (
            "#00208F#12P...It is extremely clear\x01",
            ""who" is inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah... Let's return to\x01",
            "the Merkabah and bring\x01",
            ""him" with us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD0")

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

    # Function_29_41C7 end

    def Function_30_4D0F(): pass

    label("Function_30_4D0F")

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

    # Function_30_4D0F end

    def Function_31_4D95(): pass

    label("Function_31_4D95")

    Sleep(800)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_4D95 end

    def Function_32_4DA0(): pass

    label("Function_32_4DA0")

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

    # Function_32_4DA0 end

    def Function_33_4DE1(): pass

    label("Function_33_4DE1")

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

    # Function_33_4DE1 end

    def Function_34_4E15(): pass

    label("Function_34_4E15")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E71")
    Call(0, 27)
    Jump("loc_4E74")

    label("loc_4E71")

    Call(0, 28)

    label("loc_4E74")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500B")
    BeginChrThread(0x101, 0, 0, 35)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA4")

    ChrTalk(
        0x101,
        (
            "#00006F#11P...It's no use.\x02\x03",
            "Even if we hit it, it\x01",
            "wouldn't break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PIf only we could at\x01",
            "least figure out who is\x01",
            "inside...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_500B")

    label("loc_4FA4")


    ChrTalk(
        0x101,
        (
            "#00003F#11P...Same thing with the\x01",
            "left gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PI wonder... Who could be\x01",
            "inside here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500B")

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
            "#3961V#40W#40AUhuhu... Ahahahaha...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3962V#40W#38ANot yet...? Isn't she\x01",
            "here yet...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3963V#40W#38AI'm so excited, I can't\x01",
            "wait any longer!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_586C")

    ChrTalk(
        0x106,
        "#10708F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5POh boy... It's her.\x02\x03",
            "#00301FAnd also, the one she's\x01",
            "waitin' for ain't me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_527C():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_527C)
    Sleep(50)

    def lambda_528C():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_528C)
    Sleep(50)

    def lambda_529C():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_529C)
    Sleep(50)

    def lambda_52AC():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_52AC)
    Sleep(50)

    def lambda_52BC():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_52BC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x101,
        (
            "#00003F#11P...Say, Rixia.\x02\x03",
            "#00001FIf you want, you could\x01",
            "leave her to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#6P─No.\x02\x03",
            "#10708FIn a way, both she and I\x01",
            "are the product of our\x01",
            "circumstances.\x02\x03",
            "I need to find the path\x01",
            "I'll take going forward\x01",
            "as well...\x02\x03",
            "#10701FShe and I must confront\x01",
            "each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P...Understood.\x02",
    )

    CloseMessageWindow()

    def lambda_5414():
        OP_96(0xFE, 0x2AF8, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5414)

    def lambda_542E():

        label("loc_542E")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_542E")

    QueueWorkItem2(0x101, 2, lambda_542E)

    def lambda_5440():

        label("loc_5440")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5440")

    QueueWorkItem2(0x102, 2, lambda_5440)

    def lambda_5452():

        label("loc_5452")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5452")

    QueueWorkItem2(0x103, 2, lambda_5452)

    def lambda_5464():

        label("loc_5464")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5464")

    QueueWorkItem2(0x104, 2, lambda_5464)

    def lambda_5476():

        label("loc_5476")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_5476")

    QueueWorkItem2(0xF5, 2, lambda_5476)
    Sleep(300)
    OP_68(12230, 26000, -127620, 2000)
    MoveCamera(2, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_54B9():
        OP_95(0xFE, 12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_54B9)
    Sleep(150)

    def lambda_54D6():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54D6)
    WaitChrThread(0x106, 1)

    def lambda_54EF():
        OP_96(0xFE, 0x29FE, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54EF)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55D9")

    ChrTalk(
        0x102,
        (
            "#00105F#6PThe barrier\x01",
            "disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PNow we can go to that\x01",
            "Territory's grounds,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_562D")

    label("loc_55D9")


    ChrTalk(
        0x103,
        "#00201F#6P#NIt vanished...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#5PNow we can go to the\x01",
            "Territory...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562D")

    Sleep(200)
    OP_93(0x106, 0xE1, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#10703F...#11PAn opponent is an\x01",
            "opponent.\x02\x03",
            "#10710FLet's prepare ourselves\x01",
            "accordingly, so as not to\x01",
            "be potentially overwhelmed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57DC")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5723")

    ChrTalk(
        0x109,
        (
            "#10106F#6PIt might also do us some\x01",
            "good to return to the\x01",
            "Merkabah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57D7")

    label("loc_5723")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5778")

    ChrTalk(
        0x10A,
        (
            "#00603F#6PIt might even be good to\x01",
            "return to the Merkabah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57D7")

    label("loc_5778")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57D7")

    ChrTalk(
        0x105,
        (
            "#10404F#6PIt might also be helpful\x01",
            "to return to the\x01",
            "Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D7")

    Jump("loc_585F")

    label("loc_57DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5807")

    ChrTalk(
        0x109,
        "#10101F#6PRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_585F")

    label("loc_5807")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5832")

    ChrTalk(
        0x10A,
        "#00601F#6PRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_585F")

    label("loc_5832")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_585F")

    ChrTalk(
        0x105,
        "#10402F#6PYou're right.\x02",
    )

    CloseMessageWindow()

    label("loc_585F")

    SetScenarioFlags(0x1AA, 2)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_5A2F")

    label("loc_586C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_END)), "loc_5949")

    ChrTalk(
        0x104,
        (
            "#00305F#5PThe barrier went back to\x01",
            "its original form...\x02\x03",
            "#00303FIt looks like we can't\x01",
            "enter this Territory\x01",
            "without Rixia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah... Let's return to\x01",
            "the Merkabah and bring\x01",
            "Rixia with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A2F")

    label("loc_5949")


    ChrTalk(
        0x104,
        (
            "#00306F#5POh boy... It's her.\x02\x03",
            "#00301FAnd also, the one she's\x01",
            "waitin' for ain't me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah...\x02\x03",
            "#00008F(We need to return to\x01",
            "the Merkabah and bring\x01",
            ""her" with us, but...)\x02\x03",
            "(Is it really alright to\x01",
            "have her come?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A2F")

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

    # Function_34_4E15 end

    def Function_35_5A6E(): pass

    label("Function_35_5A6E")

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

    # Function_35_5A6E end

    def Function_36_5AF4(): pass

    label("Function_36_5AF4")

    Sleep(800)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_36_5AF4 end

    def Function_37_5AFF(): pass

    label("Function_37_5AFF")

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

    # Function_37_5AFF end

    def Function_38_5B40(): pass

    label("Function_38_5B40")

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

    # Function_38_5B40 end

    def Function_39_5B74(): pass

    label("Function_39_5B74")

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

    def lambda_5D0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D0A)

    def lambda_5D1B():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D1B)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5D72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5D72)

    def lambda_5D83():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D83)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5DE0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5DE0)

    def lambda_5DF1():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DF1)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5E48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E48)

    def lambda_5E59():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E59)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5EB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_5EB6)

    def lambda_5EC7():
        OP_95(0xFE, -12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_5EC7)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5F1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_5F1E)

    def lambda_5F2F():
        OP_95(0xFE, -11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_5F2F)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_END)), "loc_621C")
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

    def lambda_6023():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6023)
    Sleep(50)

    def lambda_6033():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6033)
    Sleep(50)

    def lambda_6043():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6043)
    Sleep(50)

    def lambda_6053():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6053)
    Sleep(50)

    def lambda_6063():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6063)
    Sleep(50)

    def lambda_6073():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6073)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F#6P#NThe magical barrier!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NIt appears the two\x01",
            "Territories have been\x01",
            "released.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHehe, now we're finally\x01",
            "able to proceed forward.\x02\x03",
            "#10408F...Before that, I'd like\x01",
            "to go back to the airship\x01",
            "for a bit and rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PRight... We have to report in to everyone\x01",
            "as well, so it seems like a good idea to\x01",
            "go back to the Merkabah for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64A8")

    label("loc_621C")

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

    def lambda_62C4():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62C4)
    Sleep(50)

    def lambda_62D4():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_62D4)
    Sleep(50)

    def lambda_62E4():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_62E4)
    Sleep(50)

    def lambda_62F4():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_62F4)
    Sleep(50)

    def lambda_6304():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6304)
    Sleep(50)

    def lambda_6314():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6314)
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
            "#00005F#6PThe central gate's\x01",
            "magical barrier... has\x01",
            "weakened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PIt's probably because we\x01",
            "released Wald's Territory.\x02\x03",
            "#00201FI think this Sanctuary\x01",
            "might be connected with\x01",
            "each person's Territories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P#NThen that means, if we\x01",
            "can release the other\x01",
            "Territory, then...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10400F#6PThe magical barrier\x01",
            "would probably vanish\x01",
            "completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64A8")

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

    # Function_39_5B74 end

    def Function_40_64E5(): pass

    label("Function_40_64E5")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C6")
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6683():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6683)

    def lambda_6694():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6694)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_66EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66EB)

    def lambda_66FC():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66FC)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6759():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6759)

    def lambda_676A():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_676A)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_67C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_67C1)

    def lambda_67D2():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67D2)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_682F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_682F)

    def lambda_6840():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_6840)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6897():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6897)

    def lambda_68A8():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_68A8)
    WaitChrThread(0xF5, 1)
    Jump("loc_6B49")

    label("loc_68C6")

    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_690B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_690B)

    def lambda_691C():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_691C)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6973():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6973)

    def lambda_6984():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6984)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_69E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69E1)

    def lambda_69F2():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_69F2)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6A49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6A49)

    def lambda_6A5A():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A5A)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6AB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AB7)

    def lambda_6AC8():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AC8)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6B1F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6B1F)

    def lambda_6B30():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_6B30)
    WaitChrThread(0xF5, 1)

    label("loc_6B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_6DE7")
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

    def lambda_6C24():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C24)
    Sleep(50)

    def lambda_6C34():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6C34)
    Sleep(50)

    def lambda_6C44():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6C44)
    Sleep(50)

    def lambda_6C54():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6C54)
    Sleep(50)

    def lambda_6C64():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6C64)
    Sleep(50)

    def lambda_6C74():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6C74)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F#12PThe magical barrier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#NIt appears the two\x01",
            "Territories have been\x01",
            "released.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10702F#12PNow we're finally able\x01",
            "to move forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah. But as expected, it's been\x01",
            "a hard fight...\x02\x03",
            "#00000FWe have to report in to everyone\x01",
            "too, so I think it's best to\x01",
            "return to the Merkabah for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707E")

    label("loc_6DE7")

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

    def lambda_6E8F():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E8F)
    Sleep(50)

    def lambda_6E9F():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6E9F)
    Sleep(50)

    def lambda_6EAF():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6EAF)
    Sleep(50)

    def lambda_6EBF():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6EBF)
    Sleep(50)

    def lambda_6ECF():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6ECF)
    Sleep(50)

    def lambda_6EDF():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6EDF)
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
            "#00005F#12PThe central gate's\x01",
            "magical barrier... has\x01",
            "weakened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P#NIt's probably because we\x01",
            "released Shirley's\x01",
            "Territory.\x02\x03",
            "#00201FI think this Sanctuary\x01",
            "might be connected with\x01",
            "each person's Territories.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#12PThen that means, if we\x01",
            "can release the other\x01",
            "Territory, then...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702F#12PThat magical barrier\x01",
            "would probably disappear\x01",
            "completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707E")

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

    # Function_40_64E5 end

    def Function_41_70BB(): pass

    label("Function_41_70BB")

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

    # Function_41_70BB end

    def Function_42_719B(): pass

    label("Function_42_719B")

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

    # Function_42_719B end

    SaveToFile()

Try(main)
