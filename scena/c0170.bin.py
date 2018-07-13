from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0170.bin",                # FileName
        "c0170",                    # MapName
        "c0170",                    # Location
        0x0005,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0170",                  # 0
        "Receptionist Pearl",     # 1
        "Receptionist Cynthia",   # 2
        "Hanson",                 # 3
        "Region",                 # 4
        "Prada",                  # 5
        "Baker",                  # 6
        "Southwark",              # 7
        "Lenalee",                # 8
        "Pluna",                  # 9
        "Manager Neston",         # 10
        "Jeanetta",               # 11
        "Baggio",                 # 12
        "Dorothee",               # 13
        "Ken",                    # 14
        "Old Man Honest",         # 15
        "Yuri",                   # 16
        "Sykes",                  # 17
        "Reggie",                 # 18
        "Pliｳ",                  # 19
        "Grace",                  # 20
        "Reins",                  # 21
        "Citizen",                # 22
        "Tourist",                # 23
        "Tourist",                # 24
        "Detective Raymond",      # 25
        "Detective Dudley",       # 26
        "Fernando",               # 27
        "Joanna",                 # 28
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch21600.itc",                   # 08
        "chr/ch34600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch20500.itc",                   # 0C
        "chr/ch44102.itc",                   # 0D
        "chr/ch47500.itc",                   # 0E
        "chr/ch23600.itc",                   # 0F
        "chr/ch29000.itc",                   # 10
        "chr/ch20400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch32302.itc",                   # 13
        "chr/ch44202.itc",                   # 14
        "chr/ch06000.itc",                   # 15
        "chr/ch28100.itc",                   # 16
        "chr/ch30200.itc",                   # 17
        "chr/ch00900.itc",                   # 18
        "chr/ch27800.itc",                   # 19
        "chr/ch25700.itc",                   # 1A
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294955767, 8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294951307, 0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294958177, 0,       2869,    90,   405,  0x0, 0,   11,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(4294959777, 0,       2869,    270,  405,  0x0, 0,   12,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(4294964636, 0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294960637, 8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   17,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   28,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(4294952847, 8000,    14420,   90,   257,  0x0, 0,   8,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(6659,    8199,    6300,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(5050,    8000,    5130,    90,   389,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(7250,    8000,    4730,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   389,  0x0, 0,   16,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(4294951456, 0,       15979,   0,    389,  0x0, 0,   21,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(4294952467, 0,       14739,   315,  389,  0x0, 0,   22,  0,   0,   0,   0,   48,  255,  0)
    DeclNpc(4294952647, 0,       10310,   0,    389,  0x0, 0,   18,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(4294953826, 8199,    21430,   270,  389,  0x0, 0,   19,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(4294953826, 8199,    20629,   270,  389,  0x0, 0,   20,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(4294961697, 8000,    5699,    0,    389,  0x0, 0,   23,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(899,     8029,    27729,   315,  389,  0x0, 0,   24,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(4294953826, 0,       6510,    315,  389,  0x0, 0,   25,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(8750,    0,       1879,    90,   385,  0x0, 0,   26,  0,   0,   0,   0,   43,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  5,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  7,  0x0000)
    DeclActor(4294966816, 8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  11, 0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  13, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  15, 0x0000)
    DeclActor(4294954906, 8000,    7660,    1000,    4294955766, 9500,    8510,    0x007E, 0,  17, 0x0000)
    DeclActor(4294951266, 0,       23800,   1000,    4294951306, 1500,    25740,   0x007E, 0,  19, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  49, 0x0000)
    DeclActor(12000,   0,       15200,   1200,    12000,   1500,    15200,   0x007C, 0,  4,  0x0000)
    DeclActor(4294952316, 0,       11460,   1200,    4294952316, 1500,    11460,   0x007C, 0,  50, 0x0000)

    ChipFrameInfo(1616, 0)                                       # 0

    ScpFunction((
        "Function_0_650",          # 00, 0
        "Function_1_700",          # 01, 1
        "Function_2_7D9",          # 02, 2
        "Function_3_B98",          # 03, 3
        "Function_4_C9C",          # 04, 4
        "Function_5_DCF",          # 05, 5
        "Function_6_DD3",          # 06, 6
        "Function_7_1CAC",         # 07, 7
        "Function_8_1CB0",         # 08, 8
        "Function_9_26D4",         # 09, 9
        "Function_10_28F1",        # 0A, 10
        "Function_11_2A8B",        # 0B, 11
        "Function_12_2AAA",        # 0C, 12
        "Function_13_3D20",        # 0D, 13
        "Function_14_3D27",        # 0E, 14
        "Function_15_521E",        # 0F, 15
        "Function_16_5222",        # 10, 16
        "Function_17_62BC",        # 11, 17
        "Function_18_62C0",        # 12, 18
        "Function_19_7287",        # 13, 19
        "Function_20_728E",        # 14, 20
        "Function_21_8DE7",        # 15, 21
        "Function_22_8F62",        # 16, 22
        "Function_23_A5A9",        # 17, 23
        "Function_24_AA0A",        # 18, 24
        "Function_25_AE67",        # 19, 25
        "Function_26_B107",        # 1A, 26
        "Function_27_B512",        # 1B, 27
        "Function_28_BE76",        # 1C, 28
        "Function_29_C7CB",        # 1D, 29
        "Function_30_D2C6",        # 1E, 30
        "Function_31_DD7D",        # 1F, 31
        "Function_32_DFAE",        # 20, 32
        "Function_33_E14A",        # 21, 33
        "Function_34_E1E8",        # 22, 34
        "Function_35_E29A",        # 23, 35
        "Function_36_E337",        # 24, 36
        "Function_37_E53D",        # 25, 37
        "Function_38_E62C",        # 26, 38
        "Function_39_F195",        # 27, 39
        "Function_40_F2F8",        # 28, 40
        "Function_41_F4B9",        # 29, 41
        "Function_42_F635",        # 2A, 42
        "Function_43_F79C",        # 2B, 43
        "Function_44_F80D",        # 2C, 44
        "Function_45_FF29",        # 2D, 45
        "Function_46_FF9F",        # 2E, 46
        "Function_47_107A0",       # 2F, 47
        "Function_48_108A3",       # 30, 48
        "Function_49_10AB9",       # 31, 49
        "Function_50_10BAB",       # 32, 50
        "Function_51_114AD",       # 33, 51
        "Function_52_11682",       # 34, 52
        "Function_53_11DDB",       # 35, 53
    ))


    def Function_0_650(): pass

    label("Function_0_650")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_688"),
        (1, "loc_694"),
        (2, "loc_6A0"),
        (3, "loc_6AC"),
        (4, "loc_6B8"),
        (5, "loc_6C4"),
        (6, "loc_6D0"),
        (SWITCH_DEFAULT, "loc_6DC"),
    )


    label("loc_688")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_694")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6FF")

    Return()

    # Function_0_650 end

    def Function_1_700(): pass

    label("Function_1_700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D8")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_700")

    label("loc_7D8")

    Return()

    # Function_1_700 end

    def Function_2_7D9(): pass

    label("Function_2_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_813")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x11, -13470, 0, 6510, 135)
    SetChrPos(0x22, -12670, 0, 5710, 315)
    Jump("loc_B83")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_88F")
    SetChrPos(0x12, -17370, 30, 22740, 45)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -1360, 0, 9830, 270)
    OP_93(0x11, 0x5A, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 8060, 8000, 2080, 90)
    SetChrPos(0xF, 9560, 8000, 2080, 270)
    Jump("loc_B83")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E5")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    SetChrPos(0x15, 8020, 8000, 17270, 90)
    SetChrPos(0x14, 9070, 8000, 17290, 270)
    BeginChrThread(0x14, 0, 0, 0)
    Jump("loc_B83")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_913")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_B83")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_93C")
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_B83")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_974")
    SetChrPos(0x16, -13640, 8029, 7380, 45)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_B83")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_987")
    ClearChrFlags(0x23, 0x80)
    Jump("loc_B83")

    label("loc_987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_99A")
    ClearChrFlags(0x21, 0x80)
    Jump("loc_B83")

    label("loc_99A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9AD")
    SetChrFlags(0x12, 0x80)
    Jump("loc_B83")

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A0F")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D4")
    SetChrFlags(0x1C, 0x10)

    label("loc_9D4")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1E, 0x13)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x14)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_B83")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_A4F")
    SetChrPos(0x15, 8020, 8000, 17270, 90)
    SetChrPos(0x14, 9070, 8000, 17290, 270)
    BeginChrThread(0x14, 0, 0, 0)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x13, 0x80)
    Jump("loc_B83")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A93")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1E, 0x13)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x14)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_B83")

    label("loc_A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B10")
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0xD)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD0")
    SetChrFlags(0x17, 0x10)

    label("loc_AD0")

    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1E, 0x13)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrChipByIndex(0x1F, 0x14)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_B83")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B70")
    SetChrPos(0x12, -17370, 30, 22740, 45)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6B")
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -15840, 0, 15980, 0)
    SetChrFlags(0x1C, 0x10)

    label("loc_B6B")

    Jump("loc_B83")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B83")
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x1D, 0x80)

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B97")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_B97")

    Return()

    # Function_2_7D9 end

    def Function_3_B98(): pass

    label("Function_3_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BA5")
    OP_65(0x1, 0x1)

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    OP_65(0x0, 0x1)

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C00")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C60")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_C6E")

    label("loc_C60")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_C6E")

    OP_65(0x9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9B")
    OP_1B(0x0, 0x0, 0x35)
    OP_66(0x9, 0x1)

    label("loc_C9B")

    Return()

    # Function_3_B98 end

    def Function_4_C9C(): pass

    label("Function_4_C9C")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　★　Region Food Memo　★\x01",
            "Customers, allow us to recommend\x01",
            "Bell Berry Juice to soothe your throats.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Bell Berry Juice recipe is written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_DCB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Bell Berry Juice"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DCB")

    TalkEnd(0xFF)
    Return()

    # Function_4_C9C end

    def Function_5_DCF(): pass

    label("Function_5_DCF")

    Call(0, 6)
    Return()

    # Function_5_DCF end

    def Function_6_DD3(): pass

    label("Function_6_DD3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E73")

    ChrTalk(
        0x8,
        (
            "Scott came in here a\x01",
            "little while ago, and\x01",
            "he seems fine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's working so hard\x01",
            "for us... It makes me\x01",
            "want to do my best too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8E")
    Call(0, 23)
    Jump("loc_FD3")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F82")

    ChrTalk(
        0x8,
        (
            "Thankfully we still have\x01",
            "groceries and daily necessities\x01",
            "in stock at present, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The longer this goes on, the\x01",
            "more I worry about families\x01",
            "without reserve supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Really... What is our\x01",
            "government thinking?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD3")

    label("loc_F82")


    ChrTalk(
        0x8,
        (
            "Really... What is our\x01",
            "government thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope Scott is\x01",
            "safe too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD3")

    Jump("loc_1CA8")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EC")

    ChrTalk(
        0x8,
        (
            "The following day of the referendum, senior \x01",
            "Cynthia returned to her home in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although I don't think\x01",
            "senior was anticipating\x01",
            "this situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For a long time, her family\x01",
            "has been worried about her.\x01",
            "I'm glad she left early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11CB")

    label("loc_10EC")


    ChrTalk(
        0x8,
        (
            "Senior Cynthia promised\x01",
            "to return to this\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm worried about a lot of things, but... Anyway,\x01",
            "I believe the day will come when I can do this with\x01",
            "senior again, and I'll do my very best until then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CB")

    Jump("loc_1CA8")

    label("loc_11D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_130C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(
        0x8,
        (
            "Senior Cynthia is participating\x01",
            "in the charity event in the\x01",
            "Governmental District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, I hear she's participating\x01",
            "in the pageant. I'll have her\x01",
            "show me the photos later♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1307")

    label("loc_12A1")


    ChrTalk(
        0x8,
        (
            "I heard senior Cynthia's participating\x01",
            "in the pageant. I'll have her\x01",
            "show me the photos later.♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1307")

    Jump("loc_1CA8")

    label("loc_130C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_13AB")

    ChrTalk(
        0x8,
        "To think the mining town's occupied...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know who would do\x01",
            "something like that or why, but...\x01",
            "There's no way I can forgive them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_13AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1468")

    ChrTalk(
        0x8,
        (
            "Scott is busy working again\x01",
            "and he told me it will be extremely\x01",
            "unlikely to be able to contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's shockingly\x01",
            "calm. He isn't a\x01",
            "Bracer for nothing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14DD")

    label("loc_1468")


    ChrTalk(
        0x8,
        (
            "I guess there's no need to\x01",
            "worry about him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want him to be\x01",
            "careful not to get\x01",
            "too hurt out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DD")

    Jump("loc_1CA8")

    label("loc_14E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1543")

    ChrTalk(
        0x8,
        (
            "They said it was a train derailment...\x01",
            "Is that train trouble or something...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_1543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0x8,
        (
            "It seems like Scott\x01",
            "has been even busier\x01",
            "than usual lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Good luck, Scott. I'm\x01",
            "always supporting you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DF")
    Call(0, 10)
    Jump("loc_1672")

    label("loc_15DF")


    ChrTalk(
        0x8,
        (
            "Ah, you're the Special\x01",
            "Support Section that is\x01",
            "always coming here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you for coming today. \x01",
            "Please, take your time looking around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1672")

    Jump("loc_1CA8")

    label("loc_1677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1774")

    ChrTalk(
        0x8,
        (
            "Jeanetta invited three\x01",
            "guys to last night's\x01",
            "dinner party, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "While we were talking, all\x01",
            "three of them were totally\x01",
            "focused on senior Cynthia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jeanetta is feeling down today.\x01",
            "I wonder if she'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17BA")

    label("loc_1774")


    ChrTalk(
        0x8,
        (
            "Jeanetta is feeling down today.\x01",
            "I wonder if she'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BA")

    Jump("loc_1CA8")

    label("loc_17BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_18E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1886")

    ChrTalk(
        0x8,
        (
            "Today, after we finish work,\x01",
            "I'm going to eat with senior\x01",
            "Cynthia and Jeanetta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party in a long time... \x01",
            "Uh uh, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18DD")

    label("loc_1886")


    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party in a long time... \x01",
            "Uh uh, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DD")

    Jump("loc_1CA8")

    label("loc_18E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1999")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FD")
    Call(0, 9)
    Jump("loc_1994")

    label("loc_18FD")


    ChrTalk(
        0x8,
        (
            "I always knew she was a fan,\x01",
            "but I didn't know senior Cynthia\x01",
            "loved Miss Julia that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I want to know more\x01",
            "about that side of her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1994")

    Jump("loc_1CA8")

    label("loc_1999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9E")

    ChrTalk(
        0x8,
        (
            "I wonder what Mr. Scott\x01",
            "is doing around now.\x01",
            "With that job of his...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Ah, sorry! I said something\x01",
            "at work I shouldn't have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need any help,\x01",
            "please say so. I will do my\x01",
            "very best to assist you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AEE")

    label("loc_1A9E")


    ChrTalk(
        0x8,
        (
            "If you need any help,\x01",
            "please say so. I will do my\x01",
            "very best to assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEE")

    Jump("loc_1CA8")

    label("loc_1AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B72")

    ChrTalk(
        0x8,
        (
            "Welcome. We are open on\x01",
            "rainy days too, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please enjoy your shopping\x01",
            "today as well. (*smile*)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA8")

    label("loc_1B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C37")

    ChrTalk(
        0x8,
        (
            "Thank you for shopping at\x01",
            ""Times" department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "This is the information desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is anything you are not sure\x01",
            "about, please feel free to ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CA8")

    label("loc_1C37")


    ChrTalk(
        0x8,
        "This is the information desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is anything you are not sure\x01",
            "about, please feel free to ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CA8")

    TalkEnd(0x8)
    Return()

    # Function_6_DD3 end

    def Function_7_1CAC(): pass

    label("Function_7_1CAC")

    Call(0, 8)
    Return()

    # Function_7_1CAC end

    def Function_8_1CB0(): pass

    label("Function_8_1CB0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1CC1")
    Jump("loc_26D0")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1CCF")
    Jump("loc_26D0")

    label("loc_1CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D7F")

    ChrTalk(
        0x9,
        (
            "I've heard different things about\x01",
            "the identity of that armed group, \x01",
            "but I wonder what it really is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway... I pray that the\x01",
            "citizens are not hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E0A")

    ChrTalk(
        0x9,
        (
            "Miss Pearl and Mr. Scott have\x01",
            "been friends ever since forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's cute that her fiancｳe\x01",
            "is her childhood friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_1E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E97")

    ChrTalk(
        0x9,
        (
            "The manager said a\x01",
            "train derailed near\x01",
            "West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope everyone's injuries\x01",
            "aren't too serious, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2065")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDE")

    ChrTalk(
        0x9,
        (
            "I feel like the heat in arguments\x01",
            "over independence is building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On top of that, my family in\x01",
            "Remiferia told me to come home\x01",
            "before any problems occur, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Crossbell is my second\x01",
            "hometown, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For now, I'm planning on seeing the\x01",
            "referendum results. Then I'll return home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2060")

    label("loc_1FDE")


    ChrTalk(
        0x9,
        (
            "No matter what anyone\x01",
            "says, Crossbell is my\x01",
            "second hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll return home only after\x01",
            "seeing the referendum results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2060")

    Jump("loc_26D0")

    label("loc_2065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_211C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2080")
    Call(0, 10)
    Jump("loc_2117")

    label("loc_2080")


    ChrTalk(
        0x9,
        (
            "My... I'm terribly sorry.\x01",
            "It seems I got lost in conversation\x01",
            "during working hours...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I would be pleased to help\x01",
            "you with anything you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2117")

    Jump("loc_26D0")

    label("loc_211C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_221D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C2")

    ChrTalk(
        0x9,
        (
            "I can't believe\x01",
            "Miss Jeanetta\x01",
            "invited men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I understand that they\x01",
            "were all wealthy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "*sigh*, it's all just so tiring.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2218")

    label("loc_21C2")


    ChrTalk(
        0x9,
        (
            "I can't believe\x01",
            "Miss Jeanetta\x01",
            "invited men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "*sigh*, it's all just so tiring.\x02",
    )

    CloseMessageWindow()

    label("loc_2218")

    Jump("loc_26D0")

    label("loc_221D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_235F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F3")

    ChrTalk(
        0x9,
        (
            "Today Miss Jeanetta is \x01",
            "really in high spirits. Could\x01",
            "something have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not that going to dinner us\x01",
            "three together is the first time...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_235A")

    label("loc_22F3")


    ChrTalk(
        0x9,
        (
            "It's not that going to dinner us\x01",
            "three together is the first time...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235A")

    Jump("loc_26D0")

    label("loc_235F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_237A")
    Call(0, 9)
    Jump("loc_23F8")

    label("loc_237A")


    ChrTalk(
        0x9,
        (
            "Oh, sir... \x01",
            "Please excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Welcome to "Times" department\x01",
            "store. Please let me know if\x01",
            "there's anything you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F8")

    Jump("loc_26D0")

    label("loc_23FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24A4")

    ChrTalk(
        0x9,
        (
            "Tomorrow, VIPs from several\x01",
            "countries will be coming\x01",
            "for the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although they won't\x01",
            "be visiting our store,\x01",
            "I'm nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_24A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_253C")

    ChrTalk(
        0x9,
        (
            "Miss Pearl is in high spirits because\x01",
            "her fiancｳe, Mr. Scott, visits her\x01",
            "every so often right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uh uh, I think I'm jealous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26D0")

    label("loc_253C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2634")

    ChrTalk(
        0x9,
        (
            "Did you see the new rooftop\x01",
            "space we opened a few days ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are no special facilities\x01",
            "there, but you can get a full\x01",
            "view of the Crossbell cityscape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If you would like to, please feel free to stop by.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26D0")

    label("loc_2634")


    ChrTalk(
        0x9,
        (
            "The customers are already\x01",
            "thrilled with the rooftop space\x01",
            "we opened a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone, why not try stopping\x01",
            "by when it's time for a break?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D0")

    TalkEnd(0x9)
    Return()

    # Function_8_1CB0 end

    def Function_9_26D4(): pass

    label("Function_9_26D4")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        "Miss Pearl, did you hear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that Miss\x01",
            "Julia is coming\x01",
            "here from Liberl...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I already checked that out,\x01",
            "of course. I've already asked\x01",
            "a friend to take a picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, well, I don't know whether or not \x01",
            "she'll be able to take a good picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Miss Pearl, get one\x01",
            "picture for me too!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "O-Okay. I don't\x01",
            "mind, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Captain Julia, huh...\x01",
            "She's really popular.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F(Yes. It is Captain\x01",
            "Julia, after all.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_9_26D4 end

    def Function_10_28F1(): pass

    label("Function_10_28F1")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "Then, the place Mr. \x01",
            "Southwark confessed is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, it seems like it was\x01",
            ""Fortuna", the high-class\x01",
            "restaurant at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, he asked the staff\x01",
            "to put on a show for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Mr. Southwark is a director too, is he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, but I'm really glad\x01",
            "Jeanetta will come to be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uh uh, I've got to follow her example.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_10_28F1 end

    def Function_11_2A8B(): pass

    label("Function_11_2A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AA6")
    Call(0, 46)
    Jump("loc_2AA9")

    label("loc_2AA6")

    Call(0, 12)

    label("loc_2AA9")

    Return()

    # Function_11_2A8B end

    def Function_12_2AAA(): pass

    label("Function_12_2AAA")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B07")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B26")
    OP_AF(0x26)
    Jump("loc_2B48")

    label("loc_2B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B36")
    OP_AF(0x25)
    Jump("loc_2B48")

    label("loc_2B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B46")
    OP_AF(0x24)
    Jump("loc_2B48")

    label("loc_2B46")

    OP_AF(0x23)

    label("loc_2B48")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D17")

    label("loc_2B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B6B")
    Jump("loc_3D17")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D17")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C5C")

    ChrTalk(
        0xA,
        (
            "Even if it's hard for us to\x01",
            "sell imported goods, we have\x01",
            "a custom ordering service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From here on, we'll hire even more\x01",
            "workers, and endeavor to provide\x01",
            "everyone will a full range of services.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_2C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D3B")

    ChrTalk(
        0xA,
        (
            "I wonder just how long this martial\x01",
            "law order is going to last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even regarding groceries,\x01",
            "families will have stock\x01",
            "just for a few days...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm truly scared of the unseen\x01",
            "problems that lie ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_2D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5B")

    ChrTalk(
        0xA,
        (
            "I wonder if the State Guard\x01",
            "can really hold Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although I want to\x01",
            "believe in Mr. Arios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the two major powers invade simultaneously,\x01",
            "we'll have no choice but to capitulate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or possibly... Might there be\x01",
            "some sort of secret plan?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EF4")

    label("loc_2E5B")


    ChrTalk(
        0xA,
        (
            "If the two major powers invade simultaneously,\x01",
            "we'll have no choice but to capitulate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or possibly... Might there be\x01",
            "some sort of secret plan?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF4")

    Jump("loc_3D17")

    label("loc_2EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FAB")

    ChrTalk(
        0xA,
        (
            "It seems the city's reconstruction\x01",
            "is finally coming along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't do anything special, but...\x01",
            "I'm planning to offer reduced\x01",
            "prices on some of my goods.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_2FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_301C")

    ChrTalk(
        0xA,
        (
            "The faces of my regular\x01",
            "customers in Mainz come to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope they're\x01",
            "all safe, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_301C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_323A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3162")

    ChrTalk(
        0xA,
        (
            "Yesterday, when I heard train service had\x01",
            "stopped, I wondered what happened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thanks to the efforts of the police\x01",
            "and the station staff, it seems it's\x01",
            "been completely restored today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thanks to that, this mornings'\x01",
            "delivery arrived safely...\x01",
            "I haven't enough words of gratitude.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3235")

    label("loc_3162")


    ChrTalk(
        0xA,
        (
            "The railroad's been completely\x01",
            "repaired. It's as if yesterday's\x01",
            "accident never happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I haven't enough words of gratitude\x01",
            "to thank the efforts of the police and\x01",
            "station staff that restored service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3235")

    Jump("loc_3D17")

    label("loc_323A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_327F")

    ChrTalk(
        0xA,
        "Hmm, it seems some sort of accident has occurred.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_327F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_END)), "loc_3334")

    ChrTalk(
        0xA,
        (
            "Mr. Dudley is a regular customer at our store and\x01",
            "has us make shoes for him several times a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "His passion and pickiness\x01",
            "are hallmarks of a true fan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3334")

    Jump("loc_3D17")

    label("loc_3339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_342B")

    ChrTalk(
        0xA,
        (
            "It is only once in a lifetime that two\x01",
            "people meet for the first time. I believe\x01",
            "people and shoes are like this, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It may seem a bit strange, but\x01",
            "seeing all the shoes lined up like\x01",
            "this makes me want to greet them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_342B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0xA,
        "Truly good things are not influenced by trends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I want to offer goods that everyone\x01",
            "will love across the generations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_34B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3637")

    ChrTalk(
        0xA,
        (
            "Everyone, do you know that it would be best\x01",
            "to go choose shoes on or after evening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is because, after we wake up in the morning,\x01",
            "human feet swell little by little, and when evening\x01",
            "arrives, they could even be about 1 rege bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is regarded best to choose your size\x01",
            "on or after evening, when feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3743")

    label("loc_3637")


    ChrTalk(
        0xA,
        (
            "The truth is that, after we wake up in the morning,\x01",
            "human feet swell little by little, and when evening\x01",
            "arrives, they could even be about 1 rege bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is regarded best to choose your size\x01",
            "on or after evening, when feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3743")

    Jump("loc_3D17")

    label("loc_3748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37FA")

    ChrTalk(
        0xA,
        (
            "The more you put a pair of shoes on, the more\x01",
            "comfortable and familiar they will feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They're complicated like people,\x01",
            "and they come with a deep flavor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D17")

    label("loc_37FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3890")

    ChrTalk(
        0xA,
        (
            "We have a full complement of\x01",
            "goods for children as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, take you\x01",
            "time perusing them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A82")

    label("loc_3890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CD")

    ChrTalk(
        0xA,
        (
            "Miss Prada has been poking fun at me trying to\x01",
            "make me deal in clothes too like I did before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The world of shoes is extremely complicated.\x01",
            "You realize it when you try\x01",
            "to seriously dive into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is exactly why I want to put my heart\x01",
            "and soul on it and only focus on shoes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A82")

    label("loc_39CD")


    ChrTalk(
        0xA,
        (
            "The world of clothes is very\x01",
            "complicated, of course, and \x01",
            "the world of shoes it is too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is exactly why I want to put my heart\x01",
            "and soul on it and only focus on shoes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A82")

    Jump("loc_3D17")

    label("loc_3A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2E")

    ChrTalk(
        0xA,
        (
            "At this store, we sell\x01",
            "rain shoes as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There are customers who buy and change into\x01",
            "them immediately in sudden rain like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BA6")

    label("loc_3B2E")


    ChrTalk(
        0xA,
        (
            "At this store, we sell\x01",
            "rain shoes as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you would like, I would be happy\x01",
            "to recommend something to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA6")

    Jump("loc_3D17")

    label("loc_3BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7E")

    ChrTalk(
        0xA,
        "Welcome to "Hanson's Shoes".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you are having trouble finding anything, \x01",
            "please do not hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I would be delighted to find\x01",
            "the perfect pair of shoes for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D17")

    label("loc_3C7E")


    ChrTalk(
        0xA,
        (
            "We sell the full range of\x01",
            "shoes from casual to formal,\x01",
            "and we even sell hiking shoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I am sure I will find the\x01",
            "perfect pair of shoes for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D17")

    Jump("loc_2AB7")

    label("loc_3D1C")

    TalkEnd(0xA)
    Return()

    # Function_12_2AAA end

    def Function_13_3D20(): pass

    label("Function_13_3D20")

    SetScenarioFlags(0x2, 3)
    Call(0, 14)
    Return()

    # Function_13_3D20 end

    def Function_14_3D27(): pass

    label("Function_14_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D94")
    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "You don't look like\x01",
            "the delivery man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you're buying, please\x01",
            "head to the front.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    label("loc_3D94")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3E")

    ChrTalk(
        0x1A2,
        (
            "I see. So you deal with a lot\x01",
            "of imported ingredients here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hmm, you even have soy sauce.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Uh uh, might you be from\x01",
            "the East, young man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We offer a great number of authentic\x01",
            "ingredients here. Even someone from\x01",
            "the East would be satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you have a special\x01",
            "request then please,\x01",
            "just let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "S-Sure... I'll think about it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TalkEnd(0xB)
    Jump("loc_3FBF")

    label("loc_3F3E")

    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "If you have a special\x01",
            "request, we can special\x01",
            "order it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please let me know if there's anything you need.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)

    label("loc_3FBF")

    Return()

    label("loc_3FC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_401A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403A")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5215")

    label("loc_403A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_404E")
    Jump("loc_5215")

    label("loc_404E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5215")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4111")

    ChrTalk(
        0xB,
        (
            "I was able to get in contact with my\x01",
            "daugher and confirm her safety just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She brought out her cart right away,\x01",
            "so I've got to do my best too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_4111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_41D7")

    ChrTalk(
        0xB,
        (
            "Even so... \x01",
            "I wonder if my daughter was able\x01",
            "to take refuge at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We haven't been able to use orbal\x01",
            "communication ever since martial law\x01",
            "was declared... I'm very worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_41D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E4")

    ChrTalk(
        0xB,
        (
            "It seems train passage through\x01",
            "Crossbell has been restricted\x01",
            "ever since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I heard that at the end of today the\x01",
            "trains will stop service, same as the buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Given the situation, war comes\x01",
            "to mind, rather than sales.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_437B")

    label("loc_42E4")


    ChrTalk(
        0xB,
        (
            "I heard that at the end of today the\x01",
            "trains will stop service, same as the buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Given the situation, war comes\x01",
            "to mind, rather than sales.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_437B")

    Jump("loc_5215")

    label("loc_4380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_44F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444D")

    ChrTalk(
        0xB,
        (
            "No matter the situation, us merchants\x01",
            "mustn't lose heart. Anyway, I'll do\x01",
            "my best to focus on work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Welcome. For your worn-out bodies,\x01",
            "how about some Ord State garlic?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44EC")

    label("loc_444D")


    ChrTalk(
        0xB,
        (
            "Welcome. For your worn-out bodies,\x01",
            "how about some Ord State garlic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ord garlic is larger and rich in nutrients.\x01",
            "It's most suitable for revitalizing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44EC")

    Jump("loc_5215")

    label("loc_44F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_456F")

    ChrTalk(
        0xB,
        (
            "I wonder how the people of\x01",
            "Mainz are doing right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I hope the situation is resolved soon, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_456F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_471C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467D")

    ChrTalk(
        0xB,
        (
            "It seems orbal train service was completely\x01",
            "restored within the space of one night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to that, today's rail\x01",
            "transports could arrive as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm grateful to all the police who worked \x01",
            "through the night to restore service.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4717")

    label("loc_467D")


    ChrTalk(
        0xB,
        (
            "Thanks to that, today's rail\x01",
            "transports could arrive as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm grateful to all the police who worked \x01",
            "through the night to restore service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4717")

    Jump("loc_5215")

    label("loc_471C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_482A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47AE")

    ChrTalk(
        0xB,
        (
            "I understand a train has derailed\x01",
            "near West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if some sort\x01",
            "of cave-in occurred...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4825")

    label("loc_47AE")


    ChrTalk(
        0xB,
        (
            "I understand a train has derailed\x01",
            "near West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if some sort\x01",
            "of cave-in occurred...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4825")

    Jump("loc_5215")

    label("loc_482A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_48D0")

    ChrTalk(
        0xB,
        (
            "If you're looking for ingredients, leave it to me.\x01",
            "Welcome to "Region Foods".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Today, we're offering a great\x01",
            "deal on Republican spring onions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_48D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4958")

    ChrTalk(
        0xB,
        (
            "It seems Southwark and Jeanetta\x01",
            "have decided to go steady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Uh uh, falling in love with a co-worker is enviable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_4958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_49E8")

    ChrTalk(
        0xB,
        (
            "Somehow Jeanetta looks down today.\x01",
            "I'm worried about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She looked so happy yesterday.\x01",
            "Could something have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_49E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4A8C")

    ChrTalk(
        0xB,
        (
            "Good evening, welcome\x01",
            "to "Region Food".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you haven't prepared dinner yet,\x01",
            "by all means please come to buy\x01",
            "your ingredients from us, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5215")

    label("loc_4A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF3")

    ChrTalk(
        0xB,
        (
            "If you're looking for ingredients, leave it to me.\x01",
            "Welcome to "Region Foods".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Starting today, and for the next three days, we'll\x01",
            "be selling our special "Trade Conference Set".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've pulled the finest ingredients from the\x01",
            "Empire, Kingdom, Principality, Republic, and of\x01",
            "course our own Crossbell into this special set.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CEC")

    label("loc_4BF3")


    ChrTalk(
        0xB,
        (
            "Starting today, and for the next three days, we'll\x01",
            "be selling our special "Trade Conference Set".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've pulled the finest ingredients from the\x01",
            "Empire, Kingdom, Principality, Republic, and of\x01",
            "course our own Crossbell into this special set.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CEC")

    Jump("loc_5215")

    label("loc_4CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E52")

    ChrTalk(
        0xB,
        (
            "Welcome to "Region Food", the\x01",
            "reliable ally of every housewife!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you need any help with tonight's menu,\x01",
            "I'd be happy to give you some advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For example, how about a soup\x01",
            "using our fresh "fresh herb" that\x01",
            "just came in this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Careful though. It will\x01",
            "be bitter if you stew\x01",
            "the bay leaves too long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4EE8")

    label("loc_4E52")


    ChrTalk(
        0xB,
        (
            "If you need any help with tonight's menu,\x01",
            "I'd be happy to give you some advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the way, today's recommendation\x01",
            "is fresh herb soup dish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE8")

    Jump("loc_5215")

    label("loc_4EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC4")

    ChrTalk(
        0xB,
        (
            "My daughter is\x01",
            "working on her new\x01",
            "juice stand menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's raining today, so her stand's not open. \x01",
            "She's at home working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, it's great that\x01",
            "she has some ambition.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5030")

    label("loc_4FC4")


    ChrTalk(
        0xB,
        (
            "My daughter is\x01",
            "working on her new\x01",
            "juice stand menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, it's great that\x01",
            "she has some ambition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5030")

    Jump("loc_5215")

    label("loc_5035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515A")

    ChrTalk(
        0xB,
        (
            "If you're looking for ingredients, leave it to me.\x01",
            "Welcome to "Region Foods".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the way, there's a stand that makes\x01",
            "healthy juice using our ingredients,\x01",
            "so please give that a try, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My daughter is running the juice\x01",
            "stand in Governmental District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5215")

    label("loc_515A")


    ChrTalk(
        0xB,
        (
            "If you're looking for ingredients, leave it to me.\x01",
            "Welcome to "Region Foods".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please visit the juice stand in Governmental district. \x01",
            "Their juice is made using our ingredients!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5215")

    Jump("loc_3FCA")

    label("loc_521A")

    TalkEnd(0xB)
    Return()

    # Function_14_3D27 end

    def Function_15_521E(): pass

    label("Function_15_521E")

    Call(0, 16)
    Return()

    # Function_15_521E end

    def Function_16_5222(): pass

    label("Function_16_5222")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_522F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62B8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_527F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_527F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_529E")
    OP_AF(0x21)
    Jump("loc_52C0")

    label("loc_529E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_52AE")
    OP_AF(0x20)
    Jump("loc_52C0")

    label("loc_52AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_52BE")
    OP_AF(0x1F)
    Jump("loc_52C0")

    label("loc_52BE")

    OP_AF(0x1E)

    label("loc_52C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62B3")

    label("loc_52CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52E3")
    Jump("loc_62B3")

    label("loc_52E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62B3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_53E6")

    ChrTalk(
        0xC,
        (
            "I was thinking of doing it sooner or later...\x01",
            "But I've decided to take this opportunity \x01",
            "to introduce my new brand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            ""Greatness shines in the face of\x01",
            "adversity"― I'll create products\x01",
            "everyone will surely love!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_53E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_55C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54FD")

    ChrTalk(
        0xC,
        (
            "The President was\x01",
            "confident because of\x01",
            "those "Aion" weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...But, what is with\x01",
            "those armored soldier-\x01",
            "like monsters in town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Scaring the citizens with those things \x01",
            "without giving a proper notice...\x01",
            "What a serious fail in evaluation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55BD")

    label("loc_54FD")


    ChrTalk(
        0xC,
        (
            "...But really, what is with\x01",
            "those armored soldier-like\x01",
            "monsters in town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Scaring the citizens with those things \x01",
            "without giving a proper notice...\x01",
            "What a serious fail in evaluation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55BD")

    Jump("loc_62B3")

    label("loc_55C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5694")

    ChrTalk(
        0xC,
        (
            "Maybe it's because I'm in retail?\x01",
            "I have a bad habit of feel\x01",
            "everything from a distance, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm not sure how to put this...\x01",
            "What President Dieter said\x01",
            "seems rather irrational to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_5694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_572D")

    ChrTalk(
        0xC,
        (
            "Three days from now, each of us will\x01",
            "take turns going to the polling place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, I'm\x01",
            "still undecided.\x01",
            "*sigh*, what to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_572D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_57DD")

    ChrTalk(
        0xC,
        (
            "I don't know if it's an armed\x01",
            "group or whatever, but I\x01",
            "can't stand guys like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Trapping people with explosions...\x01",
            "It's nothing but sheer stupidity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_57DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58E2")

    ChrTalk(
        0xC,
        (
            "I feel like there's fewer customers walking\x01",
            "in with smiles on their faces lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Given yesterday's train\x01",
            "accident, I suppose\x01",
            "that's only human nature...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wish they could at\x01",
            "least forget their\x01",
            "troubles while shopping.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_597F")

    label("loc_58E2")


    ChrTalk(
        0xC,
        (
            "I feel like there's fewer customers walking\x01",
            "in with smiles on their faces lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wish they could at\x01",
            "least forget their\x01",
            "troubles while shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_597F")

    Jump("loc_62B3")

    label("loc_5984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_59B5")

    ChrTalk(
        0xC,
        "My, it sure is noisy outside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_59B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC5")

    ChrTalk(
        0xC,
        (
            "When going out, I often choose clothes\x01",
            "based on my mood. However, there are also\x01",
            "times when my clothes determine my mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So if you are ever feeling down,\x01",
            "try wearing bright colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you do that, your\x01",
            "depression could fly away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BA3")

    label("loc_5AC5")


    ChrTalk(
        0xC,
        (
            "When going out, I often choose clothes\x01",
            "based on my mood. However, there are also\x01",
            "times when my clothes determine my mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Looking for clothes that match up with how\x01",
            "you feel. ...That's also a method of choosing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BA3")

    Jump("loc_62B3")

    label("loc_5BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C72")

    ChrTalk(
        0xC,
        (
            "The more expensive clothes and handbags\x01",
            "are, the more they influence unseen trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There are many that are durable and can be used\x01",
            "for a long time, so I think they're worth it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_5C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5D1F")

    ChrTalk(
        0xC,
        (
            "Although fashion is ever changing, that phenomenon\x01",
            "is actually caused by everyone collectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a boutique owner, I try\x01",
            "to create fashion trends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_5D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5D61")

    ChrTalk(
        0xC,
        (
            "Welcome, please\x01",
            "enjoy shopping\x01",
            "in the evening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_5D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DF6")

    ChrTalk(
        0xC,
        "The Trade Conference has finally started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As someone in the fashion business, I need\x01",
            "to pay attention to the VIPs' fashions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B3")

    label("loc_5DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5F9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EBC")

    ChrTalk(
        0xC,
        (
            "Welcome. Please have\x01",
            "a look at all the latest\x01",
            "fashions we have in stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you would like to try something on,\x01",
            "please don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F9A")

    label("loc_5EBC")


    ChrTalk(
        0xC,
        (
            "Mr. Hanson was my business\x01",
            "rival when he sold clothes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At the same time, we were good rivals and\x01",
            "we improved each other's fashion sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I like shoes too, but I'm glad\x01",
            "I didn't specialize in them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5F9A")

    Jump("loc_62B3")

    label("loc_5F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_615E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60A5")

    ChrTalk(
        0xC,
        (
            "You can't skip out on fashion\x01",
            "just because it's raining.\x01",
            "That's just nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fashion is all about time, place\x01",
            "and occasion. We have styles\x01",
            "specifically for rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you would like, I could\x01",
            "show you some of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6159")

    label("loc_60A5")


    ChrTalk(
        0xC,
        (
            "You can't skip out on fashion\x01",
            "just because it's raining.\x01",
            "That's just nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fashion is all about time, place\x01",
            "and occasion. We have styles\x01",
            "specifically for rainy days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6159")

    Jump("loc_62B3")

    label("loc_615E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_62B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6227")

    ChrTalk(
        0xC,
        (
            "Welcome to\x01",
            "boutique "Lucca".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This store offers clothes from\x01",
            "various manufacturers that\x01",
            "I have selected personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please have a look at them at your leisure.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_62B3")

    label("loc_6227")


    ChrTalk(
        0xC,
        (
            "This store offers clothes from\x01",
            "various manufacturers that\x01",
            "I have selected personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please have a look at them at your leisure.\x02",
    )

    CloseMessageWindow()

    label("loc_62B3")

    Jump("loc_522F")

    label("loc_62B8")

    TalkEnd(0xC)
    Return()

    # Function_16_5222 end

    def Function_17_62BC(): pass

    label("Function_17_62BC")

    Call(0, 18)
    Return()

    # Function_17_62BC end

    def Function_18_62C0(): pass

    label("Function_18_62C0")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7283")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_631D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_631D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_635D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_633C")
    OP_AF(0x11)
    Jump("loc_634E")

    label("loc_633C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_634C")
    OP_AF(0x10)
    Jump("loc_634E")

    label("loc_634C")

    OP_AF(0xF)

    label("loc_634E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_727E")

    label("loc_635D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6371")
    Jump("loc_727E")

    label("loc_6371")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_644B")

    ChrTalk(
        0xD,
        (
            "When I saw that gigantic tree... Immediately,\x01",
            "tales of the gigantic structure that appeared\x01",
            "last year in Liberl came to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Thankfully our orbments\x01",
            "still work, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_644B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6554")

    ChrTalk(
        0xD,
        (
            "I'm pretty sure it was the State Guard who defended\x01",
            "against those Imperial Railway Cannons, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This situation is just one\x01",
            "unsettling thing after the next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The realization of a "Continental Alliance"\x01",
            "is purely academic, isn't it...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_6554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_66A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_660A")

    ChrTalk(
        0xD,
        "Such a sudden speech was surprising...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I mean, President Dieter and\x01",
            "Secretary of Defense Arios\x01",
            "said that much already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I believe in those two.\x02",
    )

    CloseMessageWindow()
    Jump("loc_669C")

    label("loc_660A")


    ChrTalk(
        0xD,
        (
            "I was surprised by their sudden speech,\x01",
            "but President Dieter and Secretary of\x01",
            "Defense Arios said that much, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I believe in those two.\x02",
    )

    CloseMessageWindow()

    label("loc_669C")

    Jump("loc_727E")

    label("loc_66A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_67AC")

    ChrTalk(
        0xD,
        (
            "To solve the root cause of Crossbell's\x01",
            "various problems, I think there is\x01",
            "no other path but independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To think something like that happened in the city... \x01",
            "We can't be sure that by obeying the major\x01",
            "powers again, order will be maintained.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_67AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6861")

    ChrTalk(
        0xD,
        (
            "Like many others, I wonder\x01",
            "if the Mainz incident was\x01",
            "some Imperial scheme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's because of incidents\x01",
            "like this that we need more\x01",
            "troops to defend the state.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_6861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_690F")

    ChrTalk(
        0xD,
        (
            "There's a rumor going around that\x01",
            "yesterday's train derailment was\x01",
            "caused by something called a "Cryptid."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmm, but just what is a Cryptid, I wonder.\x02",
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_690F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_69AE")

    ChrTalk(
        0xD,
        (
            "I've been hearing ambulances'\x01",
            "sirens for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wonder if it's a terrorist attack.\x01",
            "...We have already had so many tragedies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_69AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8D")

    ChrTalk(
        0xD,
        (
            "The value of accessories\x01",
            "isn't the same to everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I received a handmade brooch from my\x01",
            "granddaughter the other day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, it is more valuable\x01",
            "than the greatest treasure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6B17")

    label("loc_6A8D")


    ChrTalk(
        0xD,
        (
            "I received a handmade brooch from my\x01",
            "granddaughter the other day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, it is more valuable\x01",
            "than the greatest treasure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B17")

    Jump("loc_727E")

    label("loc_6B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6CCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1D")

    ChrTalk(
        0xD,
        (
            "Hmm, state independence, huh. This is\x01",
            "a problem that requires a lot of thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Though I myself once threw\x01",
            "away the Empire and came\x01",
            "to live here in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I cannot help but say this\x01",
            "is an unthinkable problem.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6CC6")

    label("loc_6C1D")


    ChrTalk(
        0xD,
        (
            "Though I myself once threw\x01",
            "away the Empire and came\x01",
            "to live here in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't help but say the state independence\x01",
            "proposal is a difficult question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CC6")

    Jump("loc_727E")

    label("loc_6CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6D4F")

    ChrTalk(
        0xD,
        (
            "Hmm, so the Trade Conference\x01",
            "finally started, has it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Anyway, I just want it to be\x01",
            "a meaningful conference.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_6D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E10")

    ChrTalk(
        0xD,
        "It's already dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's right, the Arc-en-ciel's\x01",
            "performance for the heads of\x01",
            "state should ending soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mmm, I do hope they are\x01",
            "enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6E9E")

    label("loc_6E10")


    ChrTalk(
        0xD,
        (
            "That's right, the Arc-en-ciel's\x01",
            "performance for the heads of\x01",
            "state should ending soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Mmm, I do hope they are\x01",
            "enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E9E")

    Jump("loc_727E")

    label("loc_6EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6F30")

    ChrTalk(
        0xD,
        (
            "I saw the inauguration\x01",
            "ceremony from our rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Orchis Tower is truly a sight to\x01",
            "behold. I am at a loss for words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_727E")

    label("loc_6F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7080")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FE0")

    ChrTalk(
        0xD,
        (
            "Welcome to "Baker's"\x01",
            "accessories shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there is anything here that catches\x01",
            "your eye then please, take a closer look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707B")

    label("loc_6FE0")


    ChrTalk(
        0xD,
        (
            "Many..."warm-hearted"\x01",
            "customers visit our\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's very different from Imperial nobles,\x01",
            "though I do not mean to compare the two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707B")

    Jump("loc_727E")

    label("loc_7080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_718B")

    ChrTalk(
        0xD,
        (
            "When it rains like this, I am\x01",
            "reminded of my days as an art dealer\x01",
            "in the Empire for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The work pulling in\x01",
            "valuable works of art back\x01",
            "then was hard every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*sigh*, I feel out of breath\x01",
            "just thinking back on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_71FF")

    label("loc_718B")


    ChrTalk(
        0xD,
        (
            "I apologize. You all are probably not\x01",
            "interested in my personal stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Welcome. Please,\x01",
            "take your time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71FF")

    Jump("loc_727E")

    label("loc_7204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_727E")

    ChrTalk(
        0xD,
        (
            "Welcome. Please,\x01",
            "have a look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our accessories are\x01",
            "great as gifts or as a\x01",
            "reward for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_727E")

    Jump("loc_62CD")

    label("loc_7283")

    TalkEnd(0xD)
    Return()

    # Function_18_62C0 end

    def Function_19_7287(): pass

    label("Function_19_7287")

    SetScenarioFlags(0x2, 4)
    Call(0, 20)
    Return()

    # Function_19_7287 end

    def Function_20_728E(): pass

    label("Function_20_728E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73BE")
    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733D")

    ChrTalk(
        0xE,
        (
            "Huh, where did you\x01",
            "guys come in from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Oh, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "For now, if you want to\x01",
            "buy something, speak to me\x01",
            "from across the counter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_73BA")

    label("loc_733D")


    ChrTalk(
        0xE,
        (
            "For now, if you want to\x01",
            "buy something, speak to me\x01",
            "from across the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, please don't\x01",
            "touch that inventory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BA")

    TalkEnd(0xE)
    Return()

    label("loc_73BE")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74BE")

    ChrTalk(
        0xE,
        (
            "Oh, hello. Welcome to General\x01",
            "Goods Corner "Southwark".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "From daily necessities to souvenirs, we\x01",
            "sell a wide variety of different products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Please, take your time looking through them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7548")

    label("loc_74BE")


    ChrTalk(
        0xE,
        (
            "From daily necessities to souvenirs, we\x01",
            "sell a wide variety of different products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Please, take your time looking through them.\x02",
    )

    CloseMessageWindow()

    label("loc_7548")

    TalkEnd(0xE)
    Return()

    label("loc_7551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76BC")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd spoke to shopkeeper\x01",
            "Southwark in a low voice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000F(Excuse me, how\x01",
            "much is it for a \x01",
            ""Tick-Tock Michey"?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "(Oh, that'll be 500 mira.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "(Uh uh, might it be a\x01",
            "present for that child?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Uh, yes. I'm still thinking about it though.)\x02\x03",
            "#00003F(It's 500 mira... \x01",
            "Should I buy it for Shing?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7712")

    label("loc_76BC")


    ChrTalk(
        0xE,
        (
            "(It's 500 mira for a Tick-Tock Michey. \x01",
            "Are you buying it?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Hmm...)\x02",
    )

    CloseMessageWindow()

    label("loc_7712")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Buy a "Tick-Tock Michey"\x01",      # 0
            "Still Thinking About It\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7809")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F(Umm, then, I'd like one please.)\x02",
    )

    CloseMessageWindow()
    Sound(20, 0, 80, 0)

    ChrTalk(
        0xE,
        "(Alright. Thanks for your business.)\x02",
    )

    CloseMessageWindow()
    Call(0, 52)
    Jump("loc_78B1")

    label("loc_7809")


    ChrTalk(
        0x101,
        "#00000F(Umm, then, please...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(I don't have the mira...\x01",
            "*sigh*, just how poor am I?)\x02\x03",
            "#00000F(Sorry, I'll go without.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "(???)\x02",
    )

    CloseMessageWindow()

    label("loc_78B1")

    Jump("loc_78EF")

    label("loc_78B6")


    ChrTalk(
        0x101,
        (
            "#00003F(I'd like to think about\x01",
            "it a bit longer...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78EF")

    TalkEnd(0xE)
    Return()

    label("loc_78F8")


    ChrTalk(
        0xE,
        (
            "It seems he\x01",
            "loved it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, as expected,\x01",
            "Michey sure is great.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    label("loc_7944")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_794E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_799E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_799E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_79BD")
    OP_AF(0x1D)
    Jump("loc_7A3F")

    label("loc_79BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_79CD")
    OP_AF(0x1C)
    Jump("loc_7A3F")

    label("loc_79CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_79DD")
    OP_AF(0x1B)
    Jump("loc_7A3F")

    label("loc_79DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_79ED")
    OP_AF(0x1A)
    Jump("loc_7A3F")

    label("loc_79ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_79FD")
    OP_AF(0x19)
    Jump("loc_7A3F")

    label("loc_79FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A0D")
    OP_AF(0x18)
    Jump("loc_7A3F")

    label("loc_7A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_7A1D")
    OP_AF(0x17)
    Jump("loc_7A3F")

    label("loc_7A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7A2D")
    OP_AF(0x16)
    Jump("loc_7A3F")

    label("loc_7A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7A3D")
    OP_AF(0x15)
    Jump("loc_7A3F")

    label("loc_7A3D")

    OP_AF(0x14)

    label("loc_7A3F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8DDE")

    label("loc_7A4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A62")
    Jump("loc_8DDE")

    label("loc_7A62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DDE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B61")

    ChrTalk(
        0xE,
        (
            "All we merchants can do\x01",
            "is keep operating our\x01",
            "businesses as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The prospects for reopening international trade\x01",
            "routes don't look so good, but... We've got to\x01",
            "think of a way to get through this somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DDE")

    label("loc_7B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7C0D")

    ChrTalk(
        0xE,
        (
            "In times like these, it's reassuring\x01",
            "to have one's loved ones close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm not sure how to say this, but I\x01",
            "feel courage welling up from inside me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DDE")

    label("loc_7C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D9A")

    ChrTalk(
        0xE,
        (
            "This morning, an evacuation notice from the\x01",
            "Republican government suddenly came in.\x01",
            "All Republic citizens are to return ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They're preparing to use force.\x01",
            "I don't know what's going to happen\x01",
            "next, but it's not hard to imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To me, the most precious\x01",
            "thing in Crossbell is my\x01",
            "girlfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That's why, no matter\x01",
            "what happens, I've\x01",
            "decided to stay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7E02")

    label("loc_7D9A")


    ChrTalk(
        0xE,
        (
            "No matter what happens, I've\x01",
            "decided to stay put here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I'll definitely protect my girlfriend.\x02",
    )

    CloseMessageWindow()

    label("loc_7E02")

    Jump("loc_8DDE")

    label("loc_7E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7EBB")

    ChrTalk(
        0xE,
        (
            "Why did that have to happen to Miss Ilya?\x01",
            "It was the long-awaited renewal performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wasn't scared during the attack, but... \x01",
            "Now I'm positively mad!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DDE")

    label("loc_7EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FDA")

    ChrTalk(
        0xE,
        (
            "The renewal version of\x01",
            ""Golden Sun, Silver Moon"\x01",
            "finally opens this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But with the situation in\x01",
            "Mainz right now, this is\x01",
            "no time to be festive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A play is a play...letting everyone\x01",
            "enjoy it could, in a sense,\x01",
            "give them courage and energy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_808C")

    label("loc_7FDA")


    ChrTalk(
        0xE,
        (
            "But with the situation in\x01",
            "Mainz right now, this is\x01",
            "no time to be festive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A play is a play...letting everyone\x01",
            "enjoy it could, in a sense,\x01",
            "give them courage and energy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_808C")

    Jump("loc_8DDE")

    label("loc_8091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_813D")

    ChrTalk(
        0xE,
        (
            "I've been in business for a long\x01",
            "time, but after I got a girlfriend\x01",
            "my whole world changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "How to put it... This must\x01",
            "be what they call happiness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DDE")

    label("loc_813D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_81C6")

    ChrTalk(
        0xE,
        (
            "There's an uproar over the train\x01",
            "accident that occurred west of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I hope it's not a terrorist attack, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DDE")

    label("loc_81C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82CA")

    ChrTalk(
        0xE,
        (
            "A referendum to question the independence propriety...\x01",
            "It's a serious responsibility even though\x01",
            "it's just confirming the will of the people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Though I can't vote because\x01",
            "I'm a Republican, the question\x01",
            "really made me think.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_835E")

    label("loc_82CA")


    ChrTalk(
        0xE,
        "The referendum to question the independence propriety...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Though I can't vote because\x01",
            "I'm a Republican, the question\x01",
            "really made me think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_835E")

    Jump("loc_8DDE")

    label("loc_8363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_84BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_842C")

    ChrTalk(
        0xE,
        (
            "At first I thought she was like a cute\x01",
            "little sister... I don't understand\x01",
            "people's feelings, do I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, I'm happy. Thank goodness\x01",
            "I had the courage to ask her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_84B8")

    label("loc_842C")


    ChrTalk(
        0xE,
        (
            "Jeanetta, at first I thought she\x01",
            "was like a cute little sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, I'm happy. Thank goodness\x01",
            "I had the courage to ask her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84B8")

    Jump("loc_8DDE")

    label("loc_84BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_85D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857E")

    ChrTalk(
        0xE,
        (
            "It seems Jeanetta had dinner\x01",
            "with some rich men last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "But it seems she was utterly rejected by all of them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hmm, I wonder why I feel relieved.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_85D4")

    label("loc_857E")


    ChrTalk(
        0xE,
        "Hmm, I wonder why I feel relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "In other words, could this feeling be...\x02",
    )

    CloseMessageWindow()

    label("loc_85D4")

    Jump("loc_8DDE")

    label("loc_85D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_876C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86ED")

    ChrTalk(
        0xE,
        (
            "Miss Jeanetta looks to be really\x01",
            "happy since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She was saying something I didn't\x01",
            "understand, like that tomorrow she's going\x01",
            "to make a fresh start as "super Jeanetta"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I don't know but for some reason I'm really worried.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8767")

    label("loc_86ED")


    ChrTalk(
        0xE,
        (
            "Miss Jeanetta looks to be really\x01",
            "happy since this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I don't know but for some reason I'm really worried.\x02",
    )

    CloseMessageWindow()

    label("loc_8767")

    Jump("loc_8DDE")

    label("loc_876C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8883")

    ChrTalk(
        0xE,
        (
            "The inauguration ceremony, eh? \x01",
            "I couldn't see it, but it must've been amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's amazing that all those heads\x01",
            "of state gathered. You only ever see \x01",
            "them in news magazines and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't wait for the next\x01",
            "issue of Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8902")

    label("loc_8883")


    ChrTalk(
        0xE,
        (
            "The inauguration ceremony, eh? \x01",
            "It must've been amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, I can't wait\x01",
            "for the next issue\x01",
            "of Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8902")

    Jump("loc_8DDE")

    label("loc_8907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B0E")

    ChrTalk(
        0xE,
        (
            "Did you know Arc-en-ciel's\x01",
            ""Golden Sun, Silver Moon" is\x01",
            "getting a renewal performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The details haven't been announced, but I\x01",
            "heard they are making a bold new addition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ha ha ha. And somehow...\x01",
            "I was able to get two\x01",
            "tickets for the opening night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FWow, glad to hear it.\x02\x03",
            "#00309FBy the way, who are you takin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Ugh... Please, don't ask me that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A-Anyway, there's a month\x01",
            "left until the opening night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I'll do something about that before then. Yeah.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8BB3")

    label("loc_8B0E")


    ChrTalk(
        0xE,
        (
            "I was lucky to be able to get two\x01",
            "tickets for the opening night of the\x01",
            "Arc-en-ciel renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm planning on looking\x01",
            "for someone to go with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BB3")

    Jump("loc_8DDE")

    label("loc_8BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BD3")
    Call(0, 21)
    Jump("loc_8C23")

    label("loc_8BD3")


    ChrTalk(
        0xE,
        (
            "I'd understand if it was her birthday, but...\x01",
            "She's pestering me as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C23")

    Jump("loc_8DDE")

    label("loc_8C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7A")

    ChrTalk(
        0xE,
        (
            "Oh, hello. Welcome to General\x01",
            "Goods Corner "Southwark".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Lately, I've been stocking more Michey goods\x01",
            "to live up to my customers' high expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "If you like, please have a look at them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWow, Michey goods, huh?\x01",
            "I'm sure Tio will be delighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, that's for sure.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8DDE")

    label("loc_8D7A")


    ChrTalk(
        0xE,
        (
            "Fortunately, our Michey \x01",
            "goods are very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "If you like, please have a look at them.\x02",
    )

    CloseMessageWindow()

    label("loc_8DDE")

    Jump("loc_794E")

    label("loc_8DE3")

    TalkEnd(0xE)
    Return()

    # Function_20_728E end

    def Function_21_8DE7(): pass

    label("Function_21_8DE7")

    OP_4B(0x12, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x12,
        (
            "Ah, this Michey plushy is so cute!\x01",
            "I'd like this one, Mr. Southwark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, sure. \x01",
            "Umm, that would be 500 mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "That's not what I mean.\x01",
            "Buy it for me as a present, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Why do I have to buy you a present?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "It's because we work at the same department store.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Oh no no no. \x01",
            "That's no reason at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x12, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_21_8DE7 end

    def Function_22_8F62(): pass

    label("Function_22_8F62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90A2")

    ChrTalk(
        0xFE,
        (
            "Just when martial law was canceled that\x01",
            "mysterious gigantic tree appeared... \x01",
            "And the threat of the two major powers remains too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Against unprecedented difficulties like these,\x01",
            "what can a simple man such as myself do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All any of us can do is think\x01",
            "logically, and then act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_913B")

    label("loc_90A2")


    ChrTalk(
        0xFE,
        (
            "Against unprecedented difficulties like these,\x01",
            "what can a simple man such as myself do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All any of us can do is think\x01",
            "logically, and then act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913B")

    Jump("loc_A5A5")

    label("loc_9140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_91DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_915B")
    Call(0, 23)
    Jump("loc_91D5")

    label("loc_915B")


    ChrTalk(
        0xFE,
        (
            "Like Mr. Lloyd says, we will\x01",
            "abide to martial law and\x01",
            "ascertain the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Please, everyone. Be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_91D5")

    Jump("loc_A5A5")

    label("loc_91DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_93D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9329")

    ChrTalk(
        0xFE,
        (
            "It's been a mere week since the referendum\x01",
            "and the situation's already this bad... I can't\x01",
            "even imagine what's going to happen next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it probably won't be surprising\x01",
            "if something were to happen next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the continued existence of this department\x01",
            "store, I need to exhaust all my ideas.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_93D3")

    label("loc_9329")


    ChrTalk(
        0xFE,
        (
            "Anyway, it probably won't be surprising\x01",
            "if something were to happen next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the continued existence of this department\x01",
            "store, I need to exhaust all my ideas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93D3")

    Jump("loc_A5A5")

    label("loc_93D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9546")

    ChrTalk(
        0xFE,
        (
            "Today, a charity event will be held at\x01",
            "the City Meeting Hall with support for\x01",
            "the city's reconstruction as the theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The plan is for the city and the\x01",
            "Merchants Association to come\x01",
            "together and cheer up the citizens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our department store is doing all it\x01",
            "can to support the event, so please\x01",
            "drop by if you have the chance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_962F")

    label("loc_9546")


    ChrTalk(
        0xFE,
        (
            "Today, a charity event will be held at\x01",
            "the City Meeting Hall with support for\x01",
            "the city's reconstruction as the theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our department store is doing all it\x01",
            "can to support the event, so please\x01",
            "drop by if you have the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_962F")

    Jump("loc_A5A5")

    label("loc_9634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_96FE")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group occupying Mainz...\x01",
            "The situation reminds me of the nightmare\x01",
            "that was the disputes period back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope the\x01",
            "situation's resolved ASAP.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5A5")

    label("loc_96FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_98C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9719")
    Call(0, 26)
    Jump("loc_98BF")

    label("loc_9719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9844")

    ChrTalk(
        0xFE,
        (
            "I understand yesterday's train\x01",
            "derailment seems to have been\x01",
            "caused by a huge ogre-like monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And lately, there's been rumors of\x01",
            "large, mysterious monsters appearing\x01",
            "all throughout the autonomous state, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder if those events\x01",
            "are connected somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_98BF")

    label("loc_9844")


    ChrTalk(
        0xFE,
        (
            "A huge ogre-like monster, and\x01",
            "large, mysterious monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder if those events\x01",
            "are connected somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98BF")

    Jump("loc_A5A5")

    label("loc_98C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9989")

    ChrTalk(
        0xFE,
        (
            "A customer who passed\x01",
            "by the station told me\x01",
            "a train has derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know the details, but...\x01",
            "Anyway, I'm worried about the people\x01",
            "taken by ambulance to the hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5A5")

    label("loc_9989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9A5F")

    ChrTalk(
        0xFE,
        (
            "Lately, I have been hearing\x01",
            "customers talking about the\x01",
            "state independence pros and cons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of people support it. Also,\x01",
            "a lot of people are worried about\x01",
            "the two major powers' reaction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5A5")

    label("loc_9A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9BBF")

    ChrTalk(
        0xFE,
        (
            "Thinking back on it now, the events of the Trade\x01",
            "Conference the other day were a veritable storm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was surprised by the\x01",
            "terrorist attack as well as\x01",
            "Mayor Dieter's proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know how the proposal will be received by\x01",
            "the international community, but... It's certain\x01",
            "that all eyes will be on Crossbell going forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5A5")

    label("loc_9BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9D7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CD3")

    ChrTalk(
        0xFE,
        (
            "A lot of people are on\x01",
            "our roof viewing Orchis\x01",
            "Tower today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, we have more\x01",
            "customer traffic, and sales are up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But above all, I am glad for this\x01",
            "lively atmosphere. The customers\x01",
            "are enjoying themselves as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9D76")

    label("loc_9CD3")


    ChrTalk(
        0xFE,
        (
            "A lot of people are on\x01",
            "our roof viewing Orchis\x01",
            "Tower today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our store is busier than you usually see,\x01",
            "and the customers are enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D76")

    Jump("loc_A5A5")

    label("loc_9D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9E10")

    ChrTalk(
        0xFE,
        (
            "Like usual, today's\x01",
            "operating hours\x01",
            "end at 8:00.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please pay attention to not forget what\x01",
            "you bought and your own belongings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5A5")

    label("loc_9E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F3D")

    ChrTalk(
        0xFE,
        (
            "Although it's embarrassing to say, I joined the\x01",
            "customers in viewing the inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The majesty of "Orchis Tower"\x01",
            "is truly a sight to behold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A skyscraper that stretches 40\x01",
            "floors above the ground... One could\x01",
            "call it the new symbol of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9FAB")

    label("loc_9F3D")


    ChrTalk(
        0xFE,
        (
            "A skyscraper that stretches 40\x01",
            "floors above the ground... One could\x01",
            "call it the new symbol of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FAB")

    Jump("loc_A5A5")

    label("loc_9FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A33A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A141")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0DB")
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "Oh, Lady Elie. You have brought an\x01",
            "unusual guest with you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAh, yes. Today, we're showing\x01",
            "this boy around Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In that case, I am happy\x01",
            "you brought him here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, take as\x01",
            "long as you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A13C")

    label("loc_A0DB")


    ChrTalk(
        0x11,
        (
            "I'm pleased that you brought\x01",
            "him to our store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, take as\x01",
            "long as you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A13C")

    Jump("loc_A335")

    label("loc_A141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A28C")

    ChrTalk(
        0xFE,
        (
            "The Trade Conference will\x01",
            "finally be held tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Representatives from Crossbell and the\x01",
            "four surrounding nations will all meet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "History will look back on this\x01",
            "as one of the most important\x01",
            "events of the decade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am not sure how to express it, but I\x01",
            "am quite excited to learn the outcome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A335")

    label("loc_A28C")


    ChrTalk(
        0xFE,
        (
            "Representatives from Crossbell and the\x01",
            "four surrounding nations will all meet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am not sure how to express it, but I\x01",
            "am quite excited to learn the outcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A335")

    Jump("loc_A5A5")

    label("loc_A33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A355")
    Call(0, 24)
    Jump("loc_A404")

    label("loc_A355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A367")
    Call(0, 25)
    Jump("loc_A404")

    label("loc_A367")


    ChrTalk(
        0x11,
        (
            "We have prepared a small\x01",
            "gift for the customers who come\x01",
            "to our store on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, everyone. Enjoy as much\x01",
            "shopping as you'd like today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A404")

    Jump("loc_A5A5")

    label("loc_A409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A5A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A424")
    Call(0, 24)
    Jump("loc_A5A5")

    label("loc_A424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50D")

    ChrTalk(
        0xFE,
        (
            "Everyone, allow me to thank\x01",
            "you for coming to "Times"\x01",
            "department store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our establishment has many types of sales\x01",
            "counters to attract the customers' attention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please take your time, and enjoy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A5A5")

    label("loc_A50D")


    ChrTalk(
        0xFE,
        (
            "We have many types of sales counters to attract\x01",
            "the customers' attention in this department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please take\x01",
            "your time and enjoy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5A5")

    TalkEnd(0xFE)
    Return()

    # Function_22_8F62 end

    def Function_23_A5A9(): pass

    label("Function_23_A5A9")

    OP_4B(0x11, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x11,
        "Lady Elie and the Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Could the movement restrictions have been...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo... Unfortunately,\x01",
            "they're still in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FMr. Neston, will you tell us how\x01",
            "the department store's doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes. Yesterday, we were keeping open as\x01",
            "much as we could even after the martial law,\x01",
            "like the customers wished we did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Shortly after, that mist appeared. Immediately\x01",
            "afterward, customers and staff came rushing\x01",
            "inside. They've been trapped here ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were making new\x01",
            "announcements all night, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Really, what does this\x01",
            "government think they're doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F...I see. We really have\x01",
            "to intervene now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FSir, we're now\x01",
            "acting to bring this\x01",
            "situation to an end.\x02\x03",
            "Everyone, please. Continue to\x01",
            "remain indoors until the situation\x01",
            "has calmed down outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Understood. ...Please\x01",
            "be careful yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, that's right.\x01",
            "Please, take this\x01",
            "as a protection.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FD, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00100FMr. Neston... \x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1BB, 4)
    Return()

    # Function_23_A5A9 end

    def Function_24_AA0A(): pass

    label("Function_24_AA0A")


    ChrTalk(
        0x11,
        (
            "Hello. And welcome to\x01",
            ""Times" department store.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x11,
        "Well, well. If it isn't Lady Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I heard that you were visiting several\x01",
            "nations with Chairman MacDowell,\x01",
            "but it seems you have returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, just a few days ago.\x02\x03",
            "We will be acting again as the Special Support\x01",
            "Section, so please, give us your support again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, of course. \x01",
            "I will pray for your success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FDo you know the\x01",
            "manager, Miss Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, he has known my grandfather since a long \x01",
            "time ago and he's always treated us more than well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, that's the Chairman's daughter for you.\x01",
            "And I'm sure you're flexible, right, manager?\x02\x03",
            "I mean, I was wondering if we, who are her\x01",
            "companions, would get the VIP treatment too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x105, 500)
    Sleep(100)

    ChrTalk(
        0x11,
        (
            "No. Please know that you\x01",
            "will not be having a special\x01",
            "treatment like Lady Elie has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We will treat all of you the same\x01",
            "as we would any other customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, there you have it.\x01",
            "I'm sorry for you, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FOh boy, he's so serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, a little too much, maybe.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 3)
    Return()

    # Function_24_AA0A end

    def Function_25_AE67(): pass

    label("Function_25_AE67")


    ChrTalk(
        0x11,
        (
            "Ladies and gentlemen, thank you for coming\x01",
            "to our establishment with such a bad weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "If you like, please take his.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00105FMr. Neston, this is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, it is a little thank\x01",
            "you to our customers who\x01",
            "visit us even in rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It is a service we have started\x01",
            "that is limited to just the first\x01",
            "100 customers on said days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see, this is a\x01",
            "nice service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, the rain seems a little\x01",
            "more fun now, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you very much. \x01",
            "I am glad to hear you say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, ladies and gentlemen, please \x01",
            "enjoy your shopping on this rainy day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 4)
    Return()

    # Function_25_AE67 end

    def Function_26_B107(): pass

    label("Function_26_B107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_END)), "loc_B290")

    ChrTalk(
        0x11,
        "Thank you for coming today too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "If you like, please take his.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FOh, this is that service for rainy days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It is I who should thank all of you\x01",
            "for being our longtime customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Ladies and gentlemen, please enjoy\x01",
            "your shopping on this rainy day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B50E")

    label("loc_B290")


    ChrTalk(
        0x11,
        (
            "Thank you for coming to our\x01",
            "store with such a bad weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "If you like, please take his.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x20B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00105FMr. Neston, this is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, it is a little thank\x01",
            "you to our customers who\x01",
            "visit us even in rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It is a service we have started\x01",
            "that is limited to just the first\x01",
            "100 customers on said days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see, this is a\x01",
            "nice service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, the rain seems a little\x01",
            "more fun now, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you very much. \x01",
            "I am glad to hear you say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Then, ladies and gentlemen, please \x01",
            "enjoy your shopping on this rainy day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B50E")

    SetScenarioFlags(0x16C, 5)
    Return()

    # Function_26_B107 end

    def Function_27_B512(): pass

    label("Function_27_B512")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B5C9")

    ChrTalk(
        0xFE,
        (
            "All of the staff here are\x01",
            "committed to getting\x01",
            "through these hard times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am committed too...\x01",
            "Or perhaps I should say I'll do\x01",
            "my best as a committed lady!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_B5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B650")

    ChrTalk(
        0xFE,
        (
            "Actually I'm full of anxiety,\x01",
            "but seeing Mr. Southwark's\x01",
            "face calms me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, what a mysterious feeling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_B650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B70D")

    ChrTalk(
        0xFE,
        (
            "Mr. Southwark is saying\x01",
            "he'll stay behind in\x01",
            "Crossbell because of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the situation, I'd never tell him to do\x01",
            "something like that, but I'm happy to hear that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_B70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B7BA")

    ChrTalk(
        0xFE,
        (
            "...No matter how much I try to,\x01",
            "I can't forget the fear I felt\x01",
            "when Arc-en-ciel was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What on earth were the criminals\x01",
            "trying to achieve...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_B7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B89C")

    ChrTalk(
        0xFE,
        (
            "I'm planning on seeing the long-\x01",
            "awaited Arc-en-ciel renewal\x01",
            "performance after work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have been looking\x01",
            "forward to it recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll try not to miss even\x01",
            "a single moment of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B903")

    label("loc_B89C")


    ChrTalk(
        0xFE,
        (
            "I have been looking\x01",
            "forward to it recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll try not to miss even\x01",
            "a single moment of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B903")

    Jump("loc_BE72")

    label("loc_B908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9BE")

    ChrTalk(
        0xFE,
        (
            "Tomorrow is the opening day of \x01",
            "Arc-en-ciel's "Golden Sun, Silver\x01",
            "Moon" renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to see it\x01",
            "with Mr. Southwark.\x01",
            "Oh, I can't really wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_B9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BA31")

    ChrTalk(
        0xFE,
        "A-A lot of ambulances went by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm worried about the patients being taken to the hospital.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_BA31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BAE1")

    ChrTalk(
        0xFE,
        (
            "So why do we want independence in\x01",
            "the first place? I don't understand\x01",
            "complicated things, you see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that's right; I'll have Mr. Southwark tell me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_BAE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BAEF")
    Jump("loc_BE72")

    label("loc_BAEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BC62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC0F")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I thought yesterday\x01",
            "went very well, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But really, senior Cynthia is so charming.\x01",
            "I think I'm in love with her,\x01",
            "even though she's a woman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But while that may be true, I\x01",
            "really wish at least one of them\x01",
            "had been interested in me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BC5D")

    label("loc_BC0F")


    ChrTalk(
        0xFE,
        (
            "*sob*... I wonder if\x01",
            "there's anyone out there\x01",
            "who understands my charms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC5D")

    Jump("loc_BE72")

    label("loc_BC62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_BCEA")

    ChrTalk(
        0xFE,
        (
            "The clothes are ready and the\x01",
            "makeup condition is perfect too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhuhu, I'm going to be a bit different tonight㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE72")

    label("loc_BCEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BE0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD97")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, in this world there're\x01",
            "also proactive customers, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How long has it been since the last mixer? \x01",
            "Evening can't come soon enough!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BE0A")

    label("loc_BD97")


    ChrTalk(
        0xFE,
        (
            "And all of our guests\x01",
            "are businessmen working\x01",
            "in Waterfront Area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is my chance! My ultimate chance!\x02",
    )

    CloseMessageWindow()

    label("loc_BE0A")

    Jump("loc_BE72")

    label("loc_BE0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BE1D")
    Jump("loc_BE72")

    label("loc_BE1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BE69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE38")
    Call(0, 21)
    Jump("loc_BE64")

    label("loc_BE38")


    ChrTalk(
        0xFE,
        "*sigh*, Mr. Southwark, you're so mean.\x02",
    )

    CloseMessageWindow()

    label("loc_BE64")

    Jump("loc_BE72")

    label("loc_BE69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BE72")

    label("loc_BE72")

    TalkEnd(0xFE)
    Return()

    # Function_27_B512 end

    def Function_28_BE76(): pass

    label("Function_28_BE76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BF0B")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking of stepping outside,\x01",
            "that thing appeared from out of thin air...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What in the world\x01",
            "is going on!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_BF0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BF19")
    Jump("loc_C7C7")

    label("loc_BF19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BFA7")

    ChrTalk(
        0xFE,
        (
            "I-I don't really get it, but they\x01",
            "say a war will happen...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't bear this anxiety, but... \x01",
            "Ken, I'll protect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_BFA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C031")

    ChrTalk(
        0xFE,
        (
            "I've had a few days off, but\x01",
            "I resumed shopping today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, if we don't spend,\x01",
            "the economy won't move around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C0D8")

    ChrTalk(
        0xFE,
        (
            "I'm just as anxious at home and\x01",
            "can't calm down, so I came to the\x01",
            "department store today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shopping really does\x01",
            "wonders for one's mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C0D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C18B")

    ChrTalk(
        0xFE,
        (
            "A train accident. How unsettling. But I'm\x01",
            "glad service was restored so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because if trade routes closed down,\x01",
            "I wouldn't be able to shop like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1F1")

    ChrTalk(
        0xFE,
        (
            "Looks like there's an uproar over something.\x01",
            "Maybe I should head home early today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C1F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C2D3")

    ChrTalk(
        0xFE,
        (
            "My husband has had a scowl on his\x01",
            "face recently. It seems like he's\x01",
            "thinking about state independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well for now, I'll leave the complicated discussions\x01",
            "to my husband. I just want to enjoy shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C2D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C352")

    ChrTalk(
        0xFE,
        "My, they've added new goods, haven't they.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's par for the course\x01",
            "for Times department store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C3E7")

    ChrTalk(
        0xFE,
        "This is the day of the Trade Conference, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I can't attend it directly,\x01",
            "I can't help but be concerned over it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C4BC")

    ChrTalk(
        0xFE,
        "Listen, Ken.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as we go back, first we tell papa we're sorry.\x01",
            "Then, let's hug him without a moment of delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine, if we both sandwich him,\x01",
            "there won't be anything to fear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C4BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C5C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C541")

    ChrTalk(
        0xFE,
        "That inauguration ceremony earlier was amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm excited. I might buy\x01",
            "more than usual today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C5C3")

    label("loc_C541")


    ChrTalk(
        0xFE,
        (
            "It's right after payday, and that\x01",
            "money is burning a hole in my wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm going to take my time looking around today.\x02",
    )

    CloseMessageWindow()

    label("loc_C5C3")

    Jump("loc_C7C7")

    label("loc_C5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C664")

    ChrTalk(
        0xFE,
        (
            "I always think this, but people\x01",
            "who think about goods are amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're always thinking\x01",
            "about new features to\x01",
            "grab the customer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7C7")

    label("loc_C664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C74B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C707")

    ChrTalk(
        0xFE,
        (
            "Compared to when I was\x01",
            "shopping with him before, \x01",
            "Ken has fewer complaints lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This too is love. Mama is happy, you know?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C746")

    label("loc_C707")


    ChrTalk(
        0xFE,
        "It's he happiness of a mother who has a well behaved son.\x02",
    )

    CloseMessageWindow()

    label("loc_C746")

    Jump("loc_C7C7")

    label("loc_C74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C7C7")

    ChrTalk(
        0xFE,
        "Hm, hm-hmm♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter when I come here or for how long,\x01",
            "I never lose interest in this department store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C7")

    TalkEnd(0xFE)
    Return()

    # Function_28_BE76 end

    def Function_29_C7CB(): pass

    label("Function_29_C7CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C862")

    ChrTalk(
        0xFE,
        (
            "To think a tree grew right out of thin air...\x01",
            "What could be the theory behind such a thing?\x01",
            "Am I dreaming? Is it an illusion...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_C862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C870")
    Jump("loc_D2C2")

    label("loc_C870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C88B")

    ChrTalk(
        0xFE,
        "Mama...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_C88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C8E7")

    ChrTalk(
        0xFE,
        (
            "Mama is really tough.\x01",
            "I don't really get it, but\x01",
            "I am encouraged by her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_C8E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C974")

    ChrTalk(
        0xFE,
        (
            "Mama doesn't have her usual\x01",
            "carefree personality today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But thinking about Mainz,\x01",
            "I suppose that's understandable...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_C974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CA34")

    ChrTalk(
        0xFE,
        (
            "Mama's shopping passion doesn't\x01",
            "wear out because of some mere rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is still fine, but whenever I go\x01",
            "shopping with her in heavy rain,\x01",
            "I end up completely soaked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_CA34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_CB3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAD7")

    ChrTalk(
        0xFE,
        (
            "Those ambulance' sirens\x01",
            "are extremely loud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet they'd be even\x01",
            "more annoying close up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do the drivers\x01",
            "wear earplugs?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CB36")

    label("loc_CAD7")


    ChrTalk(
        0xFE,
        (
            "Those ambulance' sirens\x01",
            "are extremely loud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do the people driving\x01",
            "them use earplugs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB36")

    Jump("loc_D2C2")

    label("loc_CB3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CBDB")

    ChrTalk(
        0xFE,
        (
            "If everyone was as\x01",
            "thoughtless as my mama,\x01",
            "we'd all be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if we did that, we'd\x01",
            "be annexed by the Empire\x01",
            "in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_CBDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CD38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCBF")

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll kill time\x01",
            "today by people watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, the general store guy and the\x01",
            "information desk lady have been awfully close lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, could this be...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CD33")

    label("loc_CCBF")


    ChrTalk(
        0xFE,
        (
            "The general store guy and the information\x01",
            "desk lady have been awfully close lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, could this be...\x02",
    )

    CloseMessageWindow()

    label("loc_CD33")

    Jump("loc_D2C2")

    label("loc_CD38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CE38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDCE")

    ChrTalk(
        0xFE,
        (
            "My mama's "operation apology"\x01",
            "yesterday was a smashing success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That hug, and those tears...\x01",
            "Mama is incredible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CE33")

    label("loc_CDCE")


    ChrTalk(
        0xFE,
        (
            "Dad was totally taken in\x01",
            "by mama's hug and tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That might be a weakness\x01",
            "of men in love.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE33")

    Jump("loc_D2C2")

    label("loc_CE38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_CEB7")

    ChrTalk(
        0xFE,
        (
            "Because mama was absorbed into\x01",
            "her shopping, it's this late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that papa is\x01",
            "going to be angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_CEB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CFF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF7D")

    ChrTalk(
        0xFE,
        "That inauguration ceremony was spectacle itself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, my mama seems a\x01",
            "little down for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she doesn't buy\x01",
            "anything we don't need, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CFEE")

    label("loc_CF7D")


    ChrTalk(
        0xFE,
        (
            "My mama's eye color is\x01",
            "a little different today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she doesn't buy\x01",
            "anything we don't need, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFEE")

    Jump("loc_D2C2")

    label("loc_CFF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D0A6")

    ChrTalk(
        0xFE,
        (
            "I always think this, but people who\x01",
            "think about products have it tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have to think of new\x01",
            "things to pull in customers\x01",
            "like my mama, day after day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_D0A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D1CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D166")

    ChrTalk(
        0xFE,
        (
            "I devised a way of killing time\x01",
            "I like to call people watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since all different kind of people come to this\x01",
            "department store, I never get tired of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_D1C6")

    label("loc_D166")


    ChrTalk(
        0xFE,
        (
            "Since all different kind of people come to this\x01",
            "department store, I never get tired of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1C6")

    Jump("loc_D2C2")

    label("loc_D1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D2C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D250")

    ChrTalk(
        0xFE,
        (
            "A redhead who looked\x01",
            "like he was on vacation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like he\x01",
            "went up to the\x01",
            "roof just now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2C2")

    label("loc_D250")


    ChrTalk(
        0xFE,
        (
            "Going window shopping with\x01",
            "my mama is my daily routine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm used to it, but it's the height of boredom.\x02",
    )

    CloseMessageWindow()

    label("loc_D2C2")

    TalkEnd(0xFE)
    Return()

    # Function_29_C7CB end

    def Function_30_D2C6(): pass

    label("Function_30_D2C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D399")

    ChrTalk(
        0xFE,
        (
            "A gigantic floating tree that suddenly\x01",
            "appeared in mid-air, is it? Personally,\x01",
            "I don't see the problem, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'd like that\x01",
            "unsightly thing to hurry\x01",
            "up and disappear already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D3A7")
    Jump("loc_DD79")

    label("loc_D3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D3E0")

    ChrTalk(
        0xFE,
        (
            "Hmmm... This is an\x01",
            "unusual situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D4CD")

    ChrTalk(
        0xFE,
        (
            "Now, the question of whether we should\x01",
            "abandon independence and believe in the two\x01",
            "major powers is a different question entirely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Either way, the military threat from each\x01",
            "of them is a  problem we can't ignore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D5D3")

    ChrTalk(
        0xFE,
        (
            "Hmm. If we were to declare independence, then\x01",
            "whether we have a military that can stand up\x01",
            "to those nations would be the problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, the Empire's Railway\x01",
            "Cannons... Would we capitulate after\x01",
            "taking just a single shot from them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D5D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D65A")

    ChrTalk(
        0xFE,
        "I heard about an ogre-like monster, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the first time I've heard\x01",
            "such a mysterious tale in my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D6A6")

    ChrTalk(
        0xFE,
        (
            "It's noisy outside. I wonder\x01",
            "just what exactly happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D746")

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm thinking about\x01",
            "my next gift to my old woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've given her a brooch before... \x01",
            "I was thinking of going with a ring this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D7ED")

    ChrTalk(
        0xFE,
        (
            "I didn't think I'd hear the word \x01",
            ""independence" at my age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be great if it were possible,\x01",
            "but I don't think it'll go that smoothly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D8A7")

    ChrTalk(
        0xFE,
        (
            "Hmm, the problems at the conference are\x01",
            "going to be Osborne and Rocksmith...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of plan the mayor has\x01",
            "for dealing with the audacity of those men.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_D909")

    ChrTalk(
        0xFE,
        "Well then, time to go back home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd be no match for my angered old lady.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D9C9")

    ChrTalk(
        0xFE,
        (
            "Hoh hoh, the roof of this place is the\x01",
            "best spot from which to see the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't forget the fire its magnificent form\x01",
            "lit in my eyes the moment that curtain fell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_D9C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DB2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA89")

    ChrTalk(
        0xFE,
        (
            "The Trade Conference\x01",
            "finally opens tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was shocked when\x01",
            "Mayor Crois first\x01",
            "proposed it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe it's\x01",
            "actually going to be held.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DB27")

    label("loc_DA89")


    ChrTalk(
        0xFE,
        (
            "I can't believe the Trade Conference\x01",
            "is actually going to be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was probably able to do it because he's\x01",
            "both the IBC President and the mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB27")

    Jump("loc_DD79")

    label("loc_DB2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DBC9")

    ChrTalk(
        0xFE,
        (
            "Hmm. I'm always impressed whenever\x01",
            "I see this store's lineup of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder which I should choose\x01",
            "as a present for my old woman.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD79")

    label("loc_DBC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DD79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE4")

    ChrTalk(
        0xFE,
        (
            "Hmm, but even so I'm amazed\x01",
            "at Mayor Crois' and Chairman\x01",
            "MacDowell's actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially the Chairman. He's almost my age\x01",
            "and yet he could achieve all that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh hoh, this must be what it means to be \x01",
            "old in age but young in body and mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DD79")

    label("loc_DCE4")


    ChrTalk(
        0xFE,
        (
            "Hoh hoh, this must be what it means to be \x01",
            "old in age but young in body and mind, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chairman MacDowell is the\x01",
            "star of my old generation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD79")

    TalkEnd(0xFE)
    Return()

    # Function_30_D2C6 end

    def Function_31_DD7D(): pass

    label("Function_31_DD7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DD8E")
    Jump("loc_DFAA")

    label("loc_DD8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DE27")

    ChrTalk(
        0xFE,
        (
            "Martial law was declared,\x01",
            "but I didn't think this\x01",
            "situation would ever happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... Honestly,\x01",
            "I really should've gone home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFAA")

    label("loc_DE27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DECD")

    ChrTalk(
        0xFE,
        (
            "I'm told that we won't pay taxes to the Empire\x01",
            "or Republic if we declare independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, if Mr. Dieter says it,\x01",
            "can it really be wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFAA")

    label("loc_DECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DF27")

    ChrTalk(
        0xFE,
        (
            "A service for rainy days?\x01",
            "This department store sure is sophisticated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFAA")

    label("loc_DF27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DFAA")

    ChrTalk(
        0xFE,
        (
            "Homework?\x01",
            "I don't have time for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way... It seems Mr. Arios\x01",
            "is on a business trip again, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFAA")

    TalkEnd(0xFE)
    Return()

    # Function_31_DD7D end

    def Function_32_DFAE(): pass

    label("Function_32_DFAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DFBF")
    Jump("loc_E146")

    label("loc_DFBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E04A")

    ChrTalk(
        0xFE,
        (
            "But, the situation being what it is,\x01",
            "it'll be the same wherever we go, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm lonely without my family, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E146")

    label("loc_E04A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E0C7")

    ChrTalk(
        0xFE,
        (
            "Lately, all the adults are shouting\x01",
            ""independence, independence", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What do they mean, exactly?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E146")

    label("loc_E0C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E146")

    ChrTalk(
        0xFE,
        (
            "Or rather, that guy's\x01",
            "the manager, isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a man, receiving us on purpose...\x01",
            "That's kind of amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E146")

    TalkEnd(0xFE)
    Return()

    # Function_32_DFAE end

    def Function_33_E14A(): pass

    label("Function_33_E14A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E15F")
    Call(0, 36)
    Jump("loc_E1E4")

    label("loc_E15F")


    ChrTalk(
        0xFE,
        (
            "Hmm? Oh, you guys, the police's\x01",
            "What's-It-Called Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, get out of here.\x01",
            "Don't talk to us like you know us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1E4")

    TalkEnd(0xFE)
    Return()

    # Function_33_E14A end

    def Function_34_E1E8(): pass

    label("Function_34_E1E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1FD")
    Call(0, 36)
    Jump("loc_E296")

    label("loc_E1FD")


    ChrTalk(
        0xFE,
        (
            "Aww, man. We're on a trip and all, so\x01",
            "I wanted something a little more exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, should we try going to\x01",
            "that shady store on Back Street?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E296")

    TalkEnd(0xFE)
    Return()

    # Function_34_E1E8 end

    def Function_35_E29A(): pass

    label("Function_35_E29A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2AF")
    Call(0, 36)
    Jump("loc_E333")

    label("loc_E2AF")


    ChrTalk(
        0xFE,
        (
            "Hey, listen, let's go to the\x01",
            "orbal store later too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we're here, I want to tune up \x01",
            "the car as much as possible too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E333")

    TalkEnd(0xFE)
    Return()

    # Function_35_E29A end

    def Function_36_E337(): pass

    label("Function_36_E337")

    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)

    ChrTalk(
        0x17,
        (
            "Man... For a trade\x01",
            "city, this department\x01",
            "store's no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Yeah, they have\x01",
            "hardly anything that\x01",
            "matches my glasses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, they have a lot of\x01",
            "goods for commoners.\x01",
            "What did you expect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Let's just buy some "nibbles"\x01",
            "to go with drinks today too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E471")
    Jump("loc_E528")

    label("loc_E471")


    ChrTalk(
        0x104,
        (
            "#00301F(Oh, so these guys are the\x01",
            "rumored cheeky kiddos, huh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Honestly, they even hang\x01",
            "out here, do they...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(...Well, let's leave them alone for now.)\x02",
    )

    CloseMessageWindow()

    label("loc_E528")

    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_36_E337 end

    def Function_37_E53D(): pass

    label("Function_37_E53D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E5AA")

    ChrTalk(
        0xFE,
        (
            "I ran out of pastries\x01",
            "at home so I rushed\x01",
            "here to buy some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm such a birdbrain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E628")

    label("loc_E5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E628")

    ChrTalk(
        0xFE,
        (
            "I've got to stock up on\x01",
            "pastries while I have the time㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be a problem if I ran\x01",
            "out at the wrong time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E628")

    TalkEnd(0xFE)
    Return()

    # Function_37_E53D end

    def Function_38_E62C(): pass

    label("Function_38_E62C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E706")

    ChrTalk(
        0xFE,
        (
            "That stupidly large tree aside, freedom\x01",
            "sure is a good thing. Feeling cramped\x01",
            "under martial law can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. This is a good\x01",
            "chance, so I'll bring some\x01",
            "refreshments to sister Xilun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_E706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E714")
    Jump("loc_F191")

    label("loc_E714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E7D4")

    ChrTalk(
        0xFE,
        (
            "Mysterious accidents, huh?\x01",
            "I did get the feeling they\x01",
            "were those type of accidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We also bear the sin for\x01",
            "having overlooked them...\x01",
            "It's just as the President said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_E7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E883")

    ChrTalk(
        0xFE,
        (
            "Although it's a matter of course...\x01",
            "St. Ursula Hospital looks very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sister Xilun seems calm,\x01",
            "but I feel worthless, not\x01",
            "being able to do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_E883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E9E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E951")

    ChrTalk(
        0xFE,
        "W-What's with the attack on Mainz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard CGF were carried\x01",
            "one-by-one to the hospital\x01",
            "yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, why do guys who do\x01",
            "such stupid things have to exist?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_E9DC")

    label("loc_E951")


    ChrTalk(
        0xFE,
        (
            "I heard CGF were carried\x01",
            "one-by-one to the hospital\x01",
            "yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, why do guys who do\x01",
            "such stupid things have to exist?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9DC")

    Jump("loc_F191")

    label("loc_E9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EAB7")

    ChrTalk(
        0xFE,
        (
            "Some of the train accident victims\x01",
            "were severely wounded, but...\x01",
            "It seems everyone survived it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard all the doctors worked\x01",
            "through the night treating them.\x01",
            "They're truly model citizens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_EAB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EB01")

    ChrTalk(
        0xFE,
        (
            "W-What? An ambulance...?\x01",
            "And quite a lot of them, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_EB01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_EB9A")

    ChrTalk(
        0xFE,
        "Hmm, now what does my family want today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. At my age, I want to\x01",
            "support my family however I can,\x01",
            "even if it's just shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_EB9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_ED9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECF5")

    ChrTalk(
        0xFE,
        (
            "Sister Xilun suggested I become\x01",
            "a male nurse. I'll have to\x01",
            "think seriously about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I have to wait for\x01",
            "next year's exam, I already\x01",
            "did well on a practice one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, I'm planning on taking\x01",
            "next year's medical intern exams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It makes me feel at easy when I\x01",
            "think there's not just one path.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_ED99")

    label("loc_ECF5")


    ChrTalk(
        0xFE,
        (
            "Unless they do their best to be positive,\x01",
            "humans can't master what they could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Studying is somehow more fun than it\x01",
            "was before. ...Just a little, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED99")

    Jump("loc_F191")

    label("loc_ED9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_EDAC")
    Jump("loc_F191")

    label("loc_EDAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_EDBA")
    Jump("loc_F191")

    label("loc_EDBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EE96")

    ChrTalk(
        0xFE,
        (
            "Everyone is happy due to the\x01",
            "inauguration ceremony, but...\x01",
            "My heart is down in the dumps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On that point, I'm jealous of sister \x01",
            "Xilun's carefree personality. \x01",
            "I can't really think we're siblings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_EE96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EF5F")

    ChrTalk(
        0xFE,
        "Studying again another year to prepare for exams, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow, lately the stares of my family\x01",
            "have been getting colder and colder...\x01",
            "*haah*, what am I going to do with my life?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_EF5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F041")

    ChrTalk(
        0xFE,
        (
            "Hmm, for today's shopping, \x01",
            "I need black pepper, mustard\x01",
            "sauce and olive oil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, I can't remember what I'm supposed\x01",
            "to get without a list! I want to try doing this\x01",
            "as a way to improve my memory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F191")

    label("loc_F041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F120")

    ChrTalk(
        0xFE,
        (
            "I failed the St. Ursula Medical College\x01",
            "entrance exam again this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know what they say... 3rd time's the\x01",
            "charm... But it turned out just like I\x01",
            "thought. I'm not cut out for this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F191")

    label("loc_F120")


    ChrTalk(
        0xFE,
        (
            "And now my worthless self is just\x01",
            "the dinner ingredients gofer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*, I'm no good. No good at all.\x02",
    )

    CloseMessageWindow()

    label("loc_F191")

    TalkEnd(0xFE)
    Return()

    # Function_38_E62C end

    def Function_39_F195(): pass

    label("Function_39_F195")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F274")

    ChrTalk(
        0xFE,
        (
            "I really want a large\x01",
            "Michey doll, but they\x01",
            "sure are expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I pool my spending money and go for\x01",
            "the large one, or should I go for the convenient\x01",
            "small one right now... Hmm, what to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2F4")

    label("loc_F274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F2F4")

    ChrTalk(
        0xFE,
        (
            "Wow, so they really do have a Michey\x01",
            "corner at the general goods store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I-I can't let this opportunity pass.\x02",
    )

    CloseMessageWindow()

    label("loc_F2F4")

    TalkEnd(0xFE)
    Return()

    # Function_39_F195 end

    def Function_40_F2F8(): pass

    label("Function_40_F2F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F382")

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll buy a souvenir\x01",
            "and then head for the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, but this was a\x01",
            "very productive trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4B5")

    label("loc_F382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_F390")
    Jump("loc_F4B5")

    label("loc_F390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F403")

    ChrTalk(
        0xFE,
        (
            "Man, the inauguration ceremony\x01",
            "was more amazing than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's Crossbell for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4B5")

    label("loc_F403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F4B5")

    ChrTalk(
        0xFE,
        (
            "Man, as expected, Crossbell\x01",
            "is such a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow is the Orchis Tower inauguration\x01",
            "ceremony. This trip looks like it's going to\x01",
            "be a lot of fun, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4B5")

    TalkEnd(0xFE)
    Return()

    # Function_40_F2F8 end

    def Function_41_F4B9(): pass

    label("Function_41_F4B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F515")

    ChrTalk(
        0xFE,
        (
            "Aww, why'd this trip\x01",
            "have to end? It was over\x01",
            "in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F631")

    label("loc_F515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_F523")
    Jump("loc_F631")

    label("loc_F523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F5BA")

    ChrTalk(
        0xFE,
        (
            "I saw the inauguration ceremony from this\x01",
            "store's roof. It was a really good spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'm glad I\x01",
            "researched it beforehand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F631")

    label("loc_F5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F631")

    ChrTalk(
        0xFE,
        (
            "Crossbell is a very\x01",
            "exciting place to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No matter how many times I come, I never get tired of it.\x02",
    )

    CloseMessageWindow()

    label("loc_F631")

    TalkEnd(0xFE)
    Return()

    # Function_41_F4B9 end

    def Function_42_F635(): pass

    label("Function_42_F635")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F70D")

    ChrTalk(
        0xFE,
        (
            "Hmm, Manager Neston's\x01",
            "words are pregnant for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am still inexperienced as both\x01",
            "a businessman and a trader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I want to do\x01",
            "all I can for Crossbell,\x01",
            "given my position.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_F798")

    label("loc_F70D")


    ChrTalk(
        0xFE,
        (
            "I am still inexperienced as both\x01",
            "a businessman and a trader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, I want to do\x01",
            "all I can for Crossbell,\x01",
            "given my position.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F798")

    TalkEnd(0xFE)
    Return()

    # Function_42_F635 end

    def Function_43_F79C(): pass

    label("Function_43_F79C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I want to buy a few things\x01",
            "for tonight's dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's noisy outside... \x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_F79C end

    def Function_44_F80D(): pass

    label("Function_44_F80D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F8DD")

    ChrTalk(
        0xFE,
        (
            "I'm told there's a high chance terrorists will\x01",
            "attack the Trade Conference's main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, man oh man... If they\x01",
            "really do attack, I wonder if\x01",
            "we'll be able to handle them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF25")

    label("loc_F8DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F9FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F992")

    ChrTalk(
        0xFE,
        (
            "*sigh*, there's a huge\x01",
            "crowd today, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm too busy to count the\x01",
            "number of beautiful women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm, same old Mr.\x01",
            "Raymond, I guess.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_F9FA")

    label("loc_F992")


    ChrTalk(
        0xFE,
        (
            "*sigh*, there's a huge\x01",
            "crowd today, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm too busy to count the\x01",
            "number of beautiful women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9FA")

    Jump("loc_FF25")

    label("loc_F9FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB77")

    ChrTalk(
        0xFE,
        (
            "Oh, you there... Could\x01",
            "you be lost and looking\x01",
            "for your parents?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "...Who's lost, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I'm touring\x01",
            "Crossbell right now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A2, 500)

    ChrTalk(
        0xFE,
        "Wow, touring Crossbell?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "That's a support request too, I guess.\x01",
            "The Support Section's work sounds tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, it's not that bad.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_FBF5")

    label("loc_FB77")


    ChrTalk(
        0xFE,
        (
            "Anyway, this is the first day the\x01",
            "security structure's in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't fly off the\x01",
            "rails. Everything\x01",
            "in moderation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBF5")

    Jump("loc_FF25")

    label("loc_FBFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE00")

    ChrTalk(
        0xFE,
        (
            "Ah, you guys. We sure\x01",
            "have it tough, don't we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt's not that bad. We're\x01",
            "managing, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FDoes your being here mean you're\x01",
            "in charge of the department store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Strictly speaking, it's the Central Square\x01",
            "commerce facilities I'm responsible for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a lot of pretty ladies here,\x01",
            "so I'm managing to stay alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Hmm, what an\x01",
            "impure motive.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F(Ha ha, well I think it's\x01",
            "fine as long as he's\x01",
            "staying alert somehow.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_FF25")

    label("loc_FE00")


    ChrTalk(
        0xFE,
        (
            "Guard duty gives you stiff shoulders. When I see a\x01",
            "pretty lady though, my fatigue just flies away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up until now there's been 31 pretty ladies...\x01",
            "I think I can still expect a few more.\x02",
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

    label("loc_FF25")

    TalkEnd(0xFE)
    Return()

    # Function_44_F80D end

    def Function_45_FF29(): pass

    label("Function_45_FF29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF3E")
    Call(0, 46)
    Jump("loc_FF9B")

    label("loc_FF3E")


    ChrTalk(
        0x21,
        (
            "#00603FI'm going to try on\x01",
            "these shoes I ordered.\x02\x03",
            "#00600FStay out of my way, will you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF9B")

    TalkEnd(0xFE)
    Return()

    # Function_45_FF29 end

    def Function_46_FF9F(): pass

    label("Function_46_FF9F")

    EventBegin(0x0)
    Fade(500)
    OP_68(-90, 8900, 27440, 0)
    MoveCamera(70, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17690, 0)
    SetChrPos(0x101, -1280, 8029, 26410, 74)
    SetChrPos(0x102, -1420, 8029, 27490, 74)
    SetChrPos(0x103, -2650, 8000, 26650, 74)
    SetChrPos(0x104, -2690, 8000, 27740, 74)
    SetChrPos(0x109, -3700, 8000, 27000, 74)
    SetChrPos(0x105, -3320, 8000, 25680, 74)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0x21, 0x13B, 0x0)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x14, 0x0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Mr. Dudley, these are\x01",
            "the shoes you ordered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#11P#00602FHmm, then allow me to try them on immediately...\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    ChrTalk(
        0x21,
        (
            "#11P#00600FMrr, guys. What're\x01",
            "you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FIf I had to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FWe should be askin'\x01",
            "you that question.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#12P#10305FHmm, those look\x01",
            "expensive, don't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FShoes, right? Where is\x01",
            "the brand name though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00603FHmph, don't lump me\x01",
            "in with people who\x01",
            "care about brands.\x02\x03",
            "#00602F...These are order-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FWow, you're picky,\x01",
            "aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FOrder-made shoes, huh...\x02\x03",
            "#00003FI wear basically\x01",
            "only sneakers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "#11P#00601F...Bannings. What're\x01",
            "you trying to say?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00600FIt's almost like you're trying\x01",
            "to say leather shoes are worthless.\x02\x03",
            "#00603FBut... \x01",
            "That's where you're wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FI-I don't really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00602FShoe leather is a deep\x01",
            "and complicated subject.\x02\x03",
            "#00604FThey feel friendlier when wearing them\x01",
            "and if you maintain them properly, the\x01",
            "texture feels like it has way more depth...\x02\x03",
            "#00601FAre you saying sneakers can\x01",
            "deliver that kind of pleasure?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00206FI feel like things have heated up for some reason...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109FI agree. I didn't expect this at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00606F*a-ahem*... It seems\x01",
            "we've gotten off track.\x02\x03",
            "#00600FAnyway, I'm here because I just\x01",
            "happened to have some free time.\x02\x03",
            "I have another appointment after this,\x01",
            "of course. Stay out of my way, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FU-Understood...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0xA, 0xFF)
    OP_4C(0x21, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0x21, 0x13B, 0x0)
    SetScenarioFlags(0x171, 4)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 13800, 8000, 6200, 225)
    BeginChrThread(0x14, 0, 0, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1700, 8029, 27020, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_46_FF9F end

    def Function_47_107A0(): pass

    label("Function_47_107A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10828")

    ChrTalk(
        0x1B,
        (
            "#02106FYeah, yeah, I know already.\x02\x03",
            "#02109FAnyway, I can't do without\x01",
            "this manufacturer's pen\x01",
            "they have here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_1089F")

    label("loc_10828")


    ChrTalk(
        0x1B,
        (
            "#02105FWow, Reinford has strengthened\x01",
            "their lineup with these new models.\x02\x03",
            "#02109FHmm, should I try\x01",
            "this one out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1089F")

    TalkEnd(0xFE)
    Return()

    # Function_47_107A0 end

    def Function_48_108A3(): pass

    label("Function_48_108A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_109B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10912")

    ChrTalk(
        0xFE,
        (
            "Senior Grace!\x01",
            "Please hurry and finish!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why are you\x01",
            "going so slow!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x2, 0)
    Jump("loc_109B1")

    label("loc_10912")


    ChrTalk(
        0xFE,
        (
            "*sigh*, you said we were going shopping\x01",
            "because you suddenly ran out of ink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got still time left, but for\x01",
            "some kind of reason I'm worried...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109B1")

    Jump("loc_10AB5")

    label("loc_109B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A62")

    ChrTalk(
        0xFE,
        (
            "Umm, restoratives, antidotes...\x01",
            "I also need smelling salts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Looks like he's preparing a medkit... \x01",
            "Where could he be going?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_10AB5")

    label("loc_10A62")


    ChrTalk(
        0xFE,
        (
            "EP Charges... \x01",
            "Do I need those too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just the Smoke Balls\x01",
            "to go, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AB5")

    TalkEnd(0xFE)
    Return()

    # Function_48_108A3 end

    def Function_49_10AB9(): pass

    label("Function_49_10AB9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F Boutique "Lucca"\x01",
            "2F Hanson Shoes\x01",
            "2F Accessory "Baker"\x01",
            "1F "Region Food"\x01",
            "1F General Corner "Southwark"\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※If you have any questions,\x01",
            "please enquire freely at the\x01",
            "front office information.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_49_10AB9 end

    def Function_50_10BAB(): pass

    label("Function_50_10BAB")

    EventBegin(0x0)
    Fade(500)
    OP_68(-15210, 1000, 9790, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10C32")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x104, -14350, 0, 8000, 0)
    Jump("loc_10CD1")

    label("loc_10C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10C84")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x109, -14350, 0, 8000, 0)
    Jump("loc_10CD1")

    label("loc_10C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10CD1")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x105, -14350, 0, 8000, 0)

    label("loc_10CD1")

    OP_0D()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PC-Could these be\x01",
            ""Michey Dolls"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PWhy? This isn't\x01",
            "the theme park...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, this is a recently created\x01",
            "exclusive goods corner, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FDo you like\x01",
            "Michey, Shing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Y-You... Are you\x01",
            "making fun of me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "How could one burdened with the future \x01",
            "of Heiyue be interested in such a thing...\x01",
            "There's a limit to how much rude you can be!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10FA6")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_10EEA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10EEA)
    Sleep(50)

    def lambda_10EFA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10EFA)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FS-Shing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FYou don't have to take it so seriously...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FYeah, and it doesn't have\x01",
            "anything to do with the Heiyue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111CE")

    label("loc_10FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_110BA")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_10FFF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10FFF)
    Sleep(50)

    def lambda_1100F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1100F)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FS-Shing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FYou don't have to take it so seriously...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FYes, and it doesn't have\x01",
            "anything to do with the Heiyue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111CE")

    label("loc_110BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_111CE")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_11113():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11113)
    Sleep(50)

    def lambda_11123():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11123)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FS-Shing...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FYou don't have to take it so seriously...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FYeah, and it doesn't have\x01",
            "anything to do with the Heiyue, no?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111CE")

    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Hmph, anyway―\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PWhat's this? A Times\x01",
            "department store exclusive,\x01",
            ""Tick-Tock Michey"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        "#12P―Hah!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "A-Anyway, such a thing\x01",
            "is nice as kid's stuff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "And I'm not interested\x01",
            "in it or anything, at all!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1135D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1140A")

    label("loc_1135D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_113B6")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_1140A")

    label("loc_113B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1140A")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_1140A")


    ChrTalk(
        0x101,
        "#12P#00012F(H-He's easy to understand...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F(Yes, it's as if he's saying\x01",
            "he really is interested.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 7)
    OP_65(0x9, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15080, 0, 8820, 0)
    EventEnd(0x5)
    Return()

    # Function_50_10BAB end

    def Function_51_114AD(): pass

    label("Function_51_114AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-960, 3000, 1530, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11539")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x104, 600, 0, 2900, 180)
    Jump("loc_115D8")

    label("loc_11539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1158B")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x109, 600, 0, 2900, 180)
    Jump("loc_115D8")

    label("loc_1158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_115D8")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x105, 600, 0, 2900, 180)

    label("loc_115D8")

    OP_68(-960, 1600, 1530, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow then, we'll head to the\x01",
            "shops, then to the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PYeah! Lead the way!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x154, 3)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 2900, 0)
    OP_1B(0x0, 0x0, 0x35)
    OP_66(0x9, 0x1)
    EventEnd(0x5)
    Return()

    # Function_51_114AD end

    def Function_52_11682(): pass

    label("Function_52_11682")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17440, 1600, 19460, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1170F")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x104, -15690, 30, 21350, 270)
    Jump("loc_117AE")

    label("loc_1170F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11761")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x109, -15690, 30, 21350, 270)
    Jump("loc_117AE")

    label("loc_11761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_117AE")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x105, -15690, 30, 21350, 270)

    label("loc_117AE")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A2,
        (
            "#12PHey, you've been whispering\x01",
            "stuff for awhile now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah. Actually, this is for you.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11843")

    def lambda_11831():

        label("loc_11831")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_11831")

    QueueWorkItem2(0x104, 1, lambda_11831)
    Jump("loc_1187E")

    label("loc_11843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11863")

    def lambda_11851():

        label("loc_11851")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_11851")

    QueueWorkItem2(0x109, 1, lambda_11851)
    Jump("loc_1187E")

    label("loc_11863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1187E")

    def lambda_11871():

        label("loc_11871")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_11871")

    QueueWorkItem2(0x105, 1, lambda_11871)

    label("loc_1187E")

    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_118BC")
    EndChrThread(0x104, 0x1)

    def lambda_1189F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1189F)
    Sleep(50)

    def lambda_118AF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_118AF)
    Jump("loc_11915")

    label("loc_118BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_118EB")
    EndChrThread(0x109, 0x1)

    def lambda_118CE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_118CE)
    Sleep(50)

    def lambda_118DE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_118DE)
    Jump("loc_11915")

    label("loc_118EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11915")
    EndChrThread(0x105, 0x1)

    def lambda_118FD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_118FD)
    Sleep(50)

    def lambda_1190D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1190D)

    label("loc_11915")

    Sleep(300)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave the "Tick-Tock\x01",
            "Michey" to Shing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x5DC, 0x0)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#12PThis is... This store's limited edition...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI see, so that's what you were doing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11A25")

    ChrTalk(
        0x104,
        "#11P#00309FWow, how considerate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11A9B")

    label("loc_11A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11A6A")

    ChrTalk(
        0x109,
        "#11P#10109FUh uh, you're considerate, aren't you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11A9B")

    label("loc_11A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11A9B")

    ChrTalk(
        0x105,
        "#11P#10302FHu hu, how considerate.\x02",
    )

    CloseMessageWindow()

    label("loc_11A9B")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "#12PW-What's with this? What are\x01",
            "you doing giving this to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, this is what\x01",
            "you call a present.\x02\x03",
            "Why not accept it? It'll help\x01",
            "you remember today's tour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PSomething to remember today by...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)
    OP_93(0x1A2, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12P...Now that you've bought it,\x01",
            "it's not like I can throw it away. \x01",
            "In that case, I'll take it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PHowever, let me just say this.\x01",
            "I have absolutely no interest\x01",
            "in dolls like this, you hear!?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11CDF")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_11D8C")

    label("loc_11CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11D38")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_11D8C")

    label("loc_11D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11D8C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_11D8C")


    ChrTalk(
        0x101,
        "#00000FY-Yeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C6, 0)
    OP_29(0x73, 0x1, 0xC)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15900, 0, 20830, 180)
    EventEnd(0x5)
    Return()

    # Function_52_11682 end

    def Function_53_11DDB(): pass

    label("Function_53_11DDB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FI don't have time to show him around outside.\x02\x03",
            "We'll head to the shops, then\x01",
            "we'll take him up on the roof.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -600, 30, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_53_11DDB end

    SaveToFile()

Try(main)
