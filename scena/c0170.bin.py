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
        "Function_5_DD2",          # 05, 5
        "Function_6_DD6",          # 06, 6
        "Function_7_1C5F",         # 07, 7
        "Function_8_1C63",         # 08, 8
        "Function_9_2658",         # 09, 9
        "Function_10_284B",        # 0A, 10
        "Function_11_29C4",        # 0B, 11
        "Function_12_29E3",        # 0C, 12
        "Function_13_3BBC",        # 0D, 13
        "Function_14_3BC3",        # 0E, 14
        "Function_15_501E",        # 0F, 15
        "Function_16_5022",        # 10, 16
        "Function_17_6093",        # 11, 17
        "Function_18_6097",        # 12, 18
        "Function_19_701E",        # 13, 19
        "Function_20_7025",        # 14, 20
        "Function_21_8B20",        # 15, 21
        "Function_22_8C81",        # 16, 22
        "Function_23_A229",        # 17, 23
        "Function_24_A65F",        # 18, 24
        "Function_25_AA23",        # 19, 25
        "Function_26_AC74",        # 1A, 26
        "Function_27_B03F",        # 1B, 27
        "Function_28_B966",        # 1C, 28
        "Function_29_C2A9",        # 1D, 29
        "Function_30_CD88",        # 1E, 30
        "Function_31_D7E5",        # 1F, 31
        "Function_32_DA0E",        # 20, 32
        "Function_33_DB8C",        # 21, 33
        "Function_34_DC29",        # 22, 34
        "Function_35_DCE2",        # 23, 35
        "Function_36_DD6C",        # 24, 36
        "Function_37_DF47",        # 25, 37
        "Function_38_E030",        # 26, 38
        "Function_39_EB83",        # 27, 39
        "Function_40_ECED",        # 28, 40
        "Function_41_EE9A",        # 29, 41
        "Function_42_F012",        # 2A, 42
        "Function_43_F17B",        # 2B, 43
        "Function_44_F1EB",        # 2C, 44
        "Function_45_F916",        # 2D, 45
        "Function_46_F990",        # 2E, 46
        "Function_47_10181",       # 2F, 47
        "Function_48_10283",       # 30, 48
        "Function_49_10489",       # 31, 49
        "Function_50_1057E",       # 32, 50
        "Function_51_10DDC",       # 33, 51
        "Function_52_10FB1",       # 34, 52
        "Function_53_116FC",       # 35, 53
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
            "The Bell Berry Juice\x01",
            "recipe is written here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_DCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Bell Berry\x01",
            "Juice"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_DCE")

    TalkEnd(0xFF)
    Return()

    # Function_4_C9C end

    def Function_5_DD2(): pass

    label("Function_5_DD2")

    Call(0, 6)
    Return()

    # Function_5_DD2 end

    def Function_6_DD6(): pass

    label("Function_6_DD6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E76")

    ChrTalk(
        0x8,
        (
            "Scott came in here a\x01",
            "little while ago, and he\x01",
            "seems fine for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's working so hard for\x01",
            "us... It makes me want\x01",
            "to do my best too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5B")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E91")
    Call(0, 23)
    Jump("loc_FD9")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")

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
    Jump("loc_FD9")

    label("loc_F85")


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
            "I'm glad Scott is safe,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD9")

    Jump("loc_1C5B")

    label("loc_FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F1")

    ChrTalk(
        0x8,
        (
            "On account of tomorrow's\x01",
            "referendum, Cynthia returned to\x01",
            "her home state of Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although I don't think\x01",
            "Cynthia was anticipating\x01",
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
    Jump("loc_11C6")

    label("loc_10F1")


    ChrTalk(
        0x8,
        (
            "Cynthia promised to\x01",
            "return to this\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm worried about a lot of things, but... Anyway, I\x01",
            "believe the day will come when I can do this with\x01",
            "her again, and I'll do my very best until then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C6")

    Jump("loc_1C5B")

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1292")

    ChrTalk(
        0x8,
        (
            "Cynthia is participating\x01",
            "in the charity event in\x01",
            "Governmental District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, I hear she's participating\x01",
            "in the pageant. I'll have her\x01",
            "show me the photos later.♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12F1")

    label("loc_1292")


    ChrTalk(
        0x8,
        (
            "I heard Cynthia's participating\x01",
            "in the pageant. I'll have her\x01",
            "show me the photos later.♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F1")

    Jump("loc_1C5B")

    label("loc_12F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(
        0x8,
        (
            "To think the mining\x01",
            "town's occupied...\x02",
        )
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
    Jump("loc_1C5B")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1448")

    ChrTalk(
        0x8,
        (
            "Scott is busy working again and\x01",
            "he told me he doesn't think\x01",
            "he'll be able to contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's shockingly calm. He\x01",
            "isn't a bracer for\x01",
            "nothing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14BD")

    label("loc_1448")


    ChrTalk(
        0x8,
        (
            "I guess there's no need\x01",
            "to worry about him,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want him to be careful\x01",
            "not to get too hurt out\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BD")

    Jump("loc_1C5B")

    label("loc_14C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1520")

    ChrTalk(
        0x8,
        (
            "They said it was a train\x01",
            "derailment... Is that train\x01",
            "trouble or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5B")

    label("loc_1520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15A2")

    ChrTalk(
        0x8,
        (
            "It seems like Scott has\x01",
            "been even busier than\x01",
            "usual lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Good luck, Scott. I'm\x01",
            "always rooting for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5B")

    label("loc_15A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BD")
    Call(0, 10)
    Jump("loc_164C")

    label("loc_15BD")


    ChrTalk(
        0x8,
        (
            "Ah, you're the Special\x01",
            "Support Section that's\x01",
            "always coming here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you for coming\x01",
            "today. Please, take your\x01",
            "time looking around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164C")

    Jump("loc_1C5B")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_178F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1744")

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
            "While were talking, all\x01",
            "three of them were totally\x01",
            "focused on Cynthia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jeanetta is feeling down\x01",
            "today. I wonder if\x01",
            "she'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_178A")

    label("loc_1744")


    ChrTalk(
        0x8,
        (
            "Jeanetta is feeling down\x01",
            "today. I wonder if\x01",
            "she'll be all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178A")

    Jump("loc_1C5B")

    label("loc_178F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_18AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1850")

    ChrTalk(
        0x8,
        (
            "After we finish work today,\x01",
            "I'm going out to eat with\x01",
            "Cynthia and Jeanetta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party\x01",
            "in a long time... Haha, I'm\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18A5")

    label("loc_1850")


    ChrTalk(
        0x8,
        (
            "I haven't had a dinner party\x01",
            "in a long time... Haha, I'm\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A5")

    Jump("loc_1C5B")

    label("loc_18AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C5")
    Call(0, 9)
    Jump("loc_194F")

    label("loc_18C5")


    ChrTalk(
        0x8,
        (
            "I always knew she was a fan,\x01",
            "but I didn't know Cynthia\x01",
            "loved Julia that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I want to know\x01",
            "more about that side of\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194F")

    Jump("loc_1C5B")

    label("loc_1954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A54")

    ChrTalk(
        0x8,
        (
            "I wonder what Scott's\x01",
            "doing around now. With\x01",
            "that job of his...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Ah, sorry! I said\x01",
            "something at work I\x01",
            "shouldn't have.\x02",
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
    Jump("loc_1AA4")

    label("loc_1A54")


    ChrTalk(
        0x8,
        (
            "If you need any help,\x01",
            "please say so. I will do my\x01",
            "very best to assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA4")

    Jump("loc_1C5B")

    label("loc_1AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B27")

    ChrTalk(
        0x8,
        (
            "Welcome. We're open on\x01",
            "rainy days too, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please enjoy your\x01",
            "shopping today as well.\x01",
            "(*smile*)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5B")

    label("loc_1B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEA")

    ChrTalk(
        0x8,
        (
            "Thank you for shopping\x01",
            "at Times Department\x01",
            "Store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is the information\x01",
            "desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is anything you\x01",
            "are not sure about, please\x01",
            "feel free to ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C5B")

    label("loc_1BEA")


    ChrTalk(
        0x8,
        (
            "This is the information\x01",
            "desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is anything you\x01",
            "are not sure about, please\x01",
            "feel free to ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5B")

    TalkEnd(0x8)
    Return()

    # Function_6_DD6 end

    def Function_7_1C5F(): pass

    label("Function_7_1C5F")

    Call(0, 8)
    Return()

    # Function_7_1C5F end

    def Function_8_1C63(): pass

    label("Function_8_1C63")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C74")
    Jump("loc_2654")

    label("loc_1C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C82")
    Jump("loc_2654")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D2A")

    ChrTalk(
        0x9,
        (
            "I've heard different things about\x01",
            "the identity of that armed group.\x01",
            "I wonder who it really is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway... I pray that\x01",
            "the citizens are not\x01",
            "hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_1D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DAB")

    ChrTalk(
        0x9,
        (
            "Pearl and Scott have\x01",
            "been friends ever since\x01",
            "forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's cute that her\x01",
            "fiancｳ is her childhood\x01",
            "friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_1DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E38")

    ChrTalk(
        0x9,
        (
            "The manager said a train\x01",
            "derailed near West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope everyone's\x01",
            "injuries aren't too\x01",
            "serious, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_1E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7F")

    ChrTalk(
        0x9,
        (
            "I feel like the heat in\x01",
            "arguments over\x01",
            "independence is building.\x02",
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
            "For now, I'm planning on\x01",
            "seeing the referendum results.\x01",
            "Then I'll return home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2001")

    label("loc_1F7F")


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
            "I'll return home only\x01",
            "after seeing the\x01",
            "referendum results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2001")

    Jump("loc_2654")

    label("loc_2006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2021")
    Call(0, 10)
    Jump("loc_20BA")

    label("loc_2021")


    ChrTalk(
        0x9,
        (
            "My... I'm terribly sorry. It\x01",
            "seems I got lost in conversation\x01",
            "during working hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I would be pleased to\x01",
            "help you with anything\x01",
            "you may need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BA")

    Jump("loc_2654")

    label("loc_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2160")

    ChrTalk(
        0x9,
        (
            "I can't believe Jeanetta\x01",
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
        (
            "*sigh*, it's all just so\x01",
            "tiring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21B1")

    label("loc_2160")


    ChrTalk(
        0x9,
        (
            "I can't believe Jeanetta\x01",
            "invited men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*, it's all just so\x01",
            "tiring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    Jump("loc_2654")

    label("loc_21B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_22F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2286")

    ChrTalk(
        0x9,
        (
            "Jeanetta is in awfully\x01",
            "high spirits today. Could\x01",
            "something have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not the first time the three\x01",
            "of us have had dinner together...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22EC")

    label("loc_2286")


    ChrTalk(
        0x9,
        (
            "It's not the first time the three\x01",
            "of us have had dinner together...\x01",
            "Maybe I'm worrying too much?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EC")

    Jump("loc_2654")

    label("loc_22F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_238C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230C")
    Call(0, 9)
    Jump("loc_2387")

    label("loc_230C")


    ChrTalk(
        0x9,
        (
            "Oh, sir... Please excuse\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Welcome to Times Department\x01",
            "Store. Please let me know if\x01",
            "there's anything you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2387")

    Jump("loc_2654")

    label("loc_238C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2433")

    ChrTalk(
        0x9,
        (
            "Tomorrow, VIPs from several\x01",
            "countries will be coming\x01",
            "for the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although they won't be\x01",
            "visiting our store, I'm\x01",
            "nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_2433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_24C0")

    ChrTalk(
        0x9,
        (
            "Pearl is in high spirits because\x01",
            "her fiancｳ, Scott, visits her\x01",
            "every so often right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I think I'm\x01",
            "jealous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2654")

    label("loc_24C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B8")

    ChrTalk(
        0x9,
        (
            "Did you see the new\x01",
            "rooftop space we opened\x01",
            "a few days ago?\x02",
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
        (
            "If you would like to,\x01",
            "please feel free to stop\x01",
            "by.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2654")

    label("loc_25B8")


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
            "Everyone, why not try\x01",
            "stopping by when it's\x01",
            "time for a break.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2654")

    TalkEnd(0x9)
    Return()

    # Function_8_1C63 end

    def Function_9_2658(): pass

    label("Function_9_2658")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        "Pearl, did you hear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that Julia is\x01",
            "coming here from Liberl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I already checked that out,\x01",
            "of course. I've already asked my\x01",
            "friend to take her picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, well, I don't know\x01",
            "whether or not it's any\x01",
            "good.\x02",
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
            "Pearl, hand over that\x01",
            "photo, now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "O-Okay. I don't mind,\x01",
            "but...\x02",
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

    # Function_9_2658 end

    def Function_10_284B(): pass

    label("Function_10_284B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "Then, the place\x01",
            "Southwark confessed\x01",
            "is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, it seems like it was\x01",
            "Fortuna, the high-class\x01",
            "restaurant at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, he asked the staff\x01",
            "to put on a show for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So Southwark is a\x01",
            "director, is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, but I'm glad\x01",
            "Jeanetta liked it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I've got to follow\x01",
            "her example.\x02",
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

    # Function_10_284B end

    def Function_11_29C4(): pass

    label("Function_11_29C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29DF")
    Call(0, 46)
    Jump("loc_29E2")

    label("loc_29DF")

    Call(0, 12)

    label("loc_29E2")

    Return()

    # Function_11_29C4 end

    def Function_12_29E3(): pass

    label("Function_12_29E3")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A42")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2A42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A61")
    OP_AF(0x26)
    Jump("loc_2A83")

    label("loc_2A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2A71")
    OP_AF(0x25)
    Jump("loc_2A83")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A81")
    OP_AF(0x24)
    Jump("loc_2A83")

    label("loc_2A81")

    OP_AF(0x23)

    label("loc_2A83")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BB3")

    label("loc_2A92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA6")
    Jump("loc_3BB3")

    label("loc_2AA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B96")

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
            "For here on, we'll hire even more\x01",
            "workers, and endeavor to provide\x01",
            "everyone will a full range of services.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB3")

    label("loc_2B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C7B")

    ChrTalk(
        0xA,
        (
            "I wonder just how long\x01",
            "this martial law order\x01",
            "is going to last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Regarding food and supplies,\x01",
            "most families only have\x01",
            "enough to last a few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm truly scared of the\x01",
            "unseen problems that lie\x01",
            "ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB3")

    label("loc_2C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D96")

    ChrTalk(
        0xA,
        (
            "I wonder if the State\x01",
            "Guard can really hold\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although I want to\x01",
            "believe in Arios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the two major powers invade\x01",
            "simultaneously, we'll have no\x01",
            "choice but to capitulate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or possibly... Might he\x01",
            "have some sort of secret\x01",
            "plan?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E2E")

    label("loc_2D96")


    ChrTalk(
        0xA,
        (
            "If the two major powers invade\x01",
            "simultaneously, we'll have no\x01",
            "choice but to capitulate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or possibly... Might he\x01",
            "have some sort of secret\x01",
            "plan?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2E")

    Jump("loc_3BB3")

    label("loc_2E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EE5")

    ChrTalk(
        0xA,
        (
            "It seems the city's\x01",
            "reconstruction is\x01",
            "finally coming along.\x02",
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
    Jump("loc_3BB3")

    label("loc_2EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F56")

    ChrTalk(
        0xA,
        (
            "The faces of my regular\x01",
            "customers in Mainz come\x01",
            "to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope they're all safe,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB3")

    label("loc_2F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_313F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3075")

    ChrTalk(
        0xA,
        (
            "Yesterday, when I heard train\x01",
            "service had stopped, I\x01",
            "wondered what happened, but...\x02",
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
            "Thanks to that, this\x01",
            "morning's delivery\x01",
            "arrived safely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_313A")

    label("loc_3075")


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
            "To thank the efforts of the police\x01",
            "and station staff that restored\x01",
            "service, words are not enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313A")

    Jump("loc_3BB3")

    label("loc_313F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3184")

    ChrTalk(
        0xA,
        (
            "Hmm, it seems some sort\x01",
            "of accident has\x01",
            "occurred.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB3")

    label("loc_3184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_323E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_END)), "loc_3239")

    ChrTalk(
        0xA,
        (
            "Mr. Dudley is a regular customer\x01",
            "at our store and has us make shoes\x01",
            "for him several times a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "His passion and\x01",
            "pickiness are hallmarks\x01",
            "of a true fan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3239")

    Jump("loc_3BB3")

    label("loc_323E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3330")

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
    Jump("loc_3BB3")

    label("loc_3330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33B4")

    ChrTalk(
        0xA,
        (
            "Truly good things are\x01",
            "not influenced by\x01",
            "trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I always offer goods\x01",
            "that are loved across\x01",
            "the generations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB3")

    label("loc_33B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_363F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3530")

    ChrTalk(
        0xA,
        (
            "Everyone, did you know that\x01",
            "it's best to try on shoes\x01",
            "in the evening or later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is because, after we wake in the morning,\x01",
            "human feet swell little by little, and when evening\x01",
            "arrives, they can be as much as 1 rige bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is thought best to choose\x01",
            "your size in the evening or later, when\x01",
            "your feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_363A")

    label("loc_3530")


    ChrTalk(
        0xA,
        (
            "The truth is, after we wake in the morning, human\x01",
            "feet swell little by little, and when evening\x01",
            "arrives, they can be as much as 1 rige bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is why it is thought best to choose\x01",
            "your size in the evening or later, when\x01",
            "your feet are at their biggest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363A")

    Jump("loc_3BB3")

    label("loc_363F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36D9")

    ChrTalk(
        0xA,
        (
            "The more you put a pair of\x01",
            "shoes on, the more comfortable\x01",
            "and familiar they will feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "People and relationships\x01",
            "are the same way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB3")

    label("loc_36D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3959")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3770")

    ChrTalk(
        0xA,
        (
            "We have a full\x01",
            "complement of goods for\x01",
            "children as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, take your time\x01",
            "perusing them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3954")

    label("loc_3770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_389F")

    ChrTalk(
        0xA,
        (
            "Prada has been poking fun at\x01",
            "me for as long as she's been\x01",
            "handling the clothes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The world of shoes is extremely\x01",
            "complicated. She would understand that\x01",
            "if she were in my shoes for a day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is exactly why I\x01",
            "disregard her comments and\x01",
            "focus exclusively on shoes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3954")

    label("loc_389F")


    ChrTalk(
        0xA,
        (
            "The world of clothes is the same,\x01",
            "of course, but the world of shoes\x01",
            "is extremely complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is exactly why I\x01",
            "disregard her comments and\x01",
            "focus exclusively on shoes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3954")

    Jump("loc_3BB3")

    label("loc_3959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F1")

    ChrTalk(
        0xA,
        (
            "We sell rain shoes as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There are customers who buy and\x01",
            "change into them immediately in\x01",
            "sudden rain like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A5A")

    label("loc_39F1")


    ChrTalk(
        0xA,
        (
            "We sell rain shoes as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you would like, I would\x01",
            "be happy to recommend\x01",
            "something to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A5A")

    Jump("loc_3BB3")

    label("loc_3A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B26")

    ChrTalk(
        0xA,
        (
            "Welcome to Hanson's\x01",
            "Shoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you are having trouble\x01",
            "finding anything, please\x01",
            "do not hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I would be delighted to\x01",
            "find the perfect pair\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BB3")

    label("loc_3B26")


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
            "I will surely find the\x01",
            "perfect pair for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB3")

    Jump("loc_29F0")

    label("loc_3BB8")

    TalkEnd(0xA)
    Return()

    # Function_12_29E3 end

    def Function_13_3BBC(): pass

    label("Function_13_3BBC")

    SetScenarioFlags(0x2, 3)
    Call(0, 14)
    Return()

    # Function_13_3BBC end

    def Function_14_3BC3(): pass

    label("Function_14_3BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C30")
    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "You don't look like the\x01",
            "delivery man.\x02",
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

    label("loc_3C30")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD9")

    ChrTalk(
        0x1A2,
        (
            "I see. So you deal with\x01",
            "a lot of imported\x01",
            "ingredients here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmm, you even have soy\x01",
            "sauce.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Haha, might you be from\x01",
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
        (
            "S-Sure... I'll think\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TalkEnd(0xB)
    Jump("loc_3E5A")

    label("loc_3DD9")

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
        (
            "Please let me know if\x01",
            "there's anything you\x01",
            "need.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)

    label("loc_3E5A")

    Return()

    label("loc_3E5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_501A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EB7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED7")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5015")

    label("loc_3ED7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EEB")
    Jump("loc_5015")

    label("loc_3EEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5015")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FAF")

    ChrTalk(
        0xB,
        (
            "I was able to get in contact\x01",
            "with my daughter and confirm\x01",
            "her safety just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She brought out her cart\x01",
            "right away, so I've got\x01",
            "to do my best too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5015")

    label("loc_3FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4062")

    ChrTalk(
        0xB,
        (
            "Even so... Wouldn't my\x01",
            "daughter be safer at\x01",
            "home?\x02",
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
    Jump("loc_5015")

    label("loc_4062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416E")

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
            "I heard that today, the trains\x01",
            "will finally stop service, the\x01",
            "same as the buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Given the situation, war\x01",
            "comes to mind, rather\x01",
            "than sales.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4204")

    label("loc_416E")


    ChrTalk(
        0xB,
        (
            "I heard that today, the trains\x01",
            "will finally stop service, the\x01",
            "same as the buses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Given the situation, war\x01",
            "comes to mind, rather\x01",
            "than sales.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4204")

    Jump("loc_5015")

    label("loc_4209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D8")

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
            "Welcome. For your worn-\x01",
            "out bodies, how about\x01",
            "some Ored State garlic?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_435D")

    label("loc_42D8")


    ChrTalk(
        0xB,
        (
            "Welcome. For your worn-\x01",
            "out bodies, how about\x01",
            "some Ored State garlic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ored garlic is large and\x01",
            "nutritious. I recommend\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435D")

    Jump("loc_5015")

    label("loc_4362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_43DE")

    ChrTalk(
        0xB,
        (
            "I wonder how the people\x01",
            "of Mainz are doing right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hope the situation is\x01",
            "resolved soon, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5015")

    label("loc_43DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_456F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44DC")

    ChrTalk(
        0xB,
        (
            "It seems orbal train service\x01",
            "was completely restored in\x01",
            "the space of one night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to that, today's\x01",
            "train arrived as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm grateful to the all the\x01",
            "police who worked through the\x01",
            "night to restore service.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_456A")

    label("loc_44DC")


    ChrTalk(
        0xB,
        (
            "Thanks to that, today's\x01",
            "train arrived as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm grateful to the all the\x01",
            "police who worked through the\x01",
            "night to restore service.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456A")

    Jump("loc_5015")

    label("loc_456F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45FE")

    ChrTalk(
        0xB,
        (
            "I understand a train has\x01",
            "derailed near West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if some sort of\x01",
            "cave-in occurred.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4672")

    label("loc_45FE")


    ChrTalk(
        0xB,
        (
            "I understand a train has\x01",
            "derailed near West\x01",
            "Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wonder if some sort of\x01",
            "cave-in occurred.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4672")

    Jump("loc_5015")

    label("loc_4677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4710")

    ChrTalk(
        0xB,
        (
            "If you're looking for\x01",
            "ingredients, then\x01",
            "welcome to Region Foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Today, we're offering a\x01",
            "great deal on Republican\x01",
            "spring onions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5015")

    label("loc_4710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_479E")

    ChrTalk(
        0xB,
        (
            "It seems Southwark and\x01",
            "Jeanetta have been going\x01",
            "steady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, I'd like to fall\x01",
            "in love with one of my\x01",
            "co-workers too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5015")

    label("loc_479E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4826")

    ChrTalk(
        0xB,
        (
            "Jeanetta looks down\x01",
            "today. I'm worried about\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She looked so happy\x01",
            "yesterday. Could\x01",
            "something have happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5015")

    label("loc_4826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_48CB")

    ChrTalk(
        0xB,
        (
            "Good evening, and\x01",
            "welcome to Region Foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you haven't prepared dinner\x01",
            "yet, by all means, please come buy\x01",
            "your ingredients from us, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5015")

    label("loc_48CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A23")

    ChrTalk(
        0xB,
        (
            "If you're looking for\x01",
            "ingredients, then\x01",
            "welcome to Region Foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Starting today, and for the next\x01",
            "three days, we'll be selling our\x01",
            "special Trade Conference Set.\x02",
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
    Jump("loc_4B1A")

    label("loc_4A23")


    ChrTalk(
        0xB,
        (
            "Starting today, and for the next\x01",
            "three days, we'll be selling our\x01",
            "special Trade Conference Set.\x02",
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

    label("loc_4B1A")

    Jump("loc_5015")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C7D")

    ChrTalk(
        0xB,
        (
            "Welcome to Region Foods,\x01",
            "the reliable ally of\x01",
            "every housewife!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you need any help with\x01",
            "tonight's menu, I'd be happy\x01",
            "to give you some advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For example, how about a soup\x01",
            "using our fresh fresh herb that\x01",
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
    Jump("loc_4D0E")

    label("loc_4C7D")


    ChrTalk(
        0xB,
        (
            "If you need any help with\x01",
            "tonight's menu, I'd be happy\x01",
            "to give you some advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the way, today's\x01",
            "recommendation is fresh\x01",
            "herb soup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D0E")

    Jump("loc_5015")

    label("loc_4D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE8")

    ChrTalk(
        0xB,
        (
            "My daughter is working\x01",
            "on her new juice stand\x01",
            "menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's raining today, so her\x01",
            "stand's not open. She's at\x01",
            "home working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, it's great that\x01",
            "she has some ambition.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E53")

    label("loc_4DE8")


    ChrTalk(
        0xB,
        (
            "My daughter is working\x01",
            "on her new juice stand\x01",
            "menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, it's great that\x01",
            "she has some ambition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E53")

    Jump("loc_5015")

    label("loc_4E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F68")

    ChrTalk(
        0xB,
        (
            "If you're looking for\x01",
            "ingredients, then\x01",
            "welcome to Region Foods.\x02",
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
            "My daughter runs a juice\x01",
            "stand in Governmental\x01",
            "District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5015")

    label("loc_4F68")


    ChrTalk(
        0xB,
        (
            "If you're looking for\x01",
            "ingredients, then\x01",
            "welcome to Region Foods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please visit the juice stand in\x01",
            "Governmental district. Their juice\x01",
            "is made using our ingredients!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5015")

    Jump("loc_3E65")

    label("loc_501A")

    TalkEnd(0xB)
    Return()

    # Function_14_3BC3 end

    def Function_15_501E(): pass

    label("Function_15_501E")

    Call(0, 16)
    Return()

    # Function_15_501E end

    def Function_16_5022(): pass

    label("Function_16_5022")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_502F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5081")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5081")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50A0")
    OP_AF(0x21)
    Jump("loc_50C2")

    label("loc_50A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50B0")
    OP_AF(0x20)
    Jump("loc_50C2")

    label("loc_50B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50C0")
    OP_AF(0x1F)
    Jump("loc_50C2")

    label("loc_50C0")

    OP_AF(0x1E)

    label("loc_50C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_608A")

    label("loc_50D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50E5")
    Jump("loc_608A")

    label("loc_50E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51E6")

    ChrTalk(
        0xC,
        (
            "I was thinking of doing it sooner or\x01",
            "later... But I've decided to take this\x01",
            "opportunity to introduce my new brand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Greatness shiness in the face of\x01",
            "adversity― I'll create products\x01",
            "everyone will surely love!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_51E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_53C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52FC")

    ChrTalk(
        0xC,
        (
            "The President was\x01",
            "confident because of\x01",
            "those Aion weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...But, what's with\x01",
            "those armored soldier-\x01",
            "like monsters in town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Scaring the citizens with those things\x01",
            "without giving a proper notice... They\x01",
            "have their priorities backwards.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53BE")

    label("loc_52FC")


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
            "Scaring the citizens with those things\x01",
            "without giving a proper notice... They\x01",
            "have their priorities backwards.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53BE")

    Jump("loc_608A")

    label("loc_53C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5498")

    ChrTalk(
        0xC,
        (
            "Maybe it's because I'm in retail.\x01",
            "I have a bad habit of viewing\x01",
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
    Jump("loc_608A")

    label("loc_5498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5531")

    ChrTalk(
        0xC,
        (
            "Three days from now, each\x01",
            "of us will take turns going\x01",
            "to the polling place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, I'm still\x01",
            "undecided. *sigh*, what\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_5531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_55E1")

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
            "Trapping people with\x01",
            "explosions... It's nothing\x01",
            "but sheer stupidity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_55E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56E4")

    ChrTalk(
        0xC,
        (
            "I feel like there's fewer\x01",
            "customers walking in with\x01",
            "smiles on their faces lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Given yesterday's train\x01",
            "accident, I suppose\x01",
            "that's only human nature.\x02",
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
    Jump("loc_5781")

    label("loc_56E4")


    ChrTalk(
        0xC,
        (
            "I feel like there's fewer\x01",
            "customers walking in with\x01",
            "smiles on their faces lately.\x02",
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

    label("loc_5781")

    Jump("loc_608A")

    label("loc_5786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57B7")

    ChrTalk(
        0xC,
        (
            "My, it sure is noisy\x01",
            "outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_57B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_59A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C5")

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
            "So if you're ever\x01",
            "feeling down, try\x01",
            "wearing bright colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you do that, your\x01",
            "depression will fly\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_59A0")

    label("loc_58C5")


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
            "Look for clothes that match up\x01",
            "with how you feel. ...That's\x01",
            "also a method of choosing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59A0")

    Jump("loc_608A")

    label("loc_59A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5A6F")

    ChrTalk(
        0xC,
        (
            "The more expensive clothes\x01",
            "and handbags are, the more\x01",
            "they influence unseen trends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There are many that are durable\x01",
            "and can be used for a long time,\x01",
            "so I think they're worth it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_5A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B1C")

    ChrTalk(
        0xC,
        (
            "Although fashion is ever changing,\x01",
            "that phenomenon is actually caused\x01",
            "by everyone collectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a boutique owner, I\x01",
            "try to create fashion\x01",
            "trends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_5B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5B61")

    ChrTalk(
        0xC,
        (
            "Welcome, please enjoy\x01",
            "your shopping this\x01",
            "evening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_5B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BF6")

    ChrTalk(
        0xC,
        (
            "The trade conference has\x01",
            "finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As someone in the fashion\x01",
            "business, I need to pay\x01",
            "attention to the VIP's fashions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_5BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D7A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CB8")

    ChrTalk(
        0xC,
        (
            "Welcome. Please have a\x01",
            "look at all the latest\x01",
            "fashions we have in stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If you'd like to try\x01",
            "something on, please\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D75")

    label("loc_5CB8")


    ChrTalk(
        0xC,
        (
            "Hanson was my business\x01",
            "rival when he sold\x01",
            "clothes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sometimes, having a\x01",
            "rival motivates each to\x01",
            "improve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I like shoes too, but\x01",
            "I'm glad I didn't\x01",
            "specialize in them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5D75")

    Jump("loc_608A")

    label("loc_5D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E80")

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
            "If you would like, I\x01",
            "could show you some of\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F34")

    label("loc_5E80")


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

    label("loc_5F34")

    Jump("loc_608A")

    label("loc_5F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_608A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6000")

    ChrTalk(
        0xC,
        (
            "Welcome to boutique\x01",
            ""Lucca".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This store offers clothes from\x01",
            "various manufacturers that\x01",
            "I've selected personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please have a look at\x01",
            "them at your leisure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_608A")

    label("loc_6000")


    ChrTalk(
        0xC,
        (
            "This store offers clothes from\x01",
            "various manufacturers that\x01",
            "I've selected personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please have a look at\x01",
            "them at your leisure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_608A")

    Jump("loc_502F")

    label("loc_608F")

    TalkEnd(0xC)
    Return()

    # Function_16_5022 end

    def Function_17_6093(): pass

    label("Function_17_6093")

    Call(0, 18)
    Return()

    # Function_17_6093 end

    def Function_18_6097(): pass

    label("Function_18_6097")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_701A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60F6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_60F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6115")
    OP_AF(0x11)
    Jump("loc_6127")

    label("loc_6115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6125")
    OP_AF(0x10)
    Jump("loc_6127")

    label("loc_6125")

    OP_AF(0xF)

    label("loc_6127")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7015")

    label("loc_6136")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_614A")
    Jump("loc_7015")

    label("loc_614A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7015")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6224")

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
    Jump("loc_7015")

    label("loc_6224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6329")

    ChrTalk(
        0xD,
        (
            "I'm pretty sure it wasn't the State\x01",
            "Guard who defended against those\x01",
            "Imperial railway cannons, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This situation is just\x01",
            "one unsettling thing\x01",
            "after the next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Realization of a\x01",
            ""Continental Alliance" is\x01",
            "purely academic, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_6329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63DF")

    ChrTalk(
        0xD,
        (
            "Such a sudden speech was\x01",
            "surprising...\x02",
        )
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
    Jump("loc_6471")

    label("loc_63DF")


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

    label("loc_6471")

    Jump("loc_7015")

    label("loc_6476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_655C")

    ChrTalk(
        0xD,
        (
            "To solve the root cause of\x01",
            "Crossbell's various problems, there\x01",
            "is no other path but independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To think something like that happened\x01",
            "to the city... We can be sure the\x01",
            "major powers cannot maintain order.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_655C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6611")

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
    Jump("loc_7015")

    label("loc_6611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66BB")

    ChrTalk(
        0xD,
        (
            "There a rumor going around that\x01",
            "yesterday's train derailment was\x01",
            "caused by something called a cryptid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, but just what is a\x01",
            "cryptid, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_66BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6756")

    ChrTalk(
        0xD,
        (
            "I've been hearing\x01",
            "ambulance sirens for\x01",
            "some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wonder if it's a terrorist\x01",
            "attack. ...We've already had\x01",
            "so many tragedies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_6756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_68C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6835")

    ChrTalk(
        0xD,
        (
            "The value of accessories\x01",
            "isn't the same to\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I received a handmade brooch\x01",
            "from my granddaughter the\x01",
            "other day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, it is more\x01",
            "valuable than the\x01",
            "greatest treasure.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_68BF")

    label("loc_6835")


    ChrTalk(
        0xD,
        (
            "I received a handmade brooch\x01",
            "from my granddaughter the\x01",
            "other day, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To me, it is more\x01",
            "valuable than the\x01",
            "greatest treasure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68BF")

    Jump("loc_7015")

    label("loc_68C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C5")

    ChrTalk(
        0xD,
        (
            "Hmm, state independence,\x01",
            "huh. This is a problem that\x01",
            "requires a lot of thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Though I myself once threw\x01",
            "away the Empire and came to\x01",
            "live here in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I cannot help but say\x01",
            "this is an unthinkable\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A6E")

    label("loc_69C5")


    ChrTalk(
        0xD,
        (
            "Though I myself once threw\x01",
            "away the Empire and came to\x01",
            "live here in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't help but say the\x01",
            "state independence proposal\x01",
            "is a difficult question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A6E")

    Jump("loc_7015")

    label("loc_6A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6AF6")

    ChrTalk(
        0xD,
        (
            "Hmm, so the trade\x01",
            "conference finally\x01",
            "started, has it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Anyway, I just want the\x01",
            "conference to be\x01",
            "worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_6AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB6")

    ChrTalk(
        0xD,
        "It's already dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's right, Arc-en-Ciel's\x01",
            "performance for the heads of\x01",
            "state should be ending soon.\x02",
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
    Jump("loc_6C43")

    label("loc_6BB6")


    ChrTalk(
        0xD,
        (
            "That's right, Arc-en-Ciel's\x01",
            "performance for the heads of\x01",
            "state should be ending soon.\x02",
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

    label("loc_6C43")

    Jump("loc_7015")

    label("loc_6C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6CD2")

    ChrTalk(
        0xD,
        (
            "I saw the unveiling\x01",
            "ceremony from our\x01",
            "rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Orchis tower is truly a\x01",
            "sight to behold. I am at\x01",
            "a loss for words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7015")

    label("loc_6CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6E17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D7B")

    ChrTalk(
        0xD,
        (
            "Welcome to Baker's\x01",
            "Accessories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there is anything here\x01",
            "that catches your eye then\x01",
            "please, take a closer look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E12")

    label("loc_6D7B")


    ChrTalk(
        0xD,
        (
            "Many warm-hearted\x01",
            "customers visit our\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's very different from\x01",
            "Imperial nobles, though I do\x01",
            "not mean to compare the two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E12")

    Jump("loc_7015")

    label("loc_6E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F22")

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
            "*sigh*, I feel out of\x01",
            "breath just thinking\x01",
            "back on it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F96")

    label("loc_6F22")


    ChrTalk(
        0xD,
        (
            "I apologize. You all are\x01",
            "probably not interested\x01",
            "in my personal stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Welcome. Please, take\x01",
            "your time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F96")

    Jump("loc_7015")

    label("loc_6F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7015")

    ChrTalk(
        0xD,
        (
            "Welcome. Please, have a\x01",
            "look around.\x02",
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

    label("loc_7015")

    Jump("loc_60A4")

    label("loc_701A")

    TalkEnd(0xD)
    Return()

    # Function_18_6097 end

    def Function_19_701E(): pass

    label("Function_19_701E")

    SetScenarioFlags(0x2, 4)
    Call(0, 20)
    Return()

    # Function_19_701E end

    def Function_20_7025(): pass

    label("Function_20_7025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7151")
    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D0")

    ChrTalk(
        0xE,
        (
            "Huh, where did you guys\x01",
            "come in from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Oh, right.\x02",
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
    Jump("loc_714D")

    label("loc_70D0")


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
            "Oh, please don't touch\x01",
            "that inventory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_714D")

    TalkEnd(0xE)
    Return()

    label("loc_7151")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7251")

    ChrTalk(
        0xE,
        (
            "Oh, hello. Welcome to\x01",
            "Southwark's General\x01",
            "Goods Corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "From daily necessities to\x01",
            "souvenirs, we sell a wide\x01",
            "variety of different products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please, take your time\x01",
            "looking through them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_72DB")

    label("loc_7251")


    ChrTalk(
        0xE,
        (
            "From daily necessities to\x01",
            "souvenirs, we sell a wide\x01",
            "variety of different products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please, take your time\x01",
            "looking through them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72DB")

    TalkEnd(0xE)
    Return()

    label("loc_72E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7443")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd spoke to\x01",
            "shopkeeper Southwark in\x01",
            "a low voice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000F(Excuse me, how much for\x01",
            "a "Tick-Tock Mishy"?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "(Oh, that'll be 500\x01",
            "mira.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "(Haha, might it be a\x01",
            "present for your kid?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Uh, yes. I'm still\x01",
            "thinking about it\x01",
            "though.)\x02\x03",
            "#00003F(It's 500 mira... Should\x01",
            "I buy it for Shing?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7490")

    label("loc_7443")


    ChrTalk(
        0xE,
        (
            "(It's 500 mira for a\x01",
            "Tick-Tock Mishy. You\x01",
            "buying?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Hmm...)\x02",
    )

    CloseMessageWindow()

    label("loc_7490")

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
            "Buy a [Tick-Tock Mishy]\x01",      # 0
            "Think about it\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7625")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_757D")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F(Umm, then, I'd like one\x01",
            "please.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(20, 0, 80, 0)

    ChrTalk(
        0xE,
        (
            "(Alright. Thanks for\x01",
            "your business.)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 52)
    Jump("loc_7620")

    label("loc_757D")


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
            "#00006F(I don't have the\x01",
            "mira... *sigh*, how poor\x01",
            "am I?)\x02\x03",
            "#00000F(Sorry, I'll go\x01",
            "without.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "(???)\x02",
    )

    CloseMessageWindow()

    label("loc_7620")

    Jump("loc_765E")

    label("loc_7625")


    ChrTalk(
        0x101,
        (
            "#00003F(I'd like to think about\x01",
            "it a bit longer...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_765E")

    TalkEnd(0xE)
    Return()

    label("loc_7667")


    ChrTalk(
        0xE,
        "I'm sure he'll love it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, but Mishy sure is\x01",
            "great.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    label("loc_76AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B1C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7707")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7707")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7726")
    OP_AF(0x1D)
    Jump("loc_77A8")

    label("loc_7726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7736")
    OP_AF(0x1C)
    Jump("loc_77A8")

    label("loc_7736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7746")
    OP_AF(0x1B)
    Jump("loc_77A8")

    label("loc_7746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7756")
    OP_AF(0x1A)
    Jump("loc_77A8")

    label("loc_7756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7766")
    OP_AF(0x19)
    Jump("loc_77A8")

    label("loc_7766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7776")
    OP_AF(0x18)
    Jump("loc_77A8")

    label("loc_7776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_7786")
    OP_AF(0x17)
    Jump("loc_77A8")

    label("loc_7786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7796")
    OP_AF(0x16)
    Jump("loc_77A8")

    label("loc_7796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_77A6")
    OP_AF(0x15)
    Jump("loc_77A8")

    label("loc_77A6")

    OP_AF(0x14)

    label("loc_77A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B17")

    label("loc_77B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77CB")
    Jump("loc_8B17")

    label("loc_77CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B17")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78CA")

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
    Jump("loc_8B17")

    label("loc_78CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7976")

    ChrTalk(
        0xE,
        (
            "In times like these, it's\x01",
            "reassuring to have one's\x01",
            "loved ones close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm not sure how to say\x01",
            "this, but I feel courage\x01",
            "welling up from inside me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B17")

    label("loc_7976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B03")

    ChrTalk(
        0xE,
        (
            "This morning, an evacuation notice from the\x01",
            "Republican government suddenly came in. All\x01",
            "Republic citizens are to return ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "They're preparing to use force. I\x01",
            "don't know what's going to happen\x01",
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
    Jump("loc_7B6B")

    label("loc_7B03")


    ChrTalk(
        0xE,
        (
            "No matter what happens,\x01",
            "I've decided to stay put\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll definitely protect\x01",
            "my girlfriend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B6B")

    Jump("loc_8B17")

    label("loc_7B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7C1C")

    ChrTalk(
        0xE,
        (
            "Why did that have to happen to\x01",
            "Ilya? It's the long-awaited\x01",
            "renewal performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I wasn't scared during\x01",
            "the attack, but... Now\x01",
            "I'm positively mad!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B17")

    label("loc_7C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7DDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D2F")

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
            "Perhaps letting everyone\x01",
            "enjoy the performance will\x01",
            "give them courage and energy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7DD5")

    label("loc_7D2F")


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
            "Perhaps letting everyone\x01",
            "enjoy the performance will\x01",
            "give them courage and energy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD5")

    Jump("loc_8B17")

    label("loc_7DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7E86")

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
            "How to put it... This\x01",
            "must be what they call\x01",
            "happiness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B17")

    label("loc_7E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7F0F")

    ChrTalk(
        0xE,
        (
            "There's an uproar over\x01",
            "the train accident that\x01",
            "occurred west of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I hope it's not a\x01",
            "terrorist attack, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B17")

    label("loc_7F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_80A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8010")

    ChrTalk(
        0xE,
        (
            "The referendum on the question of independence,\x01",
            "eh? It's a serious responsibility even though\x01",
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
    Jump("loc_809F")

    label("loc_8010")


    ChrTalk(
        0xE,
        (
            "The referendum on the\x01",
            "question of\x01",
            "independence, eh?\x02",
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

    label("loc_809F")

    Jump("loc_8B17")

    label("loc_80A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_81F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8168")

    ChrTalk(
        0xE,
        (
            "At first I thought she was a cute\x01",
            "little sister... I don't understand\x01",
            "people's feelings, do I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, I'm happy. Thank\x01",
            "goodness I had the\x01",
            "courage to ask her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_81F2")

    label("loc_8168")


    ChrTalk(
        0xE,
        (
            "Jeanetta, at first I\x01",
            "thought she was your\x01",
            "cute little sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, I'm happy. Thank\x01",
            "goodness I had the\x01",
            "courage to ask her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F2")

    Jump("loc_8B17")

    label("loc_81F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8323")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C9")

    ChrTalk(
        0xE,
        (
            "It seems Jeanetta had\x01",
            "dinner with some rich\x01",
            "men last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "But it seems she was\x01",
            "utterly rejected by all\x01",
            "of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hmm, I wonder if there's\x01",
            "anything I can do for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_831E")

    label("loc_82C9")


    ChrTalk(
        0xE,
        (
            "Hmm, I wonder if there's\x01",
            "anything I can do for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I feel the same way...\x02",
    )

    CloseMessageWindow()

    label("loc_831E")

    Jump("loc_8B17")

    label("loc_8323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_84A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_842E")

    ChrTalk(
        0xE,
        (
            "Jeanetta has been\x01",
            "looking really happy\x01",
            "since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "She was saying something I didn't\x01",
            "understand, like she's going to make a\x01",
            "fresh start tomorrow as "super Jeanetta"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't know, but for\x01",
            "some reason I'm really\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_84A4")

    label("loc_842E")


    ChrTalk(
        0xE,
        (
            "Jeanetta has been\x01",
            "looking really happy\x01",
            "since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't know, but for\x01",
            "some reason I'm really\x01",
            "worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84A4")

    Jump("loc_8B17")

    label("loc_84A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85D3")

    ChrTalk(
        0xE,
        (
            "The unveiling ceremony, eh?\x01",
            "I couldn't see myself, it\x01",
            "but it must've been amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's amazing that Dieter was able to\x01",
            "gather all those heads of state. You only\x01",
            "ever see them in news magazines and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can't wait for the\x01",
            "next issue of Crossbell\x01",
            "Times.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_864F")

    label("loc_85D3")


    ChrTalk(
        0xE,
        (
            "The unveiling ceremony,\x01",
            "eh? IIt must've been\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway, I can't wait for\x01",
            "the next issue of\x01",
            "Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_864F")

    Jump("loc_8B17")

    label("loc_8654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_88F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884F")

    ChrTalk(
        0xE,
        (
            "Did you know Arc-en-Ciel's\x01",
            ""Golden Sun, Silver Moon" is\x01",
            "getting a renewal performance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The details haven't been\x01",
            "announced, but I heard they are\x01",
            "making a bold new addition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hahaha. And somehow... I\x01",
            "was able to get two\x01",
            "tickets for opening night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FWow, glad to hear it.\x02\x03",
            "#00309FBy the way, who are you\x01",
            "taking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ooh... Please, don't ask\x01",
            "me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "A-Anyway, there a month\x01",
            "left until opening\x01",
            "night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll do something about\x01",
            "that before then. Yeah.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_88F0")

    label("loc_884F")


    ChrTalk(
        0xE,
        (
            "I was lucky to be able to get two\x01",
            "tickets for opening night of the\x01",
            "Arc-en-Ciel renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm planning on looking\x01",
            "for someone to go with\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88F0")

    Jump("loc_8B17")

    label("loc_88F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8910")
    Call(0, 21)
    Jump("loc_8960")

    label("loc_8910")


    ChrTalk(
        0xE,
        (
            "I'd understand if it was\x01",
            "her birthday, but... She's\x01",
            "pestering me as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8960")

    Jump("loc_8B17")

    label("loc_8965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AB4")

    ChrTalk(
        0xE,
        (
            "Oh, hello. Welcome to\x01",
            "Southwark's General\x01",
            "Goods Corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Lately, I've been stocking more\x01",
            "Mishy goods to live up to my\x01",
            "customers' high expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you like, please take\x01",
            "one home with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWow, Mishy goods, huh?\x01",
            "I'm sure Tio will be\x01",
            "delighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHaha, that's for sure.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8B17")

    label("loc_8AB4")


    ChrTalk(
        0xE,
        (
            "Our Mishy goods are\x01",
            "thankfully very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If you like, please take\x01",
            "one home with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B17")

    Jump("loc_76B5")

    label("loc_8B1C")

    TalkEnd(0xE)
    Return()

    # Function_20_7025 end

    def Function_21_8B20(): pass

    label("Function_21_8B20")

    OP_4B(0x12, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x12,
        (
            "Ah, this Mishy doll is\x01",
            "so cute! I'd like this\x01",
            "one, Southwark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, sure. Umm, it's 500\x01",
            "mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "That's not what I mean.\x01",
            "Buy it for me, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Why do I have to give\x01",
            "you another present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It's because we work at\x01",
            "the same department\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Oh no no no. That's no\x01",
            "reason at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x12, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_21_8B20 end

    def Function_22_8C81(): pass

    label("Function_22_8C81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DBE")

    ChrTalk(
        0xFE,
        (
            "Just when martial law was canceled that\x01",
            "mysterious gigantic tree appeared... And the\x01",
            "threat of the major powers still remains...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Against unprecedented\x01",
            "difficulties like these, what can\x01",
            "a simple man such as myself do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All any of us can do is\x01",
            "think logically, and\x01",
            "then act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8E57")

    label("loc_8DBE")


    ChrTalk(
        0xFE,
        (
            "Against unprecedented\x01",
            "difficulties like these, what can\x01",
            "a simple man such as myself do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All any of us can do is\x01",
            "think logically, and\x01",
            "then act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E57")

    Jump("loc_A225")

    label("loc_8E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E77")
    Call(0, 23)
    Jump("loc_8F12")

    label("loc_8E77")


    ChrTalk(
        0xFE,
        (
            "It is as you say, Lloyd. It is precisely\x01",
            "because of the movement restrictions\x01",
            "that I want to see the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Please, everyone. Be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F12")

    Jump("loc_A225")

    label("loc_8F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_90E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_904C")

    ChrTalk(
        0xFE,
        (
            "It's been a mere week since the referendum and\x01",
            "the situation's already this bad... I can't\x01",
            "even imagine what's going to happen next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, it's likely\x01",
            "something will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the continued existence of\x01",
            "this department store, we'll\x01",
            "need to exhaust all our ideas.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_90DC")

    label("loc_904C")


    ChrTalk(
        0xFE,
        (
            "Anyway, it's likely\x01",
            "something will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the continued existence of\x01",
            "this department store, we'll\x01",
            "need to exhaust all our ideas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90DC")

    Jump("loc_A225")

    label("loc_90E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_933D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_924F")

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
    Jump("loc_9338")

    label("loc_924F")


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

    label("loc_9338")

    Jump("loc_A225")

    label("loc_933D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_93F8")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group occupying Mainz...\x01",
            "The situation reminds of the nightmare of\x01",
            "the conflict three months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I hope the\x01",
            "situation's resolved\x01",
            "ASAP.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A225")

    label("loc_93F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_95B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9413")
    Call(0, 26)
    Jump("loc_95AF")

    label("loc_9413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9533")

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
            "all throughout the state, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder if those\x01",
            "events are connected\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_95AF")

    label("loc_9533")


    ChrTalk(
        0xFE,
        (
            "A large ogre-like\x01",
            "monster, and large,\x01",
            "mysterious monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I wonder if those\x01",
            "events are connected\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95AF")

    Jump("loc_A225")

    label("loc_95B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9679")

    ChrTalk(
        0xFE,
        (
            "A customer who passed by\x01",
            "the station told me a\x01",
            "train has derailed.\x02",
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
    Jump("loc_A225")

    label("loc_9679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_973A")

    ChrTalk(
        0xFE,
        (
            "Lately, a lot of customers\x01",
            "have been asking me about\x01",
            "state independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of people support it. Also,\x01",
            "a lot of people are worried about\x01",
            "the major powers' reaction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A225")

    label("loc_973A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_989A")

    ChrTalk(
        0xFE,
        (
            "Thinking back on it now, the\x01",
            "events of the trade conference the\x01",
            "other day were a veritable storm.\x02",
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
    Jump("loc_A225")

    label("loc_989A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99AC")

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
            "Thanks to that, we have\x01",
            "more customer traffic,\x01",
            "and sales are up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But above all, I'm glad for this\x01",
            "lively atmosphere. The customers\x01",
            "are enjoying themselves as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9A4F")

    label("loc_99AC")


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
            "Our store is busier than you\x01",
            "usually see, and the customers\x01",
            "are enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A4F")

    Jump("loc_A225")

    label("loc_9A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_9AE1")

    ChrTalk(
        0xFE,
        (
            "Today's business hours\x01",
            "end at 20:00, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take care not to\x01",
            "forget your purchases or\x01",
            "personal belongings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A225")

    label("loc_9AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C09")

    ChrTalk(
        0xFE,
        (
            "Although it's embarrassing to\x01",
            "say, I joined the customers in\x01",
            "viewing the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The majesty of Orchis\x01",
            "Tower is truly a sight\x01",
            "to behold.\x02",
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
    Jump("loc_9C77")

    label("loc_9C09")


    ChrTalk(
        0xFE,
        (
            "A skyscraper that stretches 40\x01",
            "floors above the ground... One could\x01",
            "call it the new symbol of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C77")

    Jump("loc_A225")

    label("loc_9C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A001")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DA4")
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "Oh, Lady Elie. You've\x01",
            "brought an unusual guest\x01",
            "with you today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAh, yes. Today, we're\x01",
            "showing this boy around\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "In that case, I'm happy\x01",
            "you brought him here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, take as long as\x01",
            "you like.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9E05")

    label("loc_9DA4")


    ChrTalk(
        0x11,
        (
            "I'm pleased that you\x01",
            "brought him to our store\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, take as long as\x01",
            "you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E05")

    Jump("loc_9FFC")

    label("loc_9E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F54")

    ChrTalk(
        0xFE,
        (
            "The trade conference\x01",
            "will finally be held\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Representatives from Crossbell\x01",
            "and the four surrounding\x01",
            "nations will all meet...\x02",
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
            "I'm not sure how to express\x01",
            "it, but I am quite excited\x01",
            "to learn the outcome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9FFC")

    label("loc_9F54")


    ChrTalk(
        0xFE,
        (
            "Representatives from Crossbell\x01",
            "and the four surrounding\x01",
            "nations will all meet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not sure how to express\x01",
            "it, but I am quite excited\x01",
            "to learn the outcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FFC")

    Jump("loc_A225")

    label("loc_A001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A0D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A01C")
    Call(0, 24)
    Jump("loc_A0D0")

    label("loc_A01C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A02E")
    Call(0, 25)
    Jump("loc_A0D0")

    label("loc_A02E")


    ChrTalk(
        0x11,
        (
            "We have prepared this small\x01",
            "gift for you, just for coming\x01",
            "to our store on this rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, everyone. Enjoy\x01",
            "as much shopping as\x01",
            "you'd like today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0D0")

    Jump("loc_A225")

    label("loc_A0D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0F0")
    Call(0, 24)
    Jump("loc_A225")

    label("loc_A0F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1BB")

    ChrTalk(
        0xFE,
        (
            "Everyone, allow me to thank\x01",
            "you for coming to Times\x01",
            "Department Store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our store has several\x01",
            "sales counters you may\x01",
            "want to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please take your time,\x01",
            "and enjoy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A225")

    label("loc_A1BB")


    ChrTalk(
        0xFE,
        (
            "We have several sales\x01",
            "counters throughout our\x01",
            "store.\x02",
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

    label("loc_A225")

    TalkEnd(0xFE)
    Return()

    # Function_22_8C81 end

    def Function_23_A229(): pass

    label("Function_23_A229")

    OP_4B(0x11, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x11,
        (
            "Lady Elie and the\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could the movement\x01",
            "restrictions have\x01",
            "been...?\x02",
        )
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
        "Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FMr. Neston, will you tell\x01",
            "us how the department\x01",
            "store's doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes. Yesterday, we were just\x01",
            "about to open when martial\x01",
            "law was handed down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Shortly after, that mist appeared. Immediately\x01",
            "after that, customers and staff came rushing\x01",
            "inside. They've been trapped here ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They were making new\x01",
            "announcements all night,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Really, what does this\x01",
            "government think they're\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F...I see. So they're not\x01",
            "postponing anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FWe're now acting to bring this\x01",
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
            "Understood. ...Please be\x01",
            "careful yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, that's right.\x01",
            "Please, take this to\x01",
            "protect yourselves.\x02",
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
            "#00100FNeston... Thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x11, 0x5A, 0x0)
    SetScenarioFlags(0x1BB, 4)
    Return()

    # Function_23_A229 end

    def Function_24_A65F(): pass

    label("Function_24_A65F")


    ChrTalk(
        0x11,
        (
            "Hello. And welcome to\x01",
            "Times Department Store.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x11,
        (
            "Well, well. If it isn't\x01",
            "Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I heard that you were visiting several\x01",
            "nations with Chairman MacDowell, but\x01",
            "it seems you've returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, just a few days ago.\x02\x03",
            "We will be acting again as\x01",
            "the Special Support Section,\x01",
            "so please look forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, of course. I pray\x01",
            "for your continued well-\x01",
            "being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FYou know the manager,\x01",
            "Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. My grandfather has\x01",
            "known him for a long\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, that's the chairman's\x01",
            "daughter for you. You know\x01",
            "about finance too, right?\x02\x03",
            "I was wondering if we would\x01",
            "get the VIP treatment too.\x02",
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
            "Sorry. I've been told to\x01",
            "offer that to no one but\x01",
            "Lady Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We will treat all of you\x01",
            "the same as we would any\x01",
            "other customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FHaha, there you have it.\x01",
            "Sorry, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FMan, give me a break.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, it is a bit of a\x01",
            "waste.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 3)
    Return()

    # Function_24_A65F end

    def Function_25_AA23(): pass

    label("Function_25_AA23")


    ChrTalk(
        0x11,
        (
            "Thank you for coming on\x01",
            "this rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If you like, please take\x01",
            "this.\x02",
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
        "#00105FNeston, is this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, it's a little thank\x01",
            "you to our customers who\x01",
            "visit us even in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a service we've started\x01",
            "that's limited to just the\x01",
            "first 100 customers each day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell I'm glad we made it\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, the rain seems a\x01",
            "little more fun now,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you very much. I'm\x01",
            "glad to hear you say\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And everyone, please\x01",
            "enjoy your shopping on\x01",
            "this rainy day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 4)
    Return()

    # Function_25_AA23 end

    def Function_26_AC74(): pass

    label("Function_26_AC74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_END)), "loc_ADEE")

    ChrTalk(
        0x11,
        (
            "Thank you for coming\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If you like, please take\x01",
            "this.\x02",
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
        (
            "#00000FOh, this is that service\x01",
            "for rainy days.\x02",
        )
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
            "It is I who should thank\x01",
            "all of you for being our\x01",
            "longtime customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Everyone, please enjoy\x01",
            "your shopping on this\x01",
            "rainy day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B03B")

    label("loc_ADEE")


    ChrTalk(
        0x11,
        (
            "Thank you for coming on\x01",
            "this rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If you like, please take\x01",
            "this.\x02",
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
        "#00105FNeston, is this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, it's a little thank\x01",
            "you to our customers who\x01",
            "visit us even in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "It's a service we've started\x01",
            "that's limited to just the\x01",
            "first 100 customers each day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWell I'm glad we made it\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, the rain seems a\x01",
            "little more fun now,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you very much. I'm\x01",
            "glad to hear you say\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And everyone, please\x01",
            "enjoy your shopping on\x01",
            "this rainy day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B03B")

    SetScenarioFlags(0x16C, 5)
    Return()

    # Function_26_AC74 end

    def Function_27_B03F(): pass

    label("Function_27_B03F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B0F6")

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
            "I am committed too... Or\x01",
            "perhaps I should say I'll do\x01",
            "my best as a committed lady!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B0F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B178")

    ChrTalk(
        0xFE,
        (
            "Actually I'm full of anxiety,\x01",
            "but seeing Southwark's face\x01",
            "calms me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, what a mysterious\x01",
            "feeling.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B22F")

    ChrTalk(
        0xFE,
        (
            "Southwark is saying\x01",
            "he'll stay behind in\x01",
            "Crossbell because of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the situation, I'd never\x01",
            "tell him to do something like\x01",
            "that, but I happy to hear that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B2D3")

    ChrTalk(
        0xFE,
        (
            "...No matter how much I try to,\x01",
            "I can't forget the fear I felt\x01",
            "when Arc-en-Ciel was attacked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, what was the\x01",
            "criminal trying to\x01",
            "achieve?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B2D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B42D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3BB")

    ChrTalk(
        0xFE,
        (
            "I'm planning on seeing the long-\x01",
            "awaited Arc-en-Ciel renewal\x01",
            "performance after work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone has been\x01",
            "looking forward to it\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll try not to miss\x01",
            "even a single moment of\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B428")

    label("loc_B3BB")


    ChrTalk(
        0xFE,
        (
            "Everyone has been\x01",
            "looking forward to it\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll try not to miss\x01",
            "even a single moment of\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B428")

    Jump("loc_B962")

    label("loc_B42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B4D4")

    ChrTalk(
        0xFE,
        (
            "Tomorrow is opening day of Arc-\x01",
            "en-Ciel's "Golden Sun, Silver\x01",
            "Moon" renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to see it with\x01",
            "Southwark. Oh, I can't\x01",
            "wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B547")

    ChrTalk(
        0xFE,
        (
            "A-A lot of ambulances\x01",
            "went by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "patients being taken to\x01",
            "the hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B5FC")

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
        (
            "Oh, that's right. I'll\x01",
            "have Southwark explain\x01",
            "it to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B60A")
    Jump("loc_B962")

    label("loc_B60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B71F")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I thought\x01",
            "yesterday went very\x01",
            "well, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Cynthia is really charming.\x01",
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
    Jump("loc_B76D")

    label("loc_B71F")


    ChrTalk(
        0xFE,
        (
            "*sob*... I wonder if\x01",
            "there's anyone out there\x01",
            "who understands my charms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B76D")

    Jump("loc_B962")

    label("loc_B772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B7F3")

    ChrTalk(
        0xFE,
        (
            "The western clothes are\x01",
            "ready and my makeup is\x01",
            "perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I'm going to be a\x01",
            "bit different tonight㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B962")

    label("loc_B7F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B890")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, some active\x01",
            "guests will be there\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How long has it been since\x01",
            "the last mixer? Evening\x01",
            "can't come soon enough!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B903")

    label("loc_B890")


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
        (
            "This is my chance! My\x01",
            "ultimate chance!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B903")

    Jump("loc_B962")

    label("loc_B908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B916")
    Jump("loc_B962")

    label("loc_B916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B959")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B931")
    Call(0, 21)
    Jump("loc_B954")

    label("loc_B931")


    ChrTalk(
        0xFE,
        (
            "*sigh*, Southwark is so\x01",
            "mean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B954")

    Jump("loc_B962")

    label("loc_B959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B962")

    label("loc_B962")

    TalkEnd(0xFE)
    Return()

    # Function_27_B03F end

    def Function_28_B966(): pass

    label("Function_28_B966")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B9FB")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking of\x01",
            "stepping outside, that thing\x01",
            "appeared from out of thin air...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What in the world is\x01",
            "going on!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_B9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BA09")
    Jump("loc_C2A5")

    label("loc_BA09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BA93")

    ChrTalk(
        0xFE,
        (
            "I-I don't really get it,\x01",
            "but is this what they\x01",
            "call war?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't bear this\x01",
            "anxiety, but... Ken,\x01",
            "I'll protect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BA93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BB1D")

    ChrTalk(
        0xFE,
        (
            "I've had a few days off,\x01",
            "but I've resumed\x01",
            "shopping today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're looking for\x01",
            "bargains so as to avoid\x01",
            "overspending.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BB1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BBC4")

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
    Jump("loc_C2A5")

    label("loc_BBC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC77")

    ChrTalk(
        0xFE,
        (
            "A train accident. How\x01",
            "unsettling. But I'm glad service\x01",
            "was restored so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because if trade routes\x01",
            "closed down, I wouldn't be\x01",
            "able to shop like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BC77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BCDD")

    ChrTalk(
        0xFE,
        (
            "Looks like there's an uproar\x01",
            "over something. Maybe I\x01",
            "should head home early today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BCDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BDBF")

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
            "Well for now, I'll leave the\x01",
            "complicated discussions to my husband.\x01",
            "I just want to enjoy shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BDBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BE3E")

    ChrTalk(
        0xFE,
        (
            "My, they've added new\x01",
            "goods, haven't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's par for the\x01",
            "course for Times\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BE3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BED3")

    ChrTalk(
        0xFE,
        (
            "This is the day of the\x01",
            "trade conference, isn't\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though I can't attend it\x01",
            "directly, I can't help\x01",
            "but be concerned over it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_BFAA")

    ChrTalk(
        0xFE,
        "Listen, Ken.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as we get back, first tell\x01",
            "your dad you're sorry. Then, let's\x01",
            "hug him without a moment's delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine. If we both\x01",
            "sandwich him, there won't\x01",
            "be anything to fear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2A5")

    label("loc_BFAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C0B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C02C")

    ChrTalk(
        0xFE,
        (
            "That unveiling ceremony\x01",
            "earlier was amazing.\x02",
        )
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
    Jump("loc_C0AE")

    label("loc_C02C")


    ChrTalk(
        0xFE,
        (
            "It's right after payday,\x01",
            "and that money is burning\x01",
            "a hole in my wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to take my\x01",
            "time looking around\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0AE")

    Jump("loc_C2A5")

    label("loc_C0B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C14F")

    ChrTalk(
        0xFE,
        (
            "I always think this, but\x01",
            "people who think about\x01",
            "goods are amazing.\x02",
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
    Jump("loc_C2A5")

    label("loc_C14F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1E6")

    ChrTalk(
        0xFE,
        (
            "Compared to when I was\x01",
            "shopping with him before, Ken\x01",
            "has fewer complaints lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This must be love. Mom's\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C224")

    label("loc_C1E6")


    ChrTalk(
        0xFE,
        (
            "This must be what\x01",
            "happiness means to\x01",
            "mothers with a son.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C224")

    Jump("loc_C2A5")

    label("loc_C229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C2A5")

    ChrTalk(
        0xFE,
        "Hm, hm-hmm♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter when I come here or for\x01",
            "how long, I never lose interest\x01",
            "in this department store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2A5")

    TalkEnd(0xFE)
    Return()

    # Function_28_B966 end

    def Function_29_C2A9(): pass

    label("Function_29_C2A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C33B")

    ChrTalk(
        0xFE,
        (
            "To think a tree grew right out of thin\x01",
            "air. What could be the theory behind such\x01",
            "a thing? Am I dreaming? Is it an illusion?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C349")
    Jump("loc_CD84")

    label("loc_C349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C363")

    ChrTalk(
        0xFE,
        "Mom...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3BD")

    ChrTalk(
        0xFE,
        (
            "Mom is really tough. I\x01",
            "don't really get it, but\x01",
            "I'm encouraged by her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C444")

    ChrTalk(
        0xFE,
        (
            "My mom isn't in her\x01",
            "usual carefree mood\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she's thinking about\x01",
            "Mainz, I suppose that's\x01",
            "understandable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C4EC")

    ChrTalk(
        0xFE,
        (
            "Mom's shopping passion\x01",
            "is as steady as this\x01",
            "rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is fine, but whenever I go\x01",
            "shopping with her in heavy rain,\x01",
            "I end up completely soaked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C5EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58C")

    ChrTalk(
        0xFE,
        (
            "Those ambulance sirens\x01",
            "are extremely loud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet they'd be even\x01",
            "more annoying close up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do the drivers wear\x01",
            "earplugs?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C5EA")

    label("loc_C58C")


    ChrTalk(
        0xFE,
        (
            "Those ambulance sirens\x01",
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

    label("loc_C5EA")

    Jump("loc_CD84")

    label("loc_C5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C689")

    ChrTalk(
        0xFE,
        (
            "If everyone was as\x01",
            "positive as my mom, we'd\x01",
            "all be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But in that case, we'd\x01",
            "be annexed by the Empire\x01",
            "in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76D")

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "kill time today by\x01",
            "people watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, the general\x01",
            "store guy and the information desk\x01",
            "lady have been awfully close lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, could this be...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C7E1")

    label("loc_C76D")


    ChrTalk(
        0xFE,
        (
            "The general store guy and the\x01",
            "information desk lady have\x01",
            "been awfully close lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, could this be...\x02",
    )

    CloseMessageWindow()

    label("loc_C7E1")

    Jump("loc_CD84")

    label("loc_C7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C8EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C87E")

    ChrTalk(
        0xFE,
        (
            "My mom's "operation\x01",
            "apology" yesterday was a\x01",
            "smashing success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That hug, and those\x01",
            "tears... My mom was\x01",
            "incredible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C8E5")

    label("loc_C87E")


    ChrTalk(
        0xFE,
        (
            "Dad was totally taken in\x01",
            "by my mom's hug and\x01",
            "tears.\x02",
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

    label("loc_C8E5")

    Jump("loc_CD84")

    label("loc_C8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C966")

    ChrTalk(
        0xFE,
        (
            "Because mom was absorbed\x01",
            "in her shopping, it's\x01",
            "gotten this late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think dad's going to\x01",
            "be angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_C966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CA9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA28")

    ChrTalk(
        0xFE,
        (
            "That unveiling ceremony\x01",
            "was spectacle itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, my mom seems a\x01",
            "little down for some\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she doesn't buy\x01",
            "anything we don't need,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CA98")

    label("loc_CA28")


    ChrTalk(
        0xFE,
        (
            "My mom's eye color is a\x01",
            "little different today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she doesn't buy\x01",
            "anything we don't need,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA98")

    Jump("loc_CD84")

    label("loc_CA9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CB4F")

    ChrTalk(
        0xFE,
        (
            "I always think this, but\x01",
            "people who think about\x01",
            "products have it tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They have to think of new\x01",
            "things to pull in customers\x01",
            "like my mom, day after day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_CB4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CC8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC1A")

    ChrTalk(
        0xFE,
        (
            "I devised a way of\x01",
            "killing time I like to\x01",
            "call people watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because all different kinds of people\x01",
            "come to this department store.\x01",
            "Surprisingly, it never gets old.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_CC85")

    label("loc_CC1A")


    ChrTalk(
        0xFE,
        (
            "Because all different kinds of people\x01",
            "come to this department store.\x01",
            "Surprisingly, it never gets old.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC85")

    Jump("loc_CD84")

    label("loc_CC8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CD84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD13")

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
            "I looks like he went up\x01",
            "to the roof just now,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD84")

    label("loc_CD13")


    ChrTalk(
        0xFE,
        (
            "Going window shopping\x01",
            "with my mom is my daily\x01",
            "routine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm used to it, but it's\x01",
            "the height of boredom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD84")

    TalkEnd(0xFE)
    Return()

    # Function_29_C2A9 end

    def Function_30_CD88(): pass

    label("Function_30_CD88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CE5B")

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
    Jump("loc_D7E1")

    label("loc_CE5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CE69")
    Jump("loc_D7E1")

    label("loc_CE69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CEA2")

    ChrTalk(
        0xFE,
        (
            "Hmmm... This is an\x01",
            "unusual situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_CEA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CF88")

    ChrTalk(
        0xFE,
        (
            "Now, the question of whether we should\x01",
            "abandon independence and believe in the major\x01",
            "powers is a different question entirely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Either way, the military\x01",
            "threat from each of them are\x01",
            "problems we can't ignore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_CF88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D08E")

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
            "For example, the Empire's railway\x01",
            "cannons... Would we capitulate after\x01",
            "taking just a single shot from them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D08E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D116")

    ChrTalk(
        0xFE,
        (
            "I heard about an ogre-\x01",
            "like monster, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the first time I've\x01",
            "heard such a mysterious\x01",
            "tale in my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D162")

    ChrTalk(
        0xFE,
        (
            "It's noisy outside. I\x01",
            "wonder just what exactly\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D1F8")

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm thinking about\x01",
            "my next gift to my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gave her a brooch\x01",
            "before... I was thinking of\x01",
            "going with a ring this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D29E")

    ChrTalk(
        0xFE,
        (
            "I didn't think I'd hear\x01",
            "the word "independence"\x01",
            "at my age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be great if it were\x01",
            "possible, but I don't think\x01",
            "it'll go that smoothly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D358")

    ChrTalk(
        0xFE,
        (
            "Hmm, the problems at the\x01",
            "conference are going to be\x01",
            "Osborne and Rocksmith...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of plan the\x01",
            "mayor has for dealing with the\x01",
            "audacity of those men.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_D3BE")

    ChrTalk(
        0xFE,
        (
            "Well then, time to go\x01",
            "back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would be no match for\x01",
            "my angered old lady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D47B")

    ChrTalk(
        0xFE,
        (
            "Hoho, the roof of this\x01",
            "place is the best spot from\x01",
            "which to see the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't forget the fire its\x01",
            "magnificent form lit in my eyes\x01",
            "the moment that curtain fell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D5DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D53B")

    ChrTalk(
        0xFE,
        (
            "The trade conference\x01",
            "finally opens tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was shocked when Mayor\x01",
            "Crois first proposed it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe it's\x01",
            "actually going to be\x01",
            "held.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D5D9")

    label("loc_D53B")


    ChrTalk(
        0xFE,
        (
            "I can't believe the trade\x01",
            "conference is actually\x01",
            "going to be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was probably able to do\x01",
            "it because he's both the IBC\x01",
            "President and the mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5D9")

    Jump("loc_D7E1")

    label("loc_D5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D676")

    ChrTalk(
        0xFE,
        (
            "Hmm. I'm always impressed\x01",
            "whenever I see this\x01",
            "store's lineup of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder which I should\x01",
            "choose as a present for\x01",
            "my wife.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7E1")

    label("loc_D676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D7E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D76F")

    ChrTalk(
        0xFE,
        (
            "Hmm, but even so, I'm amazed\x01",
            "at Mayor Crois' and Chairman\x01",
            "MacDowell's actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially the chairman.\x01",
            "He's almost my age, and\x01",
            "yet he works so hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, this must be what\x01",
            "it means to be old and\x01",
            "active.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D7E1")

    label("loc_D76F")


    ChrTalk(
        0xFE,
        (
            "Hoho, this must be what\x01",
            "it means to be old and\x01",
            "active.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chairman MacDowell is\x01",
            "the star of my\x01",
            "generation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7E1")

    TalkEnd(0xFE)
    Return()

    # Function_30_CD88 end

    def Function_31_D7E5(): pass

    label("Function_31_D7E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D7F6")
    Jump("loc_DA0A")

    label("loc_D7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D88B")

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
            "*sigh*... Honestly, I\x01",
            "really have to go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA0A")

    label("loc_D88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D92F")

    ChrTalk(
        0xFE,
        (
            "I'm told that we won't pay\x01",
            "tax to the Empire or Republic\x01",
            "if we declare independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, if Mr. Dieter\x01",
            "says it, can it really\x01",
            "be wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA0A")

    label("loc_D92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D989")

    ChrTalk(
        0xFE,
        (
            "A service for rainy days?\x01",
            "This department store\x01",
            "sure is sophisticated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA0A")

    label("loc_D989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DA0A")

    ChrTalk(
        0xFE,
        (
            "Homework? I don't have\x01",
            "time for that kind of\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way... It\x01",
            "seems Arios is away\x01",
            "again, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA0A")

    TalkEnd(0xFE)
    Return()

    # Function_31_D7E5 end

    def Function_32_DA0E(): pass

    label("Function_32_DA0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DA1F")
    Jump("loc_DB88")

    label("loc_DA1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DA9E")

    ChrTalk(
        0xFE,
        (
            "But, the situation being\x01",
            "what it is, it'll be the\x01",
            "same wherever we go, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I miss my family, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB88")

    label("loc_DA9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DB1B")

    ChrTalk(
        0xFE,
        (
            "Lately, all the adults are\x01",
            "shouting "independence,\x01",
            "independence", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What do they mean,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB88")

    label("loc_DB1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DB88")

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
            "I served him before.\x01",
            "That's kind of amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB88")

    TalkEnd(0xFE)
    Return()

    # Function_32_DA0E end

    def Function_33_DB8C(): pass

    label("Function_33_DB8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBA1")
    Call(0, 36)
    Jump("loc_DC25")

    label("loc_DBA1")


    ChrTalk(
        0xFE,
        (
            "Hmm? Oh, it's you guys,\x01",
            "the police's What's-It-\x01",
            "Called Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, get out of here.\x01",
            "Don't act like you know\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC25")

    TalkEnd(0xFE)
    Return()

    # Function_33_DB8C end

    def Function_34_DC29(): pass

    label("Function_34_DC29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC3E")
    Call(0, 36)
    Jump("loc_DCDE")

    label("loc_DC3E")


    ChrTalk(
        0xFE,
        (
            "Aww, man. Just when I got back\x01",
            "from my trip, I wanted something\x01",
            "a little more exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, should we try\x01",
            "going to that shady\x01",
            "store on Back Street?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCDE")

    TalkEnd(0xFE)
    Return()

    # Function_34_DC29 end

    def Function_35_DCE2(): pass

    label("Function_35_DCE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCF7")
    Call(0, 36)
    Jump("loc_DD68")

    label("loc_DCF7")


    ChrTalk(
        0xFE,
        (
            "Yeah, yeah. Let's go to\x01",
            "the orbal store after\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to tune up the\x01",
            "car as much as possible\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD68")

    TalkEnd(0xFE)
    Return()

    # Function_35_DCE2 end

    def Function_36_DD6C(): pass

    label("Function_36_DD6C")

    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)

    ChrTalk(
        0x17,
        (
            "Man... For a trade city,\x01",
            "this department store's\x01",
            "no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Yeah, they have hardly\x01",
            "anything that matches my\x01",
            "glasses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well they have a lot of\x01",
            "goods for commoners.\x01",
            "What did you expect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'll just buy a beer and\x01",
            "go.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE87")
    Jump("loc_DF32")

    label("loc_DE87")


    ChrTalk(
        0x104,
        (
            "#00301F(Oh, so those guys are\x01",
            "just your usual brats,\x01",
            "eh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(So they even hang out\x01",
            "here, do they...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...Well, let's leave\x01",
            "them alone for now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF32")

    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_36_DD6C end

    def Function_37_DF47(): pass

    label("Function_37_DF47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DFB1")

    ChrTalk(
        0xFE,
        (
            "I ran out of candy at\x01",
            "home so I rushed here to\x01",
            "buy some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm such a birdbrain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E02C")

    label("loc_DFB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E02C")

    ChrTalk(
        0xFE,
        (
            "I've got to stock up on\x01",
            "candy while I have the\x01",
            "time㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be a problem if I\x01",
            "ran out at the wrong\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E02C")

    TalkEnd(0xFE)
    Return()

    # Function_37_DF47 end

    def Function_38_E030(): pass

    label("Function_38_E030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E103")

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
            "refreshments to Xilun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_E103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E111")
    Jump("loc_EB7F")

    label("loc_E111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E1D2")

    ChrTalk(
        0xFE,
        (
            "Mysterious accidents, huh? I\x01",
            "did get the feeling they were\x01",
            "those kinds of accidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We also bear the sin for\x01",
            "having overlooked them... It's\x01",
            "just as the President said.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_E1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E272")

    ChrTalk(
        0xFE,
        (
            "Though it's only\x01",
            "natural... St. Ursula\x01",
            "Hospital looks very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Xilun seems calm, but I\x01",
            "feel worthless, not being\x01",
            "able to do anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_E272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E3E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E348")

    ChrTalk(
        0xFE,
        (
            "W-What's with the attack\x01",
            "on Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard CGF are being taken\x01",
            "to the hospital one after the\x01",
            "next since yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, why do such\x01",
            "worthless idiots have to\x01",
            "exist?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_E3DB")

    label("loc_E348")


    ChrTalk(
        0xFE,
        (
            "I heard CGF are being taken\x01",
            "to the hospital one after the\x01",
            "next since yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, why do such\x01",
            "worthless idiots have to\x01",
            "exist?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3DB")

    Jump("loc_EB7F")

    label("loc_E3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E4B6")

    ChrTalk(
        0xFE,
        (
            "Some of the train accident victims\x01",
            "were severely wounded, but... it\x01",
            "seems everyone survived it.\x02",
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
    Jump("loc_EB7F")

    label("loc_E4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E500")

    ChrTalk(
        0xFE,
        (
            "W-What? An ambulance...?\x01",
            "And quite a lot of them,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_E500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E599")

    ChrTalk(
        0xFE,
        (
            "Hmm, now what does my\x01",
            "family want today?\x02",
        )
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
    Jump("loc_EB7F")

    label("loc_E599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6E8")

    ChrTalk(
        0xFE,
        (
            "Xilun suggested I become a\x01",
            "male nurse. I'll have to\x01",
            "think seriously about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I have to wait for\x01",
            "next year's exam, I already\x01",
            "did well on a practice exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, I'm planning on\x01",
            "taking next year's\x01",
            "residency exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It makes me feel at ease\x01",
            "when I think there's not\x01",
            "just one path.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_E782")

    label("loc_E6E8")


    ChrTalk(
        0xFE,
        (
            "If you just stay positive\x01",
            "and do your best, you can\x01",
            "master anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Studying is somehow more\x01",
            "fun than it was before.\x01",
            "...Just a little, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E782")

    Jump("loc_EB7F")

    label("loc_E787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E795")
    Jump("loc_EB7F")

    label("loc_E795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E7A3")
    Jump("loc_EB7F")

    label("loc_E7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E878")

    ChrTalk(
        0xFE,
        (
            "Everyone is happy due to the\x01",
            "unveiling ceremony, but... My\x01",
            "heart is down in the dumps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On that point, I'm jealous of Xilun's\x01",
            "carefree personality. She doesn't\x01",
            "think of her siblings at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_E878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E95B")

    ChrTalk(
        0xFE,
        (
            "For the next year, I'll live\x01",
            "the life of a ronin (student\x01",
            "who failed an entrance exam).\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And lately, the stares of my family\x01",
            "have been getting colder and colder...\x01",
            "Ah, what am I going to do with my life?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_E95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_EA30")

    ChrTalk(
        0xFE,
        (
            "Hmm, for today's shopping, I\x01",
            "need black pepper, mustard\x01",
            "sauce and olive oil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, I can't remember what I'm supposed\x01",
            "to get without a list! I'm trying this\x01",
            "as a way to improve my memory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7F")

    label("loc_EA30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EB7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB0E")

    ChrTalk(
        0xFE,
        (
            "I failed the St. Ursula\x01",
            "Medical School entrance\x01",
            "exam again this year.\x02",
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
    Jump("loc_EB7F")

    label("loc_EB0E")


    ChrTalk(
        0xFE,
        (
            "And now my worthless\x01",
            "self is just the dinner\x01",
            "ingredients gofer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I'm no good. No\x01",
            "good at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB7F")

    TalkEnd(0xFE)
    Return()

    # Function_38_E030 end

    def Function_39_EB83(): pass

    label("Function_39_EB83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_EC61")

    ChrTalk(
        0xFE,
        (
            "I really want a large\x01",
            "Mishy doll, but they\x01",
            "sure are expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I pool my spending money and go for the\x01",
            "large one, or should I go for the convenient\x01",
            "small one right now... Hmm, what to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECE9")

    label("loc_EC61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_ECE9")

    ChrTalk(
        0xFE,
        (
            "Wow, so they really do\x01",
            "have a Mishy corner at\x01",
            "the general goods store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-Now I don't have to\x01",
            "look all over for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECE9")

    TalkEnd(0xFE)
    Return()

    # Function_39_EB83 end

    def Function_40_ECED(): pass

    label("Function_40_ECED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_ED76")

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "buy a souvenir and then\x01",
            "head for the airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, but this was a very\x01",
            "productive trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE96")

    label("loc_ED76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_ED84")
    Jump("loc_EE96")

    label("loc_ED84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EDF4")

    ChrTalk(
        0xFE,
        (
            "Man, the unveiling\x01",
            "ceremony was more\x01",
            "amazing than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's Crossbell for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE96")

    label("loc_EDF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EE96")

    ChrTalk(
        0xFE,
        (
            "Man, Crossbell is such a\x01",
            "nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow is the Orchis Tower unveiling\x01",
            "ceremony. This trip looks like it's\x01",
            "going to be a lot of fun, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE96")

    TalkEnd(0xFE)
    Return()

    # Function_40_ECED end

    def Function_41_EE9A(): pass

    label("Function_41_EE9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_EEF6")

    ChrTalk(
        0xFE,
        (
            "Aww, why'd this trip\x01",
            "have to end? It was over\x01",
            "in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F00E")

    label("loc_EEF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_EF04")
    Jump("loc_F00E")

    label("loc_EF04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EF97")

    ChrTalk(
        0xFE,
        (
            "I saw the unveiling ceremony\x01",
            "from this store's roof. It\x01",
            "was a really good spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm glad I\x01",
            "researched it\x01",
            "beforehand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F00E")

    label("loc_EF97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F00E")

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
        (
            "No matter how many times\x01",
            "I come, I never get\x01",
            "tired of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F00E")

    TalkEnd(0xFE)
    Return()

    # Function_41_EE9A end

    def Function_42_F012(): pass

    label("Function_42_F012")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0EA")

    ChrTalk(
        0xFE,
        (
            "Hmm, Manager Neston's\x01",
            "words are full of\x01",
            "meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am still inexperienced\x01",
            "as both a businessman\x01",
            "and a merchant...\x02",
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
    Jump("loc_F177")

    label("loc_F0EA")


    ChrTalk(
        0xFE,
        (
            "I am still inexperienced\x01",
            "as both a businessman\x01",
            "and a merchant...\x02",
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

    label("loc_F177")

    TalkEnd(0xFE)
    Return()

    # Function_42_F012 end

    def Function_43_F17B(): pass

    label("Function_43_F17B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I want to buy a few\x01",
            "things for tonight's\x01",
            "dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's noisy outside... I\x01",
            "wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_F17B end

    def Function_44_F1EB(): pass

    label("Function_44_F1EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F2BB")

    ChrTalk(
        0xFE,
        (
            "I'm told there's a high chance\x01",
            "terrorists will attack the trade\x01",
            "conference's main session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, man oh man... If they\x01",
            "really do attack, I wonder if\x01",
            "we'll be able to handle them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F912")

    label("loc_F2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F3D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F36C")

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
            "I'm too busy to count\x01",
            "the number of beautiful\x01",
            "women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Hmm, same old Raymond,\x01",
            "I guess.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_F3D4")

    label("loc_F36C")


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
            "I'm too busy to count\x01",
            "the number of beautiful\x01",
            "women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3D4")

    Jump("loc_F912")

    label("loc_F3D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F565")

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
        (
            "...Which of us is really\x01",
            "lost, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I'm touring Crossbell\x01",
            "right now.\x02",
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
            "That's a support request\x01",
            "too, I guess. The Support\x01",
            "Section's work sounds tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, it's not that bad.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_F5E3")

    label("loc_F565")


    ChrTalk(
        0xFE,
        (
            "Anyway, this is the\x01",
            "first day the security\x01",
            "structure's in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't fly off the rails.\x01",
            "Everything in\x01",
            "moderation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5E3")

    Jump("loc_F912")

    label("loc_F5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7EC")

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
            "#00100FDoes your being here\x01",
            "mean you're in charge of\x01",
            "the department store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Strictly speaking it's the\x01",
            "Central Square commerce\x01",
            "facilities I'm responsible for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a lot of pretty\x01",
            "ladies here, so I'm\x01",
            "managing to stay alert.\x02",
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
            "#10106F(Hmm, what an impure\x01",
            "motive.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F(Haha, well I think it's\x01",
            "fine as long as he's\x01",
            "staying alert somehow.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_F912")

    label("loc_F7EC")


    ChrTalk(
        0xFE,
        (
            "Guard duty gives you stiff\x01",
            "shoulders. When I see a pretty lady\x01",
            "though, my fatigue just flies away~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Up until now there's been 31\x01",
            "pretty ladies... I think I\x01",
            "can still expect a few more.\x02",
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

    label("loc_F912")

    TalkEnd(0xFE)
    Return()

    # Function_44_F1EB end

    def Function_45_F916(): pass

    label("Function_45_F916")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92B")
    Call(0, 46)
    Jump("loc_F98C")

    label("loc_F92B")


    ChrTalk(
        0x21,
        (
            "#00603FI'm going to try on\x01",
            "these shoes I ordered.\x02\x03",
            "#00600FI'll have you stay out\x01",
            "of my way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F98C")

    TalkEnd(0xFE)
    Return()

    # Function_45_F916 end

    def Function_46_F990(): pass

    label("Function_46_F990")

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
        (
            "#11P#00602FHmm, then allow me to\x01",
            "try them on\x01",
            "immediately...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    ChrTalk(
        0x21,
        (
            "#11P#00600FG-Guys. What are you\x01",
            "doing here?\x02",
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
            "#6P#00306FWe should be asking you\x01",
            "that question.\x02",
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
            "#11P#00603FHmph, don't lump me in\x01",
            "with people who care\x01",
            "about brands.\x02\x03",
            "#00602FThese are order-made.\x02",
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
            "#00003FI wear basically just\x01",
            "sneakers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "#11P#00601F...Bannings. What are\x01",
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
            "#11P#00600FIt's almost like you're\x01",
            "trying to say leather\x01",
            "shoes are stupid.\x02\x03",
            "#00603FBut... That's where\x01",
            "you're wrong.\x02",
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
            "#11P#00602FShoe leather is a deep and complicated\x01",
            "subject.\x02\x03",
            "#00604FThe more you wear them the more familiar\x01",
            "they are. If you maintain them properly,\x01",
            "the feeling gains more depth...\x02\x03",
            "#00601FAre you saying sneakers can deliver that\x01",
            "kind of pleasure?\x02",
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
        (
            "#6P#00206FI feel like things have\x01",
            "heated up for some\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FI agree. I didn't expect\x01",
            "this at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00606FA-Ahem... It seems we've\x01",
            "gotten off track.\x02\x03",
            "#00600FAnyway, I'm here because I\x01",
            "just happened to have some\x01",
            "free time.\x02\x03",
            "I have another appointment\x01",
            "after this, of course. I'll\x01",
            "have you stay out of my way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FU-Understood.\x02",
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

    # Function_46_F990 end

    def Function_47_10181(): pass

    label("Function_47_10181")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10209")

    ChrTalk(
        0x1B,
        (
            "#02106FYeah, yeah, I know\x01",
            "already.\x02\x03",
            "#02109FAnyway, I can't do without\x01",
            "this manufacturer's pen\x01",
            "they have here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_1027F")

    label("loc_10209")


    ChrTalk(
        0x1B,
        (
            "#02105FWow, Reinford has\x01",
            "strengthened their lineup\x01",
            "with these new model.\x02\x03",
            "#02109FHmm, should I try this\x01",
            "one out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1027F")

    TalkEnd(0xFE)
    Return()

    # Function_47_10181 end

    def Function_48_10283(): pass

    label("Function_48_10283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1037F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102EB")

    ChrTalk(
        0xFE,
        (
            "Grace! Please hurry and\x01",
            "finish!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why are you going so\x01",
            "slow!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x2, 0)
    Jump("loc_1037A")

    label("loc_102EB")


    ChrTalk(
        0xFE,
        (
            "*sigh*, why'd we have to\x01",
            "go shopping because you\x01",
            "suddenly ran out of ink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's not that much\x01",
            "time left, so I'm kind\x01",
            "of worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1037A")

    Jump("loc_10485")

    label("loc_1037F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10429")

    ChrTalk(
        0xFE,
        (
            "Umm, restorative,\x01",
            "antidote... We also need\x01",
            "smelling salts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Looks like he's\x01",
            "preparing a medkit...\x01",
            "Where could he be going?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_10485")

    label("loc_10429")


    ChrTalk(
        0xFE,
        (
            "EP Charge... Nope, don't\x01",
            "need those I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just the Smoke Balls to\x01",
            "go, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10485")

    TalkEnd(0xFE)
    Return()

    # Function_48_10283 end

    def Function_49_10489(): pass

    label("Function_49_10489")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F Boutique "Lucca"\x01",
            "2F Hanson's Shoes\x01",
            "2F Baker's Accessories\x01",
            "1F Region Foods\x01",
            "1F Southwark's General Goods Corner\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※If you have any questions,\x01",
            "please feel free to ask at\x01",
            "the information desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_49_10489 end

    def Function_50_1057E(): pass

    label("Function_50_1057E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-15210, 1000, 9790, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10605")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x104, -14350, 0, 8000, 0)
    Jump("loc_106A4")

    label("loc_10605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10657")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x109, -14350, 0, 8000, 0)
    Jump("loc_106A4")

    label("loc_10657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_106A4")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x105, -14350, 0, 8000, 0)

    label("loc_106A4")

    OP_0D()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PC-Could this be a "Mishy\x01",
            "Doll"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PWhy? This isn't a theme\x01",
            "park...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, this is a recently\x01",
            "created exclusive goods\x01",
            "corner, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FDo you like Mishy,\x01",
            "Shing?\x02",
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
            "Y-You... Are you making\x01",
            "fun of me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "How could one burdened with the\x01",
            "future of Heiyue be interested\x01",
            "in such a thing. How rude!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10929")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1088F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1088F)
    Sleep(50)

    def lambda_1089F():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1089F)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FS-Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FIf you're that angry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FYeah, and we have no\x01",
            "connection with Heiyue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B10")

    label("loc_10929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10A1B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_10982():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10982)
    Sleep(50)

    def lambda_10992():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10992)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FS-Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FIf you're that angry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FYes, and we have no\x01",
            "connection with Heiyue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B10")

    label("loc_10A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10B10")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_10A74():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10A74)
    Sleep(50)

    def lambda_10A84():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10A84)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FS-Shing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FIf you're that angry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FYeah, and we have no\x01",
            "connection with Heiyue,\x01",
            "do we.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B10")

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
            ""Tick-Tock Mishy"?\x02",
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
            "A-Anyway, I want this to\x01",
            "appease me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "And I'm not interested\x01",
            "in it or anything!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10C8C")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_10D39")

    label("loc_10C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10CE5")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_10D39")

    label("loc_10CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10D39")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_10D39")


    ChrTalk(
        0x101,
        (
            "#12P#00012F(H-He's easy to\x01",
            "understand...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F(Yes, it's as if he's\x01",
            "saying he really is\x01",
            "interested.)\x02",
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

    # Function_50_1057E end

    def Function_51_10DDC(): pass

    label("Function_51_10DDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-960, 3000, 1530, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10E68")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x104, 600, 0, 2900, 180)
    Jump("loc_10F07")

    label("loc_10E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10EBA")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x109, 600, 0, 2900, 180)
    Jump("loc_10F07")

    label("loc_10EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10F07")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x105, 600, 0, 2900, 180)

    label("loc_10F07")

    OP_68(-960, 1600, 1530, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow then, we'll head to\x01",
            "the shops, then to the\x01",
            "roof.\x02",
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

    # Function_51_10DDC end

    def Function_52_10FB1(): pass

    label("Function_52_10FB1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17440, 1600, 19460, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1103E")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x104, -15690, 30, 21350, 270)
    Jump("loc_110DD")

    label("loc_1103E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11090")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x109, -15690, 30, 21350, 270)
    Jump("loc_110DD")

    label("loc_11090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_110DD")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x105, -15690, 30, 21350, 270)

    label("loc_110DD")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A2,
        (
            "#12PHey, you've been\x01",
            "whispering stuff for a\x01",
            "while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah. Actually, this is\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11173")

    def lambda_11161():

        label("loc_11161")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_11161")

    QueueWorkItem2(0x104, 1, lambda_11161)
    Jump("loc_111AE")

    label("loc_11173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11193")

    def lambda_11181():

        label("loc_11181")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_11181")

    QueueWorkItem2(0x109, 1, lambda_11181)
    Jump("loc_111AE")

    label("loc_11193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_111AE")

    def lambda_111A1():

        label("loc_111A1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_111A1")

    QueueWorkItem2(0x105, 1, lambda_111A1)

    label("loc_111AE")

    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_111EC")
    EndChrThread(0x104, 0x1)

    def lambda_111CF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111CF)
    Sleep(50)

    def lambda_111DF():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_111DF)
    Jump("loc_11245")

    label("loc_111EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1121B")
    EndChrThread(0x109, 0x1)

    def lambda_111FE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_111FE)
    Sleep(50)

    def lambda_1120E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1120E)
    Jump("loc_11245")

    label("loc_1121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_11245")
    EndChrThread(0x105, 0x1)

    def lambda_1122D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1122D)
    Sleep(50)

    def lambda_1123D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1123D)

    label("loc_11245")

    Sleep(300)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave the "Tick-\x01",
            "Tock Mishy" to Shing.\x07\x00\x02",
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
        (
            "#12PThis is... This store's\x01",
            "limited edition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI see, so that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1134B")

    ChrTalk(
        0x104,
        "#11P#00309FWow, how considerate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_113BF")

    label("loc_1134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1138F")

    ChrTalk(
        0x109,
        (
            "#11P#10109FHaha, you're\x01",
            "considerate, aren't you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113BF")

    label("loc_1138F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_113BF")

    ChrTalk(
        0x105,
        "#11P#10302FHaha, how considerate.\x02",
    )

    CloseMessageWindow()

    label("loc_113BF")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "#12PW-What's with this? What\x01",
            "are you doing giving\x01",
            "this to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha. It's a present.\x01",
            "Nothing more.\x02\x03",
            "Why not accept it? It'll\x01",
            "help you remember\x01",
            "today's tour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PSomething to remember\x01",
            "today by...\x02",
        )
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
            "it's not like you can throw it\x01",
            "away. In that case, I'll take it.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_11600")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_116AD")

    label("loc_11600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_11659")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_116AD")

    label("loc_11659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_116AD")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_116AD")


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

    # Function_52_10FB1 end

    def Function_53_116FC(): pass

    label("Function_53_116FC")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have time to\x01",
            "show him around outside.\x02\x03",
            "We'll head to the shops,\x01",
            "then we'll take him up\x01",
            "on the roof.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -600, 30, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_53_116FC end

    SaveToFile()

Try(main)
