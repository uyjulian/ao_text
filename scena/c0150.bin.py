from ScenarioHelper import *

def main():
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
        "Hoistov",             # 1
        "Brown",               # 2
        "Seruteo",               # 3
        "Nonno",                 # 4
        "Frote",                 # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "Citizen",                   # 8
        "Citizen",                   # 9
        "Citizen",                   # 10
        "Citizen",                   # 11
        "tourist",                 # 12
        "tourist",                 # 13
        "tourist",                 # 14
        "tourist",                 # 15
        "Citizen",                   # 16
        "Citizen",                   # 17
        "Yona",                   # 18
        "Roberts boss",           # 19
        "Abel",                 # 20
        "Mimi",                   # 21
        "Sally",                 # 22
        "Assistant Kirika",           # 23
        "Gironde",               # 24
        "Clyde",               # 25
        "Mrs. Margaret",       # 26
        "cuisine",                   # 27
        "cuisine",                   # 28
        "cuisine",                   # 29
        "cuisine",                   # 30
        "cuisine",                   # 31
        "cuisine",                   # 32
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
        "Function_5_EC5",          # 05, 5
        "Function_6_EC9",          # 06, 6
        "Function_7_272D",         # 07, 7
        "Function_8_2731",         # 08, 8
        "Function_9_3E69",         # 09, 9
        "Function_10_4DFA",        # 0A, 10
        "Function_11_60B7",        # 0B, 11
        "Function_12_6ED7",        # 0C, 12
        "Function_13_7FDF",        # 0D, 13
        "Function_14_80A0",        # 0E, 14
        "Function_15_8190",        # 0F, 15
        "Function_16_822D",        # 10, 16
        "Function_17_82F2",        # 11, 17
        "Function_18_8417",        # 12, 18
        "Function_19_84E7",        # 13, 19
        "Function_20_85EB",        # 14, 20
        "Function_21_8781",        # 15, 21
        "Function_22_8998",        # 16, 22
        "Function_23_8BFB",        # 17, 23
        "Function_24_8CEF",        # 18, 24
        "Function_25_8E55",        # 19, 25
        "Function_26_90B8",        # 1A, 26
        "Function_27_933D",        # 1B, 27
        "Function_28_94F2",        # 1C, 28
        "Function_29_966B",        # 1D, 29
        "Function_30_96F0",        # 1E, 30
        "Function_31_A7F3",        # 1F, 31
        "Function_32_B3EB",        # 20, 32
        "Function_33_B6D8",        # 21, 33
        "Function_34_C341",        # 22, 34
        "Function_35_D2BA",        # 23, 35
        "Function_36_D2EA",        # 24, 36
        "Function_37_D330",        # 25, 37
        "Function_38_D376",        # 26, 38
        "Function_39_D3AD",        # 27, 39
        "Function_40_D3E4",        # 28, 40
        "Function_41_D42A",        # 29, 41
        "Function_42_D46E",        # 2A, 42
        "Function_43_D4B2",        # 2B, 43
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
            "= New menu · Herbal pasta =\x01",
            "· Reproduce the old taste of customers\x01",
            "· Leverage fresh herbs\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Herb pasta recipes are written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_EC1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Herb pasta\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_EC1")

    TalkEnd(0xFF)
    Return()

    # Function_4_DB1 end

    def Function_5_EC5(): pass

    label("Function_5_EC5")

    Call(0, 6)
    Return()

    # Function_5_EC5 end

    def Function_6_EC9(): pass

    label("Function_6_EC9")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A2")

    ChrTalk(
        0x1F,
        "So, the Special Affairs Support Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I heard from Sergei,\x01",
            "It's time to restart.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "Hmm? With redheaded older brother\x01",
            "Lady of the magician,\x01",
            "It is still nice …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, 2 people are still\x01",
            "There was errands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Huh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "So, two people there\x01",
            "Is it a new member?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I'm listening to stories about the product from Sergei.\x01",
            "Well, do not look at it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, you have a lot of support.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102Fthank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 2)

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AE")
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "Yo, calming ……\x01",
            "You often came!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Gironde,\x01",
            "long time no see.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_128E")

    ChrTalk(
        0x1F,
        (
            "Hello, I'm relieved\x01",
            "It is nothing more than a matter of facing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "But what is Dudley together?\x01",
            "Is it supposed to start moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYeah, when it gets a bit noisy\x01",
            "Thought, please pardon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Happy ending\x01",
            "I guess I care now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, for the time being,\x01",
            "The shop hit various things\x01",
            "Somehow the items are in a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "A big deal is hey,\x01",
            "Please go look at it properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1382")

    label("loc_128E")


    ChrTalk(
        0x1F,
        (
            "Hello, I'm relieved\x01",
            "It is nothing more than a matter of facing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "By the way from the police guys\x01",
            "I heard the story a lot.\x01",
            "You do not need to talk much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, for the time being\x01",
            "The shop hit various things\x01",
            "Somehow the items are in a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "A big deal is hey,\x01",
            "Please go look at it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1382")


    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 0)

    label("loc_13AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2729")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1416")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1416")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1435")
    OP_AF(0x5)
    Jump("loc_1477")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1445")
    OP_AF(0x4)
    Jump("loc_1477")

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1455")
    OP_AF(0x3)
    Jump("loc_1477")

    label("loc_1455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1465")
    OP_AF(0x2)
    Jump("loc_1477")

    label("loc_1465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1475")
    OP_AF(0x1)
    Jump("loc_1477")

    label("loc_1475")

    OP_AF(0x0)

    label("loc_1477")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2724")

    label("loc_1486")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_149A")
    Jump("loc_2724")

    label("loc_149A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2724")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_155D")

    ChrTalk(
        0x1F,
        (
            "Fuu, anyhow that spooky big tree,\x01",
            "Finally the town is calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, the future is exactly hard … …\x01",
            "That's it, I'm just scratching a tokoton.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_155D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15D9")

    ChrTalk(
        0x1F,
        (
            "Heck, but again like this\x01",
            "Worship the face of the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Anyway you guys,\x01",
            "Keep it up in the future!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_15D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")

    ChrTalk(
        0x1F,
        (
            "Defense Army, Dieter Crois also\x01",
            "I also did big things again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Carefully prepared your uniforms,\x01",
            "It is a pretty well prepared story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Monsters are weapons and weapons\x01",
            "I do not really have a way to go … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, nothing like that\x01",
            "It is reality that I can not say it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179E")

    label("loc_16FC")


    ChrTalk(
        0x1F,
        (
            "Monsters are weapons and weapons\x01",
            "I do not really have a way to go … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, nothing like that\x01",
            "It is reality that I can not say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Well … … I will be thoughtful of the future.\x02",
    )

    CloseMessageWindow()

    label("loc_179E")

    Jump("loc_2724")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1937")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A3")

    ChrTalk(
        0x1F,
        (
            "Because of the uproar of Mainz in front of us,\x01",
            "Citizen wants to buy weapons\x01",
            "I'm going to push the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I need a license\x01",
            "I do not care about selling … …\x01",
            "There are some persistent inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, this is the situation\x01",
            "I do not even know the feelings … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1932")

    label("loc_18A3")


    ChrTalk(
        0x1F,
        (
            "Anyway, weapons are dealing with MON\x01",
            "I just corresponded to him\x01",
            "I have responsibility and understanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's a good opportunity.\x01",
            "You should remember me again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1932")

    Jump("loc_2724")

    label("loc_1937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A03")

    ChrTalk(
        0x1F,
        (
            "Well, today again\x01",
            "It is a spiritual thorny tumor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If you are in a dangerous place from now on\x01",
            "If you are going to step in,\x01",
            "You never neglect to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "It is not a hobby that customers die.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A7D")

    label("loc_1A03")


    ChrTalk(
        0x1F,
        (
            "If you are in a dangerous place from now on\x01",
            "If you are going to step in,\x01",
            "You never neglect to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "It is not a hobby that customers die.\x02",
    )

    CloseMessageWindow()

    label("loc_1A7D")

    Jump("loc_2724")

    label("loc_1A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7C")

    ChrTalk(
        0x1F,
        (
            "The train accident happened yesterday is,\x01",
            "Everything is onigiri me\x01",
            "Is not it a rumor that the work of the chemistry is done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Heck, say it is a demon easily,\x01",
            "It's just about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "No way, I think human beings are gone.\x01",
            "I guess it's nothing like walking … …\x01",
            "Anyhow, it is a noisy story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C09")

    label("loc_1B7C")


    ChrTalk(
        0x1F,
        (
            "Heck, say it is a demon easily,\x01",
            "It's just about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "No way, I think human beings are gone.\x01",
            "I guess it's nothing like walking … …\x01",
            "Anyhow, it is a noisy story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C09")

    Jump("loc_2724")

    label("loc_1C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C98")

    ChrTalk(
        0x1F,
        (
            "Ha, the siren sounds\x01",
            "There is no way to say bad guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I do not know whether it is a case or an accident ……\x01",
            "This town is totally noisy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_1C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D81")

    ChrTalk(
        0x1F,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Anything's fine\x01",
            "Pick it up, papat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When I stayed somewhere,\x01",
            "It is hard to read magazines and it is a way out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(… … as usual, decently\x01",
            "I do not feel like doing work. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DFD")

    label("loc_1D81")


    ChrTalk(
        0x1F,
        (
            "I do not know what you want,\x01",
            "Just choose Papat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "When I stayed somewhere,\x01",
            "It is hard to read magazines and it is a way out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFD")

    Jump("loc_2724")

    label("loc_1E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EA2")

    ChrTalk(
        0x1F,
        (
            "Haha, I swallow the demands of the two great countries\x01",
            "No matter how far I am advocating for independence here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, whatever, to this past war\x01",
            "I'm praying only if you do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_1EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_22BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224C")

    ChrTalk(
        0x1F,
        (
            "Yo, Lady.\x01",
            "At last it seems to have returned to the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "That man left a magician\x01",
            "I thought he was coming soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, that man …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, probably not the boss.\x02\x03",
            "#00211FThis forward feeling,\x01",
            "There are a couple of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FWell, well, that's it.\x01",
            "I guess that you are worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, so much\x01",
            "I mean I'm not a bad person,\x01",
            "I think it is a pretty good person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F…… I can not accept that point,\x01",
            "That's only extra, nature#4RAfter all#Is it bad?\x02\x03",
            "#00200FIn the beginning too much intervention\x01",
            "I am clumsy and many wasteful stories ……\x01",
            "I can not get along with them very much.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2126")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2126")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214C")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_214C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2172")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2172")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2198")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2198")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10103FI see,\x01",
            "There are various things in Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Fahaha, do not know well\x01",
            "From now on the handling of the magic wand will resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Please tell me whenever you need it anytime.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 5)
    Jump("loc_22B6")

    label("loc_224C")


    ChrTalk(
        0x1F,
        (
            "My girlfriend returned,\x01",
            "The handling of the magician also resumes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, if it is necessary\x01",
            "Please call me at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B6")

    Jump("loc_2724")

    label("loc_22BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E7")

    ChrTalk(
        0x1F,
        (
            "You look like Dudley.\x01",
            "Walking along with the support department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FNo, I was worried a bit.\x02\x03",
            "#00600FWith only these guys\x01",
            "I am not going to rely, so I just accompany them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Heck, you are as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Oh well, it's about time for shops\x01",
            "If you see it, please look like chatcher.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2454")

    label("loc_23E7")


    ChrTalk(
        0x1F,
        (
            "Because it is sooner Mong.\x01",
            "If you see it, please look like chatcher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "I'm going up early and doing a drink.\x02",
    )

    CloseMessageWindow()

    label("loc_2454")

    Jump("loc_2724")

    label("loc_2459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2525")

    ChrTalk(
        0x1F,
        (
            "Although I do not know what it is a trade meeting,\x01",
            "Do not get licked by two major countries\x01",
            "You gotta do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Yatsura, even if this is a bit\x01",
            "Let's show you a sweet thrush If you are a mon,\x01",
            "I will come up with it soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_2525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E9")

    ChrTalk(
        0x1F,
        (
            "Rubache is gone,\x01",
            "Although it seems that donkeys on the back are decreasing … …\x01",
            "Conversely, it is creepy and useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "As it is, nothing must happen\x01",
            "I do not care but … Are you looking at yume too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2651")

    label("loc_25E9")


    ChrTalk(
        0x1F,
        (
            "With a lot of time, recently\x01",
            "I've come to spare time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Goddess, I will ask\x01",
            "Please do not let me work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2651")

    Jump("loc_2724")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26CC")

    ChrTalk(
        0x1F,
        (
            "Ha, today again\x01",
            "The weather was quite obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well this is closed\x01",
            "There was no relationship in store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2724")

    label("loc_26CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2724")

    ChrTalk(
        0x1F,
        (
            "Weapons dealt with by you\x01",
            "We have prepared one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        "Well, do not look at it properly.\x02",
    )

    CloseMessageWindow()

    label("loc_2724")

    Jump("loc_13B8")

    label("loc_2729")

    TalkEnd(0x1F)
    Return()

    # Function_6_EC9 end

    def Function_7_272D(): pass

    label("Function_7_272D")

    Call(0, 8)
    Return()

    # Function_7_272D end

    def Function_8_2731(): pass

    label("Function_8_2731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2768")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2768")
    Call(0, 33)
    Return()

    label("loc_2768")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29EF")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, you guys are the police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Surely independent from the Defense Forces\x01",
            "I heard that it is moving … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, somehow\x01",
            "In order to converge this situation\x01",
            "It is a moving place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf you are here,\x01",
            "Is there any inconvenience?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, you are here a bit\x01",
            "Because there are only staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even compared to other places\x01",
            "I think that you are calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is a restaurant,\x01",
            "I do not have trouble eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see,\x01",
            "Surely the neighborhood is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIn any case,\x01",
            "It is dangerous to go outside now.\x02\x03",
            "#00100FThe manager will stay with you as it is\x01",
            "Please stay in the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, I got it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BB, 7)
    TalkEnd(0x8)
    Return()

    label("loc_29EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E65")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A57")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A76")
    OP_AF(0x9)
    Jump("loc_2A78")

    label("loc_2A76")

    OP_AF(0x8)

    label("loc_2A78")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E60")

    label("loc_2A87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A9B")
    Jump("loc_3E60")

    label("loc_2A9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E60")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2B20")

    ChrTalk(
        0x8,
        (
            "Next time, by all means, with lots of people\x01",
            "Please come over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Still visiting us again\x01",
            "I will be waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_2B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C01")

    ChrTalk(
        0x8,
        (
            "Seruteo and nonno,\x01",
            "If you leave it to these two people\x01",
            "Van Set is also safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, just before that\x01",
            "The entire crossbell makes difficulties\x01",
            "I have to get over it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What, if everyone ties together\x01",
            "There is nothing you can not do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_2C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2CD2")

    ChrTalk(
        0x8,
        (
            "Hmm, but to the police\x01",
            "If you can call me out\x01",
            "You can be very relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyways,\x01",
            "This place as a manager\x01",
            "I take responsibility and keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, when going out outside\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DDF")

    ChrTalk(
        0x8,
        (
            "The IBC asset freeze is declared … …\x01",
            "And from this morning the transcontinental railroad\x01",
            "Is it virtually stopped? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, when it becomes like this,\x01",
            "No wonder whatever happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I plan to keep operating as much as possible … …\x01",
            "To be honest, I am full of anxious feelings.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E8E")

    label("loc_2DDF")


    ChrTalk(
        0x8,
        (
            "The IBC asset freeze is declared … …\x01",
            "And from this morning the transcontinental railroad\x01",
            "Is it virtually stopped? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I plan to keep operating as much as possible … …\x01",
            "To be honest, I am full of anxious feelings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8E")

    Jump("loc_3E60")

    label("loc_2E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE7")

    ChrTalk(
        0x8,
        (
            "There is such an incident, too,\x01",
            "Ceoteoteo and nonno dish confrontation\x01",
            "I intended to postpone it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With the strong demands of the two,\x01",
            "Make a decision after closing yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "result--\x01",
            "Both are really wonderful\x01",
            "It was a tearful tear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, hasty growth\x01",
            "To witness it,\x01",
            "That's such a wonderful thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_306C")

    label("loc_2FE7")


    ChrTalk(
        0x8,
        (
            "Hmm, after all, the arms of nonno\x01",
            "It is as if to keep it as it is\x01",
            "It is unnecessary, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Three people in the kitchen … …\x01",
            "Let's consider it seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306C")

    Jump("loc_3E60")

    label("loc_3071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3109")

    ChrTalk(
        0x8,
        (
            "Among customers who use our store\x01",
            "Of course there are people in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because there are many people with familiar face ……\x01",
            "I'm really sick and I'm dying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_3109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_329A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FC")

    ChrTalk(
        0x8,
        (
            "Huh, apparently Seruteo\x01",
            "It seems like I think a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I used to do so,\x01",
            "The answer is troubled and suffering\x01",
            "Something that is bothering me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Celteo has this experience\x01",
            "I want you to make it a good food.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3295")

    label("loc_31FC")


    ChrTalk(
        0x8,
        (
            "I used to do so,\x01",
            "The answer is troubled and suffering\x01",
            "Something that is bothering me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Celteo has this experience\x01",
            "I want you to make it a good food.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3295")

    Jump("loc_3E60")

    label("loc_329A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33F0")

    ChrTalk(
        0x8,
        (
            "Anything, on the West Crossbell Highway\x01",
            "I heard that a train accident happened … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Was it also a falling rock?\x01",
            "There seem to be many injured people,\x01",
            "Makes you worry, right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33EB")

    ChrTalk(
        0x101,
        (
            "#00008F(The gourmet guide coverage here\x01",
            "It looks like it could be done … …)\x02\x03",
            "#00003F(It is not right now.\x01",
            "Let's not forget to come later. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33EB")

    Jump("loc_3E60")

    label("loc_33F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_353C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0x8,
        (
            "Recently, Celteo's work attitude\x01",
            "It got better enough to make a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For beautiful women's customers\x01",
            "It is no longer overreacting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, what a splendid thing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3537")

    label("loc_34B9")


    ChrTalk(
        0x8,
        (
            "I have been heading for ladies until now\x01",
            "Passion of Celteo gradually\x01",
            "You seem to be starting to cook dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, what a splendid thing.\x02",
    )

    CloseMessageWindow()

    label("loc_3537")

    Jump("loc_3E60")

    label("loc_353C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_35B1")

    ChrTalk(
        0x8,
        (
            "Huhu, apparently Seruteo too\x01",
            "It seems that he finally got serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I am looking forward to the direction of the game.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E60")

    label("loc_35B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3686")

    ChrTalk(
        0x8,
        (
            "Brown cooks non nono\x01",
            "Listen as you leave, Celtio of flukes too\x01",
            "You seem to be impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm … … apparently to Seruteo\x01",
            "What was missing was like a rival\x01",
            "Perhaps it was a presence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_373E")

    label("loc_3686")


    ChrTalk(
        0x8,
        (
            "If I think about it, I\x01",
            "Always compete with Brown for arms,\x01",
            "And they came to polish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm … … apparently to Seruteo\x01",
            "What was missing was like a rival\x01",
            "Perhaps it was a presence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373E")

    Jump("loc_3E60")

    label("loc_3743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3822")

    ChrTalk(
        0x8,
        (
            "I heard from Brown,\x01",
            "Apparently to nonno the cook's\x01",
            "It seems there is sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Initially we had a simple help\x01",
            "I was going to just do it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, this is\x01",
            "It might be an unexpected harvest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3892")

    label("loc_3822")


    ChrTalk(
        0x8,
        (
            "A simple help to nonno\x01",
            "I was going to just do it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, this is\x01",
            "It might be an unexpected harvest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3892")

    Jump("loc_3E60")

    label("loc_3897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F2")

    ChrTalk(
        0x8,
        (
            "I will leave that celtio to serve customers\x01",
            "Courage came, apparently surprising\x01",
            "You seem to be doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even when I talk to my favorite woman\x01",
            "It seems to be keeping the minimum moderation,\x01",
            "If so, there is no concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, how about the rest?\x01",
            "Cook's basic attitude\x01",
            "It makes me realize … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "After all, this is somewhat challenging.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AA8")

    label("loc_39F2")


    ChrTalk(
        0x8,
        (
            "When Seruteo makes cooking,\x01",
            "Always be concerned with surprises\x01",
            "It only makes fun ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of that orthodox\x01",
            "I hate extreme … but how\x01",
            "Will you change my mind?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA8")

    Jump("loc_3E60")

    label("loc_3AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B46")

    ChrTalk(
        0x8,
        (
            "If you pick up your work,\x01",
            "I thought that I was shocked … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, apparently\x01",
            "It seems that Ate has gone off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BF0")

    label("loc_3B46")


    ChrTalk(
        0x8,
        (
            "When you remove Seruteo by whatever it is,\x01",
            "The burden on Brown\x01",
            "It will be quite a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Do not make such a thing meaningless\x01",
            "I can not go on to continue … ….\x01",
            "Hmm, what is wrong?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF0")

    Jump("loc_3E60")

    label("loc_3BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3D01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C90")

    ChrTalk(
        0x8,
        (
            "Well, Mr. Celtio of my place is\x01",
            "It seems that it does not grow by merely leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hm … … Here is one\x01",
            "Shall I go with rough treatment?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CFC")

    label("loc_3C90")


    ChrTalk(
        0x8,
        (
            "Hm … … Here is one\x01",
            "Shall I go with rough treatment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this, Seruteo\x01",
            "I hope it will change, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFC")

    Jump("loc_3E60")

    label("loc_3D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEB")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Welcome to \"Van Set\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In our shop a few times a year, according to the time\x01",
            "We have revised some menus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Chef Brown boasting of our shop devised\x01",
            "Please appreciate the new menu.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E60")

    label("loc_3DEB")


    ChrTalk(
        0x8,
        (
            "In our shop a few times a year, according to the time\x01",
            "We have revised some menus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "If you do not mind, please appreciate it.\x02",
    )

    CloseMessageWindow()

    label("loc_3E60")

    Jump("loc_29F9")

    label("loc_3E65")

    TalkEnd(0x8)
    Return()

    # Function_8_2731 end

    def Function_9_3E69(): pass

    label("Function_9_3E69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3EEE")

    ChrTalk(
        0xFE,
        (
            "Celteo's guy,\x01",
            "Something suddenly flew away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, but it's a nice tendency.\x01",
            "I wonder what I am like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_3EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3FA2")

    ChrTalk(
        0xFE,
        (
            "Willing to eat the meal I made\x01",
            "I can eat it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess the cook's happiness is\x01",
            "Besides this, hey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in this situation\x01",
            "Just with a customer who behaves a meal\x01",
            "Something's gonna come up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402E")

    ChrTalk(
        0xFE,
        "The railroad has completely stopped since this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to replace imported ingredients ……\x01",
            "This is his immediate task.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40CD")

    label("loc_402E")


    ChrTalk(
        0xFE,
        (
            "Something smells like kina but …\x01",
            "For now, we cook\x01",
            "There is only one thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to replace imported ingredients ……\x01",
            "This is his immediate task.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40CD")

    Jump("loc_4DF6")

    label("loc_40D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_42BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4204")

    ChrTalk(
        0xFE,
        (
            "Celteo's guy, apparently\x01",
            "I feel relieved as if I had peeled away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pasta sauce that he made is\x01",
            "Seafood flavor in tomato base\x01",
            "It was a monkey that was made effective ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Other hidden taste, several kinds of spices\x01",
            "It is exquisitely charged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The taste was outstanding, and as it was\x01",
            "There was a fresh taste and it was a good result.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_42B6")

    label("loc_4204")


    ChrTalk(
        0xFE,
        (
            "Previous Seruteo,\x01",
            "A combination of food materials that is considered as a standard\x01",
            "Anyway I have a tendency to hate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, the vision is reversed\x01",
            "It's getting narrower … ….\x01",
            "Apparently a little seems to have grown up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42B6")

    Jump("loc_4DF6")

    label("loc_42BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4351")

    ChrTalk(
        0xFE,
        (
            "Hmm, I do not care Today is more than usual\x01",
            "It seems a bit dull customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well … that such incident happened yesterday today\x01",
            "Since it happened it was no use way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43CF")

    ChrTalk(
        0xFE,
        "Anyway, cook showdown?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nonono and Seruteo each\x01",
            "It seems that we are working seriously,\x01",
            "It was pretty bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_43CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_44E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445B")

    ChrTalk(
        0xFE,
        "The sound of an ambulance can be obtained from a little while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to you hear the deep-fried sounds Hey,\x01",
            "I got burnt a little bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44DB")

    label("loc_445B")


    ChrTalk(
        0xFE,
        (
            "Oops, scorched fried fish\x01",
            "Please do not give it to the guests at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Later to Celteo's guy\x01",
            "I am planning to eat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44DB")

    Jump("loc_4DF6")

    label("loc_44E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4578")

    ChrTalk(
        0xFE,
        (
            "Hmm, the work of nonno first\x01",
            "Compared a lot better than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hire a new hall clerk\x01",
            "It may be ants to put the kitchen in a 3 person regime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_476C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EF")

    ChrTalk(
        0xFE,
        "Hello, Hoistov also do it well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything is impatient with the achievements of nonno\x01",
            "Using Celteo's feelings\x01",
            "I do not care about growing as a chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By whatever, I'm betting on the seat of the cook\x01",
            "Two people in a week\x01",
            "I'm sorry to have a couple showdown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, such an excuse,\x01",
            "If there is only a willingness to truly\x01",
            "I'd like you to do a cock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oops, the current story is a secret to Seruteo?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4767")

    label("loc_46EF")


    ChrTalk(
        0xFE,
        "Hello, Hoistov also do it well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, Celteo's guy too\x01",
            "It seems to be motivated,\x01",
            "I think that it is a good idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4767")

    Jump("loc_4DF6")

    label("loc_476C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_481B")

    ChrTalk(
        0xFE,
        (
            "Haha, the non-guy fellow,\x01",
            "It seems that he is puzzled by running water,\x01",
            "Somehow it sounds pretty motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds good, that feeling for the first time.\x01",
            "I remember the era when I was a little young.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_481B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4871")

    ChrTalk(
        0xFE,
        (
            "Yosh, better yet\x01",
            "Tomorrow I was drunk\x01",
            "Do you try leaving cooking to non-no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF6")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4940")

    ChrTalk(
        0xFE,
        (
            "Okay, this morning to nonno\x01",
            "The bouillon that I asked was in a good condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Surprised, that's more than I expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that I cook at home … …\x01",
            "In this case it might be nice to leave it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49CE")

    label("loc_4940")


    ChrTalk(
        0xFE,
        (
            "Hmm, this broth.\x01",
            "I can draw out the taste of the material firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that I cook at home … …\x01",
            "In this case it might be nice to leave it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CE")

    Jump("loc_4DF6")

    label("loc_49D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB0")

    ChrTalk(
        0xFE,
        (
            "Hmmm, but also Hoistov\x01",
            "I will do drunken things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not meant to keep it from the scene\x01",
            "I did not think so … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just well, indeed in his case,\x01",
            "If you do not do that much\x01",
            "It may not change.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B24")

    label("loc_4AB0")


    ChrTalk(
        0xFE,
        (
            "Anyway, Celteo's guy\x01",
            "It seems I can not bear at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's changing my position now.\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B24")

    Jump("loc_4DF6")

    label("loc_4B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C23")

    ChrTalk(
        0xFE,
        (
            "Everything about cuisine, first of all basics\x01",
            "I can not do anything to stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, even in the painting world, famous abstract painters\x01",
            "That's why I'm drawing superb realist paintings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time for Celteo guys soon.\x01",
            "I would like you to know things around me ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4CAF")

    label("loc_4C23")


    ChrTalk(
        0xFE,
        (
            "Everything about cuisine, first of all basics\x01",
            "I can not do anything to stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time for Celteo guys soon.\x01",
            "I would like you to know things around me ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CAF")

    Jump("loc_4DF6")

    label("loc_4CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D84")

    ChrTalk(
        0xFE,
        (
            "I previously imposed Celtio's guy\x01",
            "Making a new menu\x01",
            "After all it was a failure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He is never good at striking … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I'm in tune, what I can become a part of\x01",
            "It is still ahead for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4DF6")

    label("loc_4D84")


    ChrTalk(
        0xFE,
        (
            "Celteo's guy\x01",
            "Nevertheless the line is not bad … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I'm in tune, what I can become a part of\x01",
            "It is still ahead for the time being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF6")

    TalkEnd(0xFE)
    Return()

    # Function_9_3E69 end

    def Function_10_4DFA(): pass

    label("Function_10_4DFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE7")

    ChrTalk(
        0xFE,
        (
            "Whatever the city is like this,\x01",
            "Only one can do as a chef … …\x01",
            "Just to serve delicious food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the future food ingredients will be limited,\x01",
            "You should be able to get over with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to work hard again today!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F50")

    label("loc_4EE7")


    ChrTalk(
        0xFE,
        (
            "Only one can do as a chef … …\x01",
            "It is only to serve delicious food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to work hard again today!\x02",
    )

    CloseMessageWindow()

    label("loc_4F50")

    Jump("loc_60B3")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_50FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506F")

    ChrTalk(
        0xFE,
        (
            "I do not care if it is not such a time\x01",
            "I am merciful but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What Brown says is\x01",
            "I understand somewhat really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, she is a cook.\x01",
            "Only with a customer ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Self-satisfying cooking only\x01",
            "I am making it\x01",
            "It makes me feel embarrassed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50FA")

    label("loc_506F")


    ChrTalk(
        0xFE,
        (
            "Yeah, she is a cook.\x01",
            "Only with a customer ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Self-satisfying cooking only\x01",
            "I am making it\x01",
            "It makes me feel embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50FA")

    Jump("loc_60B3")

    label("loc_50FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5197")

    ChrTalk(
        0xFE,
        (
            "President Dieter's speech,\x01",
            "It was truly amazingly powerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, listening to that person's words\x01",
            "I feel like being courageous and proud.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_5197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5248")

    ChrTalk(
        0xFE,
        "Man, the manager is also bad for the manager.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Decide winning or losing from the beginning\x01",
            "I did not plan to do it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hecks, for what purpose\x01",
            "I do not know whether I struggled.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52D5")

    label("loc_5248")


    ChrTalk(
        0xFE,
        (
            "even if……\x01",
            "Recently, I feel too much noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But in that sense,\x01",
            "It is something you can do normally like this now\x01",
            "It makes me feel happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D5")

    Jump("loc_60B3")

    label("loc_52DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5366")

    ChrTalk(
        0xFE,
        (
            "It's an occupation … …\x01",
            "A terrible thing, it's a ridiculous story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dominate people with violence\x01",
            "I'm talking about what is fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_5366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5450")

    ChrTalk(
        0xFE,
        (
            "Dammit, even policies are not fixed\x01",
            "Just time just passes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Early birds, to get pasta\x01",
            "The direction of the source is hardened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomato base, cream base,\x01",
            "Or make it an unknown source ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54BE")

    label("loc_5450")


    ChrTalk(
        0xFE,
        (
            "So, that's why\x01",
            "What is unknown sauce! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haa … somehow,\x01",
            "I feel like I can see my faults.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54BE")

    Jump("loc_60B3")

    label("loc_54C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_54F9")

    ChrTalk(
        0xFE,
        "Hmm? Somewhat burning outside is noisy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_54F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_566D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FC")

    ChrTalk(
        0xFE,
        (
            "Even if I say it is delicious anyway,\x01",
            "As it is cooking, the appearance is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, this is our confrontation theme\x01",
            "Separately the brand newness is not important, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, basically\x01",
            "Make it a classic menu\x01",
            "I wonder if I think in the direction to add arrangements.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5668")

    label("loc_55FC")


    ChrTalk(
        0xFE,
        (
            "Ha, but definitely\x01",
            "I do not like the word staple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because if it's a staple\x01",
            "Is it natural for you to be good?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5668")

    Jump("loc_60B3")

    label("loc_566D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5701")

    ChrTalk(
        0xFE,
        (
            "… … No way no\x01",
            "I do not want to have a dish confrontation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, delicious pasta dish, or …\x01",
            "First of all, what is the policy is a problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_5701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_584D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57CF")

    ChrTalk(
        0xFE,
        (
            "No, nonno cooks,\x01",
            "Is it somewhat too early to deploy …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, I guess\x01",
            "Will it be dried like this …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no no,\x01",
            "That's impossible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5848")

    label("loc_57CF")


    ChrTalk(
        0xFE,
        (
            "No matter how nonno can cook\x01",
            "It is too early to make dishes to serve customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I mean, what about my position?\x02",
    )

    CloseMessageWindow()

    label("loc_5848")

    Jump("loc_60B3")

    label("loc_584D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58FE")

    ChrTalk(
        0xFE,
        (
            "I did not mind at all,\x01",
            "Non-no-no guy, until noticing\x01",
            "It was supposed to be entrusted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way, as it is in the cook\x01",
            "Hey hey hey … hey ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B3")

    label("loc_58FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59CD")

    ChrTalk(
        0xFE,
        (
            "Welcome, if you enjoy in the shop\x01",
            "Attach to the vacant table everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you wish, now\x01",
            "We can also guide second-floor seats with priority for reservation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please feel free to call out.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A54")

    label("loc_59CD")


    ChrTalk(
        0xFE,
        (
            "No, ~, hospitality\x01",
            "It is such a fun thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Customers …… especially beautiful people\x01",
            "What is the smile of female customers?\x01",
            "It is an energy source that can not be changed anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A54")

    Jump("loc_60B3")

    label("loc_5A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5CA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C12")

    ChrTalk(
        0xFE,
        (
            "From the store manager, for a while\x01",
            "I was told to do a waiter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know what you're going to do,\x01",
            "Sometimes such work is also nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Female customers are unlimited,\x01",
            "In addition, I can do it truly.\x02",
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
            "#00006F(Customers are Nampa\x01",
            "It looks bad for drifting … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Yes, it's also seen\x01",
            "I feel restless. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5C9E")

    label("loc_5C12")


    ChrTalk(
        0xFE,
        (
            "I do not know what the manager is going to do,\x01",
            "Sometimes the waiter is also nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Female customers are unlimited,\x01",
            "In addition, I can do it truly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C9E")

    Jump("loc_60B3")

    label("loc_5CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5DDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5B")

    ChrTalk(
        0xFE,
        (
            "Cooking is art.\x01",
            "Creativity is important for anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time when the story of the new menu comes again,\x01",
            "Surely surprise the world\x01",
            "I will create the ultimate menu.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DD5")

    label("loc_5D5B")


    ChrTalk(
        0xFE,
        (
            "By the way, now the customer … …\x01",
            "Two girls on the entrance side table?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, wait ~.\x01",
            "I'm carrying cooking now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD5")

    Jump("loc_60B3")

    label("loc_5DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_60B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F09")

    ChrTalk(
        0xFE,
        (
            "Well, my new menu is\x01",
            "Where the hell did not go wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put together the taste and appearance properly,\x01",
            "More than anything, that glittery texture\x01",
            "I think that it was epoch - making.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(\"Gyuri\" … …?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(I'm not sure,\x01",
            "I do not think I want to eat it …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_60B3")

    label("loc_5F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6066")

    ChrTalk(
        0xFE,
        (
            "\"Dolo Bun Hime Stew\" Demon Beast Eye \"…\x01",
            "I thought that I opened up a new frontier.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F86")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5F86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FAC")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5FAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FD2")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5FD2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FF8")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5FF8")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F(That is a terrible naming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Huh, Terada\x01",
            "It looks like Geteonese food. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_60B3")

    label("loc_6066")


    ChrTalk(
        0xFE,
        (
            "\"Dolo Bun Hime Stew\" Demon Beast Eye \"…\x01",
            "I thought that I opened up a new frontier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B3")

    TalkEnd(0xFE)
    Return()

    # Function_10_4DFA end

    def Function_11_60B7(): pass

    label("Function_11_60B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6140")

    ChrTalk(
        0xFE,
        (
            "Hehe, Celteo.\x01",
            "I feel somewhat enthusiastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a situation full of anxiety, but … ….\x01",
            "I got a little cheerful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6206")

    ChrTalk(
        0xFE,
        (
            "Anomalous situation occurring in the city right now ……\x01",
            "This is because the government itself\x01",
            "It is a happening event, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The circumstances around us, more quickly and in detail\x01",
            "If you can tell me, a bit more\x01",
            "I should have suppressed confusion though ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_629A")

    ChrTalk(
        0xFE,
        (
            "Listen to the presidential speech\x01",
            "I thought that it was very wonderful … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the store manager says, I feel honest\x01",
            "It is confusing because there are too many elements.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_629A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6372")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62CC")
    Call(0, 43)
    Return()

    label("loc_62CC")


    ChrTalk(
        0xFE,
        (
            "It was a little over a month,\x01",
            "I was happy to have it in the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The store manager also said that,\x01",
            "I, once in a while, serve a cook\x01",
            "I think I aim for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_63CA")

    ChrTalk(
        0xFE,
        "People in Mainz … are worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am afraid I am hungry … ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_63CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647C")

    ChrTalk(
        0xFE,
        (
            "Recipes for cooking showdown,\x01",
            "Mr. Celtio is various\x01",
            "You seem to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am accustomed to making it simply from the usual way\x01",
            "I am planning to hit a good dish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64FC")

    label("loc_647C")


    ChrTalk(
        0xFE,
        (
            "Carbonara is good at me, pasta\x01",
            "I often make it for my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, with cooking showdown\x01",
            "I'm thinking of acting like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64FC")

    Jump("loc_6ED3")

    label("loc_6501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_656A")

    ChrTalk(
        0xFE,
        (
            "Sound of siren,\x01",
            "You can do it very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even though I was in the kitchen, I heard it clearly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_656A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6601")

    ChrTalk(
        0xFE,
        "Pervaded\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pepper in basil and besides\x01",
            "Sprinkle some salt a little … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, in this\x01",
            "The underlying meat is perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6662")

    label("loc_6601")


    ChrTalk(
        0xFE,
        "Pervaded\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next, let it sleep for about 30 minutes … …\x01",
            "In the meantime I cut vegetables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6662")

    Jump("loc_6ED3")

    label("loc_6667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67BC")

    ChrTalk(
        0xFE,
        (
            "Actually it's time for the hall\x01",
            "I was planning to go back but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The store manager asked me for a while\x01",
            "I decided to work in the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, Celteo's\x01",
            "For that in the future,\x01",
            "It is supposed to go out with cooking confrontation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehu, Celteo\x01",
            "It is bad as it seems to be deceiving,\x01",
            "Because it seemed to be fun, I accepted it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6861")

    label("loc_67BC")


    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "It is a dish that I was doing by extension,\x01",
            "It is fun to stand in the kitchen like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhuu, like this\x01",
            "I wonder if you seriously aim for a cook.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6861")

    Jump("loc_6ED3")

    label("loc_6866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6933")

    ChrTalk(
        0xFE,
        (
            "Mr. Brown suddenly asked Mr. Brown\x01",
            "I decided to try cooking though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I'm really something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, to expectation\x01",
            "I will do my utmost to respond.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_698C")

    label("loc_6933")


    ChrTalk(
        0xFE,
        (
            "Um, first of all\x01",
            "Give the ingredients a flavor and then ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, I am nervous about cooking stones.\x02",
    )

    CloseMessageWindow()

    label("loc_698C")

    Jump("loc_6ED3")

    label("loc_6991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6A0B")

    ChrTalk(
        0xFE,
        (
            "After finishing this preparation\x01",
            "Next, wash the dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fu … … after all\x01",
            "Dinner time is busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AAE")

    ChrTalk(
        0xFE,
        (
            "Er, this vegetable\x01",
            "Fire is hard to pass\x01",
            "You had better put a hidden kitchen knife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sakusakutsu su ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, this is OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6AF4")

    label("loc_6AAE")


    ChrTalk(
        0xFE,
        "Ton Ton Ton Tsu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, I guess the chopped one is like this.\x02",
    )

    CloseMessageWindow()

    label("loc_6AF4")

    Jump("loc_6ED3")

    label("loc_6AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6B9C")

    ChrTalk(
        0xFE,
        (
            "Instead of Celtio\x01",
            "I decided to help a little kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although basically it is a dish washing,\x01",
            "The rest is easy help\x01",
            "It's a nice place though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED3")

    label("loc_6B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7E")

    ChrTalk(
        0xFE,
        (
            "Mr. Celteo, as usual\x01",
            "When I came out of the kitchen, I got a table seat\x01",
            "It seems that she sees the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not been asked again today\x01",
            "Do you intend to carry cooking by yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, that person also does not care.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D00")

    label("loc_6C7E")


    ChrTalk(
        0xFE,
        (
            "Mr. Celteo, as usual\x01",
            "When I came out of the kitchen, I got a table seat\x01",
            "It seems that she sees the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, that person also does not care.\x02",
    )

    CloseMessageWindow()

    label("loc_6D00")

    Jump("loc_6ED3")

    label("loc_6D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6ED3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E11")

    ChrTalk(
        0xFE,
        (
            "Mr. Frote who is in the back seat\x01",
            "This shop's regulars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always come to the shop as soon as you open\x01",
            "You can sit in there all day\x01",
            "It is not uncommon ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you get crowded you can remove your seat,\x01",
            "Sometimes I order additional order,\x01",
            "It's pretty careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6ED3")

    label("loc_6E11")


    ChrTalk(
        0xFE,
        (
            "Mr. Floté is always open at the same time\x01",
            "Come to the shop and stay as is\x01",
            "It is not uncommon to sit there … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you get crowded you can remove your seat,\x01",
            "Sometimes I order additional order,\x01",
            "It's pretty careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED3")

    TalkEnd(0xFE)
    Return()

    # Function_11_60B7 end

    def Function_12_6ED7(): pass

    label("Function_12_6ED7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_701A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F8E")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A pale big tree, or …\x01",
            "Recently what is real and what is dream,\x01",
            "I feel a bit less confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A little more\x01",
            "Would you like me to keep caffeine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7015")

    label("loc_6F8E")


    ChrTalk(
        0xFE,
        (
            "A pale big tree, or …\x01",
            "Recently what is real and what is dream,\x01",
            "I feel a bit less confident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A little more\x01",
            "Would you like me to keep caffeine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7015")

    Jump("loc_7FDB")

    label("loc_701A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_71DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7137")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… while going to the toilet\x01",
            "Moya came out and I could not get out\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rather than why\x01",
            "It is like such a weapon of human type\x01",
            "Are you wandering around the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even from two major countries\x01",
            "Even if it is to protect the city,\x01",
            "I will demand a proper explanation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_71DA")

    label("loc_7137")


    ChrTalk(
        0xFE,
        (
            "Even if we use weapons like \"Shinkansen\"\x01",
            "Even with the barrier covering the city,\x01",
            "I will demand a proper explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead of protecting the city in this case,\x01",
            "Rather, are not you in danger?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71DA")

    Jump("loc_7FDB")

    label("loc_71DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72DD")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter in the Crossbell independent country,\x01",
            "And Secretary of Defense Arios,?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that only names and titles are splendid,\x01",
            "I wonder if it guards us properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Just looking around,\x01",
            "It really does not get stylish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_738C")

    label("loc_72DD")


    ChrTalk(
        0xFE,
        (
            "Independent nation, President or Secretary of Defense … …\x01",
            "It seems that only names and titles are splendid,\x01",
            "I wonder if it guards us properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Just looking around,\x01",
            "It really does not get stylish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_738C")

    Jump("loc_7FDB")

    label("loc_7391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_756D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7493")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Receiving some other recent raid incident\x01",
            "It seems that independent proponents are excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I do not know the feelings,\x01",
            "I wonder if we can argue more intelligently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Emotional theory destroys the body …\x01",
            "I feel like someone was saying that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7568")

    label("loc_7493")


    ChrTalk(
        0xFE,
        (
            "Receiving some other recent raid incident\x01",
            "It seems that independent proponents are excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I do not know the feelings,\x01",
            "I wonder if we can argue more intelligently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Emotional theory destroys the body …\x01",
            "I feel like someone was saying that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7568")

    Jump("loc_7FDB")

    label("loc_756D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7622")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group in Mainz ……\x01",
            "It is already rumored already in part,\x01",
            "I wonder if it is a conspiracy of the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Accept the military stationed instead of helping\"\x01",
            "…… Although it can not be laughed, it seems likely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_7622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_774D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_770D")

    ChrTalk(
        0xFE,
        (
            "Today is from the morning, in the direction of the city hall\x01",
            "A citizen forum with the theme of national independence\x01",
            "It seems to be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I do not participate in a forum separately\x01",
            "I am going to know the point of independence,\x01",
            "Would you like to have a look out a little?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7748")

    label("loc_770D")


    ChrTalk(
        0xFE,
        (
            "Is it a citizen forum …?\x01",
            "Would you like to have a look out a little?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7748")

    Jump("loc_7FDB")

    label("loc_774D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_77A3")

    ChrTalk(
        0xFE,
        "Somewhat outside is noisy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will not drink coffee calmly.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_77A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_78EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7873")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Renewal version of alkane shell\x01",
            "I wonder if tomorrow was the release date.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was also aiming for a ticket ……\x01",
            "In the other 2 months' coming soon\x01",
            "What does it mean to be sold out?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_78E5")

    label("loc_7873")


    ChrTalk(
        0xFE,
        (
            "Huh, well … separately\x01",
            "Even if you do not see an alkane shell\x01",
            "Because human beings will not die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wow, but I wanted to see it to death.\x02",
    )

    CloseMessageWindow()

    label("loc_78E5")

    Jump("loc_7FDB")

    label("loc_78EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7978")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is national independence.\x01",
            "There is no care for if simply carrying things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am concerned about security in anyway.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7A23")

    label("loc_7978")


    ChrTalk(
        0xFE,
        (
            "Personally, in the Empire and the Republic\x01",
            "It is also possible to entrust security\x01",
            "I do not think it's a bad thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, historical history is historical,\x01",
            "It is reality that it will not work so easily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A23")

    Jump("loc_7FDB")

    label("loc_7A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC4")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even so, the city is staggering.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was in a police officer like that,\x01",
            "You can not walk around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7B1D")

    label("loc_7AC4")


    ChrTalk(
        0xFE,
        "In that respect, the inside of the shop will settle down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, today as well.\x01",
            "I have a meaningful reading time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B1D")

    Jump("loc_7FDB")

    label("loc_7B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7BC6")

    ChrTalk(
        0xFE,
        (
            "Today, I am keen on reading\x01",
            "I stayed until the sunset for the first time in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is bad for shopkeepers as well as flowing stones,\x01",
            "I wonder if I eat it evening supper as it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_7BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CA7")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is no unveiling ceremony nearby\x01",
            "Although I can not see it, everyone takes out the trouble\x01",
            "It is hard work to go outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I used coffee here with one hand\x01",
            "On the next Crossbell Times magazine,\x01",
            "I am going to show you gracefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D5B")

    label("loc_7CA7")


    ChrTalk(
        0xFE,
        (
            "There is no unveiling ceremony nearby\x01",
            "Although I can not see it, everyone takes out the trouble\x01",
            "It is hard work to go outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I used coffee here with one hand\x01",
            "On the next Crossbell Times magazine,\x01",
            "I am going to show you gracefully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D5B")

    Jump("loc_7FDB")

    label("loc_7D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7DC9")

    ChrTalk(
        0xFE,
        (
            "How come you have a cock today\x01",
            "I wonder if I am taking an order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am struggling to understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FDB")

    label("loc_7DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E74")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Inside the store on a rainy day, as usual\x01",
            "It's also nice to have a different taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bustle of the store and the rain sounds mix\x01",
            "I feel the best BGM.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7EF2")

    label("loc_7E74")


    ChrTalk(
        0xFE,
        (
            "Inside the store on a rainy day, as usual\x01",
            "It's also nice to have a different taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bustle of the store and the rain sounds mix\x01",
            "I feel the best BGM.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EF2")

    Jump("loc_7FDB")

    label("loc_7EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9A")

    ChrTalk(
        0xFE,
        "Well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after all\x01",
            "This shop is ideal for reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His favorite noise and doubt\x01",
            "Coffee will pay for drowsiness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7FDB")

    label("loc_7F9A")


    ChrTalk(
        0xFE,
        (
            "Come, stay tenacious today\x01",
            "I will read books borrowed from the library.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FDB")

    TalkEnd(0xFE)
    Return()

    # Function_12_6ED7 end

    def Function_13_7FDF(): pass

    label("Function_13_7FDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8052")

    ChrTalk(
        0xFE,
        (
            "Yeah, it's raining.\x01",
            "I have not heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a pleasant trip.\x01",
            "What will you do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_809C")

    label("loc_8052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_809C")

    ChrTalk(
        0xFE,
        (
            "That's right, and the price is not too expensive.\x01",
            "You may want to get through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809C")

    TalkEnd(0xFE)
    Return()

    # Function_13_7FDF end

    def Function_14_80A0(): pass

    label("Function_14_80A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8125")

    ChrTalk(
        0xFE,
        (
            "Yeah yeah, I know.\x01",
            "Do not get me involved in bitches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is rain, how to enjoy indoors with rain\x01",
            "You just think about it, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818C")

    label("loc_8125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_818C")

    ChrTalk(
        0xFE,
        (
            "This shop,\x01",
            "I want to take it in Frank\x01",
            "Cooking is pretty authentic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe he likes it.\x02",
    )

    CloseMessageWindow()

    label("loc_818C")

    TalkEnd(0xFE)
    Return()

    # Function_14_80A0 end

    def Function_15_8190(): pass

    label("Function_15_8190")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_81C1")

    ChrTalk(
        0xFE,
        "Hehe, you are tasty.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8229")

    label("loc_81C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8229")

    ChrTalk(
        0xFE,
        (
            "You bother for me,\x01",
            "Thank you for reserving your seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I always thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_8229")

    TalkEnd(0xFE)
    Return()

    # Function_15_8190 end

    def Function_16_822D(): pass

    label("Function_16_822D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8289")

    ChrTalk(
        0xFE,
        "Well, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, most likely\x01",
            "I will lose to your cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EE")

    label("loc_8289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_82EE")

    ChrTalk(
        0xFE,
        "Waah, what kind of thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Likewise,\x01",
            "Always doing something about my house\x01",
            "I am grateful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82EE")

    TalkEnd(0xFE)
    Return()

    # Function_16_822D end

    def Function_17_82F2(): pass

    label("Function_17_82F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8360")

    ChrTalk(
        0xFE,
        (
            "Open the menu and click\x01",
            "He who pointed, I will ask for it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay, first, keep your eyes closed ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8413")

    label("loc_8360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_836E")
    Jump("loc_8413")

    label("loc_836E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_83D1")

    ChrTalk(
        0xFE,
        "Yosh, I'm going to make fish today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There, but today\x01",
            "Is this deals a great deal ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8413")

    label("loc_83D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8413")

    ChrTalk(
        0xFE,
        (
            "Well, what shall I do.\x01",
            "Well, I want to eat anything ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8413")

    TalkEnd(0xFE)
    Return()

    # Function_17_82F2 end

    def Function_18_8417(): pass

    label("Function_18_8417")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8459")

    ChrTalk(
        0xFE,
        (
            "you……\x01",
            "Does not matter, so do you make it sooner?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84E3")

    label("loc_8459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8467")
    Jump("loc_84E3")

    label("loc_8467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_849D")

    ChrTalk(
        0xFE,
        "Huh, you are really indecisive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_84E3")

    label("loc_849D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_84E3")

    ChrTalk(
        0xFE,
        (
            "You … … Are you going to do so?\x01",
            "I have already decided.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84E3")

    TalkEnd(0xFE)
    Return()

    # Function_18_8417 end

    def Function_19_84E7(): pass

    label("Function_19_84E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8547")

    ChrTalk(
        0xFE,
        (
            "Er, the first day\x01",
            "What I am talking about is different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Boobooo, you are bad cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E7")

    label("loc_8547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8555")
    Jump("loc_85E7")

    label("loc_8555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_85AD")

    ChrTalk(
        0xFE,
        "Mogmog …… ah, happiness ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After all, the real thrill of travel is meal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E7")

    label("loc_85AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_85E7")

    ChrTalk(
        0xFE,
        (
            "Hehe, I did it ♪\x01",
            "Distraction is a lovable darling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E7")

    TalkEnd(0xFE)
    Return()

    # Function_19_84E7 end

    def Function_20_85EB(): pass

    label("Function_20_85EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_867D")

    ChrTalk(
        0xFE,
        (
            "Well, it is.\x01",
            "It's very hard to say\x01",
            "Travel expenses are pretty exciting ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So as much as possible\x01",
            "Reasonable menu ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_877D")

    label("loc_867D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_868B")
    Jump("loc_877D")

    label("loc_868B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8717")

    ChrTalk(
        0xFE,
        (
            "Well, but again\x01",
            "From expensive menus one after another ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is a pleasant trip.\x01",
            "Let's not care about the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_877D")

    label("loc_8717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_877D")

    ChrTalk(
        0xFE,
        (
            "Now, like whatever you like\x01",
            "Just ask him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a pleasant trip.\x02",
    )

    CloseMessageWindow()

    label("loc_877D")

    TalkEnd(0xFE)
    Return()

    # Function_20_85EB end

    def Function_21_8781(): pass

    label("Function_21_8781")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_87CD")

    ChrTalk(
        0xFE,
        (
            "Well, no doubt while traveling\x01",
            "It seems like this happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_87CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8827")

    ChrTalk(
        0xFE,
        (
            "Well, today is\x01",
            "Give up going out towards the highway\x01",
            "I wonder if I even shop in the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_8827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_887B")

    ChrTalk(
        0xFE,
        (
            "I am an ambulance,\x01",
            "Because it seems I passed a few items\x01",
            "I do not seem to be a sick person … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_887B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_88FD")

    ChrTalk(
        0xFE,
        (
            "Well, today as well.\x01",
            "I will look around various places ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First of all, to replenish the photosensitive quartz,\x01",
            "I wonder to drop in at the oval store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8994")

    label("loc_88FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8994")

    ChrTalk(
        0xFE,
        (
            "Given the recent security of Crossbell,\x01",
            "I also thought about the trip … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all it was a correct answer.\x01",
            "She is also very pleased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8994")

    TalkEnd(0xFE)
    Return()

    # Function_21_8781 end

    def Function_22_8998(): pass

    label("Function_22_8998")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8A2B")

    ChrTalk(
        0xFE,
        (
            "Today we are in Mainz\x01",
            "I was going to go see it ….\x01",
            "I can not go in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, the residents are worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8AB4")

    ChrTalk(
        0xFE,
        (
            "Is not it\x01",
            "On the day to go out to the suburbs\x01",
            "I will not let it rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Am I a rain girl?\x01",
            "Or … Or is he rain?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8AFF")

    ChrTalk(
        0xFE,
        (
            "It is the sound of an ambulance just before.\x01",
            "What on earth was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8B8B")

    ChrTalk(
        0xFE,
        (
            "Yesterday I took a picture of the Orchis Tower\x01",
            "I took it from various places in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if you notice photosensitive quartz\x01",
            "I used two of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF7")

    label("loc_8B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8BF7")

    ChrTalk(
        0xFE,
        "Huhu, Cross Bell is a nice place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As much as possible go to various places,\x01",
            "I will make a lot of memories ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF7")

    TalkEnd(0xFE)
    Return()

    # Function_22_8998 end

    def Function_23_8BFB(): pass

    label("Function_23_8BFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8C76")

    ChrTalk(
        0xFE,
        (
            "President Dieter's speech,\x01",
            "It rings to my heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our citizens can do,\x01",
            "I have to cooperate with everything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CEB")

    label("loc_8C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8CEB")

    ChrTalk(
        0xFE,
        (
            "Anything that raid incident,\x01",
            "It seems that it was the work of the empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not forgive you.\x01",
            "What on earth are you going to do! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CEB")

    TalkEnd(0xFE)
    Return()

    # Function_23_8BFB end

    def Function_24_8CEF(): pass

    label("Function_24_8CEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8DA6")

    ChrTalk(
        0xFE,
        (
            "Is it independent? … Of course\x01",
            "I wonder what will be tough in the future\x01",
            "I feel bad now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We will now have true freedom\x01",
            "When I thought that I was grabbing it,\x01",
            "Courage comes from the depths of your heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E51")

    label("loc_8DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8E51")

    ChrTalk(
        0xFE,
        (
            "Hire armed groups\x01",
            "To attack the city … …\x01",
            "Doing seriously is not dirty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I occasionally forget it,\x01",
            "The Eleventh Empire is\x01",
            "A ridiculous invasion nation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E51")

    TalkEnd(0xFE)
    Return()

    # Function_24_8CEF end

    def Function_25_8E55(): pass

    label("Function_25_8E55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E6A")
    Call(0, 30)
    Jump("loc_90B4")

    label("loc_8E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9078")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F05")
    Jump("loc_8F4F")

    label("loc_8F05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F25")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4F")

    label("loc_8F25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F45")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4F")

    label("loc_8F45")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F4F")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#02306FKun, I can not wait to be supervised by the boss at all times\x01",
            "Uza something else … …\x02\x03",
            "#02310FRemember, Tio …!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#00203FWell, let's go everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#02306FHey, ignorance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109F(Well, surely Tio-chan ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    Jump("loc_90B4")

    label("loc_9078")

    SetChrSubChip(0x19, 0x0)

    ChrTalk(
        0x19,
        (
            "#02306FGood, that is ……\x01",
            "Eat yourself! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90B4")

    TalkEnd(0xFE)
    Return()

    # Function_25_8E55 end

    def Function_26_90B8(): pass

    label("Function_26_90B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90CD")
    Call(0, 30)
    Jump("loc_9339")

    label("loc_90CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C7")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9168")
    Jump("loc_91B2")

    label("loc_9168")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9188")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B2")

    label("loc_9188")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91A8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B2")

    label("loc_91A8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91B2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Tio, do not worry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will take responsibility for Jonah\x01",
            "I will take care of you!\x02",
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
            "#00006F(Tio, how to handle the boss\x01",
            "I feel like I'm getting better … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_9339")

    label("loc_92C7")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hey Hey, Jonah!\x01",
            "Green peppers and carrots are delicious ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What was that?\x01",
            "Shall I give it to you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9339")

    TalkEnd(0xFE)
    Return()

    # Function_26_90B8 end

    def Function_27_933D(): pass

    label("Function_27_933D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9436")

    ChrTalk(
        0xFE,
        (
            "As a city official\x01",
            "I had evacuation guidance\x01",
            "I myself have been evacuated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In anticipation of it,\x01",
            "My wife and Mimi to me\x01",
            "It came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering safety\x01",
            "I wanted you to be waiting at home, but …\x01",
            "Honestly I am happy that I can stay with my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_94EE")

    label("loc_9436")


    ChrTalk(
        0xFE,
        (
            "Considering safety\x01",
            "I wanted you to be waiting at home, but …\x01",
            "Honestly I am happy that I can stay with my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People in the restaurant, too\x01",
            "It is warm and good people,\x01",
            "Even under such circumstances feelings will be saved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94EE")

    TalkEnd(0xFE)
    Return()

    # Function_27_933D end

    def Function_28_94F2(): pass

    label("Function_28_94F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9615")

    ChrTalk(
        0xFE,
        (
            "Because my husband's returning is late\x01",
            "I picked it up with my child … …\x01",
            "That Moya was truly amazed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, that eerie doll is\x01",
            "Not to recognize citizens and attack them\x01",
            "It seems to be done … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, to that doll\x01",
            "The fear of being sent a gaze is\x01",
            "It was hard to say anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_9667")

    label("loc_9615")


    ChrTalk(
        0xFE,
        (
            "Huhu, even so\x01",
            "After all the children are cute.\x01",
            "I feel happy even at such times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9667")

    TalkEnd(0xFE)
    Return()

    # Function_28_94F2 end

    def Function_29_966B(): pass

    label("Function_29_966B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hey, he's that.\x01",
            "People in the shop for Mimi\x01",
            "It was a treat for Gohan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It was very tasty, too.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_966B end

    def Function_30_96F0(): pass

    label("Function_30_96F0")

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
            "#11PHello, Tio you guys\x01",
            "is not it~!\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9868")
    Jump("loc_98B2")

    label("loc_9868")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9888")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98B2")

    label("loc_9888")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98A8")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_98B2")

    label("loc_98A8")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_98B2")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        "#5P#02302FWell, after a long absence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FRoberts, and Jonah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FDid you come for meals with two people?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11POh, sometimes to Jonah\x01",
            "A good balance of nutrition\x01",
            "I want to eat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWhatever you do with Jonah,\x01",
            "Even at the Foundation headquarters in Leman\x01",
            "Because he seems to have been eating pizza.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00203FOh, that 's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FTo that extent, too much vegetables\x01",
            "It seems I have not put my hands on?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x19, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00105FOh, really.\x01",
            "Leave the green pepper and the carrot ……\x02\x03",
            "#00106FJonah, you do not like picky things.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B6F")
    Jump("loc_9BB9")

    label("loc_9B6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B8F")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BB9")

    label("loc_9B8F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BAF")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BB9")

    label("loc_9BAF")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9BB9")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#5P#02306FHun, I do not care whatever I eat.\x02\x03",
            "Approximately, I bother to come to the restaurant\x01",
            "To eat with a knife and a fork,\x01",
            "Waste of time is also a problem.\x02\x03",
            "#02309FAfter all, even while operating the terminal\x01",
            "Pizza is easier to eat … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    ChrTalk(
        0x1A,
        (
            "#11PSounds like that … ….\x01",
            "This delicious vegetables\x01",
            "I do not agree with Jonah's mouth … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11POh, it's my responsibility!\x01",
            "I will give you good things for Jonah\x01",
            "I thought you could eat me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PIn this way, collect the chefs on the continent\x01",
            "Jonah like your mouth as if anything\x01",
            "I only have vegetables cooked …! It is!\x02",
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
            "#5P#02301F…… ah, now,\x01",
            "It is troublesome Osan!\x02\x03",
            "Without liking and disliking\x01",
            "You ought to eat it, do not you eat it!\x02\x03",
            "#02306Fぱ く ぱ く …… ugly, bitter ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FHaha, I still want to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206F… …. Gooday.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A00E")
    Jump("loc_A058")

    label("loc_A00E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A02E")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A058")

    label("loc_A02E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A04E")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A058")

    label("loc_A04E")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A058")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#5P#02305FMunching … … gargle.\x01",
            "… Oh, that's right.\x02\x03",
            "#02301FYou, Michelam\x01",
            "I was involved in the tower incident\x01",
            "Do not you know the whereabouts of \"clown\"?\x02",
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

    def lambda_A181():
        TurnDirection(0x0, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A181)
    Sleep(50)

    def lambda_A191():
        TurnDirection(0x1, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_A191)
    Sleep(50)

    def lambda_A1A1():
        TurnDirection(0x2, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_A1A1)
    Sleep(50)

    def lambda_A1B1():
        TurnDirection(0x3, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_A1B1)
    Sleep(50)

    def lambda_A1C1():
        TurnDirection(0x4, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_A1C1)
    Sleep(50)

    def lambda_A1D1():
        TurnDirection(0x5, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x5, 0, lambda_A1D1)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    WaitChrThread(0x4, 0)
    WaitChrThread(0x5, 0)

    ChrTalk(
        0x101,
        "#6P#00003F…… No, I do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108F(I met with Michelin, but …\x01",
            "Truly with a bellaby\x01",
            "Is not it a thing to say? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#02306FIt looks chic, is not it?\x02\x03",
            "#02310FThat \"clown\", since the tower incident\x01",
            "I do not appear in the power net.\x02\x03",
            "I have my bass\x01",
            "A thank you for choosing me\x01",
            "You can not go getting plenty … …\x02\x03",
            "If you grab something\x01",
            "Please give me information as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FWell, it is\x01",
            "I can not promise, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#02306FDo not be afraid … …\x01",
            "Just type it in the database\x01",
            "You just have to give up.\x02\x03",
            "#02309FAfter that I hacked on my own\x01",
            "I will make you see.\x02",
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
        "#12P#00306FCome on … …\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#6P#00206F…… Now we are in the branch of the IBC building\x01",
            "It seems I am indebted to you,\x01",
            "I should say that I should keep it a little.\x02\x03",
            "#00200FChief, Jonah properly\x01",
            "Please keep an eye on me.\x02\x03",
            "#00203FCurrently the basic conduct guidelines law was enacted,\x01",
            "If you discover explicit hacking behavior\x01",
            "Because it can not be overlooked as expected.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x1)

    ChrTalk(
        0x1A,
        "#11PI understood, Tio!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A, 0x0)

    ChrTalk(
        0x1A,
        (
            "#11PJonah, I have responsibility\x01",
            "I will keep you watching over the clock!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#5P#02305FHey, Tio …\x01",
            "Truly this is terrible! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    ChrTalk(
        0x103,
        "#5P#00203FLet's go, everyone.\x02",
    )

    CloseMessageWindow()

    def lambda_A71D():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A71D)
    Sleep(50)

    def lambda_A72D():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A72D)
    Sleep(50)

    def lambda_A73D():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A73D)
    Sleep(50)

    def lambda_A74D():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A74D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#12P#00005FOh, ah ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302F(Huh, I often pressed the boss well.\x02",
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

    # Function_30_96F0 end

    def Function_31_A7F3(): pass

    label("Function_31_A7F3")

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
        "#11P#00305FOh it's Kilika!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLong time no see Kilika\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12002FOh it's you guys\x02\x03",
            "#12004FHuh, I'm grateful.\x01",
            "It is strange to see him in such a place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003FIf you follow eyewitness testimonials\x01",
            "I reached here.\x02\x03",
            "#00001FIt's been since the auctioneer.\x01",
            "…… Locksmith chief engine manager,\x01",
            "Kirika · Lawran.\x02",
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
            "Well, when I saw you before\x01",
            "The position is also different - again\x01",
            "Let me introduce myself.\x02\x03",
            "In the Republic of Calvert\x01",
            "He is presidential aide,\x01",
            "Kirika Lawran.\x02\x03",
            "I have other titles ….\x01",
            "Well it is not to talk daringly.\x02",
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
            "#00100FBy the way, I mentioned earlier\x01",
            "What is an entertainer producer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6P#12004FHuhu, it also\x01",
            "It is one of certain titles.\x02\x03",
            "#12002FNaturally even the office,\x01",
            "It exists in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F--I see.\x01",
            "There is not much elbow around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe, the face of the table\x01",
            "Is it a woman intelligence officer who uses more than one? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00309F(Well, that kind of mysterious\x01",
            "Kirika may also be nice. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Senpai, that remark to the drift\x01",
            "It seems like lack of tension … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105Fby the way……\x01",
            "I am visiting as presidential aide to the president\x01",
            "Why are you living in such a place?\x02\x03",
            "Today Rock Smith President\x01",
            "If you are observing IBC\x01",
            "I was listening … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12004FI got that little president\x01",
            "I have been asked to use it.\x02\x03",
            "#12000FShopping with an encounter,\x01",
            "Late lunch here\x01",
            "I have you take me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWhat thing\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6P#12004FThis\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kirika is a windmill#4RTankaguruma#Take out\x01",
            "I blew my breath away.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The windmill's feathers spun.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10105FP-pinwheel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12000FA stall vanishes with a limousine going out,\x01",
            "It seems that she wanted to be asexual.\x02\x03",
            "Before we meet tomorrow's plenary session,\x01",
            "As a relaxing item\x01",
            "It seems like you want to keep it at hand.\x02\x03",
            "#12004FIn addition, for dinner of a dinner of tonight\x01",
            "Together with fruits.\x02",
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
            "#11P#00306FWhat, what ….\x01",
            "Is not it really used?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuhu, as expected, known for the common people\x01",
            "I feel like President Rock Smith.\x02\x03",
            "#10304FThat is when you came out of town\x01",
            "If it was a real purpose#8R噵 噵 噵 噵#, Although that's story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12004FHah, well youi'll have to guess a bit more\x02\x03",
            "#12000FWell, the meal has ended\x01",
            "I will be rude about that.\x02\x03",
            "You guys also have security during trade conference\x01",
            "Good luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FYes.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1800, 6500, 17260, 1000)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2610, 5000, 17800, 180)
    Sleep(1200)

    def lambda_B2B0():

        label("loc_B2B0")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2B0")

    QueueWorkItem2(0x101, 2, lambda_B2B0)

    def lambda_B2C2():

        label("loc_B2C2")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2C2")

    QueueWorkItem2(0x102, 2, lambda_B2C2)

    def lambda_B2D4():

        label("loc_B2D4")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2D4")

    QueueWorkItem2(0x104, 2, lambda_B2D4)

    def lambda_B2E6():

        label("loc_B2E6")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2E6")

    QueueWorkItem2(0x109, 2, lambda_B2E6)

    def lambda_B2F8():

        label("loc_B2F8")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_B2F8")

    QueueWorkItem2(0x105, 2, lambda_B2F8)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_B39D")
    Call(0, 32)
    Jump("loc_B3A0")

    label("loc_B39D")

    Sleep(1000)

    label("loc_B3A0")

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

    # Function_31_A7F3 end

    def Function_32_B3EB(): pass

    label("Function_32_B3EB")

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
            "#00003FLechter, and Kilika\x02\x03",
            "Empire and republican intelligence agents,\x01",
            "At similar timing\x01",
            "I was out in the city.\x02\x03",
            "#00001FWhat do you guys think\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_B4CB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B4CB)
    Sleep(50)

    def lambda_B4DB():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B4DB)
    Sleep(50)

    def lambda_B4EB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B4EB)
    Sleep(50)

    def lambda_B4FB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B4FB)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10103FI think it's all awfully suspicious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, if you were like this\x01",
            "Do you want to track them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FBut this is getting more complicated\x02\x03",
            "#00103FNeither of us gets to you\x01",
            "It was kind of like I knew … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F… … For Dudley\x01",
            "Would you like to go report it?\x02\x03",
            "#00000FTogether with the information of the investigation department\x01",
            "You may understand something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FYes, let's do that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOkay, if you decide so\x01",
            "Try going to the police headquarters.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_32_B3EB end

    def Function_33_B6D8(): pass

    label("Function_33_B6D8")

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
            "Welcome.\x01",
            "Welcome to \"Van Set\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Do you have a reservation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, did everyone do that?\x01",
            "I'm telling you the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, on an empty table\x01",
            "Please attach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This season's new work of our shop, \"Herb Pasta\"\x01",
            "I will prepare you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, thank you.\x02",
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
            "Lloyd 's table seat,\x01",
            "I ate herbal pasta.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00200FMunching …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, our chef\x01",
            "How about pasta which boasts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FYes, it is very tasty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, I have a rich body\x01",
            "I also have a bit of aftertaste.\x02\x03",
            "#10300FHerbs are cool and cool\x01",
            "You can enjoy the texture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh, this restaurant\x01",
            "After all it is the taste of the iron plate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, please enjoy it\x01",
            "It is most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, this time Ka'a-chan\x01",
            "I have to bring along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, let 's do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, all the staff,\x01",
            "I will be waiting for another visit.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_BEC3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_BEE0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_BEF3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BEF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_BF06")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_BF23")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_BF36")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_BF53")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_BF66")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_BF83")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_BF96")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BF96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_BFB3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BFB3")

    OP_29(0x80, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0B6")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C0AD")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C0AD")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_C0B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C187")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_C187")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C1A9")
    Jump("loc_C311")

    label("loc_C1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C1CE")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_C311")

    label("loc_C1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C1DC")
    Jump("loc_C311")

    label("loc_C1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C1EA")
    Jump("loc_C311")

    label("loc_C1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C226")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C262")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C29E")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C2DA")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_C311")

    label("loc_C2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C311")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)

    label("loc_C311")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -510, 0, 9440, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_B6D8 end

    def Function_34_C341(): pass

    label("Function_34_C341")

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
        "#00005FAh……\x02",
    )

    CloseMessageWindow()

    def lambda_C564():
        OP_93(0x102, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C564)
    Sleep(50)

    def lambda_C574():
        OP_93(0x103, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C574)
    Sleep(50)

    def lambda_C584():
        OP_93(0x104, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C584)
    Sleep(50)

    def lambda_C594():
        OP_93(0x109, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C594)
    Sleep(50)

    def lambda_C5A4():
        OP_93(0x105, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C5A4)
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
        "host?",
        (
            "…… Haha, Margaret's\x01",
            "You have the same kind of eyes.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "host?",
        (
            "What is it like to say such a thing,\x01",
            "It is a waste for my current husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Okho …\x01",
            "As you are good at everyday,\x01",
            "Mr. Clyde … …\x02",
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
            "#00100FApparently, the wife of deputy director\x01",
            "He seems to be wrong with that person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FThen, sitting opposite you\x01",
            "Could it be a host \"Clyde\"?\x02\x03",
            "#10303FWell, I do not remember anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, so as not to be disturbed\x01",
            "Let's sit in a nearby table.\x02\x03",
            "#00001FI might be able to hear some information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FIt is good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell then, properly divided\x01",
            "Let's sit down.\x02",
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
            "Oh yeah, I got it this long\x01",
            "I had you see the pamphlet … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "I saw the pictures and I liked it at first sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "I am honored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Well then, by all means\x01",
            "Let's try going with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "If you would like the hotel too\x01",
            "I will arrange it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Ho ho ho, it does not reach it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "To tell the truth, I'm already doing previewing.\x01",
            "It's quite a scenery and I do not have any complaints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Oh, is that so!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "No, I am saved too!\x01",
            "But promise promptly too ……\x02",
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
        "#00001F(… … I'm pretty politely talking.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Together we go on a trip to Michelin\x01",
            "It seems like I'm making an appointment … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(For that, it looks like\x01",
            "I am funny though. )\x02",
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
            "#00303F(Men are\x01",
            "It is also politeness easily\x01",
            "Somehow it is anxious. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(But what is decisive is\x01",
            "I do not know yet ….)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Huh, well a little more\x01",
            "Let's try listening. )\x02",
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
        "… Well then, I will excuse myself today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Yes, I understand.\x01",
            "Well then, at that shop later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "It is \"Neue-Blanc\" in the entertainment district.\x01",
            "Huh, I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Have the wife's choice\x01",
            "Let's suppose to come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Well, I'm waiting.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x20, 1, 0, 41)
    Sleep(300)
    BeginChrThread(0x21, 1, 0, 42)
    Sleep(300)
    OP_68(-650, 1550, 7560, 3000)
    WaitChrThread(0x20, 1)
    Sleep(800)

    def lambda_CFC6():
        OP_95(0x20, 4230, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_CFC6)
    Sleep(200)
    WaitChrThread(0x21, 1)

    def lambda_CFE7():
        OP_95(0x21, 4230, 0, 7840, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_CFE7)
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

    def lambda_D064():
        OP_95(0x20, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D064)

    def lambda_D07E():
        OP_95(0x21, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D07E)
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
        "#00001F(Apparently it seems like leaving the store …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWhat are you doing, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(The definitive information is still\x01",
            "I did not get it … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(… … Let's train them.)\x02\x03",
            "#00000F(Me and Wadi, Randy is\x01",
            "A man named that Clyde. )\x02\x03",
            "(Eli and Tio, Noel\x01",
            "Follow Mrs. Margaret. )\x02\x03",
            "(But be careful not to be noticed\x01",
            "Take as much care as possible. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F(……I understand!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F(Well then, why do not you go.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F(Huh, I'm getting interesting.\x02",
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

    # Function_34_C341 end

    def Function_35_D2BA(): pass

    label("Function_35_D2BA")


    def lambda_D2BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D2BF)

    def lambda_D2D0():
        OP_95(0x101, 10110, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D2D0)
    WaitChrThread(0x101, 1)
    Return()

    # Function_35_D2BA end

    def Function_36_D2EA(): pass

    label("Function_36_D2EA")


    def lambda_D2EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D2EF)

    def lambda_D300():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D300)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, 10600, 0, 10450, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_36_D2EA end

    def Function_37_D330(): pass

    label("Function_37_D330")


    def lambda_D335():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D335)

    def lambda_D346():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D346)
    WaitChrThread(0x103, 1)
    OP_95(0xFE, 11310, 0, 7580, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_D330 end

    def Function_38_D376(): pass

    label("Function_38_D376")


    def lambda_D37B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D37B)

    def lambda_D38C():
        OP_95(0xFE, 11630, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D38C)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_38_D376 end

    def Function_39_D3AD(): pass

    label("Function_39_D3AD")


    def lambda_D3B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D3B2)

    def lambda_D3C3():
        OP_95(0xFE, 12860, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D3C3)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_D3AD end

    def Function_40_D3E4(): pass

    label("Function_40_D3E4")


    def lambda_D3E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D3E9)

    def lambda_D3FA():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D3FA)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, 12200, 0, 10670, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_D3E4 end

    def Function_41_D42A(): pass

    label("Function_41_D42A")

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

    # Function_41_D42A end

    def Function_42_D46E(): pass

    label("Function_42_D46E")

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

    # Function_42_D46E end

    def Function_43_D4B2(): pass

    label("Function_43_D4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D691")

    ChrTalk(
        0xB,
        "Welcome ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please sit down in your favorite seat.\x01",
            "I will order an order later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(If this person Miscon\x01",
            "In the \"waitress\" frame\x01",
            "It might be inviting. )\x02\x03",
            "#00000FExcuse me.\x01",
            "It is a little consultation … …\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Charity event\x01",
            "I asked for participation in Miscon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "Well, yeah?\x01",
            "Is participation in Miscon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yup……\x01",
            "I'm sorry but ….\x01",
            "I'm not a bit curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FIs that so …?\x01",
            "That was rude.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 5)
    Jump("loc_D706")

    label("loc_D691")


    ChrTalk(
        0xB,
        (
            "To participate in MISCON\x01",
            "I am not particularly interested in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As a waitress\x01",
            "If you only want to help\x01",
            "It might be nice, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D706")

    TalkEnd(0xB)
    Return()

    # Function_43_D4B2 end

    SaveToFile()

Try(main)
