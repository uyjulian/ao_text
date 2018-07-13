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

    Sepith("Sepith_7348", 7,   7,   7,   7,   11,  11,  11)
    Sepith("Sepith_7360", 9,   9,   9,   9,   10,  10,  10)
    Sepith("Sepith_7340", 13,  13,  13,  13,  4,   4,   4)
    Sepith("Sepith_7368", 11,  23,  0,   15,  0,   0,   19)
    Sepith("Sepith_7358", 0,   0,   0,   0,   15,  38,  15)

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
        "BattleInfo_6AC", 0x0000, 100, 6, 60, 10, 1, 40, 0, "bm9010", "Sepith_7348", 40, 30, 20, 10,
        (
            ("ms80900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
            ("ms80900.dat", "ms80900.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_510"),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_7360", 40, 30, 20, 10,
        (
            ("ms79900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms79900.dat", "ms79900.dat", "ms79900.dat", "ms79900.dat", 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
        )
    )

    BattleInfo(
        "BattleInfo_610", 0x0000, 100, 6, 60, 10, 1, 35, 0, "bm9010", "Sepith_7340", 50, 30, 20, 0,
        (
            ("ms85300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            ("ms85300.dat", "ms80900.dat", "ms80900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 100, 6, 60, 4, 1, 30, 0, "bm9010", "Sepith_7368", 100, 0, 0, 0,
        (
            ("ms85200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5D0", "ed7452", "ed7453", "ATBonus_520"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0010, 100, 6, 180, 10, 1, 5, 0, "bm9010", "Sepith_7358", 50, 35, 15, 0,
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
        "Function_5_1AE4",         # 05, 5
        "Function_6_1C36",         # 06, 6
        "Function_7_1E52",         # 07, 7
        "Function_8_1ECB",         # 08, 8
        "Function_9_214B",         # 09, 9
        "Function_10_22A4",        # 0A, 10
        "Function_11_2524",        # 0B, 11
        "Function_12_267D",        # 0C, 12
        "Function_13_3ED8",        # 0D, 13
        "Function_14_3F81",        # 0E, 14
        "Function_15_3F96",        # 0F, 15
        "Function_16_3FAB",        # 10, 16
        "Function_17_3FC0",        # 11, 17
        "Function_18_3FD5",        # 12, 18
        "Function_19_3FEA",        # 13, 19
        "Function_20_3FFF",        # 14, 20
        "Function_21_4014",        # 15, 21
        "Function_22_4033",        # 16, 22
        "Function_23_4048",        # 17, 23
        "Function_24_405D",        # 18, 24
        "Function_25_4072",        # 19, 25
        "Function_26_4087",        # 1A, 26
        "Function_27_40C8",        # 1B, 27
        "Function_28_4109",        # 1C, 28
        "Function_29_41D7",        # 1D, 29
        "Function_30_4D56",        # 1E, 30
        "Function_31_4DDC",        # 1F, 31
        "Function_32_4DE7",        # 20, 32
        "Function_33_4E28",        # 21, 33
        "Function_34_4E5C",        # 22, 34
        "Function_35_5AFB",        # 23, 35
        "Function_36_5B81",        # 24, 36
        "Function_37_5B8C",        # 25, 37
        "Function_38_5BCD",        # 26, 38
        "Function_39_5C01",        # 27, 39
        "Function_40_6571",        # 28, 40
        "Function_41_7158",        # 29, 41
        "Function_42_7238",        # 2A, 42
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A94")

    Jump("loc_1AD8")

    label("loc_1A99")

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

    label("loc_1AD8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_18C8 end

    def Function_5_1AE4(): pass

    label("Function_5_1AE4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE0")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1B69")
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
    Jump("loc_1BDB")

    label("loc_1B69")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
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

    label("loc_1BDB")

    Jump("loc_1C2A")

    label("loc_1BE0")

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

    label("loc_1C2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1AE4 end

    def Function_6_1C36(): pass

    label("Function_6_1C36")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E07")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D39")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1C93():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C93)

    def lambda_1CAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CAD)
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
        (0, "loc_1D1A"),
        (2, "loc_1D29"),
        (1, "loc_1D36"),
        (SWITCH_DEFAULT, "loc_1D39"),
    )


    label("loc_1D1A")

    SetScenarioFlags(0x218, 5)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1D39")

    label("loc_1D29")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1D36")

    OP_B9(0x0)
    Return()

    label("loc_1D39")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7F, 1)"), scpexpr(EXPR_END)), "loc_1D92")
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
    Jump("loc_1E02")

    label("loc_1D92")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
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

    label("loc_1E02")

    Jump("loc_1E46")

    label("loc_1E07")

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

    label("loc_1E46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C36 end

    def Function_7_1E52(): pass

    label("Function_7_1E52")

    Battle("BattleInfo_9E4", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E99")
    OP_90(0x0, 123300, -2590, -74250, 187)
    EventEnd(0x5)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_1ECA")

    label("loc_1E99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAC")
    Jump("loc_1ECA")

    label("loc_1EAC")

    ModifyEventFlags(0, 3, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetScenarioFlags(0x1B8, 2)
    EventEnd(0x5)

    label("loc_1ECA")

    Return()

    # Function_7_1E52 end

    def Function_8_1ECB(): pass

    label("Function_8_1ECB")

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

    def lambda_1FDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1FDB)

    def lambda_1FEC():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1FEC)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2043():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2043)

    def lambda_2054():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2054)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_20B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_20B1)

    def lambda_20C2():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_20C2)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_2119():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2119)

    def lambda_212A():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_212A)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_1ECB end

    def Function_9_214B(): pass

    label("Function_9_214B")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_21A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_21A4)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_21EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_21EF)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_223A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_223A)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2285():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2285)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9050", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_214B end

    def Function_10_22A4(): pass

    label("Function_10_22A4")

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

    def lambda_23B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_23B4)

    def lambda_23C5():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_23C5)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_241C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_241C)

    def lambda_242D():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_242D)
    Sleep(500)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_248A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_248A)

    def lambda_249B():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_249B)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_24F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_24F2)

    def lambda_2503():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2503)
    WaitChrThread(0x3, 1)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_22A4 end

    def Function_11_2524(): pass

    label("Function_11_2524")

    EventBegin(0x0)
    OP_E2(0x3)
    LoadEffect(0x1, "event\\evwarp.eff")
    Sound(936, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_257D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_257D)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_25C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_25C8)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2613)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_265E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_265E)
    StopSound(112, 1000, 50)
    Sleep(1000)
    NewScene("m9060", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2524 end

    def Function_12_267D(): pass

    label("Function_12_267D")

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

    def lambda_27A4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27A4)
    Sleep(50)

    def lambda_27BC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_27BC)
    Sleep(50)

    def lambda_27D4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27D4)
    Sleep(50)

    def lambda_27EC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27EC)
    Sleep(50)

    def lambda_2804():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_2804)
    Sleep(50)

    def lambda_281C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_281C)
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

    def lambda_28E0():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28E0)
    Sleep(50)

    def lambda_28F8():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28F8)
    Sleep(50)

    def lambda_2910():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2910)
    Sleep(50)

    def lambda_2928():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2928)
    Sleep(50)

    def lambda_2940():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_2940)
    Sleep(50)

    def lambda_2958():
        OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_2958)
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

    def lambda_29EF():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_29EF)
    Sleep(50)

    def lambda_29FF():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_29FF)
    Sleep(50)

    def lambda_2A0F():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A0F)
    Sleep(50)

    def lambda_2A1F():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A1F)
    Sleep(50)

    def lambda_2A2F():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2A2F)
    Sleep(50)

    def lambda_2A3F():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2A3F)
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
            "#00301F#6PThe heck...?\x01",
            "It seems it's covered by\x01",
            "something like a barrier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PIt is probably a kind of\x01",
            ""magical barrier", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PSetting aside the central part...\x01",
            "I wonder what're those at the left and right sides?\x02",
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
            "#3788V#40W#35AUh uh...\x01",
            "Those are known as "territories".\x07\x00\x02",
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
            "#00107F#5PBell...!?\x01",
            "...Bell, is that you!?\x02",
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

    def lambda_2DC7():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DC7)
    Sleep(50)

    def lambda_2DD7():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2DD7)
    Sleep(50)

    def lambda_2DE7():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DE7)
    Sleep(50)

    def lambda_2DF7():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DF7)
    Sleep(50)

    def lambda_2E07():
        TurnDirection(0xF4, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2E07)
    Sleep(50)

    def lambda_2E17():
        TurnDirection(0xF5, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2E17)
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
            "#30WUhuhu...\x01",
            "Of course, Elie.\x02\x03",
            "──Welcome to the "Tree of Azure".\x02\x03",
            "Miss KeA too will be\x01",
            "glad that you have come.\x02\x03",
            "No──uh uh.\x01",
            "Rather, she will be sad, perhaps?\x07\x00\x02",
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
        "#00101F#12P#NBell...you...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#NPutting aside your aims...\x02\x03",
            "#00001FIt seems you don't have any\x01",
            "intention to stop us at all, right?\x02",
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
            "#30WYes, this "Sanctuary" is Miss\x01",
            "KeA's very own interior...\x02\x03",
            "The expression of her mind wanting\x01",
            "you to come, and not wanting you\x01",
            "to come, is reflected here like that.\x02\x03",
            "That appears in the form of\x01",
            "guardians loitering around.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_317A")
    OP_FC(0x6)
    Jump("loc_317D")

    label("loc_317A")

    OP_FC(0xC)

    label("loc_317D")


    ChrTalk(
        0x10A,
        "#00601F#13P#NSuch a structure...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_31A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3202")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D2")
    OP_FC(0x6)
    Jump("loc_31D5")

    label("loc_31D2")

    OP_FC(0xC)

    label("loc_31D5")


    ChrTalk(
        0x109,
        "#10111F#13P#NS-Such a structure...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3258")

    label("loc_3202")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3258")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_322C")
    OP_FC(0x6)
    Jump("loc_322F")

    label("loc_322C")

    OP_FC(0xC)

    label("loc_322F")


    ChrTalk(
        0x106,
        "#10712F#13P#NSuch a structure is...\x02",
    )

    CloseMessageWindow()

    label("loc_3258")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3285")
    OP_FC(0x6)
    Jump("loc_3288")

    label("loc_3285")

    OP_FC(0xC)

    label("loc_3288")


    ChrTalk(
        0x105,
        (
            "#10406F#13P#NSo it's because it's her mental interior\x01",
            "that there's so much space, eh...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_32EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3363")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3315")
    OP_FC(0x6)
    Jump("loc_3318")

    label("loc_3315")

    OP_FC(0xC)

    label("loc_3318")


    ChrTalk(
        0x106,
        (
            "#10706F#13P#NBeing her mental inside,\x01",
            "there's this much space...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3363")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_338D")
    OP_FC(0x6)
    Jump("loc_3390")

    label("loc_338D")

    OP_FC(0xC)

    label("loc_3390")


    ChrTalk(
        0x109,
        (
            "#10108F#13P#NThis is KeA's space at\x01",
            "the core of her mind...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D1")

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
            "#30WUh uh, however, this is the last banquet.\x02\x03",
            "To have much more fun, I\x01",
            "prepared different grounds.\x02\x03",
            "Those are── their "gates".\x07\x00\x02",
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

    def lambda_34D6():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_34D6)
    Sleep(50)

    def lambda_34E6():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_34E6)
    Sleep(50)

    def lambda_34F6():
        OP_93(0xF4, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_34F6)
    Sleep(50)

    def lambda_3506():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3506)
    Sleep(50)

    def lambda_3516():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3516)
    Sleep(50)

    def lambda_3526():
        OP_93(0xF5, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3526)
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

    def lambda_3582():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3582)
    Sleep(50)

    def lambda_3592():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3592)
    Sleep(50)

    def lambda_35A2():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_35A2)
    Sleep(50)

    def lambda_35B2():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_35B2)
    Sleep(50)

    def lambda_35C2():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_35C2)
    Sleep(50)

    def lambda_35D2():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_35D2)
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

    def lambda_3631():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3631)
    Sleep(50)

    def lambda_3641():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3641)
    Sleep(50)

    def lambda_3651():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3651)
    Sleep(50)

    def lambda_3661():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3661)
    Sleep(50)

    def lambda_3671():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3671)
    Sleep(50)

    def lambda_3681():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3681)
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
            "#00306F#6P#NHey now...can't you\x01",
            "stop puttin' on airs?\x02",
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
            "#30WUhuhu, it is something simple.\x02\x03",
            "Like this "sanctuary" is reacting\x01",
            "to Miss KeA's interior...\x02\x03",
            "Those gates are linked to\x01",
            ""territories" that reacted\x01",
            "to other people's interiors.\x07\x00\x02",
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
            "#30WUh uh, if you have people\x01",
            "with a connection to them...\x02\x03",
            "You will be granted access\x01",
            "to the different grounds.\x02\x03",
            "Then── My guidance ends\x01",
            "here. I will be waiting for\x01",
            "you at the main grounds.\x02\x03",
            "Provided you manage to\x01",
            "reach it safely, alive.\x07\x00\x02",
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
            "#00003F#5PThis is really beyond a joke...\x02\x03",
            "#00008FHowever, leaving aside the central gate, it\x01",
            "seems we can enter those on the left and right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PThe problem is "who"\x01",
            "is further in there...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#00306F#5PWell, for now let's give it a try.\x02\x03",
            "#00300FIt seems if there isn't a guy related\x01",
            "to that, it's not possible to enter.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CE0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CE0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D12")
    OP_FC(0x6)
    Jump("loc_3D15")

    label("loc_3D12")

    OP_FC(0xC)

    label("loc_3D15")


    ChrTalk(
        0x105,
        "#10408F#13PRight...\x02",
    )

    CloseMessageWindow()

    label("loc_3D2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D73")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D58")
    OP_FC(0x6)
    Jump("loc_3D5B")

    label("loc_3D58")

    OP_FC(0xC)

    label("loc_3D5B")


    ChrTalk(
        0x106,
        "#10708F#13P...Yes.\x02",
    )

    CloseMessageWindow()

    label("loc_3D73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E00")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D9D")
    OP_FC(0x6)
    Jump("loc_3DA0")

    label("loc_3D9D")

    OP_FC(0xC)

    label("loc_3DA0")


    ChrTalk(
        0x109,
        (
            "#10101F#13PIf we need to, it should\x01",
            "be better to go back\x01",
            "temporarily to the Merkabah.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E87")

    label("loc_3E00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E2A")
    OP_FC(0x6)
    Jump("loc_3E2D")

    label("loc_3E2A")

    OP_FC(0xC)

    label("loc_3E2D")


    ChrTalk(
        0x10A,
        (
            "#00601F#13PIf we need to, it could\x01",
            "be better to go back\x01",
            "temporarily to the Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E87")

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

    # Function_12_267D end

    def Function_13_3ED8(): pass

    label("Function_13_3ED8")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x1F4)

    def lambda_3EE8():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EE8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x320)
    Sleep(300)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xA0, 0x96)

    label("loc_3F23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F3A")
    Sleep(50)
    Jump("loc_3F23")

    label("loc_3F3A")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x96)
    Sleep(300)
    Sleep(50)

    def lambda_3F50():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F50)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x40, 0x1F4)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    Sleep(300)
    Return()

    # Function_13_3ED8 end

    def Function_14_3F81(): pass

    label("Function_14_3F81")

    Sleep(100)
    OP_93(0xFE, 0x4B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0xC3, 0x1F4)
    Return()

    # Function_14_3F81 end

    def Function_15_3F96(): pass

    label("Function_15_3F96")

    Sleep(200)
    OP_93(0xFE, 0x11D, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xA5, 0x1F4)
    Return()

    # Function_15_3F96 end

    def Function_16_3FAB(): pass

    label("Function_16_3FAB")

    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_16_3FAB end

    def Function_17_3FC0(): pass

    label("Function_17_3FC0")

    Sleep(400)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x14A, 0x1F4)
    Return()

    # Function_17_3FC0 end

    def Function_18_3FD5(): pass

    label("Function_18_3FD5")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_18_3FD5 end

    def Function_19_3FEA(): pass

    label("Function_19_3FEA")

    Sleep(600)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(850)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_19_3FEA end

    def Function_20_3FFF(): pass

    label("Function_20_3FFF")

    Sleep(500)
    OP_93(0xFE, 0xC3, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x4B, 0x1F4)
    Return()

    # Function_20_3FFF end

    def Function_21_4014(): pass

    label("Function_21_4014")

    Sleep(200)
    OP_93(0xFE, 0xD2, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(600)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_21_4014 end

    def Function_22_4033(): pass

    label("Function_22_4033")

    Sleep(500)
    OP_93(0xFE, 0x1E, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0x96, 0x1F4)
    Return()

    # Function_22_4033 end

    def Function_23_4048(): pass

    label("Function_23_4048")

    Sleep(400)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(900)
    OP_93(0xFE, 0xD2, 0x1F4)
    Return()

    # Function_23_4048 end

    def Function_24_405D(): pass

    label("Function_24_405D")

    Sleep(650)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(450)
    OP_93(0xFE, 0x1E, 0x1F4)
    Return()

    # Function_24_405D end

    def Function_25_4072(): pass

    label("Function_25_4072")

    Sleep(550)
    OP_93(0xFE, 0x6E, 0x1F4)
    Sleep(550)
    OP_93(0xFE, 0xE6, 0x1F4)
    Return()

    # Function_25_4072 end

    def Function_26_4087(): pass

    label("Function_26_4087")

    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_409F")
    OP_CF(0x1, 0xF5, 0x5)

    label("loc_409F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40B3")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_40B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40C7")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_40C7")

    Return()

    # Function_26_4087 end

    def Function_27_40C8(): pass

    label("Function_27_40C8")

    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40E0")
    OP_CF(0x1, 0xF5, 0x4)

    label("loc_40E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40F4")
    OP_CF(0x1, 0xF5, 0x8)

    label("loc_40F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4108")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4108")

    Return()

    # Function_27_40C8 end

    def Function_28_4109(): pass

    label("Function_28_4109")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4168")
    OP_CF(0x1, 0xF4, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4136")
    OP_CF(0x1, 0xF5, 0x4)
    Jump("loc_4163")

    label("loc_4136")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_414F")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_4163")

    label("loc_414F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4163")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_4163")

    Jump("loc_41D6")

    label("loc_4168")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41AE")
    OP_CF(0x1, 0xF4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4195")
    OP_CF(0x1, 0xF5, 0x8)
    Jump("loc_41A9")

    label("loc_4195")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41A9")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_41A9")

    Jump("loc_41D6")

    label("loc_41AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41D6")
    OP_CF(0x1, 0xF4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41D6")
    OP_CF(0x1, 0xF5, 0x9)

    label("loc_41D6")

    Return()

    # Function_28_4109 end

    def Function_29_41D7(): pass

    label("Function_29_41D7")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4233")
    Call(0, 26)
    Jump("loc_4236")

    label("loc_4233")

    Call(0, 28)

    label("loc_4236")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F7")
    BeginChrThread(0x101, 0, 0, 30)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438C")

    ChrTalk(
        0x101,
        (
            "#00006F#5P...It's no use. \x02\x03",
            "#00001FIt looks like that even if we hit it,\x01",
            "it wouldn't break down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PIf only we could at least figure\x01",
            "out who is inside there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F7")

    label("loc_438C")


    ChrTalk(
        0x101,
        "#00003F#5P...It's the same with the right gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#12PI wonder...\x01",
            "Who could be inside here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F7")

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
            "#3577V#50W#40AEh eh eh...gwah ha ha...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3578V#50W#50A...I...\x01",
            "My power is the greatest...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3579V#50W#50AYeah, that's right...\x01",
            "Even greater than that bastard's...!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BB9")

    ChrTalk(
        0x105,
        (
            "#10408F#12P...Honestly.\x01",
            "Why does he have to be particular\x01",
            "about a blockhead like me?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_4666():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4666)
    Sleep(50)

    def lambda_4676():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4676)
    Sleep(50)

    def lambda_4686():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4686)
    Sleep(50)

    def lambda_4696():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4696)
    Sleep(50)

    def lambda_46A6():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_46A6)
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
            "#10401FIt looks like "he" desires\x01",
            "to settle things with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P...Understood.\x02",
    )

    CloseMessageWindow()

    def lambda_475F():
        OP_96(0xFE, 0xFFFFD508, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_475F)

    def lambda_4779():

        label("loc_4779")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_4779")

    QueueWorkItem2(0x101, 2, lambda_4779)

    def lambda_478B():

        label("loc_478B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_478B")

    QueueWorkItem2(0x102, 2, lambda_478B)

    def lambda_479D():

        label("loc_479D")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_479D")

    QueueWorkItem2(0x103, 2, lambda_479D)

    def lambda_47AF():

        label("loc_47AF")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_47AF")

    QueueWorkItem2(0x104, 2, lambda_47AF)

    def lambda_47C1():

        label("loc_47C1")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_47C1")

    QueueWorkItem2(0xF5, 2, lambda_47C1)
    Sleep(300)
    OP_68(-12230, 26000, -127620, 2000)
    MoveCamera(358, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_4804():
        OP_95(0xFE, -12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4804)
    Sleep(150)

    def lambda_4821():
        OP_9B(0x1, 0xFE, 0x2D, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4821)
    Sleep(500)

    def lambda_4839():
        OP_96(0xFE, 0xFFFFD602, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4839)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4926")

    ChrTalk(
        0x102,
        "#00105F#12PThe barrier disappeared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PNow we can go to that\x01",
            ""territory" grounds, huh...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_497D")

    label("loc_4926")


    ChrTalk(
        0x103,
        "#00201F#6P#NIt vanished...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#11PNow we can go to the "territory"...\x02",
    )

    CloseMessageWindow()

    label("loc_497D")

    Sleep(200)
    OP_93(0x105, 0x87, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10406F#5PYeah...however, just this time it\x01",
            "won't end in a game of fun.\x02\x03",
            "#10400FLet's face him well prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A67")

    ChrTalk(
        0x109,
        (
            "#10108F#12PIt could also be good to go back\x01",
            "to the Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B29")

    label("loc_4A67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AC9")

    ChrTalk(
        0x10A,
        (
            "#00603F#12PIt could even be good to return\x01",
            "to the Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B29")

    label("loc_4AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B29")

    ChrTalk(
        0x106,
        (
            "#10708F#12PIt could also do us good to return\x01",
            "to the Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B29")

    Jump("loc_4BAC")

    label("loc_4B2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B5B")

    ChrTalk(
        0x109,
        "#10101F#12PYes...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BAC")

    label("loc_4B5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B84")

    ChrTalk(
        0x10A,
        "#00601F#12PHm.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BAC")

    label("loc_4B84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BAC")

    ChrTalk(
        0x106,
        "#10701F#12PYes...!\x02",
    )

    CloseMessageWindow()

    label("loc_4BAC")

    SetScenarioFlags(0x1AA, 1)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_4D17")

    label("loc_4BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_END)), "loc_4C92")

    ChrTalk(
        0x103,
        (
            "#00205F#12PThe barrier went back to how it was...\x02\x03",
            "#00203FIt looks like without Mr. Wazy\x01",
            "we can't enter this "territory".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PYeah...let's return to the Merkabah\x01",
            "and bring Wazy with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D17")

    label("loc_4C92")


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
            "#00006F#11PYeah...let's return to the Merkabah\x01",
            "and bring him with us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D17")

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

    # Function_29_41D7 end

    def Function_30_4D56(): pass

    label("Function_30_4D56")

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

    # Function_30_4D56 end

    def Function_31_4DDC(): pass

    label("Function_31_4DDC")

    Sleep(800)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_4DDC end

    def Function_32_4DE7(): pass

    label("Function_32_4DE7")

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

    # Function_32_4DE7 end

    def Function_33_4E28(): pass

    label("Function_33_4E28")

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

    # Function_33_4E28 end

    def Function_34_4E5C(): pass

    label("Function_34_4E5C")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EB8")
    Call(0, 27)
    Jump("loc_4EBB")

    label("loc_4EB8")

    Call(0, 28)

    label("loc_4EBB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5073")
    BeginChrThread(0x101, 0, 0, 35)
    WaitChrThread(0x101, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5009")

    ChrTalk(
        0x101,
        (
            "#00006F#11P...It's no use. It looks\x02\x03",
            "like that even if we hit it,\x01",
            "it wouldn't break down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PIf only we could at least figure\x01",
            "out who is inside there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5073")

    label("loc_5009")


    ChrTalk(
        0x101,
        "#00003F#11P...It's the same with the left gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6PI wonder...\x01",
            "Who could be inside here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5073")

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
            "#3961V#40W#40AUhuhu...aaah ha ha ha ha...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3962V#40W#38ANot yet...?\x01",
            "Isn't she coming yet...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3963V#40W#38AI'm so looking forward to it\x01",
            "that I can't wait anymore...!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58F2")

    ChrTalk(
        0x106,
        "#10708F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5POh boy...it's her.\x02\x03",
            "#00301FAnd also, it seems who\x01",
            "she's waitin' is not me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_52FF():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_52FF)
    Sleep(50)

    def lambda_530F():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_530F)
    Sleep(50)

    def lambda_531F():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_531F)
    Sleep(50)

    def lambda_532F():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_532F)
    Sleep(50)

    def lambda_533F():
        TurnDirection(0xF5, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_533F)
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
            "#10706F#6P──No.\x02\x03",
            "#10708FIn a certain sense, she and I\x01",
            "have similar circumstances.\x02\x03",
            "I have to confront\x01",
            "her one more time...\x02\x03",
            "#10701FEven in order to find\x01",
            "out my future path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P......Understood.\x02",
    )

    CloseMessageWindow()

    def lambda_548A():
        OP_96(0xFE, 0x2AF8, 0x639C, 0xFFFE09A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_548A)

    def lambda_54A4():

        label("loc_54A4")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_54A4")

    QueueWorkItem2(0x101, 2, lambda_54A4)

    def lambda_54B6():

        label("loc_54B6")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_54B6")

    QueueWorkItem2(0x102, 2, lambda_54B6)

    def lambda_54C8():

        label("loc_54C8")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_54C8")

    QueueWorkItem2(0x103, 2, lambda_54C8)

    def lambda_54DA():

        label("loc_54DA")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_54DA")

    QueueWorkItem2(0x104, 2, lambda_54DA)

    def lambda_54EC():

        label("loc_54EC")

        TurnDirection(0xFE, 0x106, 500)
        Yield()
        Jump("loc_54EC")

    QueueWorkItem2(0xF5, 2, lambda_54EC)
    Sleep(300)
    OP_68(12230, 26000, -127620, 2000)
    MoveCamera(2, 26, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(13750, 2000)

    def lambda_552F():
        OP_95(0xFE, 12000, 25800, -129000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_552F)
    Sleep(150)

    def lambda_554C():
        OP_9B(0x1, 0xFE, 0x13B, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_554C)
    WaitChrThread(0x106, 1)

    def lambda_5565():
        OP_96(0xFE, 0x29FE, 0x64C8, 0xFFFE0336, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5565)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5650")

    ChrTalk(
        0x102,
        "#00105F#6PThe barrier disappeared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PNow we can go to that\x01",
            ""territory" grounds, huh...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AA, 0)
    Jump("loc_56A6")

    label("loc_5650")


    ChrTalk(
        0x103,
        "#00201F#6P#NIt vanished...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#5PNow we can go to the "territory"...\x02",
    )

    CloseMessageWindow()

    label("loc_56A6")

    Sleep(200)
    OP_93(0x106, 0xE1, 0x1F4)

    ChrTalk(
        0x106,
        (
            "#10703F......#11PAn opponent is an opponent.\x02\x03",
            "#10710FLet's be very well prepared so to\x01",
            "not be overwhelmed one-sidedly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5862")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5798")

    ChrTalk(
        0x109,
        (
            "#10106F#6PIt could also be good to go back\x01",
            "to the Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_585D")

    label("loc_5798")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57F9")

    ChrTalk(
        0x10A,
        (
            "#00603F#6PIt could even be good to return\x01",
            "to the Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_585D")

    label("loc_57F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_585D")

    ChrTalk(
        0x105,
        (
            "#10404F#6PIt could also benefit us good to return\x01",
            "to the Merkabah temporarily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_585D")

    Jump("loc_58E5")

    label("loc_5862")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_588E")

    ChrTalk(
        0x109,
        "#10101F#6PYes...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_588E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58B8")

    ChrTalk(
        0x10A,
        "#00601F#6PYeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_58E5")

    label("loc_58B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58E5")

    ChrTalk(
        0x105,
        "#10402F#6PYou're right.\x02",
    )

    CloseMessageWindow()

    label("loc_58E5")

    SetScenarioFlags(0x1AA, 2)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_5ABC")

    label("loc_58F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_END)), "loc_59D4")

    ChrTalk(
        0x104,
        (
            "#00305F#5PThe barrier went back to its original form...\x02\x03",
            "#00303FIt looks like we can't\x01",
            "enter this "territory"\x01",
            "without dear Rixia..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah...let's return to the Merkabah\x01",
            "and bring Rixia with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABC")

    label("loc_59D4")


    ChrTalk(
        0x104,
        (
            "#00306F#5POh boy...it's her.\x02\x03",
            "#00301FAnd also, it seems who\x01",
            "she's waitin' is not me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah....\x02\x03",
            "#00008F(We need to return to the Merkabah\x01",
            "and bring "her" with us, but...)\x02\x03",
            "(Is it really alright to have her come?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ABC")

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

    # Function_34_4E5C end

    def Function_35_5AFB(): pass

    label("Function_35_5AFB")

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

    # Function_35_5AFB end

    def Function_36_5B81(): pass

    label("Function_36_5B81")

    Sleep(800)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_36_5B81 end

    def Function_37_5B8C(): pass

    label("Function_37_5B8C")

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

    # Function_37_5B8C end

    def Function_38_5BCD(): pass

    label("Function_38_5BCD")

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

    # Function_38_5BCD end

    def Function_39_5C01(): pass

    label("Function_39_5C01")

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

    def lambda_5D97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D97)

    def lambda_5DA8():
        OP_95(0xFE, -10480, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DA8)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5DFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DFF)

    def lambda_5E10():
        OP_95(0xFE, -11560, 25000, -131300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E10)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5E6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5E6D)

    def lambda_5E7E():
        OP_95(0xFE, -9720, 25000, -129240, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E7E)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5ED5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5ED5)

    def lambda_5EE6():
        OP_95(0xFE, -12970, 25000, -131780, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EE6)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5F43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_5F43)

    def lambda_5F54():
        OP_95(0xFE, -12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_5F54)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_5FAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_5FAB)

    def lambda_5FBC():
        OP_95(0xFE, -11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_5FBC)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 5)), scpexpr(EXPR_END)), "loc_62A3")
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

    def lambda_60B0():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_60B0)
    Sleep(50)

    def lambda_60C0():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_60C0)
    Sleep(50)

    def lambda_60D0():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_60D0)
    Sleep(50)

    def lambda_60E0():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_60E0)
    Sleep(50)

    def lambda_60F0():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_60F0)
    Sleep(50)

    def lambda_6100():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F#6P#NThe magical barrier...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#6P#NIt appears that the two "territories"\x01",
            "have been released.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHu hu, now we're finally\x01",
            "able to proceed forward.\x02\x03",
            "#10408F...Before that, I'd like to go back\x01",
            "to the airship for a bit and rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PRight...we have to report to everyone too, so it\x01",
            "would be nice going back to the Merkabah for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6534")

    label("loc_62A3")

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

    def lambda_634B():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_634B)
    Sleep(50)

    def lambda_635B():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_635B)
    Sleep(50)

    def lambda_636B():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_636B)
    Sleep(50)

    def lambda_637B():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_637B)
    Sleep(50)

    def lambda_638B():
        OP_93(0xF4, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_638B)
    Sleep(50)

    def lambda_639B():
        OP_93(0xF5, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_639B)
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
            "#00005F#6PThe central gate magical barrier...\x01",
            "Has weakened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PProbably because we could release\x01",
            "Mr. Wald's "territory".\x02\x03",
            "#00201FI think that maybe this "Sanctuary"\x01",
            "is connected with each\x01",
            "person's "territory".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P#NSo it means that if we can\x01",
            "release the other "territory"...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10400F#6PMaybe that magical barrier\x01",
            "would vanish completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6534")

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

    # Function_39_5C01 end

    def Function_40_6571(): pass

    label("Function_40_6571")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6952")
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_670F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_670F)

    def lambda_6720():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6720)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x102, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6777():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6777)

    def lambda_6788():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6788)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_67E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_67E5)

    def lambda_67F6():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_67F6)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_684D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_684D)

    def lambda_685E():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_685E)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_68BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_68BB)

    def lambda_68CC():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_68CC)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6923():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6923)

    def lambda_6934():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_6934)
    WaitChrThread(0xF5, 1)
    Jump("loc_6BD5")

    label("loc_6952")

    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xF5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6997():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6997)

    def lambda_69A8():
        OP_95(0xFE, 10560, 25000, -129930, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_69A8)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_69FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_69FF)

    def lambda_6A10():
        OP_95(0xFE, 9760, 25000, -128710, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A10)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6A6D)

    def lambda_6A7E():
        OP_95(0xFE, 11490, 25000, -130720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A7E)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6AD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6AD5)

    def lambda_6AE6():
        OP_95(0xFE, 12490, 25000, -131720, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6AE6)
    Sleep(400)
    Sound(920, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6B43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B43)

    def lambda_6B54():
        OP_95(0xFE, 12220, 25700, -129840, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B54)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xF4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_6BAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6BAB)

    def lambda_6BBC():
        OP_95(0xFE, 11280, 25700, -128870, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_6BBC)
    WaitChrThread(0xF5, 1)

    label("loc_6BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 0)), scpexpr(EXPR_END)), "loc_6E7F")
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

    def lambda_6CB0():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6CB0)
    Sleep(50)

    def lambda_6CC0():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6CC0)
    Sleep(50)

    def lambda_6CD0():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6CD0)
    Sleep(50)

    def lambda_6CE0():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6CE0)
    Sleep(50)

    def lambda_6CF0():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6CF0)
    Sleep(50)

    def lambda_6D00():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6D00)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00102F#12PThe magical barrier...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#NIt appears that the two "territories"\x01",
            "have been released.\x02",
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
            "#00006F#11PYeah, however it's been a\x01",
            "hard fight like expected...\x02\x03",
            "#00000FWe have to report to everyone too, so it would\x01",
            "be nice going back to the Merkabah for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_711B")

    label("loc_6E7F")

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

    def lambda_6F27():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F27)
    Sleep(50)

    def lambda_6F37():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6F37)
    Sleep(50)

    def lambda_6F47():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6F47)
    Sleep(50)

    def lambda_6F57():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6F57)
    Sleep(50)

    def lambda_6F67():
        OP_93(0xF4, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_6F67)
    Sleep(50)

    def lambda_6F77():
        OP_93(0xF5, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_6F77)
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
            "#00005F#12PThe central gate magical barrier...\x01",
            "Has weakened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P#NProbably because we could release\x01",
            "Miss Shirley's "territory".\x02\x03",
            "#00201FI think that maybe this "Sanctuary"\x01",
            "is connected with each\x01",
            "person's "territory".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#12PSo it means that if we can\x01",
            "release the other "territory"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702F#12PMaybe that magical barrier\x01",
            "would disappear completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_711B")

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

    # Function_40_6571 end

    def Function_41_7158(): pass

    label("Function_41_7158")

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

    # Function_41_7158 end

    def Function_42_7238(): pass

    label("Function_42_7238")

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

    # Function_42_7238 end

    SaveToFile()

Try(main)
