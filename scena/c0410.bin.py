from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0410.bin",                # FileName
        "c0410",                    # MapName
        "c0410",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0410",                  # 0
        "Karelia",                # 1
        "Manager Balsamo",        # 2
        "Receptionist Rolando",   # 3
        "Troupe Chief Aban",      # 4
        "Eugene",                 # 5
        "Theodore",               # 6
        "Nikol",                  # 7
        "Pliｳ",                  # 8
        "Celine",                 # 9
        "Reporter Noticia",       # 10
        "Sully",                  # 11
        "Ilya",                   # 12
        "Mary",                   # 13
        "Rixia",                  # 14
        "Heintz",                 # 15
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch24200.itc",                   # 01
        "chr/ch28900.itc",                   # 02
        "chr/ch05102.itc",                   # 03
        "chr/ch05200.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch25900.itc",                   # 06
        "chr/ch27500.itc",                   # 07
        "chr/ch28700.itc",                   # 08
        "chr/ch28702.itc",                   # 09
        "chr/ch28800.itc",                   # 0A
        "chr/ch29000.itc",                   # 0B
        "chr/ch29100.itc",                   # 0C
        "chr/ch29102.itc",                   # 0D
        "chr/ch36600.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch36700.itc",                   # 10
        "chr/ch36900.itc",                   # 11
        "apl/ch50257.itc",                   # 12
        "chr/ch09800.itc",                   # 13
        "chr/ch10000.itc",                   # 14
        "chr/ch36800.itc",                   # 15
        "chr/ch47900.itc",                   # 16
        "chr/ch14100.itc",                   # 17
        "chr/ch37000.itc",                   # 18
    ))

    DeclNpc(4294843496, 0,       4294965007, 180,  261,  0x0, 0,   5,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294965046, 2500,    15000,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294925206, 5599,    102569,  135,  389,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294842087, 0,       4294966817, 270,  261,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294879987, 0,       4294965316, 90,   261,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294917357, 0,       13039,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(4294873936, 0,       4294965296, 180,  261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294842046, 0,       4294966836, 270,  261,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4294963376, 0,       4294966647, 0,    389,  0x0, 0,   22,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(4294845136, 0,       1000,    270,  389,  0x0, 0,   23,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(4294879756, 50,      4294967267, 90,   389,  0x0, 0,   3,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  11, 0x0000)
    DeclActor(4294841406, 0,       4530,    1200,    4294841406, 2000,    4530,    0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1068, 0)                                       # 0

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4DC",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_532",          # 03, 3
        "Function_4_55D",          # 04, 4
        "Function_5_588",          # 05, 5
        "Function_6_CC0",          # 06, 6
        "Function_7_DE2",          # 07, 7
        "Function_8_E8F",          # 08, 8
        "Function_9_1210",         # 09, 9
        "Function_10_15FE",        # 0A, 10
        "Function_11_2233",        # 0B, 11
        "Function_12_2237",        # 0C, 12
        "Function_13_2BB4",        # 0D, 13
        "Function_14_3003",        # 0E, 14
        "Function_15_3178",        # 0F, 15
        "Function_16_32F4",        # 10, 16
        "Function_17_3620",        # 11, 17
        "Function_18_3A30",        # 12, 18
        "Function_19_3B81",        # 13, 19
        "Function_20_412B",        # 14, 20
        "Function_21_42C3",        # 15, 21
        "Function_22_4577",        # 16, 22
        "Function_23_477F",        # 17, 23
        "Function_24_4BEC",        # 18, 24
        "Function_25_4DAB",        # 19, 25
        "Function_26_5452",        # 1A, 26
        "Function_27_5790",        # 1B, 27
        "Function_28_5A7A",        # 1C, 28
        "Function_29_5B3C",        # 1D, 29
        "Function_30_5E77",        # 1E, 30
        "Function_31_6608",        # 1F, 31
        "Function_32_72B2",        # 20, 32
        "Function_33_72FD",        # 21, 33
        "Function_34_7348",        # 22, 34
        "Function_35_7393",        # 23, 35
        "Function_36_73DE",        # 24, 36
        "Function_37_7429",        # 25, 37
        "Function_38_7474",        # 26, 38
        "Function_39_74AB",        # 27, 39
        "Function_40_74D7",        # 28, 40
        "Function_41_8759",        # 29, 41
        "Function_42_87A4",        # 2A, 42
        "Function_43_87EF",        # 2B, 43
        "Function_44_9261",        # 2C, 44
        "Function_45_9290",        # 2D, 45
        "Function_46_92BF",        # 2E, 46
        "Function_47_92EE",        # 2F, 47
        "Function_48_931D",        # 30, 48
        "Function_49_99FF",        # 31, 49
        "Function_50_9A23",        # 32, 50
        "Function_51_A0F6",        # 33, 51
        "Function_52_AAC2",        # 34, 52
        "Function_53_AE99",        # 35, 53
        "Function_54_B39A",        # 36, 54
        "Function_55_B434",        # 37, 55
        "Function_56_B4C4",        # 38, 56
        "Function_57_B554",        # 39, 57
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_464"),
        (1, "loc_470"),
        (2, "loc_47C"),
        (3, "loc_488"),
        (4, "loc_494"),
        (5, "loc_4A0"),
        (6, "loc_4AC"),
        (SWITCH_DEFAULT, "loc_4B8"),
    )


    label("loc_464")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_470")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_47C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_488")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_494")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4DB")

    Return()

    # Function_0_42C end

    def Function_1_4DC(): pass

    label("Function_1_4DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_506")
    OP_94(0xFE, 0xFFFFF402, 0xFFFFF59C, 0xB72, 0xD0C, 0x3E8)
    Sleep(300)
    Jump("Function_1_4DC")

    label("loc_506")

    Return()

    # Function_1_4DC end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_531")
    OP_94(0xFE, 0xFFFE9F26, 0x5B4, 0xFFFE9346, 0xFFFFFA56, 0x3E8)
    Sleep(300)
    Jump("Function_2_507")

    label("loc_531")

    Return()

    # Function_2_507 end

    def Function_3_532(): pass

    label("Function_3_532")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55C")
    OP_94(0xFE, 0xFFFE17C2, 0xFFFFF8C6, 0xFFFE244C, 0x546, 0x3E8)
    Sleep(300)
    Jump("Function_3_532")

    label("loc_55C")

    Return()

    # Function_3_532 end

    def Function_4_55D(): pass

    label("Function_4_55D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_587")
    OP_94(0xFE, 0xFFFF403E, 0x201C, 0xFFFF3760, 0x42E0, 0x3E8)
    Sleep(300)
    Jump("Function_4_55D")

    label("loc_587")

    Return()

    # Function_4_55D end

    def Function_5_588(): pass

    label("Function_5_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_629")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xF, -6840, 0, 7100, 180)
    SetChrPos(0xB, -6840, 0, 6000, 0)
    SetChrPos(0x9, 3940, 0, 2900, 90)
    SetChrPos(0x8, -125110, 0, -1840, 270)
    SetChrPos(0x10, -90070, 0, 0, 270)
    SetChrPos(0xE, -91860, 0, 0, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_624")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_624")

    Jump("loc_B24")

    label("loc_629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6A0")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xF, -90070, 0, 0, 270)
    SetChrPos(0xD, -91860, 0, 0, 90)
    SetChrPos(0x8, -123770, 0, 1000, 90)
    SetChrPos(0x12, -122160, 0, 1000, 270)
    SetChrChipByIndex(0x12, 0x17)
    SetChrChipByIndex(0xD, 0x10)
    SetChrChipByIndex(0xF, 0x11)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x12, 0x10)
    Jump("loc_B24")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6C7")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_740")
    SetChrPos(0xC, -123770, 0, 1000, 90)
    SetChrPos(0xD, -122160, 0, 1000, 270)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -48960, 0, 11170, 0)
    SetChrPos(0x10, -48960, 0, 12870, 180)
    SetChrPos(0xF, -90070, 0, 0, 270)
    SetChrPos(0x8, -91860, 0, 0, 90)
    Jump("loc_B24")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_784")
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xF, -90070, 0, 0, 270)
    SetChrPos(0x8, -91860, 0, 0, 90)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_B24")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7B0")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7DC")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_808")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8FB")
    SetChrPos(0x10, -87750, 200, -2320, 90)
    SetChrPos(0x8, -88360, 0, -980, 135)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_847")
    SetChrFlags(0x8, 0x10)

    label("loc_847")

    SetChrChipByIndex(0x10, 0xD)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0xC, -124240, 0, -2210, 180)
    SetChrPos(0xF, -125280, 0, -1530, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_893")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_8A1")

    label("loc_893")

    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)

    label("loc_8A1")

    SetChrChipByIndex(0xF, 0x11)
    SetChrChipByIndex(0xC, 0xE)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -90360, 0, 4590, 270)
    SetChrPos(0xD, -92070, 0, 4590, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    SetChrFlags(0xD, 0x10)

    label("loc_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE")
    SetChrFlags(0xE, 0x10)

    label("loc_8EE")

    SetChrChipByIndex(0xE, 0x15)
    SetChrChipByIndex(0xD, 0x10)
    Jump("loc_B24")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9A4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -122610, 0, 2100, 45)
    SetChrPos(0x8, -121870, 0, 3110, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_93F")

    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x13, 0x3)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0xF, -92910, 0, 5840, 180)
    SetChrPos(0x10, -92910, 0, 4520, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_990")
    SetChrFlags(0xF, 0x10)

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F")
    SetChrFlags(0x10, 0x10)

    label("loc_99F")

    Jump("loc_B24")

    label("loc_9A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9C6")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A7C")
    SetChrPos(0xC, -123770, 0, 1000, 90)
    SetChrPos(0xD, -122160, 0, 1000, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A00")
    SetChrFlags(0xC, 0x10)

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0F")
    SetChrFlags(0xD, 0x10)

    label("loc_A0F")

    SetChrChipByIndex(0xC, 0xE)
    SetChrChipByIndex(0xD, 0x10)
    SetChrPos(0x8, -91860, 0, 1270, 135)
    SetChrPos(0x10, -89460, 0, 1670, 225)
    SetChrPos(0xF, -90070, 0, -590, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A59")
    SetChrFlags(0x8, 0x10)

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A68")
    SetChrFlags(0x10, 0x10)

    label("loc_A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A77")
    SetChrFlags(0xF, 0x10)

    label("loc_A77")

    Jump("loc_B24")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AA8")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_B24")

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B24")
    SetChrPos(0x10, -90860, 0, 5430, 180)
    SetChrPos(0xC, -90360, 0, -590, 270)
    SetChrPos(0xD, -92070, 0, -590, 90)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x8, -123770, 0, 1000, 90)
    SetChrPos(0xF, -122160, 0, 1000, 270)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B24")
    SetChrFlags(0xF, 0x10)

    label("loc_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_B3F")

    Jump("loc_C22")

    label("loc_B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5F")
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_B5F")

    Jump("loc_C22")

    label("loc_B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B72")
    Jump("loc_C22")

    label("loc_B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B80")
    Jump("loc_C22")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B8E")
    Jump("loc_C22")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B9C")
    Jump("loc_C22")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_BAD")
    Event(0, 53)
    Jump("loc_C22")

    label("loc_BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_BBE")
    Event(0, 53)
    Jump("loc_C22")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BCC")
    Jump("loc_C22")

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_BDA")
    Jump("loc_C22")

    label("loc_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BE8")
    Jump("loc_C22")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BF6")
    Jump("loc_C22")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C07")
    Event(0, 52)
    Jump("loc_C22")

    label("loc_C07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C22")
    SetMapFlags(0x10000000)
    Event(0, 50)

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C3B")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_C63")

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C54")
    ClearScenarioFlags(0x22, 1)
    SetMapFlags(0x10000000)
    Event(0, 43)
    Jump("loc_C63")

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_C63")
    ClearScenarioFlags(0x22, 2)
    Event(0, 49)

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C93")
    SetMapFlags(0x10000000)
    Event(0, 48)
    Jump("loc_CBF")

    label("loc_C93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    Event(0, 40)

    label("loc_CBF")

    Return()

    # Function_5_588 end

    def Function_6_CC0(): pass

    label("Function_6_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF3")

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D0F")
    OP_10(0x0, 0x0)
    OP_10(0x11, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_D34")

    label("loc_D0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2B")
    OP_10(0x0, 0x0)
    OP_10(0x11, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_D34")

    label("loc_D2B")

    OP_10(0x0, 0x1)
    OP_10(0x11, 0x0)
    OP_10(0x10, 0x0)

    label("loc_D34")

    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D56")
    ModifyEventFlags(0, 0, 0x80)
    OP_1B(0x3, 0xFF, 0xFFFF)

    label("loc_D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6A")
    ClearMapObjFlags(0x1D, 0x4)

    label("loc_D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D82")
    OP_1B(0x4, 0x0, 0x39)

    label("loc_D82")

    Jump("loc_DAA")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAA")
    OP_1B(0x4, 0x0, 0x39)

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC2")
    ModifyEventFlags(1, 5, 0x80)
    OP_1B(0x5, 0x0, 0x36)

    label("loc_DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD4")
    OP_65(0x0, 0x1)

    label("loc_DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_DE1")
    OP_65(0x0, 0x1)

    label("loc_DE1")

    Return()

    # Function_6_CC0 end

    def Function_7_DE2(): pass

    label("Function_7_DE2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a car magazine,\x01",
            ""Orbal Car Nobility".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36D, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8B")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Noble\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36D, 1)

    label("loc_E8B")

    TalkEnd(0xFF)
    Return()

    # Function_7_DE2 end

    def Function_8_E8F(): pass

    label("Function_8_E8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F39")

    ChrTalk(
        0xFE,
        (
            "Actually, Ilya's support for all of\x01",
            "us here at the troupe came through\x01",
            "by orbal communication just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like Ilya gives\x01",
            "us all courage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120C")

    label("loc_F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F47")
    Jump("loc_120C")

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F55")
    Jump("loc_120C")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F63")
    Jump("loc_120C")

    label("loc_F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F71")
    Jump("loc_120C")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F7F")
    Jump("loc_120C")

    label("loc_F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F8D")
    Jump("loc_120C")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F9B")
    Jump("loc_120C")

    label("loc_F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FA9")
    Jump("loc_120C")

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC4")
    Call(0, 9)
    Jump("loc_11D4")

    label("loc_FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111D")

    ChrTalk(
        0xB,
        (
            "Hmm... I of all people. Because\x01",
            "of the excitement, I failed to\x01",
            "notice your presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, thank goodness\x01",
            "it was you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If this had been seen by another\x01",
            "member... Ilya would have bashed\x01",
            "them a hundred times.\x02",
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
    SetScenarioFlags(0x0, 0)
    Jump("loc_11D4")

    label("loc_111D")


    ChrTalk(
        0xFE,
        (
            "Hmm... I of all people. Because\x01",
            "of the excitement, I failed to\x01",
            "notice your presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this had been seen by another\x01",
            "member... Ilya would have bashed\x01",
            "them a hundred times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D4")

    Jump("loc_120C")

    label("loc_11D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11E7")
    Jump("loc_120C")

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11F5")
    Jump("loc_120C")

    label("loc_11F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1203")
    Jump("loc_120C")

    label("loc_1203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_120C")

    label("loc_120C")

    TalkEnd(0xFE)
    Return()

    # Function_8_E8F end

    def Function_9_1210(): pass

    label("Function_9_1210")

    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "I tried making that\x01",
            "costume design we talked\x01",
            "about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What do you think of\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, very good! With this\x01",
            "style, I don't think there\x01",
            "will be any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll arrange a meeting\x01",
            "for Ilya to give her\x01",
            "opinion on it later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(A new costume design?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(...I'm very excited to\x01",
            "see it.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0x8,
        "My, you all are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm, who, exactly...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "Oh, you are... Could you\x01",
            "have overheard?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140B")

    ChrTalk(
        0x101,
        "#00006FUmm... Sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1503")

    label("loc_140B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143C")

    ChrTalk(
        0x102,
        "#00106FUmm... Excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1503")

    label("loc_143C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146D")

    ChrTalk(
        0x103,
        "#00206FUmm... Excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1503")

    label("loc_146D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(
        0x104,
        "#00306FAhh... Sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1503")

    label("loc_149A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(
        0x109,
        "#10106FU-Umm... Sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1503")

    label("loc_14C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1503")

    ChrTalk(
        0x105,
        (
            "#10302FHaha, who knows? What\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1503")


    ChrTalk(
        0xB,
        "...Well, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, that conversation\x01",
            "is a top secret matter to\x01",
            "this theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You all didn't hear\x01",
            "anything, and didn't see\x01",
            "anything. Understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yes... We understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FW-We promise.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x14B, 5)
    Return()

    # Function_9_1210 end

    def Function_10_15FE(): pass

    label("Function_10_15FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(
        0xFE,
        (
            "With Crossbell surrounded like this,\x01",
            "the situation is even more chaotic,\x01",
            "but... We don't have time fret over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must do only one thing― Do all\x01",
            "that we can to resume our\x01",
            "performances as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222F")

    label("loc_16EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_17FF")

    ChrTalk(
        0xFE,
        (
            "The sudden declaration of martial\x01",
            "law and travel restrictions were\x01",
            "baffling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We discussed it, and all members\x01",
            "decided to stay here and practice\x01",
            "instead of returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, everyone is\x01",
            "so focused on dance\x01",
            "practice, it's shocking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222F")

    label("loc_17FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_193D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C3")

    ChrTalk(
        0xFE,
        (
            "Karelia is on her way to\x01",
            "Ilya's hospital room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Ilya still\x01",
            "hasn't awakened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us here at the\x01",
            "theater believe she will\x01",
            "awaken someday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1938")

    label("loc_18C3")


    ChrTalk(
        0xFE,
        (
            "It seems Ilya still\x01",
            "hasn't awakened, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us here at the\x01",
            "theater believe she will\x01",
            "awaken someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1938")

    Jump("loc_222F")

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C62")

    ChrTalk(
        0x9,
        "Oh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FIs the entire troupe\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes. For now, our entire\x01",
            "membership shows up\x01",
            "daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, ever since that\x01",
            "day, Rixia has not shown\x01",
            "her face even once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, all of us here at the\x01",
            "theater are taking turns visiting\x01",
            "Ilya's hospital room to support her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sully will be there all\x01",
            "day long today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFC")

    ChrTalk(
        0x109,
        "#10105FSully...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B32")

    label("loc_1AFC")


    ChrTalk(
        0x109,
        (
            "#10100FYes... We saw her just\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I see...\x02",
    )

    CloseMessageWindow()

    label("loc_1B32")


    ChrTalk(
        0x9,
        (
            "...However, I still\x01",
            "don't believe it myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think this may be a\x01",
            "long dream... I suppose\x01",
            "that can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FManager...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...Sorry for rambling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, thank you for\x01",
            "visiting the theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please visit anytime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Thank you for your\x01",
            "concern.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 4)
    SetScenarioFlags(0x18C, 7)
    Jump("loc_1CD5")

    label("loc_1C62")


    ChrTalk(
        0xFE,
        (
            "Sully is visiting Ilya's\x01",
            "hospital room today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I want her to\x01",
            "regain consciousness\x01",
            "quickly, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD5")

    Jump("loc_222F")

    label("loc_1CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(
        0xFE,
        (
            "This afternoon is the long-awaited\x01",
            "premiere of the "Golden Sun,\x01",
            "Silver Moon" renewal performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The dances are\x01",
            "perfect... I am certain\x01",
            "everyone will love it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222F")

    label("loc_1D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1EB8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E17")

    ChrTalk(
        0xFE,
        (
            "If you like, I'll call\x01",
            "Sully for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure speaking with\x01",
            "you will be a good break\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB3")

    label("loc_1E17")


    ChrTalk(
        0xFE,
        (
            "Sully said not to tell Ilya\x01",
            "where she went, but... To her\x01",
            "it was obvious, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It seems Ilya\x01",
            "can't leave Sully alone,\x01",
            "no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB3")

    Jump("loc_222F")

    label("loc_1EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1EC6")
    Jump("loc_222F")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1ED4")
    Jump("loc_222F")

    label("loc_1ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE2")

    ChrTalk(
        0xFE,
        (
            "The renewal performance's\x01",
            "opening night is just\x01",
            "three days away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, we're planning\x01",
            "our final dress rehearsal\x01",
            "for all day tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only troupe staff will be\x01",
            "permitted entry into the theater,\x01",
            "so please be aware of that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2083")

    label("loc_1FE2")


    ChrTalk(
        0xFE,
        (
            "We're planning our final\x01",
            "dress rehearsal for all\x01",
            "day tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only troupe staff will be\x01",
            "permitted entry into the theater,\x01",
            "so please be aware of that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2083")

    Jump("loc_222F")

    label("loc_2088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_211A")

    ChrTalk(
        0xFE,
        (
            "Yesterday's dances were\x01",
            "magnificent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But more importantly, it\x01",
            "seems the heads of state were\x01",
            "pleased with our performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222F")

    label("loc_211A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2128")
    Jump("loc_222F")

    label("loc_2128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21AB")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you all.\x01",
            "Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking for Ilya,\x01",
            "she is with Rixia and the\x01",
            "troupe manager on stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222F")

    label("loc_21AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21B9")
    Jump("loc_222F")

    label("loc_21B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_222F")

    ChrTalk(
        0xFE,
        (
            "If you are looking for\x01",
            "Ilya or Rixia, they\x01",
            "should be in the hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please go\x01",
            "see them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222F")

    TalkEnd(0xFE)
    Return()

    # Function_10_15FE end

    def Function_11_2233(): pass

    label("Function_11_2233")

    Call(0, 12)
    Return()

    # Function_11_2233 end

    def Function_12_2237(): pass

    label("Function_12_2237")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2311")

    ChrTalk(
        0xA,
        (
            "There's still plenty of chaos to go\x01",
            "around. Still, we're gradually getting\x01",
            "in contact with other locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, the first thing we\x01",
            "need to do is pull together\x01",
            "all the information we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_2311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2506")

    ChrTalk(
        0xA,
        (
            "Right after the State Guard was\x01",
            "formed, we got a request for a special\x01",
            "performance for the citizens, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "With our cast incomplete, it was\x01",
            "impossible to do it immediately.\x01",
            "This took some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After that, the troupe leader wrote\x01",
            "the script himself and everyone\x01",
            "practiced through today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Given the situation, the\x01",
            "government would never let\x01",
            "us hold a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, no matter the\x01",
            "situation, we intend to make\x01",
            "the performance a reality.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_258F")

    label("loc_2506")


    ChrTalk(
        0xA,
        (
            "Given the situation, the\x01",
            "government would never let\x01",
            "us hold a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, we plan to hold\x01",
            "it no matter what\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258F")

    Jump("loc_2BB0")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_269E")

    ChrTalk(
        0xA,
        (
            "Although Crossbell is in an\x01",
            "important position right now, there\x01",
            "is only one thing we must do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And that is, to continue to\x01",
            "believe in Ilya's recovery and\x01",
            "continue to practice daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I will support her with\x01",
            "everything I have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_271D")

    label("loc_269E")


    ChrTalk(
        0xA,
        (
            "We must do only one thing.\x01",
            "Support Ilya and continue\x01",
            "to practice daily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I will support her with\x01",
            "everything I have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_271D")

    Jump("loc_2BB0")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_282C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27DB")

    ChrTalk(
        0xA,
        (
            "Just who was that red-\x01",
            "headed girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, just where did\x01",
            "Rixia...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway... There are a lot\x01",
            "of inexplicable things\x01",
            "right now and I'm confused.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2827")

    label("loc_27DB")


    ChrTalk(
        0xA,
        (
            "Just who was that red-\x01",
            "headed girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, just where did\x01",
            "Rixia...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2827")

    Jump("loc_2BB0")

    label("loc_282C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28BE")

    ChrTalk(
        0xA,
        (
            "Finally, the renewal\x01",
            "performance's opening\x01",
            "day has arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, I pray only for\x01",
            "the success of tonight's\x01",
            "performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_28BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28CC")
    Jump("loc_2BB0")

    label("loc_28CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28DA")
    Jump("loc_2BB0")

    label("loc_28DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28E8")
    Jump("loc_2BB0")

    label("loc_28E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_297C")

    ChrTalk(
        0xA,
        (
            "Opening night fast\x01",
            "approaches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I feel the excitement of the\x01",
            "artists and other staff building.\x01",
            "Myself included, of course.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A51")

    ChrTalk(
        0xA,
        (
            "Last night, I received a thank-\x01",
            "you directly from Her Highness,\x01",
            "Princess Klaudia of Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "She must be very kind-hearted if\x01",
            "she would go out of her way to\x01",
            "thank even staff such as myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_2A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A5F")
    Jump("loc_2BB0")

    label("loc_2A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B17")

    ChrTalk(
        0xA,
        (
            "The "West Zemuria Trade\x01",
            "Conference"... It\x01",
            "finally opens tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Conferences of this scale have\x01",
            "been quite rare until now. Even\x01",
            "I am getting a little nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_2B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B25")
    Jump("loc_2BB0")

    label("loc_2B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2BB0")

    ChrTalk(
        0xA,
        (
            "Everyone, welcome to the\x01",
            "Arc-en-Ciel troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have any questions\x01",
            "about our theater, please\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB0")

    TalkEnd(0xA)
    Return()

    # Function_12_2237 end

    def Function_13_2BB4(): pass

    label("Function_13_2BB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2BC5")
    Jump("loc_2FE5")

    label("loc_2BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D15")

    ChrTalk(
        0xFE,
        (
            "Ilya... She sure is\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She protected Sully without any\x01",
            "hesitation at all... Even though she\x01",
            "got injured, I'm glad Sully's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And until the end, the\x01",
            "performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All of us here would like to do whatever\x01",
            "we can, but... At a time like this, I\x01",
            "wonder if there's anything we can do.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DC1")

    label("loc_2D15")


    ChrTalk(
        0xFE,
        (
            "All of us here would like to do whatever\x01",
            "we can, but... At a time like this, I\x01",
            "wonder if there's anything we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn... I just can't\x01",
            "stop thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC1")

    Jump("loc_2FE5")

    label("loc_2DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2DD4")
    Jump("loc_2FE5")

    label("loc_2DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DE2")
    Jump("loc_2FE5")

    label("loc_2DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2DF0")
    Jump("loc_2FE5")

    label("loc_2DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DFE")
    Jump("loc_2FE5")

    label("loc_2DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E19")
    Call(0, 14)
    Jump("loc_2E62")

    label("loc_2E19")


    ChrTalk(
        0xFE,
        "Ooh, I'm nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe my clumsiness goes\x01",
            "beyond the stage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E62")

    Jump("loc_2FE5")

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E75")
    Jump("loc_2FE5")

    label("loc_2E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E83")
    Jump("loc_2FE5")

    label("loc_2E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9E")
    Call(0, 15)
    Jump("loc_2F2B")

    label("loc_2E9E")


    ChrTalk(
        0xC,
        (
            "*sigh*. Whenever I do an even\x01",
            "slightly violent movement, I\x01",
            "end up like this immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to speak with\x01",
            "Karelia, and soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2B")

    Jump("loc_2FE5")

    label("loc_2F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F3E")
    Jump("loc_2FE5")

    label("loc_2F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F59")
    Call(0, 16)
    Jump("loc_2FE5")

    label("loc_2F59")


    ChrTalk(
        0xC,
        (
            "A docile young man... In\x01",
            "short, a late bloomer\x01",
            "and a gentle character?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmph, in that case,\x01",
            "preparing for the role\x01",
            "will be simple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE5")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3002")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_3002")

    Return()

    # Function_13_2BB4 end

    def Function_14_3003(): pass

    label("Function_14_3003")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "Ahh, I wonder where that\x01",
            "Karelia's lazing around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Alright, if it's like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x0)

    ChrTalk(
        0xF,
        (
            "Eugene, there's\x01",
            "something I want you to\x01",
            "do for me...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x13B, 0x0)

    ChrTalk(
        0xC,
        "What is it, Pliｳ?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "My sash has become a\x01",
            "little loose, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can't tie it myself.\x01",
            "Help me out?㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "S-Seriously?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x16D, 4)
    Return()

    # Function_14_3003 end

    def Function_15_3178(): pass

    label("Function_15_3178")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Man~. As always, my\x01",
            "figure in costume is\x01",
            "sinfulness itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This gallant form...\x01",
            "Looks like I'll get some\x01",
            "new fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...I hope you're right,\x01",
            "Eugene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The shoulders and\x01",
            "threads are fraying.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Guh, seriously?... I've\x01",
            "got to have a word with\x01",
            "that Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmph, what kind of\x01",
            "prince does she think I\x01",
            "am?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_15_3178 end

    def Function_16_32F4(): pass

    label("Function_16_32F4")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3607")

    ChrTalk(
        0xC,
        (
            "But, that Nikol seems\x01",
            "the same as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah. And it seems his\x01",
            "skill is steadily\x01",
            "improving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He'll surpass you before\x01",
            "long if you're not\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmph, who do you think\x01",
            "you're saying that to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Do you really think the\x01",
            "Prince of Arc-en-Ciel will\x01",
            "be surpassed that easily?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...It seems like docile\x01",
            "young men like Nikol have\x01",
            "gotten more popular lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "According to Roland,\x01",
            "Nikol has been getting\x01",
            "more fan mail lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "S-Seriously? How can\x01",
            "that be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Haha, heck if I know.\x01",
            "Why don't you try asking\x01",
            "him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "Theodore, teach me everything\x01",
            "I need to know to be that\x01",
            "kind of docile young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll master it in a\x01",
            "week.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "...That's not the\x01",
            "problem here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 3)

    label("loc_3607")

    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_16_32F4 end

    def Function_17_3620(): pass

    label("Function_17_3620")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3631")
    Jump("loc_3A2C")

    label("loc_3631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_36ED")

    ChrTalk(
        0xFE,
        (
            "I feel like Sully has\x01",
            "been putting a lot into\x01",
            "her acting lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's so impressive that\x01",
            "everyone who sees it is\x01",
            "fascinated by it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...As if we'd lose to\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2C")

    label("loc_36ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_36FB")
    Jump("loc_3A2C")

    label("loc_36FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_383D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37CC")

    ChrTalk(
        0xFE,
        (
            "But... Just where is\x01",
            "Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like there's some\x01",
            "truth she's hiding,\x01",
            "but... She's one of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think anyone's\x01",
            "ever disappeared without\x01",
            "a word before, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3838")

    label("loc_37CC")


    ChrTalk(
        0xFE,
        (
            "...Just where did Rixia\x01",
            "go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think anyone's\x01",
            "ever disappeared without\x01",
            "a word before, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3838")

    Jump("loc_3A2C")

    label("loc_383D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_384B")
    Jump("loc_3A2C")

    label("loc_384B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3859")
    Jump("loc_3A2C")

    label("loc_3859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3867")
    Jump("loc_3A2C")

    label("loc_3867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3875")
    Jump("loc_3A2C")

    label("loc_3875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3890")
    Call(0, 18)
    Jump("loc_3910")

    label("loc_3890")


    ChrTalk(
        0xFE,
        (
            "...At the end of the day, one's\x01",
            "problems can't be solved without\x01",
            "first acknowledging them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya is so irritating\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3910")

    Jump("loc_3A2C")

    label("loc_3915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3923")
    Jump("loc_3A2C")

    label("loc_3923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3931")
    Jump("loc_3A2C")

    label("loc_3931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394C")
    Call(0, 15)
    Jump("loc_3993")

    label("loc_394C")


    ChrTalk(
        0xFE,
        (
            "...Now then, I've\x01",
            "finished changing. It's\x01",
            "time to get practicing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3993")

    Jump("loc_3A2C")

    label("loc_3998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_39A6")
    Jump("loc_3A2C")

    label("loc_39A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C1")
    Call(0, 16)
    Jump("loc_3A2C")

    label("loc_39C1")


    ChrTalk(
        0xD,
        (
            "...Looks like it was a\x01",
            "mistake to stir things\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I guess it was\x01",
            "effective in its own\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A2C")

    TalkEnd(0xFE)
    Return()

    # Function_17_3620 end

    def Function_18_3A30(): pass

    label("Function_18_3A30")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "That Sully... She looks\x01",
            "quite worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It seems like she's\x01",
            "thinking about where her\x01",
            "acting is lacking, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yeah... Seems that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, this is Sully's\x01",
            "problem... Only she can\x01",
            "find the answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Because of that, let's\x01",
            "keep quiet and watch\x01",
            "over her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Y-Yeah... You're right.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_18_3A30 end

    def Function_19_3B81(): pass

    label("Function_19_3B81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C00")

    ChrTalk(
        0xFE,
        (
            "Hearing Ilya's energetic\x01",
            "voice was a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya is Ilya, after all.\x01",
            "We've got to do our best\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_410D")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3CDF")

    ChrTalk(
        0xFE,
        (
            "Sully is doing her best to fill the\x01",
            "role of princess herself without\x01",
            "succumbing to the pressure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Doing her best on the performance is\x01",
            "to repay Ilya... She didn't actually\x01",
            "say that, but it's obvious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_410D")

    label("loc_3CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CED")
    Jump("loc_410D")

    label("loc_3CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7A")

    ChrTalk(
        0xFE,
        (
            "Normally, it'd be time\x01",
            "for singing practice,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*... I don't\x01",
            "feel like it at all\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3DD1")

    label("loc_3D7A")


    ChrTalk(
        0xFE,
        (
            "To think something like\x01",
            "that happened to Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can hardly believe\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD1")

    Jump("loc_410D")

    label("loc_3DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E80")

    ChrTalk(
        0xFE,
        (
            "Ah, ah, ah.♪ Haha, my\x01",
            "voice is in top form\x01",
            "today㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to put on\x01",
            "my mask and protect my voice\x01",
            "until the performance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3EC4")

    label("loc_3E80")


    ChrTalk(
        0xFE,
        (
            "The voice is precious to\x01",
            "a songstress. I need\x01",
            "another lozenge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC4")

    Jump("loc_410D")

    label("loc_3EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3ED7")
    Jump("loc_410D")

    label("loc_3ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3EE5")
    Jump("loc_410D")

    label("loc_3EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EF3")
    Jump("loc_410D")

    label("loc_3EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3F8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0E")
    Call(0, 14)
    Jump("loc_3F8A")

    label("loc_3F0E")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, looking at Eugene\x01",
            "like this, he's unexpectedly\x01",
            "innocent, isn't he㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even I am embarrassed\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8A")

    Jump("loc_410D")

    label("loc_3F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FAA")
    Call(0, 20)
    Jump("loc_402D")

    label("loc_3FAA")


    ChrTalk(
        0xFE,
        (
            "Hmm, somehow I\x01",
            "understood that they're\x01",
            "all extremely famous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being all lined up like\x01",
            "that, as expected, I\x01",
            "couldn't tell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402D")

    Jump("loc_410D")

    label("loc_4032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4040")
    Jump("loc_410D")

    label("loc_4040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405B")
    Call(0, 21)
    Jump("loc_40A5")

    label("loc_405B")


    ChrTalk(
        0xFE,
        "Hmm, too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The rice crackers Rixia\x01",
            "gave me were really\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A5")

    Jump("loc_410D")

    label("loc_40AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40B8")
    Jump("loc_410D")

    label("loc_40B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_410D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D3")
    Call(0, 22)
    Jump("loc_410D")

    label("loc_40D3")


    ChrTalk(
        0xFE,
        (
            "*crunch, munch*... Ah,\x01",
            "this is h-a-p-p-i-n-e-\x01",
            "s-s~㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410D")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_412A")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_412A")

    Return()

    # Function_19_3B81 end

    def Function_20_412B(): pass

    label("Function_20_412B")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "...Yesterday was\x01",
            "overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Chancellor Osborne and\x01",
            "Prince Olivert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "President Rocksmith and\x01",
            "Archduke Albert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Princess Klaudia and Lt.\x01",
            "Julia... Each and every\x01",
            "one of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Haha, you sure know your\x01",
            "stuff, Celine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I have barely any idea\x01",
            "who any of them are.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "Ooh... I'm envious of\x01",
            "your carefree nature,\x01",
            "Pliｳ.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_20_412B end

    def Function_21_42C3(): pass

    label("Function_21_42C3")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "Ooh, it's still the day\x01",
            "before... As expected,\x01",
            "there's a lot of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, we won't have our\x01",
            "usual guests this time,\x01",
            "will we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, you've overcome\x01",
            "many difficulties up\x01",
            "until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Have a little more\x01",
            "confidence in yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Karelia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That's right, Celine. Worrying\x01",
            "about things like that is just\x01",
            "going to make you hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh, want to have a snack\x01",
            "together? I've got some Eastern\x01",
            "rice crackers from Rixia on me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "No thanks. At a time like\x01",
            "this, I don't want to eat\x01",
            "anything at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pliｳ... You really do\x01",
            "everything at your own\x01",
            "pace, don't you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_21_42C3 end

    def Function_22_4577(): pass

    label("Function_22_4577")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "*munch, crunch*... Mmm,\x01",
            "snacks during practice\x01",
            "are the best~㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh*. Oh, Pliｳ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How many times do I have\x01",
            "to tell you? No sweets\x01",
            "in the costumes room!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Huh? I mean, we're on\x01",
            "break now, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Sweets are banned during\x01",
            "practice. If I want to eat\x01",
            "them, I can only do it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Seriously... You're such\x01",
            "a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Pliｳ, the Mysterious\x01",
            "Diva... She's pretty\x01",
            "mischievous, isn't she.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(S-Seriously. It's very\x01",
            "different from when\x01",
            "she's on stage.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_22_4577 end

    def Function_23_477F(): pass

    label("Function_23_477F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4838")

    ChrTalk(
        0xFE,
        (
            "Ilya's voice... It's been a\x01",
            "while since I heard it, but\x01",
            "I'm glad she's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what that\x01",
            "huge tree is, but anyway,\x01",
            "all we can do is practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE8")

    label("loc_4838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4846")
    Jump("loc_4BE8")

    label("loc_4846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4854")
    Jump("loc_4BE8")

    label("loc_4854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_48F9")

    ChrTalk(
        0xFE,
        (
            "Sully... That girl is...\x01",
            "She's taking it harder\x01",
            "than the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was taken in by Ilya...\x01",
            "and she's been blaming\x01",
            "herself this whole time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE8")

    label("loc_48F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4907")
    Jump("loc_4BE8")

    label("loc_4907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4915")
    Jump("loc_4BE8")

    label("loc_4915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4923")
    Jump("loc_4BE8")

    label("loc_4923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4931")
    Jump("loc_4BE8")

    label("loc_4931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_497C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494C")
    Call(0, 24)
    Jump("loc_4977")

    label("loc_494C")


    ChrTalk(
        0xFE,
        (
            "I am who I am... Is that\x01",
            "really true?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4977")

    Jump("loc_4BE8")

    label("loc_497C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_49D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4997")
    Call(0, 20)
    Jump("loc_49CE")

    label("loc_4997")


    ChrTalk(
        0xFE,
        (
            "Ooh... I'm envious of\x01",
            "your carefree nature,\x01",
            "Pliｳ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49CE")

    Jump("loc_4BE8")

    label("loc_49D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49E1")
    Jump("loc_4BE8")

    label("loc_49E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FC")
    Call(0, 21)
    Jump("loc_4A45")

    label("loc_49FC")


    ChrTalk(
        0xFE,
        (
            "When I look at Pliｳ, I\x01",
            "can no longer understand\x01",
            "my own nervousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A45")

    Jump("loc_4BE8")

    label("loc_4A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4A58")
    Jump("loc_4BE8")

    label("loc_4A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B76")

    ChrTalk(
        0xFE,
        (
            "Theo and Eugene are\x01",
            "always together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think this is what they\x01",
            "call BL? The imaginations\x01",
            "of some fans...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0xFE,
        (
            "...Hey, what am I doing\x01",
            "thinking about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these\x01",
            "that I need to focus on\x01",
            "image training.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4BE8")

    label("loc_4B76")


    ChrTalk(
        0xFE,
        (
            "W-What am I doing\x01",
            "thinking about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these\x01",
            "that I need to focus on\x01",
            "image training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE8")

    TalkEnd(0xFE)
    Return()

    # Function_23_477F end

    def Function_24_4BEC(): pass

    label("Function_24_4BEC")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Even though I got a more\x01",
            "important role than\x01",
            "Nikol, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What are you saying,\x01",
            "Celine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you succeed here,\x01",
            "you'll have more chances\x01",
            "in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Even so, if you compare\x01",
            "me to others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jeez. No one could\x01",
            "compare you to anyone\x01",
            "else. You know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You are the one and only\x01",
            "you in this troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "C'mon, smile for me.\x01",
            "You'll ruin your makeup if\x01",
            "you keep making that face.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_24_4BEC end

    def Function_25_4DAB(): pass

    label("Function_25_4DAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4E2D")

    ChrTalk(
        0xFE,
        (
            "I'm repairing Ilya's\x01",
            "costume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's my job to make sure\x01",
            "our costumes are always\x01",
            "stage ready, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544E")

    label("loc_4E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E48")
    Call(0, 26)
    Jump("loc_4EC0")

    label("loc_4E48")


    ChrTalk(
        0xFE,
        (
            "Haha. Come to think of\x01",
            "it, Sully still has a\x01",
            "lot of growing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm really looking\x01",
            "forward to seeing that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EC0")

    Jump("loc_544E")

    label("loc_4EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4ED3")
    Jump("loc_544E")

    label("loc_4ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5042")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC6")

    ChrTalk(
        0xFE,
        (
            "...Even just thinking\x01",
            "back to what happened\x01",
            "that day is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya's costume, it was ruined and\x01",
            "stained with blood... I couldn't\x01",
            "even bear to look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Ilya... Why did this\x01",
            "have to happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_503D")

    label("loc_4FC6")


    ChrTalk(
        0xFE,
        (
            "...Even just thinking\x01",
            "back to what happened\x01",
            "that day is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Ilya... Why did this\x01",
            "have to happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_503D")

    Jump("loc_544E")

    label("loc_5042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50C0")

    ChrTalk(
        0xFE,
        (
            "Haha, Pliｳ always goes\x01",
            "at her own pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Celine seems well this\x01",
            "morning too, so I think\x01",
            "we'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544E")

    label("loc_50C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_50CE")
    Jump("loc_544E")

    label("loc_50CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_50DC")
    Jump("loc_544E")

    label("loc_50DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50EA")
    Jump("loc_544E")

    label("loc_50EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_517C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5105")
    Call(0, 24)
    Jump("loc_5177")

    label("loc_5105")


    ChrTalk(
        0xFE,
        (
            "Celine seems worried\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand what she's\x01",
            "feeling, but... I want her\x01",
            "to get through it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5177")

    Jump("loc_544E")

    label("loc_517C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5197")
    Call(0, 9)
    Jump("loc_5301")

    label("loc_5197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5262")

    ChrTalk(
        0xFE,
        "Umm, sorry everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We haven't given the renewal\x01",
            "performance details to any of\x01",
            "the artists except Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So please, keep what you\x01",
            "just saw a secret for a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5301")

    label("loc_5262")


    ChrTalk(
        0xFE,
        (
            "We haven't given the renewal\x01",
            "performance details to any of\x01",
            "the artists except Ilya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So please, keep what you\x01",
            "just saw a secret for a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5301")

    Jump("loc_544E")

    label("loc_5306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5314")
    Jump("loc_544E")

    label("loc_5314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_53A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532F")
    Call(0, 21)
    Jump("loc_539E")

    label("loc_532F")


    ChrTalk(
        0xFE,
        (
            "Ilya aside, even Pliｳ is\x01",
            "unaffected by pressure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd give some\x01",
            "of their courage to\x01",
            "Celine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_539E")

    Jump("loc_544E")

    label("loc_53A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53B1")
    Jump("loc_544E")

    label("loc_53B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_544E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CC")
    Call(0, 22)
    Jump("loc_544E")

    label("loc_53CC")


    ChrTalk(
        0xFE,
        (
            "*sigh*. Anyway, I'll\x01",
            "coordinate their costumes\x01",
            "during this break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't stop you\x01",
            "anymore, so please eat\x01",
            "them quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_544E")

    TalkEnd(0xFE)
    Return()

    # Function_25_4DAB end

    def Function_26_5452(): pass

    label("Function_26_5452")

    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, Sully... Have you\x01",
            "grown again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12205FHuh, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, don't\x01",
            "underestimate a costume\x01",
            "designer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can tell just by\x01",
            "seeing you wear it a\x01",
            "little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And so, it just needs a\x01",
            "small adjustment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12202FI see... You're amazing,\x01",
            "Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Come to think of\x01",
            "it, you still have a lot\x01",
            "of growing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please try to both eat\x01",
            "and practice a lot from\x01",
            "here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12206FS-Sure... Thanks,\x01",
            "Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Even though the situation's\x01",
            "pretty bad outside... That's a\x01",
            "heartwarming change of pace.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_570D")

    ChrTalk(
        0x106,
        (
            "#10702F(Haha, seems that way.)\x02\x03",
            "#10704F(How can I say this...\x01",
            "This theater feels like\x01",
            "a whole other world.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_577A")

    label("loc_570D")


    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*, indeed.)\x02\x03",
            "#00104F(How can I say this...\x01",
            "This theater seems like\x01",
            "a whole other world.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577A")

    SetScenarioFlags(0x1, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_26_5452 end

    def Function_27_5790(): pass

    label("Function_27_5790")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58CA")

    ChrTalk(
        0xFE,
        (
            "No matter what happens,\x01",
            "I'll put my all into my\x01",
            "acting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think like that,\x01",
            "my feelings of uneasiness\x01",
            "seem to disappear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though saying that\x01",
            "might be conceited, it's\x01",
            "all Ilya's fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I listen to her\x01",
            "speak, it feels like power\x01",
            "is gushing out of me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_593C")

    label("loc_58CA")


    ChrTalk(
        0xFE,
        (
            "Ilya is like the sun\x01",
            "itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Giving me this much power\x01",
            "with just words... I'm\x01",
            "really thankful for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_593C")

    Jump("loc_5A76")

    label("loc_5941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_594F")
    Jump("loc_5A76")

    label("loc_594F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_595D")
    Jump("loc_5A76")

    label("loc_595D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_59E9")

    ChrTalk(
        0xFE,
        (
            "I wonder what Ilya would\x01",
            "say to us at a time like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand we've got\x01",
            "to do our best, but...\x01",
            "but... but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A76")

    label("loc_59E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5A76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A04")
    Call(0, 18)
    Jump("loc_5A76")

    label("loc_5A04")


    ChrTalk(
        0xFE,
        (
            "That Sully, she seems\x01",
            "quite worried, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I suppose this is\x01",
            "her problem. ...Theodore\x01",
            "has a point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A76")

    TalkEnd(0xFE)
    Return()

    # Function_27_5790 end

    def Function_28_5A7A(): pass

    label("Function_28_5A7A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha. It's a reporter's special\x01",
            "privilege to be able to enter the\x01",
            "venue prior to the event like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about Mainz,\x01",
            "but for today I'll focus\x01",
            "on Arc-en-Ciel coverage.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_5A7A end

    def Function_29_5B3C(): pass

    label("Function_29_5B3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5A")
    Call(0, 26)
    Jump("loc_5E73")

    label("loc_5B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CA0")
    TurnDirection(0x12, 0x106, 500)

    ChrTalk(
        0x12,
        (
            "#12201FRixia... Please be careful during\x01",
            "the infiltration, ok?\x02\x03",
            "#12203FI can't really do anything to help\x01",
            "you, but I've gotta at least give\x01",
            "practice everything I've got...\x02\x03",
            "#12201FSo Rixia and everyone else, you\x01",
            "have to do your best for me too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702FSully... Yes,\x01",
            "understood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D24")

    label("loc_5CA0")


    ChrTalk(
        0x12,
        (
            "#12200FGuys... Please be\x01",
            "careful during the\x01",
            "infiltration, ok?\x02\x03",
            "And please take care of\x01",
            "Rixia for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, got it.\x02",
    )

    CloseMessageWindow()

    label("loc_5D24")

    SetScenarioFlags(0x1, 3)
    Jump("loc_5E73")

    label("loc_5D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E02")
    TurnDirection(0x12, 0x106, 500)

    ChrTalk(
        0x12,
        (
            "#12203FI can't really do anything to help\x01",
            "you, but I've gotta at least give\x01",
            "practice everything I've got...\x02\x03",
            "#12202FSo Rixia and everyone else, you\x01",
            "have to do your best for me too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E73")

    label("loc_5E02")


    ChrTalk(
        0x12,
        (
            "#12200FGuys... Please be\x01",
            "careful during the\x01",
            "infiltration, ok?\x02\x03",
            "#12203FAnd please take care of\x01",
            "Rixia for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E73")

    TalkEnd(0xFE)
    Return()

    # Function_29_5B3C end

    def Function_30_5E77(): pass

    label("Function_30_5E77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_657E")

    ChrTalk(
        0x13,
        (
            "#01700FMy, if it isn't little\x01",
            "bro.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#01700FAnd Tio, too. Haha, it's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYes, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01700FWith this, the full\x01",
            "membership of the Support\x01",
            "Section is finally assembled.\x02\x03",
            "#01704FIt seems like each and every\x01",
            "one of you has grown from\x01",
            "when I first saw you.\x02\x03",
            "#01709FWe here at Arc-en-Ciel won't\x01",
            "lose to you, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, I'm glad to hear\x01",
            "you say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FBut, you guys seem a\x01",
            "whole other level of\x01",
            "fired up today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01703FWell, our next performance will\x01",
            "be the last one before the\x01",
            "renewal.\x02\x03",
            "#01700FThinking of it as a culmination,\x01",
            "naturally we want to put\x01",
            "everything we have into it.\x02\x03",
            "#01706FIt's too bad Rixia's off today,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_END)), "loc_62F9")

    ChrTalk(
        0x109,
        (
            "#10105FCome to think of it,\x01",
            "Rixia said she had some\x01",
            "business at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01705FOh, did you see Rixia?\x02\x03",
            "#01703FIt's gotten less frequent lately, but...\x01",
            "When she wanted time off, there were many\x01",
            "times when she let me know just before.\x02\x03",
            "#01709FAnd each time, I wondered if she was\x01",
            "secretly meeting with a guy, y'know~?\x02\x03",
            "#01704FWell if it's really true, the hand of\x01",
            "this Ilya won't be silent. (*twitch*)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6452")

    label("loc_62F9")


    ChrTalk(
        0x109,
        (
            "#10100FSo that's how it is,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01703FYes. It's gotten less frequent lately,\x01",
            "but... When she wanted time off, there were\x01",
            "many times when she let me know just before.\x02\x03",
            "#01709FAnd each time, I wondered if she was\x01",
            "secretly meeting with a guy, y'know~?\x02\x03",
            "#01704FWell if it's really true, the hand of this\x01",
            "Ilya won't be silent. (*twitch*)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6452")


    ChrTalk(
        0x102,
        "#00105F(*shiver*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, I think I can\x01",
            "picture the scene you're\x01",
            "imagining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(Elie...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01700FWell, setting aside the\x01",
            "issue of Rixia, we've\x01",
            "got to go all-out today.\x02\x03",
            "#01709FYou guys must be busy\x01",
            "too, so let's each do\x01",
            "what we have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 5)
    Jump("loc_6604")

    label("loc_657E")


    ChrTalk(
        0x13,
        (
            "#01704FNow then, we've got to\x01",
            "go all-out today in any\x01",
            "case.\x02\x03",
            "#01700FYou guys must be busy\x01",
            "too, so let's each do\x01",
            "what we have to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6604")

    TalkEnd(0xFE)
    Return()

    # Function_30_5E77 end

    def Function_31_6608(): pass

    label("Function_31_6608")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 0, 0, 900, 180)
    OP_4B(0x9, 0xFF)
    OP_68(-470, 1350, -3340, 0)
    MoveCamera(52, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14990, 0)
    SetChrPos(0x101, -70, 0, -7720, 0)
    SetChrPos(0x102, -70, 0, -7720, 0)
    SetChrPos(0x109, -70, 0, -7720, 0)
    SetChrPos(0x105, -70, 0, -7720, 0)
    SetChrPos(0x104, -70, 0, -7720, 0)
    SetChrPos(0x1A3, -70, 0, -7720, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 32)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    OP_68(-400, 1350, -2210, 3000)
    BeginChrThread(0x109, 3, 0, 35)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 37)
    OP_6F(0x1)
    WaitChrThread(0x1A3, 3)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#5PAh, everyone. Welcome.\x01",
            "How nice of you to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PJust now, a kitten ran\x01",
            "in here at a blindingly\x01",
            "fast speed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah, sorry about that.\x02\x03",
            "#00000FActually, we're in the\x01",
            "middle of tracking down\x01",
            "that kitten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FUmm... Is it alright if\x01",
            "we search the theater?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYes. On the contrary, it\x01",
            "would be a great help if\x01",
            "you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWe're currently preparing for a\x01",
            "performance tonight to which\x01",
            "the heads of state are invited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYour timing is perfect.\x01",
            "All of our artists are\x01",
            "on break right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell that's convenient.\x02\x03",
            "Then, we'll conduct a\x01",
            "quick search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBy the way, do know\x01",
            "where the kitten was\x01",
            "headed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PI'm terribly sorry,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PShe was so fast and it\x01",
            "happened so suddenly. I'm\x01",
            "afraid I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHowever, I'm absolutely\x01",
            "certain that she ran up\x01",
            "those stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... In that case,\x01",
            "we should split up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FRight. How do you want\x01",
            "to divide us?\x02\x03",
            "#00103FShould we keep our three\x01",
            "teams of two?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00003FRight...\x02",
    )

    CloseMessageWindow()
    OP_68(-30, 1150, -2770, 3000)
    MoveCamera(42, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15460, 3000)
    OP_95(0x1A3, 1560, 0, -3800, 3000, 0x0)
    OP_95(0x1A3, 1610, 0, -1100, 3000, 0x0)
    OP_95(0x1A3, 610, 0, -1240, 3000, 0x0)
    Sound(812, 0, 100, 0)
    TurnDirection(0x1A3, 0x105, 500)
    OP_6F(0x79)

    ChrTalk(
        0x1A3,
        (
            "#04609FShirley's going to be\x01",
            "with Lloyd, then.㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6CA8():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6CA8)
    Sleep(50)

    def lambda_6CB8():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6CB8)
    Sleep(50)

    def lambda_6CC8():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6CC8)
    Sleep(50)

    def lambda_6CD8():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6CD8)
    Sleep(50)

    def lambda_6CE8():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CE8)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x102,
        "#6P#00101FW-Wait a minute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWhy does it have to be\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04605FMmm, just because?\x02\x03",
            "#04609FAh, did you ladies want\x01",
            "to be with Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)
    OP_64(0x109)

    ChrTalk(
        0x102,
        "#6P#00106FI-I wouldn't say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's not the issue\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FAhaha, seems interesting\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00006FI told you. This isn't\x01",
            "your problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FThat's an odd thing to\x01",
            "say now that we've come\x01",
            "this far.\x02\x03",
            "#00301FShirley. No passes at\x01",
            "Lloyd, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#04604FYeah, yeah, I know.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#04600FHe's cute but not really\x01",
            "my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FCute? Hmph, whatever.\x02\x03",
            "#00000FAnyway, let's split up\x01",
            "and search the theater.\x02\x03",
            "Everyone, meet at the\x01",
            "entrance once you're\x01",
            "finished.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(48590, 1300, -180, 0)
    MoveCamera(34, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14900, 0)
    SetChrPos(0x101, 45300, 0, 40, 90)
    SetChrPos(0x1A3, 45300, 0, 40, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 39)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x1A3,
        (
            "#6P#04602FHaha, then let's get\x01",
            "started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, of course.\x02\x03",
            "#00003F(But talking with her like this,\x01",
            "you'd think she's an innocent\x01",
            "and whimsical girl, but...)\x02\x03",
            "(Her threat to kill those bums\x01",
            "earlier was genuine.)\x02\x03",
            "#00001F(I wonder which of them is the\x01",
            "real her?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A3,
        (
            "#6P#04605FHuh, something wrong?\x02\x03",
            "#04609FCould it be you've\x01",
            "fallen for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOf course not.\x02\x03",
            "#00000FFor now, let's search\x01",
            "the S-class seats on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#6P#04609FAhaha, yes sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x155, 5)
    ModifyEventFlags(1, 5, 0x80)
    OP_1B(0x5, 0x0, 0x36)
    OP_29(0x74, 0x1, 0x6)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 49470, 0, 40, 0)
    EventEnd(0x5)
    Return()

    # Function_31_6608 end

    def Function_32_72B2(): pass

    label("Function_32_72B2")


    def lambda_72B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72B7)

    def lambda_72C8():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72C8)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 900, 0, -1900, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_72B2 end

    def Function_33_72FD(): pass

    label("Function_33_72FD")


    def lambda_7302():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7302)

    def lambda_7313():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7313)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -900, 0, -1900, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_72FD end

    def Function_34_7348(): pass

    label("Function_34_7348")


    def lambda_734D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_734D)

    def lambda_735E():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_735E)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -900, 0, -4300, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_7348 end

    def Function_35_7393(): pass

    label("Function_35_7393")


    def lambda_7398():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7398)

    def lambda_73A9():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_73A9)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 0, -3100, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_35_7393 end

    def Function_36_73DE(): pass

    label("Function_36_73DE")


    def lambda_73E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_73E3)

    def lambda_73F4():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_73F4)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -900, 0, -3100, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_36_73DE end

    def Function_37_7429(): pass

    label("Function_37_7429")


    def lambda_742E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_742E)

    def lambda_743F():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_743F)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 800, 0, -4300, 2000, 0x0)
    OP_93(0x1A3, 0x0, 0x1F4)
    Return()

    # Function_37_7429 end

    def Function_38_7474(): pass

    label("Function_38_7474")


    def lambda_7479():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7479)

    def lambda_748A():
        OP_95(0xFE, 50110, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_748A)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x1A3, 500)
    Return()

    # Function_38_7474 end

    def Function_39_74AB(): pass

    label("Function_39_74AB")


    def lambda_74B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_74B0)

    def lambda_74C1():
        OP_95(0xFE, 48110, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_74C1)
    Return()

    # Function_39_74AB end

    def Function_40_74D7(): pass

    label("Function_40_74D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, 660, 270)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x15, 0x13)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, 1200, 0, 2260, 270)
    OP_68(-3160, 3750, -1920, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, 7220, 2500, 13500, 225)
    SetChrPos(0x1A3, 7220, 2500, 14500, 225)
    SetChrPos(0x104, -900, 0, 1060, 90)
    SetChrPos(0x109, -900, 0, 2260, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetCameraDistance(9010, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    Fade(500)
    OP_68(5640, 3950, 12260, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11610, 0)
    OP_0D()
    OP_63(0x1A3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A3,
        "#5P#04605FHuh, who's she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FIt's... Is that Rixia?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-70, 1450, 5100, 0)
    MoveCamera(42, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13470, 0)
    SetChrPos(0x101, 960, 1530, 9450, 180)
    SetChrPos(0x1A3, -450, 1620, 9500, 180)
    OP_93(0x15, 0x0, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)

    def lambda_7755():
        OP_95(0xFE, 900, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7755)
    Sleep(50)

    def lambda_7772():
        OP_95(0xFE, -800, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7772)
    OP_68(-660, 1450, 2200, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13470, 3000)
    WaitChrThread(0x1A3, 1)

    def lambda_77BE():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_77BE)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5P#00000FIt is Rixia.\x02\x03",
            "#00005FWeren't all the artists\x01",
            "on break?\x02",
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
        0x15,
        (
            "Ah, Lloyd.\x02\x03",
            "Umm, I was having my clothes\x01",
            "repaired late last night...\x02\x03",
            "I'm performing a final costume\x01",
            "check before tonight's performance.\x02\x03",
            "But more importantly... I hear a\x01",
            "kitty got in here?\x02",
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
        0x101,
        (
            "#5P#00001FYes, that's right,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00005FBut what?\x02\x03",
            "I could've sworn the\x01",
            "kitten we're chasing\x01",
            "came in here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    TurnDirection(0x104, 0x15, 500)

    ChrTalk(
        0x104,
        "#12P#00305FOh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI don't think it came in\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)
    Fade(500)
    OP_68(-9590, 3950, 12900, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12320, 0)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    SetChrPos(0x102, -10590, 2500, 14070, 135)
    SetChrPos(0x105, -10590, 2500, 14070, 135)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_68(-8560, 3950, 12020, 3000)
    Sound(103, 0, 100, 0)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 42)
    WaitChrThread(0x105, 3)
    Sleep(1000)
    OP_6F(0x1)

    ChrTalk(
        0x105,
        "#6P#10300FOh, everyone's here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FLooks like it. Even\x01",
            "Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#N#00000FWazy, Elie... It seems\x01",
            "you haven't seen her.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-870, 1450, 2630, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14250, 0)
    SetChrPos(0x105, -2400, 0, 3460, 90)
    SetChrPos(0x102, -2200, 0, 1960, 90)
    SetChrPos(0x104, -900, 0, 560, 90)
    SetChrPos(0x109, -900, 0, 1960, 90)
    OP_93(0x101, 0xE1, 0x0)
    OP_93(0x1A3, 0x87, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x9, 0x13B, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00005FIf that's true, then it\x01",
            "means no one's seen her\x01",
            "since we lost sight of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI had them close the\x01",
            "entrance...\x02\x03",
            "#00100FShe's most likely still\x01",
            "in this hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHmm, it seems like she's\x01",
            "hiding somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI agree. Shall we all\x01",
            "search together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FYeah, that sounds good.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A3)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x15, 0x1A3, 500)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#12P#06202FUmm...?\x02\x03",
            "Who is that girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FAh, she's─\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#5P#04609FAhaha, you're amazing♪\x02\x03",
            "#04611FI've been watching you for\x01",
            "quite a while. And you never\x01",
            "let down your guard even once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12P#06205FUhh... Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...She's my stupid\x01",
            "cousin.\x02\x03",
            "#00300FDon't worry about her\x01",
            "too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11P#06205FYour...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1A3,
        (
            "Shirley Orlando! You can call me\x01",
            "Shirley!\x02\x03",
            "I saw you on the Arc-en-Ciel\x01",
            "stage, though.\x02\x03",
            "Looking at you from up close like\x01",
            "this though, it seems like you\x01",
            "have some destructive power in\x02\x03",
            "you!\x02\x03",
            "Must be nice. They're so big. I'm\x01",
            "jealous.㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x15, 0xB4, 0x1F4, 0x5DC, 0x0)

    ChrTalk(
        0x15,
        "#12P#06209FUmm, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00113FShe already gave me a\x01",
            "traumatic experience.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x1A3,
        (
            "#5P#04609FAhaha, it's fine. That\x01",
            "was no big deal.\x02\x03",
            "We might have some kind\x01",
            "of connection─\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x15)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_826E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_826E)
    Sleep(50)

    def lambda_827E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_827E)
    Sleep(300)

    ChrTalk(
        0x1A3,
        "#6P#04605FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12P#06205FAh!\x02",
    )

    CloseMessageWindow()

    def lambda_82B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_82B6)
    Sleep(50)

    def lambda_82C6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_82C6)
    Sleep(50)

    def lambda_82D6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_82D6)
    Sleep(50)

    def lambda_82E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_82E6)
    Sleep(50)

    def lambda_82F6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82F6)
    Sleep(50)

    def lambda_8306():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8306)
    Sleep(50)

    def lambda_8316():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8316)
    OP_68(3650, 1450, 17480, 4000)
    MoveCamera(28, 27, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(15360, 4000)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 3500, 2500, 15290, 135)
    OP_95(0x14, 4420, 2500, 14500, 1500, 0x0)
    OP_68(-50, 3950, 13550, 3000)
    MoveCamera(32, 33, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14250, 3000)
    OP_95(0x14, 3250, 2500, 13660, 1500, 0x0)
    OP_95(0x14, 50, 2500, 13570, 1500, 0x0)
    Sleep(300)
    OP_6F(0x79)
    TurnDirection(0x14, 0x101, 500)
    OP_63(0x14, 0x0, 1200, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-50, 3950, 15320, 3000)

    def lambda_841C():
        OP_95(0xFE, 0, 2500, 18930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_841C)
    Sleep(1000)

    def lambda_8439():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8439)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-870, 1450, 2630, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14250, 0)
    SetChrFlags(0x14, 0x80)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00011FS-So that's where she\x01",
            "was hiding!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11P#06201FI'll chase her!\x02",
    )

    CloseMessageWindow()

    def lambda_84DB():

        label("loc_84DB")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_84DB")

    QueueWorkItem2(0x102, 1, lambda_84DB)

    def lambda_84ED():

        label("loc_84ED")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_84ED")

    QueueWorkItem2(0x104, 1, lambda_84ED)

    def lambda_84FF():

        label("loc_84FF")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_84FF")

    QueueWorkItem2(0x109, 1, lambda_84FF)

    def lambda_8511():

        label("loc_8511")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_8511")

    QueueWorkItem2(0x105, 1, lambda_8511)
    OP_95(0x15, 1290, 0, 5610, 4000, 0x0)

    def lambda_8537():
        OP_95(0xFE, 0, 2500, 15240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8537)
    Sleep(500)

    ChrTalk(
        0x1A3,
        "#11P#04602FAhaha, Shirley will too!\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A3, -230, 10, 3500, 4000, 0x0)
    OP_95(0x1A3, 0, 2500, 15240, 4000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1A3, 0x80)
    OP_0D()

    ChrTalk(
        0x104,
        "#12P#00306F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FUmm... What should we\x01",
            "do?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FI'll back them up.\x02\x03",
            "She might escape again.\x01",
            "You all standby here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_865B():

        label("loc_865B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_865B")

    QueueWorkItem2(0x102, 1, lambda_865B)
    Sleep(50)

    def lambda_8670():

        label("loc_8670")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8670")

    QueueWorkItem2(0x104, 1, lambda_8670)
    Sleep(50)

    def lambda_8685():

        label("loc_8685")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8685")

    QueueWorkItem2(0x109, 1, lambda_8685)
    Sleep(50)

    def lambda_869A():

        label("loc_869A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_869A")

    QueueWorkItem2(0x105, 1, lambda_869A)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHehe. I hope we finally\x01",
            "get her this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 40, 0, 5330, 4000, 0x0)
    OP_95(0x101, 0, 2500, 15240, 4000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SoundLoad(3243)
    SoundLoad(3244)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c0420", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_40_74D7 end

    def Function_41_8759(): pass

    label("Function_41_8759")


    def lambda_875E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_875E)

    def lambda_876F():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_876F)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -6510, 2500, 12970, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_41_8759 end

    def Function_42_87A4(): pass

    label("Function_42_87A4")


    def lambda_87A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_87A9)

    def lambda_87BA():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_87BA)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -7770, 2500, 12730, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_42_87A4 end

    def Function_43_87EF(): pass

    label("Function_43_87EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 1200, 0, 900, 180)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -1200, 0, 900, 180)
    SetChrChipByIndex(0x15, 0x13)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 0, 0, 900, 180)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -1400, 0, -1900, 0)
    OP_68(-740, 1550, -1860, 0)
    MoveCamera(41, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14480, 0)
    SetChrPos(0x101, 900, 0, -1900, 0)
    SetChrPos(0x1A3, -400, 0, -1900, 0)
    SetChrPos(0x102, 900, 0, -3100, 0)
    SetChrPos(0x109, -900, 0, -3100, 0)
    SetChrPos(0x104, -900, 0, -4300, 0)
    SetChrPos(0x105, 900, 0, -4300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-740, 1450, -1860, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x1A3,
        (
            "#12P#04600FAhaha, thanks♪ You\x01",
            "really helped me out\x01",
            "back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, I should be\x01",
            "thanking you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#06209FDon't mention it. My body\x01",
            "just moved on its own.\x02\x03",
            "#06204FAnd, I'm sure Shirley would\x01",
            "have saved the kitten if I\x01",
            "hadn't stepped in.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04605FHah, see that?\x02\x03",
            "#04604FWith that timing, I could have\x01",
            "saved her if I jumped.\x02\x03",
            "#04609FAnyway, I'm satisfied with just\x01",
            "having gotten to see your chest\x01",
            "in motion during that jump.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#00306FShirley, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FMy deepest apologies,\x01",
            "Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#06209FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "E-Even so, I'm terribly\x01",
            "sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To think there was a\x01",
            "kitten on stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Even so, we'll need to\x01",
            "look over our equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04600FWell isn't it fine?\x02\x03",
            "#04604FNo one got hurt, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FRight. So don't worry\x01",
            "about it too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FAnyway... Isn't it about time\x01",
            "for us to be heading back to\x01",
            "Mr. Bond's apartment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FOh, right. He's probably\x01",
            "in the middle of worriedly\x01",
            "searching for Mary.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0x14,
        "#6PMeow♪\x02",
    )

    CloseMessageWindow()

    def lambda_8E04():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E04)
    Sleep(50)

    def lambda_8E14():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8E14)
    Sleep(50)

    def lambda_8E24():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E24)
    Sleep(50)

    def lambda_8E34():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E34)
    Sleep(50)

    def lambda_8E44():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E44)
    Sleep(50)

    def lambda_8E54():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8E54)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00309FHaha, she's something\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FThat's true. She was so\x01",
            "scared until just a\x01",
            "moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#11P#04609FAhaha, that's how cats\x01",
            "are, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F(This girl can be\x01",
            "incredibly persuasive.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00000F─Well then, allow us to\x01",
            "excuse ourselves.\x02\x03",
            "Thanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FA6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8FA6)
    Sleep(50)

    def lambda_8FB6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FB6)
    Sleep(50)

    def lambda_8FC6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8FC6)
    Sleep(50)

    def lambda_8FD6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8FD6)
    Sleep(50)

    def lambda_8FE6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8FE6)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "No, no. Perish the\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#06202FHaha. Please, take care.\x02",
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    OP_68(-940, 1450, -2690, 2000)
    MoveCamera(38, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14480, 2000)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 44)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 45)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 46)
    Sleep(300)
    BeginChrThread(0x14, 3, 0, 46)
    Sleep(700)

    def lambda_90A6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_90A6)
    WaitChrThread(0x14, 3)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A3, 0x15, 500)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#12P#04605FOh, hey lady.\x02\x03",
            "#04602FCan I call you Rixia?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#5P#06205FAh...\x02\x03",
            "#06202FYes. Of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FHaha, thanks Rixia.\x02\x03",
            "#04600FLater!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x1A3, 3, 0, 47)
    WaitChrThread(0x1A3, 3)
    Sleep(500)
    Sound(107, 0, 100, 0)
    OP_68(-700, 1450, 80, 3000)
    SetCameraDistance(13480, 3000)
    OP_6F(0x1)
    OP_63(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x15)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x15,
        (
            "#06203F#3243V(Randy's cousin...)\x02\x03",
            "#06201F#3244V(So that's the rumored\x01",
            "Bloody Shirley...)\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCAC)
    OP_C9(0x1, 0x80000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("c1040", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_43_87EF end

    def Function_44_9261(): pass

    label("Function_44_9261")


    def lambda_9266():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9266)
    Sleep(800)

    def lambda_9283():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9283)
    Return()

    # Function_44_9261 end

    def Function_45_9290(): pass

    label("Function_45_9290")


    def lambda_9295():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9295)
    Sleep(1500)

    def lambda_92B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92B2)
    Return()

    # Function_45_9290 end

    def Function_46_92BF(): pass

    label("Function_46_92BF")


    def lambda_92C4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92C4)
    Sleep(2000)

    def lambda_92E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92E1)
    Return()

    # Function_46_92BF end

    def Function_47_92EE(): pass

    label("Function_47_92EE")


    def lambda_92F3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92F3)
    Sleep(500)

    def lambda_9310():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9310)
    Return()

    # Function_47_92EE end

    def Function_48_931D(): pass

    label("Function_48_931D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-480, 1500, -1260, 0)
    MoveCamera(58, 20, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(17780, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2410, 0, 4800, 360)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9430, 0)
    SetChrPos(0x104, -500, 0, -9630, 0)
    SetChrPos(0x109, 500, 0, -10630, 0)
    SetChrPos(0x105, -500, 0, -10830, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9432():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9432)

    def lambda_944C():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_944C)
    Sleep(50)

    def lambda_9460():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9460)

    def lambda_947A():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_947A)
    Sleep(50)

    def lambda_948E():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_948E)

    def lambda_94A8():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_94A8)
    Sleep(50)

    def lambda_94BC():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_94BC)

    def lambda_94D6():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_94D6)
    Sleep(50)

    def lambda_94EA():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_94EA)

    def lambda_9504():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9504)
    Sleep(50)

    def lambda_9518():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9518)

    def lambda_9532():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9532)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-160, 1500, -2060, 3000)
    OP_95(0x9, 0, 0, 0, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "Oh, it's the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're closed today, but\x01",
            "did you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUh, no, we're just\x01",
            "stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe opening of the\x01",
            "renewal performance...\x01",
            "It's finally tomorrow.\x02\x03",
            "Are you resting today in\x01",
            "preparation for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's still one person\x01",
            "practicing today,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWow, how devoted. Could\x01",
            "they be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You understand\x01",
            "correctly. Yes, it is\x01",
            "Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tomorrow is her big\x01",
            "moment, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems that she can't\x01",
            "calm down if she's not\x01",
            "moving her body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you all would like,\x01",
            "please go watch her\x01",
            "practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA-Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes of course. If it is you all who have\x01",
            "helped us countless times, none of us here at\x01",
            "Arc-en-Ciel would have any problem with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On top of that, it seems she's\x01",
            "been at it since morning with\x01",
            "hardly any breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you like, please go\x01",
            "speak with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will make a\x01",
            "nice break for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see. Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThank you for your\x01",
            "kindness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x178, 3)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, -2250, 2500, 15000, 180)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x1, 5)
    EventEnd(0x5)
    Return()

    # Function_48_931D end

    def Function_49_99FF(): pass

    label("Function_49_99FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -70, 2500, 15340, 180)
    EventEnd(0x5)
    Return()

    # Function_49_99FF end

    def Function_50_9A23(): pass

    label("Function_50_9A23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -70, 0, -7720, 0)
    SetChrPos(0x102, -70, 0, -7720, 0)
    SetChrPos(0x109, -70, 0, -7720, 0)
    SetChrPos(0x105, -70, 0, -7720, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 4500, 0, 4500, 90)
    OP_68(0, 1750, 5000, 6000)
    MoveCamera(34, 10, 0, 6000)
    SetCameraDistance(25500, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 1050, -1700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    def lambda_9B1C():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B1C)

    def lambda_9B36():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B36)
    Sleep(50)

    def lambda_9B4A():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B4A)

    def lambda_9B64():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9B64)
    Sleep(500)

    def lambda_9B78():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9B78)

    def lambda_9B92():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9B92)
    Sleep(50)

    def lambda_9BA6():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9BA6)

    def lambda_9BC0():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9BC0)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#00005FArc-en-Ciel, huh... It's\x01",
            "been a while since we\x01",
            "were last here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha, indeed. I wonder\x01",
            "if Ilya and Rixia are\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, you guys sure do\x01",
            "know a lot of famous\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FBut, are you sure? Just\x01",
            "entering like this for\x01",
            "no reason...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 500)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9D0B():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9D0B)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "Well, well, if it isn't\x01",
            "Lloyd and Elie of the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It has been a long time.\x01",
            "What business do you\x01",
            "have with us today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, you see the Support\x01",
            "Section has resumed its\x01",
            "activities.\x02\x03",
            "We were patrolling the\x01",
            "city and wanted to stop\x01",
            "by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FAre we bothering you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No, of course you are no\x01",
            "bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We are on break right\x01",
            "now, so please, do come\x01",
            "in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure Ilya and the\x01",
            "others will be delighted\x01",
            "to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112FU-Umm...\x02",
    )

    CloseMessageWindow()

    def lambda_9F39():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F39)
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#00105FWhat's wrong, Noｱl?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#12P#10102FWell, I just want to say\x01",
            "again how amazing the\x01",
            "Special Support Section is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHaha, that's right. To think\x01",
            "you're both so famous you can\x01",
            "even get into Arc-en-Ciel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHaha. You're right, now\x01",
            "that I think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. I'm thankful for\x01",
            "our good connections.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -600, 0, -2900, 0)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, -2250, 2500, 15000, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x137, 1)
    Sleep(50)
    EventEnd(0x5)
    Return()

    # Function_50_9A23 end

    def Function_51_A0F6(): pass

    label("Function_51_A0F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1380, 1850, -1910, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15070, 0)
    SetChrPos(0xA, 740, 0, 4400, 270)
    SetChrPos(0x9, -740, 0, 4400, 90)
    SetChrPos(0x101, -500, 0, -7720, 0)
    SetChrPos(0x102, 500, 0, -7720, 0)
    SetChrPos(0x103, -500, 0, -7720, 0)
    SetChrPos(0x104, 500, 0, -7720, 0)
    SetChrPos(0xF4, -500, 0, -7720, 0)
    SetChrPos(0xF5, 500, 0, -7720, 0)
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
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A21D():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A21D)

    def lambda_A237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A237)
    Sleep(100)

    def lambda_A24B():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A24B)

    def lambda_A265():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A265)
    Sleep(500)

    def lambda_A279():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A279)

    def lambda_A293():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A293)
    Sleep(100)
    OP_68(-970, 1450, -1300, 3000)
    MoveCamera(44, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15070, 3000)

    def lambda_A2D5():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2D5)

    def lambda_A2EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A2EF)
    Sleep(500)

    def lambda_A303():
        OP_95(0xFE, -500, 0, -5100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A303)

    def lambda_A31D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A31D)
    Sleep(100)

    def lambda_A331():
        OP_95(0xFE, 500, 0, -5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A331)

    def lambda_A34B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A34B)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A3A0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A3A0)
    Sleep(50)

    def lambda_A3B0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A3B0)
    Sleep(300)

    ChrTalk(
        0xA,
        "#5PY-You all are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYou're the Special\x01",
            "Support Section, aren't\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-270, 1350, 1970, 3000)
    MoveCamera(44, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13600, 3000)

    def lambda_A440():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A440)
    Sleep(50)

    def lambda_A45D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A45D)
    Sleep(50)

    def lambda_A47A():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A47A)
    Sleep(50)

    def lambda_A497():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A497)
    Sleep(50)

    def lambda_A4B4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A4B4)
    Sleep(50)

    def lambda_A4D1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A4D1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00000FIt's good to see you're\x01",
            "both safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FCould everyone else be\x01",
            "here too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. All staff and\x01",
            "artists are accounted\x01",
            "for.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A69C")

    ChrTalk(
        0x9,
        (
            "By the way, we're\x01",
            "practicing for the\x01",
            "reconstruction performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The sudden declaration of martial\x01",
            "law and travel restrictions were\x01",
            "baffling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We discussed the matter, and all\x01",
            "members decided to stay here and\x01",
            "practice instead of returning home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A724")

    label("loc_A69C")


    ChrTalk(
        0x9,
        (
            "By the way, we're\x01",
            "practicing for the\x01",
            "reconstruction performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although the situation\x01",
            "is what it is, this is\x01",
            "all we can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A724")


    ChrTalk(
        0x103,
        "#12P#00204FI see... How admirable.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9AD")

    ChrTalk(
        0x106,
        "#12P#10708F............\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    ChrTalk(
        0xA,
        (
            "#5PCould that be... Is that\x01",
            "Rixia with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x106, 500)

    ChrTalk(
        0x9,
        "Rixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10706F...It's been a while.\x02\x03",
            "#10710FMost importantly, you're\x01",
            "both safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No... How nice of you to\x01",
            "come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I understand there are\x01",
            "details you'd rather not\x01",
            "discuss, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Would you like to\x01",
            "observe our practice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone is doing their\x01",
            "best with practice,\x01",
            "Sully included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10712F#30W............\x02\x03",
            "#10704FI... see...\x02\x01",
            "#10710FIf only for a short\x01",
            "while, could I please...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        "#5P#00002FRixia...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA3F")

    label("loc_A9AD")


    ChrTalk(
        0x9,
        (
            "If you like, please\x01",
            "observe our practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone is doing their\x01",
            "best with practice,\x01",
            "Sully included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()

    label("loc_AA3F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 2110, 0)
    SetScenarioFlags(0x1CF, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AA9D")
    SetChrPos(0x9, 3940, 0, 2900, 90)
    Jump("loc_AAAE")

    label("loc_AA9D")

    SetChrPos(0x9, -2250, 2500, 15000, 180)

    label("loc_AAAE")

    SetChrPos(0xA, 6970, 0, 3480, 270)
    EventEnd(0x5)
    Return()

    # Function_51_A0F6 end

    def Function_52_AAC2(): pass

    label("Function_52_AAC2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_68(-570, 1450, -4770, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16420, 0)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x109, 500, 0, -9730, 0)
    SetChrPos(0x105, -500, 0, -9930, 0)
    SetChrPos(0x9, 5120, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AB86():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB86)

    def lambda_ABA0():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ABA0)
    Sleep(50)

    def lambda_ABB4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABB4)

    def lambda_ABCE():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_ABCE)
    Sleep(50)

    def lambda_ABE2():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ABE2)

    def lambda_ABFC():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_ABFC)
    Sleep(50)

    def lambda_AC10():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC10)

    def lambda_AC2A():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AC2A)
    OP_68(-510, 1450, -3330, 3000)
    SetCameraDistance(17420, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_ACBC():

        label("loc_ACBC")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_ACBC")

    QueueWorkItem2(0x0, 1, lambda_ACBC)

    def lambda_ACCE():

        label("loc_ACCE")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_ACCE")

    QueueWorkItem2(0x1, 1, lambda_ACCE)

    def lambda_ACE0():

        label("loc_ACE0")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_ACE0")

    QueueWorkItem2(0x2, 1, lambda_ACE0)

    def lambda_ACF2():

        label("loc_ACF2")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_ACF2")

    QueueWorkItem2(0x3, 1, lambda_ACF2)
    OP_95(0x9, 0, 0, -1760, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0x9,
        (
            "Special Support Section,\x01",
            "thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, we're terribly sorry.\x01",
            "We're now preparing for this\x01",
            "afternoon's performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FIs that so. Excuse us,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FWell it's not like we\x01",
            "have any business. We'll\x01",
            "come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FSorry for bothering you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x137, 0)
    SetScenarioFlags(0x22, 6)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_AAC2 end

    def Function_53_AE99(): pass

    label("Function_53_AE99")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1450, -6360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16420, 0)
    SetChrPos(0x101, 500, 0, -8230, 0)
    SetChrPos(0x102, -500, 0, -8430, 0)
    SetChrPos(0x103, 500, 0, -9430, 0)
    SetChrPos(0x104, -500, 0, -9630, 0)
    SetChrPos(0x109, 500, 0, -10630, 0)
    SetChrPos(0x105, -500, 0, -10830, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x9, 5120, 0, 3190, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AFA9():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFA9)

    def lambda_AFC3():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AFC3)
    Sleep(50)

    def lambda_AFD7():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AFD7)

    def lambda_AFF1():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AFF1)
    Sleep(50)

    def lambda_B005():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B005)

    def lambda_B01F():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B01F)
    Sleep(50)

    def lambda_B033():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B033)

    def lambda_B04D():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B04D)
    Sleep(50)

    def lambda_B061():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B061)

    def lambda_B07B():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B07B)
    Sleep(50)

    def lambda_B08F():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B08F)

    def lambda_B0A9():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B0A9)
    OP_68(0, 1450, -4360, 3000)
    SetCameraDistance(17420, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B167():

        label("loc_B167")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B167")

    QueueWorkItem2(0x0, 1, lambda_B167)

    def lambda_B179():

        label("loc_B179")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B179")

    QueueWorkItem2(0x1, 1, lambda_B179)

    def lambda_B18B():

        label("loc_B18B")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B18B")

    QueueWorkItem2(0x2, 1, lambda_B18B)

    def lambda_B19D():

        label("loc_B19D")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B19D")

    QueueWorkItem2(0x3, 1, lambda_B19D)

    def lambda_B1AF():

        label("loc_B1AF")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B1AF")

    QueueWorkItem2(0x4, 1, lambda_B1AF)

    def lambda_B1C1():

        label("loc_B1C1")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B1C1")

    QueueWorkItem2(0x5, 1, lambda_B1C1)
    OP_95(0x9, 0, 0, -1760, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0x9,
        (
            "Special Support Section,\x01",
            "thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, we're terribly sorry. We're\x01",
            "now in the middle of the final\x01",
            "renewal performance rehearsal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so. It is coming\x01",
            "up soon, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI'd love to take a peek,\x01",
            "but maybe it would...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. Let's leave before\x01",
            "we bother them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FSorry for bothering you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x16D, 5)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 6)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_AE99 end

    def Function_54_B39A(): pass

    label("Function_54_B39A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow then, we've got to\x01",
            "hurry and catch Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04600FWe're supposed to search\x01",
            "the 2F S-seats, right?\x01",
            "Then let's go!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 48300, 0, -230, 90)
    EventEnd(0x4)
    Return()

    # Function_54_B39A end

    def Function_55_B434(): pass

    label("Function_55_B434")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FThis way is the 2F\x01",
            "audience seats.\x02\x03",
            "We'll be a bother if we\x01",
            "aimlessly wander. Let's\x01",
            "refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_B434 end

    def Function_56_B4C4(): pass

    label("Function_56_B4C4")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FThis way is the 2F\x01",
            "audience seats.\x02\x03",
            "We'll be a bother if we\x01",
            "aimlessly wander. Let's\x01",
            "refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_56_B4C4 end

    def Function_57_B554(): pass

    label("Function_57_B554")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B5E7")

    ChrTalk(
        0x101,
        (
            "#00000FEveryone's doing their best\x01",
            "practicing.\x02\x03",
            "If we want to observe them,\x01",
            "let's enter the stage from\x01",
            "the front entrance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B644")

    label("loc_B5E7")


    ChrTalk(
        0x101,
        (
            "#00000FBalsamo said Sully's\x01",
            "practicing alone today.\x02\x03",
            "Let's not enter the\x01",
            "dressing room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B644")

    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_57_B554 end

    SaveToFile()

Try(main)
