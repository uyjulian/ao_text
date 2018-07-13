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
        "Function_8_E97",          # 08, 8
        "Function_9_1220",         # 09, 9
        "Function_10_162A",        # 0A, 10
        "Function_11_232B",        # 0B, 11
        "Function_12_232F",        # 0C, 12
        "Function_13_2D0F",        # 0D, 13
        "Function_14_3157",        # 0E, 14
        "Function_15_32D6",        # 0F, 15
        "Function_16_3447",        # 10, 16
        "Function_17_3783",        # 11, 17
        "Function_18_3BA2",        # 12, 18
        "Function_19_3CED",        # 13, 19
        "Function_20_428F",        # 14, 20
        "Function_21_4431",        # 15, 21
        "Function_22_46F8",        # 16, 22
        "Function_23_491F",        # 17, 23
        "Function_24_4D8A",        # 18, 24
        "Function_25_4F57",        # 19, 25
        "Function_26_5660",        # 1A, 26
        "Function_27_59A9",        # 1B, 27
        "Function_28_5CB3",        # 1C, 28
        "Function_29_5D7A",        # 1D, 29
        "Function_30_60BC",        # 1E, 30
        "Function_31_685C",        # 1F, 31
        "Function_32_754B",        # 20, 32
        "Function_33_7596",        # 21, 33
        "Function_34_75E1",        # 22, 34
        "Function_35_762C",        # 23, 35
        "Function_36_7677",        # 24, 36
        "Function_37_76C2",        # 25, 37
        "Function_38_770D",        # 26, 38
        "Function_39_7744",        # 27, 39
        "Function_40_7770",        # 28, 40
        "Function_41_8A1C",        # 29, 41
        "Function_42_8A67",        # 2A, 42
        "Function_43_8AB2",        # 2B, 43
        "Function_44_9568",        # 2C, 44
        "Function_45_9597",        # 2D, 45
        "Function_46_95C6",        # 2E, 46
        "Function_47_95F5",        # 2F, 47
        "Function_48_9624",        # 30, 48
        "Function_49_9D14",        # 31, 49
        "Function_50_9D38",        # 32, 50
        "Function_51_A42C",        # 33, 51
        "Function_52_AE0E",        # 34, 52
        "Function_53_B1E6",        # 35, 53
        "Function_54_B6EA",        # 36, 54
        "Function_55_B780",        # 37, 55
        "Function_56_B811",        # 38, 56
        "Function_57_B8A2",        # 39, 57
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
            "There is a car magazine, "Orbal Car Nobility".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36D, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E93")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Noble Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36D, 1)

    label("loc_E93")

    TalkEnd(0xFF)
    Return()

    # Function_7_DE2 end

    def Function_8_E97(): pass

    label("Function_8_E97")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F33")

    ChrTalk(
        0xFE,
        (
            "Actually, Ilya cheered all of\x01",
            "us at the troupe through\x01",
            "orbal phone just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like we're always getting\x01",
            "encouraged by her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121C")

    label("loc_F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F41")
    Jump("loc_121C")

    label("loc_F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F4F")
    Jump("loc_121C")

    label("loc_F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F5D")
    Jump("loc_121C")

    label("loc_F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F6B")
    Jump("loc_121C")

    label("loc_F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F79")
    Jump("loc_121C")

    label("loc_F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F87")
    Jump("loc_121C")

    label("loc_F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F95")
    Jump("loc_121C")

    label("loc_F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FA3")
    Jump("loc_121C")

    label("loc_FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBE")
    Call(0, 9)
    Jump("loc_11E4")

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1122")

    ChrTalk(
        0xB,
        (
            "Hmm... I of all people. Because of the excitement,\x01",
            "I completely failed to notice your presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "However, thank goodness it was you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If this had been seen by another member...\x01",
            "Ilya would have bashed them a hundred times.\x02",
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
    Jump("loc_11E4")

    label("loc_1122")


    ChrTalk(
        0xFE,
        (
            "Hmm... I of all people. Because of the excitement,\x01",
            "I completely failed to notice your presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this had been seen by another member...\x01",
            "Ilya would have bashed them a hundred times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E4")

    Jump("loc_121C")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11F7")
    Jump("loc_121C")

    label("loc_11F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1205")
    Jump("loc_121C")

    label("loc_1205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1213")
    Jump("loc_121C")

    label("loc_1213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_121C")

    label("loc_121C")

    TalkEnd(0xFE)
    Return()

    # Function_8_E97 end

    def Function_9_1220(): pass

    label("Function_9_1220")

    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "I tried to make that costume\x01",
            "design we spoke of before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What do you think about this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yes, very good!\x01",
            "With this direction, I think \x01",
            "there won't be any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Let's have Ilya see it too,\x01",
            "get her opinion and meet\x01",
            "again later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(A new costume design...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(...I'm very excited to see it.)\x02",
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
        "Hmm, who, I wonder...(*hides*)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "Oh, you are...\x01",
            "Could you have overheard?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1430")

    ChrTalk(
        0x101,
        (
            "#00006FUmm...\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_1430")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1461")

    ChrTalk(
        0x102,
        "#00106FEhm... Excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_1461")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1492")

    ChrTalk(
        0x103,
        "#00206FUmm... Excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_1492")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C5")

    ChrTalk(
        0x104,
        (
            "#00306FAhh...\x01",
            "Well, sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_14C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F4")

    ChrTalk(
        0x109,
        (
            "#10106FU-Umm...\x01",
            "Sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_14F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1525")

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, well.\x01",
            "I wonder?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1525")


    ChrTalk(
        0xB,
        "...W-Well, it is all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, that conversation is a top\x01",
            "secret matter to this troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You all didn't hear anything, and\x01",
            "didn't see anything... Understand?\x02",
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

    # Function_9_1220 end

    def Function_10_162A(): pass

    label("Function_10_162A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1711")

    ChrTalk(
        0xFE,
        (
            "With the situation we are in,\x01",
            "Crossbell is even more chaotic, but...\x01",
            "We don't have time to fret over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must do only one thing― \x01",
            "Do all that we can to resume our\x01",
            "performances as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1822")

    ChrTalk(
        0xFE,
        (
            "The sudden declaration of martial law and\x01",
            "travel restrictions were baffling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All members discussed and \x01",
            "decided to stay here and train \x01",
            "instead of returning home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, everyone is so focused\x01",
            "on dance practice that it's surprising.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18ED")

    ChrTalk(
        0xFE,
        (
            "Miss Karelia is on her way to\x01",
            "Miss Ilya's hospital room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Miss Ilya has\x01",
            "not awakened yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the troupe members believe\x01",
            "she will awaken someday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_195F")

    label("loc_18ED")


    ChrTalk(
        0xFE,
        (
            "It seems Miss Ilya has\x01",
            "not awakened yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the troupe members believe\x01",
            "she will awaken someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195F")

    Jump("loc_2327")

    label("loc_1964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC3")

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
        "#00105FIs the entire troupe here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes. For now, they\x01",
            "all show up daily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, ever since that day, Miss Rixia\x01",
            "has not shown her face even once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, all the troupe\x01",
            "members are taking turns visiting\x01",
            "Miss Ilya's hospital room to support her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Miss Sully will be there\x01",
            "all day long today.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1B")

    ChrTalk(
        0x109,
        "#10105FSully...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B51")

    label("loc_1B1B")


    ChrTalk(
        0x109,
        "#10100FYes... We saw her just now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I see...\x02",
    )

    CloseMessageWindow()

    label("loc_1B51")


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
            "I think this may be a long dream...\x01",
            "I suppose that can't be helped.\x02",
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
        (
            "...I am very sorry\x01",
            "for rambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In any case, it's perfectly\x01",
            "fine for you all to go in\x01",
            "and out the theatre.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please visit us anytime\x01",
            "if you need something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Thank you for your concern.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 4)
    SetScenarioFlags(0x18C, 7)
    Jump("loc_1D3B")

    label("loc_1CC3")


    ChrTalk(
        0xFE,
        (
            "Miss Sully is visiting Miss Ilya's\x01",
            "hospital room today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I want her to regain\x01",
            "consciousness quickly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3B")

    Jump("loc_2327")

    label("loc_1D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1DF6")

    ChrTalk(
        0xFE,
        (
            "This evening is the long-awaited\x01",
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
    Jump("loc_2327")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F54")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7D")

    ChrTalk(
        0xFE,
        (
            "If you like, please\x01",
            "talk to Miss Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure speaking with you\x01",
            "will be a good break for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4F")

    label("loc_1E7D")


    ChrTalk(
        0xFE,
        (
            "Miss Sully said she went out without\x01",
            "telling Miss Ilya where she was going, but...\x01",
            "To her, it was clear where she went, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. It seems Miss Ilya\x01",
            "too can't leave Miss Sully\x01",
            "alone, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4F")

    Jump("loc_2327")

    label("loc_1F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1F62")
    Jump("loc_2327")

    label("loc_1F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F70")
    Jump("loc_2327")

    label("loc_1F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2124")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207E")

    ChrTalk(
        0xFE,
        (
            "The renewal performance's opening\x01",
            "night is just three days away.\x02",
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
    Jump("loc_211F")

    label("loc_207E")


    ChrTalk(
        0xFE,
        (
            "We're planning our\x01",
            "final dress rehearsal\x01",
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

    label("loc_211F")

    Jump("loc_2327")

    label("loc_2124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21FD")

    ChrTalk(
        0xFE,
        (
            "About yesterday's play, even the\x01",
            "Troupe Chief was delighted, saying\x01",
            "that is was more successful than usual.\x02",
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
    Jump("loc_2327")

    label("loc_21FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_220B")
    Jump("loc_2327")

    label("loc_220B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2299")

    ChrTalk(
        0xFE,
        (
            "Oh, it's all of\x01",
            "you. Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are looking for Miss Ilya,\x01",
            "she is with Miss Rixia and the\x01",
            "troupe chief on stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2327")

    label("loc_2299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_22A7")
    Jump("loc_2327")

    label("loc_22A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2327")

    ChrTalk(
        0xFE,
        (
            "If you are looking for Miss Ilya or Miss\x01",
            "Rixia, they should be in the hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please\x01",
            "go see them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2327")

    TalkEnd(0xFE)
    Return()

    # Function_10_162A end

    def Function_11_232B(): pass

    label("Function_11_232B")

    Call(0, 12)
    Return()

    # Function_11_232B end

    def Function_12_232F(): pass

    label("Function_12_232F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2402")

    ChrTalk(
        0xA,
        (
            "We're still in the midst of chaos...\x01",
            "Still, we're gradually getting\x01",
            "in contact with other locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, the first thing we need to do is\x01",
            "pull together all the information we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0B")

    label("loc_2402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2603")

    ChrTalk(
        0xA,
        (
            "Right after the State Guard was formed,\x01",
            "we got a request for a special\x01",
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
            "After that, the troupe chief wrote\x01",
            "the script himself, and everyone\x01",
            "practiced up until today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Given the situation, it's\x01",
            "probably impossible to\x01",
            "hold a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, no matter how things are,\x01",
            "we absolutely intend to make\x01",
            "this public performance happen!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26B2")

    label("loc_2603")


    ChrTalk(
        0xA,
        (
            "Given the situation, it's\x01",
            "probably impossible to\x01",
            "hold a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, no matter how things are,\x01",
            "we absolutely intend to make\x01",
            "this public performance happen!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B2")

    Jump("loc_2D0B")

    label("loc_26B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CC")

    ChrTalk(
        0xA,
        (
            "Although Crossbell is in an\x01",
            "important position right now,\x01",
            "there is only one thing we must do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And that is, to continue to believe in Miss Ilya's\x01",
            "recovery and continue to practice daily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I will support her with\x01",
            "everything I have too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2854")

    label("loc_27CC")


    ChrTalk(
        0xA,
        (
            "We must do only one thing.\x01",
            "Support Miss Ilya and continue\x01",
            "to practice daily...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I will support her with\x01",
            "everything I have too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2854")

    Jump("loc_2D0B")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_296F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2918")

    ChrTalk(
        0xA,
        (
            "Just who was that\x01",
            "redheaded girl...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, just where\x01",
            "did Miss Rixia...?\x02",
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
    Jump("loc_296A")

    label("loc_2918")


    ChrTalk(
        0xA,
        (
            "Just who was that\x01",
            "redheaded girl...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And, just where\x01",
            "did Miss Rixia...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296A")

    Jump("loc_2D0B")

    label("loc_296F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A0C")

    ChrTalk(
        0xA,
        (
            "Finally, opening night of the renewal\x01",
            "performance has finally arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, I pray only for the\x01",
            "success of tonight's performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0B")

    label("loc_2A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A1A")
    Jump("loc_2D0B")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A28")
    Jump("loc_2D0B")

    label("loc_2A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A36")
    Jump("loc_2D0B")

    label("loc_2A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ACA")

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
    Jump("loc_2D0B")

    label("loc_2ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B9F")

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
    Jump("loc_2D0B")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BAD")
    Jump("loc_2D0B")

    label("loc_2BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C71")

    ChrTalk(
        0xA,
        (
            "The "West Zemuria Trade Conference"...\x01",
            "It finally opens tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's been quite rare to have a\x01",
            "conference on this scale up until now.\x01",
            "Even I am getting a little nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D0B")

    label("loc_2C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C7F")
    Jump("loc_2D0B")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D0B")

    ChrTalk(
        0xA,
        (
            "Everyone, welcome to the\x01",
            ""Arc-en-ciel" troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you have any question\x01",
            "about our theater, please\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0B")

    TalkEnd(0xA)
    Return()

    # Function_12_232F end

    def Function_13_2D0F(): pass

    label("Function_13_2D0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D20")
    Jump("loc_3139")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E75")

    ChrTalk(
        0xFE,
        "Miss Ilya... She sure is amazing.\x02",
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
        "And until the end, the performance...\x02",
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
    Jump("loc_2F21")

    label("loc_2E75")


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

    label("loc_2F21")

    Jump("loc_3139")

    label("loc_2F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F34")
    Jump("loc_3139")

    label("loc_2F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F42")
    Jump("loc_3139")

    label("loc_2F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F50")
    Jump("loc_3139")

    label("loc_2F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F5E")
    Jump("loc_3139")

    label("loc_2F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F79")
    Call(0, 14)
    Jump("loc_2FBD")

    label("loc_2F79")


    ChrTalk(
        0xFE,
        "Ooh, somehow I'm nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If I do a blunder, it's over.\x02",
    )

    CloseMessageWindow()

    label("loc_2FBD")

    Jump("loc_3139")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FD0")
    Jump("loc_3139")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FDE")
    Jump("loc_3139")

    label("loc_2FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_308A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF9")
    Call(0, 15)
    Jump("loc_3085")

    label("loc_2FF9")


    ChrTalk(
        0xC,
        (
            "*sigh*, whenever I do a slight\x01",
            "violent movement, it ends\x01",
            "up like this immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've got to speak with\x01",
            "Miss Karelia, and soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3085")

    Jump("loc_3139")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3098")
    Jump("loc_3139")

    label("loc_3098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B3")
    Call(0, 16)
    Jump("loc_3139")

    label("loc_30B3")


    ChrTalk(
        0xC,
        (
            "A docile young man... In short,\x01",
            "a late bloomer gentle character?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmph, in that case, preparing for the role will be simple.\x02",
    )

    CloseMessageWindow()

    label("loc_3139")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3156")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_3156")

    Return()

    # Function_13_2D0F end

    def Function_14_3157(): pass

    label("Function_14_3157")

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
        "Alright, if it's like this...\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x0)

    ChrTalk(
        0xF,
        (
            "Eugene, there's something\x01",
            "I want you to do for me...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x13B, 0x0)

    ChrTalk(
        0xC,
        "What is it, Miss Pliｳ?\x02",
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
            "I can't tie it myself alone.\x01",
            "Help me out㈱\x02",
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

    # Function_14_3157 end

    def Function_15_32D6(): pass

    label("Function_15_32D6")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Maaan, as always, my figure in\x01",
            "a costume is sinfulness itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This gallant figure... \x01",
            "Looks like I'll get some new fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "...I hope you're right, Eugene.\x02",
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
            "Guh, seriously?... I've got to\x01",
            "have a word with Miss Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hmph, what a "prince" you're.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_15_32D6 end

    def Function_16_3447(): pass

    label("Function_16_3447")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376A")

    ChrTalk(
        0xC,
        (
            "In any case, that Nikol seems\x01",
            "to be his old self completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah. And it seems his skill\x01",
            "is steadily improving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "He'll surpass you before long if you aren't careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmph, who do you think you're saying that to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Do you really think the "Prince of Arc-\x01",
            "en-ciel" will be surpassed that easily?\x02",
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
        "S-Seriously? How can that be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hu hu, heck if I know.\x01",
            "Why not try asking him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "Theodore, teach me everything you know\x01",
            "to be that kind of docile young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll master it in a week.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "...That's not the problem here.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 3)

    label("loc_376A")

    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_16_3447 end

    def Function_17_3783(): pass

    label("Function_17_3783")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3794")
    Jump("loc_3B9E")

    label("loc_3794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3851")

    ChrTalk(
        0xFE,
        (
            "I feel like Sully has truly\x01",
            "been putting a lot into\x01",
            "her acting lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone remains so impressed\x01",
            "before her technique and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...As if we'd lose to that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B9E")

    label("loc_3851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_385F")
    Jump("loc_3B9E")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_39A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3933")

    ChrTalk(
        0xFE,
        (
            "Still... \x01",
            "Just where is Rixia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like there's some truth she's\x01",
            "hiding, but... She's one of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to believe that\x01",
            "she didn't disappear\x01",
            "from us just like that...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_399F")

    label("loc_3933")


    ChrTalk(
        0xFE,
        (
            "...Just where\x01",
            "did Rixia go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to believe that\x01",
            "she didn't disappear\x01",
            "from us just like that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399F")

    Jump("loc_3B9E")

    label("loc_39A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39B2")
    Jump("loc_3B9E")

    label("loc_39B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39C0")
    Jump("loc_3B9E")

    label("loc_39C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39CE")
    Jump("loc_3B9E")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39DC")
    Jump("loc_3B9E")

    label("loc_39DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F7")
    Call(0, 18)
    Jump("loc_3A7B")

    label("loc_39F7")


    ChrTalk(
        0xFE,
        (
            "...At the end of the day, one's problems can't\x01",
            "be solved without first acknowledging them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Ilya too is\x01",
            "so impatient.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7B")

    Jump("loc_3B9E")

    label("loc_3A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A8E")
    Jump("loc_3B9E")

    label("loc_3A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A9C")
    Jump("loc_3B9E")

    label("loc_3A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB7")
    Call(0, 15)
    Jump("loc_3AFE")

    label("loc_3AB7")


    ChrTalk(
        0xFE,
        (
            "...Now then, I've\x01",
            "finished changing. It's\x01",
            "time to get practicing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AFE")

    Jump("loc_3B9E")

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B11")
    Jump("loc_3B9E")

    label("loc_3B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2C")
    Call(0, 16)
    Jump("loc_3B9E")

    label("loc_3B2C")


    ChrTalk(
        0xD,
        (
            "...Looks like it was a\x01",
            "mistake to stir things up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I guess it brought some\x01",
            "results in its own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B9E")

    TalkEnd(0xFE)
    Return()

    # Function_17_3783 end

    def Function_18_3BA2(): pass

    label("Function_18_3BA2")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "That Sully... \x01",
            "She looks quite worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It seems like she's thinking about\x01",
            "if her acting is lacking, but...\x02",
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
            "But, this is Sully's problem...\x01",
            "Only she can find the answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...Then, we should keep\x01",
            "quiet and watch over her.\x02",
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

    # Function_18_3BA2 end

    def Function_19_3CED(): pass

    label("Function_19_3CED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D73")

    ChrTalk(
        0xFE,
        (
            "Hearing Ilya's energetic\x01",
            "voice was really a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya is Ilya, after all.\x01",
            "We've got to do our best too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4271")

    label("loc_3D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E4A")

    ChrTalk(
        0xFE,
        (
            "Sully is doing her best to fill\x01",
            "the role of princess herself\x01",
            "without losing to pressure.\x02",
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
    Jump("loc_4271")

    label("loc_3E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E58")
    Jump("loc_4271")

    label("loc_3E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE5")

    ChrTalk(
        0xFE,
        (
            "Normally, it'd be time for\x01",
            "singing practice, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*... I don't feel\x01",
            "like it at all right now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3F3C")

    label("loc_3EE5")


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
        "...I can hardly believe it.\x02",
    )

    CloseMessageWindow()

    label("loc_3F3C")

    Jump("loc_4271")

    label("loc_3F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FEE")

    ChrTalk(
        0xFE,
        (
            "Aah, aah, aah♪ \x01",
            "Uhuh, my voice is in top form today㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to put on my mask and\x01",
            "protect my voice until the performance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4032")

    label("loc_3FEE")


    ChrTalk(
        0xFE,
        (
            "The voice is precious to a songstress.\x01",
            "I need another lozenge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4032")

    Jump("loc_4271")

    label("loc_4037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4045")
    Jump("loc_4271")

    label("loc_4045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4053")
    Jump("loc_4271")

    label("loc_4053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4061")
    Jump("loc_4271")

    label("loc_4061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407C")
    Call(0, 14)
    Jump("loc_40F0")

    label("loc_407C")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, looking at Eugene like this,\x01",
            "he's unexpectedly innocent, isn't he㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Somehow even I am embarrassed.\x02",
    )

    CloseMessageWindow()

    label("loc_40F0")

    Jump("loc_4271")

    label("loc_40F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4110")
    Call(0, 20)
    Jump("loc_4193")

    label("loc_4110")


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
            "Being all lined up like that,\x01",
            "as expected, I couldn't tell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4193")

    Jump("loc_4271")

    label("loc_4198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_41A6")
    Jump("loc_4271")

    label("loc_41A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_420F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C1")
    Call(0, 21)
    Jump("loc_420A")

    label("loc_41C1")


    ChrTalk(
        0xFE,
        "Hmm, too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The rice crackers Rixia\x01",
            "gave me are really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_420A")

    Jump("loc_4271")

    label("loc_420F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_421D")
    Jump("loc_4271")

    label("loc_421D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4238")
    Call(0, 22)
    Jump("loc_4271")

    label("loc_4238")


    ChrTalk(
        0xFE,
        (
            "*crunch, munch*... \x01",
            "Ah, this is h-a-p-p-i-n-e-s-s㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4271")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_428E")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_428E")

    Return()

    # Function_19_3CED end

    def Function_20_428F(): pass

    label("Function_20_428F")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "...Yesterday was truly\x01",
            "overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Chancellor Osborne\x01",
            "and Prince Olivert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "President Rocksmith\x01",
            "and Archduke Albert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Princess Klaudia and\x01",
            "Captain Julia... \x01",
            "And then, and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Uh uh, oh Celine, \x01",
            "you sure know your stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I have barely\x01",
            "any idea who\x01",
            "they all are.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "Ooh... I'm envious of your\x01",
            "carefree nature, Miss Pliｳ.\x02",
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

    # Function_20_428F end

    def Function_21_4431(): pass

    label("Function_21_4431")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "Ooh, it's still the day before... \x01",
            "As expected, there's a lot of tension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, we won't have our usual\x01",
            "guests this time, will we.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, you've overcome many\x01",
            "difficulties up until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Have a little more confidence in yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Miss Karelia...\x02",
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
            "Oh, do you want to have a snack\x01",
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
            "No thanks. At a time like this, \x01",
            "I don't want to eat anything at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Miss Pliｳ... You really do everything\x01",
            "at your own pace, don't you.\x02",
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

    # Function_21_4431 end

    def Function_22_46F8(): pass

    label("Function_22_46F8")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "*munch, crunch*... Mmm,\x01",
            "snacks during practice\x01",
            "are the beeest㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "*sigh*. Oh, Miss Pliｳ.\x02",
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
        "Huh? I mean, we're on break now, aren't we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Because sweets are banned during practice,\x01",
            "if I want to eat them, I can only do it now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Seriously... \x01",
            "You're really such a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Pliｳ, the "Mysterious Songstress"... \x01",
            "She's pretty mischievous, isn't she.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(S-Seriously. It's very different\x01",
            "from when she's on stage.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_22_46F8 end

    def Function_23_491F(): pass

    label("Function_23_491F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_49E0")

    ChrTalk(
        0xFE,
        (
            "Miss Ilya's voice... It's been\x01",
            "awhile since I heard it, but\x01",
            "I'm glad she's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what that gigantic tree is,\x01",
            "but anyway, all we can do is practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D86")

    label("loc_49E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_49EE")
    Jump("loc_4D86")

    label("loc_49EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_49FC")
    Jump("loc_4D86")

    label("loc_49FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AA2")

    ChrTalk(
        0xFE,
        (
            "Sully... That girl is... \x01",
            "She's taking it harder than the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Ilya covered for her...and she's\x01",
            "been blaming herself this whole time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D86")

    label("loc_4AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4AB0")
    Jump("loc_4D86")

    label("loc_4AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4ABE")
    Jump("loc_4D86")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4ACC")
    Jump("loc_4D86")

    label("loc_4ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4ADA")
    Jump("loc_4D86")

    label("loc_4ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF5")
    Call(0, 24)
    Jump("loc_4B1A")

    label("loc_4AF5")


    ChrTalk(
        0xFE,
        (
            "I am me...\x01",
            "Is that really true?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B1A")

    Jump("loc_4D86")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3A")
    Call(0, 20)
    Jump("loc_4B76")

    label("loc_4B3A")


    ChrTalk(
        0xFE,
        (
            "Ooh... I'm envious of your\x01",
            "carefree nature, Miss Pliｳ.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B76")

    Jump("loc_4D86")

    label("loc_4B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B89")
    Jump("loc_4D86")

    label("loc_4B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA4")
    Call(0, 21)
    Jump("loc_4BF3")

    label("loc_4BA4")


    ChrTalk(
        0xFE,
        (
            "When I look at Miss Pliｳ, \x01",
            "I can no longer understand\x01",
            "my own nervousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF3")

    Jump("loc_4D86")

    label("loc_4BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C06")
    Jump("loc_4D86")

    label("loc_4C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1E")

    ChrTalk(
        0xFE,
        (
            "Seniors Theo and Eugene\x01",
            "are always together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could it be what they call BL?\x01",
            "The imaginations of some fans...\x02",
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
            "At times like this, I need\x01",
            "to focus on image training.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4D86")

    label("loc_4D1E")


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
            "At times like this, I need\x01",
            "to focus on image training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D86")

    TalkEnd(0xFE)
    Return()

    # Function_23_491F end

    def Function_24_4D8A(): pass

    label("Function_24_4D8A")

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
            "important role than Nikol, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jeez, what are you\x01",
            "saying, Miss Celine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The number of times you appear\x01",
            "in this play have increased, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Even so, if you compare me to others...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jeez, no one could compare you to\x01",
            "anyone else. You know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You are you, the only\x01",
            "one in this troupe.\x02",
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

    # Function_24_4D8A end

    def Function_25_4F57(): pass

    label("Function_25_4F57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FDE")

    ChrTalk(
        0xFE,
        (
            "I'm repairing Miss\x01",
            "Ilya's costume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's my job to make sure our costumes\x01",
            "are always stage ready, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_565C")

    label("loc_4FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF9")
    Call(0, 26)
    Jump("loc_507D")

    label("loc_4FF9")


    ChrTalk(
        0xFE,
        (
            "Uh uh, now that I think\x01",
            "about it, Miss Sully still\x01",
            "has a lot of growing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm really looking forward to seeing that.\x02",
    )

    CloseMessageWindow()

    label("loc_507D")

    Jump("loc_565C")

    label("loc_5082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5090")
    Jump("loc_565C")

    label("loc_5090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5190")

    ChrTalk(
        0xFE,
        (
            "...Even just thinking back to what\x01",
            "happened that day is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Ilya's costume, it was ruined\x01",
            "and stained with blood... \x01",
            "I couldn't even bear to look at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, Miss Ilya... \x01",
            "Why did this have to happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_520E")

    label("loc_5190")


    ChrTalk(
        0xFE,
        (
            "...Even just thinking back to what\x01",
            "happened that day is terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, Miss Ilya... \x01",
            "Why did this have to happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_520E")

    Jump("loc_565C")

    label("loc_5213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_529E")

    ChrTalk(
        0xFE,
        (
            "Uh uh, Miss Pliｳ always\x01",
            "goes at her own pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Celine too seems \x01",
            "well this morning,\x01",
            "so I think she'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_565C")

    label("loc_529E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_52AC")
    Jump("loc_565C")

    label("loc_52AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_52BA")
    Jump("loc_565C")

    label("loc_52BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_52C8")
    Jump("loc_565C")

    label("loc_52C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52E3")
    Call(0, 24)
    Jump("loc_5360")

    label("loc_52E3")


    ChrTalk(
        0xFE,
        (
            "Miss Celine too seems\x01",
            "quite worried.\x02",
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

    label("loc_5360")

    Jump("loc_565C")

    label("loc_5365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5380")
    Call(0, 9)
    Jump("loc_54FC")

    label("loc_5380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5454")

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
            "the artists except Miss Ilya yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So please, keep what you just\x01",
            "saw a secret for a little while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_54FC")

    label("loc_5454")


    ChrTalk(
        0xFE,
        (
            "We haven't given the renewal\x01",
            "performance details to any of\x01",
            "the artists except Miss Ilya yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So please, keep what you just\x01",
            "saw a secret for a little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54FC")

    Jump("loc_565C")

    label("loc_5501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_550F")
    Jump("loc_565C")

    label("loc_550F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_55B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552A")
    Call(0, 21)
    Jump("loc_55AD")

    label("loc_552A")


    ChrTalk(
        0xFE,
        (
            "Miss Ilya aside, even\x01",
            "Miss Pliｳ is unaffected\x01",
            "by pressure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish they'd give\x01",
            "some of their courage \x01",
            "to Miss Celine too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AD")

    Jump("loc_565C")

    label("loc_55B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_55C0")
    Jump("loc_565C")

    label("loc_55C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_565C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55DB")
    Call(0, 22)
    Jump("loc_565C")

    label("loc_55DB")


    ChrTalk(
        0xFE,
        (
            "*sigh*. Anyway, I'll\x01",
            "coordinate your costume\x01",
            "during this break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't stop you anymore, \x01",
            "so please eat them quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_565C")

    TalkEnd(0xFE)
    Return()

    # Function_25_4F57 end

    def Function_26_5660(): pass

    label("Function_26_5660")

    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, Sully... \x01",
            "Have you grown again?\x02",
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
            "Uh uh, don't underestimate\x01",
            "the costume designer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can tell just by seeing\x01",
            "you wearing it a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And so, it just\x01",
            "needs a small\x01",
            "adjustment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12202FI see... \x01",
            "You're amazing, Miss Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, now that I think\x01",
            "about it, Miss Sully still\x01",
            "has a lot of growing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please try to both eat and\x01",
            "practice a lot from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12206FS-Sure...\x01",
            "Thanks, Miss Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Even though the situation's like\x01",
            "this... That's very heartwarming.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5926")

    ChrTalk(
        0x106,
        (
            "#10702F(Uh uh, seems that way.)\x02\x03",
            "#10704F(How can I say this... This theater\x01",
            "seems like a whole other world.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5993")

    label("loc_5926")


    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*, indeed.)\x02\x03",
            "#00104F(How can I say this... This theater\x01",
            "seems like a whole other world.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5993")

    SetScenarioFlags(0x1, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_26_5660 end

    def Function_27_59A9(): pass

    label("Function_27_59A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF1")

    ChrTalk(
        0xFE,
        (
            "No matter what happens, \x01",
            "I'll put my all into my acting...\x02",
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
            "Even though saying that might be conceited,\x01",
            "it's all thanks to Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I listened to her words, I felt\x01",
            "like real power was gushing out of me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5B69")

    label("loc_5AF1")


    ChrTalk(
        0xFE,
        (
            "Miss Ilya is like\x01",
            "the sun itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Giving me this much power\x01",
            "with just words... \x01",
            "I'm really thankful for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B69")

    Jump("loc_5CAF")

    label("loc_5B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B7C")
    Jump("loc_5CAF")

    label("loc_5B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B8A")
    Jump("loc_5CAF")

    label("loc_5B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C1D")

    ChrTalk(
        0xFE,
        (
            "At a time like this, what would\x01",
            "Miss Ilya say to us, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand we've got to do\x01",
            "our best, but... but... but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CAF")

    label("loc_5C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C38")
    Call(0, 18)
    Jump("loc_5CAF")

    label("loc_5C38")


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
            "But I suppose this\x01",
            "is her problem. \x01",
            "...Senior Theodore is right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAF")

    TalkEnd(0xFE)
    Return()

    # Function_27_59A9 end

    def Function_28_5CB3(): pass

    label("Function_28_5CB3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Uh uh, it's a reporter's special privilege to be able\x01",
            "to enter the venue prior to the event like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about Mainz too,\x01",
            "but for today I'll focus on\x01",
            "Arc-en-ciel coverage.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_5CB3 end

    def Function_29_5D7A(): pass

    label("Function_29_5D7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_60B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D98")
    Call(0, 26)
    Jump("loc_60B8")

    label("loc_5D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F70")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EDF")
    TurnDirection(0x12, 0x106, 500)

    ChrTalk(
        0x12,
        (
            "#12201FSis Rixia...\x01",
            "Be very careful on that\x01",
            "breaking into operation.\x02\x03",
            "#12203FI can't really do anything,\x01",
            "but anyway, I've got to at least give\x01",
            "practice everything I've got...\x02\x03",
            "#12201FSo, Sis Rixia and the rest of you\x01",
            "have to do your own best too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702FSully...\x01",
            "Yes, all right!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F68")

    label("loc_5EDF")


    ChrTalk(
        0x12,
        (
            "#12200FGuys...\x01",
            "Be very careful on that\x01",
            "breakthrough operation.\x02\x03",
            "And please take care\x01",
            "of sis Rixia for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah, got it.\x02",
    )

    CloseMessageWindow()

    label("loc_5F68")

    SetScenarioFlags(0x1, 3)
    Jump("loc_60B8")

    label("loc_5F70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6042")
    TurnDirection(0x12, 0x106, 500)

    ChrTalk(
        0x12,
        (
            "#12203FI can't really do anything,\x01",
            "but anyway, I've got to at least give\x01",
            "practice everything I've got...\x02\x03",
            "#12202FSo, Sis Rixia and the rest of you\x01",
            "have to do your own best too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60B8")

    label("loc_6042")


    ChrTalk(
        0x12,
        (
            "#12200FGuys...\x01",
            "Be very careful on that\x01",
            "breakthrough operation.\x02\x03",
            "#12203FAnd please take care\x01",
            "of sis Rixia for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B8")

    TalkEnd(0xFE)
    Return()

    # Function_29_5D7A end

    def Function_30_60BC(): pass

    label("Function_30_60BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D2")

    ChrTalk(
        0x13,
        "#01700FMy, if it isn't the younger brother.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#01700FAnd Tio, too.\x01",
            "Uh uh, it's been awhile.\x02",
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
            "#01700FNow the full membership of the\x01",
            "Support Section is finally assembled.\x02\x03",
            "#01704FIt seems like each and\x01",
            "every one of you has grown\x01",
            "from when I first saw you.\x02\x03",
            "#01709FUs here at Arc-en-ciel won't\x01",
            "lose to you, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHa ha, I'm glad to hear you say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FBut, you guys seem a whole\x01",
            "other level of fired up today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01703FWell, our next performance\x01",
            "will be the last one\x01",
            "before the renewal.\x02\x03",
            "#01700FThinking of it as a culmination, naturally\x01",
            "we want to put everything we have into it.\x02\x03",
            "#01706FIt's too bad Rixia's\x01",
            "off today, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_END)), "loc_654F")

    ChrTalk(
        0x109,
        (
            "#10105FCome to think of it, Miss\x01",
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
            "#01709FAnd each time, I wondered\x01",
            "if she was secretly\x01",
            "meeting with a guy.\x02\x03",
            "#01704FWell if that were the case,\x01",
            "the "Ilya Hands" won't stay silent.\x01",
            "(*fingers moving restlessly*)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_669F")

    label("loc_654F")


    ChrTalk(
        0x109,
        "#10100FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01703FWell, it's gotten less frequent lately, but...\x01",
            "When she wanted time off, there were\x01",
            "many times when she let me know just before.\x02\x03",
            "#01709FAnd each time, I wondered\x01",
            "if she was secretly\x01",
            "meeting with a guy.\x02\x03",
            "#01704FWell if that were the case,\x01",
            "the "Ilya Hands" won't stay silent.\x01",
            "(*fingers moving restlessly*)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_669F")


    ChrTalk(
        0x102,
        "#00105F(*shiver*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I think I can picture\x01",
            "the scene you're imagining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(Miss Elie...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01700FWell, setting aside the issue of Rixia,\x01",
            "we've got to go all-out today.\x02\x03",
            "#01709FYou guys must be busy too,\x01",
            "so let's each do what we have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, got it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 5)
    Jump("loc_6858")

    label("loc_67D2")


    ChrTalk(
        0x13,
        (
            "#01704FNow then, we've got to go\x01",
            "all-out today in any case.\x02\x03",
            "#01700FYou guys must be busy too,\x01",
            "so let's each do what we have to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6858")

    TalkEnd(0xFE)
    Return()

    # Function_30_60BC end

    def Function_31_685C(): pass

    label("Function_31_685C")

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
            "#5PAh, everyone...\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PJust now, a kitty ran\x01",
            "in here at a blindingly\x01",
            "fast speed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah, sorry about that.\x02\x03",
            "#00000FActually, we're in the middle\x01",
            "of tracking down that kitty.\x02",
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
            "#5PYes. On the contrary, it would\x01",
            "be a great help if you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWe're currently preparing for a performance\x01",
            "tonight to which the heads of state are invited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYour timing is perfect. All of our\x01",
            "artists are on break right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, that's convenient.\x02\x03",
            "Then, we'll conduct a quick search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBy the way, do you know\x01",
            "where the kitty was headed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PI'm terribly sorry, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIt was so fast and it\x01",
            "happened so suddenly. \x01",
            "I'm afraid I do not know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHowever, I'm absolutely certain\x01",
            "that it ran up those stairs.\x02",
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
            "#6P#00100FRight. How do you want to divide us?\x02\x03",
            "#00103FThere're three doors, so should\x01",
            "we go with two people for each?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00003FGood point...\x02",
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
            "#04609FShirley's going to accompany\x01",
            "you mister, then㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6F1C():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F1C)
    Sleep(50)

    def lambda_6F2C():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F2C)
    Sleep(50)

    def lambda_6F3C():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6F3C)
    Sleep(50)

    def lambda_6F4C():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F4C)
    Sleep(50)

    def lambda_6F5C():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6F5C)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x102,
        "#6P#00101FW-Wait a minute!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FWhy does it have to be like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04605FMmm, just because?\x02\x03",
            "#04609FAh, did you\x01",
            "misses want to\x01",
            "be with him?\x02",
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
        "#12P#10101FThat's not the issue here...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FAhaha, seems\x01",
            "interesting at least.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00006FThinking it's not your problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...We've come that far, so\x01",
            "don't act in any odd way.\x02\x03",
            "#00301FShirley. \x01",
            "No weird passes at Lloyd,\x01",
            "you hear me?\x02",
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
            "#04600FMister here is cute but not\x01",
            "really Shirley's type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FCute...? \x01",
            "*sigh*, whatever.\x02\x03",
            "#00000FAnyway, let's split up\x01",
            "and search the theater.\x02\x03",
            "Everyone, meet at the entrance\x01",
            "once you're finished.\x02",
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
            "#6P#04602FUh uh, then let's look\x01",
            "for Mary now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, of course.\x02\x03",
            "#00003F(Talking with her like this,\x01",
            "you'd think she's an innocent\x01",
            "and whimsical girl, but...)\x02\x03",
            "(Her threat to kill those\x01",
            "lazy sons earlier was genuine...)\x02\x03",
            "#00001F(I wonder which of\x01",
            "them is the real her...?)\x02",
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
            "fallen for Shirley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I haven't.\x02\x03",
            "#00000FFor now, let's search\x01",
            "the S-seats on 2F.\x02",
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

    # Function_31_685C end

    def Function_32_754B(): pass

    label("Function_32_754B")


    def lambda_7550():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7550)

    def lambda_7561():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7561)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 900, 0, -1900, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_754B end

    def Function_33_7596(): pass

    label("Function_33_7596")


    def lambda_759B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_759B)

    def lambda_75AC():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75AC)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -900, 0, -1900, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_7596 end

    def Function_34_75E1(): pass

    label("Function_34_75E1")


    def lambda_75E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_75E6)

    def lambda_75F7():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75F7)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -900, 0, -4300, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_75E1 end

    def Function_35_762C(): pass

    label("Function_35_762C")


    def lambda_7631():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7631)

    def lambda_7642():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7642)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 0, -3100, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_35_762C end

    def Function_36_7677(): pass

    label("Function_36_7677")


    def lambda_767C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_767C)

    def lambda_768D():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_768D)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -900, 0, -3100, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_36_7677 end

    def Function_37_76C2(): pass

    label("Function_37_76C2")


    def lambda_76C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_76C7)

    def lambda_76D8():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_76D8)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 800, 0, -4300, 2000, 0x0)
    OP_93(0x1A3, 0x0, 0x1F4)
    Return()

    # Function_37_76C2 end

    def Function_38_770D(): pass

    label("Function_38_770D")


    def lambda_7712():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7712)

    def lambda_7723():
        OP_95(0xFE, 50110, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7723)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x1A3, 500)
    Return()

    # Function_38_770D end

    def Function_39_7744(): pass

    label("Function_39_7744")


    def lambda_7749():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_7749)

    def lambda_775A():
        OP_95(0xFE, 48110, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_775A)
    Return()

    # Function_39_7744 end

    def Function_40_7770(): pass

    label("Function_40_7770")

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
        "#5P#04605FHuh, who's that girl...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FCould she be...\x01",
            "Rixia?\x02",
        )
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

    def lambda_79F7():
        OP_95(0xFE, 900, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79F7)
    Sleep(50)

    def lambda_7A14():
        OP_95(0xFE, -800, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7A14)
    OP_68(-660, 1450, 2200, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13470, 3000)
    WaitChrThread(0x1A3, 1)

    def lambda_7A60():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7A60)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5P#00000FIt is Rixia.\x02\x03",
            "#00005FWasn't all the\x01",
            "artists on break?\x02",
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
            "Oh, Mr. Lloyd.\x02\x03",
            "Umm, I was having my clothes\x01",
            "repaired late last night...\x02\x03",
            "I'm performing a final costume\x01",
            "check before tonight's performance.\x02\x03",
            "But more importantly... \x01",
            "I hear a kitty got in here?\x02",
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
        "#5P#00001FYes, that's right, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00005FWait, huh?\x02\x03",
            "Chasing her down,\x01",
            "we returned here...\x02",
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
            "#6P#10100FI don't think she\x01",
            "came in here.\x02",
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
            "#5P#00100FLooks like it.\x01",
            "Even Miss Rixia.\x02",
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
            "#11P#00005FIf that's true, then it means no one's\x01",
            "seen her since we lost sight of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FI had them close the entrance...\x02\x03",
            "#00100FShe's most likely\x01",
            "still in this hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHmm, it seems like\x01",
            "she's hidin' somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI agree. Shall we\x01",
            "all search together?\x02",
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
        "#5P#00000FAh, she's──\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#5P#04609FAhaha, you're amazing♪\x02\x03",
            "#04611FI've been watching you for quite awhile.\x01",
            "And you never let down your guard even once!\x02",
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
            "#12P#00303F...She's my \x01",
            "stupid cousin.\x02\x03",
            "#00300FDon't worry about her too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11P#06205FMr. Randy's...\x02",
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
            "Shirley Orlando!\x01",
            "You can call me Shirley!\x02\x03",
            "Man, I saw you on the \x01",
            "Arc-en-ciel stage, though.\x02\x03",
            "Looking at you from up close like\x01",
            "this though, it seems like your\x01",
            "destructive power is exceptional!\x02\x03",
            "Must be nice. They're\x01",
            "so big. I'm jealous㈱\x02",
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
            "#5P#04609FAhaha, it's fine.\x01",
            "It's not that they'll shrink...\x02\x03",
            "This too could be some kind of fate──\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x15)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_851F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_851F)
    Sleep(50)

    def lambda_852F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_852F)
    Sleep(300)

    ChrTalk(
        0x1A3,
        "#6P#04605FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12P#06205FAh...!\x02",
    )

    CloseMessageWindow()

    def lambda_856D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_856D)
    Sleep(50)

    def lambda_857D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_857D)
    Sleep(50)

    def lambda_858D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_858D)
    Sleep(50)

    def lambda_859D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_859D)
    Sleep(50)

    def lambda_85AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85AD)
    Sleep(50)

    def lambda_85BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_85BD)
    Sleep(50)

    def lambda_85CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_85CD)
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

    def lambda_86D3():
        OP_95(0xFE, 0, 2500, 18930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_86D3)
    Sleep(1000)

    def lambda_86F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_86F0)
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
            "#11P#00011FS-So that's where\x01",
            "she was hiding...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11P#06201FI'll chase her!\x02",
    )

    CloseMessageWindow()

    def lambda_8795():

        label("loc_8795")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_8795")

    QueueWorkItem2(0x102, 1, lambda_8795)

    def lambda_87A7():

        label("loc_87A7")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_87A7")

    QueueWorkItem2(0x104, 1, lambda_87A7)

    def lambda_87B9():

        label("loc_87B9")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_87B9")

    QueueWorkItem2(0x109, 1, lambda_87B9)

    def lambda_87CB():

        label("loc_87CB")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_87CB")

    QueueWorkItem2(0x105, 1, lambda_87CB)
    OP_95(0x15, 1290, 0, 5610, 4000, 0x0)

    def lambda_87F1():
        OP_95(0xFE, 0, 2500, 15240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_87F1)
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
        "#12P#00306F*sigh*, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FUmm... \x01",
            "What should we do?\x02",
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

    def lambda_891B():

        label("loc_891B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_891B")

    QueueWorkItem2(0x102, 1, lambda_891B)
    Sleep(50)

    def lambda_8930():

        label("loc_8930")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8930")

    QueueWorkItem2(0x104, 1, lambda_8930)
    Sleep(50)

    def lambda_8945():

        label("loc_8945")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8945")

    QueueWorkItem2(0x109, 1, lambda_8945)
    Sleep(50)

    def lambda_895A():

        label("loc_895A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_895A")

    QueueWorkItem2(0x105, 1, lambda_895A)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, I hope we finally\x01",
            "catch her this time.\x02",
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

    # Function_40_7770 end

    def Function_41_8A1C(): pass

    label("Function_41_8A1C")


    def lambda_8A21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A21)

    def lambda_8A32():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A32)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -6510, 2500, 12970, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_41_8A1C end

    def Function_42_8A67(): pass

    label("Function_42_8A67")


    def lambda_8A6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8A6C)

    def lambda_8A7D():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A7D)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -7770, 2500, 12730, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_42_8A67 end

    def Function_43_8AB2(): pass

    label("Function_43_8AB2")

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
            "#12P#04600FAhaha, thanks♪ \x01",
            "You really saved her.\x02",
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
            "#06204FAnd, I'm sure Miss Shirley \x01",
            "would have saved the kitty\x01",
            "if I hadn't stepped in.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04605FHah, see that?\x02\x03",
            "#04604FWith that timing, I could\x01",
            "have saved her if I jumped.\x02\x03",
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
        "#12P#00106FMy deepest apologies, Miss Rixia.\x02",
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
            "E-Even so,\x01",
            "I'm terribly sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "To think there was a kitty on stage...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Still, I was operating our equipment\x01",
            "for inspection without checking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04600FWell, isn't it fine?\x02\x03",
            "#04604FNo one got hurt, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FRight. Please, don't worry\x01",
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
            "#12P#10300FOh, right. He's probably in the middle\x01",
            "of worriedly searching for Mary.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0x14,
        "#6PNya～n♪\x02",
    )

    CloseMessageWindow()

    def lambda_90E5():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_90E5)
    Sleep(50)

    def lambda_90F5():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_90F5)
    Sleep(50)

    def lambda_9105():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9105)
    Sleep(50)

    def lambda_9115():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9115)
    Sleep(50)

    def lambda_9125():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9125)
    Sleep(50)

    def lambda_9135():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9135)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00309FHa ha...how\x01",
            "self-interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FThat's true. She was so scared\x01",
            "until just a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#11P#04609FAhaha, that's how cats are, see?\x02",
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
            "#12P#00000F──Well then, allow us\x01",
            "to excuse ourselves.\x02\x03",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_928D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_928D)
    Sleep(50)

    def lambda_929D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_929D)
    Sleep(50)

    def lambda_92AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_92AD)
    Sleep(50)

    def lambda_92BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92BD)
    Sleep(50)

    def lambda_92CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_92CD)
    Sleep(300)

    ChrTalk(
        0x9,
        "No, no. Perish the thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#06202FUh uh. Please, take care.\x02",
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

    def lambda_938E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_938E)
    WaitChrThread(0x14, 3)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A3, 0x15, 500)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#12P#04605FOh, hey miss.\x02\x03",
            "#04602FCan I call\x01",
            "you Rixia?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#5P#06205FAh...\x02\x03",
            "#06202FYes. Of course,\x01",
            "I don't mind it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FUh uh, thanks Rixia.\x02\x03",
            "#04600FSee you later!\x02",
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
            "#06203F#3243V(Mr. Randy's cousin...)\x02\x03",
            "#06201F#3244V(So she's the rumored\x01",
            ""Bloody Shirley"...)\x02",
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

    # Function_43_8AB2 end

    def Function_44_9568(): pass

    label("Function_44_9568")


    def lambda_956D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_956D)
    Sleep(800)

    def lambda_958A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_958A)
    Return()

    # Function_44_9568 end

    def Function_45_9597(): pass

    label("Function_45_9597")


    def lambda_959C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_959C)
    Sleep(1500)

    def lambda_95B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_95B9)
    Return()

    # Function_45_9597 end

    def Function_46_95C6(): pass

    label("Function_46_95C6")


    def lambda_95CB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95CB)
    Sleep(2000)

    def lambda_95E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_95E8)
    Return()

    # Function_46_95C6 end

    def Function_47_95F5(): pass

    label("Function_47_95F5")


    def lambda_95FA():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95FA)
    Sleep(500)

    def lambda_9617():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9617)
    Return()

    # Function_47_95F5 end

    def Function_48_9624(): pass

    label("Function_48_9624")

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

    def lambda_9739():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9739)

    def lambda_9753():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9753)
    Sleep(50)

    def lambda_9767():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9767)

    def lambda_9781():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9781)
    Sleep(50)

    def lambda_9795():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9795)

    def lambda_97AF():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_97AF)
    Sleep(50)

    def lambda_97C3():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_97C3)

    def lambda_97DD():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_97DD)
    Sleep(50)

    def lambda_97F1():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_97F1)

    def lambda_980B():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_980B)
    Sleep(50)

    def lambda_981F():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_981F)

    def lambda_9839():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9839)
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
        "Oh, it's the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although we are closed today,\x01",
            "did you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUh, no, we're\x01",
            "just stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThe opening of the renewal\x01",
            "performance... It's finally tomorrow.\x02\x03",
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
            "practicing today, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWow, how devoted.\x01",
            "Could she be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You understand correctly.\x01",
            "Yes, it is Miss Sully.\x02",
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
            "It seems that she can't calm down\x01",
            "if she is not moving her body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you all would like, please\x01",
            "go watch her practicing.\x02",
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
            "Yes of course. If it is you all, who have\x01",
            "helped us countless times, none of us here at\x01",
            "Arc-en-ciel would have any problem with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "On top of that, it seems she has\x01",
            "been at it since morning with\x01",
            "hardly any breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you like, please\x01",
            "go speak with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think it will make\x01",
            "a nice break for her.\x02",
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
        "#00100FThank you for your kindness.\x02",
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

    # Function_48_9624 end

    def Function_49_9D14(): pass

    label("Function_49_9D14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -70, 2500, 15340, 180)
    EventEnd(0x5)
    Return()

    # Function_49_9D14 end

    def Function_50_9D38(): pass

    label("Function_50_9D38")

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

    def lambda_9E31():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E31)

    def lambda_9E4B():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E4B)
    Sleep(50)

    def lambda_9E5F():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E5F)

    def lambda_9E79():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E79)
    Sleep(500)

    def lambda_9E8D():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E8D)

    def lambda_9EA7():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9EA7)
    Sleep(50)

    def lambda_9EBB():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9EBB)

    def lambda_9ED5():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9ED5)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#00005FThe Arc-en-ciel, huh... It's been\x01",
            "awhile since we were last here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, indeed.\x01",
            "I wonder if Miss Ilya and\x01",
            "Miss Rixia are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, you guys sure know\x01",
            "a lot of famous people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FB-But, are you sure? \x01",
            "Entering like this for no reason...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 500)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A02D():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A02D)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "Well, well, if it isn't Mr. Lloyd and Miss\x01",
            "Elie of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It has been a long time. What\x01",
            "business do you have with us today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FActually, the Support Section\x01",
            "has resumed its activities recently.\x02\x03",
            "We were patrolling the city\x01",
            "and wanted to stop by.\x02",
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
            "No, of course you\x01",
            "are no bother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We are on break right\x01",
            "now, so please, come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am sure Miss Ilya and the others\x01",
            "will be delighted to see you.\x02",
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

    def lambda_A26D():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A26D)
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#00105FWhat's wrong, Miss Noｱl?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#12P#10102FWell, I just want to say again how\x01",
            "amazing the Special Support Section is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, that's right. To think\x01",
            "you're so famous you can\x01",
            "get into even Arc-en-ciel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHa ha, now that I think\x01",
            "about it, you're right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes. I'm thankful for our good connections.\x02",
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

    # Function_50_9D38 end

    def Function_51_A42C(): pass

    label("Function_51_A42C")

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

    def lambda_A553():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A553)

    def lambda_A56D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A56D)
    Sleep(100)

    def lambda_A581():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A581)

    def lambda_A59B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A59B)
    Sleep(500)

    def lambda_A5AF():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A5AF)

    def lambda_A5C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A5C9)
    Sleep(100)
    OP_68(-970, 1450, -1300, 3000)
    MoveCamera(44, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15070, 3000)

    def lambda_A60B():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A60B)

    def lambda_A625():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A625)
    Sleep(500)

    def lambda_A639():
        OP_95(0xFE, -500, 0, -5100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A639)

    def lambda_A653():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A653)
    Sleep(100)

    def lambda_A667():
        OP_95(0xFE, 500, 0, -5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A667)

    def lambda_A681():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A681)
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

    def lambda_A6D6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A6D6)
    Sleep(50)

    def lambda_A6E6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A6E6)
    Sleep(300)

    ChrTalk(
        0xA,
        "#5PY-You guys are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYou're the Special Support\x01",
            "Section, aren't you!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-270, 1350, 1970, 3000)
    MoveCamera(44, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13600, 3000)

    def lambda_A777():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A777)
    Sleep(50)

    def lambda_A794():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A794)
    Sleep(50)

    def lambda_A7B1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A7B1)
    Sleep(50)

    def lambda_A7CE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A7CE)
    Sleep(50)

    def lambda_A7EB():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A7EB)
    Sleep(50)

    def lambda_A808():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A808)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00000FGood to see you're both safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FCould everyone\x01",
            "else be here too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes. All staff and artists\x01",
            "are accounted for.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C2")

    ChrTalk(
        0x9,
        (
            "By the way, they're now\x01",
            "practicing on the newly\x01",
            "reconstructed stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The sudden declaration of martial law and\x01",
            "travel restrictions were baffling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "All members discussed and \x01",
            "decided to stay here and train \x01",
            "instead of returning home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA4E")

    label("loc_A9C2")


    ChrTalk(
        0x9,
        (
            "By the way, they're now\x01",
            "practicing on the newly\x01",
            "reconstructed stage.\x02",
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

    label("loc_AA4E")


    ChrTalk(
        0x103,
        (
            "#12P#00204FI see... \x01",
            "How admirable.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACE8")

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
            "#5PCould that be...\x01",
            "Is that Miss\x01",
            "Rixia with you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x106, 500)

    ChrTalk(
        0x9,
        "Miss Rixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10706F...It has been awhile.\x02\x03",
            "#10710FI'm glad you're all safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No... How good of you\x01",
            "to show your face too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I understand there are details\x01",
            "you would rather not discuss, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Would you like to\x01",
            "observe them practice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Starting with Miss Sully, everyone\x01",
            "is doing their best practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10712F#30W............\x02\x03",
            "#10704FI...see...\x02\x01",
            "#10710FIf it is only for a short while...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        "#5P#00002FRixia...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD8B")

    label("loc_ACE8")


    ChrTalk(
        0x9,
        (
            "If you like, please\x01",
            "observe them practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Starting with Miss Sully, everyone\x01",
            "is doing their best practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FSure, thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_AD8B")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ADE9")
    SetChrPos(0x9, 3940, 0, 2900, 90)
    Jump("loc_ADFA")

    label("loc_ADE9")

    SetChrPos(0x9, -2250, 2500, 15000, 180)

    label("loc_ADFA")

    SetChrPos(0xA, 6970, 0, 3480, 270)
    EventEnd(0x5)
    Return()

    # Function_51_A42C end

    def Function_52_AE0E(): pass

    label("Function_52_AE0E")

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

    def lambda_AED2():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AED2)

    def lambda_AEEC():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AEEC)
    Sleep(50)

    def lambda_AF00():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF00)

    def lambda_AF1A():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AF1A)
    Sleep(50)

    def lambda_AF2E():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AF2E)

    def lambda_AF48():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF48)
    Sleep(50)

    def lambda_AF5C():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF5C)

    def lambda_AF76():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AF76)
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

    def lambda_B008():

        label("loc_B008")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B008")

    QueueWorkItem2(0x0, 1, lambda_B008)

    def lambda_B01A():

        label("loc_B01A")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B01A")

    QueueWorkItem2(0x1, 1, lambda_B01A)

    def lambda_B02C():

        label("loc_B02C")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B02C")

    QueueWorkItem2(0x2, 1, lambda_B02C)

    def lambda_B03E():

        label("loc_B03E")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B03E")

    QueueWorkItem2(0x3, 1, lambda_B03E)
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
            "#11P#00005FIs that so.\x01",
            "Excuse us, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FWell it's not like we have any\x01",
            "business. We'll come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHu hu, that's right.\x02",
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

    # Function_52_AE0E end

    def Function_53_B1E6(): pass

    label("Function_53_B1E6")

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

    def lambda_B2F6():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2F6)

    def lambda_B310():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B310)
    Sleep(50)

    def lambda_B324():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B324)

    def lambda_B33E():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B33E)
    Sleep(50)

    def lambda_B352():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B352)

    def lambda_B36C():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B36C)
    Sleep(50)

    def lambda_B380():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B380)

    def lambda_B39A():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B39A)
    Sleep(50)

    def lambda_B3AE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B3AE)

    def lambda_B3C8():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B3C8)
    Sleep(50)

    def lambda_B3DC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B3DC)

    def lambda_B3F6():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B3F6)
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

    def lambda_B4B4():

        label("loc_B4B4")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B4B4")

    QueueWorkItem2(0x0, 1, lambda_B4B4)

    def lambda_B4C6():

        label("loc_B4C6")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B4C6")

    QueueWorkItem2(0x1, 1, lambda_B4C6)

    def lambda_B4D8():

        label("loc_B4D8")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B4D8")

    QueueWorkItem2(0x2, 1, lambda_B4D8)

    def lambda_B4EA():

        label("loc_B4EA")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B4EA")

    QueueWorkItem2(0x3, 1, lambda_B4EA)

    def lambda_B4FC():

        label("loc_B4FC")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B4FC")

    QueueWorkItem2(0x4, 1, lambda_B4FC)

    def lambda_B50E():

        label("loc_B50E")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B50E")

    QueueWorkItem2(0x5, 1, lambda_B50E)
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
            "However, we're terribly sorry. \x01",
            "We're now in the middle of the final\x01",
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
            "but maybe this would...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes. Let's leave\x01",
            "before we bother them.\x02",
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

    # Function_53_B1E6 end

    def Function_54_B6EA(): pass

    label("Function_54_B6EA")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FNow then, we've got\x01",
            "to hurry after Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04600FWe're supposed to search the 2F\x01",
            "S-seats, right? Then let's go!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 48300, 0, -230, 90)
    EventEnd(0x4)
    Return()

    # Function_54_B6EA end

    def Function_55_B780(): pass

    label("Function_55_B780")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FThis way is the 2F audience seats.\x02\x03",
            "We'll be a bother if we aimlessly wander. \x01",
            "Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_B780 end

    def Function_56_B811(): pass

    label("Function_56_B811")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FThis way is the 2F audience seats.\x02\x03",
            "We'll be a bother if we aimlessly wander. \x01",
            "Let's refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_56_B811 end

    def Function_57_B8A2(): pass

    label("Function_57_B8A2")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B935")

    ChrTalk(
        0x101,
        (
            "#00000FEveryone's doing their best practicing.\x02\x03",
            "If we want to observe them, let's enter\x01",
            "the stage from the front entrance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B99D")

    label("loc_B935")


    ChrTalk(
        0x101,
        (
            "#00000F...Manager Balsamo said Sully's\x01",
            "practicing alone today.\x02\x03",
            "Let's not enter the dressing room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B99D")

    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_57_B8A2 end

    SaveToFile()

Try(main)
