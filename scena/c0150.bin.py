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
        "Function_5_E8E",          # 05, 5
        "Function_6_E92",          # 06, 6
        "Function_7_2A0D",         # 07, 7
        "Function_8_2A11",         # 08, 8
        "Function_9_4129",         # 09, 9
        "Function_10_5145",        # 0A, 10
        "Function_11_6565",        # 0B, 11
        "Function_12_73C7",        # 0C, 12
        "Function_13_8742",        # 0D, 13
        "Function_14_8813",        # 0E, 14
        "Function_15_8919",        # 0F, 15
        "Function_16_899E",        # 10, 16
        "Function_17_8A72",        # 11, 17
        "Function_18_8BC4",        # 12, 18
        "Function_19_8CB6",        # 13, 19
        "Function_20_8DEC",        # 14, 20
        "Function_21_8F9C",        # 15, 21
        "Function_22_9221",        # 16, 22
        "Function_23_94BB",        # 17, 23
        "Function_24_95C6",        # 18, 24
        "Function_25_970C",        # 19, 25
        "Function_26_9966",        # 1A, 26
        "Function_27_9BC5",        # 1B, 27
        "Function_28_9D9F",        # 1C, 28
        "Function_29_9F06",        # 1D, 29
        "Function_30_9F77",        # 1E, 30
        "Function_31_B03D",        # 1F, 31
        "Function_32_BC60",        # 20, 32
        "Function_33_BF56",        # 21, 33
        "Function_34_CC15",        # 22, 34
        "Function_35_DB43",        # 23, 35
        "Function_36_DB73",        # 24, 36
        "Function_37_DBB9",        # 25, 37
        "Function_38_DBFF",        # 26, 38
        "Function_39_DC36",        # 27, 39
        "Function_40_DC6D",        # 28, 40
        "Function_41_DCB3",        # 29, 41
        "Function_42_DCF7",        # 2A, 42
        "Function_43_DD3B",        # 2B, 43
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
            "==New Menu - Herb\x01",
            "Pasta==\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Herb Pasta recipe is\x01",
            "written here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_E8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Herb Pasta"\x07\x00\x01",
            "recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E8A")

    TalkEnd(0xFF)
    Return()

    # Function_4_DB1 end

    def Function_5_E8E(): pass

    label("Function_5_E8E")

    Call(0, 6)
    Return()

    # Function_5_E8E end

    def Function_6_E92(): pass

    label("Function_6_E92")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AF")

    ChrTalk(
        0x1F,
        (
            "Yo, Special Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I heard from Sergei. You\x01",
            "guys finally started\x01",
            "back up again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1F,
        (
            "Hmm? That redhead and the\x01",
            "young orbal staff user\x01",
            "aren't with you yet, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, those two have\x01",
            "personal business to\x01",
            "attend to.\x02",
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
            "And those two must be\x01",
            "the new members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I heard about your preferred\x01",
            "arms from Sergei. Come see if\x01",
            "there's anything you might like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, thanks for getting\x01",
            "everything ready for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 2)

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DC")
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
            "#00000FMr. Gironde, it's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12A9")

    ChrTalk(
        0x1F,
        (
            "Hehe, you look like you\x01",
            "can be trusted, same as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "But Dudley's with you\x01",
            "too? Could you have\x01",
            "already restarted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FYeah. It's a little\x01",
            "noisy so please forgive\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Heh, it's a little late\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well I've got everything\x01",
            "ready for you guys,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It was really no big\x01",
            "deal, but feel free to\x01",
            "have a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BB")

    label("loc_12A9")


    ChrTalk(
        0x1F,
        (
            "Hehe, you look like you\x01",
            "can be trusted, same as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "By the way, I heard about what's\x01",
            "going on from the police. No\x01",
            "need to say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well I got everything\x01",
            "ready for you guys,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It was really no big\x01",
            "deal, but feel free to\x01",
            "have a look around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BB")


    ChrTalk(
        0x101,
        "#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 0)

    label("loc_13DC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A09")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1438")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1457")
    OP_AF(0x5)
    Jump("loc_1499")

    label("loc_1457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1467")
    OP_AF(0x4)
    Jump("loc_1499")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1477")
    OP_AF(0x3)
    Jump("loc_1499")

    label("loc_1477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1487")
    OP_AF(0x2)
    Jump("loc_1499")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1497")
    OP_AF(0x1)
    Jump("loc_1499")

    label("loc_1497")

    OP_AF(0x0)

    label("loc_1499")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A04")

    label("loc_14A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BC")
    Jump("loc_2A04")

    label("loc_14BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A04")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15AD")

    ChrTalk(
        0x1F,
        (
            "*sigh*, that weird tree\x01",
            "aside, I feel like the\x01",
            "city's finally calmed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, it's gonna be a struggle from here\x01",
            "on out, but... With things like this,\x01",
            "each of us has to do the best we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_15AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_163B")

    ChrTalk(
        0x1F,
        (
            "Heh, but I have new\x01",
            "respect for the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Anyway guys, from now\x01",
            "on, give this everything\x01",
            "you have!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_163B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1825")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176A")

    ChrTalk(
        0x1F,
        (
            "Dieter Crois and the\x01",
            "State Guard have done an\x01",
            "outrageous thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "They even had special uniforms\x01",
            "ready, so they must've been\x01",
            "planning this for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It'd be better if they\x01",
            "didn't have weapons and\x01",
            "arms, but...\x02",
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
    Jump("loc_1820")

    label("loc_176A")


    ChrTalk(
        0x1F,
        (
            "It'd be better if they\x01",
            "didn't have weapons and\x01",
            "arms, but...\x02",
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
        (
            "Man oh man... I'm\x01",
            "worried about what's\x01",
            "going to happen next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1820")

    Jump("loc_2A04")

    label("loc_1825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1955")

    ChrTalk(
        0x1F,
        (
            "Many citizens came into the\x01",
            "store due to that disturbance\x01",
            "over at Mainz a while back.\x02",
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
            "Well, given the\x01",
            "situation, I understand\x01",
            "how they feel, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F2")

    label("loc_1955")


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
            "This is a good chance.\x01",
            "You guys should keep\x01",
            "that in mind yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F2")

    Jump("loc_2A04")

    label("loc_19F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD8")

    ChrTalk(
        0x1F,
        (
            "Hey, you've got those\x01",
            "gloomy looks on your\x01",
            "faces again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If you guys are going anywhere\x01",
            "dangerous, you'd best prepare\x01",
            "yourselves beforehand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Dead customers are bad\x01",
            "for business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B5B")

    label("loc_1AD8")


    ChrTalk(
        0x1F,
        (
            "If you guys are going anywhere\x01",
            "dangerous, you'd best prepare\x01",
            "yourselves beforehand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Dead customers are bad\x01",
            "for business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5B")

    Jump("loc_2A04")

    label("loc_1B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C92")

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
            "Heh, it's easy to say "an\x01",
            "ogre", but what the heck\x01",
            "are they talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's not the case that humans\x01",
            "can turn into ogres but...\x01",
            "Anyway, it's a disturbing story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D41")

    label("loc_1C92")


    ChrTalk(
        0x1F,
        (
            "Heh, it's easy to say "an\x01",
            "ogre", but what the heck\x01",
            "are they talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's not the case that humans\x01",
            "can turn into ogres but...\x01",
            "Anyway, it's a disturbing story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D41")

    Jump("loc_2A04")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DDB")

    ChrTalk(
        0x1F,
        (
            "Ahh, that annoying sound\x01",
            "must be a siren.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I don't know if it's an\x01",
            "accident or an incident, but...\x01",
            "It's really noisy in town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_1DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE4")

    ChrTalk(
        0x1F,
        "Oh, it's you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I don't care what you\x01",
            "want, but hurry up and\x01",
            "choose already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's hard to read my\x01",
            "magazine with you guys\x01",
            "standing there, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(...As usual, he has no\x01",
            "intention of doing a\x01",
            "proper job.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F74")

    label("loc_1EE4")


    ChrTalk(
        0x1F,
        (
            "I don't know what you\x01",
            "guys want, but hurry up\x01",
            "and choose already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "It's hard to read my\x01",
            "magazine with you guys\x01",
            "standing there, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F74")

    Jump("loc_2A04")

    label("loc_1F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_202C")

    ChrTalk(
        0x1F,
        (
            "*sigh*, we can't accept the\x01",
            "demands of the major powers, hence\x01",
            "the independence proposal, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Anyway, I just pray that\x01",
            "we can avoid a\x01",
            "declaration of war.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_202C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246D")

    ChrTalk(
        0x1F,
        (
            "Hey there young lady. Looks\x01",
            "like you've finally returned\x01",
            "to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "That man left some orbal\x01",
            "staves with me, so I thought\x01",
            "you might be stopping by.\x02",
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
            "#00203FYes, that was most likely\x01",
            "Chief Roberts.\x02\x03",
            "#00211FKnowing he'll be stopping\x01",
            "be here often makes me feel\x01",
            "annoyed for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FW-Well, he must be\x01",
            "worried about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, he's not that bad a\x01",
            "person. Actually, I think\x01",
            "he's a pretty good person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FI don't deny it. I think it's his excessive\x01",
            "nature that I don't like.\x02\x03",
            "#00200FAnd if you add his excessive interference and\x01",
            "frequent awkward chatting on top of that....\x01",
            "He's not someone I want to hang around with.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2326")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2326")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234C")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_234C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2372")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2372")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2398")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2398")

    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10103FI-I see. It seems\x01",
            "there'a a lot between\x01",
            "you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Bwah ha ha. I don't really get\x01",
            "it, but we'll have orbal staves\x01",
            "for sale from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If you ever need one,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 5)
    Jump("loc_24E7")

    label("loc_246D")


    ChrTalk(
        0x1F,
        (
            "Because you've returned,\x01",
            "young lady, we've resumed\x01",
            "dealing in orbal staves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If you need one, you\x01",
            "need only ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E7")

    Jump("loc_2A04")

    label("loc_24EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_26EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(
        0x1F,
        (
            "Hey, if it isn't Dudley.\x01",
            "A friendly stroll with\x01",
            "the Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FNo, there's something\x01",
            "I'm a tad concerned\x01",
            "about.\x02\x03",
            "#00600FSince I can't leave it\x01",
            "to just them, I'm going\x01",
            "along too. That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Oh, so you're the same\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, whatever. I'm about to\x01",
            "close up shop, so if you want\x01",
            "to have a look, do it quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26EA")

    label("loc_2662")


    ChrTalk(
        0x1F,
        (
            "I'm about to close up shop,\x01",
            "you see. If you want to\x01",
            "have a look, do it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I want to close up quick\x01",
            "and go have a drink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EA")

    Jump("loc_2A04")

    label("loc_26EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(
        0x1F,
        (
            "I don't know if it's due to the trade\x01",
            "conference or whatever, but those major\x01",
            "powers aren't to be taken lightly.\x02",
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
    Jump("loc_2A04")

    label("loc_27D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BE")

    ChrTalk(
        0x1F,
        (
            "With Revache gone, there's been fewer\x01",
            "gunfights in the underworld, but...\x01",
            "Things strangely seem more ominous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If things stay quiet like\x01",
            "this, I'll be out of business\x01",
            "before long. Am I dreaming?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2920")

    label("loc_28BE")


    ChrTalk(
        0x1F,
        (
            "I've had more free time\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Goddess, I beg of you.\x01",
            "Please, let me continue\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2920")

    Jump("loc_2A04")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_29AE")

    ChrTalk(
        0x1F,
        (
            "*sigh*, there's been a\x01",
            "lot of stormy weather\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Well, I guess it doesn't\x01",
            "matter 'cuz I've been\x01",
            "here all day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_29AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A04")

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
        "Come have a look.\x02",
    )

    CloseMessageWindow()

    label("loc_2A04")

    Jump("loc_13E6")

    label("loc_2A09")

    TalkEnd(0x1F)
    Return()

    # Function_6_E92 end

    def Function_7_2A0D(): pass

    label("Function_7_2A0D")

    Call(0, 8)
    Return()

    # Function_7_2A0D end

    def Function_8_2A11(): pass

    label("Function_8_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A48")
    Call(0, 33)
    Return()

    label("loc_2A48")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CBA")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, you're that police\x01",
            "unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I heard you guys are\x01",
            "separate from the State\x01",
            "Guard, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's right. We're\x01",
            "working to end this\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAre we inconveniencing\x01",
            "you somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. We're short-handed\x01",
            "right now, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although I think we're\x01",
            "doing better than other\x01",
            "places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is a restaurant, so\x01",
            "there's no need to worry about\x01",
            "getting something to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FI see. That's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIn any case, it's\x01",
            "dangerous to go outside\x01",
            "right now.\x02\x03",
            "#00100FPlease stand by here\x01",
            "with everyone.\x02",
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

    label("loc_2CBA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4125")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D16")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2D16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D35")
    OP_AF(0x9)
    Jump("loc_2D37")

    label("loc_2D35")

    OP_AF(0x8)

    label("loc_2D37")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4120")

    label("loc_2D46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D5A")
    Jump("loc_4120")

    label("loc_2D5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4120")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_2DD7")

    ChrTalk(
        0x8,
        (
            "By all means, please\x01",
            "come visit again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll be waiting for your\x01",
            "next visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_2DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EB9")

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
            "all its difficulties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if everyone works\x01",
            "together, there's\x01",
            "nothing we can't do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_2EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F95")

    ChrTalk(
        0x8,
        (
            "Hmm, but if the police\x01",
            "are here, that's very\x01",
            "reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, as the manager, I\x01",
            "have to take responsibility\x01",
            "for this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please be\x01",
            "careful when you're\x01",
            "walking around outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_2F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_31B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D6")

    ChrTalk(
        0x8,
        (
            "IBC declared an asset freeze... and\x01",
            "rail and bus services have been\x01",
            "suspended as of this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. In this situation,\x01",
            "it wouldn't be strange\x01",
            "if something did happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I intend to continue my business if\x01",
            "possible but... Honestly, there are\x01",
            "a lot of things I'm worried about.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31AF")

    label("loc_30D6")


    ChrTalk(
        0x8,
        (
            "IBC declared an asset freeze... and\x01",
            "rail and bus services have been\x01",
            "suspended as of this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I intend to continue my business if\x01",
            "possible but... Honestly, there are\x01",
            "a lot of things I'm worried about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AF")

    Jump("loc_4120")

    label("loc_31B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_33C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3318")

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
            "They insisted on it, so\x01",
            "we held it after closing\x01",
            "yesterday evening.\x02",
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
            "Haha, to think they've\x01",
            "become this good under\x01",
            "my tutelage.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33C1")

    label("loc_3318")


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
            "Three people in the kitchen...\x01",
            "I've got to think about how\x01",
            "this is going to go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C1")

    Jump("loc_4120")

    label("loc_33C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3454")

    ChrTalk(
        0x8,
        (
            "We have some Mainz\x01",
            "residents among our\x01",
            "customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know a lot of them\x01",
            "personally... and I'm\x01",
            "very worried about them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_3454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_35B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3530")

    ChrTalk(
        0x8,
        (
            "Haha, it seems Certeo is\x01",
            "thinking hard about\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I did that once, and the\x01",
            "answer came only after\x01",
            "worrying a whole bunch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think the experience\x01",
            "will be good for Certeo.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35B4")

    label("loc_3530")


    ChrTalk(
        0x8,
        (
            "I did that once, and the\x01",
            "answer came only after\x01",
            "worrying a whole bunch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think the experience\x01",
            "will be good for Certeo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B4")

    Jump("loc_4120")

    label("loc_35B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_371E")

    ChrTalk(
        0x8,
        (
            "I heard a train accident\x01",
            "occurred near West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It must've been falling rocks\x01",
            "that did it. It seems many people\x01",
            "were injured. I'm worried.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3719")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get\x01",
            "coverage for the gourmet\x01",
            "guide here, but...)\x02\x03",
            "#00003F(Now's not the time.\x01",
            "Let's not forget to stop\x01",
            "by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3719")

    Jump("loc_4120")

    label("loc_371E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3891")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3804")

    ChrTalk(
        0x8,
        (
            "Certeo's attitude towards work\x01",
            "has changed recently. It's like\x01",
            "he's a whole different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "His reactions towards our\x01",
            "attractive female customers\x01",
            "have disappeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, how wonderful.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_388C")

    label("loc_3804")


    ChrTalk(
        0x8,
        (
            "Until now, Certeo has been passionate\x01",
            "about women, but he's gradually\x01",
            "turned his passion towards cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, how wonderful.\x02",
    )

    CloseMessageWindow()

    label("loc_388C")

    Jump("loc_4120")

    label("loc_3891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3917")

    ChrTalk(
        0x8,
        (
            "Haha, it seems Certeo\x01",
            "has finally gotten\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At this rate, I have no\x01",
            "idea how the battle is\x01",
            "going to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4120")

    label("loc_3917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DA")

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
            "Hmm... Maybe what Certeo\x01",
            "was lacking all this\x01",
            "time was a rival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A9B")

    label("loc_39DA")


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
            "Hmm... Maybe what Certeo\x01",
            "was lacking all this\x01",
            "time was a rival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A9B")

    Jump("loc_4120")

    label("loc_3AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7C")

    ChrTalk(
        0x8,
        (
            "I've heard about it from\x01",
            "Brown. It seems Nonno\x01",
            "has a feel for cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At first I only intended\x01",
            "to get some simple help\x01",
            "from her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, this could be an\x01",
            "unexpected result.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BEA")

    label("loc_3B7C")


    ChrTalk(
        0x8,
        (
            "I only intended to get\x01",
            "some simple help from\x01",
            "Nonno, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm, this could be an\x01",
            "unexpected result.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BEA")

    Jump("loc_4120")

    label("loc_3BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D63")

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
        (
            "Well, maybe I should\x01",
            "look at it as a personal\x01",
            "challenge.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E1A")

    label("loc_3D63")


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
            "He hates the orthodox\x01",
            "method, but... I hope\x01",
            "he'll rethink that for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1A")

    Jump("loc_4120")

    label("loc_3E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB3")

    ChrTalk(
        0x8,
        (
            "When he started working,\x01",
            "I thought he was in for\x01",
            "a shock, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems it went better\x01",
            "than I was expecting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F25")

    label("loc_3EB3")


    ChrTalk(
        0x8,
        (
            "Somehow, Brown makes up\x01",
            "for what Certeo is\x01",
            "lacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can't continue this\x01",
            "nonsense... Hmm, what to\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F25")

    Jump("loc_4120")

    label("loc_3F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FBA")

    ChrTalk(
        0x8,
        (
            "Hmm, just leaving our\x01",
            "Certeo alone won't\x01",
            "develop him at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I've got to\x01",
            "consider drastic\x01",
            "measures.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4010")

    label("loc_3FBA")


    ChrTalk(
        0x8,
        (
            "Hmm... I've got to\x01",
            "consider drastic\x01",
            "measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope Certeo changes,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4010")

    Jump("loc_4120")

    label("loc_4015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4120")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40C4")

    ChrTalk(
        0x8,
        (
            "Hello, and welcome to\x01",
            "Vingt Sept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We change a portion of\x01",
            "our menu seasonally each\x01",
            "year.\x02",
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
    Jump("loc_4120")

    label("loc_40C4")


    ChrTalk(
        0x8,
        (
            "We change a portion of\x01",
            "our menu seasonally each\x01",
            "year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you like, please try\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4120")

    Jump("loc_2CC4")

    label("loc_4125")

    TalkEnd(0x8)
    Return()

    # Function_8_2A11 end

    def Function_9_4129(): pass

    label("Function_9_4129")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4192")

    ChrTalk(
        0xFE,
        (
            "That Certeo sure forgets\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, well good then.\x01",
            "Finally, I can relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_4192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_424F")

    ChrTalk(
        0xFE,
        (
            "I would love to have you\x01",
            "try my food...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For a chef, there is no\x01",
            "greater happiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Knowing there are customers\x01",
            "even in a situation like\x01",
            "this gives me strength.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_424F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_43BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FE")

    ChrTalk(
        0xFE,
        (
            "Rail has been shut down\x01",
            "ever since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What to do about substitutes\x01",
            "for imported ingredients? For\x01",
            "us, this is a pressing issue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_43B6")

    label("loc_42FE")


    ChrTalk(
        0xFE,
        (
            "I feel like an attack could\x01",
            "come at any moment, but...\x01",
            "Right now, I'm our only chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What to do about substitutes\x01",
            "for imported ingredients? For\x01",
            "us, this is a pressing issue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B6")

    Jump("loc_5141")

    label("loc_43BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44DA")

    ChrTalk(
        0xFE,
        (
            "I'm relieved to see that\x01",
            "Certeo finally showed\x01",
            "his true colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He gave his pasta sauce\x01",
            "a fish flavor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He did a nice job bringing\x01",
            "out the flavor with\x01",
            "several other spices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its flavor is fresh and\x01",
            "outstanding. He did very\x01",
            "well on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_457F")

    label("loc_44DA")


    ChrTalk(
        0xFE,
        (
            "Before, Certeo would always\x01",
            "combine his favorite ingredients\x01",
            "with the standard ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, his\x01",
            "vision narrowed... It\x01",
            "seems he's grown a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_457F")

    Jump("loc_5141")

    label("loc_4584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_461F")

    ChrTalk(
        0xFE,
        (
            "Hmm, for some reason\x01",
            "there's been fewer\x01",
            "customers than usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess it can't be\x01",
            "helped with these back-\x01",
            "to-back incidents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_461F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46AB")

    ChrTalk(
        0xFE,
        (
            "Even so, a cooking\x01",
            "battle, huh.\x02",
        )
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
    Jump("loc_5141")

    label("loc_46AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_47DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475C")

    ChrTalk(
        0xFE,
        (
            "That ambulance siren has\x01",
            "been bothering me for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of it, I couldn't\x01",
            "hear the sound of the fryer\x01",
            "and burned the food a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_47D7")

    label("loc_475C")


    ChrTalk(
        0xFE,
        (
            "Don't misunderstand. I'd\x01",
            "never serve burned fries\x01",
            "to a customer.\x02",
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

    label("loc_47D7")

    Jump("loc_5141")

    label("loc_47DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48A6")

    ChrTalk(
        0xFE,
        (
            "Hmm, Nonno's skills are\x01",
            "a lot better than when\x01",
            "she first started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I'll need to hire someone\x01",
            "new to manage the dining room and bring\x01",
            "her into the kitchen full time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_48A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4AC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A47")

    ChrTalk(
        0xFE,
        (
            "Hehe, Wistoff's doing\x01",
            "very well too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Certeo is using his feelings\x01",
            "towards Nonno's accomplishments to\x01",
            "further his abilities as a chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He challenged Nonno to a cooking\x01",
            "battle one week from today, betting\x01",
            "his position as a cook on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With them both so motivated\x01",
            "like this, I wonder which\x01",
            "one I want as my chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, keep that a secret\x01",
            "from Certeo, will you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4ABB")

    label("loc_4A47")


    ChrTalk(
        0xFE,
        (
            "Hehe, Wistoff's doing\x01",
            "very well too.\x02",
        )
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

    label("loc_4ABB")

    Jump("loc_5141")

    label("loc_4AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B6D")

    ChrTalk(
        0xFE,
        (
            "Haha. Though Nonno was\x01",
            "surprised by it, she has\x01",
            "plenty of motivation also.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, what a fresh feeling.\x01",
            "It reminds me of when I\x01",
            "once trained as a chef.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_4B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4BC0")

    ChrTalk(
        0xFE,
        (
            "Alright, I'll boldly try\x01",
            "leaving the cooking to\x01",
            "Nonno tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_4BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9C")

    ChrTalk(
        0xFE,
        (
            "This morning, Nonno\x01",
            "asked me about her\x01",
            "bouillon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It was better than I\x01",
            "expected. I'm surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard she cooks at home...\x01",
            "I'm going to have her help\x01",
            "me more often, I think.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D2F")

    label("loc_4C9C")


    ChrTalk(
        0xFE,
        (
            "Hmm. She's really drawn\x01",
            "out the flavor of this\x01",
            "bouillon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard she cooks at home...\x01",
            "I'm going to have her help\x01",
            "me more often, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D2F")

    Jump("loc_5141")

    label("loc_4D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDF")

    ChrTalk(
        0xFE,
        (
            "Hmm, but Wistoff did\x01",
            "something brave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't think he'd\x01",
            "leave the store, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in his case, it'd\x01",
            "be weird if he didn't.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4E3C")

    label("loc_4DDF")


    ChrTalk(
        0xFE,
        (
            "In any case, it seems he\x01",
            "can't stand that Certeo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does he understand his\x01",
            "position?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E3C")

    Jump("loc_5141")

    label("loc_4E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F61")

    ChrTalk(
        0xFE,
        (
            "In cooking, as with anything,\x01",
            "you can't do anything 'til\x01",
            "you have the basics down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, in the world of painting,\x01",
            "all the best abstract artists are\x01",
            "pretty good realists, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Certeo will come to\x01",
            "understand that sooner\x01",
            "or later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FF8")

    label("loc_4F61")


    ChrTalk(
        0xFE,
        (
            "In cooking, as with anything,\x01",
            "you can't do anything 'til\x01",
            "you have the basics down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Certeo will come to\x01",
            "understand that sooner\x01",
            "or later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF8")

    Jump("loc_5141")

    label("loc_4FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50D5")

    ChrTalk(
        0xFE,
        (
            "I asked Certeo to make my\x01",
            "new menu before, but it\x01",
            "ended up a complete failure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy just doesn't\x01",
            "get it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, it'll be a\x01",
            "while before he's a\x01",
            "proper chef.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5141")

    label("loc_50D5")


    ChrTalk(
        0xFE,
        (
            "That Certeo just doesn't\x01",
            "get it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, it'll be a\x01",
            "while before he's a\x01",
            "proper chef.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5141")

    TalkEnd(0xFE)
    Return()

    # Function_9_4129 end

    def Function_10_5145(): pass

    label("Function_10_5145")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_52DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5269")

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
            "The available ingredients will\x01",
            "be restricted going forward,\x01",
            "but I'll think of something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alllright! I gotta do my\x01",
            "best today, too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_52D5")

    label("loc_5269")


    ChrTalk(
        0xFE,
        (
            "A chef can only do one\x01",
            "thing... provide\x01",
            "delicious food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alllright! I gotta do my\x01",
            "best today, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D5")

    Jump("loc_6561")

    label("loc_52DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_54CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5427")

    ChrTalk(
        0xFE,
        (
            "If the situation was different,\x01",
            "I wouldn't have realized how\x01",
            "pathetic I am, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I understand\x01",
            "what Brown has been\x01",
            "saying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, chefs only\x01",
            "exist because of their\x01",
            "customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm embarrassed to have been\x01",
            "making nothing but these\x01",
            "complacent dishes this whole time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_54C7")

    label("loc_5427")


    ChrTalk(
        0xFE,
        (
            "That's right, chefs only\x01",
            "exist because of their\x01",
            "customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm embarrassed to have been\x01",
            "making nothing but these\x01",
            "complacent dishes this whole time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C7")

    Jump("loc_6561")

    label("loc_54CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_554B")

    ChrTalk(
        0xFE,
        (
            "President Dieter's\x01",
            "speech was really\x01",
            "impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel courage and pride\x01",
            "just listening to him\x01",
            "speak.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6561")

    label("loc_554B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5619")

    ChrTalk(
        0xFE,
        (
            "Man, the manager is one\x01",
            "tough customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think he had no intention\x01",
            "of declaring a winner from\x01",
            "the very start...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tch. I have no idea why\x01",
            "I did all that hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_56C9")

    label("loc_5619")


    ChrTalk(
        0xFE,
        (
            "Even so... Things sure\x01",
            "have gotten dangerous\x01",
            "lately.\x02",
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

    label("loc_56C9")

    Jump("loc_6561")

    label("loc_56CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5752")

    ChrTalk(
        0xFE,
        (
            "An occupation incident...\x01",
            "Terrifying, but utterly\x01",
            "preposterous.\x02",
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
    Jump("loc_6561")

    label("loc_5752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5837")

    ChrTalk(
        0xFE,
        (
            "Damn. Without a plan,\x01",
            "I'm just sitting here\x01",
            "wasting time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to hurry and\x01",
            "pull together my pasta\x01",
            "sauce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I go with tomato or\x01",
            "cream base? Or perhaps\x01",
            "something else altogether?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_58C0")

    label("loc_5837")


    ChrTalk(
        0xFE,
        (
            "Aargh, I mean are there\x01",
            "really others besides\x01",
            "those!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I feel like I'm\x01",
            "becoming more aware of my\x01",
            "weak points somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C0")

    Jump("loc_6561")

    label("loc_58C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5908")

    ChrTalk(
        0xFE,
        (
            "Hmm? It's pretty noisy\x01",
            "outside for some reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6561")

    label("loc_5908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EB")

    ChrTalk(
        0xFE,
        (
            "Anyway, though flavor is\x01",
            "important, for food,\x01",
            "appearance is critical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, this cooking battle\x01",
            "is even more\x01",
            "important...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, I'll think\x01",
            "about adding something\x01",
            "to my standard menu.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A7C")

    label("loc_59EB")


    ChrTalk(
        0xFE,
        (
            "*sigh*, but the more I\x01",
            "think about it, the more I\x01",
            "hate the word "standard".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, if it's\x01",
            "standard, it's got to be\x01",
            "delicious, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A7C")

    Jump("loc_6561")

    label("loc_5A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B37")

    ChrTalk(
        0xFE,
        (
            "...I can't believe I'm\x01",
            "going to have a cooking\x01",
            "battle with Nonno.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, a delicious pasta dish,\x01",
            "huh... I'm concerned about just\x01",
            "exactly what I should make.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6561")

    label("loc_5B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE5")

    ChrTalk(
        0xFE,
        (
            "N-Nonno's cooking? Isn't\x01",
            "this development a\x01",
            "little too fast?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be out of a job at\x01",
            "this rate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, no, no, that'll\x01",
            "never happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5C62")

    label("loc_5BE5")


    ChrTalk(
        0xFE,
        (
            "No matter how well she can\x01",
            "cook, it's too early to be\x01",
            "serving her food to customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, what about my own\x01",
            "food?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C62")

    Jump("loc_6561")

    label("loc_5C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5D16")

    ChrTalk(
        0xFE,
        (
            "I hadn't noticed at all, but\x01",
            "before I knew it, Nonno was\x01",
            "trusted with the prep as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't tell me. At this\x01",
            "rate, she's gonna become\x01",
            "a chef, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6561")

    label("loc_5D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E1A")

    ChrTalk(
        0xFE,
        (
            "Welcome. If you're here\x01",
            "to eat, feel free to sit\x01",
            "at any open table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because we're not too busy, I can\x01",
            "even show you to the reserved seating\x01",
            "on the second floor, if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a nice, cheerful\x01",
            "greeting, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5EC3")

    label("loc_5E1A")


    ChrTalk(
        0xFE,
        (
            "Man, I never expected\x01",
            "that being a waiter\x01",
            "would be this much fun.\x02",
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

    label("loc_5EC3")

    Jump("loc_6561")

    label("loc_5EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_614D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_609D")

    ChrTalk(
        0xFE,
        (
            "The manager told me to\x01",
            "be a waiter for a little\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what he's\x01",
            "planning, but this kind of work\x01",
            "is good every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can look at the female\x01",
            "customers all I want,\x01",
            "and pick them up too.\x02",
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
            "#00006F(Picking up female\x01",
            "customers... That isn't\x01",
            "good.)\x02",
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
    Jump("loc_6148")

    label("loc_609D")


    ChrTalk(
        0xFE,
        (
            "I don't know what the manager's\x01",
            "planning, but being a waiter is\x01",
            "good every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can look at the female\x01",
            "customers all I want,\x01",
            "and pick them up too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6148")

    Jump("loc_6561")

    label("loc_614D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_628F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E4")

    ChrTalk(
        0xFE,
        (
            "Cuisine is art. And\x01",
            "creativity counts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it's time for my new\x01",
            "menu, I'll create one that\x01",
            "will shock the world.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_628A")

    label("loc_61E4")


    ChrTalk(
        0xFE,
        (
            "By the way, my current\x01",
            "customers are those two girls\x01",
            "at the table near the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I've been waiting\x01",
            "for this. I'll bring out\x01",
            "their food right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_628A")

    Jump("loc_6561")

    label("loc_628F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_639D")

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
            "in place, and the gyuri\x01",
            "texture was out of this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F("Gyuri"?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(I don't really get it,\x01",
            "but I don't think I want\x01",
            "to try it...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6561")

    label("loc_639D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6504")

    ChrTalk(
        0xFE,
        (
            ""Marshland Monster Eye Abaddon\x01",
            "Stew"... I thought I was\x01",
            "breaking new culinary ground...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_642A")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_642A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6450")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6450")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6476")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6476")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_649C")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_649C")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F(T-That name is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Hehe, seems like a\x01",
            "really strange\x01",
            "combination.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6561")

    label("loc_6504")


    ChrTalk(
        0xFE,
        (
            ""Marshland Monster Eye Abaddon\x01",
            "Stew"... I thought I was\x01",
            "breaking new culinary ground...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6561")

    TalkEnd(0xFE)
    Return()

    # Function_10_5145 end

    def Function_11_6565(): pass

    label("Function_11_6565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_65F6")

    ChrTalk(
        0xFE,
        (
            "Haha, Certeo. He's in\x01",
            "good spirits today for\x01",
            "some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a tense\x01",
            "situation... but he\x01",
            "cheered me up a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_65F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_66BD")

    ChrTalk(
        0xFE,
        (
            "This strange situation in town\x01",
            "right now... The government's\x01",
            "doing it of its own accord?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they had told the public\x01",
            "about it sooner, it wouldn't\x01",
            "have been as chaotic, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_66BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_676C")

    ChrTalk(
        0xFE,
        (
            "I thought the\x01",
            "presidential address was\x01",
            "amazing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like the manager says, there are\x01",
            "a lot of points I'm concerned\x01",
            "about, so I'm not sure about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_676C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_683A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_679E")
    Call(0, 43)
    Return()

    label("loc_679E")


    ChrTalk(
        0xFE,
        (
            "It's only been a month,\x01",
            "but it's been fun\x01",
            "working in the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The manager told me I might\x01",
            "want to think seriously\x01",
            "about becoming a chef.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_683A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_689F")

    ChrTalk(
        0xFE,
        (
            "The people of Mainz...\x01",
            "I'm worried about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if they're\x01",
            "hungry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_689F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_69D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6932")

    ChrTalk(
        0xFE,
        (
            "It seems Certeo is\x01",
            "thinking hard about his\x01",
            "cooking battle recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm planning on just\x01",
            "using my usual dishes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69CE")

    label("loc_6932")


    ChrTalk(
        0xFE,
        (
            "When it comes to pasta,\x01",
            "carbonara is my specialty. I\x01",
            "often make it for my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, I was thinking\x01",
            "of making it for the\x01",
            "cooking battle too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69CE")

    Jump("loc_73C3")

    label("loc_69D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6A29")

    ChrTalk(
        0xFE,
        (
            "That siren really\x01",
            "carries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can hear it even in\x01",
            "the kitchen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_6A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6B20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB4")

    ChrTalk(
        0xFE,
        "Hm, hm-hmm♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Basil, pepper and a\x01",
            "pinch of salt...\x02",
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
    Jump("loc_6B1B")

    label("loc_6AB4")


    ChrTalk(
        0xFE,
        "Hm, hm-hmm♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next, I'll let it sit for\x01",
            "30 minutes... During that\x01",
            "time I'll chop the veggies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1B")

    Jump("loc_73C3")

    label("loc_6B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C9F")

    ChrTalk(
        0xFE,
        (
            "I should be going back\x01",
            "to the dining area\x01",
            "before long, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I asked the manager and he\x01",
            "agreed to let me work in\x01",
            "the kitchen a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, for Certeo's\x01",
            "future I decided to go along with\x01",
            "a cooking battle against him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I feel bad since Certeo seems\x01",
            "to have been tricked into it, but\x01",
            "it seemed fun so I accepted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D4C")

    label("loc_6C9F")


    ChrTalk(
        0xFE,
        (
            "Though I only cooked before as an extension\x01",
            "of my housekeeping duties, working in the\x01",
            "kitchen like this is quite fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I think I might\x01",
            "want to become a chef.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D4C")

    Jump("loc_73C3")

    label("loc_6D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6E80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E28")

    ChrTalk(
        0xFE,
        (
            "Brown suddenly decided\x01",
            "to leave this morning's\x01",
            "prep work to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I myself wonder if it\x01",
            "will really be all\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, I'll do my\x01",
            "best to live up to his\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6E7B")

    label("loc_6E28")


    ChrTalk(
        0xFE,
        (
            "Hmm, first up is\x01",
            "seasoning the\x01",
            "ingredients, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, I'm so nervous.\x02",
    )

    CloseMessageWindow()

    label("loc_6E7B")

    Jump("loc_73C3")

    label("loc_6E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6F03")

    ChrTalk(
        0xFE,
        (
            "After I'm done with this\x01",
            "prep I'll have to wash\x01",
            "the dishes next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*phew*... Our dinner\x01",
            "hour is really busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_6F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FA1")

    ChrTalk(
        0xFE,
        (
            "Hmm. These vegetables cook\x01",
            "slowly, so maybe it's\x01",
            "better to score them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*chop, chop, chop*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There, that should do\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6FE2")

    label("loc_6FA1")


    ChrTalk(
        0xFE,
        "*taptaptap*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, so this is how fine\x01",
            "chopping goes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FE2")

    Jump("loc_73C3")

    label("loc_6FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7090")

    ChrTalk(
        0xFE,
        (
            "It was decided that I'd\x01",
            "help out in the kitchen for\x01",
            "a bit instead of Certeo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's basically\x01",
            "just dishwashing and\x01",
            "some simple prep work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_7090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_71F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7183")

    ChrTalk(
        0xFE,
        (
            "Certeo is always dashing\x01",
            "out of the kitchen to\x01",
            "check on the tables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if he's planning on carrying\x01",
            "all the plates himself again today,\x01",
            "even though no one asked him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, he's a stubborn\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_71EE")

    label("loc_7183")


    ChrTalk(
        0xFE,
        (
            "Certeo is always dashing\x01",
            "out of the kitchen to\x01",
            "check on the tables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, he's a stubborn\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71EE")

    Jump("loc_73C3")

    label("loc_71F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7300")

    ChrTalk(
        0xFE,
        (
            "Flote sitting there is\x01",
            "one of our regulars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not rare for her to\x01",
            "come right when the store\x01",
            "opens and stay all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although she is considerate. She gives\x01",
            "up her seat during busy hours and puts\x01",
            "in orders throughout the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_73C3")

    label("loc_7300")


    ChrTalk(
        0xFE,
        (
            "It's not rare for Flote to\x01",
            "come right when the store\x01",
            "opens and stay all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although she is considerate. She gives\x01",
            "up her seat during busy hours and puts\x01",
            "in orders throughout the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C3")

    TalkEnd(0xFE)
    Return()

    # Function_11_6565 end

    def Function_12_73C7(): pass

    label("Function_12_73C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7485")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A pale blue tree, huh... It's\x01",
            "sometimes hard to tell fantasy\x01",
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
    Jump("loc_7510")

    label("loc_7485")


    ChrTalk(
        0xFE,
        (
            "A pale blue tree, huh... It's\x01",
            "sometimes hard to tell fantasy\x01",
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

    label("loc_7510")

    Jump("loc_873E")

    label("loc_7515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_766C")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Just when I was going to restroom,\x01",
            "mist appeared and now I can't go\x01",
            "outside? What is the meaning of this?\x02",
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
            "Even if the major powers are\x01",
            "doing it to protect the city,\x01",
            "I demand a proper explanation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_771C")

    label("loc_766C")


    ChrTalk(
        0xFE,
        (
            "We need a proper explanation for\x01",
            "the Aion weapons and the barrier\x01",
            "covering the city as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if they're\x01",
            "protecting us or putting\x01",
            "us in even more danger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_771C")

    Jump("loc_873E")

    label("loc_7721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7919")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_783D")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President Dieter of Crossbell\x01",
            "Independent State, and Secretary\x01",
            "of Defense Arios, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The names and titles are\x01",
            "fine, but I wonder if they\x01",
            "can really protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It won't be a\x01",
            "laughing matter if\x01",
            "they're just posing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7914")

    label("loc_783D")


    ChrTalk(
        0xFE,
        (
            "The independent state, the President and the\x01",
            "Secretary of Defense... The names and titles are all\x01",
            "fine, but I wonder if they can really protect us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...It won't be a\x01",
            "laughing matter if\x01",
            "they're just posing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7914")

    Jump("loc_873E")

    label("loc_7919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7B26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A35")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attack the other day\x01",
            "got the independence\x01",
            "supporters in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how they feel,\x01",
            "but I wonder if we can have\x01",
            "a more logical discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To act on emotions is to\x01",
            "be ruined... Hmm, I\x01",
            "wonder who said that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7B21")

    label("loc_7A35")


    ChrTalk(
        0xFE,
        (
            "The attack the other day\x01",
            "got the independence\x01",
            "supporters in an uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how they feel,\x01",
            "but I wonder if we can have\x01",
            "a more logical discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To act on emotions is to\x01",
            "be ruined... Hmm, I\x01",
            "wonder who said that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B21")

    Jump("loc_873E")

    label("loc_7B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7C0B")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group in\x01",
            "Mainz... Though it's just a rumor,\x01",
            "it's probably some Imperial scheme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Instead of aid, approve the\x01",
            "garrisonning of troops"... It's no joke.\x01",
            "That's what they actually demanded.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_873E")

    label("loc_7C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CFF")

    ChrTalk(
        0xFE,
        (
            "A citizens' forum is being held at\x01",
            "City Meeting Hall this morning with\x01",
            "state independence as the theme.\x02",
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
    Jump("loc_7D42")

    label("loc_7CFF")


    ChrTalk(
        0xFE,
        (
            "A citizens' forum,\x01",
            "huh... Maybe I'll make a\x01",
            "brief appearance?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D42")

    Jump("loc_873E")

    label("loc_7D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7DAD")

    ChrTalk(
        0xFE,
        (
            "It's rather noisy\x01",
            "outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have my coffee once\x01",
            "things have quieted\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_873E")

    label("loc_7DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7F1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA4")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Opening day of the Arc-en-\x01",
            "Ciel renewal performance\x01",
            "is the day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to get tickets myself, but...\x01",
            "The ones for the next two months were\x01",
            "sold out in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7F16")

    label("loc_7EA4")


    ChrTalk(
        0xFE,
        (
            "*sigh*... Well it's not\x01",
            "like I'll die if I don't\x01",
            "see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, but I want to see\x01",
            "it so bad, I could die.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F16")

    Jump("loc_873E")

    label("loc_7F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FAA")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "State independence, huh.\x01",
            "It won't be so simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I am worried about\x01",
            "our security.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8080")

    label("loc_7FAA")


    ChrTalk(
        0xFE,
        (
            "Personally, I think accepting the\x01",
            "Empire and Republic's security\x01",
            "guarantee would be a bad thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, our history being what it\x01",
            "is, it's guaranteed that it won't\x01",
            "be as simple as they're thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8080")

    Jump("loc_873E")

    label("loc_8085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_818E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_812A")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, security in the\x01",
            "city is strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all these police\x01",
            "around, I can't even\x01",
            "take a leisurely walk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8189")

    label("loc_812A")


    ChrTalk(
        0xFE,
        (
            "That's why I came here\x01",
            "to calm down.\x02",
        )
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

    label("loc_8189")

    Jump("loc_873E")

    label("loc_818E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8280")

    ChrTalk(
        0xFE,
        (
            "*sigh*, today I unconsciously read with\x01",
            "a lot of zeal and after a long time, I\x01",
            "ended up staying until sundown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you might imagine, this isn't fair\x01",
            "to the people of the store, so I\x01",
            "think I'll eat dinner here as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_873E")

    label("loc_8280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8371")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though you can't see the\x01",
            "unveiling ceremony from up close,\x01",
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
    Jump("loc_8432")

    label("loc_8371")


    ChrTalk(
        0xFE,
        (
            "Even though you can't see the\x01",
            "unveiling ceremony from up close,\x01",
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

    label("loc_8432")

    Jump("loc_873E")

    label("loc_8437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8497")

    ChrTalk(
        0xFE,
        (
            "Why is that annoying\x01",
            "cook taking my order\x01",
            "today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't understand it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_873E")

    label("loc_8497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_862A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8576")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The store has a different\x01",
            "atmosphere than usual when\x01",
            "it's raining outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sounds of the store mix\x01",
            "together with that of the rain.\x01",
            "I think this is the best BGM.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_8625")

    label("loc_8576")


    ChrTalk(
        0xFE,
        (
            "The store has a different\x01",
            "atmosphere than usual when\x01",
            "it's raining outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sounds of the store mix\x01",
            "together with that of the rain.\x01",
            "I think this is the best BGM.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8625")

    Jump("loc_873E")

    label("loc_862A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_873E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86E6")

    ChrTalk(
        0xFE,
        "*sip sip*......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, this store is\x01",
            "great for reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a moderate level of\x01",
            "noise, and coffee as well, to\x01",
            "wipe away that drowsy feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_873E")

    label("loc_86E6")


    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll finish\x01",
            "reading this book I borrowed\x01",
            "from the library today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_873E")

    TalkEnd(0xFE)
    Return()

    # Function_12_73C7 end

    def Function_13_8742(): pass

    label("Function_13_8742")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_87B6")

    ChrTalk(
        0xFE,
        (
            "Hmm, I hadn't heard that\x01",
            "it would rain today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, why'd it have to\x01",
            "rain on my vacation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880F")

    label("loc_87B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_880F")

    ChrTalk(
        0xFE,
        (
            "I know right? And the\x01",
            "prices aren't too bad. I\x01",
            "think I'll come here often.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880F")

    TalkEnd(0xFE)
    Return()

    # Function_13_8742 end

    def Function_14_8813(): pass

    label("Function_14_8813")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_88AF")

    ChrTalk(
        0xFE,
        (
            "Yeah, yeah I get it. But\x01",
            "don't come cryin' to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the rain, you just have\x01",
            "to think of a way to enjoy\x01",
            "yourself indoors, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8915")

    label("loc_88AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8915")

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
        "Haha, I like it.\x02",
    )

    CloseMessageWindow()

    label("loc_8915")

    TalkEnd(0xFE)
    Return()

    # Function_14_8813 end

    def Function_15_8919(): pass

    label("Function_15_8919")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8944")

    ChrTalk(
        0xFE,
        "Honey, you're sweet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_899A")

    label("loc_8944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_899A")

    ChrTalk(
        0xFE,
        (
            "Thank you for reserving\x01",
            "a seat for me, honey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm always grateful.\x02",
    )

    CloseMessageWindow()

    label("loc_899A")

    TalkEnd(0xFE)
    Return()

    # Function_15_8919 end

    def Function_16_899E(): pass

    label("Function_16_899E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8A07")

    ChrTalk(
        0xFE,
        "Wahaha, is that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I don't think it's\x01",
            "as good as your home\x01",
            "cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A6E")

    label("loc_8A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8A6E")

    ChrTalk(
        0xFE,
        "Wahaha, what's this now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel the same. I'm\x01",
            "grateful for all that\x01",
            "you do at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A6E")

    TalkEnd(0xFE)
    Return()

    # Function_16_899E end

    def Function_17_8A72(): pass

    label("Function_17_8A72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8B04")

    ChrTalk(
        0xFE,
        (
            "I'll open the menu,\x01",
            "suddenly point to something\x01",
            "and say, "I want that!"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, first I need to\x01",
            "close my eyes, and...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8B12")
    Jump("loc_8BC0")

    label("loc_8B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8B7D")

    ChrTalk(
        0xFE,
        (
            "Alright, I'm having fish\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh? But they're having\x01",
            "this special today,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8BC0")

    ChrTalk(
        0xFE,
        (
            "Hmm, what to do. Hmm, I\x01",
            "could have either of\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BC0")

    TalkEnd(0xFE)
    Return()

    # Function_17_8A72 end

    def Function_18_8BC4(): pass

    label("Function_18_8BC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8C0F")

    ChrTalk(
        0xFE,
        (
            "Dear... Either is fine,\x01",
            "so would you decide\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CB2")

    label("loc_8C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8C1D")
    Jump("loc_8CB2")

    label("loc_8C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8C61")

    ChrTalk(
        0xFE,
        (
            "*sigh*. You're really\x01",
            "indecisive, you know\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CB2")

    label("loc_8C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8CB2")

    ChrTalk(
        0xFE,
        (
            "Dear... Would you hurry\x01",
            "up and pick already?\x01",
            "I've already decided.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB2")

    TalkEnd(0xFE)
    Return()

    # Function_18_8BC4 end

    def Function_19_8CB6(): pass

    label("Function_19_8CB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8D17")

    ChrTalk(
        0xFE,
        (
            "Wow, this is different\x01",
            "than when I first came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, that's so uncool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DE8")

    label("loc_8D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8D25")
    Jump("loc_8DE8")

    label("loc_8D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8DA7")

    ChrTalk(
        0xFE,
        (
            "*crunch, munch*... Mmm,\x01",
            "this is happiness\x01",
            "itself♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew it. The food is\x01",
            "the best thing about\x01",
            "traveling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE8")

    label("loc_8DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8DE8")

    ChrTalk(
        0xFE,
        (
            "Haha, you've done it!♪ I\x01",
            "knew you could, darling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DE8")

    TalkEnd(0xFE)
    Return()

    # Function_19_8CB6 end

    def Function_20_8DEC(): pass

    label("Function_20_8DEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E8D")

    ChrTalk(
        0xFE,
        (
            "H-Hmm. It pains me to say\x01",
            "it, but I'm barely scraping\x01",
            "by on my travel budget...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, if possible, I'd\x01",
            "like to see their budget\x01",
            "menu...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F98")

    label("loc_8E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_8E9B")
    Jump("loc_8F98")

    label("loc_8E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8F30")

    ChrTalk(
        0xFE,
        (
            "Hmm, but there's just\x01",
            "one expensive item after\x01",
            "the next...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Well, I'm on vacation\x01",
            "after all. I shouldn't\x01",
            "sweat the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F98")

    label("loc_8F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F98")

    ChrTalk(
        0xFE,
        (
            "So, just order all the\x01",
            "food you like without\x01",
            "hesitation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm on vacation, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F98")

    TalkEnd(0xFE)
    Return()

    # Function_20_8DEC end

    def Function_21_8F9C(): pass

    label("Function_21_8F9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9001")

    ChrTalk(
        0xFE,
        (
            "Hmm, I can't believe\x01",
            "something like this happened\x01",
            "during my trip to Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_921D")

    label("loc_9001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9073")

    ChrTalk(
        0xFE,
        (
            "Hmm. For today, I think I'll\x01",
            "give up walking the highways and\x01",
            "go shopping in the city instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_921D")

    label("loc_9073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_90C4")

    ChrTalk(
        0xFE,
        (
            "Ambulances, eh? It seems\x01",
            "a lot of them are\x01",
            "passing by, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_921D")

    label("loc_90C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_915B")

    ChrTalk(
        0xFE,
        (
            "Now then, I'll tour a\x01",
            "lot of different places\x01",
            "again today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll first pay a visit\x01",
            "the orbal store to stock\x01",
            "up on photo quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_921D")

    label("loc_915B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_921D")

    ChrTalk(
        0xFE,
        (
            "When I thought about how safe\x01",
            "Crossbell has been lately, I thought\x01",
            "about coming here on vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Coming here was the right\x01",
            "choice. My girlfriend is\x01",
            "having a great time, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_921D")

    TalkEnd(0xFE)
    Return()

    # Function_21_8F9C end

    def Function_22_9221(): pass

    label("Function_22_9221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_92C1")

    ChrTalk(
        0xFE,
        (
            "I had planned to go see Mainz\x01",
            "today, but... There's no way\x01",
            "I can go in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm worried\x01",
            "about the citizens\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94B7")

    label("loc_92C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9358")

    ChrTalk(
        0xFE,
        (
            "*sigh*. Man, why'd it have\x01",
            "to rain on the day I'm\x01",
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
    Jump("loc_94B7")

    label("loc_9358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_939C")

    ChrTalk(
        0xFE,
        (
            "Those were ambulances.\x01",
            "What could have\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94B7")

    label("loc_939C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_943E")

    ChrTalk(
        0xFE,
        (
            "Yesterday I took photos of\x01",
            "Orchis Tower from various\x01",
            "places in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, before I realized\x01",
            "it, I'd used up both of\x01",
            "my photo quartz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94B7")

    label("loc_943E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_94B7")

    ChrTalk(
        0xFE,
        (
            "Haha, Crossbell is a\x01",
            "nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to see as much of\x01",
            "it as possible and make\x01",
            "some good memories.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94B7")

    TalkEnd(0xFE)
    Return()

    # Function_22_9221 end

    def Function_23_94BB(): pass

    label("Function_23_94BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9540")

    ChrTalk(
        0xFE,
        (
            "I totally agree with\x01",
            "President Dieter's\x01",
            "address!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We citizens must do all\x01",
            "we can to support\x01",
            "Crossbell too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95C2")

    label("loc_9540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_95C2")

    ChrTalk(
        0xFE,
        (
            "It seems like that\x01",
            "attack was the Empire's\x01",
            "doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't forgive them.\x01",
            "What on earth could they\x01",
            "be planning!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95C2")

    TalkEnd(0xFE)
    Return()

    # Function_23_94BB end

    def Function_24_95C6(): pass

    label("Function_24_95C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_964F")

    ChrTalk(
        0xFE,
        "Independence huh...\x02",
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
    Jump("loc_9708")

    label("loc_964F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9708")

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
            "Though we forget it from\x01",
            "time to time, Erebonia is an\x01",
            "extremely warlike nation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9708")

    TalkEnd(0xFE)
    Return()

    # Function_24_95C6 end

    def Function_25_970C(): pass

    label("Function_25_970C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9721")
    Call(0, 30)
    Jump("loc_9962")

    label("loc_9721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9931")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x103, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97BC")
    Jump("loc_9806")

    label("loc_97BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_97DC")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9806")

    label("loc_97DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97FC")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9806")

    label("loc_97FC")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9806")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#02306FGuh, that chief having me\x01",
            "watched 24 hours a day...\x01",
            "How annoying can you get?\x02\x03",
            "#02310FI'll remember this, Tio!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00203FAlright, let's go,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#02306FH-Hey, don't ignore me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F(T-That's Tio for\x01",
            "you...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    SetChrFlags(0x19, 0x10)
    SetChrSubChip(0x19, 0x0)
    Jump("loc_9962")

    label("loc_9931")

    SetChrSubChip(0x19, 0x0)

    ChrTalk(
        0x19,
        (
            "#02306FF-Fine... I'll eat them\x01",
            "myself!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9962")

    TalkEnd(0xFE)
    Return()

    # Function_25_970C end

    def Function_26_9966(): pass

    label("Function_26_9966")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_997B")
    Call(0, 30)
    Jump("loc_9BC1")

    label("loc_997B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B5B")
    OP_52(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A16")
    Jump("loc_9A60")

    label("loc_9A16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A60")

    label("loc_9A36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A60")

    label("loc_9A56")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A60")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Don't worry about me,\x01",
            "Tio!\x02",
        )
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
        "#00202FThank you, Chief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I feel like Tio's\x01",
            "relations with the chief\x01",
            "have improved...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_9BC1")

    label("loc_9B5B")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Jona! Peppers and\x01",
            "carrots are delicious\x01",
            "too, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, will you say "aaah"\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BC1")

    TalkEnd(0xFE)
    Return()

    # Function_26_9966 end

    def Function_27_9BC5(): pass

    label("Function_27_9BC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CCF")

    ChrTalk(
        0xFE,
        (
            "As city staff I guided others\x01",
            "to the shelter, so I couldn't\x01",
            "make it there myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anticipating that, my\x01",
            "wife and Mimi came to\x01",
            "get me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd prioritize their\x01",
            "own safety and stay put at home,\x01",
            "but I'm glad to have them here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_9D9B")

    label("loc_9CCF")


    ChrTalk(
        0xFE,
        (
            "I wish they'd prioritize their\x01",
            "own safety and stay put at home,\x01",
            "but I'm glad to have them here.\x02",
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

    label("loc_9D9B")

    TalkEnd(0xFE)
    Return()

    # Function_27_9BC5 end

    def Function_28_9D9F(): pass

    label("Function_28_9D9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EAC")

    ChrTalk(
        0xFE,
        (
            "My husband was late coming home\x01",
            "so I came to get him, but...\x01",
            "That mist is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those weird dolls seem to\x01",
            "recognize citizens and\x01",
            "won't attack them, but...\x02",
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
    Jump("loc_9F02")

    label("loc_9EAC")


    ChrTalk(
        0xFE,
        (
            "Haha, but kids are really\x01",
            "cute aren't they. I feel\x01",
            "happy even in this situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F02")

    TalkEnd(0xFE)
    Return()

    # Function_28_9D9F end

    def Function_29_9F06(): pass

    label("Function_29_9F06")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "You know, you know? The\x01",
            "store people treated\x01",
            "Mimi and everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was really really\x01",
            "delicious.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_9F06 end

    def Function_30_9F77(): pass

    label("Function_30_9F77")

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
            "#11PAh, it's Tio! And\x01",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0F3")
    Jump("loc_A13D")

    label("loc_A0F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A113")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A13D")

    label("loc_A113")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A133")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A13D")

    label("loc_A133")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A13D")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        "#5P#02302FHey, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FChief Roberts, and Jona.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FDid you come here to\x01",
            "eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PYeah. I want Jona here\x01",
            "to eat a balanced diet\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PIt seems he ate nothing\x01",
            "but Pizza while at Lｳman\x01",
            "State HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FYeah, I can believe\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FNow that you say that,\x01",
            "it seems he's hardly\x01",
            "touched his veggies.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x19, 500)

    ChrTalk(
        0x102,
        (
            "#12P#00105FIndeed. The peppers and\x01",
            "carrots are left...\x02\x03",
            "#00106FJona, it's not good to\x01",
            "be picky.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A3E2")
    Jump("loc_A42C")

    label("loc_A3E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A402")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A42C")

    label("loc_A402")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A422")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A42C")

    label("loc_A422")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A42C")

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
            "don't suit your palette?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PAh, this is all my fault! And\x01",
            "I only wanted to get Jona\x01",
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
            "This is why you're so\x01",
            "annoying!\x02\x03",
            "I just have to eat\x01",
            "without being picky\x01",
            "right? I'll do it!\x02\x03",
            "#02306F*glom*... Ugh, how\x01",
            "bitter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FAhaha, he's the same as\x01",
            "always.\x02",
        )
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A892")
    Jump("loc_A8DC")

    label("loc_A892")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A8B2")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8DC")

    label("loc_A8B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8D2")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8DC")

    label("loc_A8D2")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8DC")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(
        0x19,
        (
            "#5P#02305F*crunch, munch*... *gulp*.\x01",
            "There, see?\x02\x03",
            "#02301FDo you guys know where the\x01",
            "Fool connected with that\x01",
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

    def lambda_A9FF():
        TurnDirection(0x0, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A9FF)
    Sleep(50)

    def lambda_AA0F():
        TurnDirection(0x1, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_AA0F)
    Sleep(50)

    def lambda_AA1F():
        TurnDirection(0x2, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_AA1F)
    Sleep(50)

    def lambda_AA2F():
        TurnDirection(0x3, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_AA2F)
    Sleep(50)

    def lambda_AA3F():
        TurnDirection(0x4, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x4, 0, lambda_AA3F)
    Sleep(50)

    def lambda_AA4F():
        TurnDirection(0x5, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x5, 0, lambda_AA4F)
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
            "#6P#10108F(We did see him at Michelam,\x01",
            "but... We didn't tell anyone\x01",
            "about it, right?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#5P#02306FTch, so that's how it\x01",
            "is... Well all right.\x02\x03",
            "#02310FThat Fool has been showing\x01",
            "up on the orbal net ever\x01",
            "since the tower incident.\x02\x03",
            "I'll have to pay him back\x01",
            "for making a total mess\x01",
            "out of my base...\x02\x03",
            "If you guys learn anything\x01",
            "about him, I'd love to\x01",
            "hear it.\x02",
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
            "#6P#00206F...You're supporting the IBC\x01",
            "branch now. You should be more\x01",
            "respectful.\x02\x03",
            "#00200FChief, I'd like you to keep a\x01",
            "close eye on him.\x02\x03",
            "#00203FWe can't overlook overt hacking\x01",
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
            "#11PJona, I'll take responsibility\x01",
            "for you and have you watched\x01",
            "24 hours a day!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "#5P#02305FH-Hey, Tio! Isn't that a\x01",
            "little too cruel!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)

    ChrTalk(
        0x103,
        "#5P#00203FLet's go, everyone.\x02",
    )

    CloseMessageWindow()

    def lambda_AF60():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF60)
    Sleep(50)

    def lambda_AF70():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AF70)
    Sleep(50)

    def lambda_AF80():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AF80)
    Sleep(50)

    def lambda_AF90():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF90)
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
        (
            "#6P#10302F(Hehe, she tactfully\x01",
            "forced that on the\x01",
            "chief.)\x02",
        )
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

    # Function_30_9F77 end

    def Function_31_B03D(): pass

    label("Function_31_B03D")

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
        (
            "#00000FLong time no see,\x01",
            "Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12002FOh, it's you guys...\x02\x03",
            "#12004FHaha, good day to you\x01",
            "all. Fancy seeing you\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003FWe asked if anyone had seen you\x01",
            "and ended up here.\x02\x03",
            "#00001FYou were at that "Auktion",\x01",
            "weren't you. ...Rocksmith Agency\x01",
            "Section Chief Kilika Rouran.\x02",
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
            "I am Kilika Rouran, aide to the\x01",
            "President of the Republic of\x01",
            "Calvard.\x02\x03",
            "Although that is my title, I don't\x01",
            "give it out without reason, you\x01",
            "see.\x02",
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
            "#00100FSo why did you say you\x01",
            "were an entertainment\x01",
            "producer last time, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6P#12004FHaha, that is another of\x01",
            "my many titles.\x02\x03",
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
            "#10302F(Haha, a spy with many\x01",
            "faces.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00309F(Hmm, I love the\x01",
            "mysterious Kilika too, I\x01",
            "guess.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(That kind of comment\x01",
            "isn't what we need right\x01",
            "now...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FBy the way, what is a presidential\x01",
            "aide such as yourself doing in a\x01",
            "place like this?\x02\x03",
            "I heard President Rocksmith was\x01",
            "taking a tour of the IBC building\x01",
            "today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12004FThat same President had me\x01",
            "do a little errand for him.\x02\x03",
            "#12000FThough I'm shopping\x01",
            "incognito, I decided to have\x01",
            "a leisurely lunch here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAn errand... you say?\x02",
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
            "Kilika took out a pinwheel and blew on it.\x02",
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
        "#10105FA-A pinwheel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12000FCatching a glimpse of the stall\x01",
            "from our passing limousine, it\x01",
            "seemed he greatly desired one.\x02\x03",
            "Before tomorrow's main session,\x01",
            "I thought I'd purchase one to\x01",
            "help him relax.\x02\x03",
            "#12004FBut while I'm here, I thought\x01",
            "I'd get tonight's dessert as\x01",
            "well.\x02",
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
            "#12P#10302FHaha, President Rocksmith\x01",
            "really does seem like a\x01",
            "populist.\x02\x03",
            "#10304FThat is, if getting that\x01",
            "pinwheel was your real\x01",
            "objective in coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#6P#12004FHaha, well I've leave\x01",
            "the guesswork to you.\x02\x03",
            "#12000FNow then, I've finished\x01",
            "eating, so I must excuse\x01",
            "myself.\x02\x03",
            "Please, do your best\x01",
            "with trade conference\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FW-We will. Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-1800, 6500, 17260, 1000)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2610, 5000, 17800, 180)
    Sleep(1200)

    def lambda_BB25():

        label("loc_BB25")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BB25")

    QueueWorkItem2(0x101, 2, lambda_BB25)

    def lambda_BB37():

        label("loc_BB37")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BB37")

    QueueWorkItem2(0x102, 2, lambda_BB37)

    def lambda_BB49():

        label("loc_BB49")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BB49")

    QueueWorkItem2(0x104, 2, lambda_BB49)

    def lambda_BB5B():

        label("loc_BB5B")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BB5B")

    QueueWorkItem2(0x109, 2, lambda_BB5B)

    def lambda_BB6D():

        label("loc_BB6D")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_BB6D")

    QueueWorkItem2(0x105, 2, lambda_BB6D)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_BC12")
    Call(0, 32)
    Jump("loc_BC15")

    label("loc_BC12")

    Sleep(1000)

    label("loc_BC15")

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

    # Function_31_B03D end

    def Function_32_BC60(): pass

    label("Function_32_BC60")

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
            "#00003FLechter, and Kilika too...\x02\x03",
            "Both the Imperial spy and the\x01",
            "Republican one came to the\x01",
            "city with similar timing.\x02\x03",
            "#00001FWhat do you guys think?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_BD4D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BD4D)
    Sleep(50)

    def lambda_BD5D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BD5D)
    Sleep(50)

    def lambda_BD6D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BD6D)
    Sleep(50)

    def lambda_BD7D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BD7D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10103FIt's suspicious,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, if that's the\x01",
            "case, shall we follow\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FI think that would be\x01",
            "difficult.\x02\x03",
            "#00103FI got the sense that\x01",
            "both of them knew we\x01",
            "were coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FShall we report this to\x01",
            "Detective Dudley and the\x01",
            "others?\x02\x03",
            "#00000FThey might learn\x01",
            "something if they combine\x01",
            "it with their other info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FYeah... That sounds\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIt's decided then. Let's\x01",
            "head to HQ.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_32_BC60 end

    def Function_33_BF56(): pass

    label("Function_33_BF56")

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
            "Hello, and welcome to\x01",
            "Vingt Sept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you customers with a\x01",
            "reservation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Oh, so you all are the\x01",
            "ones who are doing it. I\x01",
            "heard about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, please sit at any\x01",
            "open table you would\x01",
            "like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Allow me to recommend\x01",
            "our new seasonal "Herb\x01",
            "Pasta".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, thank you. We'd\x01",
            "love to try it.\x02",
        )
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
            "Lloyd and the others sat\x01",
            "at a table and sampled\x01",
            "the herb pasta.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00200F*crunch, munch*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So how do you like our\x01",
            "pasta special?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FWow, this is really\x01",
            "delicious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIt has a full flavor but\x01",
            "no aftertaste.\x02\x03",
            "#10300FThe herbs give it a nice\x01",
            "flavor and it has a good\x01",
            "texture, too.\x02",
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
            "Haha, I'm just glad you\x01",
            "all enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FMaybe we should bring\x01",
            "KeA here next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, I'd like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, all of us here\x01",
            "will be looking forward\x01",
            "to your next visit.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_C772")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_C78F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_C7A2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_C7B5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C7B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_C7D2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_C7E5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_C802")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_C815")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_C832")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_C845")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_C862")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C862")

    OP_29(0x80, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96D")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C964")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C964")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_C96D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA5B")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_CA5B")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CA7D")
    Jump("loc_CBE5")

    label("loc_CA7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CAA2")
    SetChrPos(0xB, 7020, 0, 10470, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_CBE5")

    label("loc_CAA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CAB0")
    Jump("loc_CBE5")

    label("loc_CAB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CABE")
    Jump("loc_CBE5")

    label("loc_CABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CAFA")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_CBE5")

    label("loc_CAFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CB36")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_CBE5")

    label("loc_CB36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CB72")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_CBE5")

    label("loc_CB72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CBAE")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)
    Jump("loc_CBE5")

    label("loc_CBAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CBE5")
    SetChrPos(0xB, -52030, 0, 3650, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xA, -8880, 0, 3240, 45)
    BeginChrThread(0xA, 0, 0, 1)

    label("loc_CBE5")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -510, 0, 9440, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_BF56 end

    def Function_34_CC15(): pass

    label("Function_34_CC15")

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

    def lambda_CE37():
        OP_93(0x102, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE37)
    Sleep(50)

    def lambda_CE47():
        OP_93(0x103, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CE47)
    Sleep(50)

    def lambda_CE57():
        OP_93(0x104, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE57)
    Sleep(50)

    def lambda_CE67():
        OP_93(0x109, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CE67)
    Sleep(50)

    def lambda_CE77():
        OP_93(0x105, 0xE1, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CE77)
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
            "...Haha. You have quite\x01",
            "the keen eye, Mrs.\x01",
            "Margaret.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x20,
        "Host?",
        (
            "If he would say something\x01",
            "like that, then you are\x01",
            "wasted on your husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Ohoho... You are such a\x01",
            "flatterer, Mr. Clyde.\x02",
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
            "#00100F...She's the Vice\x01",
            "Chief's wife, if I\x01",
            "recall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FAnd the host sitting\x01",
            "across from her is\x01",
            ""Clyde", apparently.\x02\x03",
            "#10303FHmm, I don't recall\x01",
            "seeing him before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, let's sit at a\x01",
            "nearby table and try not\x01",
            "to arouse suspicion.\x02\x03",
            "#00001FWe may learn something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FAgreed.\x02",
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
            "Oh yes, I saw the\x01",
            "pamphlet from the other\x01",
            "day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "When I saw those photos,\x01",
            "I fell in love with it\x01",
            "at first sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "Haha, what an honor.\x02",
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
        (
            "Hohoho, that won't be\x01",
            "necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Actually, I've already gone to\x01",
            "see it. The scenery is good,\x01",
            "and I have no complaints.\x02",
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
            "That's a huge help.\x01",
            "Then, about those\x01",
            "reservations...\x02",
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
        (
            "#00001F(...They're quite\x01",
            "friendly with each\x01",
            "other, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(It seems like they're\x01",
            "planning a trip to\x01",
            "Michelam together, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Even so, I feel the\x01",
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
            "#00303F(The guy's excessive\x01",
            "politeness is what\x01",
            "worries me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(But, we don't have\x01",
            "anything decisive\x01",
            "yet...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe. Let's keep\x01",
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
        (
            "...Well then, if you'll\x01",
            "excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "I understand. I'll see\x01",
            "you later, at that\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "Neue-Blanc in\x01",
            "Entertainment District,\x01",
            "right? Haha, understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I'll bring what you're\x01",
            "looking for and see you\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Alright. I'll be\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x20, 1, 0, 41)
    Sleep(300)
    BeginChrThread(0x21, 1, 0, 42)
    Sleep(300)
    OP_68(-650, 1550, 7560, 3000)
    WaitChrThread(0x20, 1)
    Sleep(800)

    def lambda_D890():
        OP_95(0x20, 4230, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D890)
    Sleep(200)
    WaitChrThread(0x21, 1)

    def lambda_D8B1():
        OP_95(0x21, 4230, 0, 7840, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D8B1)
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

    def lambda_D92E():
        OP_95(0x20, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D92E)

    def lambda_D948():
        OP_95(0x21, 15500, 0, 9000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_D948)
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
        (
            "#00001F(Looks like they're\x01",
            "leaving...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Lloyd, what should we\x01",
            "do?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(We haven't gotten any\x01",
            "decisive info yet,\x01",
            "but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...Let's tail them.)\x02\x03",
            "#00000F(Randy, Wazy and I will\x01",
            "be on "Clyde".)\x02\x03",
            "(Elie, Tio and Noｱl, you\x01",
            "take Mrs. Margaret.)\x02\x03",
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
        (
            "#10302F(Hehe, this is getting\x01",
            "interesting.)\x02",
        )
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

    # Function_34_CC15 end

    def Function_35_DB43(): pass

    label("Function_35_DB43")


    def lambda_DB48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB48)

    def lambda_DB59():
        OP_95(0x101, 10110, 0, 8780, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB59)
    WaitChrThread(0x101, 1)
    Return()

    # Function_35_DB43 end

    def Function_36_DB73(): pass

    label("Function_36_DB73")


    def lambda_DB78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DB78)

    def lambda_DB89():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB89)
    WaitChrThread(0x102, 1)
    OP_95(0xFE, 10600, 0, 10450, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_36_DB73 end

    def Function_37_DBB9(): pass

    label("Function_37_DBB9")


    def lambda_DBBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DBBE)

    def lambda_DBCF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DBCF)
    WaitChrThread(0x103, 1)
    OP_95(0xFE, 11310, 0, 7580, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_DBB9 end

    def Function_38_DBFF(): pass

    label("Function_38_DBFF")


    def lambda_DC04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DC04)

    def lambda_DC15():
        OP_95(0xFE, 11630, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC15)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_38_DBFF end

    def Function_39_DC36(): pass

    label("Function_39_DC36")


    def lambda_DC3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DC3B)

    def lambda_DC4C():
        OP_95(0xFE, 12860, 0, 9250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DC4C)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_DC36 end

    def Function_40_DC6D(): pass

    label("Function_40_DC6D")


    def lambda_DC72():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DC72)

    def lambda_DC83():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DC83)
    WaitChrThread(0x105, 1)
    OP_95(0xFE, 12200, 0, 10670, 1500, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_DC6D end

    def Function_41_DCB3(): pass

    label("Function_41_DCB3")

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

    # Function_41_DCB3 end

    def Function_42_DCF7(): pass

    label("Function_42_DCF7")

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

    # Function_42_DCF7 end

    def Function_43_DD3B(): pass

    label("Function_43_DD3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF03")

    ChrTalk(
        0xB,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please sit wherever you'd\x01",
            "like. I'll be there to\x01",
            "take your order shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Maybe I can invite her\x01",
            "to the pageant as our\x01",
            "waitress.)\x02\x03",
            "#00000FUmm, excuse me. I'd like\x01",
            "to ask you something...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Asked Nonno to\x01",
            "participate in the\x01",
            "charity event pageant.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        (
            "W-What? I can\x01",
            "participate in a\x01",
            "pageant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmm. I'm sorry, but...\x01",
            "I'm not interested.\x02",
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
    Jump("loc_DF89")

    label("loc_DF03")


    ChrTalk(
        0xB,
        (
            "I'm not especially\x01",
            "interested in participating\x01",
            "in a beauty pageant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm okay if you just\x01",
            "need help from a\x01",
            "waitress, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF89")

    TalkEnd(0xB)
    Return()

    # Function_43_DD3B end

    SaveToFile()

Try(main)
