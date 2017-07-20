from ScenarioHelper import *

def main():
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
        "Karelia",               # 1
        "Balsamo Manager",         # 2
        "Reception Roland",         # 3
        "Aban Theater Company Manager",           # 4
        "Eugene",             # 5
        "Theodore",             # 6
        "Nicole",                 # 7
        "Priure",                 # 8
        "Celine",               # 9
        "Reporter Noticia",         # 10
        "Shuri",                 # 11
        "Ilia",                 # 12
        "Mary",                 # 13
        "Lisha",               # 14
        "Heinz",               # 15
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
        "Function_8_E83",          # 08, 8
        "Function_9_11A5",         # 09, 9
        "Function_10_15C9",        # 0A, 10
        "Function_11_2264",        # 0B, 11
        "Function_12_2268",        # 0C, 12
        "Function_13_2B61",        # 0D, 13
        "Function_14_2ECE",        # 0E, 14
        "Function_15_304C",        # 0F, 15
        "Function_16_319A",        # 10, 16
        "Function_17_34A7",        # 11, 17
        "Function_18_38BF",        # 12, 18
        "Function_19_3A18",        # 13, 19
        "Function_20_3F74",        # 14, 20
        "Function_21_4115",        # 15, 21
        "Function_22_438C",        # 16, 22
        "Function_23_4564",        # 17, 23
        "Function_24_49CB",        # 18, 24
        "Function_25_4BA6",        # 19, 25
        "Function_26_528B",        # 1A, 26
        "Function_27_55B4",        # 1B, 27
        "Function_28_58AF",        # 1C, 28
        "Function_29_5945",        # 1D, 29
        "Function_30_5C46",        # 1E, 30
        "Function_31_6397",        # 1F, 31
        "Function_32_7070",        # 20, 32
        "Function_33_70BB",        # 21, 33
        "Function_34_7106",        # 22, 34
        "Function_35_7151",        # 23, 35
        "Function_36_719C",        # 24, 36
        "Function_37_71E7",        # 25, 37
        "Function_38_7232",        # 26, 38
        "Function_39_7269",        # 27, 39
        "Function_40_7295",        # 28, 40
        "Function_41_85A1",        # 29, 41
        "Function_42_85EC",        # 2A, 42
        "Function_43_8637",        # 2B, 43
        "Function_44_9117",        # 2C, 44
        "Function_45_9146",        # 2D, 45
        "Function_46_9175",        # 2E, 46
        "Function_47_91A4",        # 2F, 47
        "Function_48_91D3",        # 30, 48
        "Function_49_9890",        # 31, 49
        "Function_50_98B4",        # 32, 50
        "Function_51_9F3C",        # 33, 51
        "Function_52_A950",        # 34, 52
        "Function_53_AD1F",        # 35, 53
        "Function_54_B212",        # 36, 54
        "Function_55_B29C",        # 37, 55
        "Function_56_B315",        # 38, 56
        "Function_57_B38E",        # 39, 57
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
            "There is a car magazine \"Driving Car Noblemen\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('高贵色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7F")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Noble color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('高贵色彩', 1)

    label("loc_E7F")

    TalkEnd(0xFF)
    Return()

    # Function_7_DE2 end

    def Function_8_E83(): pass

    label("Function_8_E83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F27")

    ChrTalk(
        0xFE,
        (
            "Actually, earlier from Iria\x01",
            "Through conduct communication to everyone in the theater company\x01",
            "The ale arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To what extent, to Iria\x01",
            "I've only got the courage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A1")

    label("loc_F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_F35")
    Jump("loc_11A1")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F43")
    Jump("loc_11A1")

    label("loc_F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F51")
    Jump("loc_11A1")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F5F")
    Jump("loc_11A1")

    label("loc_F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F6D")
    Jump("loc_11A1")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F7B")
    Jump("loc_11A1")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F89")
    Jump("loc_11A1")

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F97")
    Jump("loc_11A1")

    label("loc_F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_116E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB2")
    Call(0, 9)
    Jump("loc_1169")

    label("loc_FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D9")

    ChrTalk(
        0xB,
        (
            "Ummm … what you have done with me.\x01",
            "I was excited and did not notice my signs at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "But it was still good for you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If other members were watching it ……\x01",
            "It was the place where Iria was hit by a hundred.\x02",
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
    Jump("loc_1169")

    label("loc_10D9")


    ChrTalk(
        0xFE,
        (
            "Ummm … what you have done with me.\x01",
            "I was excited and did not notice my signs at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If other members were watching it ……\x01",
            "It was the place where Iria was hit by a hundred.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1169")

    Jump("loc_11A1")

    label("loc_116E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_117C")
    Jump("loc_11A1")

    label("loc_117C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_118A")
    Jump("loc_11A1")

    label("loc_118A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1198")
    Jump("loc_11A1")

    label("loc_1198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_11A1")

    label("loc_11A1")

    TalkEnd(0xFE)
    Return()

    # Function_8_E83 end

    def Function_9_11A5(): pass

    label("Function_9_11A5")

    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "A design picture of an example costume\x01",
            "I tried to wake up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How about with this feeling?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, it's okay!\x01",
            "The basic direction is this\x01",
            "I do not think there is any problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Iria, have you take a look\x01",
            "Because I put together opinions,\x01",
            "Let's meet again later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(A new costume design picture …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(…… It is very interesting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 0)

    ChrTalk(
        0x8,
        "Oh, are you …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Mumu, someone … (Sasa)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 0)

    ChrTalk(
        0xB,
        (
            "Oh, you guys ……\x01",
            "… … … No way, are you talking about now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(
        0x101,
        (
            "#00006FEr …\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_13B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EB")

    ChrTalk(
        0x102,
        "#00106FExcuse me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_13EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")

    ChrTalk(
        0x103,
        "#00206FUm … … I'm sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1423")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1464")

    ChrTalk(
        0x104,
        (
            "#00306FUh……\x01",
            "Something, sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_1464")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149F")

    ChrTalk(
        0x109,
        (
            "#10106FLet me see……\x01",
            "Excuse me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D5")

    label("loc_149F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D5")

    ChrTalk(
        0x105,
        (
            "#10302FHuh, come on.\x01",
            "what about?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D5")


    ChrTalk(
        0xB,
        "… Well, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, the current story is that of our theater company\x01",
            "In top secret matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You guys did not see anything here,\x01",
            "I did not hear anything … good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FOh, I promise.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x14B, 5)
    Return()

    # Function_9_11A5 end

    def Function_10_15C9(): pass

    label("Function_10_15C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16A0")

    ChrTalk(
        0xFE,
        (
            "The circumstances surrounding the crossbell are\x01",
            "I have also tried to confuse even more … …\x01",
            "I do not have time to think freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One thing we should do -\x01",
            "Everything for resuming as soon as possible\x01",
            "It's only to make efforts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_16A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1780")

    ChrTalk(
        0xFE,
        (
            "For sudden martial law and curfews\x01",
            "I was puzzled … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as I return home,\x01",
            "Whether practicing here or not\x01",
            "Discuss with everyone and decide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even now, with amazing concentration ability\x01",
            "I am working on the stage practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_18BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1848")

    ChrTalk(
        0xFE,
        (
            "Today I went to Iria's room.\x01",
            "Karelia is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Iria still has his eyes\x01",
            "I do not seem to get awake ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All members of the theater company,\x01",
            "I believe in the day of waking up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18B6")

    label("loc_1848")


    ChrTalk(
        0xFE,
        (
            "Ilia still has his eyes\x01",
            "I do not seem to get awake ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All members of the theater company,\x01",
            "I believe in the day of waking up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B6")

    Jump("loc_2260")

    label("loc_18BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4E")

    ChrTalk(
        0x9,
        "Why, everyone ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Fthat………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FAll the members of the group ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, everyone has a face every day\x01",
            "I am trying to make it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even so, since that day,\x01",
            "Although we are not showing up in any way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By the way, to Iria's sickroom\x01",
            "The members of the theater exchange on a daily basis\x01",
            "I am going to take care of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today Sri Mr.\x01",
            "You should have taken care of yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")

    ChrTalk(
        0x109,
        "#10105FShri-chan …\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD9")

    label("loc_1A98")


    ChrTalk(
        0x109,
        "#10100FYeah … … I just met you a while ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh really……\x02",
    )

    CloseMessageWindow()

    label("loc_1AD9")


    ChrTalk(
        0x9,
        (
            "……However,\x01",
            "I still can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if you are watching even a long dream,\x01",
            "Thinking that … … It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FManager …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Talk about taking no mercy\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, if you are\x01",
            "Allow free access to the theater\x01",
            "Please do it fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is something again,\x01",
            "Please come at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F…… Thank you for your consideration.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 4)
    SetScenarioFlags(0x18C, 7)
    Jump("loc_1CC8")

    label("loc_1C4E")


    ChrTalk(
        0xFE,
        (
            "To Iria's room\x01",
            "Shuri should be doing today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, consciousness as soon as possible\x01",
            "I'd like you to regain it ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC8")

    Jump("loc_2260")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D7F")

    ChrTalk(
        0xFE,
        (
            "Today afternoon,\x01",
            "Finally \"Golden Sun, the Moon of Silver\"\x01",
            "Renewal performance will be released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The finish of the stage is splendid ……\x01",
            "If you can satisfy everyone\x01",
            "I am convinced.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ECD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E12")

    ChrTalk(
        0xFE,
        (
            "If you do not mind, Shuri\x01",
            "Please give me a voice as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely, even for that girl\x01",
            "I think that it will be a good relief.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC8")

    label("loc_1E12")


    ChrTalk(
        0xFE,
        (
            "Shuri is a secret to Iria\x01",
            "I was told that it came out … …\x01",
            "Were you where the location was obvious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, but Iria also\x01",
            "All about Shuri\x01",
            "I do not think you can leave it alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC8")

    Jump("loc_2260")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1EDB")
    Jump("loc_2260")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EE9")
    Jump("loc_2260")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2076")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDB")

    ChrTalk(
        0xFE,
        (
            "The release date of the renewal performance also\x01",
            "Finally I came close in three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, tomorrow it took a whole day\x01",
            "Final rehearsal assuming real number\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside the theater company,\x01",
            "Because it will be off limits\x01",
            "Please acknowledge it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2071")

    label("loc_1FDB")


    ChrTalk(
        0xFE,
        (
            "Take me one day tomorrow\x01",
            "Final rehearsal assuming real number\x01",
            "We are planning to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside the theater company,\x01",
            "Because it will be off limits\x01",
            "Please acknowledge it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2071")

    Jump("loc_2260")

    label("loc_2076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2126")

    ChrTalk(
        0xFE,
        (
            "Yesterday's stage increased more than ever\x01",
            "He said that it was a workmanship\x01",
            "The theater company manager was also pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the leaders as well\x01",
            "Thank you very much for your satisfaction\x01",
            "It is truly the most important thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2134")
    Jump("loc_2260")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21CF")

    ChrTalk(
        0xFE,
        (
            "Aw, everyone.\x01",
            "Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Iria, if you were,\x01",
            "Now I am theater company chief and Lisa's three\x01",
            "You will come to the stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2260")

    label("loc_21CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21DD")
    Jump("loc_2260")

    label("loc_21DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2260")

    ChrTalk(
        0xFE,
        (
            "Iria and Leisha, if you were,\x01",
            "It should be in the hall now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do not mind,\x01",
            "Please come and see us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2260")

    TalkEnd(0xFE)
    Return()

    # Function_10_15C9 end

    def Function_11_2264(): pass

    label("Function_11_2264")

    Call(0, 12)
    Return()

    # Function_11_2264 end

    def Function_12_2268(): pass

    label("Function_12_2268")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2314")

    ChrTalk(
        0xA,
        (
            "It is still confusing … …\x01",
            "Still slowly contact with each place\x01",
            "I am getting attached to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, first as far as possible\x01",
            "I have to collect information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E3")

    ChrTalk(
        0xA,
        (
            "Immediately after the foundation of the Defense Forces, from the government side\x01",
            "Special performance for citizens\x01",
            "I was asked to hold a meeting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In a situation where casts do not come together\x01",
            "As it is impossible right away,\x01",
            "It got time to get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Then the theater company chief is alone\x01",
            "I wrote the screenplay and everyone\x01",
            "I have practiced until today … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As far as this situation is concerned,\x01",
            "Government-led performances etc.\x01",
            "It will be impossible at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, no matter what shape it takes\x01",
            "We will re-present this\x01",
            "I will definitely make it happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2583")

    label("loc_24E3")


    ChrTalk(
        0xA,
        (
            "As far as this situation is concerned,\x01",
            "Government-led performances etc.\x01",
            "It will be impossible at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, no matter what shape it takes\x01",
            "We will re-present this\x01",
            "I will definitely make it happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2583")

    Jump("loc_2B5D")

    label("loc_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_26F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2669")

    ChrTalk(
        0xA,
        (
            "…… Crossbell now,\x01",
            "It seems to be in an important phase\x01",
            "We have one thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That is, Iria's recovery\x01",
            "Believe and continue practicing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I also do my best,\x01",
            "I will support you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26EE")

    label("loc_2669")


    ChrTalk(
        0xA,
        (
            "There is one thing we need to do.\x01",
            "Believe in recovery of Iria\x01",
            "To continue practicing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I also do my best,\x01",
            "I will support you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EE")

    Jump("loc_2B5D")

    label("loc_26F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_280F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AE")

    ChrTalk(
        0xA,
        (
            "That redhead girl\x01",
            "Who the hell are you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Besides, Mr. Lisha\x01",
            "Where the hell ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyways……\x01",
            "All I do not understand\x01",
            "It is confusing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_280A")

    label("loc_27AE")


    ChrTalk(
        0xA,
        (
            "That redhead girl\x01",
            "Who the hell are you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Besides, Mr. Lisha\x01",
            "Where the hell ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280A")

    Jump("loc_2B5D")

    label("loc_280F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2887")

    ChrTalk(
        0xA,
        (
            "Finally, the renewal performance\x01",
            "The release date came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Anyway, now the success of the stage\x01",
            "I only pray.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2895")
    Jump("loc_2B5D")

    label("loc_2895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28A3")
    Jump("loc_2B5D")

    label("loc_28A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28B1")
    Jump("loc_2B5D")

    label("loc_28B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2954")

    ChrTalk(
        0xA,
        (
            "The date of release is finally over\x01",
            "I came closer to approaching … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Not to mention artists,\x01",
            "All of the other staff including me\x01",
            "I feel that the spirit is rising.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A1E")

    ChrTalk(
        0xA,
        (
            "When I leave here last night\x01",
            "From Royal Highness Claudia\x01",
            "I got a word of direct thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even one staff like me\x01",
            "To bother sending a voice,\x01",
            "It is really a gentle heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A2C")
    Jump("loc_2B5D")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AD1")

    ChrTalk(
        0xA,
        (
            "'Western Zemria Trade Council' … …\x01",
            "It will start from tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "International conferences of this size are\x01",
            "It is very unusual.\x01",
            "Somehow my nervousness will come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5D")

    label("loc_2AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2ADF")
    Jump("loc_2B5D")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2B5D")

    ChrTalk(
        0xA,
        (
            "Everyone, Welcome\x01",
            "To the theater company \"alkane shell\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In theaters\x01",
            "If there is something unknown,\x01",
            "Please do not hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5D")

    TalkEnd(0xA)
    Return()

    # Function_12_2268 end

    def Function_13_2B61(): pass

    label("Function_13_2B61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B72")
    Jump("loc_2EB0")

    label("loc_2B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C75")

    ChrTalk(
        0xFE,
        "Mr. Ilya ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just shave the shri … …\x01",
            "Even if you are injured,\x01",
            "I was delighted with the safety of Sri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Also to the end the stage ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can do it\x01",
            "I would like to do anything …… At such times,\x01",
            "What on earth can we do?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CF8")

    label("loc_2C75")


    ChrTalk(
        0xFE,
        (
            "If we can do it\x01",
            "I would like to do anything …… At such times,\x01",
            "What on earth can we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it …\x01",
            "It is impossible for me to think all the way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF8")

    Jump("loc_2EB0")

    label("loc_2CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D0B")
    Jump("loc_2EB0")

    label("loc_2D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D19")
    Jump("loc_2EB0")

    label("loc_2D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D27")
    Jump("loc_2EB0")

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D35")
    Jump("loc_2EB0")

    label("loc_2D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D50")
    Call(0, 14)
    Jump("loc_2D8E")

    label("loc_2D50")


    ChrTalk(
        0xFE,
        "Uh, something nervous … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It may be more than a stage if it is poor.\x02",
    )

    CloseMessageWindow()

    label("loc_2D8E")

    Jump("loc_2EB0")

    label("loc_2D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DA1")
    Jump("loc_2EB0")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2DAF")
    Jump("loc_2EB0")

    label("loc_2DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DCA")
    Call(0, 15)
    Jump("loc_2E2F")

    label("loc_2DCA")


    ChrTalk(
        0xC,
        (
            "Haa, hey\x01",
            "With intense movements\x01",
            "It's this soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As soon as I can,\x01",
            "Say to Karelia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2F")

    Jump("loc_2EB0")

    label("loc_2E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E42")
    Jump("loc_2EB0")

    label("loc_2E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5D")
    Call(0, 16)
    Jump("loc_2EB0")

    label("loc_2E5D")


    ChrTalk(
        0xC,
        (
            "Herbivorous boys……\x01",
            "Is not it hot or thick character you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huru, it's easy to create a role.\x02",
    )

    CloseMessageWindow()

    label("loc_2EB0")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2ECD")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_2ECD")

    Return()

    # Function_13_2B61 end

    def Function_14_2ECE(): pass

    label("Function_14_2ECE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "Oh, Karelia\x01",
            "I wonder where I sell oil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "No, like this … …\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x87, 0x0)

    ChrTalk(
        0xF,
        (
            "Eugene, a bit\x01",
            "I'd like you to be asked me ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x13B, 0x0)

    ChrTalk(
        0xC,
        "What is it, Mr. Prerie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Chorus, the band of costumes\x01",
            "It got loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I can not be closed by myself.\x01",
            "Help me out\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        "Are you serious?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x16D, 4)
    Return()

    # Function_14_2ECE end

    def Function_15_304C(): pass

    label("Function_15_304C")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "No, but, as usual\x01",
            "My costumes are sinful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This dignified figure ……\x01",
            "I also have a lot of fans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "…… That is fine, Eugene.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "On the shoulder, also the broken thread\x01",
            "You are protruding.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Is it true?\x01",
            "Say to Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hideo, Prince Oda.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_15_304C end

    def Function_16_319A(): pass

    label("Function_16_319A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x136, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348E")

    ChrTalk(
        0xC,
        (
            "However, Nicole's guy also\x01",
            "I feel like I was completely restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, and besides him\x01",
            "We are steadily expanding our strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "If you are not careful, you will be drawn inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huu, you're saying to whom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This \"prince of alkane shell\"\x01",
            "I guess there's no blow easily pulled out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… Recently, in part\x01",
            "A herbivorous boy like Nicole\x01",
            "It seems that it is in fashion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In Roland's story,\x01",
            "Fan letter to Nicole as well\x01",
            "It seems that this place has increased considerably.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Are you serious? Just do it for once ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Huh, I do not know.\x01",
            "Why do not you ask yourself?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "…… Theodore, for her herbivorous men\x01",
            "Please wash the necessary elements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I will master it in a week.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "…… That is not the problem.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x136, 3)

    label("loc_348E")

    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_16_319A end

    def Function_17_34A7(): pass

    label("Function_17_34A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34B8")
    Jump("loc_38BB")

    label("loc_34B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_356F")

    ChrTalk(
        0xFE,
        (
            "Here's the latest, Sri\x01",
            "How to feel like acting\x01",
            "It is exactly like a masterpiece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Prior to technology,\x01",
            "There is a force to take away the heart of the viewer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… We can not be defeated.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BB")

    label("loc_356F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_357D")
    Jump("loc_38BB")

    label("loc_357D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3658")

    ChrTalk(
        0xFE,
        (
            "But … …. Lisha\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There seems to be some sort of obscurity … …\x01",
            "He is a member of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without showing the figure as it is\x01",
            "There is no way it will cease to exist\x01",
            "I want to believe it ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_36CF")

    label("loc_3658")


    ChrTalk(
        0xFE,
        (
            "…… Lisha\x01",
            "What is going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without showing the figure as it is\x01",
            "There is no way it will cease to exist\x01",
            "I want to believe it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CF")

    Jump("loc_38BB")

    label("loc_36D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36E2")
    Jump("loc_38BB")

    label("loc_36E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36F0")
    Jump("loc_38BB")

    label("loc_36F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_36FE")
    Jump("loc_38BB")

    label("loc_36FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_370C")
    Jump("loc_38BB")

    label("loc_370C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_379E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3727")
    Call(0, 18)
    Jump("loc_3799")

    label("loc_3727")


    ChrTalk(
        0xFE,
        (
            "… … The problem of ourselves, after all,\x01",
            "You can only solve it by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Iria, too,\x01",
            "It is honest and frustrating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3799")

    Jump("loc_38BB")

    label("loc_379E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_37AC")
    Jump("loc_38BB")

    label("loc_37AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37BA")
    Jump("loc_38BB")

    label("loc_37BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D5")
    Call(0, 15)
    Jump("loc_381F")

    label("loc_37D5")


    ChrTalk(
        0xFE,
        (
            "…… Well, I'm changing clothes, too\x01",
            "That's it,\x01",
            "Would you head for practice at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_381F")

    Jump("loc_38BB")

    label("loc_3824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3832")
    Jump("loc_38BB")

    label("loc_3832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_38BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384D")
    Call(0, 16)
    Jump("loc_38BB")

    label("loc_384D")


    ChrTalk(
        0xD,
        (
            "It seems like\x01",
            "It sounds like I misplaced it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, this means that this,\x01",
            "Perhaps it was effective.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BB")

    TalkEnd(0xFE)
    Return()

    # Function_17_34A7 end

    def Function_18_38BF(): pass

    label("Function_18_38BF")

    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "Shri's guy ……\x01",
            "It seems to be pretty annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What is missing in my performance,\x01",
            "It seems that I have been thinking for a long time ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Oh … it seems like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, this is Shuri's own problem …\x01",
            "The answer can only be found by himself / herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… Then,\x01",
            "We should keep silent and watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, yeah … it certainly is.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_18_38BF end

    def Function_19_3A18(): pass

    label("Function_19_3A18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A9B")

    ChrTalk(
        0xFE,
        (
            "Listen to Yuria's healthy voice\x01",
            "It was really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all Iria is Iria ~.\x01",
            "We have to work hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F56")

    label("loc_3A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B5B")

    ChrTalk(
        0xFE,
        (
            "Shuri uses the role of the princess alone\x01",
            "Do not defeat the pressure on the back\x01",
            "I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To settle for the stage to Iria\x01",
            "I will give back more than anything ……\x01",
            "I do not put it out, but you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F56")

    label("loc_3B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B69")
    Jump("loc_3F56")

    label("loc_3B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3C50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF4")

    ChrTalk(
        0xFE,
        (
            "As usual practice singing\x01",
            "It's time to … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Haha ………………\x01",
            "I can not feel that way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3C4B")

    label("loc_3BF4")


    ChrTalk(
        0xFE,
        (
            "Ilia like that\x01",
            "It will not be …………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Really, I can not believe it.\x02",
    )

    CloseMessageWindow()

    label("loc_3C4B")

    Jump("loc_3F56")

    label("loc_3C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE3")

    ChrTalk(
        0xFE,
        (
            "Oh, oh, oh.\x01",
            "Uh, today's tone of voice is perfect\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that put a mask up to the actual,\x01",
            "I wonder if I keep my throat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3D22")

    label("loc_3CE3")


    ChrTalk(
        0xFE,
        (
            "Thief is important to Diva ~.\x01",
            "Let's get another throat candy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D22")

    Jump("loc_3F56")

    label("loc_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D35")
    Jump("loc_3F56")

    label("loc_3D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D43")
    Jump("loc_3F56")

    label("loc_3D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3D51")
    Jump("loc_3F56")

    label("loc_3D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6C")
    Call(0, 14)
    Jump("loc_3DCF")

    label("loc_3D6C")


    ChrTalk(
        0xFE,
        (
            "Uhufu, Eugene is yours\x01",
            "It seems like this is surprisingly undoubtedly a spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Somehow my sister will be shy.\x02",
    )

    CloseMessageWindow()

    label("loc_3DCF")

    Jump("loc_3F56")

    label("loc_3DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEF")
    Call(0, 20)
    Jump("loc_3E80")

    label("loc_3DEF")


    ChrTalk(
        0xFE,
        (
            "Well, everyone's super\x01",
            "Because famous people are somehow\x01",
            "I knew it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When that one is settled,\x01",
            "I could not keep track of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E80")

    Jump("loc_3F56")

    label("loc_3E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E93")
    Jump("loc_3F56")

    label("loc_3E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAE")
    Call(0, 21)
    Jump("loc_3EFD")

    label("loc_3EAE")


    ChrTalk(
        0xFE,
        "Well, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Senbei received by Lisha,\x01",
            "Even though it is really delicious ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EFD")

    Jump("loc_3F56")

    label("loc_3F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F10")
    Jump("loc_3F56")

    label("loc_3F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2B")
    Call(0, 22)
    Jump("loc_3F56")

    label("loc_3F2B")


    ChrTalk(
        0xFE,
        (
            "Spacious …\x01",
            "Ahh, you · · · · · ~ ~ a jet\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F56")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3F73")
    OP_93(0xF, 0x87, 0x0)
    OP_93(0xC, 0x13B, 0x0)
    ClearScenarioFlags(0x1, 4)

    label("loc_3F73")

    Return()

    # Function_19_3A18 end

    def Function_20_3F74(): pass

    label("Function_20_3F74")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "…… Yesterday is really\x01",
            "I was overwhelmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "To the Osborne president,\x01",
            "Olivart Prince ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "To Rock Smith President\x01",
            "Grand Duke Albert ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "To His Highness Claudia\x01",
            "Assistant Yulia ……\x01",
            "Then from then …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Huhu, Celine.\x01",
            "I study hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "After all,\x01",
            "Only somehow who's who\x01",
            "I did not know.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "Uu …… Mr. Pree\x01",
            "I am jealous of it.\x02",
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

    # Function_20_3F74 end

    def Function_21_4115(): pass

    label("Function_21_4115")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        (
            "Huh, still the day before … …\x01",
            "I will get nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, this time to fluffy\x01",
            "It is different from just a guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But you've seen it many times\x01",
            "I have overcome hardships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please be more confident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Mr. Karelia ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yes, Celine.\x01",
            "Where I was careful\x01",
            "Because I am just hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "That's right, why do not you eat oats together?\x01",
            "I got it by Lisha\x01",
            "There was a cracker in the east.\x02",
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
            "No, basically this kind of time\x01",
            "Because I do not want to put things in my stomach ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Pree ……\x01",
            "You are really my own pace.\x02",
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

    # Function_21_4115 end

    def Function_22_438C(): pass

    label("Function_22_438C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        (
            "Spacious …\x01",
            "Uof, between rehearsals\x01",
            "Oyatsu is the best ~ spray\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haa ~, Pree san.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Costume Room with sweets\x01",
            "Do not bring it in.\x01",
            "How many times can I tell you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Well, because now it's taking a break?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Because sweets are banned during practice,\x01",
            "If you eat it now is only now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Altogether ….\x01",
            "It really is a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(\"Mysterious Diva\" Preie … …\x01",
            "It is quite a crowd. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Honestly.\x01",
            "It is a great difference from the stage. )\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_22_438C end

    def Function_23_4564(): pass

    label("Function_23_4564")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4614")

    ChrTalk(
        0xFE,
        (
            "Iria's voice ……\x01",
            "I have heard it after a long absence\x01",
            "It looks healthy and was truly the most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know how much it is Taiki,\x01",
            "We have practice only anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C7")

    label("loc_4614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4622")
    Jump("loc_49C7")

    label("loc_4622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4630")
    Jump("loc_49C7")

    label("loc_4630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46BE")

    ChrTalk(
        0xFE,
        (
            "Shuri … … that girl is also ……\x01",
            "…… It is harder than people, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is because of the obstruction of myself … …\x01",
            "I always blamed myself … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49C7")

    label("loc_46BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46CC")
    Jump("loc_49C7")

    label("loc_46CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46DA")
    Jump("loc_49C7")

    label("loc_46DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46E8")
    Jump("loc_49C7")

    label("loc_46E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46F6")
    Jump("loc_49C7")

    label("loc_46F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_474D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4711")
    Call(0, 24)
    Jump("loc_4748")

    label("loc_4711")


    ChrTalk(
        0xFE,
        (
            "I am … I\x01",
            "Is that really the case?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4748")

    Jump("loc_49C7")

    label("loc_474D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_47A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4768")
    Call(0, 20)
    Jump("loc_479D")

    label("loc_4768")


    ChrTalk(
        0xFE,
        (
            "Uu …… Mr. Pree\x01",
            "I am jealous of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479D")

    Jump("loc_49C7")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47B0")
    Jump("loc_49C7")

    label("loc_47B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_482E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47CB")
    Call(0, 21)
    Jump("loc_4829")

    label("loc_47CB")


    ChrTalk(
        0xFE,
        (
            "While watching Mr. Pree,\x01",
            "Why are you so nervous\x01",
            "I do not understand a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4829")

    Jump("loc_49C7")

    label("loc_482E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_483C")
    Jump("loc_49C7")

    label("loc_483C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495B")

    ChrTalk(
        0xFE,
        (
            "Teo seniors and Eugene seniors,\x01",
            "It is really always together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… You sure said that BL?\x01",
            "I also love the fans' imagination ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0xFE,
        (
            "……, I am\x01",
            "I wonder what he is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, while doing this\x01",
            "Without solidifying the image of acting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_49C7")

    label("loc_495B")


    ChrTalk(
        0xFE,
        (
            "Wow, I\x01",
            "I wonder what he is thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, while doing this\x01",
            "Without solidifying the image of acting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C7")

    TalkEnd(0xFE)
    Return()

    # Function_23_4564 end

    def Function_24_49CB(): pass

    label("Function_24_49CB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0x10,
        "Ha\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Nicole even more important cast\x01",
            "I got it, but I …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What are you saying?\x01",
            "Mr. Celine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even you are in this stage\x01",
            "Even the number is on the increase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Still, compared with others ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Already, doing nothing any more\x01",
            "There is nothing to compare with others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You, even in this theater company\x01",
            "Because there is only one existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Here, please smile.\x01",
            "With such face as it is,\x01",
            "I also messed up my make-up.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_24_49CB end

    def Function_25_4BA6(): pass

    label("Function_25_4BA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C2F")

    ChrTalk(
        0xFE,
        (
            "Now Irri's\x01",
            "I am taking care of costumes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To let you pass the sleeve at any time\x01",
            "It is my job to prepare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5287")

    label("loc_4C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4CBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4A")
    Call(0, 26)
    Jump("loc_4CBA")

    label("loc_4C4A")


    ChrTalk(
        0xFE,
        (
            "Huhu, if you think carefully\x01",
            "Mr. Shri is still there\x01",
            "The future is growing season.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm really looking forward to the future.\x02",
    )

    CloseMessageWindow()

    label("loc_4CBA")

    Jump("loc_5287")

    label("loc_4CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CCD")
    Jump("loc_5287")

    label("loc_4CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DAA")

    ChrTalk(
        0xFE,
        (
            "…… About that day,\x01",
            "Just remembering it now is horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Iria's costume,\x01",
            "Painfully painted in blood … ….\x01",
            "I was not able to see it very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uu, Iria … …\x01",
            "Why is it such a thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4E18")

    label("loc_4DAA")


    ChrTalk(
        0xFE,
        (
            "…… About that day,\x01",
            "Just remembering it now is horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uu, Iria … …\x01",
            "Why is it such a thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E18")

    Jump("loc_5287")

    label("loc_4E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4EAC")

    ChrTalk(
        0xFE,
        (
            "Hehe, Mr. Prie really\x01",
            "It is always my own pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Celine, too\x01",
            "It seemed to be fine this morning,\x01",
            "It seems to be able to watch with confidence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5287")

    label("loc_4EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EBA")
    Jump("loc_5287")

    label("loc_4EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4EC8")
    Jump("loc_5287")

    label("loc_4EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4ED6")
    Jump("loc_5287")

    label("loc_4ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF1")
    Call(0, 24)
    Jump("loc_4F70")

    label("loc_4EF1")


    ChrTalk(
        0xFE,
        (
            "Celine, too\x01",
            "It seems like a serious problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking of her feelings\x01",
            "I will feel it is unreasonable ….\x01",
            "I want somehow to recover.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F70")

    Jump("loc_5287")

    label("loc_4F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F90")
    Call(0, 9)
    Jump("loc_5112")

    label("loc_4F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506D")

    ChrTalk(
        0xFE,
        "Er, sorry, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For details of the renewal performance\x01",
            "Not yet an artist other than Mr. Iria\x01",
            "In a situation I did not tell …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, what you saw here is\x01",
            "Please do it for a while for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5112")

    label("loc_506D")


    ChrTalk(
        0xFE,
        (
            "For details of the renewal performance\x01",
            "Not yet an artist other than Mr. Iria\x01",
            "In a situation I did not tell …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, what you saw here is\x01",
            "Please do it for a while for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5112")

    Jump("loc_5287")

    label("loc_5117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5125")
    Jump("loc_5287")

    label("loc_5125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_51E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5140")
    Call(0, 21)
    Jump("loc_51DC")

    label("loc_5140")


    ChrTalk(
        0xFE,
        (
            "Even Iria is,\x01",
            "Mr. Prie is also under pressure\x01",
            "It is an unrelated person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The strength of that heart\x01",
            "Divide it for Mr. Celine as well\x01",
            "I want it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DC")

    Jump("loc_5287")

    label("loc_51E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_51EF")
    Jump("loc_5287")

    label("loc_51EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_520A")
    Call(0, 22)
    Jump("loc_5287")

    label("loc_520A")


    ChrTalk(
        0xFE,
        (
            "Fuu, anyway\x01",
            "Costume matching during the break\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will not stop,\x01",
            "Please eat it soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5287")

    TalkEnd(0xFE)
    Return()

    # Function_25_4BA6 end

    def Function_26_528B(): pass

    label("Function_26_528B")

    OP_4B(0x12, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, Shuri … …\x01",
            "Did your body get bigger again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12205FWell, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, the costume clerk\x01",
            "You can not lick it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A little dressed\x01",
            "It is understood by feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But,\x01",
            "To the extent that you need to make it lengthier\x01",
            "I do not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12202FI see……\x01",
            "Wonderful, Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, if you think carefully\x01",
            "Mr. Shri is still there\x01",
            "The future is growing season.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on eating a cup\x01",
            "Please try hard for practicing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12206FNo……\x01",
            "Thank you, Karelia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(This is the situation … ….\x01",
            "Do something, heartwarming. )\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_553B")

    ChrTalk(
        0x106,
        (
            "#10702F(Hehe, I see.)\x02\x03",
            "#10704F(How do you say, this theater only\x01",
            "I feel like a different world. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_559E")

    label("loc_553B")


    ChrTalk(
        0x102,
        (
            "#00100F(Hehe, indeed.)\x02\x03",
            "#00104F(How do you say, this theater only\x01",
            "I feel like a different world. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_559E")

    SetScenarioFlags(0x1, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x12, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_26_528B end

    def Function_27_55B4(): pass

    label("Function_27_55B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_575F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56E5")

    ChrTalk(
        0xFE,
        (
            "no matter what happens,\x01",
            "Anyway it faces acting with full power … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With that kind of thought,\x01",
            "To anxiety and such feelings\x01",
            "It is not strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I said things that seemed to be great\x01",
            "This is all thanks to Iria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While listening to that person's words,\x01",
            "I feel that the power really rises.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_575A")

    label("loc_56E5")


    ChrTalk(
        0xFE,
        (
            "Iria-san,\x01",
            "It is exactly the sun itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With words alone\x01",
            "I can not get such a strong … …\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_575A")

    Jump("loc_58AB")

    label("loc_575F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_576D")
    Jump("loc_58AB")

    label("loc_576D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_577B")
    Jump("loc_58AB")

    label("loc_577B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5811")

    ChrTalk(
        0xFE,
        (
            "When such time …… Iria\x01",
            "What kind of voice will you call us …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I have to do firmly\x01",
            "I understand … but … but … … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58AB")

    label("loc_5811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_58AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_582C")
    Call(0, 18)
    Jump("loc_58AB")

    label("loc_582C")


    ChrTalk(
        0xFE,
        (
            "Shri's guy,\x01",
            "It seems pretty annoying ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But my own problem,?\x01",
            "…… Theodor senior's words\x01",
            "I have a connotation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58AB")

    TalkEnd(0xFE)
    Return()

    # Function_27_55B4 end

    def Function_28_58AF(): pass

    label("Function_28_58AF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Huhu, like this before opening\x01",
            "It is a reporter's privilege to put in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am also concerned about the mining town,\x01",
            "Today in the interview of the alkane shell\x01",
            "I will concentrate.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_58AF end

    def Function_29_5945(): pass

    label("Function_29_5945")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5963")
    Call(0, 26)
    Jump("loc_5C42")

    label("loc_5963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B1E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A85")
    TurnDirection(0x12, 0x106, 500)

    ChrTalk(
        0x12,
        (
            "#12201FLisa's older sister ……\x01",
            "What is the inrush strategy?\x01",
            "Be careful again.\x02\x03",
            "#12203FI can not do anything,\x01",
            "Just for practice alone\x01",
            "I will try hard so hard ……\x02\x03",
            "#12201FSo Leejia sisters too\x01",
            "Do your best with all your strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702FShri-chan ……\x01",
            "Yes, I understand!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B16")

    label("loc_5A85")


    ChrTalk(
        0x12,
        (
            "#12200FYou are …\x01",
            "What is the inrush strategy?\x01",
            "Be careful again.\x02\x03",
            "Also, about Lisa's older sister\x01",
            "I'm asking for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOh, that's OK.\x02",
    )

    CloseMessageWindow()

    label("loc_5B16")

    SetScenarioFlags(0x1, 3)
    Jump("loc_5C42")

    label("loc_5B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BC5")
    TurnDirection(0x12, 0x106, 500)

    ChrTalk(
        0x12,
        (
            "#12203FI can not do anything,\x01",
            "Just for practice alone\x01",
            "I will try hard so hard ……\x02\x03",
            "#12202FSo Leejia sisters too\x01",
            "Do your best with all your strength.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C42")

    label("loc_5BC5")


    ChrTalk(
        0x12,
        (
            "#12200FYou are …\x01",
            "What is the inrush strategy?\x01",
            "Be careful again.\x02\x03",
            "#12203FAlso, about Lisa's older sister\x01",
            "I'm asking for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C42")

    TalkEnd(0xFE)
    Return()

    # Function_29_5945 end

    def Function_30_5C46(): pass

    label("Function_30_5C46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6305")

    ChrTalk(
        0x13,
        "#01700FOh my brother, you guys.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        (
            "#01700FThen also Tio.\x01",
            "Huh, for quite a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FYes, this is the first time in a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01700FAt last the support department also\x01",
            "It is a full member.\x02\x03",
            "#01704FApparently, everyone\x01",
            "Both one and two times as before\x01",
            "It seems I grew up ….\x02\x03",
            "#01709FWe also alkane shell\x01",
            "I can not lose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHaha, I am honored to say so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHowever, some day today\x01",
            "I feel much more excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01703FWell, whatever.\x01",
            "Next performance before the renewal\x01",
            "It will be the last show.\x02\x03",
            "#01700FAs one culmination,\x01",
            "I wonder if you get nerd and spirit.\x02\x03",
            "#01706FToday, Lisha is on holiday\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_END)), "loc_609A")

    ChrTalk(
        0x109,
        (
            "#10105FBy the way, Mr. Lisha,\x01",
            "I have something to go to the city hall\x01",
            "You said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01705FHmm, did you meet Risha?\x02\x03",
            "#01703FRecently I got fewer … …\x01",
            "When she takes a day off, just before the break\x01",
            "I have declared it several times.\x02\x03",
            "#01709FEvery time, hide\x01",
            "I guess he meets a man as well\x01",
            "I doubt it ~.\x02\x03",
            "#01704FWell, if so\x01",
            "This Iria hand is silent though.\x01",
            "(Exciting)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61D2")

    label("loc_609A")


    ChrTalk(
        0x109,
        "#10100FIs that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01703FYes, recently it has gotten less ….\x01",
            "When she takes a day off, just before the break\x01",
            "I have declared it several times.\x02\x03",
            "#01709FEvery time, hide\x01",
            "I guess he meets a man as well\x01",
            "I doubt it ~.\x02\x03",
            "#01704FWell, if so\x01",
            "This Iria hand is silent though.\x01",
            "(Exciting)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D2")


    ChrTalk(
        0x102,
        "#00105F(Peeping ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, now something's sight for a moment\x01",
            "I feel like I came to my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F(Erie-san … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01700FWell, regardless of Lisha\x01",
            "I have to keep up well today.\x02\x03",
            "#01709FMy younger brother will be busy with you a lot, though\x01",
            "Let's do everything we should do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 5)
    Jump("loc_6393")

    label("loc_6305")


    ChrTalk(
        0x13,
        (
            "#01704FWell, at any rate\x01",
            "I have to keep up well today.\x02\x03",
            "#01700FMy younger brother will be busy with you a lot, though\x01",
            "Let's do everything we should do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6393")

    TalkEnd(0xFE)
    Return()

    # Function_30_5C46 end

    def Function_31_6397(): pass

    label("Function_31_6397")

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
            "#5POh, everyone ….\x01",
            "Please come welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PA kitten suddenly comes in now\x01",
            "At a tremendous speed\x01",
            "Although it ran through, … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah, sorry about that\x02\x03",
            "#00000FActually, we, that kitten\x01",
            "I am following it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FThat……\x01",
            "Is it okay to search inside the theater?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYeah, rather\x01",
            "I will be saved if you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PToday I invited the leaders of the countries at night\x01",
            "I am waiting for the stage … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PJust as the whole artist\x01",
            "Because it was a place to take a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell that's good to hear\x02\x03",
            "Ok then we'll take care of it\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBy the way, kitten\x01",
            "Do you know where you headed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PI'm sorry but I didn't see\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PIt was too amazing momentum\x01",
            "It was a sudden incident\x01",
            "A bit more detailed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PJust run up that stairway\x01",
            "I definitely did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FIndeed …… and when it comes to hands\x01",
            "You seemed better to be searched.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FRight. How should we split up?\x02\x03",
            "#00103FJust because there are three doors\x01",
            "Are you going to split into two people?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00003FGood point\x02",
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
            "#04609FWell, Charlie\x01",
            "I will act with your older brother\x02",
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

    def lambda_6A0F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A0F)
    Sleep(50)

    def lambda_6A1F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6A1F)
    Sleep(50)

    def lambda_6A2F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6A2F)
    Sleep(50)

    def lambda_6A3F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6A3F)
    Sleep(50)

    def lambda_6A4F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6A4F)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x102,
        "#6P#00101FW-wait a minute?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FW-why would it end up like that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04605FJust because?\x02\x03",
            "#04609FOh, perhaps\x01",
            "Your sister together\x01",
            "Did you want to go with your older brother?\x02",
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
        "#6P#00106FN-no not that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FNo problem!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHaha, what?\x01",
            "It is becoming an interesting thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00006FYou guys keep acting like it's not your problem though\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F….. Well, until this point\x01",
            "I do not do fancy good man.\x02\x03",
            "#00301FShirley.\x01",
            "It is strange for Lloyd\x01",
            "Do not multiply it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#04604FYeah yeah, I know\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#04600FMy older brother is cute,\x01",
            "It is different from Charlie's hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FIt's cute …\x01",
            "Well, okay.\x02\x03",
            "#00000FAnyway, organize it\x01",
            "Let's search the theater.\x02\x03",
            "Everyone, if you check it all out\x01",
            "Gather at the entrance.\x02",
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
            "#6P#04602FHuh, then,\x01",
            "Search Marie right away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah of course\x02\x03",
            "#00003F(But when you talk like this\x01",
            "Only for innocent and fickle girls\x01",
            "I can not see it … …)\x02\x03",
            "(A while ago, Dora sons\x01",
            "Threatened thirst was real … …)\x02\x03",
            "#00001F(Who is it?\x01",
            "Is this real child … ….? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A3,
        (
            "#6P#04605FOh, what's wrong?\x02\x03",
            "#04609FPossibly\x01",
            "Have you fallen in love with Charlie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNot at all\x02\x03",
            "#00000FTentatively, 2F\x01",
            "Let's examine the S seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#6P#04609FEheh, yes sir!\x02",
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

    # Function_31_6397 end

    def Function_32_7070(): pass

    label("Function_32_7070")


    def lambda_7075():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7075)

    def lambda_7086():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7086)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 900, 0, -1900, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_32_7070 end

    def Function_33_70BB(): pass

    label("Function_33_70BB")


    def lambda_70C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_70C0)

    def lambda_70D1():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70D1)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -900, 0, -1900, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_33_70BB end

    def Function_34_7106(): pass

    label("Function_34_7106")


    def lambda_710B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_710B)

    def lambda_711C():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_711C)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -900, 0, -4300, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_34_7106 end

    def Function_35_7151(): pass

    label("Function_35_7151")


    def lambda_7156():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7156)

    def lambda_7167():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7167)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 0, -3100, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_35_7151 end

    def Function_36_719C(): pass

    label("Function_36_719C")


    def lambda_71A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_71A1)

    def lambda_71B2():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71B2)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -900, 0, -3100, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_36_719C end

    def Function_37_71E7(): pass

    label("Function_37_71E7")


    def lambda_71EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_71EC)

    def lambda_71FD():
        OP_95(0xFE, 0, 0, -4610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_71FD)
    WaitChrThread(0x1A3, 1)
    OP_95(0x1A3, 800, 0, -4300, 2000, 0x0)
    OP_93(0x1A3, 0x0, 0x1F4)
    Return()

    # Function_37_71E7 end

    def Function_38_7232(): pass

    label("Function_38_7232")


    def lambda_7237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7237)

    def lambda_7248():
        OP_95(0xFE, 50110, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7248)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x1A3, 500)
    Return()

    # Function_38_7232 end

    def Function_39_7269(): pass

    label("Function_39_7269")


    def lambda_726E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_726E)

    def lambda_727F():
        OP_95(0xFE, 48110, 0, 10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_727F)
    Return()

    # Function_39_7269 end

    def Function_40_7295(): pass

    label("Function_40_7295")

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
        "#5P#04605FOh, that girl is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FThat is……\x01",
            "Perhaps Lisha?\x02",
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

    def lambda_7529():
        OP_95(0xFE, 900, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7529)
    Sleep(50)

    def lambda_7546():
        OP_95(0xFE, -800, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7546)
    OP_68(-660, 1450, 2200, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13470, 3000)
    WaitChrThread(0x1A3, 1)

    def lambda_7592():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7592)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5P#00000FIt is Rixia\x02\x03",
            "#00005FAll the artists,\x01",
            "Was not she being taken a break?\x02",
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
            "Oh Lloyd\x02\x03",
            "Uh, yesterday late at night\x01",
            "I had my costume repaired ……\x02\x03",
            "As a final check before actual production\x01",
            "I was doing my costume match.\x02\x03",
            "More than that …\x01",
            "It seems that a kitten has entered?\x02",
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
        "#5P#00001FYeah that's right\x02",
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
            "We, follow the kitten you ran away\x01",
            "I came back here ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    TurnDirection(0x104, 0x15, 500)

    ChrTalk(
        0x104,
        "#12P#00305FOh really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FAt least here\x01",
            "I think that he did not come ….\x02",
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
        "#6P#10300FYo, everyone is there\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00100FI see.\x01",
            "Also, Mr. Lisha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#N#00000FWise to Erie ……\x01",
            "It seems that you do not see it as it seems.\x02",
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
            "#11P#00005FThen, after we lost track of it\x01",
            "Has not anyone seen Mary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThe entrance is still closed\x02\x03",
            "#00100FAs a matter of fact the vicinity of this hall\x01",
            "I wonder if it is doubtful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FHmm, somewhere behind the scenes\x01",
            "There seems to be a possibility of hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FI agree.\x01",
            "Let's all look for it once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FYeah, that sounds good\x02",
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
            "#12P#06202FUh…?\x02\x03",
            "Who is this girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FOhh, this is-\x02",
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#5P#04609FEhehe, you're awesome\x02\x03",
            "#04611FI am aiming for it from a little while ago\x01",
            "There is no gap between Zen Sen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#12P#06205FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F… … That's my,\x01",
            "Unfit cousin#5RItoko#You know.\x02\x03",
            "#00300FDon't worry about her\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11P#06205FRandys…\x02",
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
            "Charlie Orlando!\x01",
            "Please call me Charlie!\x02\x03",
            "No, what about your sister?\x01",
            "I saw it on the stage of the alkane shell.\x02\x03",
            "If you look close in this way\x01",
            "The destructive power is also cocktail ~!\x02\x03",
            "I do not mind.\x01",
            "I'm jealous and envious\x02",
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
        "#12P#06209FUh, that is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00113F…… already I, once,\x01",
            "Because I am injured.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x15, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x1A3,
        (
            "#5P#04609FHaha, that's good.\x01",
            "It is not going to be reduced.\x02\x03",
            "This might be some kind of fate\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x15)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8074():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8074)
    Sleep(50)

    def lambda_8084():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8084)
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

    def lambda_80C9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80C9)
    Sleep(50)

    def lambda_80D9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_80D9)
    Sleep(50)

    def lambda_80E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_80E9)
    Sleep(50)

    def lambda_80F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_80F9)
    Sleep(50)

    def lambda_8109():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8109)
    Sleep(50)

    def lambda_8119():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8119)
    Sleep(50)

    def lambda_8129():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8129)
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

    def lambda_822F():
        OP_95(0xFE, 0, 2500, 18930, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_822F)
    Sleep(1000)

    def lambda_824C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_824C)
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
            "#11P#00011FOh, in such a place\x01",
            "Had it been hiding …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11P#06201FLet's go chase her!\x02",
    )

    CloseMessageWindow()

    def lambda_82F6():

        label("loc_82F6")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_82F6")

    QueueWorkItem2(0x102, 1, lambda_82F6)

    def lambda_8308():

        label("loc_8308")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_8308")

    QueueWorkItem2(0x104, 1, lambda_8308)

    def lambda_831A():

        label("loc_831A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_831A")

    QueueWorkItem2(0x109, 1, lambda_831A)

    def lambda_832C():

        label("loc_832C")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_832C")

    QueueWorkItem2(0x105, 1, lambda_832C)
    OP_95(0x15, 1290, 0, 5610, 4000, 0x0)

    def lambda_8352():
        OP_95(0xFE, 0, 2500, 15240, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8352)
    Sleep(500)

    ChrTalk(
        0x1A3,
        "#11P#04602FMe too!\x02",
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
        "#12P#00306FUgh, seriously\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FEr …\x01",
            "What should I do?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FI'll go follow.\x02\x03",
            "It may also run away,\x01",
            "Everyone wait here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_849D():

        label("loc_849D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_849D")

    QueueWorkItem2(0x102, 1, lambda_849D)
    Sleep(50)

    def lambda_84B2():

        label("loc_84B2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_84B2")

    QueueWorkItem2(0x104, 1, lambda_84B2)
    Sleep(50)

    def lambda_84C7():

        label("loc_84C7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_84C7")

    QueueWorkItem2(0x109, 1, lambda_84C7)
    Sleep(50)

    def lambda_84DC():

        label("loc_84DC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_84DC")

    QueueWorkItem2(0x105, 1, lambda_84DC)
    Sleep(300)

    ChrTalk(
        0x109,
        "#6P#10100FUnderstood\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, this time well\x01",
            "I hope you can catch it.\x02",
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

    # Function_40_7295 end

    def Function_41_85A1(): pass

    label("Function_41_85A1")


    def lambda_85A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_85A6)

    def lambda_85B7():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85B7)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -6510, 2500, 12970, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_41_85A1 end

    def Function_42_85EC(): pass

    label("Function_42_85EC")


    def lambda_85F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_85F1)

    def lambda_8602():
        OP_95(0xFE, -8320, 2500, 14010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8602)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -7770, 2500, 12730, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_42_85EC end

    def Function_43_8637(): pass

    label("Function_43_8637")

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
            "#12P#04600FAhaha, thanks ♪\x01",
            "Your older sister has been rescued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, from me too\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#06209FNo, thank you.\x01",
            "Because the body just moved.\x02\x03",
            "#06204FAnd even if I do not take pride\x01",
            "If she was Mr. Charlie\x01",
            "I think he was helping a kitten.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FR-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04605FHuh? You know huh\x02\x03",
            "#04604FCertainly at that timing\x01",
            "Although I was helped when I jumped in … …\x02\x03",
            "#04609FTentatively, with your sister's jump\x01",
            "Dynamic breast movement\x01",
            "Is it satisfied from being seen?\x02",
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
        "#12P#00306FShirley, you know…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FMy deepest apologies, Rixia\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#06209FAhah\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Well, even so\x01",
            "I'm so sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "To think there was a kitty in here\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "However, without checking, for inspection\x01",
            "Move the device … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04600FWell it's fine\x02\x03",
            "#04604FNo one got hurt \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, so\x01",
            "Please do not mind so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FTentatively …\x01",
            "It is almost time for Mr. Bond\x01",
            "Shall we return?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FYes, still worried\x01",
            "I'm looking for it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0x14,
        "#6PPaternity ♪\x02",
    )

    CloseMessageWindow()

    def lambda_8C4F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C4F)
    Sleep(50)

    def lambda_8C5F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8C5F)
    Sleep(50)

    def lambda_8C6F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8C6F)
    Sleep(50)

    def lambda_8C7F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C7F)
    Sleep(50)

    def lambda_8C8F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C8F)
    Sleep(50)

    def lambda_8C9F():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C9F)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#11P#00309Fmy mother……\x01",
            "It's cash, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FWell, until a while ago\x01",
            "Even though I was frightened by that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#11P#04609FAhaha, that's how cats ar\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F(As this child says\x01",
            "It seems like it is very persuasive … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00000F── Well then,\x01",
            "We, we will excuse it.\x02\x03",
            "Thank you so much for your help\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DEC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8DEC)
    Sleep(50)

    def lambda_8DFC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8DFC)
    Sleep(50)

    def lambda_8E0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8E0C)
    Sleep(50)

    def lambda_8E1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E1C)
    Sleep(50)

    def lambda_8E2C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8E2C)
    Sleep(300)

    ChrTalk(
        0x9,
        "No no, not at all\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#06202FHeh, please take care\x02",
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

    def lambda_8EF3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8EF3)
    WaitChrThread(0x14, 3)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A3, 0x15, 500)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#12P#04605FHey hey, you\x02\x03",
            "#04602FAbout your older sister,\x01",
            "May I call Lisha?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#5P#06205FAh…\x02\x03",
            "#06202F…. Yeah.\x01",
            "Of course not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FHehe, thanks, Rixia\x02\x03",
            "#04600FWell then, laters!\x02",
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
            "#06203F#3243V(Randy's cousin…)\x02\x03",
            "#06201F#3244V(… … that's rumor\x01",
            "Blooded#9RBloody#Shirley \"… …)\x02",
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

    # Function_43_8637 end

    def Function_44_9117(): pass

    label("Function_44_9117")


    def lambda_911C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_911C)
    Sleep(800)

    def lambda_9139():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9139)
    Return()

    # Function_44_9117 end

    def Function_45_9146(): pass

    label("Function_45_9146")


    def lambda_914B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_914B)
    Sleep(1500)

    def lambda_9168():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9168)
    Return()

    # Function_45_9146 end

    def Function_46_9175(): pass

    label("Function_46_9175")


    def lambda_917A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_917A)
    Sleep(2000)

    def lambda_9197():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9197)
    Return()

    # Function_46_9175 end

    def Function_47_91A4(): pass

    label("Function_47_91A4")


    def lambda_91A9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91A9)
    Sleep(500)

    def lambda_91C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_91C6)
    Return()

    # Function_47_91A4 end

    def Function_48_91D3(): pass

    label("Function_48_91D3")

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

    def lambda_92E8():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92E8)

    def lambda_9302():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9302)
    Sleep(50)

    def lambda_9316():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9316)

    def lambda_9330():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9330)
    Sleep(50)

    def lambda_9344():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9344)

    def lambda_935E():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_935E)
    Sleep(50)

    def lambda_9372():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9372)

    def lambda_938C():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_938C)
    Sleep(50)

    def lambda_93A0():
        OP_97(0xFE, 0x0, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_93A0)

    def lambda_93BA():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_93BA)
    Sleep(50)

    def lambda_93CE():
        OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_93CE)

    def lambda_93E8():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93E8)
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
        "Oh, everyone at the Special Affairs Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today is a closed day,\x01",
            "Did you have something for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh my, hey\x01",
            "I just stopped by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FReleasing the renewal stage ……\x01",
            "It approached tomorrow at last.\x02\x03",
            "Today, for that\x01",
            "Is it a holiday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, still only one person\x01",
            "Although some practice it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWell, you are keen.\x01",
            "Could it be …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do you understand?\x01",
            "Yes, she is Sri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway,\x01",
            "Tomorrow is her sunny setting …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently the body is not moving\x01",
            "It looks like I do not feel calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's okay, even in the state of practice\x01",
            "Please look into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs not it good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, always let me get together\x01",
            "If you are a member,\x01",
            "No one complains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently,\x01",
            "From the morning almost without taking a break\x01",
            "He seems to be stuffing roots … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you do not mind,\x01",
            "Please give me a voice as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Also for that girl\x01",
            "I think that it will be a good relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOk, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you very carefully.\x02",
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

    # Function_48_91D3 end

    def Function_49_9890(): pass

    label("Function_49_9890")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -70, 2500, 15340, 180)
    EventEnd(0x5)
    Return()

    # Function_49_9890 end

    def Function_50_98B4(): pass

    label("Function_50_98B4")

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

    def lambda_99AD():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99AD)

    def lambda_99C7():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_99C7)
    Sleep(50)

    def lambda_99DB():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_99DB)

    def lambda_99F5():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_99F5)
    Sleep(500)

    def lambda_9A09():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A09)

    def lambda_9A23():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9A23)
    Sleep(50)

    def lambda_9A37():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A37)

    def lambda_9A51():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9A51)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        (
            "#00005FIs it alkane shell?\x01",
            "It's been a while since I entered the theater.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHehe, that's right.\x01",
            "Iria and Leisha\x01",
            "I wonder if there are any.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, you guys are really\x01",
            "There are many famous acquaintances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWell, is it okay?\x01",
            "I got in arbitrarily … …\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0x101, 500)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9B8D():
        OP_95(0xFE, 0, 0, -500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9B8D)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "This is because the\x01",
            "Is not Ms. Lloyd like Mr. Eli?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's been a while since a long absence.\x01",
            "What kind of work do you need today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, in fact this time the activities of the support department\x01",
            "It is time to resume.\x02\x03",
            "Look around the state of the city,\x01",
            "I will keep my face on here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FDid you trouble you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, of course it's annoying\x01",
            "Not like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Now it's just a break,\x01",
            "Please be greeted by me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I think that Iria's people will be delighted as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000Fthank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112FLet me see………\x02",
    )

    CloseMessageWindow()

    def lambda_9DC0():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DC0)
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#00105FWhat's wrong, Noel?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#12P#10102FNo, what's new\x01",
            "The mission support department is amazing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, that's right.\x01",
            "That alkane shell\x01",
            "It's nothing like a face pass.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00000FHahaha, if you ask me\x01",
            "That's true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYeah, it is a truly appreciated edge.\x02",
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

    # Function_50_98B4 end

    def Function_51_9F3C(): pass

    label("Function_51_9F3C")

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

    def lambda_A063():
        OP_95(0xFE, -600, 0, -2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A063)

    def lambda_A07D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A07D)
    Sleep(100)

    def lambda_A091():
        OP_95(0xFE, 600, 0, -3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A091)

    def lambda_A0AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A0AB)
    Sleep(500)

    def lambda_A0BF():
        OP_95(0xFE, -900, 0, -4000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A0BF)

    def lambda_A0D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A0D9)
    Sleep(100)
    OP_68(-970, 1450, -1300, 3000)
    MoveCamera(44, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15070, 3000)

    def lambda_A11B():
        OP_95(0xFE, 900, 0, -4100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A11B)

    def lambda_A135():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A135)
    Sleep(500)

    def lambda_A149():
        OP_95(0xFE, -500, 0, -5100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A149)

    def lambda_A163():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A163)
    Sleep(100)

    def lambda_A177():
        OP_95(0xFE, 500, 0, -5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A177)

    def lambda_A191():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_A191)
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

    def lambda_A1E6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A1E6)
    Sleep(50)

    def lambda_A1F6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A1F6)
    Sleep(300)

    ChrTalk(
        0xA,
        "#5POh, you are …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAt the Special Affairs Support Division\x01",
            "Is there……!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-270, 1350, 1970, 3000)
    MoveCamera(44, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13600, 3000)

    def lambda_A285():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A285)
    Sleep(50)

    def lambda_A2A2():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2A2)
    Sleep(50)

    def lambda_A2BF():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2BF)
    Sleep(50)

    def lambda_A2DC():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2DC)
    Sleep(50)

    def lambda_A2F9():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A2F9)
    Sleep(50)

    def lambda_A316():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_A316)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00000FWere both of you safe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FPerhaps,\x01",
            "Are other people here too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yes, both staff and artists\x01",
            "Everyone gathers together.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4B9")

    ChrTalk(
        0x9,
        (
            "By the way, now it is new\x01",
            "To practice reconstructed stage\x01",
            "It is a place where I am working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For sudden martial law and curfews\x01",
            "I was puzzled … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As long as I return home,\x01",
            "Whether practicing here or not\x01",
            "We decided to talk with everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A557")

    label("loc_A4B9")


    ChrTalk(
        0x9,
        (
            "By the way, now it is new\x01",
            "To practice reconstructed stage\x01",
            "It is a place where I am working together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Despite this situation,\x01",
            "What we can do is\x01",
            "That's all there is to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A557")


    ChrTalk(
        0x103,
        (
            "#12P#00204FI see……\x01",
            "My head lowers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A822")

    ChrTalk(
        0x106,
        "#12P#10708F…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x106, 500)

    ChrTalk(
        0xA,
        (
            "#5PDid you mean ……\x01",
            "There are\x01",
            "Are you Mr. Lisha?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x106, 500)

    ChrTalk(
        0x9,
        "Mr. Lisha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10706F……long time no see.\x02\x03",
            "#10710FEveryone was safe and than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No … …. Lisha too\x01",
            "You often showed your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are various circumstances\x01",
            "I know, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you like, I will show you how to practice\x01",
            "Could you please go looking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shuri, including you, everyone\x01",
            "Because we are working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10712F#30W………………………….\x02\x03",
            "#10704FI agree……\x02\x01",
            "#10710FIf you are going to peek a little … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        "#5P#00002FLisha …\x02",
    )

    CloseMessageWindow()
    Jump("loc_A8CD")

    label("loc_A822")


    ChrTalk(
        0x9,
        (
            "If you like, I will show you how to practice\x01",
            "Please go and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shuri, including you, everyone\x01",
            "Because we are working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_A8CD")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A92B")
    SetChrPos(0x9, 3940, 0, 2900, 90)
    Jump("loc_A93C")

    label("loc_A92B")

    SetChrPos(0x9, -2250, 2500, 15000, 180)

    label("loc_A93C")

    SetChrPos(0xA, 6970, 0, 3480, 270)
    EventEnd(0x5)
    Return()

    # Function_51_9F3C end

    def Function_52_A950(): pass

    label("Function_52_A950")

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

    def lambda_AA14():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA14)

    def lambda_AA2E():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA2E)
    Sleep(50)

    def lambda_AA42():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA42)

    def lambda_AA5C():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA5C)
    Sleep(50)

    def lambda_AA70():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA70)

    def lambda_AA8A():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AA8A)
    Sleep(50)

    def lambda_AA9E():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AA9E)

    def lambda_AAB8():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AAB8)
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

    def lambda_AB4A():

        label("loc_AB4A")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB4A")

    QueueWorkItem2(0x0, 1, lambda_AB4A)

    def lambda_AB5C():

        label("loc_AB5C")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB5C")

    QueueWorkItem2(0x1, 1, lambda_AB5C)

    def lambda_AB6E():

        label("loc_AB6E")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB6E")

    QueueWorkItem2(0x2, 1, lambda_AB6E)

    def lambda_AB80():

        label("loc_AB80")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AB80")

    QueueWorkItem2(0x3, 1, lambda_AB80)
    OP_95(0x9, 0, 0, -1760, 3000, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0x9,
        (
            "To all of the support department,\x01",
            "Please come welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, sorry.\x01",
            "Now for the afternoon performance\x01",
            "I am preparing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FIs that so,\x01",
            "That was rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FWell I did not have any errands,\x01",
            "Let's start over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHuh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FI'm sorry to disturb you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x137, 0)
    SetScenarioFlags(0x22, 6)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_A950 end

    def Function_53_AD1F(): pass

    label("Function_53_AD1F")

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

    def lambda_AE2F():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE2F)

    def lambda_AE49():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE49)
    Sleep(50)

    def lambda_AE5D():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE5D)

    def lambda_AE77():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AE77)
    Sleep(50)

    def lambda_AE8B():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE8B)

    def lambda_AEA5():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AEA5)
    Sleep(50)

    def lambda_AEB9():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEB9)

    def lambda_AED3():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AED3)
    Sleep(50)

    def lambda_AEE7():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AEE7)

    def lambda_AF01():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF01)
    Sleep(50)

    def lambda_AF15():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF15)

    def lambda_AF2F():
        OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AF2F)
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

    def lambda_AFED():

        label("loc_AFED")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AFED")

    QueueWorkItem2(0x0, 1, lambda_AFED)

    def lambda_AFFF():

        label("loc_AFFF")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_AFFF")

    QueueWorkItem2(0x1, 1, lambda_AFFF)

    def lambda_B011():

        label("loc_B011")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B011")

    QueueWorkItem2(0x2, 1, lambda_B011)

    def lambda_B023():

        label("loc_B023")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B023")

    QueueWorkItem2(0x3, 1, lambda_B023)

    def lambda_B035():

        label("loc_B035")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B035")

    QueueWorkItem2(0x4, 1, lambda_B035)

    def lambda_B047():

        label("loc_B047")

        TurnDirection(0xFE, 0x9, 400)
        Yield()
        Jump("loc_B047")

    QueueWorkItem2(0x5, 1, lambda_B047)
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
            "To all of the support department,\x01",
            "Please come welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, sorry.\x01",
            "Now it's renewal stage\x01",
            "During the final rehearsal ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs that so,\x01",
            "Certainly it is finally time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou should look into it,\x01",
            "I wish this was only …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, within trouble\x01",
            "Let's turn back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FI'm sorry to disturb you.\x02",
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

    # Function_53_AD1F end

    def Function_54_B212(): pass

    label("Function_54_B212")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWell, immediately\x01",
            "I have to chase Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04600FCheck the S seat of 2F.\x01",
            "Well then Let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 48300, 0, -230, 90)
    EventEnd(0x4)
    Return()

    # Function_54_B212 end

    def Function_55_B29C(): pass

    label("Function_55_B29C")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the auditorium on the second floor.\x02\x03",
            "It is annoying if it does not do much.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_55_B29C end

    def Function_56_B315(): pass

    label("Function_56_B315")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the auditorium on the second floor.\x02\x03",
            "It is annoying if it does not do much.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_56_B315 end

    def Function_57_B38E(): pass

    label("Function_57_B38E")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B405")

    ChrTalk(
        0x101,
        (
            "#00000FIt is a story that everyone is practicing.\x02\x03",
            "If you look at the situation, from the front entrance\x01",
            "Enter the stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B467")

    label("loc_B405")


    ChrTalk(
        0x101,
        (
            "#00000F… … Today is Sli\x01",
            "I was practicing alone.\x02\x03",
            "Do not leave the dressing room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B467")

    SetChrPos(0x0, -8200, 0, 4980, 90)
    EventEnd(0x4)
    Return()

    # Function_57_B38E end

    SaveToFile()

Try(main)
