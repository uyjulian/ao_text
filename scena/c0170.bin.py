from ScenarioHelper import *

def main():
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
        "Receptionist Pearl",           # 1
        "Receptionist Cynthia",         # 2
        "Hanson",               # 3
        "Region",               # 4
        "Prada",                 # 5
        "Baker",               # 6
        "Southwark",               # 7
        "Linally",               # 8
        "Pruna",               # 9
        "Neston Manager",         # 10
        "Janetta",             # 11
        "Badgeo",               # 12
        "Dorothe",                 # 13
        "Ken",                   # 14
        "Honest elderly",           # 15
        "Yuri",                 # 16
        "Sykes",               # 17
        "Reggie",                 # 18
        "Priure",                 # 19
        "Grace",               # 20
        "Raines",               # 21
        "Citizen",                   # 22
        "tourist",                 # 23
        "tourist",                 # 24
        "Raymond investigator",       # 25
        "Dudley investigator",         # 26
        "Fernando",           # 27
        "Joanna",             # 28
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
        "Function_7_1C76",         # 07, 7
        "Function_8_1C7A",         # 08, 8
        "Function_9_26A5",         # 09, 9
        "Function_10_28DD",        # 0A, 10
        "Function_11_2A79",        # 0B, 11
        "Function_12_2A98",        # 0C, 12
        "Function_13_3B00",        # 0D, 13
        "Function_14_3B07",        # 0E, 14
        "Function_15_4DA3",        # 0F, 15
        "Function_16_4DA7",        # 10, 16
        "Function_17_5DD1",        # 11, 17
        "Function_18_5DD5",        # 12, 18
        "Function_19_6C7A",        # 13, 19
        "Function_20_6C81",        # 14, 20
        "Function_21_85E9",        # 15, 21
        "Function_22_8739",        # 16, 22
        "Function_23_9AD4",        # 17, 23
        "Function_24_9ED5",        # 18, 24
        "Function_25_A29D",        # 19, 25
        "Function_26_A4FA",        # 1A, 26
        "Function_27_A8B2",        # 1B, 27
        "Function_28_B1CC",        # 1C, 28
        "Function_29_B9EB",        # 1D, 29
        "Function_30_C419",        # 1E, 30
        "Function_31_CD55",        # 1F, 31
        "Function_32_CF45",        # 20, 32
        "Function_33_D0B1",        # 21, 33
        "Function_34_D148",        # 22, 34
        "Function_35_D1E9",        # 23, 35
        "Function_36_D280",        # 24, 36
        "Function_37_D45E",        # 25, 37
        "Function_38_D556",        # 26, 38
        "Function_39_DF64",        # 27, 39
        "Function_40_E095",        # 28, 40
        "Function_41_E219",        # 29, 41
        "Function_42_E35E",        # 2A, 42
        "Function_43_E4DC",        # 2B, 43
        "Function_44_E555",        # 2C, 44
        "Function_45_EB99",        # 2D, 45
        "Function_46_EC17",        # 2E, 46
        "Function_47_F3CC",        # 2F, 47
        "Function_48_F4DB",        # 30, 48
        "Function_49_F6AF",        # 31, 49
        "Function_50_F7C7",        # 32, 50
        "Function_51_10079",       # 33, 51
        "Function_52_10258",       # 34, 52
        "Function_53_10982",       # 35, 53
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
            "　　★　Regionフード・メモ　★\x01",
            "For visitors, refreshing throat\x01",
            "We propose bellyberry juice.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The recipe of berberry juice is written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_DCE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x16)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Bellberry juice\"\x07\x00",
            "I learned the recipe.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(
        0x8,
        (
            "A while ago Scott\x01",
            "He came to show my face,\x01",
            "It seems to be fine for the time being, and it was nothing more than something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Only he\x01",
            "I am doing my best … ….\x01",
            "I hope you do your best not to do it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_101C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB8")
    Call(0, 23)
    Jump("loc_1017")

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")

    ChrTalk(
        0x8,
        (
            "Fortunately, this place for the time being,\x01",
            "In kind of groceries and daily necessities\x01",
            "There is nothing to worry about ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If this situation persists for a long time,\x01",
            "Rather, there is no such accumulation\x01",
            "I am worried about your family and others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Really … the government\x01",
            "What is he thinking?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1017")

    label("loc_FAF")


    ChrTalk(
        0x8,
        (
            "Really … the government\x01",
            "What is he thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Scott also\x01",
            "I hope it is safe ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1017")

    Jump("loc_1C72")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112A")

    ChrTalk(
        0x8,
        (
            "Cynthia-senpai is the next day of referendum\x01",
            "I went back to my hometown of Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Seniors, too\x01",
            "The current situation of the crossbell is\x01",
            "I think that I did not expect it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Family members from before\x01",
            "It seems that it was considerably worried,\x01",
            "It was really nice to be able to return home earlier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E2")

    label("loc_112A")


    ChrTalk(
        0x8,
        (
            "Cynthia-senpai, sure again\x01",
            "I'm back in this department store.\x01",
            "I promised you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am worried about various things from now on ….\x01",
            "Believe in the day we can be together with your seniors\x01",
            "Anyway I will try hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E2")

    Jump("loc_1C72")

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AE")

    ChrTalk(
        0x8,
        (
            "Cynthia-senpai is an administrative district\x01",
            "In the charity event being done\x01",
            "I am participating with help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Besides, anything\x01",
            "They also participate in Miscon.\x01",
            "Let me see the pictures later ♪ ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_130E")

    label("loc_12AE")


    ChrTalk(
        0x8,
        (
            "Cynthia-senpai, whatever\x01",
            "It seems that MISCON will also participate.\x01",
            "Let me see the pictures later ♪ ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130E")

    Jump("loc_1C72")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1399")

    ChrTalk(
        0x8,
        "To occupy the mining town … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For whom and what\x01",
            "I do not know if I planned ….\x01",
            "There is no such thing as permission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_1399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1458")

    ChrTalk(
        0x8,
        (
            "From Scott\x01",
            "Also for the time being, my work is busy\x01",
            "I was told that I could not get in touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But it is a toy.\x01",
            "That is the person of the hoardman\x01",
            "It is because we are going to be together.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14D3")

    label("loc_1458")


    ChrTalk(
        0x8,
        (
            "Because that is about that person\x01",
            "I do not need to worry … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Repeatedly\x01",
            "Do not only do big injuries\x01",
            "I want you to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D3")

    Jump("loc_1C72")

    label("loc_14D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1525")

    ChrTalk(
        0x8,
        (
            "It is a train derailment … …\x01",
            "Is it a vehicle trouble or something …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_1525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15BC")

    ChrTalk(
        0x8,
        (
            "Scott,\x01",
            "Recently somewhat more than ever\x01",
            "It seems I'm getting busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Go for it, Mr. Scott.\x01",
            "I always have it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D7")
    Call(0, 10)
    Jump("loc_1660")

    label("loc_15D7")


    ChrTalk(
        0x8,
        (
            "Oh, everyone\x01",
            "I always use it\x01",
            "The Special Affairs Support Division ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thank you for coming to our store today.\x01",
            "Please, take a moment and go around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1660")

    Jump("loc_1C72")

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_179F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175B")

    ChrTalk(
        0x8,
        (
            "At a dinner party yesterday,\x01",
            "Janettaちゃんが男性を\x01",
            "Three people were calling ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In a talk a little while\x01",
            "All three people's interests to Cynthia seniors\x01",
            "I focused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Janettaちゃん、今日は\x01",
            "I did not feel well, but I wonder if it is okay ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179A")

    label("loc_175B")


    ChrTalk(
        0x8,
        (
            "Janettaちゃん、今日は\x01",
            "I did not feel well, but I wonder if it is okay ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179A")

    Jump("loc_1C72")

    label("loc_179F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_186F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183D")

    ChrTalk(
        0x8,
        (
            "Today at the end of work,\x01",
            "シンシア先輩とJanettaちゃんの\x01",
            "I go to dinner with three people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A dinner party for the first time in a while,\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_186A")

    label("loc_183D")


    ChrTalk(
        0x8,
        (
            "A dinner party for the first time in a while,\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186A")

    Jump("loc_1C72")

    label("loc_186F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188A")
    Call(0, 9)
    Jump("loc_192B")

    label("loc_188A")


    ChrTalk(
        0x8,
        (
            "I have heard from fans before, but,\x01",
            "My seniors are so\x01",
            "It was Yumia's love … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, Cynthia-senpai's\x01",
            "I am also happy to know a new aspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_192B")

    Jump("loc_1C72")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4D")

    ChrTalk(
        0x8,
        (
            "Scott,\x01",
            "I wonder what I am doing now.\x01",
            "I know I'm at work ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, I'm sorry … ___ ___ 0\x01",
            "I have to do something extra while working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is any inconvenience\x01",
            "Please do not hesitate to ask me.\x01",
            "Because I will correspond with integrity sincerity.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AAB")

    label("loc_1A4D")


    ChrTalk(
        0x8,
        (
            "If there is any inconvenience\x01",
            "Please do not hesitate to ask me.\x01",
            "Because I will correspond with integrity sincerity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAB")

    Jump("loc_1C72")

    label("loc_1AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B3A")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "Even on rainy days our shop is of course open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have a nice shopping today too\x01",
            "Please enjoy. (Nicoti)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C72")

    label("loc_1B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C01")

    ChrTalk(
        0x8,
        (
            "We use department store \"Times\"\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "This is general information.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something unclear point\x01",
            "Please do not hesitate to ask us anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C72")

    label("loc_1C01")


    ChrTalk(
        0x8,
        "This is general information.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something unclear point\x01",
            "Please do not hesitate to ask us anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C72")

    TalkEnd(0x8)
    Return()

    # Function_6_DD6 end

    def Function_7_1C76(): pass

    label("Function_7_1C76")

    Call(0, 8)
    Return()

    # Function_7_1C76 end

    def Function_8_1C7A(): pass

    label("Function_8_1C7A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C8B")
    Jump("loc_26A1")

    label("loc_1C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C99")
    Jump("loc_26A1")

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D38")

    ChrTalk(
        0x9,
        (
            "About the identity of the armed group\x01",
            "Although it is said variously,\x01",
            "What is the actual place … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway … for the residents\x01",
            "I pray for no injuries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_1D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DBA")

    ChrTalk(
        0x9,
        (
            "Mr. Pearl and Mr. Scott\x01",
            "He seems to be a childhood friend from a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My childhood friend and fiancee,\x01",
            "I feel like I adore you somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E63")

    ChrTalk(
        0x9,
        (
            "I heard from the manager,\x01",
            "Apparently in the direction of the West Crossbell Highway\x01",
            "I heard that the train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone in the victim,\x01",
            "I hope not to get cherished … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_1E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA7")

    ChrTalk(
        0x9,
        (
            "At this point, discussion on independence gradually\x01",
            "I feel like getting heated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From families in Remiferia\x01",
            "Even though I came back before any problems occurred\x01",
            "I have been told … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cross Bell, for me\x01",
            "It's a second place to call home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tentatively, the referendum\x01",
            "I am going to keep seeing only the other side.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_204E")

    label("loc_1FA7")


    ChrTalk(
        0x9,
        (
            "Whatever you say ……\x01",
            "Cross Bell, for me\x01",
            "It's a second place to call home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Participating in the referendum responsibly,\x01",
            "そのI am going to keep seeing only the other side.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204E")

    Jump("loc_26A1")

    label("loc_2053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206E")
    Call(0, 10)
    Jump("loc_20FB")

    label("loc_206E")


    ChrTalk(
        0x9,
        (
            "Oh … I'm sorry.\x01",
            "I am at work,\x01",
            "I got caught in a talk … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If something else is good\x01",
            "Please do not hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FB")

    Jump("loc_26A1")

    label("loc_2100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C2")

    ChrTalk(
        0x9,
        (
            "まさかJanettaさんが\x01",
            "It is said that he calls a man\x01",
            "I did not think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That you are rich is\x01",
            "I understood well … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, you are tired of being like that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_222E")

    label("loc_21C2")


    ChrTalk(
        0x9,
        (
            "まさかJanettaさんが\x01",
            "It is said that he calls a man\x01",
            "I did not think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, you are tired of being like that.\x02",
    )

    CloseMessageWindow()

    label("loc_222E")

    Jump("loc_26A1")

    label("loc_2233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E2")

    ChrTalk(
        0x9,
        (
            "Janettaさん、\x01",
            "Today bashfully\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apart from going to dinner by three people\x01",
            "It is not the first time … ….\x01",
            "I wonder if you are concerned?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2330")

    label("loc_22E2")


    ChrTalk(
        0x9,
        (
            "Apart from going to dinner by three people\x01",
            "It is not the first time … ….\x01",
            "I wonder if you are concerned?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2330")

    Jump("loc_26A1")

    label("loc_2335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2350")
    Call(0, 9)
    Jump("loc_23E7")

    label("loc_2350")


    ChrTalk(
        0x9,
        (
            "Oh, oh, our guest ……\x01",
            "This was rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Welcome to department store \"Times\" today.\x01",
            "If something else is good\x01",
            "Please call out anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E7")

    Jump("loc_26A1")

    label("loc_23EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24AA")

    ChrTalk(
        0x9,
        (
            "At the commerce meeting starting from tomorrow\x01",
            "Various VIP of participating countries\x01",
            "People are going to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Especially you can come to our shop\x01",
            "Although there is no schedule,\x01",
            "I feel somewhat nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_24AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2532")

    ChrTalk(
        0x9,
        (
            "Mr. Pearl, this place is a fiance\x01",
            "It seems that Mr. Scott could meet regularly\x01",
            "I am very energetic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hehe, it is enviable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26A1")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260C")

    ChrTalk(
        0x9,
        (
            "Rooftop space opened the other day\x01",
            "Have you seen it already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although there are no special facilities,\x01",
            "You can overlook Cros Bell City\x01",
            "It is a superb view spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please drop in if you do not mind.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26A1")

    label("loc_260C")


    ChrTalk(
        0x9,
        (
            "Rooftop space opened the other day\x01",
            "From customers as early as possible\x01",
            "We have received your favorable voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone, relaxation by all means\x01",
            "Why do not you stop by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26A1")

    TalkEnd(0x9)
    Return()

    # Function_8_1C7A end

    def Function_9_26A5(): pass

    label("Function_9_26A5")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        "Pearl, have you heard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently from Libert\x01",
            "That Julia also\x01",
            "She came … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, of course it has been checked.\x01",
            "Once, ask a friend\x01",
            "I also asked for pictures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, well, I wonder if it can be taken well\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It is! It is! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Pearl, that photo\x01",
            "Please give it to me, it is absolute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes.\x01",
            "Of course I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Yulia Associate ……\x01",
            "You are really popular. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F(Yeah, that is to say\x01",
            "That is because he is Associate Professor Julia. )\x02",
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

    # Function_9_26A5 end

    def Function_10_28DD(): pass

    label("Function_10_28DD")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x9,
        (
            "それじゃ、Southwarkさんが\x01",
            "The place I confessed is …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, whatever.\x01",
            "Michelin's fine dining restaurant\x01",
            "It seems to be \"Fortuna\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That, too, ask someone in the shop\x01",
            "I was asked to have a surprise director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Southwarkさんも演出家ですよね〜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, but Geneta-chan\x01",
            "I was really happy to be happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Huhu, I also have to apologize.\x02",
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

    # Function_10_28DD end

    def Function_11_2A79(): pass

    label("Function_11_2A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A94")
    Call(0, 46)
    Jump("loc_2A97")

    label("loc_2A94")

    Call(0, 12)

    label("loc_2A97")

    Return()

    # Function_11_2A79 end

    def Function_12_2A98(): pass

    label("Function_12_2A98")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AFC")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B03")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B22")
    OP_AF(0x26)
    Jump("loc_2B44")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2B32")
    OP_AF(0x25)
    Jump("loc_2B44")

    label("loc_2B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B42")
    OP_AF(0x24)
    Jump("loc_2B44")

    label("loc_2B42")

    OP_AF(0x23)

    label("loc_2B44")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AF7")

    label("loc_2B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B67")
    Jump("loc_3AF7")

    label("loc_2B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C4A")

    ChrTalk(
        0xA,
        (
            "Even if it is difficult to sell imported goods,\x01",
            "There is a custom-made service for us\x01",
            "I have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "From now on more craftsmen will be added\x01",
            "We will provide you with a full service\x01",
            "I will make an effort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(
        0xA,
        (
            "This martial decree is\x01",
            "How long will it last?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even for food items\x01",
            "Those who do not have a store at home\x01",
            "I will not have it for several days … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What you can not see in the past\x01",
            "It is really horror.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E17")

    ChrTalk(
        0xA,
        (
            "Defense army, really crossbell\x01",
            "Can we defend it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I want to believe Arios\x01",
            "Of course there is a … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the two major powers invaded in total,\x01",
            "There is no choice but to surrender to flowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or …\x01",
            "Is there any secret plan?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E97")

    label("loc_2E17")


    ChrTalk(
        0xA,
        (
            "If the two major powers invaded in total,\x01",
            "There is no choice but to surrender to flowing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or …\x01",
            "Is there any secret plan?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E97")

    Jump("loc_3AF7")

    label("loc_2E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F53")

    ChrTalk(
        0xA,
        (
            "The restoration of the city finally\x01",
            "You seem to have come across a section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can not do anything serious … …\x01",
            "At least for some item sale as well\x01",
            "I will return it to everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2FC7")

    ChrTalk(
        0xA,
        (
            "I am in Mainz\x01",
            "The face of our customers is remembered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone, if you are safe\x01",
            "Is it good?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_319C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DB")

    ChrTalk(
        0xA,
        (
            "Yesterday when I heard that the train had stopped\x01",
            "I thought what would happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Started by the guard, station officials\x01",
            "Thanks to everyone's activity, today\x01",
            "It sounds like you've completely recovered completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thanks to you, delivered this morning as well\x01",
            "You can finish without excitement,\x01",
            "I do not have a word of appreciation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3197")

    label("loc_30DB")


    ChrTalk(
        0xA,
        (
            "Transcontinental railroad, as if it was yesterday\x01",
            "As if there were no train accidents\x01",
            "It sounds like you've completely recovered completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He made efforts to restore\x01",
            "To the guards and everyone involved in the station\x01",
            "I do not have a word of appreciation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3197")

    Jump("loc_3AF7")

    label("loc_319C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_31D4")

    ChrTalk(
        0xA,
        "Hmm, it seems like something accident.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_END)), "loc_326C")

    ChrTalk(
        0xA,
        (
            "Mr. Dudley is our regular customer,\x01",
            "I make leather shoes several times a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That passion and commitment for the first time\x01",
            "It is a real genuine enthusiast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326C")

    Jump("loc_3AF7")

    label("loc_3271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_335D")

    ChrTalk(
        0xA,
        (
            "As an encounter between people is a once-in-a-lifetime opportunity,\x01",
            "Also encounter with people and shoes,\x01",
            "I also think that it is a once-in-a-lifetime meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems to be a bit strange,\x01",
            "When viewing the displayed items\x01",
            "I even feel like something to talk about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_335D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33E6")

    ChrTalk(
        0xA,
        "Really good things are not influenced by fashion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I constantly think what I love beyond the times\x01",
            "I want to offer it to everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_33E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_35D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350F")

    ChrTalk(
        0xA,
        (
            "Choosing shoes is better if you go after the evening\x01",
            "Does everyone know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because the person's legs woke up in the morning\x01",
            "Gradually swollen and even in the evening\x01",
            "It will be as large as about 1 Reju at maximum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So, after the evening when the foot becomes the largest\x01",
            "It is said that it is better to choose the size.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35D2")

    label("loc_350F")


    ChrTalk(
        0xA,
        (
            "Actually, since the person's leg got up in the morning\x01",
            "Gradually swollen and even in the evening\x01",
            "It will be as large as about 1 Reju at maximum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So, after the evening when the foot becomes the largest\x01",
            "It is said that it is better to choose the size.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D2")

    Jump("loc_3AF7")

    label("loc_35D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_365F")

    ChrTalk(
        0xA,
        (
            "As leather shoes get caught in,\x01",
            "I am familiar with my feet comfortably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Deep inside the same person,\x01",
            "And it is tasty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_365F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36F1")

    ChrTalk(
        0xA,
        (
            "In our store we also offer items for children\x01",
            "We are enriching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "take your time\x01",
            "Please visit and go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A8")

    label("loc_36F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3801")

    ChrTalk(
        0xA,
        (
            "Pradaさんからよく、以前のように\x01",
            "I am being asked to treat clothes as well ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The world of shoes is\x01",
            "That alone is very deep.\x01",
            "I jumped in and realized again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's why now, without shaking the side\x01",
            "I just want to pursue just about shoes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38A8")

    label("loc_3801")


    ChrTalk(
        0xA,
        (
            "Of course the world of clothes, of course,\x01",
            "The world of shoes is also\x01",
            "That alone is very deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's why now, without shaking the side\x01",
            "I just want to pursue just about shoes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A8")

    Jump("loc_3AF7")

    label("loc_38AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3934")

    ChrTalk(
        0xA,
        (
            "Also at our shop rain shoes\x01",
            "We handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With sudden rain, as soon as I bought it\x01",
            "There are also people who change their clothes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_399C")

    label("loc_3934")


    ChrTalk(
        0xA,
        (
            "Also at our shop rain shoes\x01",
            "We handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you like,\x01",
            "I will have the recommended items.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399C")

    Jump("loc_3AF7")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A56")

    ChrTalk(
        0xA,
        "《Hansonシューズ》へようこそ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have trouble finding products,\x01",
            "Please do not hesitate to consult us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Perfect for customers\x01",
            "I will find you a pair.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AF7")

    label("loc_3A56")


    ChrTalk(
        0xA,
        (
            "In our shop casual, of course,\x01",
            "Formally for trekking\x01",
            "We have all kinds of items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "きっとPerfect for customers\x01",
            "I will find you a pair.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF7")

    Jump("loc_2AA5")

    label("loc_3AFC")

    TalkEnd(0xA)
    Return()

    # Function_12_2A98 end

    def Function_13_3B00(): pass

    label("Function_13_3B00")

    SetScenarioFlags(0x2, 3)
    Call(0, 14)
    Return()

    # Function_13_3B00 end

    def Function_14_3B07(): pass

    label("Function_14_3B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B76")
    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "People in charge …\x01",
            "It looks like it is not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you were shopping,\x01",
            "Please go to the front.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    label("loc_3B76")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D12")

    ChrTalk(
        0x1A2,
        (
            "Indeed, here are the imported ingredients\x01",
            "We handle a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hm, are you putting soy sauce?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Huhu, the boy\x01",
            "I wonder if they come from Toho?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Here also, in the eastern direction\x01",
            "You can definitely satisfy the authentic\x01",
            "I handle a lot of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I want you to put something\x01",
            "If there are demands of products, etc.,\x01",
            "Please say it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Oh, oh … I will think about it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    TalkEnd(0xB)
    Jump("loc_3D8A")

    label("loc_3D12")

    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "If there is customer's request\x01",
            "In Stock you order\x01",
            "Even doing it is possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please feel free to contact us with anything.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)

    label("loc_3D8A")

    Return()

    label("loc_3D8B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DF3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E13")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D9A")

    label("loc_3E13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E27")
    Jump("loc_4D9A")

    label("loc_3E27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3ED0")

    ChrTalk(
        0xB,
        (
            "With a contact with my daughter a while ago\x01",
            "I was able to confirm the safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My daughter also said she brought out the stand immediately,\x01",
            "I have to work hard as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_3ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3F70")

    ChrTalk(
        0xB,
        (
            "Even so ……\x01",
            "My daughter should come to my house properly\x01",
            "Did she evacuate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Since martial law, conductive communication also\x01",
            "The condition which can not be used continues … ….\x01",
            "I am really worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_3F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_40E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405D")

    ChrTalk(
        0xB,
        (
            "The train passing through the crossbell is\x01",
            "From here this morning, I will take full flight\x01",
            "It seems to be limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anything Today is the last\x01",
            "It seems that the railway will be shut down, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In this way, before business\x01",
            "Two characters of the war go across my head.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40DB")

    label("loc_405D")


    ChrTalk(
        0xB,
        (
            "Anything Today is the last\x01",
            "It seems that the railway will be shut down, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In this way, before business\x01",
            "Two characters of the war go across my head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DB")

    Jump("loc_4D9A")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41A8")

    ChrTalk(
        0xB,
        (
            "No matter what happens\x01",
            "The merchant can not be stupid.\x01",
            "Just do my best and just do the work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Welcome to the tired body\x01",
            "How about garlic from the Oread Autonomous Region?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4244")

    label("loc_41A8")


    ChrTalk(
        0xB,
        (
            "Welcome to the tired body\x01",
            "How about garlic from the Oread Autonomous Region?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Olid garlic is large in grain,\x01",
            "Because it is also nutritious, it is best for nourishing tonic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4244")

    Jump("loc_4D9A")

    label("loc_4249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_42BC")

    ChrTalk(
        0xB,
        (
            "The people of Mainz\x01",
            "I wonder what you are doing now ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I hope it will be released as soon as possible ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_42BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43A2")

    ChrTalk(
        0xB,
        (
            "Apparently the guiding railroad within the night\x01",
            "It seems that it was completely restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Thanks to you, today's rail service is also\x01",
            "I was able to receive as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He did restoration work throughout the night\x01",
            "I am grateful to all the guards.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_442E")

    label("loc_43A2")


    ChrTalk(
        0xB,
        (
            "Thanks to you, today's rail service is also\x01",
            "I was able to receive as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He did restoration work throughout the night\x01",
            "I am grateful to all the guards.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442E")

    Jump("loc_4D9A")

    label("loc_4433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_450B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AA")

    ChrTalk(
        0xB,
        (
            "Anything in the west road\x01",
            "I heard that the train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even in a fallen accident\x01",
            "Was there … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4506")

    label("loc_44AA")


    ChrTalk(
        0xB,
        (
            "Anything in the west road\x01",
            "I heard that the train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even in a fallen accident\x01",
            "Was there … ….?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4506")

    Jump("loc_4D9A")

    label("loc_450B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4599")

    ChrTalk(
        0xB,
        (
            "Leave anything for the ingredients,\x01",
            "《Regionフード》へようこそ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Today the green onions of Republic\x01",
            "It is very affordable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4616")

    ChrTalk(
        0xB,
        (
            "Southwark君とJanettaちゃんが\x01",
            "I heard you decided to go out with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hehe, it is enviable that I am romance at work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_469E")

    ChrTalk(
        0xB,
        (
            "Janettaちゃん、\x01",
            "I am worried because I do not feel well today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yesterday it was as good as that,\x01",
            "I wonder what happened …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_469E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4729")

    ChrTalk(
        0xB,
        (
            "Good evening.\x01",
            "《Regionフード》へようこそ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If supper of dinner is not yet,\x01",
            "By all means use the material\x01",
            "Please buy them and go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9A")

    label("loc_4729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_48DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4830")

    ChrTalk(
        0xB,
        (
            "Leave anything for the ingredients,\x01",
            "《Regionフード》へようこそ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From today three days only,\x01",
            "\"Commercial conference set\" is on sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Empire, Kingdom, Principality, Republic,\x01",
            "And this crossbell 's best food ingredients\x01",
            "It's an assortment of lavish sets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48D9")

    label("loc_4830")


    ChrTalk(
        0xB,
        (
            "From today three days only,\x01",
            "\"Commercial conference set\" is on sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Empire, Kingdom, Principality, Republic,\x01",
            "And this crossbell 's best food ingredients\x01",
            "It's an assortment of lavish sets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48D9")

    Jump("loc_4D9A")

    label("loc_48DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A23")

    ChrTalk(
        0xB,
        (
            "The friendly wife's ally,\x01",
            "《Regionフード》へようこそ〜！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you are having trouble arranging tonight,\x01",
            "I will give you advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For example, I just got in this morning\x01",
            "I used fresh fresh herbs\x01",
            "How about soup dishes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, it is used for soup stock\x01",
            "Laurier's leaves are too stewed\x01",
            "Please note that bitterness comes out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A9F")

    label("loc_4A23")


    ChrTalk(
        0xB,
        (
            "If you are having trouble arranging tonight,\x01",
            "I will give you advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the way, today's recommendation\x01",
            "It is a fresh herb soup dish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9F")

    Jump("loc_4D9A")

    label("loc_4AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B85")

    ChrTalk(
        0xB,
        (
            "My daughter recently,\x01",
            "To develop a new menu for juice shops\x01",
            "I am putting my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Today it can not open stalls due to rain,\x01",
            "Studying at home thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhu, you have ambition\x01",
            "It is a wonderful thing, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C0A")

    label("loc_4B85")


    ChrTalk(
        0xB,
        (
            "My daughter recently,\x01",
            "To develop a new menu for juice shops\x01",
            "I am putting my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhu, you have ambition\x01",
            "It is a wonderful thing, is not it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C0A")

    Jump("loc_4D9A")

    label("loc_4C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D14")

    ChrTalk(
        0xB,
        (
            "Leave anything for the ingredients,\x01",
            "《Regionフード》へようこそ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By the way I used the ingredients of my house\x01",
            "I have a healthy juice shop\x01",
            "Thank you for your continued support.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At the juice stand in the province,\x01",
            "My daughter is doing a shop.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D9A")

    label("loc_4D14")


    ChrTalk(
        0xB,
        (
            "Leave anything for the ingredients,\x01",
            "《Regionフード》へようこそ〜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The administrative district using the ingredients of our country\x01",
            "I would also like to ask a juice shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9A")

    Jump("loc_3D95")

    label("loc_4D9F")

    TalkEnd(0xB)
    Return()

    # Function_14_3B07 end

    def Function_15_4DA3(): pass

    label("Function_15_4DA3")

    Call(0, 16)
    Return()

    # Function_15_4DA3 end

    def Function_16_4DA7(): pass

    label("Function_16_4DA7")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DCD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E12")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4E12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E31")
    OP_AF(0x21)
    Jump("loc_4E53")

    label("loc_4E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E41")
    OP_AF(0x20)
    Jump("loc_4E53")

    label("loc_4E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E51")
    OP_AF(0x1F)
    Jump("loc_4E53")

    label("loc_4E51")

    OP_AF(0x1E)

    label("loc_4E53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5DC8")

    label("loc_4E62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E76")
    Jump("loc_5DC8")

    label("loc_4E76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4F55")

    ChrTalk(
        0xC,
        (
            "Someday I thought … ….\x01",
            "On this occasion the original brand\x01",
            "I decided to set it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fix is the food of growth -\x01",
            "Surely you can satisfy\x01",
            "I can create a product!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_4F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507C")

    ChrTalk(
        0xC,
        (
            "The president is bullish,\x01",
            "Everything is that weapon called \"God machine\"\x01",
            "I guess it sounds like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… It is in the city\x01",
            "A monster like that soldier of that armor is\x01",
            "What is it really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Without any notice at all, without such things\x01",
            "To give fear to the people ……\x01",
            "The overwork is also terrible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5134")

    label("loc_507C")


    ChrTalk(
        0xC,
        (
            "…… Even so, I'm in the city.\x01",
            "A monster like that soldier of that armor is\x01",
            "What is it really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Without any notice at all, without such things\x01",
            "To give fear to the people ……\x01",
            "The overwork is also terrible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5134")

    Jump("loc_5DC8")

    label("loc_5139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5207")

    ChrTalk(
        0xC,
        (
            "Is it because you are doing a guest business?\x01",
            "To me, things certainly\x01",
            "I have a habit of drawing one step … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What shall we say ……\x01",
            "What Dieter says is\x01",
            "I heard a quite abusive opinion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52B6")

    ChrTalk(
        0xC,
        (
            "Three days later in each department store official\x01",
            "I will take a break and go to the polling place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, I still have a position\x01",
            "I am trying to decide … ….\x01",
            "What is it, what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_52B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_536B")

    ChrTalk(
        0xC,
        (
            "I do not know how it is an armed group,\x01",
            "I have those people\x01",
            "I can not understand anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To suppress people with violence ……\x01",
            "It is nothing but anything other than foolish bones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_536B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_546D")

    ChrTalk(
        0xC,
        (
            "Recently I do not have a heart or a customer with a smile\x01",
            "I feel like it is decreasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yesterday's train accident is also so,\x01",
            "Considering the situation in this place\x01",
            "I think that there is no impossibility, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At least at the time of shopping\x01",
            "Small things to do\x01",
            "I want you to forget.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_54F8")

    label("loc_546D")


    ChrTalk(
        0xC,
        (
            "Recently I do not have a heart or a customer with a smile\x01",
            "I feel like it is decreasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At least at the time of shopping\x01",
            "Small things to do\x01",
            "I want you to forget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F8")

    Jump("loc_5DC8")

    label("loc_54FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5533")

    ChrTalk(
        0xC,
        "Oh, something outside is noisy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_570E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_564C")

    ChrTalk(
        0xC,
        (
            "In case of going out, etc. to suit your mood\x01",
            "I think it is common to choose clothes,\x01",
            "On the contrary, clothes may decide the mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For example, when depressed,\x01",
            "Please choose a bright clothes on purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That way, I feel depressed\x01",
            "You can even blow it away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5709")

    label("loc_564C")


    ChrTalk(
        0xC,
        (
            "In case of going out, etc. to suit your mood\x01",
            "I think it is common to choose clothes,\x01",
            "On the contrary, clothes may decide the mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Find clothes that match your mood ……\x01",
            "I think that way of choosing it is also ant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5709")

    Jump("loc_5DC8")

    label("loc_570E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57B2")

    ChrTalk(
        0xC,
        (
            "Clothes and bags are expensive\x01",
            "There is a tendency to adhere to invisible places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "There are many things that are tough and long to use,\x01",
            "I think that it is worth the amount.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_57B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5850")

    ChrTalk(
        0xC,
        (
            "Fashion is going to change,\x01",
            "It is something that someone creates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As an owner of a select shop,\x01",
            "I can create a fashion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58A0")

    ChrTalk(
        0xC,
        (
            "Welcome.\x01",
            "Please have a night shopping\x01",
            "Please enjoy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_58A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5923")

    ChrTalk(
        0xC,
        "The trade meeting has finally begun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As an industry person, I am a VIP of each country\x01",
            "I care about everyone's fashion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DC8")

    label("loc_5923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5ACB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59E4")

    ChrTalk(
        0xC,
        (
            "Welcome.\x01",
            "We have items of trends stocked\x01",
            "Please please take a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Because you can try it,\x01",
            "Please do not hesitate to tell us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AC6")

    label("loc_59E4")


    ChrTalk(
        0xC,
        (
            "服を扱っていた頃のHansonさんとは\x01",
            "I was a business prospect … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "At the same time, refine each other's sense\x01",
            "It was also a good rival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think that it's fine to be inclined to shoes … …\x01",
            "I think that you do not have to deal with anything special.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5AC6")

    Jump("loc_5DC8")

    label("loc_5ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BCF")

    ChrTalk(
        0xC,
        (
            "Because it is a rainy day\x01",
            "I see someone who skips fashion,\x01",
            "That's nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fashion is TPO--\x01",
            "Rather it fits because it is a rainy day\x01",
            "There is also coordination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Customers, if you like\x01",
            "I will appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5C7F")

    label("loc_5BCF")


    ChrTalk(
        0xC,
        (
            "Because it is a rainy day\x01",
            "I see someone who skips fashion,\x01",
            "That's nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fashion is TPO--\x01",
            "Rather it fits because it is a rainy day\x01",
            "There is also coordination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7F")

    Jump("loc_5DC8")

    label("loc_5C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D50")

    ChrTalk(
        0xC,
        (
            "Welcome.\x01",
            "Welcome to the boutique \"Lucca\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In our shop, I myself selected\x01",
            "Various manufacturers\x01",
            "お洋服をWe handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please take a good look.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DC8")

    label("loc_5D50")


    ChrTalk(
        0xC,
        (
            "In our shop, I myself selected\x01",
            "Various manufacturers\x01",
            "お洋服をWe handle it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Please take a good look.\x02",
    )

    CloseMessageWindow()

    label("loc_5DC8")

    Jump("loc_4DB4")

    label("loc_5DCD")

    TalkEnd(0xC)
    Return()

    # Function_16_4DA7 end

    def Function_17_5DD1(): pass

    label("Function_17_5DD1")

    Call(0, 18)
    Return()

    # Function_17_5DD1 end

    def Function_18_5DD5(): pass

    label("Function_18_5DD5")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C76")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E40")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5E40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5E5F")
    OP_AF(0x11)
    Jump("loc_5E71")

    label("loc_5E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E6F")
    OP_AF(0x10)
    Jump("loc_5E71")

    label("loc_5E6F")

    OP_AF(0xF)

    label("loc_5E71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C71")

    label("loc_5E80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E94")
    Jump("loc_6C71")

    label("loc_5E94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5F5A")

    ChrTalk(
        0xD,
        (
            "Looking at that big tree … …\x01",
            "It appeared in the Kingdom of Libert last year\x01",
            "I remember the story of a gigantic structure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Fortunately the phenomenon that leadership stops\x01",
            "I do not seem to have happened ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_5F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_601D")

    ChrTalk(
        0xD,
        (
            "When I prevented the Empire's train cannon\x01",
            "I thought both as a defense army ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the current situation\x01",
            "Just being anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The realization of the \"Continental Union Association\"\x01",
            "Is it still a desk on the desk …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_601D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D1")

    ChrTalk(
        0xD,
        "Certainly it was surprised by a sudden talk … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, with President Dieter\x01",
            "Defense Secretary Arios so far\x01",
            "I am telling you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I trust the two of you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_615F")

    label("loc_60D1")


    ChrTalk(
        0xD,
        (
            "Surely I was surprised at a sudden talk … …\x01",
            "President Dieter and Secretary of Defense Arios\x01",
            "あそこまでI am telling you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I trust the two of you.\x02",
    )

    CloseMessageWindow()

    label("loc_615F")

    Jump("loc_6C71")

    label("loc_6164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6240")

    ChrTalk(
        0xD,
        (
            "Crossbell has a number of problems\x01",
            "In order to solve from the root,\x01",
            "I think that there is no way other than independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It happened to such a thing in town … …\x01",
            "Here again in accordance with both countries,\x01",
            "I do not think that security will be protected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_6240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_62F4")

    ChrTalk(
        0xD,
        (
            "As many people say,\x01",
            "As for Mainz's incident\x01",
            "Is not it a conspiracy of the empire?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In such a situation,\x01",
            "The army to protect autonomous state\x01",
            "I will want it more and more … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_62F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6386")

    ChrTalk(
        0xD,
        (
            "Anything yesterday's train derailment accident\x01",
            "By a phantom beast\x01",
            "It is a rumor that it was caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmm, what is it like a phantom beast?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_6386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6416")

    ChrTalk(
        0xD,
        (
            "Siren of an ambulance has been\x01",
            "Although it is ringing loudly ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess it is not terrorism.\x01",
            "…… There are plenty more tragedies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_6416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6563")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64E6")

    ChrTalk(
        0xD,
        (
            "The value of the accessory is to all people\x01",
            "It is not equal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the meantime, handmade from grandchild\x01",
            "I got a brooch … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For me, what\x01",
            "It is a wonderful treasure superior to jewels.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_655E")

    label("loc_64E6")


    ChrTalk(
        0xD,
        (
            "In the meantime, handmade from grandchild\x01",
            "I got a brooch … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "For me, what\x01",
            "It is a wonderful treasure superior to jewels.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_655E")

    Jump("loc_6C71")

    label("loc_6563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_66AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6630")

    ChrTalk(
        0xD,
        (
            "Hmm, is it state independent?\x01",
            "It is a problem that is made considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Once threw out the empire,\x01",
            "I moved to crossbell\x01",
            "Me, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This is ridiculous\x01",
            "I can not help but say it is a difficult question.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66A9")

    label("loc_6630")


    ChrTalk(
        0xD,
        (
            "Once threw out the empire,\x01",
            "I moved to crossbell\x01",
            "Me, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Regarding the advocacy of national independence\x01",
            "I can not help but say it is a difficult question.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A9")

    Jump("loc_6C71")

    label("loc_66AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_673A")

    ChrTalk(
        0xD,
        (
            "Hmm, finally at last\x01",
            "Is the commencement of the trade meeting started?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Anyhow, anything\x01",
            "I would like you to make a meaningful meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_673A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67FA")

    ChrTalk(
        0xD,
        "I was completely sunny.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "By the way, by the leaders\x01",
            "The theater of the alkane shell\x01",
            "It was around the end of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, enjoy\x01",
            "I hope to have you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_687F")

    label("loc_67FA")


    ChrTalk(
        0xD,
        (
            "By the way, by the leaders\x01",
            "The theater of the alkane shell\x01",
            "It was around the end of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm, enjoy\x01",
            "I hope to have you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687F")

    Jump("loc_6C71")

    label("loc_6884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_691A")

    ChrTalk(
        0xD,
        (
            "I went out to the roof without age\x01",
            "I saw the state of the unveiling ceremony … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The Orkis Tower is truly brilliant.\x01",
            "I have lost words for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C71")

    label("loc_691A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6A5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69CC")

    ChrTalk(
        0xD,
        (
            "Welcome.\x01",
            "アクセサリ《Baker》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there is something to worry about\x01",
            "Please take it in your hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A59")

    label("loc_69CC")


    ChrTalk(
        0xD,
        (
            "Customers who come to this department store\x01",
            "How do you say,\x01",
            "There are many people with a warm heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Although it is not comparable,\x01",
            "It is very different from those of the imperial nobles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A59")

    Jump("loc_6C71")

    label("loc_6A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B60")

    ChrTalk(
        0xD,
        (
            "It will rain, somehow in the empire\x01",
            "When I was an art dealer\x01",
            "I remember it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Speaking of me at that time,\x01",
            "Just to fish up the value of arts\x01",
            "I was sending every day I was struggling … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Just to recall,\x01",
            "My breath is going to be blocked.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BD4")

    label("loc_6B60")


    ChrTalk(
        0xD,
        (
            "Sorry, bored\x01",
            "Did you talk about yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Welcome.\x01",
            "Please see with loose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD4")

    Jump("loc_6C71")

    label("loc_6BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6C71")

    ChrTalk(
        0xD,
        (
            "Welcome.\x01",
            "Please take a look and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our shop accessories and accessories\x01",
            "Gifts for loved ones and\x01",
            "Ideal for rewards to yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C71")

    Jump("loc_5DE2")

    label("loc_6C76")

    TalkEnd(0xD)
    Return()

    # Function_18_5DD5 end

    def Function_19_6C7A(): pass

    label("Function_19_6C7A")

    SetScenarioFlags(0x2, 4)
    Call(0, 20)
    Return()

    # Function_19_6C7A end

    def Function_20_6C81(): pass

    label("Function_20_6C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DB0")
    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2B")

    ChrTalk(
        0xE,
        (
            "Well, you guys\x01",
            "Where the hell did you get in from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, somewhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tentatively, if you want to shop\x01",
            "Beyond the counter properly\x01",
            "Please say that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6DAC")

    label("loc_6D2B")


    ChrTalk(
        0xE,
        (
            "Tentatively, if you want to shop\x01",
            "Beyond the counter properly\x01",
            "Please say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Also, in the inventory on that side\x01",
            "Do not touch it too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DAC")

    TalkEnd(0xE)
    Return()

    label("loc_6DB0")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_735E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA5")

    ChrTalk(
        0xE,
        (
            "Hi, welcome.\x01",
            "雑貨コーナー《Southwark》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "From our daily necessities to souvenirs at our store,\x01",
            "I handle a variety of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "If you do not mind, please take a closer look.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6F24")

    label("loc_6EA5")


    ChrTalk(
        0xE,
        (
            "From our daily necessities to souvenirs at our store,\x01",
            "I handle a variety of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "If you do not mind, please take a closer look.\x02",
    )

    CloseMessageWindow()

    label("loc_6F24")

    TalkEnd(0xE)
    Return()

    label("loc_6F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A6")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは店主のSouthwarkに\x01",
            "I spoke to him in a loud voice.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000F(Excuse me,\x01",
            "\"Mikoshi tikutaku\" is called\x01",
            "How much is the item? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "(Oh, it's 500 Mira.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "(Hehe, maybe there\x01",
            "Present for your child? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Oh yes, I'm still thinking.\x02\x03",
            "#00003F(500 Mira ……\x01",
            "What do you want to buy for Shin? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7104")

    label("loc_70A6")


    ChrTalk(
        0xE,
        (
            "(It's 500 mils in length.\x01",
            "Are you going to buy it? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(I agree……)\x02",
    )

    CloseMessageWindow()

    label("loc_7104")

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
            "Purchase \"Tikutaku Misashi\"\x01",      # 0
            "Think a little more\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72AD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_71ED")
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000FWell then, can I have it?\x02",
    )

    CloseMessageWindow()
    Sound(20, 0, 80, 0)

    ChrTalk(
        0xE,
        "(OK, there is a waitress.)\x02",
    )

    CloseMessageWindow()
    Call(0, 52)
    Jump("loc_72A8")

    label("loc_71ED")


    ChrTalk(
        0x101,
        "#00000F(Well then, then … …)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(There is no Mira ……\x01",
            "Haa, how pure I am. )\x02\x03",
            "#00000F(I'm sorry, it's okay after all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "(???)\x02",
    )

    CloseMessageWindow()

    label("loc_72A8")

    Jump("loc_72E5")

    label("loc_72AD")


    ChrTalk(
        0x101,
        (
            "#00003F(Tentatively,\x01",
            "Why do not you think about a bit … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E5")

    TalkEnd(0xE)
    Return()

    label("loc_72EE")


    ChrTalk(
        0xE,
        (
            "Apparently the gift\x01",
            "You seem to have been pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, after all\x01",
            "Mitchell is great.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    label("loc_735E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E5")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73C6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_73C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_73E5")
    OP_AF(0x1D)
    Jump("loc_7467")

    label("loc_73E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_73F5")
    OP_AF(0x1C)
    Jump("loc_7467")

    label("loc_73F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7405")
    OP_AF(0x1B)
    Jump("loc_7467")

    label("loc_7405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7415")
    OP_AF(0x1A)
    Jump("loc_7467")

    label("loc_7415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7425")
    OP_AF(0x19)
    Jump("loc_7467")

    label("loc_7425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7435")
    OP_AF(0x18)
    Jump("loc_7467")

    label("loc_7435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_7445")
    OP_AF(0x17)
    Jump("loc_7467")

    label("loc_7445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7455")
    OP_AF(0x16)
    Jump("loc_7467")

    label("loc_7455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7465")
    OP_AF(0x15)
    Jump("loc_7467")

    label("loc_7465")

    OP_AF(0x14)

    label("loc_7467")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85E0")

    label("loc_7476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_748A")
    Jump("loc_85E0")

    label("loc_748A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85E0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7557")

    ChrTalk(
        0xE,
        (
            "What can a merchant do\x01",
            "After all the business\x01",
            "There is nothing other than to continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Distribution routes outside the country fluctuate\x01",
            "There is no prospect of resuming, but …\x01",
            "I have to overcome wisdom and survive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_7557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_75E7")

    ChrTalk(
        0xE,
        (
            "An important person at such a time\x01",
            "I'm really relieved to be by my side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What I say, from the bottom of my belly\x01",
            "It feels like courage is coming up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_75E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_77E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7774")

    ChrTalk(
        0xE,
        (
            "Suddenly I stayed at Crosbell this morning\x01",
            "To the Republic, from the Republic Government\x01",
            "There was a notice prompting the return home earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It is a story that no longer exercises ability,\x01",
            "What is going to happen in the future\x01",
            "It is a place I imagined, but … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "This crossbell has\x01",
            "For me now, than anything else\x01",
            "I have an important person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So,\x01",
            "Whatever happens\x01",
            "I decided to stay in this place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_77E3")

    label("loc_7774")


    ChrTalk(
        0xE,
        (
            "たとえWhatever happens\x01",
            "I decided to stay in this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "And be sure to protect her.\x02",
    )

    CloseMessageWindow()

    label("loc_77E3")

    Jump("loc_85E0")

    label("loc_77E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_787A")

    ChrTalk(
        0xE,
        (
            "The renewal theater is awesome,\x01",
            "And Mr. Iria did that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Although there was only fear at the time of the raid ……\x01",
            "I'm full with anger now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_787A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_797B")

    ChrTalk(
        0xE,
        (
            "\"Golden Sun, Silver Moon\"\x01",
            "Renewal version release\x01",
            "It is finally this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Given the situation in Mainz\x01",
            "I feel like being floating on a fossil\x01",
            "I do not wish but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The stage is a stage,\x01",
            "Even in the sense of getting courage and energy\x01",
            "I will be entertained for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7A17")

    label("loc_797B")


    ChrTalk(
        0xE,
        (
            "Given the situation in Mainz\x01",
            "I feel like being floating on a fossil\x01",
            "I do not wish but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The stage is a stage,\x01",
            "Even in the sense of getting courage and energy\x01",
            "I will be entertained for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A17")

    Jump("loc_85E0")

    label("loc_7A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AB5")

    ChrTalk(
        0xE,
        (
            "It was a business until now,\x01",
            "Since she was done\x01",
            "You can see the world different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What I should say …\x01",
            "I guess that's what makes you happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_7AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7B20")

    ChrTalk(
        0xE,
        (
            "Somehow, in the west\x01",
            "It is a big deal to have a train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I hope it is not terrorism ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_85E0")

    label("loc_7B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE9")

    ChrTalk(
        0xE,
        (
            "Is there a referendum for inquiries about independence … ….\x01",
            "Although it is a will confirmation to the last\x01",
            "It is a serious matter responsible to what mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because I am a human in the Republic\x01",
            "I can not vote, but,\x01",
            "I can make you think a lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7C5D")

    label("loc_7BE9")


    ChrTalk(
        0xE,
        "Is there a referendum for inquiries about independence … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because I am a human in the Republic\x01",
            "I can not vote, but,\x01",
            "I can make you think a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C5D")

    Jump("loc_85E0")

    label("loc_7C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D0E")

    ChrTalk(
        0xE,
        (
            "At first it looks like a cute little sister\x01",
            "I intended to do it ….\x01",
            "You do not know how people feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway the current me is happy.\x01",
            "It was nice to be brave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7D94")

    label("loc_7D0E")


    ChrTalk(
        0xE,
        (
            "Janettaちゃん、最初は可愛い\x01",
            "I intended to be like a little sister ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Anyway the current me is happy.\x01",
            "It was nice to be brave.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D94")

    Jump("loc_85E0")

    label("loc_7D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E4D")

    ChrTalk(
        0xE,
        (
            "Janettaちゃんは昨日、\x01",
            "She seems to have eaten with rich men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "And they seemed to have been honestly crushed … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, I wonder what I am relieved.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7EA5")

    label("loc_7E4D")


    ChrTalk(
        0xE,
        "Well, I wonder what I am relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "That means that I feel like that … …\x02",
    )

    CloseMessageWindow()

    label("loc_7EA5")

    Jump("loc_85E0")

    label("loc_7EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F82")

    ChrTalk(
        0xE,
        (
            "Janettaちゃんが、\x01",
            "It seems like it will be funny this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "明日にはスーパーJanettaに\x01",
            "I was born again,\x01",
            "I was saying something I do not know well … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I wonder what it is, why.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7FE3")

    label("loc_7F82")


    ChrTalk(
        0xE,
        (
            "Janettaちゃんが、\x01",
            "It seems like it will be funny this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I wonder what it is, why.\x02",
    )

    CloseMessageWindow()

    label("loc_7FE3")

    Jump("loc_85E0")

    label("loc_7FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_815F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80E3")

    ChrTalk(
        0xE,
        (
            "I was unable to see it, although it was an unveiling ceremony\x01",
            "I guess it was truly amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Always only in news magazines\x01",
            "The leaders of the countries that you can not see\x01",
            "It's amazing as it's gathering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The next issue of Crossbell Times\x01",
            "I can not help looking forward from now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_815A")

    label("loc_80E3")


    ChrTalk(
        0xE,
        (
            "Is it an unveiling ceremony?\x01",
            "I guess it was truly amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Tentatively,\x01",
            "The next issue of Crossbell Times\x01",
            "I can not help looking forward from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_815A")

    Jump("loc_85E0")

    label("loc_815F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_83FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8352")

    ChrTalk(
        0xE,
        (
            "The stage of the alkane shell\x01",
            "\"Golden Sun, Silver Moon\" renewed\x01",
            "Do you know the story that it will be done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Although details are not yet announced at all yet,\x01",
            "It seems to add a rather bold production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhuu, and what … …\x01",
            "Actually, I will post a ticket on the opening day\x01",
            "I succeeded in getting 2 cards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, he is a good economic story.\x02\x03",
            "#00309FBy the way, who is the other party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well … I wonder if you will not ask me that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "And anyway, until release\x01",
            "There is still a little over a month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Until then it will manage somehow, yeah.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_83F5")

    label("loc_8352")


    ChrTalk(
        0xE,
        (
            "Renewal stage of alkane shell,\x01",
            "Tickets for the first performance\x01",
            "I was fortunate enough to get 2 cards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Well, who are you going with?\x01",
            "I am about to search from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F5")

    Jump("loc_85E0")

    label("loc_83FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_8459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8415")
    Call(0, 21)
    Jump("loc_8454")

    label("loc_8415")


    ChrTalk(
        0xE,
        (
            "I still know if it's my birthday … …\x01",
            "I wish you were ordinary grinning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8454")

    Jump("loc_85E0")

    label("loc_8459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_85E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8585")

    ChrTalk(
        0xE,
        (
            "Hi, welcome.\x01",
            "雑貨コーナー《Southwark》へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Recently, in response to customers' hot requests\x01",
            "I strengthened Michi goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "If you are interested, please take a look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, Michi Goods?\x01",
            "I heard that Tio would be delighted when heard it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHehe, indeed.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_85E0")

    label("loc_8585")


    ChrTalk(
        0xE,
        (
            "Michishi goods are\x01",
            "Thanks to you, it is very popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "If you are interested, please take a look.\x02",
    )

    CloseMessageWindow()

    label("loc_85E0")

    Jump("loc_7368")

    label("loc_85E5")

    TalkEnd(0xE)
    Return()

    # Function_20_6C81 end

    def Function_21_85E9(): pass

    label("Function_21_85E9")

    OP_4B(0x12, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x12,
        (
            "Oh, it is MICHICI's cute, it's cute.\x01",
            "Southwarkさん、これください。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, yeah.\x01",
            "Well it will be 500 Mira ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It is not.\x01",
            "Please give me a present ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "What is a gift, why am I again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Because I work in the same department store.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "No no no,\x01",
            "It will not be such a reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x12, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_21_85E9 end

    def Function_22_8739(): pass

    label("Function_22_8739")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_88B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8831")

    ChrTalk(
        0xFE,
        (
            "If you think that martial law was lifted\x01",
            "A mysterious big tree emerges … …\x01",
            "And the threat of the two major countries was also left … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To this unprecedented difficulty,\x01",
            "What can we do for ourself -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Each person steadily thinks,\x01",
            "And there is no choice but to act.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_88B3")

    label("loc_8831")


    ChrTalk(
        0xFE,
        (
            "To this unprecedented difficulty,\x01",
            "What can we do for ourself -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Each person steadily thinks,\x01",
            "And there is no choice but to act.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88B3")

    Jump("loc_9AD0")

    label("loc_88B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88D3")
    Call(0, 23)
    Jump("loc_894B")

    label("loc_88D3")


    ChrTalk(
        0xFE,
        (
            "As Mr. Lloyd says,\x01",
            "Follow this ban as it is\x01",
            "I would like to see the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… … Please be careful of everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_894B")

    Jump("loc_9AD0")

    label("loc_8950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A57")

    ChrTalk(
        0xFE,
        (
            "In just one week after the referendum\x01",
            "Let's be the situation so far …\x01",
            "Even though I imagined as though it was a fossil stone, I could not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, perhaps the future\x01",
            "No wonder whatever happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To survive this department store,\x01",
            "We need to think a lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8AE3")

    label("loc_8A57")


    ChrTalk(
        0xFE,
        (
            "Anyway, perhaps the future\x01",
            "No wonder whatever happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To survive this department store,\x01",
            "We need to think a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE3")

    Jump("loc_9AD0")

    label("loc_8AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C03")

    ChrTalk(
        0xFE,
        (
            "本日、Citizen会館にて街の復興支援を\x01",
            "A thematic charity event\x01",
            "It is held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city and the commerce and industry association,\x01",
            "To cheer the residents\x01",
            "This project that got up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This department store also fully cooperates\x01",
            "Since we are excited,\x01",
            "Please drop in by all means.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8CB7")

    label("loc_8C03")


    ChrTalk(
        0xFE,
        (
            "本日、Citizen会館にて街の復興支援を\x01",
            "A thematic charity event\x01",
            "It is held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This department store also fully cooperates\x01",
            "Since we are excited,\x01",
            "Please drop in by all means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB7")

    Jump("loc_9AD0")

    label("loc_8CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8D71")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group occupies Mainz ……\x01",
            "This situation, as if a conflict nightmare\x01",
            "It was as if it was revived but I could not bear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway as soon as possible,\x01",
            "I would like the situation to fit ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_8D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8C")
    Call(0, 26)
    Jump("loc_8EF9")

    label("loc_8D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E89")

    ChrTalk(
        0xFE,
        (
            "Anything, yesterday's train derailment accident\x01",
            "By a monster like a gigantic demon\x01",
            "It seems to have been caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Recently, in various parts of autonomous province\x01",
            "Large, magical monsters\x01",
            "There seems to be rumors that it will appear … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what is wrong with both?\x01",
            "Is there a causal relationship?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8EF9")

    label("loc_8E89")


    ChrTalk(
        0xFE,
        (
            "A monster like a huge demon,\x01",
            "Also a large magical monster ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what is wrong with both?\x01",
            "Is there a causal relationship?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EF9")

    Jump("loc_9AD0")

    label("loc_8EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8FBA")

    ChrTalk(
        0xFE,
        (
            "I came from the station side\x01",
            "I heard from customers,\x01",
            "Apparently it seems the train derailed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know the details … …\x01",
            "Anyway, in an ambulance\x01",
            "I am worried about the people who have been carried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_8FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9086")

    ChrTalk(
        0xFE,
        (
            "Recently, from various customers' mouths\x01",
            "About the pros and cons of national independence\x01",
            "I came to see a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are many positive opinions,\x01",
            "Based on the intention of the two biggest countries naturally\x01",
            "There seems to be many people who seem to be worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_9086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_918B")

    ChrTalk(
        0xFE,
        (
            "I think now, the other day's trade meeting\x01",
            "It was just like a storm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to be a terrorist raid,\x01",
            "More than anything, Mayor Dieter proposed\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In what form of this proposal\x01",
            "Will it appeal to international public opinion ……\x01",
            "I can not keep an eye on the future situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_918B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9351")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92A1")

    ChrTalk(
        0xFE,
        (
            "Today, on our rooftop\x01",
            "Toward the sightseeing of Orkis Tower\x01",
            "Many people are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to your support,\x01",
            "The sales direction is also good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, above all,\x01",
            "I am happy with this bustling atmosphere.\x01",
            "We are also entertaining the people of the hospitality.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_934C")

    label("loc_92A1")


    ChrTalk(
        0xFE,
        (
            "Today, on our rooftop\x01",
            "Toward the sightseeing of Orkis Tower\x01",
            "Many people are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There is a crowd that I can not see usually,\x01",
            "We are also entertaining the people of the hospitality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_934C")

    Jump("loc_9AD0")

    label("loc_9351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_93DE")

    ChrTalk(
        0xFE,
        (
            "Today's sales are as usual\x01",
            "With 20:00\x01",
            "We will end it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not forget or forgotten your purchase\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD0")

    label("loc_93DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94EB")

    ChrTalk(
        0xFE,
        (
            "Shyly, with customers\x01",
            "I was able to see the unveiling ceremony … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the prospect of \"Orkis Tower\"\x01",
            "I was just breathtaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A skyscraper is a skyscraper on the 40th floor above the ground ……\x01",
            "This cross-bell new\x01",
            "You can say that it is suitable for a symbol.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9551")

    label("loc_94EB")


    ChrTalk(
        0xFE,
        (
            "A skyscraper is a skyscraper on the 40th floor above the ground ……\x01",
            "This cross-bell new\x01",
            "You can say that it is suitable for a symbol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9551")

    Jump("loc_9AD0")

    label("loc_9556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_98B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_970B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9698")
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "Oh, this is Elie Lady.\x01",
            "Today we have a rare guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, now I cross-bell this girl\x01",
            "I'm guiding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Indeed, so in our shop\x01",
            "I am fortunate that you can visit my feet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, please\x01",
            "Please have a nice temporary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9706")

    label("loc_9698")


    ChrTalk(
        0x11,
        (
            "Please visit our shop today as well\x01",
            "It is pleasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Please, with relaxing\x01",
            "Please have a nice temporary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9706")

    Jump("loc_98AC")

    label("loc_970B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_982C")

    ChrTalk(
        0xFE,
        (
            "It is time tomorrow\x01",
            "A trade meeting will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell Autonomous State and surrounding it\x01",
            "Representatives of the four countries will meet together …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking back on these decades,\x01",
            "Just that alone Historically\x01",
            "It is very meaningful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What shall I say,\x01",
            "I feel the highlight of my feelings.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_98AC")

    label("loc_982C")


    ChrTalk(
        0xFE,
        (
            "Crossbell Autonomous State and surrounding it\x01",
            "Representatives of the four countries will meet together …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What shall I say,\x01",
            "I feel the highlight of my feelings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98AC")

    Jump("loc_9AD0")

    label("loc_98B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_997A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98CC")
    Call(0, 24)
    Jump("loc_9975")

    label("loc_98CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98DE")
    Call(0, 25)
    Jump("loc_9975")

    label("loc_98DE")


    ChrTalk(
        0x11,
        (
            "We visited our shop on a rainy day\x01",
            "Minor to customers\x01",
            "We have gifts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hello everyone, today to my heart's content\x01",
            "ショッピングをPlease enjoy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9975")

    Jump("loc_9AD0")

    label("loc_997A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9995")
    Call(0, 24)
    Jump("loc_9AD0")

    label("loc_9995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A5A")

    ChrTalk(
        0xFE,
        (
            "Everyone, today\x01",
            "Coming to department store \"Times\"\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In our shop, catch the customer's eye\x01",
            "We have various sales floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please please enjoy it slowly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9AD0")

    label("loc_9A5A")


    ChrTalk(
        0xFE,
        (
            "At our Department Store, we will draw customer's attention\x01",
            "We have various sales floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please\x01",
            "Please enjoy yourself slowly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AD0")

    TalkEnd(0xFE)
    Return()

    # Function_22_8739 end

    def Function_23_9AD4(): pass

    label("Function_23_9AD4")

    OP_4B(0x11, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    ChrTalk(
        0x11,
        "Eli ladies and support staff ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Could it be a ban on going out …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo … Unfortunately\x01",
            "It is not canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Is that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FMr. Neston, Department store's\x01",
            "Could you tell me the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, yesterday is your\x01",
            "Even after request has been made and martial law is issued\x01",
            "We opened a shop until the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "That moya came out in it,\x01",
            "With customers who came running shortly afterwards\x01",
            "All the staff are in a state of being staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Overnight a new announcement too\x01",
            "I thought that it would come out … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Really, the government\x01",
            "What is he thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F……I see,\x01",
            "After all, there is no grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FManager, we are now,\x01",
            "To converge this situation\x01",
            "I am acting.\x02\x03",
            "Until the outside calms down,\x01",
            "Do not let everyone outdoors\x01",
            "Continue to thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Certainly.\x01",
            "… … Please be careful of everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes.\x01",
            "Instead of amulets\x01",
            "Please bring here.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('圣灵药·改', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        (
            "#00100FMr. Neston ……\x01",
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

    # Function_23_9AD4 end

    def Function_24_9ED5(): pass

    label("Function_24_9ED5")


    ChrTalk(
        0x11,
        (
            "Welcome.\x01",
            "Welcome to department store \"Times\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x102, 500)
    Sleep(100)

    ChrTalk(
        0x11,
        "This is Elie Lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Together with Mr. MacDael\x01",
            "It seems that the countries were going around,\x01",
            "It was returned to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, just the other day.\x02\x03",
            "From now on again, at the Special Affairs Support Division\x01",
            "I sincerely thank you for your activity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, of course.\x01",
            "I pray for your constant and prosperous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FErie, department store\x01",
            "You are acquainted with the manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, my grandfather's acquaintance\x01",
            "I've been getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, as expected a chief daughter … …\x01",
            "Does not it interest you flexibility too?\x02\x03",
            "For example, we\x01",
            "You can get VIP treatment.\x02",
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
            "No, for that point\x01",
            "Never treat it like a special than a lady\x01",
            "Because I am receiving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "With services similar to other customers\x01",
            "I am allowed to correspond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FHuhu, that kind of thing.\x01",
            "I was sorry, Waji.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306FWhew, Serious eyes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, it may be a bit unnatural.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 3)
    Return()

    # Function_24_9ED5 end

    def Function_25_A29D(): pass

    label("Function_25_A29D")


    ChrTalk(
        0x11,
        (
            "Everyone, today is bad at your feet,\x01",
            "Thank you for visiting us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "If you want, please click here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('痊愈之药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00105FNeston, this is …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, despite rainy days\x01",
            "To customers who visited us\x01",
            "It is a small gratitude feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Limited for 100 people a day,\x01",
            "Service from last month\x01",
            "I started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIndeed, this is\x01",
            "It is a nice service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYeah, to it\x01",
            "It will make rain somehow fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you very much.\x01",
            "I would be pleased if you let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well then, everyone, rainy day\x01",
            "Please enjoy shopping.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 4)
    Return()

    # Function_25_A29D end

    def Function_26_A4FA(): pass

    label("Function_26_A4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 4)), scpexpr(EXPR_END)), "loc_A65B")

    ChrTalk(
        0x11,
        "Thank you for coming to our store today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "If you want, please click here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('痊愈之药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00000FOh, it's a service on a rainy day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100Fどうも、Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "No, this is it.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Everyone, everyone on a rainy day\x01",
            "ショッピングをPlease enjoy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8AE")

    label("loc_A65B")


    ChrTalk(
        0x11,
        (
            "Today is bad at your feet,\x01",
            "Thank you for visiting us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "If you want, please click here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('痊愈之药', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#00105FNeston, this is …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Yes, despite rainy days\x01",
            "To customers who visited us\x01",
            "It is a small gratitude feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Limited for 100 people a day,\x01",
            "Service from last month\x01",
            "I started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIndeed, this is\x01",
            "It is a nice service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYeah, to it\x01",
            "It will make rain somehow fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Thank you very much.\x01",
            "I would be pleased if you let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well then, everyone, rainy day\x01",
            "Please enjoy shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8AE")

    SetScenarioFlags(0x16C, 5)
    Return()

    # Function_26_A4FA end

    def Function_27_A8B2(): pass

    label("Function_27_A8B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A95D")

    ChrTalk(
        0xFE,
        (
            "In an effort to overcome this hardship\x01",
            "Department store staff\x01",
            "Everyone is full of motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am full of motivation ……\x01",
            "No, as motivated and full of ladies\x01",
            "I will do my best with all my might!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_A95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A9EF")

    ChrTalk(
        0xFE,
        (
            "Honestly I am full of uneasy feelings … …\x01",
            "Southwarkさんの顔を見ていると\x01",
            "My mind calms down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huhu, it is kind of strange feeling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_A9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AA92")

    ChrTalk(
        0xFE,
        (
            "Southwarkさん、\x01",
            "To me for crossbell\x01",
            "I say that it will remain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not saying in this situation\x01",
            "I think, but … I am very happy right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AB2B")

    ChrTalk(
        0xFE,
        (
            "…… How much do you think I will forget?\x01",
            "When the alkane shell was attacked\x01",
            "Fear is really unforgettable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The culprit is united,\x01",
            "What is the purpose of doing something ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AB2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_ACA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC24")

    ChrTalk(
        0xFE,
        (
            "I hurried away today and waited for it\x01",
            "Renewal of the alkane shell\x01",
            "I am going to watch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what, I have always been here\x01",
            "It's a stage I've been looking forward to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not miss even a moment\x01",
            "I intend to concentrate on theater.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_ACA4")

    label("loc_AC24")


    ChrTalk(
        0xFE,
        (
            "No matter what, I have always been here\x01",
            "It's a stage I've been looking forward to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not miss even a moment\x01",
            "I intend to concentrate on theater.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACA4")

    Jump("loc_B1C8")

    label("loc_ACA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AD6D")

    ChrTalk(
        0xFE,
        (
            "明日はいよいよThe stage of the alkane shell\x01",
            "\"Gold Sun, Month of Silver\"\x01",
            "It is the release date of the renewal version.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Southwarkさんと一緒に\x01",
            "I am planning to go see it,\x01",
            "Really, I am really looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AD6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_ADD1")

    ChrTalk(
        0xFE,
        "Cure, ambulances a lot passed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am worried about the people who were brought to the hospital ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_ADD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AE77")

    ChrTalk(
        0xFE,
        (
            "After all, as a national independence\x01",
            "What merit is there?\x01",
            "I do not know well the difficult things … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "そうだ、Southwarkさんに教えてもらおっと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_AE77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AE85")
    Jump("loc_B1C8")

    label("loc_AE85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AFDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF8B")

    ChrTalk(
        0xFE,
        (
            "Ha, yesterday definitely\x01",
            "I thought it would go well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That certainly\x01",
            "Cynthia-senpai is attractive.\x01",
            "I will fall in love even with a woman's … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, about 1 person to say so\x01",
            "Someone who is interested in me\x01",
            "Is not it good?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AFD7")

    label("loc_AF8B")


    ChrTalk(
        0xFE,
        (
            "Shinkishiku ……\x01",
            "People who understand my appeal\x01",
            "Where am I supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFD7")

    Jump("loc_B1C8")

    label("loc_AFDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B04F")

    ChrTalk(
        0xFE,
        (
            "Clothes are ready, OK,\x01",
            "Nori of makeup is also perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhufu, I'm a bit different at tonight's jet\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1C8")

    label("loc_B04F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B16D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0EC")

    ChrTalk(
        0xFE,
        (
            "Uhufu, active in the world\x01",
            "There are customers, too ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder when it was first time ago.\x01",
            "I wonder if it will be night soon ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B168")

    label("loc_B0EC")


    ChrTalk(
        0xFE,
        (
            "It is also your opponent,\x01",
            "Working in a port area\x01",
            "I am a businessman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is a chance, a chance!\x02",
    )

    CloseMessageWindow()

    label("loc_B168")

    Jump("loc_B1C8")

    label("loc_B16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B17B")
    Jump("loc_B1C8")

    label("loc_B17B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B1BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B196")
    Call(0, 21)
    Jump("loc_B1BA")

    label("loc_B196")


    ChrTalk(
        0xFE,
        "ぶう、Southwarkさんのいけず〜。\x02",
    )

    CloseMessageWindow()

    label("loc_B1BA")

    Jump("loc_B1C8")

    label("loc_B1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B1C8")

    label("loc_B1C8")

    TalkEnd(0xFE)
    Return()

    # Function_27_A8B2 end

    def Function_28_B1CC(): pass

    label("Function_28_B1CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B241")

    ChrTalk(
        0xFE,
        (
            "I think that I finally went outside\x01",
            "Such things in the sky ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What on earth …\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B24F")
    Jump("loc_B9E7")

    label("loc_B24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B2D5")

    ChrTalk(
        0xFE,
        (
            "Okay, I do not know well,\x01",
            "War is going to happen … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am anxious but … ….\x01",
            "Ken、あなたは私が守るからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B361")

    ChrTalk(
        0xFE,
        (
            "Although I have been absent for a while,\x01",
            "I will resume shopping from today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because what we do not consume\x01",
            "The economy does not turn around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B3F4")

    ChrTalk(
        0xFE,
        (
            "I am anxious to stay at home,\x01",
            "Because I feel restless\x01",
            "I came to department store today, too ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Have fun shopping on funkishi\x01",
            "I do not feel it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B492")

    ChrTalk(
        0xFE,
        (
            "An accident on a train is a noisy story.\x01",
            "But restoration is quick and I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if logistics stops,\x01",
            "I can not do shopping like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B4EB")

    ChrTalk(
        0xFE,
        (
            "There seems to be some noise.\x01",
            "Should I rather go home earlier today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B5BA")

    ChrTalk(
        0xFE,
        (
            "Recently, my husband has a difficult face.\x01",
            "Apparently regarding national independence\x01",
            "It seems there are places to think differently ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'll leave the difficult story for the time being to my husband.\x01",
            "Anyway, I enjoy shopping ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B627")

    ChrTalk(
        0xFE,
        "Oh well, new products were added again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as expected\x01",
            "Because it is a Times department store in the world.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B6B4")

    ChrTalk(
        0xFE,
        "Certainly today was the day of the trade meeting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I can not see it anyway,\x01",
            "Although it may be useless if you care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_B74E")

    ChrTalk(
        0xFE,
        "いい、Ken。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say something to Dad first when you return.\x01",
            "Then hug quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's okay, if you pinch it with two people\x01",
            "Because it is a scary thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7C0")

    ChrTalk(
        0xFE,
        "The unveiling ceremony just before was amazing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow excited\x01",
            "The purchasing willingness was stimulated.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B821")

    label("loc_B7C0")


    ChrTalk(
        0xFE,
        (
            "Well, now right after your payday\x01",
            "Because it is warm in your wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will definitely look at you today.\x02",
    )

    CloseMessageWindow()

    label("loc_B821")

    Jump("loc_B9E7")

    label("loc_B826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B8C9")

    ChrTalk(
        0xFE,
        (
            "I always think,\x01",
            "The person thinking about the product is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering new things from next to next\x01",
            "Every time, our consumers\x01",
            "Because I grab the heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9E7")

    label("loc_B8C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B98F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B962")

    ChrTalk(
        0xFE,
        (
            "Before going shopping,\x01",
            "ぐちぐち言っていたKenも\x01",
            "I have not complained recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is also love ~, Mama is happy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B98A")

    label("loc_B962")


    ChrTalk(
        0xFE,
        "I am happy with my mother who has a son who I made.\x02",
    )

    CloseMessageWindow()

    label("loc_B98A")

    Jump("loc_B9E7")

    label("loc_B98F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B9E7")

    ChrTalk(
        0xFE,
        "Pervaded\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter when you come to department stores\x01",
            "No matter how much I am getting tired of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9E7")

    TalkEnd(0xFE)
    Return()

    # Function_28_B1CC end

    def Function_29_B9EB(): pass

    label("Function_29_B9EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BA5E")

    ChrTalk(
        0xFE,
        (
            "To grow trees in the sky,\x01",
            "What on earth are they?\x01",
            "I wonder if I am seeing a dream or a vision ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BA5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BA6C")
    Jump("loc_C415")

    label("loc_BA6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BA88")

    ChrTalk(
        0xFE,
        "Mama …\x02",
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BA88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BAEA")

    ChrTalk(
        0xFE,
        (
            "Mommy is really strong.\x01",
            "I do not quite understand it,\x01",
            "You can be encouraged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BAEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BB70")

    ChrTalk(
        0xFE,
        (
            "Mumma of fluffy, today\x01",
            "I do not feel like comfortable feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, considering Mainz\x01",
            "It is unreasonable, is not it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BB70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BC0D")

    ChrTalk(
        0xFE,
        (
            "My mother's passion for shopping\x01",
            "I can not crush like rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is still fine,\x01",
            "When I got on a heavy rainy day\x01",
            "It was soaked and scattered.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BC0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BD30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC5")

    ChrTalk(
        0xFE,
        (
            "Ambulance sirens,\x01",
            "It's amazing loud volume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is quite a close distance\x01",
            "I think it is loud … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People driving a car\x01",
            "Is it also done with earplugs?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_BD2B")

    label("loc_BCC5")


    ChrTalk(
        0xFE,
        (
            "Ambulance sirens,\x01",
            "It's amazing loud volume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who is driving\x01",
            "Is it also done with earplugs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2B")

    Jump("loc_C415")

    label("loc_BD30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BDE2")

    ChrTalk(
        0xFE,
        (
            "Everyone, everyone,\x01",
            "Weather like No Mama Like Weather\x01",
            "I am happy if I can think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, then\x01",
            "In the immediate neighborhood\x01",
            "It seems to have been merged.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_BDE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BF0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA1")

    ChrTalk(
        0xFE,
        (
            "Well, today is\x01",
            "I will decide to kill time by human observation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, recently, with a brother of a general store\x01",
            "The sister 's sister' s guide is nice to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, maybe this is … …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_BF08")

    label("loc_BEA1")


    ChrTalk(
        0xFE,
        (
            "Recently, with a brother of a general store\x01",
            "The sister 's sister' s guide is nice to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, maybe this is … …\x02",
    )

    CloseMessageWindow()

    label("loc_BF08")

    Jump("loc_C415")

    label("loc_BF0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF8C")

    ChrTalk(
        0xFE,
        (
            "Yesterday's mama's\x01",
            "The apology operation was a great success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is crying in addition to hugs ……\x01",
            "A terrible thing, it is mama.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C000")

    label("loc_BF8C")


    ChrTalk(
        0xFE,
        (
            "Mom's embrace and tears, daddy is totally\x01",
            "It was watered down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The man who fell in love with that\x01",
            "Is it a weak person?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C000")

    Jump("loc_C415")

    label("loc_C005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C06B")

    ChrTalk(
        0xFE,
        (
            "Mommy is crazy about shopping\x01",
            "Until like this ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Truly dad's also\x01",
            "I think that I am angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_C06B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C16F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10E")

    ChrTalk(
        0xFE,
        "The unveiling ceremony was truly a masterpiece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…. That's right,\x01",
            "My mother's tension is somewhat concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shop for useless shopping\x01",
            "I hope I do not … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C16A")

    label("loc_C10E")


    ChrTalk(
        0xFE,
        (
            "Today's mama is a bit\x01",
            "I feel that my eyes are different colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shop for useless shopping\x01",
            "I hope I do not … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C16A")

    Jump("loc_C415")

    label("loc_C16F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C21A")

    ChrTalk(
        0xFE,
        (
            "I always think,\x01",
            "People thinking about the product are serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To hold back people like Mama\x01",
            "Every time, something new\x01",
            "I have to think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_C21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2CF")

    ChrTalk(
        0xFE,
        (
            "I've developed a way of boredom\x01",
            "One thing is human observation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many people come to department stores.\x01",
            "I do not get tired of surprising as I see people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_C31C")

    label("loc_C2CF")


    ChrTalk(
        0xFE,
        (
            "Many people come to department stores.\x01",
            "I do not get tired of surprising as I see people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C31C")

    Jump("loc_C415")

    label("loc_C321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3AC")

    ChrTalk(
        0xFE,
        (
            "Huh, Vacationsearch's\x01",
            "Is he a redhead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that person, last time\x01",
            "I went up to the rooftop\x01",
            "It looks like … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C415")

    label("loc_C3AC")


    ChrTalk(
        0xFE,
        (
            "Mom's window shopping\x01",
            "It is my daily routine to go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I got used to it, but boring is boring.\x02",
    )

    CloseMessageWindow()

    label("loc_C415")

    TalkEnd(0xFE)
    Return()

    # Function_29_B9EB end

    def Function_30_C419(): pass

    label("Function_30_C419")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C4D0")

    ChrTalk(
        0xFE,
        (
            "A huge tree floating in the sudden appearing air?\x01",
            "A particular problem at the moment\x01",
            "Do not you wake up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……Anyways,\x01",
            "Such a creepy thing will come soon\x01",
            "I want you to disappear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C4DE")
    Jump("loc_CD51")

    label("loc_C4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C521")

    ChrTalk(
        0xFE,
        (
            "Hmm … this is\x01",
            "It was unusual situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C5CE")

    ChrTalk(
        0xFE,
        (
            "Hmm, indeed at the present moment\x01",
            "In the place withdrew independence, the two major powers\x01",
            "Whether it is okay to believe it is a different problem … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nevertheless, the military threats of both countries are\x01",
            "Is it a problem that can not be ignored ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C5CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C68C")

    ChrTalk(
        0xFE,
        (
            "Hmm, as a potato tentatively became independent\x01",
            "Army able to compete against two major powers\x01",
            "Whether you can prepare is a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Empire's train cannon ……\x01",
            "Even if you take that weapon\x01",
            "There is not a single bridge such as cross bells?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C707")

    ChrTalk(
        0xFE,
        "I heard that I am like a demon … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To hear such a mysterious story\x01",
            "It is the first time that it was born.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C74C")

    ChrTalk(
        0xFE,
        (
            "It seems the outside is noisy,\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C7D8")

    ChrTalk(
        0xFE,
        (
            "Hmm, it's time for an old lady\x01",
            "You should consider the next gift seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I gave a brooch before … …\x01",
            "I am willing to make it a ring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C878")

    ChrTalk(
        0xFE,
        (
            "When I became this age, I am surely called independence\x01",
            "I did not expect to hear the words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it can be realized it would be fine,\x01",
            "That's not to say it's going well … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C91E")

    ChrTalk(
        0xFE,
        (
            "Hmm, it's a matter of meeting at the meeting\x01",
            "Osborne and Locksmith are in existence … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that iron skins,\x01",
            "What kind of measures the mayor is preparing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C978")

    ChrTalk(
        0xFE,
        "Well, I guess I'm about to leave home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "An old lady got angry, it was an enemy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_C978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CA16")

    ChrTalk(
        0xFE,
        (
            "Fofo, the rooftop here has a tower\x01",
            "It's a great spot to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The moment the curtain was removed the tower\x01",
            "A magnificent figure will burn with your eyes and go away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_CA16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CB44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAD1")

    ChrTalk(
        0xFE,
        (
            "It's time to start from tomorrow\x01",
            "A trade meeting will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Crois\x01",
            "When I was proposed to hold\x01",
            "Well, it was a surprising thing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way, really\x01",
            "It will be realized.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_CB3F")

    label("loc_CAD1")


    ChrTalk(
        0xFE,
        (
            "No, Trade Council\x01",
            "It really is what you realize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "IBC president to falling ashore\x01",
            "There is only thing that is concurrent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB3F")

    Jump("loc_CD51")

    label("loc_CB44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CBCC")

    ChrTalk(
        0xFE,
        (
            "Hmm, the selection of this store\x01",
            "Even if you look at it, it will tickle your heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which, to the old lady\x01",
            "It is supposed to be a gift for gifts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD51")

    label("loc_CBCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CD51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCD5")

    ChrTalk(
        0xFE,
        (
            "Hmm, even with the mayor of Croix\x01",
            "To McDowel's success\x01",
            "There is something truly spectacular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially the chairperson is so old with this\x01",
            "Even though it does not change, that work … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fofo, being old and growing more and more\x01",
            "Just like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_CD51")

    label("loc_CCD5")


    ChrTalk(
        0xFE,
        (
            "Fofo, being old and growing more and more\x01",
            "That's exactly this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "McDaely,\x01",
            "It is a star of our old generation generation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD51")

    TalkEnd(0xFE)
    Return()

    # Function_30_C419 end

    def Function_31_CD55(): pass

    label("Function_31_CD55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CD66")
    Jump("loc_CF41")

    label("loc_CD66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CDF9")

    ChrTalk(
        0xFE,
        (
            "Or, saying martial law\x01",
            "No way to be such a situation\x01",
            "I never tried it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha … obediently at home\x01",
            "Should I return home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF41")

    label("loc_CDF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE91")

    ChrTalk(
        0xFE,
        (
            "If anything stands independent, it will be in the Empire and the Republic\x01",
            "It seems like you do not have to pay Mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, Mr. Dieter's\x01",
            "Is not there a mistake in saying?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF41")

    label("loc_CE91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CED8")

    ChrTalk(
        0xFE,
        (
            "Service on a rainy day,\x01",
            "Department stores also do stylish things ~ are not they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF41")

    label("loc_CED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CF41")

    ChrTalk(
        0xFE,
        (
            "home work~?\x01",
            "You can not do such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way,\x01",
            "Dear Arios, you seem to be on business again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF41")

    TalkEnd(0xFE)
    Return()

    # Function_31_CD55 end

    def Function_32_CF45(): pass

    label("Function_32_CF45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CF56")
    Jump("loc_D0AD")

    label("loc_CF56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CFC1")

    ChrTalk(
        0xFE,
        (
            "But in this situation,\x01",
            "Where are they the same?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm lonely that I can not meet my family … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0AD")

    label("loc_CFC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D02E")

    ChrTalk(
        0xFE,
        (
            "Something recently, adults\x01",
            "It's noisy to be independent, independent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "In other words, what is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0AD")

    label("loc_D02E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D0AD")

    ChrTalk(
        0xFE,
        (
            "I mean,\x01",
            "That person is the manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a person bothers me from myself\x01",
            "It is amazing how crowded you are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0AD")

    TalkEnd(0xFE)
    Return()

    # Function_32_CF45 end

    def Function_33_D0B1(): pass

    label("Function_33_D0B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0C6")
    Call(0, 36)
    Jump("loc_D144")

    label("loc_D0C6")


    ChrTalk(
        0xFE,
        (
            "……Hmm? You sure are,\x01",
            "It was a police Nantoca section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, go quickly.\x01",
            "Would you carelessly speak to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D144")

    TalkEnd(0xFE)
    Return()

    # Function_33_D0B1 end

    def Function_34_D148(): pass

    label("Function_34_D148")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D15D")
    Call(0, 36)
    Jump("loc_D1E5")

    label("loc_D15D")


    ChrTalk(
        0xFE,
        (
            "Oh, I came on a trip for a long time\x01",
            "You should do somewhat more stimulating things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was towards the back street.\x01",
            "Would you like to go to a queen smelling store too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1E5")

    TalkEnd(0xFE)
    Return()

    # Function_34_D148 end

    def Function_35_D1E9(): pass

    label("Function_35_D1E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1FE")
    Call(0, 36)
    Jump("loc_D27C")

    label("loc_D1FE")


    ChrTalk(
        0xFE,
        (
            "I do not need it later.\x01",
            "Let's go to see the oval store, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's tough, as long as the car can do it\x01",
            "It's time to tune up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27C")

    TalkEnd(0xFE)
    Return()

    # Function_35_D1E9 end

    def Function_36_D280(): pass

    label("Function_36_D280")

    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)
    OP_4B(0x19, 0xFF)

    ChrTalk(
        0x17,
        (
            "Whew ……\x01",
            "Even if it says a department store in a trade city\x01",
            "It is not a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "Oh, our\x01",
            "Enemy to your glasses\x01",
            "Little put it on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Well, goods for common people\x01",
            "It seems to be large,\x01",
            "Is not it like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Today as well, only the liquor's knob\x01",
            "Let's buy it and let's go home.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3A0")
    Jump("loc_D449")

    label("loc_D3A0")


    ChrTalk(
        0x104,
        (
            "#00301F(Oh, these are rumors\x01",
            "Is it a naughty bonbon? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Indeed,\x01",
            "Hang out in a place like this … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(… Well, let's leave it now.)\x02",
    )

    CloseMessageWindow()

    label("loc_D449")

    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x17, 0x10)
    SetScenarioFlags(0x1, 5)
    Return()

    # Function_36_D280 end

    def Function_37_D45E(): pass

    label("Function_37_D45E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D4E3")

    ChrTalk(
        0xFE,
        (
            "I was stocking at home.\x01",
            "Because sweets disappeared\x01",
            "I hurried to buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D552")

    label("loc_D4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D552")

    ChrTalk(
        0xFE,
        (
            "When sweets have time\x01",
            "I have to buy it out\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it is called\x01",
            "It will be hard if you run out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D552")

    TalkEnd(0xFE)
    Return()

    # Function_37_D45E end

    def Function_38_D556(): pass

    label("Function_38_D556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D61D")

    ChrTalk(
        0xFE,
        (
            "Aside from that foolish trees,\x01",
            "After all I'm free.\x01",
            "It was cramped and unavoidable to be martial law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, it's tough,\x01",
            "Even if I insert it at Shiron Kun's place\x01",
            "I'd rather take it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D62B")
    Jump("loc_DF60")

    label("loc_D62B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D6D1")

    ChrTalk(
        0xFE,
        (
            "Inexplicable accident,?\x01",
            "Sure it's like that\x01",
            "There was a case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have overlooked it\x01",
            "We have sin … …\x01",
            "It may be as the President says.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D774")

    ChrTalk(
        0xFE,
        (
            "Of course it is natural …\x01",
            "Ursula hospital seems to be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shiron sister is also somewhat\x01",
            "It seems I'm getting depressed,\x01",
            "I can not do anything I am not good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D8DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D846")

    ChrTalk(
        0xFE,
        "What is it like to raise Ma, Mainz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From yesterday to the hospital,\x01",
            "People of the guard are one after another\x01",
            "It's talking about being carried ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, why is this useless?\x01",
            "There are people who do stupid things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_D8D9")

    label("loc_D846")


    ChrTalk(
        0xFE,
        (
            "From yesterday to the hospital,\x01",
            "People of the guard are one after another\x01",
            "It's talking about being carried ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn, why is this useless?\x01",
            "There are people who do stupid things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8D9")

    Jump("loc_DF60")

    label("loc_D8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D9A2")

    ChrTalk(
        0xFE,
        (
            "Among the people who came in the train accident\x01",
            "It seems that there were also seriously injured people … …\x01",
            "It seems that everyone else has taken it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of teachers will spend the night\x01",
            "Although it is said that it corresponded,\x01",
            "A doctor is really a human account book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D9EF")

    ChrTalk(
        0xFE,
        (
            "What is it? ambulance……?\x01",
            "It looked like a fairly large number ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_D9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DA7F")

    ChrTalk(
        0xFE,
        "Er, today's family wanted some items.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hello, I wish you a good year for your family\x01",
            "As much as you are being fed, at least\x01",
            "I should use it for shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DA7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DC51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBCA")

    ChrTalk(
        0xFE,
        (
            "To Shira Onee\x01",
            "Road of recommended male nurse,\x01",
            "I seriously tried to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being to take the exam\x01",
            "I have to wait until next year,\x01",
            "Good results have already come out on the trial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, next year's trainee exam\x01",
            "I will accept it for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you think that there is only one way\x01",
            "It became quite easy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_DC4C")

    label("loc_DBCA")


    ChrTalk(
        0xFE,
        (
            "Man, I have to work hard forward\x01",
            "You do not even learn anything that you learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow studying is more fun than before.\x01",
            "…… I'm just a little bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC4C")

    Jump("loc_DF60")

    label("loc_DC51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DC5F")
    Jump("loc_DF60")

    label("loc_DC5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_DC6D")
    Jump("loc_DF60")

    label("loc_DC6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DD19")

    ChrTalk(
        0xFE,
        (
            "In the city with an unveiling ceremony\x01",
            "It seems that it is floating ….\x01",
            "My heart sinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On that point, Shira Onee\x01",
            "Envy yourself with an easy personality.\x01",
            "I do not think it is true to my brothers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DD19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DDA9")

    ChrTalk(
        0xFE,
        "I wonder if I will be a Ronin in the coming year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something recently, my family's gaze\x01",
            "I feel like I'm becoming increasingly cold … ….\x01",
            "Huh, how do you live life?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DDA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DE63")

    ChrTalk(
        0xFE,
        (
            "Well, today's shopping is\x01",
            "Black pepper with mustard sauce,\x01",
            "Then to olive oil ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, the content of Pasiri\x01",
            "You can remember it without a note.\x01",
            "I want to use this memory ability for study.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF60")

    label("loc_DE63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DF60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF0B")

    ChrTalk(
        0xFE,
        (
            "Ursula hospital researcher exam,\x01",
            "Also it was useless this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Third honesty\x01",
            "I believed in words and challenged … …\x01",
            "I wonder if it is not suitable for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_DF60")

    label("loc_DF0B")


    ChrTalk(
        0xFE,
        (
            "Such a stupid one\x01",
            "Pacity for family use … today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, I do not think it's a bad idea.\x02",
    )

    CloseMessageWindow()

    label("loc_DF60")

    TalkEnd(0xFE)
    Return()

    # Function_38_D556 end

    def Function_39_DF64(): pass

    label("Function_39_DF64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E01F")

    ChrTalk(
        0xFE,
        (
            "Michishi wrapping\x01",
            "I'd like an L size,\x01",
            "It's a value for running away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will you collect pocket money and buy L size?\x01",
            "Should I buy an affordable S size right now …?\x01",
            "Well, I'm worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E091")

    label("loc_E01F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E091")

    ChrTalk(
        0xFE,
        (
            "Michino 's corner at a general store\x01",
            "It was true that I could do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I can not stay without this.\x02",
    )

    CloseMessageWindow()

    label("loc_E091")

    TalkEnd(0xFE)
    Return()

    # Function_39_DF64 end

    def Function_40_E095(): pass

    label("Function_40_E095")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E118")

    ChrTalk(
        0xFE,
        (
            "Well, if you buy a souvenir\x01",
            "I guess I'll head to the airport soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, but this time too\x01",
            "It was a very meaningful trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E215")

    label("loc_E118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E126")
    Jump("loc_E215")

    label("loc_E126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E191")

    ChrTalk(
        0xFE,
        (
            "No, the unveiling ceremony is\x01",
            "It was awesome than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel like running crossbells.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E215")

    label("loc_E191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E215")

    ChrTalk(
        0xFE,
        (
            "No, after all\x01",
            "Crossbell is a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tomorrow is the Orkis Tower\x01",
            "There is also an unveiling ceremony,\x01",
            "It seems to be enjoying this trip.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E215")

    TalkEnd(0xFE)
    Return()

    # Function_40_E095 end

    def Function_41_E219(): pass

    label("Function_41_E219")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E276")

    ChrTalk(
        0xFE,
        (
            "Oh, this trip is also\x01",
            "This is over.\x01",
            "It was really a blink of an eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E35A")

    label("loc_E276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E284")
    Jump("loc_E35A")

    label("loc_E284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E306")

    ChrTalk(
        0xFE,
        (
            "To see the unveiling ceremony on the rooftop here\x01",
            "It was a really good place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, in advance\x01",
            "It was worth the research.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E35A")

    label("loc_E306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E35A")

    ChrTalk(
        0xFE,
        (
            "Crossbell\x01",
            "It's a really exciting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No matter how many times I come, I will not get bored.\x02",
    )

    CloseMessageWindow()

    label("loc_E35A")

    TalkEnd(0xFE)
    Return()

    # Function_41_E219 end

    def Function_42_E35E(): pass

    label("Function_42_E35E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E445")

    ChrTalk(
        0xFE,
        (
            "ふむ、流石にNeston Managerの\x01",
            "There is a connotation in your word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am an entrepreneur and a businessman\x01",
            "Although it is still immature yet ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, through this position\x01",
            "What you can do for crossbell\x01",
            "I want to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_E4D8")

    label("loc_E445")


    ChrTalk(
        0xFE,
        (
            "I am an entrepreneur and a businessman\x01",
            "Although it is still immature yet ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, through this position\x01",
            "What you can do for crossbell\x01",
            "I want to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4D8")

    TalkEnd(0xFE)
    Return()

    # Function_42_E35E end

    def Function_43_E4DC(): pass

    label("Function_43_E4DC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the dinner of tonight,\x01",
            "I was shopping a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the table is noisy … …\x01",
            "Is there something wrong?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_E4DC end

    def Function_44_E555(): pass

    label("Function_44_E555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E5E9")

    ChrTalk(
        0xFE,
        (
            "Anything terrorists will hold a plenary session\x01",
            "There is a high possibility of attacking it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "はあ、Whew ……\x01",
            "In case of emergency\x01",
            "I wonder if it will be handy ~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB95")

    label("loc_E5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6A0")

    ChrTalk(
        0xFE,
        (
            "Today, I'm on a cool stone\x01",
            "It's a tremendous population ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Beautiful people too busy\x01",
            "I did not have time to count.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Well, Raymond is\x01",
            "As usual. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_E6FE")

    label("loc_E6A0")


    ChrTalk(
        0xFE,
        (
            "Today, I'm on a cool stone\x01",
            "It's a tremendous population ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Beautiful people too busy\x01",
            "I did not have time to count.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6FE")

    Jump("loc_EB95")

    label("loc_E703")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E85F")

    ChrTalk(
        0xFE,
        (
            "Oh, that child … …\x01",
            "Maybe even looking for a lost child\x01",
            "Are you doing it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "…… Who is lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I am going to visit crossbell now.\x01",
            "I am doing it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A2, 500)

    ChrTalk(
        0xFE,
        "Oh, you visited the crossbell?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Is this also a request for assistance?\x01",
            "The task of the support department is also hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, yeah.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_E8D2")

    label("loc_E85F")


    ChrTalk(
        0xFE,
        (
            "Well, for the time being\x01",
            "The vigilant regime is still the first day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I did not skip too much,\x01",
            "When you do your best in moderation\x01",
            "I guess it's OK.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8D2")

    Jump("loc_EB95")

    label("loc_E8D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAA2")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys.\x01",
            "It is hard work each other ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, whatever\x01",
            "This is the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FTo be here\x01",
            "Are you in charge of a department store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, strictly speaking of the central square\x01",
            "Commercial facilities in general though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because pretty beautiful people are seen\x01",
            "I'm preoccupied with caution ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105Fそ、Is that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Well, dreadfully\x01",
            "The motive is impure. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F(Well, well with that\x01",
            "If you are going to get in the mood\x01",
            "I think it's fine. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_EB95")

    label("loc_EAA2")


    ChrTalk(
        0xFE,
        (
            "Watch activity gets stiff shoulders.\x01",
            "Tiredness will blow away if you see beautiful woman ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Number of beautiful people up to this point, 31 people …\x01",
            "Mmmufu ~, I can expect more.\x02",
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

    label("loc_EB95")

    TalkEnd(0xFE)
    Return()

    # Function_44_E555 end

    def Function_45_EB99(): pass

    label("Function_45_EB99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBAE")
    Call(0, 46)
    Jump("loc_EC13")

    label("loc_EBAE")


    ChrTalk(
        0x21,
        (
            "#00603FI will take the shoes I asked from now\x01",
            "Try it on.\x02\x03",
            "#00600FWould you like me to keep in the way?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC13")

    TalkEnd(0xFE)
    Return()

    # Function_45_EB99 end

    def Function_46_EC17(): pass

    label("Function_46_EC17")

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
            "Mr. Dudley,\x01",
            "Here is the item of your order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#11P#00602FHmm, let's try it quickly ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x21, 0x101, 500)

    ChrTalk(
        0x21,
        (
            "#11P#00600FMum, you guys.\x01",
            "What on earth are you doing in such places?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FNo matter what you say … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FRather, I would like to ask\x01",
            "This is the story.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#12P#10305FWell,\x01",
            "It looks like a lot of luxury goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FLeather shoes … is it.\x01",
            "Is it some brand name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00603FHun, this me\x01",
            "Just listening to the brand\x01",
            "Do not do it with those who are willing.\x02\x03",
            "#00602F…… This is custom made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FOkay, being stuck\x01",
            "You are coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FOr-made leather shoes ……\x02\x03",
            "#00003FBasically\x01",
            "It's all sneakers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    ChrTalk(
        0x21,
        (
            "#11P#00601F…… Bannings.\x01",
            "What do you mean?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00000FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00600FAs if leather shoes are down\x01",
            "I talk that he said it.\x02\x03",
            "#00603FBut …\x01",
            "That idea is wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FOh, I … separately …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00602FIn shoes\x01",
            "There is no material deep inside as much as leather.\x02\x03",
            "#00604FFamiliar enough to wear,\x01",
            "And unless you neglect your care,\x01",
            "The texture gets deeper … …\x02\x03",
            "#00601FYou are the best part of this sneakers\x01",
            "Do you think you can taste it?\x02",
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
        "#6P#00206FWhy is it so hot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109FYes, honestly I feel unexpected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11P#00606FGo, goose …\x01",
            "A story has derailed a bit.\x02\x03",
            "#00600FAnyway, what I am here is\x01",
            "It happened that I had free time.\x02\x03",
            "Naturally, I have a future plan.\x01",
            "Would you like me to keep in the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FRyo, OK.\x02",
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

    # Function_46_EC17 end

    def Function_47_F3CC(): pass

    label("Function_47_F3CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F45D")

    ChrTalk(
        0x1B,
        (
            "#02106FYeah yeah, I know.\x02\x03",
            "#02109FAnyway I,\x01",
            "Manufacturers put here\x01",
            "It must not be a pen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_F4D7")

    label("loc_F45D")


    ChrTalk(
        0x1B,
        (
            "#02105FTo the model change\x01",
            "The lineup has been strengthened.\x02\x03",
            "#02109FHmm, this one\x01",
            "Should I try out the type too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4D7")

    TalkEnd(0xFE)
    Return()

    # Function_47_F3CC end

    def Function_48_F4DB(): pass

    label("Function_48_F4DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F5BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F556")

    ChrTalk(
        0xFE,
        (
            "Grace先輩、\x01",
            "Please do it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So what?\x01",
            "Are you making it long?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x2, 0)
    Jump("loc_F5B6")

    label("loc_F556")


    ChrTalk(
        0xFE,
        (
            "Haha, suddenly ink\x01",
            "Because I'm out of shopping so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still have time at all,\x01",
            "Something uneasy ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5B6")

    Jump("loc_F6AB")

    label("loc_F5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F6AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F657")

    ChrTalk(
        0xFE,
        (
            "Uh, an antidote for recovery drugs,\x01",
            "Then do I need a care medicine …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Preparation of medical kit … ….\x01",
            "Are you going to go somewhere from now? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_F6AB")

    label("loc_F657")


    ChrTalk(
        0xFE,
        (
            "EP charge,\x01",
            "Is not it necessary …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that,\x01",
            "I'd like to have some smoked balls too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6AB")

    TalkEnd(0xFE)
    Return()

    # Function_48_F4DB end

    def Function_49_F6AF(): pass

    label("Function_49_F6AF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "2F Boutique \"Lucca\"\x01",
            "２Ｆ　Hansonシューズ\x01",
            "２Ｆ　アクセサリ《Baker》\x01",
            "１Ｆ　《Regionフード》\x01",
            "１Ｆ　雑貨コーナー《Southwark》\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ If you have any questions\x01",
            "Front comprehensive information at\x01",
            "Please do not hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_49_F6AF end

    def Function_50_F7C7(): pass

    label("Function_50_F7C7")

    EventBegin(0x0)
    Fade(500)
    OP_68(-15210, 1000, 9790, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_F84E")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x104, -14350, 0, 8000, 0)
    Jump("loc_F8ED")

    label("loc_F84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_F8A0")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x109, -14350, 0, 8000, 0)
    Jump("loc_F8ED")

    label("loc_F8A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_F8ED")
    SetChrPos(0x1A2, -15460, 0, 9600, 0)
    SetChrPos(0x102, -14620, 0, 9600, 0)
    SetChrPos(0x101, -15860, 0, 8000, 0)
    SetChrPos(0x105, -14350, 0, 8000, 0)

    label("loc_F8ED")

    OP_0D()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PHere, maybe this\x01",
            "\"Michishi Gurumi\" …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHow come?\x01",
            "It's not even a theme park ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, surely recently\x01",
            "It is a dedicated corner that I made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMr. Shin is miserable\x01",
            "Are you interested?\x02",
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
            "Dude\x01",
            "I feel like going to buzz! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "What is it?\x01",
            "I am carrying a black moon like this …\x01",
            "There will be something rude!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FB8F")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FAE9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FAE9)
    Sleep(50)

    def lambda_FAF9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FAF9)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FShin Shin … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FEven if it does not become irritating to that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00309FOh, and to it\x01",
            "Kuroki has nothing to do with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8E")

    label("loc_FB8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FC94")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FBE8():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FBE8)
    Sleep(50)

    def lambda_FBF8():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FBF8)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FShin Shin … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FEven if it does not become irritating to that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FYeah, and Kuroki are\x01",
            "It does not matter at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8E")

    label("loc_FC94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FD8E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FCED():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FCED)
    Sleep(50)

    def lambda_FCFD():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_FCFD)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105FShin Shin … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FEven if it does not become irritating to that … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FOh, and to it\x01",
            "Kuroki has nothing to do with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD8E")

    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "Funk, anyway -\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "#12PWhat is this …?\x01",
            "Times Department store limited goods,\x01",
            "\"Tikkaku Mitsushii\" What?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        "#12P- Ha!\x02",
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
            "And anyway, this is\x01",
            "Kodomo is also a good owner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I will\x01",
            "I'm not interested!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_FF24")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_FFD1")

    label("loc_FF24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_FF7D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_FFD1")

    label("loc_FF7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_FFD1")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_FFD1")


    ChrTalk(
        0x101,
        "#12P#00012F(Wow, that's easy to understand …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F(Yes, I'm interested in this\x01",
            "It's like saying that. )\x02",
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

    # Function_50_F7C7 end

    def Function_51_10079(): pass

    label("Function_51_10079")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-960, 3000, 1530, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10105")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x104, 600, 0, 2900, 180)
    Jump("loc_101A4")

    label("loc_10105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10157")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x109, 600, 0, 2900, 180)
    Jump("loc_101A4")

    label("loc_10157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_101A4")
    SetChrPos(0x1A2, -300, 0, 1700, 0)
    SetChrPos(0x102, 300, 0, 1700, 0)
    SetChrPos(0x101, -600, 0, 2900, 180)
    SetChrPos(0x105, 600, 0, 2900, 180)

    label("loc_101A4")

    OP_68(-960, 1600, 1530, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWell, well then\x01",
            "Let's aim at the rooftop while turning around the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12POh, I will leave the guide!\x02",
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

    # Function_51_10079 end

    def Function_52_10258(): pass

    label("Function_52_10258")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17440, 1600, 19460, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16140, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_102E5")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x104, -15690, 30, 21350, 270)
    Jump("loc_10384")

    label("loc_102E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10337")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x109, -15690, 30, 21350, 270)
    Jump("loc_10384")

    label("loc_10337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10384")
    SetChrPos(0x1A2, -16890, 0, 19650, 0)
    SetChrPos(0x102, -16040, 0, 19650, 315)
    SetChrPos(0x101, -17110, 30, 21350, 180)
    SetChrPos(0x105, -15690, 30, 21350, 270)

    label("loc_10384")

    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A2,
        (
            "#12PHey, from a little while ago\x01",
            "What were you doing sneaking up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, actually I was buying this.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10411")

    def lambda_103FF():

        label("loc_103FF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_103FF")

    QueueWorkItem2(0x104, 1, lambda_103FF)
    Jump("loc_1044C")

    label("loc_10411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10431")

    def lambda_1041F():

        label("loc_1041F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1041F")

    QueueWorkItem2(0x109, 1, lambda_1041F)
    Jump("loc_1044C")

    label("loc_10431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1044C")

    def lambda_1043F():

        label("loc_1043F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1043F")

    QueueWorkItem2(0x105, 1, lambda_1043F)

    label("loc_1044C")

    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1048A")
    EndChrThread(0x104, 0x1)

    def lambda_1046D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1046D)
    Sleep(50)

    def lambda_1047D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1047D)
    Jump("loc_104E3")

    label("loc_1048A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_104B9")
    EndChrThread(0x109, 0x1)

    def lambda_1049C():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1049C)
    Sleep(50)

    def lambda_104AC():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_104AC)
    Jump("loc_104E3")

    label("loc_104B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_104E3")
    EndChrThread(0x105, 0x1)

    def lambda_104CB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_104CB)
    Sleep(50)

    def lambda_104DB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104DB)

    label("loc_104E3")

    Sleep(300)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is Shin\x01",
            "\"Mikoshi Tikutaku\" handed over.\x07\x00\x02",
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
        "#12PThis is limited to this department store ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FIndeed, that was it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_105ED")

    ChrTalk(
        0x104,
        "#11P#00309FHeck, it is quite disgusting, is not it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1065E")

    label("loc_105ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_10626")

    ChrTalk(
        0x109,
        "#11P#10109FHuhuu, I feel like a lot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1065E")

    label("loc_10626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1065E")

    ChrTalk(
        0x105,
        "#11P#10302FHuh, you are pretty obvious.\x02",
    )

    CloseMessageWindow()

    label("loc_1065E")

    OP_63(0x1A2, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "#12PWhat is it, kore.\x01",
            "What do you want of me like this …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, well\x01",
            "It is said that gifts, though.\x02\x03",
            "By saying today's memorial,\x01",
            "Would you please take it anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PToday's memorial ……\x02",
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
            "#12P… and so I bought it like this\x01",
            "You can not throw it away.\x01",
            "I will accept it for that.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A2, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PHowever, I will tell you only this\x01",
            "This stuffed animal is\x01",
            "Even my hobby is nothing!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_10887")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_10934")

    label("loc_10887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_108E0")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_10934")

    label("loc_108E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_10934")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_10934")


    ChrTalk(
        0x101,
        "#00000FOh, okay.\x02",
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

    # Function_52_10258 end

    def Function_53_10982(): pass

    label("Function_53_10982")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThere is no time to guide outside.\x02\x03",
            "Let's head around the store properly and head towards the roof.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -600, 30, 1000, 0)
    EventEnd(0x4)
    Return()

    # Function_53_10982 end

    SaveToFile()

Try(main)
