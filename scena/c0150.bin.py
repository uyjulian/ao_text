from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0150.bin",                # FileName
        "c0150",                    # MapName
        "c0150",                    # Location
        0x0007,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0150",                  # 0
        "Wistoff",                # 1
        "Brown",                  # 2
        "Certeo",                 # 3
        "Nonno",                  # 4
        "Flote",                  # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Citizen",                # 8
        "Citizen",                # 9
        "Citizen",                # 10
        "Citizen",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Citizen",                # 16
        "Citizen",                # 17
        "Jona",                   # 18
        "Chief Roberts",          # 19
        "Abel",                   # 20
        "Mimi",                   # 21
        "Sally",                  # 22
        "Aide Kilika",            # 23
        "Gironde",                # 24
        "Clyde",                  # 25
        "Mrs. Margaret",          # 26
        "Food",                   # 27
        "Food",                   # 28
        "Food",                   # 29
        "Food",                   # 30
        "Food",                   # 31
        "Food",                   # 32
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch24502.itc",                   # 06
        "chr/ch21302.itc",                   # 07
        "chr/ch21702.itc",                   # 08
        "chr/ch21602.itc",                   # 09
        "chr/ch21002.itc",                   # 0A
        "chr/ch20302.itc",                   # 0B
        "chr/ch33202.itc",                   # 0C
        "chr/ch33102.itc",                   # 0D
        "chr/ch32302.itc",                   # 0E
        "chr/ch22102.itc",                   # 0F
        "chr/ch20502.itc",                   # 10
        "chr/ch24402.itc",                   # 11
        "chr/ch06102.itc",                   # 12
        "chr/ch29302.itc",                   # 13
        "chr/ch20202.itc",                   # 14
        "chr/ch20702.itc",                   # 15
        "chr/ch34602.itc",                   # 16
        "chr/ch13302.itc",                   # 17
    ))

    DeclNpc(4294966787, 0,       12449,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294924407, 0,       5699,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294915267, 0,       3650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294958416, 0,       3240,    45,   261,  0x0, 0,   3,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(4294959847, 150,     8510,    270,  325,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   6,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(2430,    5150,    17639,   180,  453,  0x0, 0,   8,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(2430,    5150,    13430,   0,    453,  0x0, 0,   9,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(3230,    150,     4294965507, 180,  453,  0x0, 0,   10,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(5440,    150,     4294963306, 270,  453,  0x0, 0,   11,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(6360,    5150,    17639,   180,  453,  0x0, 0,   12,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(6360,    5150,    13439,   0,    453,  0x0, 0,   13,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(4460,    150,     5829,    180,  453,  0x0, 0,   14,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(6679,    150,     3630,    270,  453,  0x0, 0,   15,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(3230,    150,     4294965507, 180,  453,  0x0, 0,   16,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(5440,    150,     4294963306, 270,  453,  0x0, 0,   17,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(4294965647, 5150,    17649,   180,  453,  0x0, 0,   18,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(4294965647, 5150,    13439,   0,    453,  0x0, 0,   19,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(3190,    150,     4294961146, 0,    389,  0x0, 0,   20,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(5440,    150,     4294963306, 270,  389,  0x0, 0,   21,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(3230,    150,     4294965507, 180,  389,  0x0, 0,   22,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(4294965617, 5150,    17739,   180,  453,  0x0, 0,   23,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(60580,   4294966296, 4294958696, 270,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294964096, 699,     3349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294964096, 699,     1350,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294963097, 699,     2349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294965096, 699,     2349,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294963296, 699,     1549,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294963296, 699,     3150,    0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(59140,   4294966296, 4294958416, 1500,    60580,   500,     4294958696, 0x007E, 0,  5,  0x0000)
    DeclActor(4294966786, 0,       10640,   1000,    4294966786, 1500,    12450,   0x007E, 0,  7,  0x0000)
    DeclActor(4294927596, 0,       7810,    2000,    4294927596, 1700,    7810,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1424, 0)                                       # 0

    ScpFunction((
        "Function_0_590",          # 00, 0
        "Function_1_648",          # 01, 1
        "Function_2_6E5",          # 02, 2
        "Function_3_D37",          # 03, 3
        "Function_4_DB1",          # 04, 4
        "Function_5_ED5",          # 05, 5
        "Function_6_ED9",          # 06, 6
        "Function_7_2A91",         # 07, 7
        "Function_8_2A95",         # 08, 8
        "Function_9_4231",         # 09, 9
        "Function_10_52E5",        # 0A, 10
        "Function_11_678E",        # 0B, 11
        "Function_12_7685",        # 0C, 12
        "Function_13_8A73",        # 0D, 13
        "Function_14_8B4B",        # 0E, 14
        "Function_15_8C69",        # 0F, 15
        "Function_16_8D05",        # 10, 16
        "Function_17_8DDD",        # 11, 17
        "Function_18_8F2F",        # 12, 18
        "Function_19_9023",        # 13, 19
        "Function_20_9164",        # 14, 20
        "Function_21_9330",        # 15, 21
        "Function_22_95B7",        # 16, 22
        "Function_23_9858",        # 17, 23
        "Function_24_996A",        # 18, 24
        "Function_25_9B06",        # 19, 25
        "Function_26_9D66",        # 1A, 26
        "Function_27_9FD5",        # 1B, 27
        "Function_28_A1A3",        # 1C, 28
        "Function_29_A30D",        # 1D, 29
        "Function_30_A37E",        # 1E, 30
        "Function_31_B471",        # 1F, 31
        "Function_32_C0D8",        # 20, 32
        "Function_33_C3E5",        # 21, 33
        "Function_34_D0E4",        # 22, 34
        "Function_35_E061",        # 23, 35
        "Function_36_E091",        # 24, 36
        "Function_37_E0D7",        # 25, 37
        "Function_38_E11D",        # 26, 38
        "Function_39_E154",        # 27, 39
        "Function_40_E18B",        # 28, 40
        "Function_41_E1D1",        # 29, 41
        "Function_42_E215",        # 2A, 42
        "Function_43_E259",        # 2B, 43
    ))


    def Function_0_590(): pass

    label("Function_0_590")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5D0"),
        (1, "loc_5DC"),
        (2, "loc_5E8"),
        (3, "loc_5F4"),
        (4, "loc_600"),
        (5, "loc_60C"),
        (6, "loc_618"),
        (SWITCH_DEFAULT, "loc_624"),
    )


    label("loc_5D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_5DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_5E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_5F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_600")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_60C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_618")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_624")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_630")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_647")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_630")

    label("loc_647")

    Return()

    # Function_0_590 end

    def Function_1_648(): pass

    label("Function_1_648")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_648")

    label("loc_6E4")

    Return()

    # Function_1_648 end

    def Function_2_6E5(): pass

    label("Function_2_6E5")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_704")
    Jump("loc_D0E")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_76B")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x14)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0x16)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x15)
    SetChrSubChip(0x1C, 0x0)
    EndChrThread(0x1C, 0x0)
    SetChrBattleFlags(0x1C, 0x4)
    Jump("loc_D0E")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7A5")
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x10)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x11)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_D0E")

    label("loc_7A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7DF")
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x10)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x11)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    Jump("loc_D0E")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_847")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8AF")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_8AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_917")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_97F")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_D0E")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A13")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xF)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x12)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x13)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    Jump("loc_D0E")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AB1")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jump("loc_D0E")

    label("loc_AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_ABF")
    Jump("loc_D0E")

    label("loc_ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B86")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B05")
    SetChrFlags(0xB, 0x10)

    label("loc_B05")

    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B81")
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0x17)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)

    label("loc_B81")

    Jump("loc_D0E")

    label("loc_B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C24")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xD)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jump("loc_D0E")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C94")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_D0E")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D0E")
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)

    label("loc_D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D36")
    SetMapFlags(0x10000000)
    Event(0, 34)

    label("loc_D36")

    Return()

    # Function_2_6E5 end

    def Function_3_D37(): pass

    label("Function_3_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D6A")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D93")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_D93")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DB0")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_DB0")

    Return()

    # Function_3_D37 end

    def Function_4_DB1(): pass

    label("Function_4_DB1")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "==New Menu - Herb Pasta==\x01",
            "──Your favorite flavors are back\x01",
            "──Makes good use of fresh herbs\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Herb Pasta recipe is written here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_ED1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Herb Pasta"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_ED1")

    TalkEnd(0xFF)
    Return()

    # Function_4_DB1 end

    def Function_5_ED5(): pass

    label("Function_5_ED5")

    Call(0, 6)
    Return()

    # Function_5_ED5 end

    def Function_6_ED9(): pass

    label("Function_6_ED9")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(
        0x1F,
        "Yo, Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I heard from Sergei. You guys\x01",
            "finally started back up again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "Hmm? That redheaded guy and\x01",
            "that young miss who uses the\x01",
            "orbal staff aren't with you yet, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, they have personal\x01",
            "business to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "And those two must\x01",
            "be the new members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I heard about your preferred arms from Sergei.\x01",
            "Come see if there's anything you might like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, thanks for getting everything ready for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 2)

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145F")
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "Oh, it's you guys...\x01",
            "Thank you for coming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Gironde, \x01",
            "it's been awhile.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_131C")

    ChrTalk(
        0x1F,
        (
            "Hehe, you look like you can\x01",
            "be trusted, same as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "But Dudley being with you too means...\x01",
            "That you're finally moving to action?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYeah. It's going to get a little noisy,\x01",
            "so please forgive us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Heh, it's a little\x01",
            "late for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, I got\x01",
            "everything ready for\x01",
            "you guys, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "There's nothing too fancy, but\x01",
            "feel free to have a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1435")

    label("loc_131C")


    ChrTalk(
        0x1F,
        (
            "Hehe, you look like you can\x01",
            "be trusted, same as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "By the way, I heard about a lot\x01",
            "that's going on from the police.\x01",
            "No need to say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, I got\x01",
            "everything ready for\x01",
            "you guys, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "There's nothing too fancy, but\x01",
            "feel free to have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1435")


    ChrTalk(
        0x101,
        "#00000FSure, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 0)

    label("loc_145F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A8D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_14B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_14D8")
    OP_AF(0x5)
    Jump("loc_151A")

    label("loc_14D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14E8")
    OP_AF(0x4)
    Jump("loc_151A")

    label("loc_14E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14F8")
    OP_AF(0x3)
    Jump("loc_151A")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1508")
    OP_AF(0x2)
    Jump("loc_151A")

    label("loc_1508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1518")
    OP_AF(0x1)
    Jump("loc_151A")

    label("loc_1518")

    OP_AF(0x0)

    label("loc_151A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A88")

    label("loc_1529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_153D")
    Jump("loc_2A88")

    label("loc_153D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A88")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_162D")

    ChrTalk(
        0x1F,
        (
            "*sigh*, that weird tree aside, I feel\x01",
            "like the city's finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, it's gonna be a struggle from here on out, but... \x01",
            "Given the situation, each of us has to do the best we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_162D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_16C0")

    ChrTalk(
        0x1F,
        (
            "Heh, anyway, I have new respect\x01",
            "for the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Anyway guys, from now on, \x01",
            "give this everything you have!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_16C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_18A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F2")

    ChrTalk(
        0x1F,
        (
            "The State Guard and Dieter Crois too\x01",
            "have done an outrageous thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "They even had special uniforms ready, so\x01",
            "they must've been planning this for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It'd really prefer they didn't\x01",
            "had weapons and arms, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, the truth is that\x01",
            "it's unavoidable, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18A4")

    label("loc_17F2")


    ChrTalk(
        0x1F,
        (
            "It'd really prefer they didn't\x01",
            "had weapons and arms, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, the truth is that\x01",
            "it's unavoidable, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Oh man... I'm worried about what's going to happen next.\x02",
    )

    CloseMessageWindow()

    label("loc_18A4")

    Jump("loc_2A88")

    label("loc_18A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D8")

    ChrTalk(
        0x1F,
        (
            "Many citizens came into the\x01",
            "store due to that disturbance\x01",
            "over at Mainz awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I told them they couldn't buy weapons\x01",
            "without a license, but there were some\x01",
            "stubborn ones mixed into that crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, given the situation, I\x01",
            "understand how they feel, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A64")

    label("loc_19D8")


    ChrTalk(
        0x1F,
        (
            "Anyway, as one who deals in\x01",
            "weapons, I guess this is\x01",
            "part of the job as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's a good chance. \x01",
            "You guys too, keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A64")

    Jump("loc_2A88")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(
        0x1F,
        (
            "Hey, quite the depressed\x01",
            "mugs today again, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If you guys are going anywhere\x01",
            "dangerous, you had best\x01",
            "prepare yourselves beforehand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Dead customers are bad for business.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC2")

    label("loc_1B3D")


    ChrTalk(
        0x1F,
        (
            "If you guys are going anywhere\x01",
            "dangerous, you had best\x01",
            "prepare yourselves beforehand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Dead customers are bad for business.\x02",
    )

    CloseMessageWindow()

    label("loc_1BC2")

    Jump("loc_2A88")

    label("loc_1BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFD")

    ChrTalk(
        0x1F,
        (
            "There's a rumor going around that\x01",
            "the train accident yesterday was\x01",
            "caused by an ogre-like monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Heh, it's easy to say "an ogre",\x01",
            "but what the heck are they talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's not the case that a human\x01",
            "can turn into an ogre, but...\x01",
            "Anyway, it's a disturbing story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB0")

    label("loc_1CFD")


    ChrTalk(
        0x1F,
        (
            "Heh, it's easy to say "an ogre",\x01",
            "but what the heck are they talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's not the case that a human\x01",
            "can turn into an ogre, but...\x01",
            "Anyway, it's a disturbing story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB0")

    Jump("loc_2A88")

    label("loc_1DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E5A")

    ChrTalk(
        0x1F,
        (
            "Ahh, there's nothing more\x01",
            "irritating than sirens' sounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I don't know if it's an incident or an\x01",
            "accident, but... It's really noisy in town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_1E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F63")

    ChrTalk(
        0x1F,
        "Oh, it's you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I don't care what you want, but\x01",
            "hurry up and choose already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's hard to read my magazine with\x01",
            "you guys standing there, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(...As usual, he has no intention\x01",
            "of doing a proper job.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FF3")

    label("loc_1F63")


    ChrTalk(
        0x1F,
        (
            "I don't know what you guys want,\x01",
            "but hurry up and choose already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's hard to read my magazine with\x01",
            "you guys standing there, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF3")

    Jump("loc_2A88")

    label("loc_1FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20AF")

    ChrTalk(
        0x1F,
        (
            "*sigh*, we can't accept the demands of the two major\x01",
            "powers, hence the independence proposal, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Anyway, I just pray that we can\x01",
            "avoid a declaration of war.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_20AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E6")

    ChrTalk(
        0x1F,
        (
            "Hey there young miss. Looks like you've\x01",
            "finally returned to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "That man left some orbal staves with me,\x01",
            "so I thought you might be stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FT-That man...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes, that was most likely the chief.\x02\x03",
            "#00211FKnowing he'll be stopping here before us\x01",
            "is what makes me somehow feel annoyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FW-Well, he's just that\x01",
            "worried about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, he's not that bad a\x01",
            "person. Actually, I think\x01",
            "he's a pretty good one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...I don't deny it, but I think it's his\x01",
            "excessive disposition that I don't like.\x02\x03",
            "#00200FOn top of his excessive interference\x01",
            "and frequent awkward chatting.... He's\x01",
            "not someone I want to hang around with.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239F")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_239F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C5")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_23C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23EB")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_23EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2411")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2411")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10103FI-I see. It seems there'a\x01",
            "a lot between you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Bwah ha ha, I don't really get it, but we'll\x01",
            "have orbal staves for sale from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "If you ever need one, just say the word.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 5)
    Jump("loc_2564")

    label("loc_24E6")


    ChrTalk(
        0x1F,
        (
            "Because you've returned, young miss,\x01",
            "we've resumed dealing in orbal staves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, if you need one,\x01",
            "ask me whenever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2564")

    Jump("loc_2A88")

    label("loc_2569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DE")

    ChrTalk(
        0x1F,
        (
            "Hey, if it isn't Dudley.\x01",
            "A friendly stroll with the Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FNo, there's something I'm worried about a little.\x02\x03",
            "#00600FSince I can't leave it to just them,\x01",
            "I'm going along too, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Heh! You're the same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, whatever, since I'm about to close shop,\x01",
            "if you want to have a look, do it quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2760")

    label("loc_26DE")


    ChrTalk(
        0x1F,
        (
            "I'm about to close shop, you see.\x01",
            "If you want to have a look, do it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "I want to close up quick and have a drink.\x02",
    )

    CloseMessageWindow()

    label("loc_2760")

    Jump("loc_2A88")

    label("loc_2765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2851")

    ChrTalk(
        0x1F,
        (
            "I don't know if it's due to the Trade\x01",
            "Conference or whatever, but those two\x01",
            "major powers aren't to be taken lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If they show their sweet faces\x01",
            "in here, though, I'll be quite\x01",
            "happy to take advantage of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_2851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2944")

    ChrTalk(
        0x1F,
        (
            "With Revache gone, seems there's been\x01",
            "fewer gunfights in the underworld, but...\x01",
            "I can't help but think it's ominous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When nothing ever happens like this, I'll be\x01",
            "out of business before long. Am I dreaming?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29A7")

    label("loc_2944")


    ChrTalk(
        0x1F,
        (
            "I've had more\x01",
            "free time lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Goddess, I beg of you. \x01",
            "Please, let me continue to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A7")

    Jump("loc_2A88")

    label("loc_29AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A32")

    ChrTalk(
        0x1F,
        (
            "*sigh*, quite the gloom\x01",
            "weather today too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, I guess it doesn't matter\x01",
            "for an indoor store like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A88")

    label("loc_2A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A88")

    ChrTalk(
        0x1F,
        (
            "I've got all the weapons\x01",
            "you guys need in stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Come take a look.\x02",
    )

    CloseMessageWindow()

    label("loc_2A88")

    Jump("loc_1469")

    label("loc_2A8D")

    TalkEnd(0x1F)
    Return()

    # Function_6_ED9 end

    def Function_7_2A91(): pass

    label("Function_7_2A91")

    Call(0, 8)
    Return()

    # Function_7_2A91 end

    def Function_8_2A95(): pass

    label("Function_8_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2ACC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ACC")
    Call(0, 33)
    Return()

    label("loc_2ACC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D51")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, you're from the police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard you guys are separate\x01",
            "from the State Guard, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's right. We're\x01",
            "working to end this\x01",
            "situation in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAre you having\x01",
            "any troubles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, the customers are few and\x01",
            "there's basically just the staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think it's calmer\x01",
            "here than other places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is a restaurant, so there's no need\x01",
            "to worry about getting something to eat too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see. \x01",
            "That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIn any case, it's dangerous\x01",
            "to go outside right now.\x02\x03",
            "#00100FPlease stand put\x01",
            "here with everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Alright, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 7)
    TalkEnd(0x8)
    Return()

    label("loc_2D51")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_422D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DAB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2DAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2DCA")
    OP_AF(0x9)
    Jump("loc_2DCC")

    label("loc_2DCA")

    OP_AF(0x8)

    label("loc_2DCC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4228")

    label("loc_2DDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DEF")
    Jump("loc_4228")

    label("loc_2DEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4228")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2E72")

    ChrTalk(
        0x8,
        (
            "By all means, please\x01",
            "come visit next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We will wait for\x01",
            "your patronage again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4228")

    label("loc_2E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F56")

    ChrTalk(
        0x8,
        (
            "Vingt Sept will be fine\x01",
            "if I just leave it to\x01",
            "Certeo and Nonno.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before that, though,\x01",
            "Crossbell has to get through\x01",
            "all its difficulties...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if everyone works together,\x01",
            "there's nothing we can't do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4228")

    label("loc_2F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3032")

    ChrTalk(
        0x8,
        (
            "Hmm, if the police\x01",
            "is here, I feel very\x01",
            "reassured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, as the store manager,\x01",
            "I have to take responsibility\x01",
            "for this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please be careful when\x01",
            "you're walking around outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4228")

    label("loc_3032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3177")

    ChrTalk(
        0x8,
        (
            "The IBC declared an asset freeze...\x01",
            "And rail and bus services have been\x01",
            "suspended as of this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, in this situation, it wouldn't\x01",
            "be strange if something did happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I intend to continue my business if possible but...\x01",
            "Honestly, there are a lot of things I'm worried about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3254")

    label("loc_3177")


    ChrTalk(
        0x8,
        (
            "The IBC declared an asset freeze...\x01",
            "And rail and bus services have been\x01",
            "suspended as of this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I intend to continue my business if possible but...\x01",
            "Honestly, there are a lot of things I'm worried about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3254")

    Jump("loc_4228")

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_347E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D0")

    ChrTalk(
        0x8,
        (
            "Because of that incident, I was\x01",
            "thinking of postponing the cooking\x01",
            "battle between Certeo and Nonno, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They insisted on it, so we held it\x01",
            "after closing yesterday evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The result? Each of them\x01",
            "made such amazing dishes,\x01",
            "it brought me to tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Dear me, seeing my junior's\x01",
            "growth with my own eyes is\x01",
            "such an amazing thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3479")

    label("loc_33D0")


    ChrTalk(
        0x8,
        (
            "Hmm. With Nonno's skill,\x01",
            "leaving her out of the kitchen\x01",
            "would be a huge waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Three people in the kitchen... I've got\x01",
            "to think about how this is going to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3479")

    Jump("loc_4228")

    label("loc_347E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_350C")

    ChrTalk(
        0x8,
        (
            "We have some Mainz residents\x01",
            "among our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know a lot of them personally...\x01",
            "And I'm very worried about them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4228")

    label("loc_350C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_367A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35ED")

    ChrTalk(
        0x8,
        (
            "Hu hu, it seems Certeo is\x01",
            "thinking hard about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was like that too, and the\x01",
            "answer came only after\x01",
            "worrying a whole bunch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish this experience\x01",
            "will be good for Certeo.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3675")

    label("loc_35ED")


    ChrTalk(
        0x8,
        (
            "I was like that too, and the\x01",
            "answer came only after\x01",
            "worrying a whole bunch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wish this experience\x01",
            "will be good for Certeo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3675")

    Jump("loc_4228")

    label("loc_367A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_37E4")

    ChrTalk(
        0x8,
        (
            "I heard a train accident occurred\x01",
            "near West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must've been falling rocks\x01",
            "that did it. It seems many people\x01",
            "were injured...that's worrying.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37DF")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get coverage for\x01",
            "the gourmet guide here, but...)\x02\x03",
            "#00003F(Now's not the time. Let's\x01",
            "not forget to stop by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37DF")

    Jump("loc_4228")

    label("loc_37E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_395A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CA")

    ChrTalk(
        0x8,
        (
            "Certeo's attitude towards work has changed recently.\x01",
            "It's like he's a whole different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "His reactions towards our attractive\x01",
            "female customers have disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, how wonderful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3955")

    label("loc_38CA")


    ChrTalk(
        0x8,
        (
            "Up until now, Certeo has been passionate\x01",
            "about women, but he's gradually turned\x01",
            "his passion towards cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, how wonderful.\x02",
    )

    CloseMessageWindow()

    label("loc_3955")

    Jump("loc_4228")

    label("loc_395A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_39E0")

    ChrTalk(
        0x8,
        (
            "Hu hu, it seem Certeo has\x01",
            "finally gotten serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "At this rate, I have no idea how the battle is going to go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4228")

    label("loc_39E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA3")

    ChrTalk(
        0x8,
        (
            "As you might expect, Certeo got\x01",
            "flustered when he heard Brown\x01",
            "trusted Nonno with the cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... Maybe what\x01",
            "Certeo was lacking all\x01",
            "this time was a rival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B64")

    label("loc_3AA3")


    ChrTalk(
        0x8,
        (
            "Thinking back on it now, when I was\x01",
            "learning the trade, I was always competing\x01",
            "with Brown, and improved because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... Maybe what\x01",
            "Certeo was lacking all\x01",
            "this time was a rival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B64")

    Jump("loc_4228")

    label("loc_3B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3CC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C50")

    ChrTalk(
        0x8,
        (
            "I've heard about it from Brown.\x01",
            "It seems that Nonno has got\x01",
            "a feeling for cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first I only intended to get\x01",
            "some simple help from her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, this could be an\x01",
            "unexpected result.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CBD")

    label("loc_3C50")


    ChrTalk(
        0x8,
        (
            "I only intended to get some\x01",
            "simple help from Nonno, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm, this could be an\x01",
            "unexpected result.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBD")

    Jump("loc_4228")

    label("loc_3CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E36")

    ChrTalk(
        0x8,
        (
            "It took some courage to make\x01",
            "Certeo a waiter, but it seems\x01",
            "it went better than expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He showed a minimum level of respect\x01",
            "to his favorite female customers too.\x01",
            "He should be fine going forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. I suppose he's\x01",
            "finally ready to learn the\x01",
            "basics of being a chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, maybe I should look at it as a personal challenge.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F0A")

    label("loc_3E36")


    ChrTalk(
        0x8,
        (
            "When Certeo makes the food, he's\x01",
            "always mixing in surprise ingredients\x01",
            "and coming up with wild ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For that reason, he really hates\x01",
            "the orthodox method, but... \x01",
            "It seems I'll have to rethink things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0A")

    Jump("loc_4228")

    label("loc_3F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4030")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA3")

    ChrTalk(
        0x8,
        (
            "Taking away his job, I thought\x01",
            "he'd be shocked for sure, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, it seems it didn't go\x01",
            "as I was expecting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_402B")

    label("loc_3FA3")


    ChrTalk(
        0x8,
        (
            "Somehow, if I were to fire\x01",
            "Certeo, the burden on\x01",
            "Brown would be too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can't continue\x01",
            "this nonsense...\x01",
            "Hmm, what to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402B")

    Jump("loc_4228")

    label("loc_4030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_411B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C0")

    ChrTalk(
        0x8,
        (
            "Hmm, just leaving our Certeo\x01",
            "alone won't develop him at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I've got to\x01",
            "consider drastic measures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4116")

    label("loc_40C0")


    ChrTalk(
        0x8,
        (
            "Hmm... I've got to\x01",
            "consider drastic measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope Certeo\x01",
            "changes, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4116")

    Jump("loc_4228")

    label("loc_411B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41CC")

    ChrTalk(
        0x8,
        (
            "Hello, and welcome\x01",
            "to "Vingt Sept".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We change a portion of our\x01",
            "menu seasonally each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Would you like to try\x01",
            "Chef Brown's new menu?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4228")

    label("loc_41CC")


    ChrTalk(
        0x8,
        (
            "We change a portion of our\x01",
            "menu seasonally each year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you like, please try it.\x02",
    )

    CloseMessageWindow()

    label("loc_4228")

    Jump("loc_2D5B")

    label("loc_422D")

    TalkEnd(0x8)
    Return()

    # Function_8_2A95 end

    def Function_9_4231(): pass

    label("Function_9_4231")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_42BD")

    ChrTalk(
        0xFE,
        (
            "That Certeo, somehow he broke\x01",
            "through his doubts al of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, well good then.\x01",
            "Finally, I too can relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_42BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4382")

    ChrTalk(
        0xFE,
        (
            "Having the food you made\x01",
            "eaten with pleasure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a chef, there is\x01",
            "no greater happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Knowing there are customers\x01",
            "even in a situation like this\x01",
            "gives me strength.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_4382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4431")

    ChrTalk(
        0xFE,
        "Rail has been shut down ever since this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What to do about substitutes for imported\x01",
            "ingredients? For us, this is a pressing issue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44FF")

    label("loc_4431")


    ChrTalk(
        0xFE,
        (
            "Somehow I feel like an attack could\x01",
            "come at any moment, but... At present,\x01",
            "we chefs can only do one thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What to do about substitutes for imported\x01",
            "ingredients? For us, this is a pressing issue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FF")

    Jump("loc_52E1")

    label("loc_4504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463D")

    ChrTalk(
        0xFE,
        (
            "I'm relieved to see that Certeo\x01",
            "finally shows his true colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pasta he prepared\x01",
            "was seasoned with seafood\x01",
            "on a tomato base, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He did a nice job bringing out the\x01",
            "flavor with several other spices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its flavor is fresh and outstanding.\x01",
            "He did very well on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_46D6")

    label("loc_463D")


    ChrTalk(
        0xFE,
        (
            "Before, Certeo had the...\x01",
            "prejudice...of combining\x01",
            "standard ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that,\x01",
            "his vision narrowed...\x01",
            "It seems he's grown a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46D6")

    Jump("loc_52E1")

    label("loc_46DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4775")

    ChrTalk(
        0xFE,
        (
            "Hmm, for some reason there's been\x01",
            "fewer customers than usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess it can't be helped with\x01",
            "these back-to-back incidents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_4775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4801")

    ChrTalk(
        0xFE,
        "Even so, a cooking battle, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems both Nonno and Certeo\x01",
            "are serious about it, and\x01",
            "that's good enough for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_4801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B2")

    ChrTalk(
        0xFE,
        "Ambulances' sirens have been annoying me for a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of them, I couldn't hear the sound\x01",
            "of the fryer and burned the food a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_492D")

    label("loc_48B2")


    ChrTalk(
        0xFE,
        (
            "Don't misunderstand. I'd never\x01",
            "serve burned fries to a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to feed them to\x01",
            "that Certeo a bit later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492D")

    Jump("loc_52E1")

    label("loc_4932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_49FC")

    ChrTalk(
        0xFE,
        (
            "Hmm, Nonno's skills are a lot\x01",
            "better than when she first started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I'll need to hire someone new to manage the\x01",
            "dining room and bring her into the kitchen full time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_49FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B84")

    ChrTalk(
        0xFE,
        "Hehe, Wistoff knows his stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's using Certeo's feelings\x01",
            "towards Nonno's accomplishments\x01",
            "to further his abilities as a chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness, a cooking battle\x01",
            "one week from today, with\x01",
            "the position as cook on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With them both so motivated\x01",
            "like this, I'd like to have\x01",
            "both as chefs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, keep what I told you a secret from Certeo, eh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4BF2")

    label("loc_4B84")


    ChrTalk(
        0xFE,
        "Hehe, Wistoff knows his stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well Certeo seems pretty\x01",
            "motivated too, so I\x01",
            "think it's a good idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF2")

    Jump("loc_52E1")

    label("loc_4BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CA5")

    ChrTalk(
        0xFE,
        (
            "Ha ha. Though Nonno was\x01",
            "surprised by it, she has\x01",
            "plenty of motivation also.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, what a fresh feeling. It reminds\x01",
            "me of when I once trained as a chef.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_4CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4D08")

    ChrTalk(
        0xFE,
        (
            "Alright, tomorrow I'll resolutely\x01",
            "try to leave the cooking\x01",
            "preferably to Nonno.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E1")

    label("loc_4D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE4")

    ChrTalk(
        0xFE,
        (
            "This morning, Nonno asked\x01",
            "me about her bouillon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...It was better than I expected. I'm surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard she cooks at home... I'm going\x01",
            "to have her help me more often, I think.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E77")

    label("loc_4DE4")


    ChrTalk(
        0xFE,
        (
            "Hmm. She's really drawn out\x01",
            "the flavor of this boullion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard she cooks at home... I'm going\x01",
            "to have her help me more often, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E77")

    Jump("loc_52E1")

    label("loc_4E7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F46")

    ChrTalk(
        0xFE,
        (
            "Hmm, Wistoff too did\x01",
            "something drastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't think he'd ban\x01",
            "Certeo from the kitchen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, in his case,\x01",
            "maybe he'd never change\x01",
            "is he didn't do that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FB1")

    label("loc_4F46")


    ChrTalk(
        0xFE,
        (
            "Even so, that Certeo seems\x01",
            "he doesn't regret it at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does he understand\x01",
            "his current position?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FB1")

    Jump("loc_52E1")

    label("loc_4FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5188")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E1")

    ChrTalk(
        0xFE,
        (
            "In cooking, as with anything, you can't do\x01",
            "anything until you have the basics down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, in the world of painting, all the best\x01",
            "abstract artists are pretty good realists, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish that Certeo would come to\x01",
            "understand that sooner or later...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5183")

    label("loc_50E1")


    ChrTalk(
        0xFE,
        (
            "In cooking, as with anything, you can't do\x01",
            "anything until you have the basics down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish that Certeo would come to\x01",
            "understand that sooner or later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5183")

    Jump("loc_52E1")

    label("loc_5188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_52E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5267")

    ChrTalk(
        0xFE,
        (
            "I asked Certeo to make a\x01",
            "new menu before, but it\x01",
            "ended up a complete failure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That guy hasn't got a bad disposition, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, it'll be awhile\x01",
            "before he's a proper chef.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_52E1")

    label("loc_5267")


    ChrTalk(
        0xFE,
        (
            "That Certeo...\x01",
            "He hasn't got a bad disposition, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, it'll be awhile\x01",
            "before he's a proper chef.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E1")

    TalkEnd(0xFE)
    Return()

    # Function_9_4231 end

    def Function_10_52E5(): pass

    label("Function_10_52E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_547A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5409")

    ChrTalk(
        0xFE,
        (
            "Though I don't know what's going to\x01",
            "happen to this city, as a chef I can only\x01",
            "do one thing: provide delicious food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going forward the available ingredients will\x01",
            "be restricted, but I'll think of something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alllright! I gotta do my best today, too!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5475")

    label("loc_5409")


    ChrTalk(
        0xFE,
        (
            "A chef can only do one thing...\x01",
            "provide delicious food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alllright! I gotta do my best today, too!\x02",
    )

    CloseMessageWindow()

    label("loc_5475")

    Jump("loc_678A")

    label("loc_547A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5672")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CC")

    ChrTalk(
        0xFE,
        (
            "If the situation was different, I wouldn't\x01",
            "have realized how pathetic I am, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I understand what\x01",
            "Mr. Brown has been saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, chefs only exists\x01",
            "because of their customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm embarrassed to have been making\x01",
            "nothing but these complacent\x01",
            "dishes this whole time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_566D")

    label("loc_55CC")


    ChrTalk(
        0xFE,
        (
            "That's right, chefs only exists\x01",
            "because of their customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm embarrassed to have been making\x01",
            "nothing but these complacent\x01",
            "dishes this whole time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566D")

    Jump("loc_678A")

    label("loc_5672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_56F1")

    ChrTalk(
        0xFE,
        (
            "President Dieter's speech\x01",
            "was really impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I felt courage and pride\x01",
            "just listening to his words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_56F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5885")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57C8")

    ChrTalk(
        0xFE,
        "Man, the manager's a hard customer to deal with.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think he had no intention of declaring\x01",
            "a winner from the very start...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch. I have no idea why\x01",
            "I did all that hard work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5880")

    label("loc_57C8")


    ChrTalk(
        0xFE,
        (
            "Even though... Things sure\x01",
            "have gotten too dangerous lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I was thinking what good\x01",
            "fortune I have to be able to continue to\x01",
            "work here normally like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5880")

    Jump("loc_678A")

    label("loc_5885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_590A")

    ChrTalk(
        0xFE,
        (
            "An occupation incident... \x01",
            "Terrifying, but utterly preposterous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's so fun about\x01",
            "ruling people by force?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_590A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FF")

    ChrTalk(
        0xFE,
        (
            "Damn, while I'm not even deciding\x01",
            "what to make, time will end up passing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to hurry and pull\x01",
            "together my pasta sauce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I go with tomato or cream base?\x01",
            "Or perhaps something else altogether?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A7B")

    label("loc_59FF")


    ChrTalk(
        0xFE,
        (
            "Aargh, I mean, what's\x01",
            "an unknown sauce!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I feel like I'm becoming\x01",
            "more aware of my weak points somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A7B")

    Jump("loc_678A")

    label("loc_5A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5AC3")

    ChrTalk(
        0xFE,
        "Hmm? It's pretty noisy outside for some reason.\x02",
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_5AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")

    ChrTalk(
        0xFE,
        (
            "Anyway, though flavor is important,\x01",
            "for food, appearance is critical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, if we're talking about the decisive theme this time...\x01",
            "Brand-newness doesn't seem to be important, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, I think I'll keep\x01",
            "the standard menu and\x01",
            "add something to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5C79")

    label("loc_5BE8")


    ChrTalk(
        0xFE,
        (
            "*sigh*, but the more I think about it,\x01",
            "the more I hate the word "standard."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, if it's standard, it's\x01",
            "got to be delicious, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C79")

    Jump("loc_678A")

    label("loc_5C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D27")

    ChrTalk(
        0xFE,
        (
            "...I can't believe I'm going to have\x01",
            "a cooking battle with Nonno.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, a delicious pasta dish, huh... \x01",
            "First, I'll ponder about what to make.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_5D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DDF")

    ChrTalk(
        0xFE,
        (
            "N-Nonno cooking? Hasn't this turn\x01",
            "of events been too quick...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, I'll be out of a\x01",
            "job at this rate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No, no, no, that'll\x01",
            "never happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5E5C")

    label("loc_5DDF")


    ChrTalk(
        0xFE,
        (
            "No matter how well she can cook, it's too\x01",
            "early to be serving her food to customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wait, what about my position?\x02",
    )

    CloseMessageWindow()

    label("loc_5E5C")

    Jump("loc_678A")

    label("loc_5E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5F21")

    ChrTalk(
        0xFE,
        (
            "I hadn't noticed at all, however,\x01",
            "before I knew, Nonno was able to be\x01",
            "entrusted with preparations too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me that at this rate\x01",
            "she's gonna become a cook, eh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_5F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_60C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6013")

    ChrTalk(
        0xFE,
        (
            "Welcome. If you're here to eat,\x01",
            "feel free to sit at any open table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because we're not too busy, I can even show you to\x01",
            "the reserved seating on the second floor, if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ask me whatever you want.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_60BC")

    label("loc_6013")


    ChrTalk(
        0xFE,
        (
            "Man, I never expected that being\x01",
            "a waiter would be this much fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Customers... Especially our\x01",
            "attractive female customers, are\x01",
            "an irreplaceable energy source.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60BC")

    Jump("loc_678A")

    label("loc_60C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6296")

    ChrTalk(
        0xFE,
        (
            "The manager told me to be\x01",
            "a waiter for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what he's planning, but this\x01",
            "kind of work is good every once in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can look at the female customers\x01",
            "all I want, and pick them up too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Picking up female customers... \x01",
            "That isn't good.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Being looked at is\x01",
            "pretty unsettling too.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_633B")

    label("loc_6296")


    ChrTalk(
        0xFE,
        (
            "I don't know the manager's planning, but\x01",
            "being a waiter is good every once in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can look at the female customers\x01",
            "all I want, and pick them up too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_633B")

    Jump("loc_678A")

    label("loc_6340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63D9")

    ChrTalk(
        0xFE,
        (
            "Cuisine is art. \x01",
            "And creativity counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it's time for the new\x01",
            "menu, I'll create one that\x01",
            "will shock the world.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_647F")

    label("loc_63D9")


    ChrTalk(
        0xFE,
        (
            "By the way, my current customers are those\x01",
            "two girls at the table near the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I've been waiting for this.\x01",
            "I'll bring out their food right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_647F")

    Jump("loc_678A")

    label("loc_6484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_678A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65B7")

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder just where\x01",
            "my new menu went wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The flavor and appearance were\x01",
            "in place, and the bone chilling\x01",
            "food texture was out of this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F("Bone chilling food texture"...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(I don't really get it, but I\x01",
            "don't think I want to try it...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_678A")

    label("loc_65B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_672A")

    ChrTalk(
        0xFE,
        (
            ""Marshlands' Monster Eyes Abaddon Stew"...\x01",
            "I thought I was breaking new culinary ground...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6647")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6647")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_666D")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_666D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6693")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6693")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66B9")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_66B9")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F(W-What an amazing name...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Hu hu, seems like a really\x01",
            "strange combination.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_678A")

    label("loc_672A")


    ChrTalk(
        0xFE,
        (
            ""Marshlands' Monster Eyes Abaddon Stew"...\x01",
            "I thought I was breaking new culinary ground...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_678A")

    TalkEnd(0xFE)
    Return()

    # Function_10_52E5 end

    def Function_11_678E(): pass

    label("Function_11_678E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6820")

    ChrTalk(
        0xFE,
        (
            "Uh uh, Mr. Certeo seems\x01",
            "to be in good spirits today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a very tense situation, but...\x01",
            "He cheered me up a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_6820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_68FE")

    ChrTalk(
        0xFE,
        (
            "This strange situation in the city\x01",
            "right now... The government's\x01",
            "did it of its own accord?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they had told the public about the\x01",
            "circumstances in detail sooner, \x01",
            "it wouldn't have been as chaotic...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_68FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_69A4")

    ChrTalk(
        0xFE,
        (
            "I thought the presidential\x01",
            "address was amazing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like the manager says, there are too many\x01",
            "concerning points, so I'm not sure about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_69A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6A78")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69D6")
    Call(0, 43)
    Return()

    label("loc_69D6")


    ChrTalk(
        0xFE,
        (
            "It's only been a month, but it's\x01",
            "been fun working in the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The manager too told me, but...\x01",
            "I guess I'll try seriously\x01",
            "to become a chef now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_6A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6ADD")

    ChrTalk(
        0xFE,
        "The people of Mainz... I'm worried about them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if they're hungry...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_6ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7F")

    ChrTalk(
        0xFE,
        (
            "It seems Mr. Certeo is\x01",
            "thinking hard about his\x01",
            "cooking battle recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Me? I'm simply planning on just\x01",
            "using my usual dishes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C09")

    label("loc_6B7F")


    ChrTalk(
        0xFE,
        (
            "Carbonara is my pasta specialty.\x01",
            "I often make it for my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, I was thinking of making\x01",
            "it for the cooking battle too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C09")

    Jump("loc_7681")

    label("loc_6C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C7D")

    ChrTalk(
        0xFE,
        (
            "Those sirens' sounds\x01",
            "carry really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I could hear them clearly even in the kitchen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_6C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D08")

    ChrTalk(
        0xFE,
        "Hm, hm-hmm♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Basil, pepper and\x01",
            "a pinch of salt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, that should do it\x01",
            "for the meat seasoning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D70")

    label("loc_6D08")


    ChrTalk(
        0xFE,
        "Hm, hm-hmm♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next, I'll let it sit for 30 minutes...\x01",
            "During that time, I'll chop the veggies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D70")

    Jump("loc_7681")

    label("loc_6D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F00")

    ChrTalk(
        0xFE,
        (
            "I should be going back to the\x01",
            "dining area before long, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I asked the manager and he agreed to let\x01",
            "me work in the kitchen awhile longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, I decided to go \x01",
            "along with his holding a cooking\x01",
            "battle for Mr. Certeo's future...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. I feel bad since Mr.Certeo\x01",
            "seems to have been tricked into this,\x01",
            "but it seems fun so I've accepted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6FC2")

    label("loc_6F00")


    ChrTalk(
        0xFE,
        (
            "Though I only cooked before as an extension\x01",
            "of my housekeeping duties, working in a\x01",
            "kitchen like this is quite fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, being this the case, I might\x01",
            "seriously aim to become a chef.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FC2")

    Jump("loc_7681")

    label("loc_6FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_70FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A4")

    ChrTalk(
        0xFE,
        (
            "Mr. Brown suddenly decided to leave\x01",
            "this morning's prep work to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I myself wonder if it will really be all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "O-Of course, I'll do my best to\x01",
            "live up to his expectations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_70F7")

    label("loc_70A4")


    ChrTalk(
        0xFE,
        (
            "Hmm, first up is seasoning\x01",
            "the ingredients, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, I'm so nervous.\x02",
    )

    CloseMessageWindow()

    label("loc_70F7")

    Jump("loc_7681")

    label("loc_70FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_718F")

    ChrTalk(
        0xFE,
        (
            "After I'm done with the preparations,\x01",
            "I'll have to wash the dishes next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*phew*...it's really busy\x01",
            "during our dinner time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_718F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_722D")

    ChrTalk(
        0xFE,
        (
            "Hmm. These vegetables \x01",
            "cook slowly, so maybe it's\x01",
            "better to score them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*score, score*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There, that should do it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7274")

    label("loc_722D")


    ChrTalk(
        0xFE,
        "*chopchopchopchop*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hm, so this is how fine chopping goes.\x02",
    )

    CloseMessageWindow()

    label("loc_7274")

    Jump("loc_7681")

    label("loc_7279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_731E")

    ChrTalk(
        0xFE,
        (
            "It was decided that I'd help out in the\x01",
            "kitchen for a bit instead of Mr. Certeo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's simply\x01",
            "dishwashing and some\x01",
            "simple prep work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7681")

    label("loc_731E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_749E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741D")

    ChrTalk(
        0xFE,
        (
            "Mr. Certeo is always dashing\x01",
            "out of the kitchen to check on\x01",
            "the seats at the tables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if today, again, he's planning to choose\x01",
            "the dishes by himself although no one asked him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, he's a stubborn one.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7499")

    label("loc_741D")


    ChrTalk(
        0xFE,
        (
            "Mr. Certeo is always dashing\x01",
            "out of the kitchen to check on\x01",
            "the seats at the tables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, he's a stubborn one.\x02",
    )

    CloseMessageWindow()

    label("loc_7499")

    Jump("loc_7681")

    label("loc_749E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B8")

    ChrTalk(
        0xFE,
        (
            "Miss Flote sitting further in\x01",
            "is one of our regulars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not rare for her to\x01",
            "come right when the store\x01",
            "opens and stay all day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, she is considerate. She\x01",
            "gives up her seat during busy hours\x01",
            "and puts in orders throughout the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7681")

    label("loc_75B8")


    ChrTalk(
        0xFE,
        (
            "It's not rare for Miss Flote to\x01",
            "come right when the store\x01",
            "opens and stay all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although, she is considerate. She\x01",
            "gives up her seat during busy hours\x01",
            "and puts in orders throughout the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7681")

    TalkEnd(0xFE)
    Return()

    # Function_11_678E end

    def Function_12_7685(): pass

    label("Function_12_7685")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_77D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7744")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A pale azure tree, eh...?\x01",
            "Sometimes it's hard to tell fantasy\x01",
            "from reality these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Maybe I'll have a\x01",
            "little more caffeine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_77D0")

    label("loc_7744")


    ChrTalk(
        0xFE,
        (
            "A pale azure tree, eh...?\x01",
            "Sometimes it's hard to tell fantasy\x01",
            "from reality these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Maybe I'll have a\x01",
            "little more caffeine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77D0")

    Jump("loc_8A6F")

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_79F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_793C")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Just when I was going to the restroom,\x01",
            "mist appeared and now I can't go outside?\x01",
            "What is the meaning of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or, perhaps I should ask why\x01",
            "those human shaped weapons\x01",
            "are patrolling the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if they're doing it to protect the\x01",
            "city from the two major powers,\x01",
            "we need a proper explanation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_79EC")

    label("loc_793C")


    ChrTalk(
        0xFE,
        (
            "We need a proper explanation\x01",
            "for the "Aion" weapons and the\x01",
            "barrier covering the city, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if they are protecting\x01",
            "us or putting us in even more danger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79EC")

    Jump("loc_8A6F")

    label("loc_79F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7BED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B14")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter of the Independent State of\x01",
            "Crossbell and Secretary of Defense Arios, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The names and titles are great, but I\x01",
            "wonder if they can really protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It won't be a laughing matter\x01",
            "if they're just posing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7BE8")

    label("loc_7B14")


    ChrTalk(
        0xFE,
        (
            "The Independent State, the President and the\x01",
            "Secretary of Defense... The names and titles are\x01",
            "great, but I wonder if they can really protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It won't be a laughing matter\x01",
            "if they're just posing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BE8")

    Jump("loc_8A6F")

    label("loc_7BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D1D")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attack the other day has got the\x01",
            "independence supporters in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how they feel, but I wonder\x01",
            "if we can have a more logical discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""To act on emotions is to be ruined..."\x01",
            "Hmm, I have the feeling someone said that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7E1D")

    label("loc_7D1D")


    ChrTalk(
        0xFE,
        (
            "The attack the other day has got the\x01",
            "independence supporters in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how they feel, but I wonder\x01",
            "if we can have a more logical discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""To act on emotions is to be ruined..."\x01",
            "Hmm, I have the feeling someone said that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E1D")

    Jump("loc_8A6F")

    label("loc_7E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7F09")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group in Mainz... \x01",
            "Though it's just a rumor,\x01",
            "it's probably some Imperial scheme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Instead of help, approve the garrisoning of troops!"...\x01",
            "It's no joke. That's what they'd actually demand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A6F")

    label("loc_7F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8048")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8003")

    ChrTalk(
        0xFE,
        (
            "A civic forum is going to be hold at\x01",
            "the City Meeting Hall this morning\x01",
            "with state independence as the theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even without attending, I get the\x01",
            "main idea of independence, but\x01",
            "perhaps I'll make a brief appearance?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8043")

    label("loc_8003")


    ChrTalk(
        0xFE,
        (
            "A civic forum, huh... \x01",
            "Maybe I'll make a brief appearance?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8043")

    Jump("loc_8A6F")

    label("loc_8048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_80A4")

    ChrTalk(
        0xFE,
        "It's rather noisy outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't drink my coffee in peace at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A6F")

    label("loc_80A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_819E")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The opening day of the Arc-en-ciel renewal\x01",
            "performance is the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to get myself tickets, but...\x01",
            "The ones for the next two months were\x01",
            "sold out in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8210")

    label("loc_819E")


    ChrTalk(
        0xFE,
        (
            "*sigh*... Well it's\x01",
            "not like I'll die\x01",
            "if I don't see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, but I want to see it so much I could die.\x02",
    )

    CloseMessageWindow()

    label("loc_8210")

    Jump("loc_8A6F")

    label("loc_8215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_83A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82BC")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "State independence, huh.\x01",
            "It won't be so simple if we choose it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "In any case, I'm worried about our security.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_83A3")

    label("loc_82BC")


    ChrTalk(
        0xFE,
        (
            "Personally, I don't think accepting the\x01",
            "Empire and Republic's security guarantee\x01",
            "would be completely a bad thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, our history being what it is, it's guaranteed\x01",
            "that it won't be as simple as they're thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83A3")

    Jump("loc_8A6F")

    label("loc_83A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_84B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_844E")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even so, security in the city is strict.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all these police around, \x01",
            "I can't even take a leisurely walk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_84AD")

    label("loc_844E")


    ChrTalk(
        0xFE,
        "That's why I came here to calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "pass the day by reading.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84AD")

    Jump("loc_8A6F")

    label("loc_84B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_85A4")

    ChrTalk(
        0xFE,
        (
            "*sigh*, today I unconsciously read with a lot of zeal and\x01",
            "after a long time, I ended up staying until the sun set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since as you can imagine this is bad toward the people\x01",
            "of the store, I think I'll eat dinner too here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A6F")

    label("loc_85A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8698")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though you can't see the\x01",
            "inauguration ceremony from up close,\x01",
            "everyone's going outside anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for me, I plan to just sit\x01",
            "here, coffee in one hand,\x01",
            "Crossbell Times in the other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_875C")

    label("loc_8698")


    ChrTalk(
        0xFE,
        (
            "Even though you can't see the\x01",
            "inauguration ceremony from up close,\x01",
            "everyone's going outside anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for me, I plan to just sit\x01",
            "here, coffee in one hand,\x01",
            "Crossbell Times in the other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_875C")

    Jump("loc_8A6F")

    label("loc_8761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_87C1")

    ChrTalk(
        0xFE,
        (
            "Why is that annoying cook\x01",
            "taking my order today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't understand it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A6F")

    label("loc_87C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A0")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The store has a different atmosphere\x01",
            "than usual when it's raining outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sounds of the store mix together with that\x01",
            "of the rain. I think this is the best BGM.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_894F")

    label("loc_88A0")


    ChrTalk(
        0xFE,
        (
            "The store has a different atmosphere\x01",
            "than usual when it's raining outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sounds of the store mix together with that\x01",
            "of the rain. I think this is the best BGM.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_894F")

    Jump("loc_8A6F")

    label("loc_8954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A17")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, this store is really\x01",
            "great for reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a moderate level of noise, and coffee\x01",
            "as well, to wipe away that drowsy feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8A6F")

    label("loc_8A17")


    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll finish reading this\x01",
            "book I borrowed from the library today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A6F")

    TalkEnd(0xFE)
    Return()

    # Function_12_7685 end

    def Function_13_8A73(): pass

    label("Function_13_8A73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8AF5")

    ChrTalk(
        0xFE,
        (
            "Nooo, I hadn't heard that\x01",
            "it would rain today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why would it have to rain on\x01",
            "our long awaited vacation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B47")

    label("loc_8AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8B47")

    ChrTalk(
        0xFE,
        (
            "Right, and the prices aren't too bad.\x01",
            "I think I could get addicted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B47")

    TalkEnd(0xFE)
    Return()

    # Function_13_8A73 end

    def Function_14_8B4B(): pass

    label("Function_14_8B4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8BFE")

    ChrTalk(
        0xFE,
        (
            "Yeah, yeah I got it, but don't\x01",
            "involve me in your grumbles too, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it rains, you just have to think of\x01",
            "a way to enjoy yourself indoors, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C65")

    label("loc_8BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8C65")

    ChrTalk(
        0xFE,
        (
            "This store is relatively\x01",
            "plain but the food is a\x01",
            "different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I like it.\x02",
    )

    CloseMessageWindow()

    label("loc_8C65")

    TalkEnd(0xFE)
    Return()

    # Function_14_8B4B end

    def Function_15_8C69(): pass

    label("Function_15_8C69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8C9A")

    ChrTalk(
        0xFE,
        "Uh uh honey, you're sweet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D01")

    label("loc_8C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8D01")

    ChrTalk(
        0xFE,
        (
            "Thank you for reserving\x01",
            "seats for me, honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you for always being kind to me.\x02",
    )

    CloseMessageWindow()

    label("loc_8D01")

    TalkEnd(0xFE)
    Return()

    # Function_15_8C69 end

    def Function_16_8D05(): pass

    label("Function_16_8D05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8D6E")

    ChrTalk(
        0xFE,
        "Wahaha, is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I don't think it's as\x01",
            "good as your home cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DD9")

    label("loc_8D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8DD9")

    ChrTalk(
        0xFE,
        "Wahaha, it's nothing, you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thank you too.\x01",
            "Thank you for all\x01",
            "that you do at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD9")

    TalkEnd(0xFE)
    Return()

    # Function_16_8D05 end

    def Function_17_8DDD(): pass

    label("Function_17_8DDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E6F")

    ChrTalk(
        0xFE,
        (
            "I'll open the menu, suddenly point\x01",
            "to something and say, "I want this!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright, first I need to close my eyes, and...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F2B")

    label("loc_8E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8E7D")
    Jump("loc_8F2B")

    label("loc_8E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8EE8")

    ChrTalk(
        0xFE,
        "Alright, I'm having fish today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? But they're having\x01",
            "this special today, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F2B")

    label("loc_8EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F2B")

    ChrTalk(
        0xFE,
        (
            "Hmm, what to do. Hmm, I\x01",
            "could have either of them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F2B")

    TalkEnd(0xFE)
    Return()

    # Function_17_8DDD end

    def Function_18_8F2F(): pass

    label("Function_18_8F2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8F7A")

    ChrTalk(
        0xFE,
        (
            "Dear... Either is fine, so\x01",
            "would you decide already?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_901F")

    label("loc_8F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8F88")
    Jump("loc_901F")

    label("loc_8F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8FCC")

    ChrTalk(
        0xFE,
        "*sigh*. You're really indecisive, you know that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_901F")

    label("loc_8FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_901F")

    ChrTalk(
        0xFE,
        (
            "Dear... Would you hurry up and pick\x01",
            "already? I've already decided...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_901F")

    TalkEnd(0xFE)
    Return()

    # Function_18_8F2F end

    def Function_19_9023(): pass

    label("Function_19_9023")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9097")

    ChrTalk(
        0xFE,
        (
            "Eeh, isn't this different from what\x01",
            "yous said the very first day?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, that's so uncool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9160")

    label("loc_9097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_90A5")
    Jump("loc_9160")

    label("loc_90A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9127")

    ChrTalk(
        0xFE,
        "*crunch, munch*... Mmm, this is happiness itself♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I knew it. The food is the best thing about traveling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9160")

    label("loc_9127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9160")

    ChrTalk(
        0xFE,
        (
            "Uh uh, hooray♪\x01",
            "That's the darling I love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9160")

    TalkEnd(0xFE)
    Return()

    # Function_19_9023 end

    def Function_20_9164(): pass

    label("Function_20_9164")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9204")

    ChrTalk(
        0xFE,
        (
            "H-Hmm. It pains me to say\x01",
            "it but I'm barely scraping\x01",
            "by on my travel budget...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, if possible, I'd like\x01",
            "to see their budget menu...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_932C")

    label("loc_9204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9212")
    Jump("loc_932C")

    label("loc_9212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_92B3")

    ChrTalk(
        0xFE,
        (
            "Hmm, but there's just one\x01",
            "expensive item after the next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Well,we're on a long awaited vacation...\x01",
            "Let's not sweat the small details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_932C")

    label("loc_92B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_932C")

    ChrTalk(
        0xFE,
        (
            "So, just order all the food\x01",
            "you like with no hesitation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We're on a long awaited vacation, after all.\x02",
    )

    CloseMessageWindow()

    label("loc_932C")

    TalkEnd(0xFE)
    Return()

    # Function_20_9164 end

    def Function_21_9330(): pass

    label("Function_21_9330")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9395")

    ChrTalk(
        0xFE,
        (
            "Hmm, I can't believe something like this\x01",
            "happened during my trip to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B3")

    label("loc_9395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9407")

    ChrTalk(
        0xFE,
        (
            "Hmm. For today, I think I'll\x01",
            "give up walking the highways and\x01",
            "go shopping in the city instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B3")

    label("loc_9407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9476")

    ChrTalk(
        0xFE,
        (
            "Ambulances, eh?\x01",
            "It doesn't seem there were sick people\x01",
            "since many of them have passed by...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B3")

    label("loc_9476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_94F2")

    ChrTalk(
        0xFE,
        (
            "Today too I'll tour\x01",
            "many places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First off, I'll visit the orbal store\x01",
            "to stock up on photo Quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95B3")

    label("loc_94F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_95B3")

    ChrTalk(
        0xFE,
        (
            "I was thinking of where I'd like to visit when I\x01",
            "thought how safe it's been in Crossbell lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Coming here was the right choice.\x01",
            "My girlfriend is having a great time, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95B3")

    TalkEnd(0xFE)
    Return()

    # Function_21_9330 end

    def Function_22_95B7(): pass

    label("Function_22_95B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9657")

    ChrTalk(
        0xFE,
        (
            "We had planned to go see Mainz\x01",
            "today, but... There's no way\x01",
            "we can go in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I'm worried about all the citizens.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9854")

    label("loc_9657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_96F0")

    ChrTalk(
        0xFE,
        (
            "*sigh*. Man, why'd it have\x01",
            "to rain on the day we're\x01",
            "going to see the outskirts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could I be a rain woman?\x01",
            "...Or is he a rain man?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9854")

    label("loc_96F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9734")

    ChrTalk(
        0xFE,
        (
            "Those were ambulances.\x01",
            "What could have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9854")

    label("loc_9734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_97D9")

    ChrTalk(
        0xFE,
        (
            "Yesterday I took photos of Orchis\x01",
            "Tower from various places in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, before I realized it, I had\x01",
            "used up both of my photo Quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9854")

    label("loc_97D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9854")

    ChrTalk(
        0xFE,
        "Uh uh, Crossbell is a nice place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to see as much of it as possible \x01",
            "and make some good memories.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9854")

    TalkEnd(0xFE)
    Return()

    # Function_22_95B7 end

    def Function_23_9858(): pass

    label("Function_23_9858")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_98DD")

    ChrTalk(
        0xFE,
        (
            "I totally agree with\x01",
            "President Dieter's address!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We citizens too must do all\x01",
            "we can to support Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9966")

    label("loc_98DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9966")

    ChrTalk(
        0xFE,
        (
            "It seems like that raid incident\x01",
            "was the Empire's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't forgive them. What on\x01",
            "earth could they be planning!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9966")

    TalkEnd(0xFE)
    Return()

    # Function_23_9858 end

    def Function_24_996A(): pass

    label("Function_24_996A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9A3D")

    ChrTalk(
        0xFE,
        (
            "Independence, huh...\x01",
            "Of course things will be tough from now on,\x01",
            "but it doesn't feel bad now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think we'll finally gain\x01",
            "true freedom, courage wells up\x01",
            "in the depths of my heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B02")

    label("loc_9A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9B02")

    ChrTalk(
        0xFE,
        (
            "To think they employed an armed\x01",
            "group to attack the city...\x01",
            "What a dirty thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though we forget it from time\x01",
            "to time, the Erebonian Empire\x01",
            "is an extremely warlike nation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B02")

    TalkEnd(0xFE)
    Return()

    # Function_24_996A end

    def Function_25_9B06(): pass

    label("Function_25_9B06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1B")
    Call(0, 30)
    Jump("loc_9D62")

    label("loc_9B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D2D")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BB6")
    Jump("loc_9C00")

    label("loc_9BB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9BD6")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C00")

    label("loc_9BD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BF6")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C00")

    label("loc_9BF6")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C00")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#02306FGuh, that chief having me watched 24\x01",
            "hours a day... How annoying can he get?\x02\x03",
            "#02310FI'll remember this, Tio...!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#00203FAlright, let's go, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#02306FH-Hey, don't ignore me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F(T-That's Tio for you...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    Jump("loc_9D62")

    label("loc_9D2D")

    SetChrSubChip(0x19, 0x0)

    ChrTalk(
        0x19,
        (
            "#02306FF-Fine... \x01",
            "I'll eat them by myself!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D62")

    TalkEnd(0xFE)
    Return()

    # Function_25_9B06 end

    def Function_26_9D66(): pass

    label("Function_26_9D66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D7B")
    Call(0, 30)
    Jump("loc_9FD1")

    label("loc_9D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5B")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E16")
    Jump("loc_9E60")

    label("loc_9E16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E60")

    label("loc_9E36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E60")

    label("loc_9E56")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E60")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Don't worry about me, Tio!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take responsibility\x01",
            "for looking after Jona.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 500)

    ChrTalk(
        0x103,
        "#00202FThank you, chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I feel like Tio's relations\x01",
            "with the chief have improved...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_9FD1")

    label("loc_9F5B")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Now now, Jona! Green peppers and \x01",
            "carrots are delicious too, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, will you say\x01",
            ""aaah" for me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FD1")

    TalkEnd(0xFE)
    Return()

    # Function_26_9D66 end

    def Function_27_9FD5(): pass

    label("Function_27_9FD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0DB")

    ChrTalk(
        0xFE,
        (
            "As city staff I was guiding\x01",
            "others to the shelter, so I\x01",
            "couldn't take shelter myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anticipating that,\x01",
            "my wife and Mimi\x01",
            "came to get me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd prioritize their\x01",
            "own safety and stay put, but\x01",
            "I'm glad to have them here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A19F")

    label("loc_A0DB")


    ChrTalk(
        0xFE,
        (
            "I wish they'd prioritize their\x01",
            "own safety and stay put, but\x01",
            "I'm glad to have them here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The restaurant's people are warm\x01",
            "and inviting. It helps lighten\x01",
            "the mood a bit in this situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19F")

    TalkEnd(0xFE)
    Return()

    # Function_27_9FD5 end

    def Function_28_A1A3(): pass

    label("Function_28_A1A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2B2")

    ChrTalk(
        0xFE,
        (
            "My husband was late coming home,\x01",
            "so I came to get him, but...\x01",
            "That mist is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems those weird dolls\x01",
            "recognize citizens and\x01",
            "don't attack them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's hard to put into\x01",
            "words the fear you feel\x01",
            "when you see one of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_A309")

    label("loc_A2B2")


    ChrTalk(
        0xFE,
        (
            "Uh uh, but kids are really\x01",
            "cute aren't they. Even in\x01",
            "this situation, she's happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A309")

    TalkEnd(0xFE)
    Return()

    # Function_28_A1A3 end

    def Function_29_A30D(): pass

    label("Function_29_A30D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "You know, you know?\x01",
            "The store people treated\x01",
            "Mimi and everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It was really really delicious.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_A30D end

    def Function_30_A37E(): pass

    label("Function_30_A37E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3800, 6500, 14680, 0)
    MoveCamera(44, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21010, 0)
    SetChrPos(0x103, -3900, 5000, 16250, 90)
    SetChrPos(0x101, -3900, 5000, 14750, 90)
    SetChrPos(0x102, -3900, 5000, 13250, 45)
    SetChrPos(0x104, -5120, 5000, 13150, 45)
    SetChrPos(0x109, -5110, 5000, 16160, 90)
    SetChrPos(0x105, -5110, 5000, 14750, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    OP_0D()
    SetChrSubChip(0x1A, 0x1)

    ChrTalk(
        0x1A,
        (
            "#11PAh, it's Tio, and\x01",
            "everyone else, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A4FA")
    Jump("loc_A544")

    label("loc_A4FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A51A")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A544")

    label("loc_A51A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A53A")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A544")

    label("loc_A53A")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A544")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        "#5P#02302FHey, it's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FChief Roberts, and Jona.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FDid you come here to eat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PYeah. I want Jona here\x01",
            "to eat a balanced diet\x01",
            "every once in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PIt seems he ate nothing\x01",
            "but pizza while at\x01",
            "Leman's Foundation HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00203FYeah, I can believe that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FNow that you say that, it seems\x01",
            "he hardly touched his veggies.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x19, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00105FIndeed. The green peppers\x01",
            "and carrots are left...\x02\x03",
            "#00106FJona, it's not good to be picky.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x102, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7F2")
    Jump("loc_A83C")

    label("loc_A7F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A812")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A83C")

    label("loc_A812")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A832")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A83C")

    label("loc_A832")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A83C")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#5P#02306FHmph, I'll eat what I want.\x02\x03",
            "Coming to a restaurant like this,\x01",
            "eating with a knife and fork...\x01",
            "It's all just a waste of time.\x02\x03",
            "#02309FPizza is easier to eat when\x01",
            "operating a terminal...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    ChrTalk(
        0x1A,
        (
            "#11PI-It can't be... You mean to\x01",
            "say these delicious vegetables\x01",
            "don't suit your palate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PAh, this is all my fault!\x01",
            "And I only wanted to get Jona\x01",
            "something good to eat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PI know! I'll gather chefs from\x01",
            "throughout the continent, and create a\x01",
            "vegetable dish even Jona could eat!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    OP_63(0x19, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#5P#02301F...Ah, enough already!\x01",
            "This is why you're so annoying!\x02\x03",
            "I just have to eat without\x01",
            "being picky right? I'll do it!\x02\x03",
            "#02306F*glom*... Ugh, how bitter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FAhaha, he's the same as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206F...Really now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACA1")
    Jump("loc_ACEB")

    label("loc_ACA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACC1")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACEB")

    label("loc_ACC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACE1")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACEB")

    label("loc_ACE1")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ACEB")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#5P#02305F*crunch, munch*...*gulp*...\x01",
            "There, see?\x02\x03",
            "#02301FDo you guys know where the\x01",
            ""Fool" connected with that\x01",
            "Michelam incident went?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AE11():
        TurnDirection(0x0, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_AE11)
    Sleep(50)

    def lambda_AE21():
        TurnDirection(0x1, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_AE21)
    Sleep(50)

    def lambda_AE31():
        TurnDirection(0x2, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_AE31)
    Sleep(50)

    def lambda_AE41():
        TurnDirection(0x3, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_AE41)
    Sleep(50)

    def lambda_AE51():
        TurnDirection(0x4, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_AE51)
    Sleep(50)

    def lambda_AE61():
        TurnDirection(0x5, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x5, 0, lambda_AE61)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    WaitChrThread(0x4, 0)
    WaitChrThread(0x5, 0)

    ChrTalk(
        0x101,
        "#6P#00003F...No, no idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108F(We did see him at Michelam, but... \x01",
            "We didn't tell anyone\x01",
            "about it, right?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#02306FTch, so that's how it is... Well all right.\x02\x03",
            "#02310FThat "Fool" has been showing up on the\x01",
            "orbal net ever since the tower incident.\x02\x03",
            "I'll have to pay him back\x01",
            "for making a total mess\x01",
            "out of my base...\x02\x03",
            "Tell me if you hear\x01",
            "anything about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FHmm, we can't promise\x01",
            "you that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#02306FHow stingy... If you just\x01",
            "put it in the database,\x01",
            "that will be fine.\x02\x03",
            "#02309FI'll hack in later and\x01",
            "take a look at it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#00306FWhoa, hey now...\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#6P#00206F...It seems that you are being taken care\x01",
            "from the IBC branch office now, so I\x01",
            "think you should behave a little.\x02\x03",
            "#00200FChief, I would like you to\x01",
            "keep a close eye on Jona.\x02\x03",
            "#00203FWe can't overlook over hacking\x01",
            "now that the orbal net basic\x01",
            "law has gone into effect.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x1)

    ChrTalk(
        0x1A,
        "#11PI-I know that, Tio!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    ChrTalk(
        0x1A,
        (
            "#11PJona, I'll take responsibility for you\x01",
            "and watch over you 24 hours a day!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#5P#02305FH-Hey, Tio! Isn't that\x01",
            "a little too cruel!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    ChrTalk(
        0x103,
        "#5P#00203FThen, let's go, everyone.\x02",
    )

    CloseMessageWindow()

    def lambda_B393():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B393)
    Sleep(50)

    def lambda_B3A3():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B3A3)
    Sleep(50)

    def lambda_B3B3():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B3B3)
    Sleep(50)

    def lambda_B3C3():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B3C3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12P#00005FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302F(Hu hu, she tactfully forced that on the chief.)\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x0, -3900, 5000, 14750, 180)
    SetScenarioFlags(0x16B, 1)
    EventEnd(0x5)
    Return()

    # Function_30_A37E end

    def Function_31_B471(): pass

    label("Function_31_B471")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -440, 5000, 17810, 225)
    SetChrPos(0x102, 120, 5000, 17030, 270)
    SetChrPos(0x104, -480, 5000, 18810, 225)
    SetChrPos(0x109, 750, 5000, 18280, 225)
    SetChrPos(0x105, 150, 5000, 16110, 270)
    LoadChrToIndex("chr/ch13300.itc", 0x1E)
    SetChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12000.itp")
    OP_68(-1200, 6500, 17340, 0)
    MoveCamera(19, 31, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22980, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x104,
        "#11P#00305FOoh, it's Miss Kilika!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLong time no see, Miss Kilika.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12002FMy, it's you guys...\x02\x03",
            "#12004FUh uh, good day to you all.\x01",
            "Fancy seeing you here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003FWe asked if anyone had seen\x01",
            "you and ended up here.\x02\x03",
            "#00001FYou were at that "auktion",\x01",
            "weren't you. ...Rocksmith Agency\x01",
            "Section Chief Miss Kilika Rouran.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1E,
        (
            "That's right. The situation was\x01",
            "different last time we met. Allow\x01",
            "me to introduce myself once again.\x02\x03",
            "I am Kilika Rouran, aide\x01",
            "to the President of the\x01",
            "Republic of Calvard.\x02\x03",
            "I have other titles too, but...\x01",
            "Well, nothing to speak about.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#00100FSo why did you say you were an\x01",
            "entertainment producer last time, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6P#12004FUh uh, that is another\x01",
            "of my many titles.\x02\x03",
            "#12002FMy office is in the\x01",
            "Republic, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see. So you really\x01",
            "weren't lying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu, a female spy who\x01",
            "properly uses many faces.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00309F(Hmm, I love the mysterious\x01",
            "Miss Kilika too, I guess.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(That kind of comment isn't\x01",
            "what we need right now, senior...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBy the way, what is a presidential\x01",
            "aide such as yourself doing in a\x01",
            "place like this?\x02\x03",
            "I heard President Rocksmith\x01",
            "was taking a tour of the\x01",
            "IBC building today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12004FThat same President had me\x01",
            "do a little errand for him.\x02\x03",
            "#12000FThough I'm shopping incognito, \x01",
            "I decided to have a\x01",
            "leisurely lunch here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAn errand...you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6P#12004FIt's this.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kilika took out a pinwheel\x01",
            "and blew on it.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The blades of the pinwheel spun round.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10105FA-A pinwheel...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12000FCatching a glimpse of the stall from our passing\x01",
            "limousine, it seemed he greatly desired one.\x02\x03",
            "Before tomorrow's main session,\x01",
            "it seems he wanted one to\x01",
            "help himself relax.\x02\x03",
            "#12004FAnd also, together with some fruit\x01",
            "as dessert for tonight's dinner party.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#11P#00306FH-Hmm... I guess you\x01",
            "really are on an errand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, that really suits President Rocksmith\x01",
            "who is known for being a populist.\x02\x03",
            "#10304FThat is, if getting that pinwheel was\x01",
            "your real objective in coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12004FUh uh, well I'll leave the guesswork to you.\x02\x03",
            "#12000FNow then, I've finished eating,\x01",
            "so I must excuse myself.\x02\x03",
            "Please, do your best with\x01",
            "Trade Conference security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FW-We will. Thank\x01",
            "you very much.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1800, 6500, 17260, 1000)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2610, 5000, 17800, 180)
    Sleep(1200)

    def lambda_BF9D():

        label("loc_BF9D")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BF9D")

    QueueWorkItem2(0x101, 2, lambda_BF9D)

    def lambda_BFAF():

        label("loc_BFAF")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BFAF")

    QueueWorkItem2(0x102, 2, lambda_BFAF)

    def lambda_BFC1():

        label("loc_BFC1")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BFC1")

    QueueWorkItem2(0x104, 2, lambda_BFC1)

    def lambda_BFD3():

        label("loc_BFD3")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BFD3")

    QueueWorkItem2(0x109, 2, lambda_BFD3)

    def lambda_BFE5():

        label("loc_BFE5")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BFE5")

    QueueWorkItem2(0x105, 2, lambda_BFE5)
    OP_0D()
    OP_68(-2300, 6500, 15500, 2800)
    OP_95(0xFE, -3790, 5000, 17390, 2000, 0x1)
    OP_95(0xFE, -3790, 5000, 13140, 2000, 0x1)
    OP_68(1000, 6500, 15280, 5500)
    OP_95(0xFE, -2250, 5000, 11680, 2000, 0x1)
    OP_95(0xFE, 8000, 5000, 11660, 2000, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_C08A")
    Call(0, 32)
    Jump("loc_C08D")

    label("loc_C08A")

    Sleep(1000)

    label("loc_C08D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -300, 5000, 17650, 225)
    ClearChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 0x17)
    OP_D7(0x1E)
    OP_CC(0x1, 0x0, 0x0)
    SetScenarioFlags(0x1C7, 0)
    OP_29(0xA3, 0x1, 0xB)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_B471 end

    def Function_32_C0D8(): pass

    label("Function_32_C0D8")

    OP_68(-740, 6500, 17510, 2000)
    MoveCamera(45, 16, 0, 2000)
    OP_6E(360, 2000)
    SetCameraDistance(20440, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003FMr. Lechter and Miss Kilika...\x02\x03",
            "Both the Imperial spy and the\x01",
            "Republican one came to the\x01",
            "city with similar timing.\x02\x03",
            "#00001F...What do you guys think?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_C1CC():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C1CC)
    Sleep(50)

    def lambda_C1DC():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C1DC)
    Sleep(50)

    def lambda_C1EC():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C1EC)
    Sleep(50)

    def lambda_C1FC():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C1FC)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10103F...It's suspicious, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, if that's the case,\x01",
            "shall we follow them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FI think that would be difficult.\x02\x03",
            "#00103FI got the sense that both of\x01",
            "them knew we were coming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FShall we report this to\x01",
            "Mr. Dudley and the others?\x02\x03",
            "#00000FThey might learn something if they\x01",
            "combine it with their other info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FYeah... That sounds good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FAlright, it's decided then.\x01",
            "Let's head to police HQ.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_32_C0D8 end

    def Function_33_C3E5(): pass

    label("Function_33_C3E5")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    LoadChrToIndex("apl/ch50092.itc", 0x24)
    EventBegin(0x0)
    Fade(500)
    OP_68(-1300, 1500, 8730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrPos(0x101, 110, 0, 9440, 0)
    SetChrPos(0x102, -1110, 0, 9440, 0)
    SetChrPos(0x103, 110, 0, 8240, 0)
    SetChrPos(0x104, -1110, 0, 8240, 0)
    SetChrPos(0x109, -1110, 0, 7040, 0)
    SetChrPos(0x105, 110, 0, 7040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Hello, and welcome\x01",
            "to "Vingt Sept".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Are you customers with a reservation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from the\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, so you are the ones who are\x01",
            "doing it. I had heard about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, please sit at any\x01",
            "open table you would like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow me to recommend our\x01",
            "new seasonal "Herb Pasta".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, thank you. We'd love to try it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetChrPos(0x101, -1160, 200, 2350, 270)
    SetChrPos(0x103, -3250, 200, 180, 0)
    SetChrPos(0x104, -4460, 200, 840, 45)
    SetChrPos(0x105, -5400, 200, 2300, 90)
    SetChrPos(0x109, -4700, 200, 3800, 135)
    SetChrPos(0x102, -3140, 200, 4370, 180)
    SetChrPos(0x8, -720, 0, 4770, 240)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    OP_68(-3170, 1500, 2380, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x2)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x24)
    SetChrSubChip(0x24, 0x2)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x24)
    SetChrSubChip(0x25, 0x2)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x24)
    SetChrSubChip(0x26, 0x2)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x2)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others sat at a table\x01",
            "and sampled the Herb Pasta.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00200F*munch, munch*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, so, do you like\x01",
            "our chef's prized pasta?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYes, this is really delicious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, it has a full\x01",
            "flavor but no aftertaste.\x02\x03",
            "#10300FThe herbs give it a nice flavor\x01",
            "and it has a good texture, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah, you can really\x01",
            "sense the chef's skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha, I'm just glad\x01",
            "you all enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, maybe we should\x01",
            "bring KeA here next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, all of us here will be\x01",
            "looking forward to your next visit.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 110, 0, 9440, 0)
    SetChrPos(0x102, -1110, 0, 9440, 0)
    SetChrPos(0x103, 110, 0, 8240, 0)
    SetChrPos(0x109, -1110, 0, 8240, 0)
    SetChrPos(0x105, 110, 0, 7040, 0)
    SetChrPos(0x104, -1110, 0, 7040, 0)
    SetChrPos(0x8, -510, 0, 12450, 180)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    OP_68(-1300, 1500, 8730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetScenarioFlags(0x1, 7)
    SetScenarioFlags(0x172, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_CC2E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_CC4B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_CC5E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_CC71")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_CC8E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_CCA1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CCA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_CCBE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CCBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_CCD1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CCD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_CCEE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CCEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_CD01")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_CD1E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CD1E")

    OP_29(0x80, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE46")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished to collect data from six food places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE3D")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report\x01",
            "to Miss Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all six members'\x01",
            "favourites yet, so why don't we\x01",
            "try our best a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CE3D")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_CE46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF2A")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found the entire SSS\x01",
            "members' favourites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all\x01",
            "six members' favourites.\x02\x03",
            "We have plenty of data now.\x01",
            "Let's go now to the News Service to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_CF2A")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF4C")
    Jump("loc_D0B4")

    label("loc_CF4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CF71")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_D0B4")

    label("loc_CF71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CF7F")
    Jump("loc_D0B4")

    label("loc_CF7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CF8D")
    Jump("loc_D0B4")

    label("loc_CF8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CFC9")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_D0B4")

    label("loc_CFC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D005")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_D0B4")

    label("loc_D005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D041")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_D0B4")

    label("loc_D041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D07D")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_D0B4")

    label("loc_D07D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D0B4")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)

    label("loc_D0B4")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -510, 0, 9440, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_C3E5 end

    def Function_34_D0E4(): pass

    label("Function_34_D0E4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47500.itc", 0x1E)
    LoadChrToIndex("chr/ch44000.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    LoadChrToIndex("chr/ch02902.itc", 0x24)
    LoadChrToIndex("chr/ch03002.itc", 0x25)
    LoadChrToIndex("chr/ch47502.itc", 0x26)
    LoadChrToIndex("chr/ch44002.itc", 0x27)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(10110, 3000, 8790, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x20, 0x26)
    SetChrChipByIndex(0x21, 0x27)
    SetChrSubChip(0x20, 0x0)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrPos(0x20, -3200, 80, 4500, 180)
    SetChrPos(0x21, -1000, 80, 2450, 270)
    SetChrPos(0x101, 15000, 0, 9000, 270)
    SetChrPos(0x102, 15000, 0, 9000, 270)
    SetChrPos(0x103, 15000, 0, 9000, 270)
    SetChrPos(0x104, 15000, 0, 9000, 270)
    SetChrPos(0x109, 15000, 0, 9000, 270)
    SetChrPos(0x105, 15000, 0, 9000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(10110, 1500, 8790, 2500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 35)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 36)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 37)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 39)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(50)

    ChrTalk(
        0x101,
        "#00005FOh...\x02",
    )

    CloseMessageWindow()

    def lambda_D306():
        OP_93(0x102, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D306)
    Sleep(50)

    def lambda_D316():
        OP_93(0x103, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D316)
    Sleep(50)

    def lambda_D326():
        OP_93(0x104, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D326)
    Sleep(50)

    def lambda_D336():
        OP_93(0x109, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D336)
    Sleep(50)

    def lambda_D346():
        OP_93(0x105, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D346)
    Sleep(800)
    Fade(500)
    OP_68(-3200, 1500, 1900, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19960, 0)
    OP_0D()
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    NpcTalk(
        0x20,
        "Host?",
        (
            "...Ha ha, Mrs. Margaret\x01",
            "is rather insightful.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Host?",
        (
            "Maybe it's a bit too much saying something like this,\x01",
            "but you really are wasted on your husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Oh ho ho...\x01",
            "As always, you're good with\x01",
            "your words, Mr. Clyde...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_64(0x20)
    OP_64(0x21)
    OP_0D()
    Fade(500)
    OP_68(10110, 1500, 8790, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#00100F...No doubt, they are the Vice \x01",
            "Chief's wife and that man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FSo the host sitting across from\x01",
            "her is "Clyde", apparently.\x02\x03",
            "#10303FHmm, I don't recall seeing him before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, let's sit at a nearby table\x01",
            "and try not to arouse suspicion.\x02\x03",
            "#00001FWe might be able to learn something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThen, let's split up and\x01",
            "sit at different tables.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    OP_68(3220, 1500, -160, 0)
    MoveCamera(48, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19960, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x24)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x25)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    SetChrPos(0x101, 6800, 50, 3640, 270)
    SetChrPos(0x102, 4550, 50, 5810, 180)
    SetChrPos(0x103, 4550, 50, 1600, 0)
    SetChrPos(0x109, 3330, 50, -6250, 0)
    SetChrPos(0x105, 1050, 50, -3900, 90)
    SetChrPos(0x104, 5340, 0, -4100, 270)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    Sleep(800)
    OP_68(2730, 1500, -2710, 3000)
    OP_0D()
    Sleep(3000)
    OP_68(-3200, 1500, 1900, 3000)
    MoveCamera(24, 24, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19960, 3000)
    OP_6F(0x79)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_64(0x20)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "Oh yes, I saw the pamphlet\x01",
            "from the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "When I saw those photos, I fell\x01",
            "in love with it at first sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Ha ha, what an honor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "In that case, let's go\x01",
            "together next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If you like, I can even\x01",
            "arrange a hotel for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Ho ho ho, that won't be necessary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Actually, I've already gone to see it. \x01",
            "The scenery is good, and I have no complaints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Oh, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "That is a huge help for me too. \x01",
            "Then, about the reservation...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_64(0x20)
    OP_64(0x21)
    Sleep(500)
    Fade(500)
    OP_68(3690, 1500, 2080, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19760, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        "#00001F(...They're talking rather quietly.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(It seems like they're planning a\x01",
            "trip to Michelam together, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Even so, I think the\x01",
            "situation is strange.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(2220, 1500, -5240, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19810, 0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x2)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00303F(The guy is usin'\x01",
            "language that's\x01",
            "excessively polite.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(But, we don't have\x01",
            "anything decisive yet...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu, let's keep\x01",
            "listening in like this.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(-3200, 1500, 1900, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19960, 0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x20,
        "...Well then, if you'll excuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Yes, I understand. \x01",
            "I'll see you later, at that store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            ""Neue-Blanc" in Entertainment\x01",
            "District, right? \x01",
            "Uh uh, understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'll bring what you're looking\x01",
            "for and see you there, madam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Yes, I'll be waiting.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x20, 1, 0, 41)
    Sleep(300)
    BeginChrThread(0x21, 1, 0, 42)
    Sleep(300)
    OP_68(-650, 1550, 7560, 3000)
    WaitChrThread(0x20, 1)
    Sleep(800)

    def lambda_DDB4():
        OP_95(0x20, 4230, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_DDB4)
    Sleep(200)
    WaitChrThread(0x21, 1)

    def lambda_DDD5():
        OP_95(0x21, 4230, 0, 7840, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_DDD5)
    Sleep(1500)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    Fade(500)
    OP_68(2710, 1500, -1840, 0)
    MoveCamera(46, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22840, 0)
    SetChrPos(0x20, 11630, 0, 9250, 90)
    SetChrPos(0x21, 10110, 0, 8780, 90)

    def lambda_DE52():
        OP_95(0x20, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_DE52)

    def lambda_DE6C():
        OP_95(0x21, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_DE6C)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x2)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x1)
    OP_0D()
    Sleep(50)

    ChrTalk(
        0x101,
        "#00001F(Looks like they're leaving...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(Lloyd, what should we do?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(We haven't gotten any\x01",
            "decisive info yet, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...Let's tail them.)\x02\x03",
            "#00000F(Randy, Wazy and\x01",
            "I on "Clyde".)\x02\x03",
            "(Elie, Tio and Noｱl, \x01",
            "you take Mrs. Margaret.)\x02\x03",
            "(However, do your best\x01",
            "not to get noticed.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F(...Understood!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F(Alright, let's go.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F(Hu hu, this is getting interesting.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_34_D0E4 end

    def Function_35_E061(): pass

    label("Function_35_E061")


    def lambda_E066():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E066)

    def lambda_E077():
        OP_95(0x101, 10110, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E077)
    WaitChrThread(0x101, 1)
    Return()

    # Function_35_E061 end

    def Function_36_E091(): pass

    label("Function_36_E091")


    def lambda_E096():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E096)

    def lambda_E0A7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E0A7)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, 10600, 0, 10450, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_36_E091 end

    def Function_37_E0D7(): pass

    label("Function_37_E0D7")


    def lambda_E0DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E0DC)

    def lambda_E0ED():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E0ED)
    WaitChrThread(0x103, 1)
    OP_95(0xFE, 11310, 0, 7580, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_E0D7 end

    def Function_38_E11D(): pass

    label("Function_38_E11D")


    def lambda_E122():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E122)

    def lambda_E133():
        OP_95(0xFE, 11630, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E133)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_38_E11D end

    def Function_39_E154(): pass

    label("Function_39_E154")


    def lambda_E159():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E159)

    def lambda_E16A():
        OP_95(0xFE, 12860, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E16A)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_E154 end

    def Function_40_E18B(): pass

    label("Function_40_E18B")


    def lambda_E190():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_E190)

    def lambda_E1A1():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E1A1)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, 12200, 0, 10670, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_E18B end

    def Function_41_E1D1(): pass

    label("Function_41_E1D1")

    Fade(500)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x20, -2700, 0, 4500, 90)
    OP_0D()
    OP_95(0x20, -370, 0, 9500, 1500, 0x0)
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(500)
    Return()

    # Function_41_E1D1 end

    def Function_42_E215(): pass

    label("Function_42_E215")

    Fade(500)
    SetChrChipByIndex(0x21, 0x1F)
    SetChrSubChip(0x21, 0x0)
    Sound(812, 0, 100, 0)
    SetChrPos(0x21, -1160, 0, 2700, 0)
    OP_0D()
    Sleep(500)
    OP_95(0x21, -100, 0, 7840, 1500, 0x0)
    OP_93(0x21, 0x0, 0x1F4)
    Return()

    # Function_42_E215 end

    def Function_43_E259(): pass

    label("Function_43_E259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E431")

    ChrTalk(
        0xB,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please sit wherever you'd like. \x01",
            "I'll be there to take your order shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Maybe I can invite\x01",
            "her to the pageant\x01",
            "as our "waitress".)\x02\x03",
            "#00000FUmm, excuse me. \x01",
            "I'd like to ask you something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You asked her to participate \x01",
            "in the charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "W-What? To participate\x01",
            "in a pageant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmm...\x01",
            "I'm terribly sorry, but...\x01",
            "I'm not  interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-I see... If you'll\x01",
            "excuse us then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 5)
    Jump("loc_E4B7")

    label("loc_E431")


    ChrTalk(
        0xB,
        (
            "I'm not especially interested in\x01",
            "participating in a beauty pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm okay if you\x01",
            "just need help from\x01",
            "a waitress, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4B7")

    TalkEnd(0xB)
    Return()

    # Function_43_E259 end

    SaveToFile()

Try(main)
