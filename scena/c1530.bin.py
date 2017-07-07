from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1530.bin",                # FileName
        "c1530",                    # MapName
        "c1530",                    # Location
        0x00AE,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 174, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1530",                  # 0
        "Ian lawyer",           # 1
        "Policeman",                   # 2
        "Policeman",                   # 3
        "Pierre deputy director",         # 4
        "Grace",               # 5
        "Raines",               # 6
        "Reporter Noticia",         # 7
        "Reporter Claude",           # 8
        "Reporter Parker",           # 9
        "Empire Times News reporter",           # 10
        "Policeman",                   # 11
        "Policeman",                   # 12
        "Policeman",                   # 13
        "Reporter Thompson",         # 14
        "Tirel correspondence reporter",       # 15
        "Dudley investigator",         # 16
        "Investigator",                 # 17
        "Investigator",                 # 18
        "Grant I.",           # 19
        "Sergeant Giselle",             # 20
        "City official staff",             # 21
        "City official staff",             # 22
        "City official staff",             # 23
        "Lector clerk",         # 24
        "Mayor of Dieter",         # 25
        "Mushroute Scott",         # 26
        "Wrestler Wenzel",     # 27
        "Zookoist Rin",             # 28
        "Friend Aolia",         # 29
        "Sonya Command",           # 30
        "Douglas deputy command",         # 31
        "dummy",                 # 32
        "Chair",                   # 33
        "Chair",                   # 34
        "Chair",                   # 35
        "Chair",                   # 36
        "Dishes",                   # 37
        "A security guard",               # 38
        "A security guard",               # 39
        "A security guard",               # 40
        "A security guard",               # 41
    ))

    AddCharChip((
        "chr/ch05902.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch06400.itc",                   # 02
        "chr/ch06000.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch47900.itc",                   # 05
        "chr/ch27400.itc",                   # 06
        "chr/ch27800.itc",                   # 07
        "chr/ch27900.itc",                   # 08
        "chr/ch27600.itc",                   # 09
        "chr/ch21800.itc",                   # 0A
        "chr/ch47500.itc",                   # 0B
        "chr/ch00900.itc",                   # 0C
        "chr/ch27600.itc",                   # 0D
        "chr/ch27800.itc",                   # 0E
        "chr/ch31300.itc",                   # 0F
        "chr/ch34100.itc",                   # 10
        "chr/ch30002.itc",                   # 11
        "chr/ch25800.itc",                   # 12
        "chr/ch28200.itc",                   # 13
        "chr/ch05900.itc",                   # 14
        "chr/ch12402.itc",                   # 15
        "chr/ch27902.itc",                   # 16
        "chr/ch27802.itc",                   # 17
        "chr/ch06002.itc",                   # 18
        "chr/ch47902.itc",                   # 19
        "chr/ch21802.itc",                   # 1A
        "chr/ch47502.itc",                   # 1B
        "chr/ch06402.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 0,   28,  255,  0)
    DeclNpc(26739,   0,       1529,    180,  389,  0x0, 0,   1,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(266920,  0,       11329,   45,   389,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(336769,  0,       2880,    265,  389,  0x0, 0,   3,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(337769,  0,       2880,    265,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(265570,  0,       2539,    180,  389,  0x0, 0,   1,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(274320,  0,       9760,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(275320,  0,       13649,   89,   389,  0x0, 0,   13,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   14,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(208529,  0,       11590,   135,  389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(209529,  0,       11590,   135,  389,  0x0, 0,   16,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(136970,  0,       4294966046, 45,   389,  0x0, 0,   18,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(137970,  0,       4294966046, 45,   389,  0x0, 0,   19,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(147710,  0,       4294966446, 89,   389,  0x0, 0,   14,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   21,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 67,  34.47999954223633,     -1.190000057220459,    -1.0,                  576.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -5.74666690826416,     0.14875000715255737,   0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  68, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  68, 0x0000)
    DeclActor(4294911506, 0,       3070,    1000,    4294911506, 1500,    3070,    0x007C, 0,  69, 0x0000)
    DeclActor(148500,  0,       11990,   1000,    148500,  1500,    11990,   0x007C, 0,  70, 0x0000)
    DeclActor(148500,  0,       9700,    1000,    148500,  1500,    9700,    0x007C, 0,  70, 0x0000)

    ChipFrameInfo(1976, 0)                                       # 0

    ScpFunction((
        "Function_0_7B8",          # 00, 0
        "Function_1_868",          # 01, 1
        "Function_2_F03",          # 02, 2
        "Function_3_10DF",         # 03, 3
        "Function_4_13A1",         # 04, 4
        "Function_5_176B",         # 05, 5
        "Function_6_1AE1",         # 06, 6
        "Function_7_238C",         # 07, 7
        "Function_8_25C4",         # 08, 8
        "Function_9_2699",         # 09, 9
        "Function_10_27FF",        # 0A, 10
        "Function_11_293E",        # 0B, 11
        "Function_12_2D55",        # 0C, 12
        "Function_13_2F29",        # 0D, 13
        "Function_14_30AB",        # 0E, 14
        "Function_15_32BF",        # 0F, 15
        "Function_16_33FA",        # 10, 16
        "Function_17_390E",        # 11, 17
        "Function_18_3A41",        # 12, 18
        "Function_19_3D6A",        # 13, 19
        "Function_20_3EB1",        # 14, 20
        "Function_21_40E3",        # 15, 21
        "Function_22_4243",        # 16, 22
        "Function_23_42FA",        # 17, 23
        "Function_24_4494",        # 18, 24
        "Function_25_4988",        # 19, 25
        "Function_26_4B31",        # 1A, 26
        "Function_27_4F3A",        # 1B, 27
        "Function_28_549B",        # 1C, 28
        "Function_29_5677",        # 1D, 29
        "Function_30_56A6",        # 1E, 30
        "Function_31_5DDA",        # 1F, 31
        "Function_32_5E39",        # 20, 32
        "Function_33_5E7B",        # 21, 33
        "Function_34_5EBB",        # 22, 34
        "Function_35_691A",        # 23, 35
        "Function_36_6921",        # 24, 36
        "Function_37_694A",        # 25, 37
        "Function_38_6C40",        # 26, 38
        "Function_39_6CB0",        # 27, 39
        "Function_40_6D05",        # 28, 40
        "Function_41_6D95",        # 29, 41
        "Function_42_6DEA",        # 2A, 42
        "Function_43_6E3F",        # 2B, 43
        "Function_44_6E94",        # 2C, 44
        "Function_45_6EE9",        # 2D, 45
        "Function_46_6F3E",        # 2E, 46
        "Function_47_86E2",        # 2F, 47
        "Function_48_872C",        # 30, 48
        "Function_49_877D",        # 31, 49
        "Function_50_87D2",        # 32, 50
        "Function_51_8827",        # 33, 51
        "Function_52_887C",        # 34, 52
        "Function_53_88D1",        # 35, 53
        "Function_54_8926",        # 36, 54
        "Function_55_897B",        # 37, 55
        "Function_56_8C13",        # 38, 56
        "Function_57_8EAB",        # 39, 57
        "Function_58_AEAF",        # 3A, 58
        "Function_59_B41F",        # 3B, 59
        "Function_60_B477",        # 3C, 60
        "Function_61_B4CC",        # 3D, 61
        "Function_62_B506",        # 3E, 62
        "Function_63_B5AA",        # 3F, 63
        "Function_64_B64E",        # 40, 64
        "Function_65_B6F2",        # 41, 65
        "Function_66_B796",        # 42, 66
        "Function_67_C8A5",        # 43, 67
        "Function_68_CC8B",        # 44, 68
        "Function_69_CF7B",        # 45, 69
        "Function_70_D212",        # 46, 70
    ))


    def Function_0_7B8(): pass

    label("Function_0_7B8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7F0"),
        (1, "loc_7FC"),
        (2, "loc_808"),
        (3, "loc_814"),
        (4, "loc_820"),
        (5, "loc_82C"),
        (6, "loc_838"),
        (SWITCH_DEFAULT, "loc_844"),
    )


    label("loc_7F0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_7FC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_808")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_814")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_820")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_82C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_838")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_844")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_850")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_867")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_850")

    label("loc_867")

    Return()

    # Function_0_7B8 end

    def Function_1_868(): pass

    label("Function_1_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_876")
    Jump("loc_E34")

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_911")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 22570, 0, 1190, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 337170, 0, 1160, 89)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 338100, 0, 12950, 270)
    SetChrPos(0x11, 337100, 0, 12950, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x16, 331320, 0, 2060, 90)
    SetChrPos(0x10, 332320, 0, 2060, 270)
    Jump("loc_A1A")

    label("loc_911")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x9, 35270, 0, -1190, 270)
    SetChrPos(0xD, 34300, 0, 420, 135)
    SetChrPos(0x11, 33320, 0, -1250, 90)
    SetChrPos(0x16, 34270, 0, -2590, 45)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xC, 331320, 0, 2060, 90)
    SetChrPos(0x10, 332820, 0, 2060, 270)

    label("loc_99F")

    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0xE, 335410, 150, 4740, 270)
    SetChrPos(0x15, 335610, 150, 6960, 270)
    SetChrChipByIndex(0xE, 0x19)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0x15, 0x1)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 337580, 0, 13090, 0)
    SetChrFlags(0xF, 0x10)

    label("loc_A1A")

    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 275320, 0, 13650, 89)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 275390, 0, 6760, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 266920, 0, 11330, 45)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x17, 206870, 0, 11800, 135)
    SetChrPos(0x1A, 207940, 0, 10900, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9C")
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x1A, 0x10)

    label("loc_A9C")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 208140, 0, 9500, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_B62")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0xC, 142060, 150, 5790, 225)
    SetChrPos(0x8, 140450, 150, 6350, 185)
    SetChrPos(0x1F, 138590, 150, 5700, 125)
    SetChrChipByIndex(0xC, 0x18)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x1F, 0x15)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x1F, 0x10)
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0x1F, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15420, 0, 20630, 90)
    Jump("loc_B9F")

    label("loc_B62")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 140450, 150, 6350, 185)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15420, 0, 20630, 90)

    label("loc_B9F")

    Jump("loc_E34")

    label("loc_BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_E34")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 22570, 0, 1190, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 335770, 0, 2880, 90)
    SetChrPos(0xE, 337270, 0, 2880, 270)
    SetChrPos(0xD, 336790, 0, 830, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 332390, 150, 4870, 90)
    SetChrPos(0x16, 332390, 150, 7060, 90)
    SetChrChipByIndex(0x16, 0x1B)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrChipByIndex(0x15, 0x1A)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrSubChip(0x16, 0x2)
    SetChrSubChip(0x15, 0x1)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 337050, 0, 11080, 90)
    SetChrPos(0x10, 338550, 0, 11080, 270)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 331310, 150, 12280, 180)
    SetChrChipByIndex(0x11, 0x16)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 274320, 0, 9760, 315)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 275320, 0, 13650, 89)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x19, 0x17)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrPos(0x19, 272550, 150, 4750, 270)
    SetChrSubChip(0x19, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x11)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 269050, 0, 10840, 90)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, 265570, 0, 2540, 0)
    SetChrPos(0x13, 265570, 0, 3940, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1A, 208530, 0, 11590, 180)
    SetChrPos(0x1B, 208530, 0, 9990, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 140990, 150, 12360, 180)
    SetChrChipByIndex(0xB, 0x1C)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -15420, 0, 20630, 90)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1C, 136970, 0, -1250, 180)
    SetChrPos(0x1D, 136970, 0, -2550, 0)
    SetChrFlags(0x1C, 0x10)
    SetChrFlags(0x1D, 0x10)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 147710, 0, -850, 89)

    label("loc_E34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E")
    ClearScenarioFlags(0x25, 1)
    Call(0, 35)

    label("loc_E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E72")
    ClearScenarioFlags(0x22, 0)
    Event(0, 37)
    Jump("loc_EBD")

    label("loc_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E86")
    ClearScenarioFlags(0x22, 1)
    Event(0, 46)
    Jump("loc_EBD")

    label("loc_E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E9A")
    ClearScenarioFlags(0x22, 2)
    Event(0, 57)
    Jump("loc_EBD")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EAE")
    ClearScenarioFlags(0x22, 3)
    Event(0, 58)
    Jump("loc_EBD")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_EBD")
    ClearScenarioFlags(0x22, 4)
    Event(0, 66)

    label("loc_EBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDB")
    Event(0, 55)

    label("loc_EDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F02")
    Event(0, 56)

    label("loc_F02")

    Return()

    # Function_1_868 end

    def Function_2_F03(): pass

    label("Function_2_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F18")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2C")
    VolumeBGM(0x46, 0xC8)

    label("loc_F2C")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F44")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_F44")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FCE")
    ClearChrFlags(0x28, 0x80)
    OP_78(0xD, 0x28)
    ClearChrFlags(0x28, 0x40)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xF, 0x2A)
    ClearChrFlags(0x2A, 0x40)
    SetChrPos(0x28, 142300, 0, 6000, 45)
    OP_D5(0x28, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x2A, 138600, 0, 6000, 315)
    OP_D5(0x2A, 0x0, 0x4CE78, 0x0, 0x0)

    label("loc_FCE")

    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100C")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)

    label("loc_100C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_102B")
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_65(0x2, 0x1)

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_105E")
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A3")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_10A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_10DE")

    Return()

    # Function_2_F03 end

    def Function_3_10DF(): pass

    label("Function_3_10DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")

    ChrTalk(
        0xFE,
        (
            "Reporters also entering the upper floor\x01",
            "It seems that he finally gives up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow, but\x01",
            "What do you mean by occupation pattern ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reporter's aggressive action\x01",
            "It is the same in any country.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_121A")

    label("loc_11AC")


    ChrTalk(
        0xFE,
        (
            "Wow, but\x01",
            "What do you mean by occupation pattern ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reporter's aggressive action\x01",
            "It is the same in any country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_139D")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_122D")
    Jump("loc_139D")

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_139D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1312")

    ChrTalk(
        0xFE,
        (
            "This place was invited from each country\x01",
            "It is a waiting room of a press reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In principle during the conference,\x01",
            "The press can not go outside the waiting room\x01",
            "It is a rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because everyone gathers now,\x01",
            "Please go inside and check.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_139D")

    label("loc_1312")


    ChrTalk(
        0xFE,
        (
            "This was invited from each country\x01",
            "It is a waiting room of a press reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In principle during the conference,\x01",
            "The press can not go outside the waiting room\x01",
            "It is a rule.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139D")

    TalkEnd(0xFE)
    Return()

    # Function_3_10DF end

    def Function_4_13A1(): pass

    label("Function_4_13A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_13B5")
    Call(0, 6)
    Jump("loc_1767")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16BF")

    ChrTalk(
        0xC,
        (
            "#02100FOh Lloyd, you guys.\x01",
            "Is it safe for guards?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah, for now.\x02\x03",
            "Graceさんこそ\x01",
            "How was the joint interview?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02102FHehe, that's it ~.\x01",
            "Thanks to you for your achievements.\x02\x03",
            "Anyway, than I thought\x01",
            "I wonder if I can write a positive article?\x02\x03",
            "#02109FAfter that, I will accept the masses a bit more\x01",
            "I hope it is just a story, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FUm, I guess that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FEven more unnecessary places\x01",
            "Please do not look out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02104FAll right, my neighborhood\x01",
            "ちゃんとRaines君にも――\x02\x03",
            "#02101FNot,\x01",
            "I will protect the rules properly.\x02\x03",
            "#02109FThings for your sisters\x01",
            "You do not need to worry about anything?\x02",
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
        "#00006F(Huh, I'm worried … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F(Yes, I'm worried … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 1)
    Jump("loc_1740")

    label("loc_16BF")


    ChrTalk(
        0xC,
        (
            "#02109FIf it's a rule\x01",
            "I will protect it properly so be safe ~.\x02\x03",
            "#02100FWell, once\x01",
            "If you contact the correspondent\x01",
            "I wonder if I will go to the rest room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1740")

    Jump("loc_1767")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1764")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_1764")

    Call(0, 5)

    label("loc_1767")

    TalkEnd(0xFE)
    Return()

    # Function_4_13A1 end

    def Function_5_176B(): pass

    label("Function_5_176B")

    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BD")

    ChrTalk(
        0xC,
        (
            "#02100FSo, Mr. Naials\x01",
            "How about here …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, the interview in the Republic\x01",
            "I feel like I can not take my hand\x01",
            "I could not come quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Now over there is over there,\x01",
            "It seems to be a little bad situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02103FIndeed, that's an example\x01",
            "They are extremist groups of nationalism.\x02\x03",
            "#02101FEven at the trade meeting this time some kind of\x01",
            "I wonder if I can show my movement\x01",
            "I pinched it in my ear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhu, you also to Date\x01",
            "I do not do reporters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Certainly there is such a story.\x01",
            "Although there is no confirmation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F（Graceさんの所にも\x01",
            "Such information … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Anyways,\x01",
            "Do not keep on alarming. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1AD8")

    label("loc_19BD")


    ChrTalk(
        0xC,
        (
            "#02100FThat's right, Noticia.\x01",
            "Next time I see Mr. Naiial\x01",
            "Would you please let me know.\x02\x03",
            "\"Winning of the Füritsa Prize,\x01",
            "congratulations.\x01",
            "I will receive next time. \"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhu, that speaks to you, lady\x01",
            "I was acquainted with Naiaru\x01",
            "It was a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, I will let you know.\x02",
    )

    CloseMessageWindow()

    label("loc_1AD8")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_5_176B end

    def Function_6_1AE1(): pass

    label("Function_6_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB8")

    ChrTalk(
        0x1F,
        (
            "#11505FIndeed, Mr. Beak Bee is\x01",
            "Is it a coffee party?\x02\x03",
            "#11500FYou seem to get along with Prime Minister Shimada.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02200FHmm, is your coffee well well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11503FYeah, it's also gambling with black.\x02\x03",
            "#11502FSo always\x01",
            "Eye glowing like that\x01",
            "I think that it is clear.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#02202FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#02109FHuhu, you can certainly be convinced.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(No, something amazing.\x01",
            "It's a combination. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Yeah ….\x01",
            "It is quite dense. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 2)
    Jump("loc_238B")

    label("loc_1CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2052")

    ChrTalk(
        0xC,
        (
            "#02104FHmm, the Prime Minister Osborne\x01",
            "Coffee party, and … …\x02\x03",
            "#02100FSo, what about Lecter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11510FHmm, if I say somewhat\x01",
            "It is a tea party.\x02\x03",
            "#11500FTaste for secretary of second sister\x01",
            "What will you do after listening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FWell, quite\x01",
            "I have a sweet mask\x01",
            "I thought about keeping it in the brim.\x02\x03",
            "#02102FAnyway, beautiful beauty boy\x01",
            "Because it will be the flower of the article alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11509FHaha, I see.\x01",
            "You will be happy to say something.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_END)), "loc_1F61")

    ChrTalk(
        0x101,
        (
            "#00006F(Well, obviously\x01",
            "I feel like conversation on the upper side. )\x02\x03",
            "#00001F（Graceさんも\x01",
            "To some extent Mr. Lector\x01",
            "It seemed like I was grasping … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Fuh, mixed with falsehood\x01",
            "Is it a place to compare? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204A")

    label("loc_1F61")


    ChrTalk(
        0x101,
        (
            "#00006F(Well, obviously\x01",
            "I feel like conversation on the upper side. )\x02\x03",
            "#00001F（Graceさんもレクターさんが\x01",
            "It is not just a clerk\x01",
            "You will know … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Fuh, mixed with falsehood\x01",
            "Is it a place to compare? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204A")

    SetScenarioFlags(0x1C1, 3)
    Jump("loc_238B")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B3")

    ChrTalk(
        0x1F,
        (
            "#11501FOh yes, Mr. Beak Beard,\x01",
            "Actually, I would like to talk to the teacher\x01",
            "I have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02205FHmm, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11506FNo, actually, hey\x01",
            "I was troubled by the workplace.\x02\x03",
            "Famous for human rights issues\x01",
            "Once the view of Mr. Bear Beard\x01",
            "I thought that I would like to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02202FIs that so……\x01",
            "Well it is impossible now to fluff.\x02\x03",
            "If it's okay again please\x01",
            "Please contact the office.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ian lawyerはLector clerkに\x01",
            "I offered my business card.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        "#11509FOh, it helps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Indeed, doing this\x01",
            "You are broadening your network. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Well, this kind of extroversion\x01",
            "It is necessary for intelligence agents\x01",
            "It is a skill. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 4)
    Jump("loc_238B")

    label("loc_22B3")


    ChrTalk(
        0x1F,
        "#11500FSo, Mr. Beak Bee … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02202FYeah, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#02100FHmm, he is … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(… … Three conversations all the time\x01",
            "I can not afford to listen. )\x02\x03",
            "(more than this,\x01",
            "Let's stop stepping on. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238B")

    Return()

    # Function_6_1AE1 end

    def Function_7_238C(): pass

    label("Function_7_238C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2415")

    ChrTalk(
        0xFE,
        (
            "Well, after all it's on the VIP floor\x01",
            "It was unreasonable to infiltrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Senpai anyway,\x01",
            "Where did he go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C0")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2423")
    Jump("loc_25C0")

    label("loc_2423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_25C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2442")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2528")

    ChrTalk(
        0xFE,
        (
            "Libert communication genius cameraman,\x01",
            "Dorothy · Hyatt ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is her picture taken?\x01",
            "Being very lively\x01",
            "It attracts viewers, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Talk as a photographer by all means\x01",
            "I wanted to ask you ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_25C0")

    label("loc_2528")


    ChrTalk(
        0xFE,
        (
            "Well, next time to Libert\x01",
            "Even when I go on a trip\x01",
            "I wonder if I will visit a telecommunications company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From Rouen to the Kingdom\x01",
            "Not too much time\x01",
            "It should have not taken. …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_238C end

    def Function_8_25C4(): pass

    label("Function_8_25C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2673")

    ChrTalk(
        0xFE,
        (
            "Well, aside from the speculation of both countries\x01",
            "The outcome of the first half of the meeting\x01",
            "That is something to please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The activation of the continental economy,\x01",
            "For Libert and Remiferia\x01",
            "It's a positive story.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2695")

    label("loc_2673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2692")

    Call(0, 5)

    label("loc_2695")

    TalkEnd(0xFE)
    Return()

    # Function_8_25C4 end

    def Function_9_2699(): pass

    label("Function_9_2699")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2737")

    ChrTalk(
        0xFE,
        (
            "Hmm, the two great countries so far\x01",
            "I do not want to compromise the autonomous province's proposal\x01",
            "It is really rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Certainly the interest of the autonomous state\x01",
            "It is directly connected to the interests of two major countries, but …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27FB")

    label("loc_2737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_27FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2752")
    Call(0, 10)
    Jump("loc_27FB")

    label("loc_2752")


    ChrTalk(
        0xFE,
        (
            "However, this Orkis Tower\x01",
            "It is totally ridiculous building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remiferia is impossible for fluffy,\x01",
            "If you are from the city of Altair also in the Republic\x01",
            "You can see it perfectly?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FB")

    TalkEnd(0xFE)
    Return()

    # Function_9_2699 end

    def Function_10_27FF(): pass

    label("Function_10_27FF")


    ChrTalk(
        0x15,
        (
            "Revised, Ardent Press's\x01",
            "I say Thompson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You are tyrell communication\x01",
            "You are a photographer, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Yeah, I'm still a weak.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "As for Ardent,\x01",
            "You're a remifriya, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "No competition if the country is different -\x01",
            "I'd like a joint fight today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, that's right.\x01",
            "Nice to meet you, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_10_27FF end

    def Function_11_293E(): pass

    label("Function_11_293E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A05")

    ChrTalk(
        0xFE,
        (
            "Organization of the first half of the meeting as well\x01",
            "Have you finally calmed down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, from the second half\x01",
            "About the contents thrust further\x01",
            "Discussions should be made ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The actual number is still to come.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A73")

    label("loc_2A05")


    ChrTalk(
        0xFE,
        (
            "From the second half of the meeting\x01",
            "About the contents thrust further\x01",
            "Discussions should be made ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The actual number is still to come.\x02",
    )

    CloseMessageWindow()

    label("loc_2A73")

    Jump("loc_2D51")

    label("loc_2A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C07")
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's right, about that matter\x01",
            "It is said that agreement of each country was obtained … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Then report to the head office with its contents …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Someone with Enigma\x01",
            "It seems they are communicating. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Perhaps outside the tower\x01",
            "You probably have a reporter group. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Huh, even as soon as one minute or so\x01",
            "Information on trade council, … ….)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(What kind of work did you have trouble with?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2C88")

    label("loc_2C07")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's right, about that matter\x01",
            "It is said that agreement of each country was obtained … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Then report to the head office with its contents …\x02",
    )

    CloseMessageWindow()

    label("loc_2C88")

    Jump("loc_2D51")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA8")
    Call(0, 12)
    Jump("loc_2D51")

    label("loc_2CA8")


    ChrTalk(
        0xFE,
        (
            "Huff, if you say that\x01",
            "Rock Smith is the same as president, is not he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Seeing is believing -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From articles on Tirel communication usually\x01",
            "Beyond the impression you receive,\x01",
            "I felt a dignified style.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D51")

    TalkEnd(0xFE)
    Return()

    # Function_11_293E end

    def Function_12_2D55(): pass

    label("Function_12_2D55")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        (
            "Well ~, even so\x01",
            "Everything is about this upcoming meeting\x01",
            "It is out of the standard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There are a number of bilateral meetings,\x01",
            "Autonomous state and the four neighboring countries this time …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Moreover, with the Osborne president\x01",
            "President Rock Smith\x01",
            "Let's face it directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Whatever you say to that\x01",
            "Two people actually took a look\x01",
            "This is my first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Indeed, today,\x01",
            "It will be a historic day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Yeah, it's totally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Beginning of your Empire Times\x01",
            "Reporters from all over the world trampled -\x01",
            "I'm enthusiastic about coverage as well!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_12_2D55 end

    def Function_13_2F29(): pass

    label("Function_13_2F29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2FC7")

    ChrTalk(
        0xFE,
        (
            "Interview of the VIP floor\x01",
            "I regret that I could not do it ….\x01",
            "I still have a chance to interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An outline of the reporter question\x01",
            "I have to review it again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A7")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2FD5")
    Jump("loc_30A7")

    label("loc_2FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_30A7")

    ChrTalk(
        0xFE,
        (
            "Crossbell Police on various occasions\x01",
            "It tends to be evaluated as often incompetent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As far as security in the building is concerned,\x01",
            "I receive the impression that it is an outstanding excellent organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The problem is not the person but the structure of the autonomous state ……\x01",
            "It makes me feel strongly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A7")

    TalkEnd(0xFE)
    Return()

    # Function_13_2F29 end

    def Function_14_30AB(): pass

    label("Function_14_30AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_312A")

    ChrTalk(
        0xFE,
        (
            "Well, during that time\x01",
            "The break time is over, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Towards the second half of the meeting\x01",
            "I have to get ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BB")

    label("loc_312A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3222")

    ChrTalk(
        0xFE,
        (
            "Regarding economic-related agreements,\x01",
            "It can be said that striking results have come out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Around this point, the proposer to the flukes\x01",
            "It is also concurrently appointed IBC president\x01",
            "Mayor of Dieterなだけはある。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Economic development encourages continental stability …\x01",
            "I feel like I am not a dreamlike story.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BB")

    label("loc_3222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_32BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323D")
    Call(0, 12)
    Jump("loc_32BB")

    label("loc_323D")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "The power of Prime Minister Osborne is real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wake is different from looking at the picture.\x01",
            "It is a feeling that points of intervention went to various things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BB")

    TalkEnd(0xFE)
    Return()

    # Function_14_30AB end

    def Function_15_32BF(): pass

    label("Function_15_32BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3315")

    ChrTalk(
        0xFE,
        (
            "The break time is about to end …\x01",
            "I wonder if I will buy some drinks in the morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F6")

    label("loc_3315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3323")
    Jump("loc_33F6")

    label("loc_3323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_33F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333E")
    Call(0, 10)
    Jump("loc_33F6")

    label("loc_333E")


    ChrTalk(
        0xFE,
        (
            "Yeah, If the weather is nice\x01",
            "It's already clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to Altair City\x01",
            "The number of tourists visiting is slightly\x01",
            "I say that it increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The economic effect of this tower\x01",
            "There are tremendous things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F6")

    TalkEnd(0xFE)
    Return()

    # Function_15_32BF end

    def Function_16_33FA(): pass

    label("Function_16_33FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_34B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3418")
    Call(0, 17)
    Jump("loc_34AE")

    label("loc_3418")


    ChrTalk(
        0x17,
        (
            "#00600FOh, you guys.\x02\x03",
            "Although there is still time,\x01",
            "To the two leaders as soon as possible\x01",
            "Try to head over.\x02\x03",
            "Naturally, not much\x01",
            "I can not let you wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34AE")

    Jump("loc_390A")

    label("loc_34B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_390A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387E")

    ChrTalk(
        0x17,
        (
            "#00600FYou guys.\x02\x03",
            "Is there something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWith this monitor security of the whole\x01",
            "It is a bird's-eye view of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603FOh, of course the conference hall\x01",
            "Key points of Oskistower are\x01",
            "It can be confirmed in real time.\x02\x03",
            "#00600FBuilt in this building,\x01",
            "It is the latest security camera system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FSecurity cameras … Started IBC\x01",
            "Even in an oval store etc.\x01",
            "It is a technology that is being operated.\x02\x03",
            "#00200FAlthough this is\x01",
            "It seems that the number is orders of magnitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FI have said it,\x01",
            "What technology you care a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, either outside the city\x01",
            "You have been monitored like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, that neighborhood understands citizens\x01",
            "I feel that it will be subtle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603F…… Anyway, what is available\x01",
            "Just use it to the utmost.\x02\x03",
            "#00601FAs we can not grasp the trend of terrorists,\x01",
            "Just before the guys take action,\x01",
            "Or just hit it.\x02\x03",
            "For that, any trivial information\x01",
            "You can not overlook it.\x02\x03",
            "If there is something, please contact me soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 5)
    Call(0, 36)
    Jump("loc_390A")

    label("loc_387E")


    ChrTalk(
        0x17,
        (
            "#00603FI always keep in touch with every aspect,\x01",
            "Still no noticeable problem has not yet occurred.\x02\x03",
            "#00600FYou will continue,\x01",
            "Continue vigilance on the floor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390A")

    TalkEnd(0xFE)
    Return()

    # Function_16_33FA end

    def Function_17_390E(): pass

    label("Function_17_390E")

    OP_4B(0x17, 0xFF)
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0x17,
        (
            "#00600FGrant I.、現在の\x01",
            "How is the status of the company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Of course, everyone is feeling tension\x01",
            "I keep on keeping it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Every time at any time\x01",
            "It is our duty to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603FIndeed, it is encouraging.\x02\x03",
            "#00601FIn the latter part of the meeting\x01",
            "Policeman隊の配備についてですが――\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    OP_4C(0x1A, 0xFF)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x1A, 0x10)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_17_390E end

    def Function_18_3A41(): pass

    label("Function_18_3A41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3BBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B29")

    ChrTalk(
        0xFE,
        (
            "For both city and city,\x01",
            "Current situation No particular incident has been confirmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to the report of the surveillance team,\x01",
            "\"Red constellation\" and \"black moon\" as well\x01",
            "It is said that there is no sign of movement yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You say the calm before the storm … ….\x01",
            "To be honest, it is spooky and can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3BBA")

    label("loc_3B29")


    ChrTalk(
        0xFE,
        (
            "According to the report of the surveillance team,\x01",
            "\"Red constellation\" and \"black moon\" as well\x01",
            "It is said that there is no sign of movement yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You say the calm before the storm … ….\x01",
            "To be honest, it is spooky and can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BBA")

    Jump("loc_3D66")

    label("loc_3BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3D66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC0")

    ChrTalk(
        0xFE,
        (
            "In this security office room,\x01",
            "Information of each direction instantly concentrates\x01",
            "The system is in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The guiding terminal here is\x01",
            "It is limited, but the police headquarters\x01",
            "It is also connected to the database.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If necessary,\x01",
            "Inquiries of suspicious persons etc.\x01",
            "You can do it in this place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3D66")

    label("loc_3CC0")


    ChrTalk(
        0xFE,
        (
            "The reason why the system so far was prepared\x01",
            "Mayor of Dieterの全面協力が\x01",
            "It is because there was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The security system of this time is exactly\x01",
            "The total force of this crossbell …\x01",
            "That is why failures are forgiven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D66")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A41 end

    def Function_19_3D6A(): pass

    label("Function_19_3D6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3E01")

    ChrTalk(
        0xFE,
        (
            "As long as I keep on warning activity\x01",
            "I have not got any information yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where the terrorists are\x01",
            "Is it that they are latent?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAD")

    label("loc_3E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3EAD")

    ChrTalk(
        0xFE,
        (
            "Terrorists are still in one direction\x01",
            "I will not even grab that sign.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Plan this thoroughly before planning\x01",
            "I hope I gave up … but,\x01",
            "I can not really be optimistic.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x19, 0x2)
    Return()

    label("loc_3EAD")

    TalkEnd(0xFE)
    Return()

    # Function_19_3D6A end

    def Function_20_3EB1(): pass

    label("Function_20_3EB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA9")

    ChrTalk(
        0xFE,
        (
            "During a break or during a meeting,\x01",
            "Our watchful activities will not loosen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this perfect system,\x01",
            "Where are the terrorists\x01",
            "Are you going to pierce me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are several assumed patterns,\x01",
            "If things happen it will not move accordingly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4042")

    label("loc_3FA9")


    ChrTalk(
        0xFE,
        (
            "In this perfect system,\x01",
            "Where are the terrorists\x01",
            "Are you going to pierce me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are several assumed patterns,\x01",
            "If things happen it will not move accordingly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4042")

    Jump("loc_40DF")

    label("loc_4047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_40DF")

    ChrTalk(
        0xFE,
        (
            "While watching the monitor in this way,\x01",
            "Everyone is seriously wary of it\x01",
            "It comes down to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it a terrorist …?\x01",
            "I will not care for it if I do not care about it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_40DF")

    TalkEnd(0xFE)
    Return()

    # Function_20_3EB1 end

    def Function_21_40E3(): pass

    label("Function_21_40E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B8")

    ChrTalk(
        0xFE,
        (
            "The security of the Orkis Tower,\x01",
            "We are the people of the security department\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We always prepare for emergency\x01",
            "It is a battle school who is trained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it is time to watch the guard\x01",
            "I have confidence that I will not be late.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_423F")

    label("loc_41B8")


    ChrTalk(
        0xFE,
        (
            "We human beings in the security department\x01",
            "I always train for emergency\x01",
            "It is a battle school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it is time to watch the guard\x01",
            "I have confidence that I will not be late.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_423F")

    TalkEnd(0xFE)
    Return()

    # Function_21_40E3 end

    def Function_22_4243(): pass

    label("Function_22_4243")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We are usually related to government\x01",
            "Importance of important facilities and various important people\x01",
            "I'm in charge of security and others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even during the anniversary festival,\x01",
            "Security of international events like these\x01",
            "It 's one of the most important tasks.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_4243 end

    def Function_23_42FA(): pass

    label("Function_23_42FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_43F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4318")
    Call(0, 17)
    Jump("loc_43EB")

    label("loc_4318")


    ChrTalk(
        0xFE,
        (
            "Hmm, if you like this\x01",
            "If it does not appear in the break time,\x01",
            "Is the remaining mountain range later in the meeting and later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yet\x01",
            "It can not be helped if you think too much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway,\x01",
            "At that time then\x01",
            "I just prepare to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43EB")

    Jump("loc_4490")

    label("loc_43F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4490")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440B")
    Call(0, 24)
    Jump("loc_4490")

    label("loc_440B")


    ChrTalk(
        0xFE,
        (
            "But, it does not matter\x01",
            "Do not leave this room as two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it …?\x01",
            "What is Orkistower?\x01",
            "Everything is orders of magnitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4490")

    TalkEnd(0xFE)
    Return()

    # Function_23_42FA end

    def Function_24_4494(): pass

    label("Function_24_4494")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    TurnDirection(0x1B, 0x0, 500)

    ChrTalk(
        0x109,
        "#10100FGrant I.、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FThank you, cheers for good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Sergeant Sergeant Orlando?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I am sorry.\x01",
            "Now both are the guards\x01",
            "I did not belong to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FNo, it is definitely on loan\x01",
            "It's fine as it's easy to call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHaha, I'm good anything else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThis is……\x01",
            "Are you two alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Yes, the leaders of each country and the reporters\x01",
            "I have a front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Exposure of the guard as much as possible\x01",
            "From the judgment that it should be avoided,\x01",
            "It is minimal deployment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FThat means … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes, it is consideration to the two major powers.\x02\x03",
            "According to the autonomous state law\x01",
            "Although the armaments are restricted\x01",
            "An institution equivalent to the so-called military ……\x02\x03",
            "Although within the limits,\x01",
            "To maintain troops and to expand equipment\x01",
            "I use a large budget.\x02\x03",
            "#10108FSo, like this\x01",
            "It is easy to be cited as a spear in the meeting place\x01",
            "It is one of the agenda items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see……\x01",
            "So try not to get into your eyes as much as possible\x01",
            "Is not it striving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, diplomacy is\x01",
            "It is really troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well it certainly is,\x01",
            "Do not say so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Besides, this is for the last\x01",
            "It is a story of appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Instead, on the floor directly below\x01",
            "One unit can be dispatched at any time\x01",
            "I am waiting in the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "In case of emergency, immediately\x01",
            "You do not have to worry because it hits things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FIndeed, it is consent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FWhen it comes to emergency, please.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x1C1, 6)
    Call(0, 36)
    Return()

    # Function_24_4494 end

    def Function_25_4988(): pass

    label("Function_25_4988")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4A1B")

    ChrTalk(
        0xFE,
        (
            "Half of the meeting ended,\x01",
            "Apparently there seems to be no change in the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The movement of terrorists\x01",
            "It is somewhere I want to sense beforehand … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2D")

    label("loc_4A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A36")
    Call(0, 24)
    Jump("loc_4B2D")

    label("loc_4A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC9")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Sergeant Noel, today's mutual\x01",
            "Let's do what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I leave the floor's vigilance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FOk, got it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4B2D")

    label("loc_4AC9")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Sergeant Noel, today's mutual\x01",
            "Let's do what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I leave the floor's vigilance.\x02",
    )

    CloseMessageWindow()

    label("loc_4B2D")

    TalkEnd(0xFE)
    Return()

    # Function_25_4988 end

    def Function_26_4B31(): pass

    label("Function_26_4B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4B42")
    Jump("loc_4F36")

    label("loc_4B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B5D")
    Call(0, 27)
    Jump("loc_4F36")

    label("loc_4B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E5D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BF8")
    Jump("loc_4C42")

    label("loc_4BF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C18")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C42")

    label("loc_4C18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C38")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C42")

    label("loc_4C38")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C42")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0x101,
        (
            "#00001FBy the way, deputy director,\x01",
            "I mentioned earlier\x01",
            "Is it meant …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, I was curious.\x01",
            "Is it even information on a suspicious person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm? How is my house?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "Well, to you\x01",
            "It will be an irrelevant story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please return to your duties as soon as possible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FOk, yes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(No way, my wife's thing\x01",
            "Did you think about it? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(I was surely a godfather.\x01",
            "… … There are various things. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Well ….\x01",
            "Let's leave it gently. )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1C2, 0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_4F36")

    label("loc_4E5D")

    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        "Nearby, everyone this guy ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Even I, I …\x02",
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

    label("loc_4F36")

    TalkEnd(0xFE)
    Return()

    # Function_26_4B31 end

    def Function_27_4F3A(): pass

    label("Function_27_4F3A")

    EventBegin(0x0)
    Fade(500)
    OP_68(142170, 1500, 10600, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 142170, 0, 10600, 315)
    SetChrPos(0x102, 144770, 0, 10800, 270)
    SetChrPos(0x104, 143580, 0, 11190, 270)
    SetChrPos(0x103, 143590, 0, 10390, 315)
    SetChrPos(0x109, 143190, 0, 9390, 315)
    SetChrPos(0x105, 145000, 0, 9790, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "Mumuu, it's nothing ……\x01",
            "No, such a thing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005F(A, who is it … ….?\x02\x03",
            "#00000Fえっと、Pierre deputy director？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Ha ha! Is it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        "However, if you think that someone is a Special Affairs Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is something to do with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FUmm, what is this deputy director here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FHey, Tio -\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "No matter what you are doing … nothing ….\x01",
            "I am the director of the security office room!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305FOh, was that so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSpeaking of which,\x01",
            "I think the name was written.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F…… I see, it was a lack of study.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Kimi, you … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, it was late ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FIn advance\x01",
            "You should have taught me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FWell, indeed …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, but that director\x01",
            "Why do not you face the countermeasure room?\x02\x03",
            "I do not see any intermission break, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Funfu …… Command site command authority\x01",
            "Everything is left to Dadley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In such a situation I\x01",
            "On the way back, instead\x01",
            "It will be hard to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I do not care what you think … …\x01",
            "In that respect, I am the boss who I could refuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And anyway … you guys.\x01",
            "Repeat Dudley's feet\x01",
            "It began to be pulled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FRyo, OK.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C1, 7)
    Call(0, 36)
    EventEnd(0x5)
    Return()

    # Function_27_4F3A end

    def Function_28_549B(): pass

    label("Function_28_549B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_54AF")
    Call(0, 6)
    Jump("loc_5673")

    label("loc_54AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_566A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CF")

    ChrTalk(
        0x8,
        (
            "#02203FHmm, how is it going?\x01",
            "They are called to the two leaders.\x02\x03",
            "#02200FNaturally it will get nervous … …\x01",
            "Such opportunities rarely happen.\x02\x03",
            "Just by getting the two aura up close\x01",
            "I think it will be a pretty good study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThen, the teacher, I'll be back.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5665")

    label("loc_55CF")


    ChrTalk(
        0x8,
        (
            "#02200FI also felt at the meeting,\x01",
            "Just by getting the two aura up close\x01",
            "It should be a pretty good study.\x02\x03",
            "Without thinking about extra things,\x01",
            "You should hit anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5665")

    Jump("loc_5673")

    label("loc_566A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5673")

    label("loc_5673")

    TalkEnd(0xFE)
    Return()

    # Function_28_549B end

    def Function_29_5677(): pass

    label("Function_29_5677")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_568B")
    Call(0, 6)
    Jump("loc_56A2")

    label("loc_568B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5699")
    Jump("loc_56A2")

    label("loc_5699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_56A2")

    label("loc_56A2")

    TalkEnd(0xFE)
    Return()

    # Function_29_5677 end

    def Function_30_56A6(): pass

    label("Function_30_56A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5731")

    ChrTalk(
        0xFE,
        (
            "I do not know well … ….\x01",
            "Mr. Ian, oddly\x01",
            "Some people with aura are gathering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel an atmosphere that is nothing short of.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD6")

    label("loc_5731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_57B9")

    ChrTalk(
        0xFE,
        (
            "そういえば、Pierre deputy directorは\x01",
            "Where did it go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not readily come back,\x01",
            "Did he even go to the headquarters?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DD6")

    label("loc_57B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_583F")

    ChrTalk(
        0xFE,
        (
            "Pierre deputy director、\x01",
            "Something was murmured earlier\x01",
            "Although it seems to be saying, I wonder if it is OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… It can not help being worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD6")

    label("loc_583F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5E")

    ChrTalk(
        0xFE,
        (
            "君たち、どうやらPierre deputy directorと\x01",
            "It seems they were talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Does your condition seem to be OK?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhether or not to say that is okay\x01",
            "It's a difficult problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, if you say it as usual\x01",
            "It was as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FBut before that, over there\x01",
            "It was not a subservient person\x01",
            "I am afraid … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, it is sublime ……\x01",
            "Well, I guess it can not be helped either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, to my place\x01",
            "A person with a deputy director's title\x01",
            "I have two people … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Receiving the dismissal of the former director\x01",
            "I was appointed a new director\x01",
            "It was the other deputy director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIt certainly was.\x02\x03",
            "With us\x01",
            "There is no point of contact at all, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, that new director … …\x01",
            "実はPierre deputy directorの\x01",
            "Do you know that he is a junior?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FNew director-general … … the deputy director's junior?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nonetheless, Mr. Pierre\x01",
            "The director is not quite what I am\x01",
            "I can not imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clearly\x01",
            "I think that it is reasonable personnel … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, the same deputy director … …\x01",
            "Besides, the career is under the human\x01",
            "I can endure it if she is pulled out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FJuff, indeed\x01",
            "That would be a natural feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's why\x01",
            "That person is also seriously tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, you guys and that guy\x01",
            "Would you like to expand your mind when you touch it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you say a small saying,\x01",
            "To the contrary I care\x01",
            "I hope it makes me feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FThat's right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C2, 1)
    Jump("loc_5DD6")

    label("loc_5D5E")


    ChrTalk(
        0xFE,
        (
            "Pierre deputy directorも、\x01",
            "It looks awful and has various difficulties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am a nifty person,\x01",
            "I have to put up with this as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD6")

    TalkEnd(0xFE)
    Return()

    # Function_30_56A6 end

    def Function_31_5DDA(): pass

    label("Function_31_5DDA")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Well, the first half of the meeting\x01",
            "As soon as it is a press conference.\x01",
            "Prepare the venue quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_31_5DDA end

    def Function_32_5E39(): pass

    label("Function_32_5E39")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I understand……\x01",
            "Quickly and reliably, is not it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_32_5E39 end

    def Function_33_5E7B(): pass

    label("Function_33_5E7B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well lunch boxed lunch, and …\x01",
            "Well, I can finally get to the rice.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_5E7B end

    def Function_34_5EBB(): pass

    label("Function_34_5EBB")

    EventBegin(0x0)
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    Fade(500)
    OP_68(334710, 1500, 220, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 334710, 0, 220, 45)
    SetChrPos(0x102, 333800, 0, 1230, 45)
    SetChrPos(0x104, 335830, 0, -620, 45)
    SetChrPos(0x103, 332180, 0, 160, 45)
    SetChrPos(0x109, 333080, 0, -440, 45)
    SetChrPos(0x105, 334230, 0, -1120, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_0D()

    ChrTalk(
        0xD,
        "Everyone, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02110FYou came, Lloyd guys.\x02\x03",
            "#02102FNo, thank you.\x01",
            "At last the plenary session began.\x02\x03",
            "Crossbell autonomous state and the surrounding four countries\x01",
            "Representatives meet together,\x01",
            "Indeed unprecedented international conference ……\x02\x03",
            "And such a big event,\x01",
            "The first ever skyscraper building\x01",
            "It is done in Orkis Tower ……\x02\x03",
            "#02109FTo too much excitement and tension\x01",
            "Your sister's heart\x01",
            "It is going to explode soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FApart from excitement\x01",
            "To be very nervous\x01",
            "I can not see it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FYeah, I do not believe anything\x01",
            "いつものGraceさんかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x103, 500)

    ChrTalk(
        0xC,
        (
            "#02105FOh, Tio.\x01",
            "Even though it's been a while since it's been a while, guygui will come.\x02\x03",
            "#02104FWell, it certainly is from pounding\x01",
            "We can admit that the excitement will exceed\x01",
            "But … … anyway.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    ChrTalk(
        0xC,
        (
            "#02100FI will introduce you, Noticia.\x01",
            "They are the Special Support Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Indeed, these children.\x01",
            "Hehe is not so nice than looking at the picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's Ribeal communication notice.\x01",
            "I will do my best today.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#00000FYes, this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FLiberre communication - in the kingdom\x01",
            "It is the most major news organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, and within the industry\x01",
            "There is another hot topic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "A reporter who took the Füritsa award last year\x01",
            "Even being enrolled is famous.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_649B")

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, that person is also Nielsen\x01",
            "It is an award that he once won.\x02\x03",
            "Every year the most excellent\x01",
            "It is given to journalists.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6508")

    label("loc_649B")


    ChrTalk(
        0x105,
        (
            "#12P#10300FFürlitza Prize ……\x02\x03",
            "確か、Every year the most excellent\x01",
            "A gift to a journalist\x01",
            "It's about the prestigious award.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6508")


    ChrTalk(
        0xE,
        "#5PHehe, I know well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PBy the way, the name of the winner\x01",
            "With Nial Barnes\x01",
            "Dorothy Hyatt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PWe are proud of our reveal communications company,\x01",
            "Ace reporter and a genius photographer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FOh, but Libert reporter\x01",
            "What he said was winning last year …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FPerhaps, it happened last year.\x01",
            "Reporting on Libert's disaster\x01",
            "Was it evaluated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PYes, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PWell, strictly earlier than that\x01",
            "Comprehensive judgment including scoop\x01",
            "It seems that it was evaluated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI see……\x01",
            "It sounds like a great reporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FYes, we also\x01",
            "It is a story that I can not lose.\x02\x03",
            "#02103FAs a reporter, everyone\x01",
            "Once I admire the Fuerzza Prize ……\x02\x03",
            "Even for the crown of tomorrow\x01",
            "Every day interview, especially this time interview\x01",
            "I have to cherish it well.\x02\x03",
            "#02110FだからRaines君、\x01",
            "Do not get out around\x01",
            "I will surprise you!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)

    ChrTalk(
        0xD,
        "Yes, Yes Mam!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Well, more than usual\x01",
            "I feel good enough. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F(Tentatively,\x01",
            "If you keep me grown-up\x01",
            "I do not mind … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xE, 0x10E, 0x0)
    OP_93(0xD, 0x0, 0x0)
    SetScenarioFlags(0x1C2, 4)
    Call(0, 36)
    EventEnd(0x5)
    Return()

    # Function_34_5EBB end

    def Function_35_691A(): pass

    label("Function_35_691A")

    Sound(160, 0, 100, 0)
    Return()

    # Function_35_691A end

    def Function_36_6921(): pass

    label("Function_36_6921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6949")
    SetScenarioFlags(0x146, 3)

    label("loc_6949")

    Return()

    # Function_36_6921 end

    def Function_37_694A(): pass

    label("Function_37_694A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    CreatePortrait(0, 16, 192, 528, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis504.itp")
    OP_68(81000, 1000, 4000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 81000, 0, 5500, 180)
    SetChrPos(0x102, 81000, 0, 5500, 180)
    SetChrPos(0x103, 81000, 0, 5500, 180)
    SetChrPos(0x104, 81000, 0, 5500, 180)
    SetChrPos(0x109, 81000, 0, 5500, 180)
    SetChrPos(0x105, 81000, 0, 5500, 180)
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
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 81000, 0, 5500, 180)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(79000, 1000, 300, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 0, 0, 38)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    def lambda_6B0A():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6B0A)
    Sleep(50)

    def lambda_6B1A():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6B1A)
    Sleep(50)

    def lambda_6B2A():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6B2A)
    Sleep(50)

    def lambda_6B3A():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B3A)
    Sleep(50)

    def lambda_6B4A():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6B4A)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#5P#00102F#10AAmazing\x02",
    )

    CloseMessageWindow()
    OP_68(79000, 1000, -2700, 2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_6BB3():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BB3)
    Sleep(300)

    def lambda_6BD0():
        OP_93(0xFE, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6BD0)

    def lambda_6BDD():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BDD)
    Sleep(300)

    def lambda_6BFA():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BFA)
    Sleep(300)

    def lambda_6C17():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C17)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_694A end

    def Function_38_6C40(): pass

    label("Function_38_6C40")

    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    BeginChrThread(0x20, 3, 0, 39)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 42)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 44)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 45)
    Sleep(1300)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    Return()

    # Function_38_6C40 end

    def Function_39_6CB0(): pass

    label("Function_39_6CB0")


    def lambda_6CB5():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CB5)

    def lambda_6CCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CCF)
    WaitChrThread(0xFE, 1)

    def lambda_6CE4():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CE4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_39_6CB0 end

    def Function_40_6D05(): pass

    label("Function_40_6D05")


    def lambda_6D0A():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D0A)

    def lambda_6D24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D24)
    WaitChrThread(0xFE, 1)

    def lambda_6D39():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D39)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#5P#00005F#8AAh……\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_40_6D05 end

    def Function_41_6D95(): pass

    label("Function_41_6D95")


    def lambda_6D9A():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D9A)

    def lambda_6DB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6DB4)
    WaitChrThread(0xFE, 1)

    def lambda_6DC9():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DC9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_41_6D95 end

    def Function_42_6DEA(): pass

    label("Function_42_6DEA")


    def lambda_6DEF():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DEF)

    def lambda_6E09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6E09)
    WaitChrThread(0xFE, 1)

    def lambda_6E1E():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E1E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_42_6DEA end

    def Function_43_6E3F(): pass

    label("Function_43_6E3F")


    def lambda_6E44():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E44)

    def lambda_6E5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6E5E)
    WaitChrThread(0xFE, 1)

    def lambda_6E73():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E73)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_43_6E3F end

    def Function_44_6E94(): pass

    label("Function_44_6E94")


    def lambda_6E99():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E99)

    def lambda_6EB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6EB3)
    WaitChrThread(0xFE, 1)

    def lambda_6EC8():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EC8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_44_6E94 end

    def Function_45_6EE9(): pass

    label("Function_45_6EE9")


    def lambda_6EEE():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EEE)

    def lambda_6F08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6F08)
    WaitChrThread(0xFE, 1)

    def lambda_6F1D():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F1D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_45_6EE9 end

    def Function_46_6F3E(): pass

    label("Function_46_6F3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    OP_68(80600, 1000, -4200, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 79900, 0, -2500, 180)
    SetChrPos(0x102, 81500, 0, -2300, 180)
    SetChrPos(0x103, 79500, 0, -1500, 180)
    SetChrPos(0x104, 80400, 0, -100, 180)
    SetChrPos(0x109, 81100, 0, -1300, 180)
    SetChrPos(0x105, 78600, 0, -1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 78200, 0, 1200, 180)
    OP_68(80600, 1000, -1200, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10109F#5POh no! ~ っ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#5PIt is a wonderful view ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PNo, it's the best sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02809F#5PHa ha, you seemed satisfied.\x02\x03",
            "#02800F── This is 34 F.\x01",
            "When international conferences and so on were held,\x01",
            "The stakeholders will be on the waiting floor.\x02\x03",
            "#02800FThen,\x01",
            "Let's roughly look around.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7162():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7162)
    Sleep(50)

    def lambda_7172():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7172)
    Sleep(50)

    def lambda_7182():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7182)
    Sleep(50)

    def lambda_7192():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7192)
    Sleep(50)

    def lambda_71A2():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_71A2)
    Sleep(50)

    def lambda_71B2():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_71B2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    def lambda_71D7():

        label("loc_71D7")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_71D7")

    QueueWorkItem2(0x101, 2, lambda_71D7)

    def lambda_71E9():

        label("loc_71E9")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_71E9")

    QueueWorkItem2(0x102, 2, lambda_71E9)

    def lambda_71FB():

        label("loc_71FB")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_71FB")

    QueueWorkItem2(0x103, 2, lambda_71FB)

    def lambda_720D():

        label("loc_720D")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_720D")

    QueueWorkItem2(0x109, 2, lambda_720D)

    def lambda_721F():

        label("loc_721F")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_721F")

    QueueWorkItem2(0x105, 2, lambda_721F)

    def lambda_7231():

        label("loc_7231")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7231")

    QueueWorkItem2(0x104, 2, lambda_7231)

    ChrTalk(
        0x101,
        "#12P#00002FYes, please.\x02",
    )

    CloseMessageWindow()
    OP_68(76600, 1000, -1200, 3500)
    BeginChrThread(0x20, 3, 0, 47)
    Sleep(1700)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    def lambda_729A():
        OP_97(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_729A)
    Sleep(100)

    def lambda_72B7():
        OP_97(0x103, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_72B7)
    Sleep(100)

    def lambda_72D4():
        OP_97(0x104, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_72D4)
    Sleep(100)

    def lambda_72F1():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72F1)
    Sleep(100)

    def lambda_730E():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_730E)
    Sleep(100)

    def lambda_732B():
        OP_97(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_732B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x20, 35000, 0, -1000, 270)
    SetChrPos(0x27, 37600, -600, -1000, 270)
    SetChrPos(0x101, 37600, 0, -1400, 270)
    SetChrPos(0x102, 37600, 0, -100, 270)
    SetChrPos(0x103, 38900, 0, -1800, 270)
    SetChrPos(0x104, 38900, 0, -500, 270)
    SetChrPos(0x109, 40200, 0, -1600, 270)
    SetChrPos(0x105, 40200, 0, -300, 270)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6B(0x27)
    SetChrFlags(0x27, 0x20)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x4)
    OP_68(35000, 900, -1000, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(45, 19, 0, 11000)
    SetCameraDistance(18000, 11000)

    def lambda_7479():
        OP_95(0xFE, 8500, 0, -1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7479)

    def lambda_7493():
        OP_96(0xFE, 0x2968, 0xFFFFFDA8, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7493)

    def lambda_74AD():
        OP_97(0x101, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_74AD)
    Sleep(50)

    def lambda_74CA():
        OP_97(0x102, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_74CA)
    Sleep(50)

    def lambda_74E7():
        OP_97(0x103, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_74E7)
    Sleep(50)

    def lambda_7504():
        OP_97(0x104, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7504)
    Sleep(50)

    def lambda_7521():
        OP_97(0x109, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7521)
    Sleep(50)

    def lambda_753E():
        OP_97(0x105, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_753E)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_7564():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7564)
    Sleep(50)

    def lambda_7578():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7578)
    Sleep(500)

    def lambda_758C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_758C)
    Sleep(50)

    def lambda_75A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_75A0)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x2D, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    ChrTalk(
        0x20,
        (
            "#6P#02803FThere, in addition to the security office room\x01",
            "Waiting rooms such as reporters are lining up.\x02\x03",
            "#02800FIn case of terrorist infiltration,\x01",
            "Once, one unit of the guard corps\x01",
            "I'm in the lower floor waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F#11PI have heard a story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PThe guards are also the choice\x01",
            "You seem to be gathered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PBut what about reporters,\x01",
            "Grace女史も来るのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)

    ChrTalk(
        0x20,
        (
            "#6P#02805FOh, the Crossbell Times\x01",
            "Was it a female reporter?\x02\x03",
            "#02804FI think that it was on the list\x01",
            "Perhaps, I will come to the interview.\x02\x03",
            "#02800FBy the way, the reporters\x01",
            "Outside of press and press conference\x01",
            "I will not put it out of this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#11PIndeed, it is reasonable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FSometimes get through security\x01",
            "I'd like to make an interview\x01",
            "There are also violent reporters …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FというかGraceさんが\x01",
            "It is most like that though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWell, as expected\x01",
            "I have to stop when I find it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x1F4)

    def lambda_78F7():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_78F7)

    def lambda_7911():
        OP_97(0x101, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7911)
    Sleep(50)

    def lambda_792E():
        OP_97(0x102, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_792E)
    Sleep(50)

    def lambda_794B():
        OP_97(0x103, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_794B)
    Sleep(50)

    def lambda_7968():
        OP_97(0x104, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7968)
    Sleep(50)

    def lambda_7985():
        OP_97(0x109, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7985)
    Sleep(50)

    def lambda_79A2():
        OP_97(0x105, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_79A2)
    SetCameraDistance(21000, 5000)
    Sleep(5000)
    Fade(1000)
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x20, -13000, 0, 3500, 0)
    SetChrPos(0x27, -13000, -500, 1400, 0)
    SetChrPos(0x101, -13800, 0, 1400, 0)
    SetChrPos(0x102, -12700, 0, 1400, 0)
    SetChrPos(0x103, -13400, 0, 100, 0)
    SetChrPos(0x104, -12300, 0, 100, 0)
    SetChrPos(0x109, -13600, 0, -1200, 0)
    SetChrPos(0x105, -12500, 0, -1200, 0)
    OP_6B(0x27)
    SetChrFlags(0x27, 0x20)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x4)
    OP_68(-13000, 900, 1400, 0)
    MoveCamera(33, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(49, 19, 0, 7000)
    SetCameraDistance(18000, 7000)

    def lambda_7ACA():
        OP_97(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7ACA)

    def lambda_7AE4():
        OP_98(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7AE4)

    def lambda_7AFE():
        OP_97(0x101, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7AFE)
    Sleep(50)

    def lambda_7B1B():
        OP_97(0x102, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7B1B)
    Sleep(50)

    def lambda_7B38():
        OP_97(0x103, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7B38)
    Sleep(50)

    def lambda_7B55():
        OP_97(0x104, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7B55)
    Sleep(50)

    def lambda_7B72():
        OP_97(0x109, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7B72)
    Sleep(50)

    def lambda_7B8F():
        OP_97(0x105, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7B8F)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x10E, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    ChrTalk(
        0x20,
        (
            "#02800F#11POnce, this room is also\x01",
            "Let me show you around.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-14000, 1000, 17400, 1000)
    FadeToDark(1000, 0, -1)

    def lambda_7C11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C11)
    Sleep(50)

    def lambda_7C21():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C21)

    def lambda_7C2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7C2E)
    Sleep(50)

    def lambda_7C3E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7C3E)

    def lambda_7C4B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7C4B)
    Sleep(50)

    def lambda_7C5B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C5B)
    OP_0D()
    SetChrPos(0x101, 142100, 0, 10100, 315)
    SetChrPos(0x102, 141200, 0, 8200, 270)
    SetChrPos(0x103, 142300, 0, 7000, 225)
    SetChrPos(0x104, 145600, 0, 10200, 0)
    SetChrPos(0x109, 144100, 0, 6300, 225)
    SetChrPos(0x105, 144100, 0, 11000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 147500, 0, 7000, 270)
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x5)
    OP_68(142600, 1100, 500, 0)
    MoveCamera(33, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21500, 0)
    OP_68(143600, 1100, 11500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(143600, 1100, 8700, 0)
    MoveCamera(53, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    ChrTalk(
        0x105,
        "#11P#10302FOh … this is brilliant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00002FIt's like a rest room\x01",
            "It's a very open feeling …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02804FThis is a stakeholder in the conference\x01",
            "It is a prepared break room.\x02\x03",
            "#02800FFor breaks etc.\x01",
            "Do not hesitate to use it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E61():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E61)
    Sleep(50)

    def lambda_7E71():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E71)
    Sleep(50)

    def lambda_7E81():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7E81)
    Sleep(50)

    def lambda_7E91():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7E91)
    Sleep(50)

    def lambda_7EA1():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7EA1)
    Sleep(50)

    def lambda_7EB1():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7EB1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00004FYes, without hesitation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHuhu, even afterwards tea\x01",
            "Shall I come for a rush?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02809FWell, in such a place\x01",
            "Shall I show you to the next floor?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x20, -13000, 0, 11000, 180)
    SetChrPos(0x27, -13000, -500, 13100, 180)
    SetChrPos(0x101, -13800, 0, 13100, 180)
    SetChrPos(0x102, -12700, 0, 13100, 180)
    SetChrPos(0x103, -13400, 0, 14400, 180)
    SetChrPos(0x104, -12300, 0, 14400, 180)
    SetChrPos(0x109, -13600, 0, 15700, 180)
    SetChrPos(0x105, -12500, 0, 15700, 180)
    OP_6B(0x27)
    SetChrFlags(0x27, 0x20)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x8)
    SetChrFlags(0x27, 0x4)
    OP_68(-13000, 900, 14100, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(53, 19, 0, 4000)
    SetCameraDistance(18500, 4000)

    def lambda_8057():
        OP_95(0xFE, -13000, 0, 1800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8057)

    def lambda_8071():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8071)

    def lambda_808B():
        OP_97(0x101, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_808B)
    Sleep(50)

    def lambda_80A8():
        OP_97(0x102, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80A8)
    Sleep(50)

    def lambda_80C5():
        OP_97(0x103, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_80C5)
    Sleep(50)

    def lambda_80E2():
        OP_97(0x104, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_80E2)
    Sleep(50)

    def lambda_80FF():
        OP_97(0x109, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80FF)
    Sleep(50)

    def lambda_811C():
        OP_97(0x105, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_811C)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)

    def lambda_8144():
        OP_95(0xFE, -14800, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8144)
    WaitChrThread(0x27, 1)
    OP_6B(0xFF)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_817E():

        label("loc_817E")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_817E")

    QueueWorkItem2(0x101, 2, lambda_817E)
    WaitChrThread(0x102, 0)

    def lambda_8194():

        label("loc_8194")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8194")

    QueueWorkItem2(0x102, 2, lambda_8194)
    WaitChrThread(0x103, 0)

    def lambda_81AA():

        label("loc_81AA")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_81AA")

    QueueWorkItem2(0x103, 2, lambda_81AA)
    WaitChrThread(0x104, 0)

    def lambda_81C0():

        label("loc_81C0")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_81C0")

    QueueWorkItem2(0x104, 2, lambda_81C0)
    WaitChrThread(0x20, 1)

    def lambda_81D6():
        OP_95(0xFE, -17600, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_81D6)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_81F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_81F9)
    WaitChrThread(0x20, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    BeginChrThread(0x101, 3, 0, 48)
    Sleep(700)
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(300)
    BeginChrThread(0x103, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 48)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 48)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 48)
    OP_0D()
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x101, -48000, 0, -1000, 270)
    SetChrPos(0x102, -48000, 0, -1000, 270)
    SetChrPos(0x103, -48000, 0, -1000, 270)
    SetChrPos(0x104, -48000, 0, -1000, 270)
    SetChrPos(0x109, -48000, 0, -1000, 270)
    SetChrPos(0x105, -48000, 0, -1000, 270)
    SetChrPos(0x20, -54000, 0, 2000, 180)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x0)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x3C)
    OP_68(-50000, 1100, -1000, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(-54000, 1100, 1300, 4000)
    SetCameraDistance(19000, 4000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x5, 0x0, 0x0)
    OP_79(0xC)
    BeginChrThread(0x101, 3, 0, 49)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 50)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 51)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 52)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 53)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 54)
    Sleep(1300)
    Sound(104, 0, 100, 0)
    OP_71(0xC, 0x5, 0x0, 0x0, 0x0)
    OP_79(0xC)
    SetMapObjFlags(0xC, 0x10)
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x101,
        (
            "#12P#00005Fhere……\x01",
            "Is it an emergency staircase area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FDown stairs\x01",
            "It seems that it is blocked … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02803F#5POriginally using stairs\x01",
            "I can get off to 1F.\x02\x03",
            "#02801FHowever during this conference\x01",
            "Other than 34F, 35F, 36F\x01",
            "I try to block it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI see……\x01",
            "It is a security reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FBut if an earthquake\x01",
            "What do you do when you wake up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02806F#5PIn that case, automatically\x01",
            "All emergency staircases are opened.\x02\x03",
            "#02800FWell, perfect security\x01",
            "That is impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see……\x01",
            "I will be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00208F…… Hacking measures etc\x01",
            "It seems necessary to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02804F#5PWell, it's a big deal\x01",
            "Shall I use the stairs?\x02\x03",
            "#02800F35F\x01",
            "It is an international conference hall floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_6F3E end

    def Function_47_86E2(): pass

    label("Function_47_86E2")

    OP_92(0xFE, 0x128E0, 0x0, 0x1F4)

    def lambda_86F4():
        OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86F4)
    WaitChrThread(0xFE, 1)

    def lambda_8712():
        OP_95(0xFE, 68000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8712)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_86E2 end

    def Function_48_872C(): pass

    label("Function_48_872C")


    def lambda_8731():
        OP_95(0xFE, -14800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8731)
    WaitChrThread(0xFE, 1)

    def lambda_874F():
        OP_95(0xFE, -17600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_874F)
    Sleep(300)

    def lambda_876C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_876C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_872C end

    def Function_49_877D(): pass

    label("Function_49_877D")


    def lambda_8782():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8782)

    def lambda_879C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_879C)
    WaitChrThread(0xFE, 1)

    def lambda_87B1():
        OP_95(0xFE, -55000, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87B1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_49_877D end

    def Function_50_87D2(): pass

    label("Function_50_87D2")


    def lambda_87D7():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87D7)

    def lambda_87F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_87F1)
    WaitChrThread(0xFE, 1)

    def lambda_8806():
        OP_95(0xFE, -53500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8806)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_50_87D2 end

    def Function_51_8827(): pass

    label("Function_51_8827")


    def lambda_882C():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_882C)

    def lambda_8846():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8846)
    WaitChrThread(0xFE, 1)

    def lambda_885B():
        OP_95(0xFE, -54500, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_885B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_51_8827 end

    def Function_52_887C(): pass

    label("Function_52_887C")


    def lambda_8881():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8881)

    def lambda_889B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_889B)
    WaitChrThread(0xFE, 1)

    def lambda_88B0():
        OP_95(0xFE, -53000, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_52_887C end

    def Function_53_88D1(): pass

    label("Function_53_88D1")


    def lambda_88D6():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_88D6)

    def lambda_88F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_88F0)
    WaitChrThread(0xFE, 1)

    def lambda_8905():
        OP_95(0xFE, -51500, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8905)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_53_88D1 end

    def Function_54_8926(): pass

    label("Function_54_8926")


    def lambda_892B():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_892B)

    def lambda_8945():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8945)
    WaitChrThread(0xFE, 1)

    def lambda_895A():
        OP_95(0xFE, -51500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_895A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_8926 end

    def Function_55_897B(): pass

    label("Function_55_897B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(73000, 1200, -1000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 74500, 0, -1000, 270)
    SetChrPos(0x102, 73800, 0, 200, 225)
    SetChrPos(0x103, 73800, 0, -2200, 315)
    SetChrPos(0x104, 72200, 0, 200, 135)
    SetChrPos(0x109, 71500, 0, -1000, 90)
    SetChrPos(0x105, 72200, 0, -2200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright ……\x01",
            "Was this one round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FFor now\x01",
            "There seems to be no problem in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FOh, with this condition again,\x01",
            "Let's look around and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x02\x03",
            "#00108F…… For the conference\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right, the mayor and the chairman\x01",
            "I think I am trying hard but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is \"Chairman of Iron Blood\"\x01",
            "Is it Rock Smith President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, at break time\x01",
            "Why do not you ask someone?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_897B end

    def Function_56_8C13(): pass

    label("Function_56_8C13")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-55500, 1200, -1500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -54000, 0, -1500, 270)
    SetChrPos(0x102, -54700, 0, -300, 225)
    SetChrPos(0x103, -54700, 0, -2700, 315)
    SetChrPos(0x104, -56300, 0, -300, 135)
    SetChrPos(0x109, -57000, 0, -1500, 90)
    SetChrPos(0x105, -56300, 0, -2700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright ……\x01",
            "Was this one round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FFor now\x01",
            "There seems to be no problem in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FOh, with this condition again,\x01",
            "Let's look around and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x02\x03",
            "#00108F…… For the conference\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right, the mayor and the chairman\x01",
            "I think I am trying hard but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is \"Chairman of Iron Blood\"\x01",
            "Is it Rock Smith President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, at break time\x01",
            "Why do not you ask someone?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_8C13 end

    def Function_57_8EAB(): pass

    label("Function_57_8EAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    LoadChrToIndex("apl/ch50011.itc", 0x24)
    LoadChrToIndex("apl/ch51090.itc", 0x25)
    SoundLoad(803)
    SoundLoad(3455)
    SoundLoad(3456)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 142100, 50, 5800, 220)
    SetChrPos(0x102, 142700, 50, 4100, 275)
    SetChrPos(0x103, 142000, 50, 2500, 315)
    SetChrPos(0x104, 140450, 50, 1750, 5)
    SetChrPos(0x109, 138800, 50, 2500, 40)
    SetChrPos(0x105, 138200, 50, 4100, 95)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 140450, 50, 6350, 185)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xD, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0xE, 0x29)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xF, 0x2A)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x10, 0x2B)
    OP_49()
    SetChrPos(0x28, 142300, 0, 6000, 45)
    OP_D5(0x28, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x29, 138600, 0, 2300, 225)
    OP_D5(0x29, 0x0, 0x36EE8, 0x0, 0x0)
    SetChrPos(0x2A, 138600, 0, 6000, 315)
    OP_D5(0x2A, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0x2B, 142200, 0, 2300, 135)
    OP_D5(0x2B, 0x0, 0x20F58, 0x0, 0x0)
    SetChrChipByIndex(0x2C, 0x25)
    SetChrSubChip(0x2C, 0x7)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 140450, 550, 5650, 0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And Lloyd's\x01",
            "先に休憩に入ったIan lawyerと\x01",
            "I got the opportunity to talk again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(140450, 900, 4100, 0)
    MoveCamera(35, 33, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25500, 0)
    MoveCamera(65, 33, 0, 5000)
    SetCameraDistance(19500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(140450, 1100, 4100, 0)
    MoveCamera(68, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#02205F#5PI see …\x01",
            "Have you guys also participated in security?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00002FYeah, honestly only with a degree of relaxation\x01",
            "Although it may not be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PNo, in the incident of assassination of the mayor\x01",
            "You guys who raised big Venus.\x02\x03",
            "#02200FEven just staying in this place\x01",
            "I am very encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00104FIf you can say that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHaha, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#11PSo the teacher.\x01",
            "How is the meeting?\x02\x03",
            "The atmosphere that was so rough\x01",
            "I could not feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5POh, now it's going well.\x02\x03",
            "Some trade agreements include\x01",
            "The consent of each country was also obtained ……\x02\x03",
            "#02200FMayor of Dieterの呼びかけも\x01",
            "It looks like it was not wasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102FHehe, is that so ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FIt is a bit relieved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FBut what \"for now\" is\x01",
            "Is there any concern?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)

    ChrTalk(
        0x102,
        "#11P#00105FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F……Really?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)

    ChrTalk(
        0x8,
        (
            "#02203F#5PHmm, it is an observer\x01",
            "It's what I say from my mouth ….\x02\x03",
            "The first half, such as trade and finance\x01",
            "Economic agenda was almost there.\x02\x03",
            "#02201F── But the second half of the meeting\x01",
            "Proposal to be proposed from each country leader …\x02\x03",
            "Apparently, the crossbell\x01",
            "There seems to be a story about security.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00013Fthat is……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F…… What is security?\x01",
            "Does that mean we can also talk about military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FBut it was signed two years ago\x01",
            "There is also a \"non - war treaty\", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PThat is because His Majesty the Queen of Libert\x01",
            "The crisis situation of the crossbell of those days\x01",
            "I suggested to suppress it.\x02\x03",
            "Remiferia is not involved,\x01",
            "Above all, the crossbell itself\x01",
            "It is not involved in the \"Treaty of the Battle of the World\".\x02\x03",
            "#02201FIn that sense, it is different\x01",
            "A new security framework\x01",
            "It is certain that we are being asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106F……surely.\x01",
            "That was also my concern for my grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#11PThen, I crossed the crossbell\x01",
            "Why do not you join a new treaty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right, same as the November War Convention,\x01",
            "To solve conflicts between states with force\x01",
            "A framework to prohibit ─\x02\x03",
            "#10105F─ ─ ─ Ah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FReally……\x01",
            "Crossbell is not a \"state\".\x02\x03",
            "#00008FApproved by the Empire and the Republic\x01",
            "It is only \"autonomous state\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PYes, that means\x01",
            "I would like to conclude the \"International Convention\"\x01",
            "It means that you do not have state sovereignty.\x02\x03",
            "Economic \"agreement\" can be tied\x01",
            "It is impossible to conclude the \"treaty\" in an equal position.\x02\x03",
            "#02201FAs a result, the security of this area\x01",
            "It is a translation that has been badly jeopardized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FConfusing though ……\x01",
            "I understand somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11P……Excuse me.\x01",
            "Can I have a minute?\x02\x03",
            "#00203FBesides crossbell\x01",
            "There is autonomous state.\x02\x03",
            "Leman Autonomous Region, Oredo Autonomous Region,\x01",
            "Northern Buri Autonomous Region ……\x02\x03",
            "#00200FLike those autonomous states\x01",
            "Can not we conclude international treaties?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PNo, that's not true.\x02\x03",
            "#02200FSurely those autonomous states also\x01",
            "Depending on their historical circumstances\x01",
            "It is not established as a state … …\x02\x03",
            "In a form delegated from \"Sowing country\"\x01",
            "Equal sovereignty is recognized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FSowing country ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00103FThose autonomous states decisively\x01",
            "Differences from crossbell …\x02\x03",
            "#00101FIt approved the formation\x01",
            "It is \"Alteria law country\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F#11PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FWhen you say Alteria law country\x01",
            "Is it a headquarters mountain of the Seven Yigh Church?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00104FYeah, the land is small, but\x01",
            "I have a religious authority … …\x02\x03",
            "#00100FMany autonomous states and free cities\x01",
            "It depends on that and is established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FBut Crossbell, in the Empire and the Republic\x01",
            "\"Autonomous state\" approved and established … …\x02\x03",
            "#00001FSo to speak as well as two religious countries\x01",
            "It is in the shape it has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FYeah, and that's historically\x01",
            "Various twists#6R噵 噵 噵#And a tragedy … …\x02\x03",
            "Even a little sovereign in the crossbell\x01",
            "If accepted, a little more situation\x01",
            "It will change, but ….\x02\x03",
            "#00106F… … that the two major powers recognize it\x01",
            "It will not be possible forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F… that … … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11P… … There is sighing going out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5P── I will return the story,\x01",
            "Apparently the Prime Minister and the President,\x01",
            "There seems to be a proposal on security.\x02\x03",
            "Of course it is an equal treaty\x01",
            "It is not that each country connects.\x02\x03",
            "#02201F…… The chairman and the mayors these days\x01",
            "It seems to be a place to strengthen vigilance.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x8,
        (
            "#02210F#5PHaha, sorry.\x01",
            "You seem to have made me uneasy.\x02\x03",
            "#02200FWell, McDowell etc.\x01",
            "This situation will be familiar.\x02\x03",
            "それにMayor of Dieterの方は\x01",
            "There seems to be some workaround.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    SetChrSubChip(0x105, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        "#11P#00005FIs it a measure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FWhat does that mean ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PNo, the detailed story\x01",
            "I have not heard of it either ─ ─\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)
    SetChrSubChip(0x109, 0x0)

    ChrTalk(
        0x101,
        "#11P#00000FExcuse me.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    OP_24(0x323)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x9)
    Sleep(300)
    Sound(804, 0, 100, 0)
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00008FMission support section,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3455V#30W── Bannings.\x01",
            "The press conference here is over.\x02\x03",
            "#3456VThe leaders raised to 36 F,\x01",
            "Where are you guys?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD80)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FOh, yes.\x01",
            "It is a rest room of 34F … …\x02\x03",
            "#00001F……Did you have something?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually, with Prime Minister Osborne\x01",
            "From President Rock Smith\x01",
            "There was a request for each.\x02\x03",
            "── During your break, with you\x01",
            "I heard he wants to talk directly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(2087, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#4SWhat! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "…… The other party is your opponent.\x01",
            "You can not refuse it as expected.\x02\x03",
            "During the break, it is in 36F\x01",
            "Visit the two leaders' rooms.\x02\x03",
            "The innermost of the left wing is the president,\x01",
            "The innermost part of the right wing is the prime minister's room.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006FWait a moment, please!\x01",
            "What is it like ……\x02\x03",
            "#00011FAs expected, the load is too heavy!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─ ─ Do not take over, Bannings.\x02\x03",
            "You can see the speculation of both\x01",
            "Is not it a unique opportunity?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FIt is!\x02\x03",
            "#00003F……I understand.\x01",
            "I will head to the two leaders at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you are in emergency, depend on Miss Ellie.\x01",
            "The VIP partner should be familiar.\x02\x03",
            "Come to report when the talk is over.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FI understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x3E8)
    Sound(804, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x102,
        "#11P#00101FLloyd, this time ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FHey, do something disturbing\x01",
            "Did not I say?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#00003FAh……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"President of the Iron Blood\" and President Rock Smith\x01",
            "I explained what was called respectively.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x109,
        "#12P#10111FWell! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FWell, are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PApparently in a joke\x01",
            "It looks like it is nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02205F#5PNo, I was surprised.\x02\x03",
            "#02210FApparently more than I thought\x01",
            "The name of the Special Affairs Division is\x01",
            "It seems to be known.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00006FNo … … To the staff of the two leaders\x01",
            "I have acquainted with each other.\x02\x03",
            "#00008FSo be interested\x01",
            "It may only be held up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FI see……\x01",
            "That seems to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F……Even if\x01",
            "I can not refuse.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006FOh, 36 F\x01",
            "It is the room at the back of the left wing and the right wing.\x02\x03",
            "#00001FLet's visit at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PIt is okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FI, Yes, sir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrPos(0x28, 156000, 0, 0, 0)
    SetChrPos(0x29, 156000, 0, 0, 0)
    SetChrPos(0x2A, 156000, 0, 0, 0)
    SetChrPos(0x2B, 156000, 0, 0, 0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 144700, 0, 4800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x142, 1)
    OP_29(0xA4, 0x1, 0x2)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_57_8EAB end

    def Function_58_AEAF(): pass

    label("Function_58_AEAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31250.itc", 0x1F)
    LoadChrToIndex("chr/ch31251.itc", 0x20)
    SoundLoad(145)
    SoundLoad(143)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -48500, 0, -1000, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -48500, 0, -1000, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -48500, 0, -1000, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2D, 0x1F)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2D, 0x8000)
    OP_90(0x2D, -51500, -2000, 10000, 0)
    OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x1F)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2E, 0x4)
    SetChrFlags(0x2E, 0x8000)
    OP_90(0x2E, -51500, -2000, 10000, 0)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x1F)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x2F, 0x4)
    SetChrFlags(0x2F, 0x8000)
    OP_90(0x2F, -51500, -2000, 10000, 0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x30, 0x1F)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x30, 0x4)
    SetChrFlags(0x30, 0x8000)
    OP_90(0x30, -51500, -2000, 10000, 0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x6, 0x3C)
    OP_70(0x7, 0x3C)
    OP_68(-54000, 1100, 12500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x2D, 3, 0, 62)
    BeginChrThread(0x2E, 3, 0, 63)
    BeginChrThread(0x2F, 3, 0, 64)
    BeginChrThread(0x30, 3, 0, 65)
    OP_0D()
    OP_68(-51500, 1000, 2500, 3500)
    Sleep(1800)
    OP_71(0x7, 0x3C, 0x0, 0x0, 0x0)
    Sound(145, 2, 100, 0)
    Sleep(700)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x5)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    BeginChrThread(0x9, 3, 0, 59)
    BeginChrThread(0xA, 3, 0, 60)
    BeginChrThread(0xB, 3, 0, 61)
    OP_79(0x7)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    WaitChrThread(0x2D, 3)

    ChrTalk(
        0x2D,
        "#6PWhat is this! Is it?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        "#12PWell, why are you sudden …?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)

    ChrTalk(
        0xB,
        "#12PWhat, what is happening! Is it?\x02",
    )

    CloseMessageWindow()
    OP_68(-49400, 1000, 400, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetChrPos(0x9, 76600, 0, 2600, 0)
    SetChrPos(0xA, 74700, 0, 1800, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xC, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 76500, 0, 200, 315)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 75800, 0, -1200, 0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 74200, 0, -1000, 0)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 72400, 0, -200, 45)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 72700, 0, -1300, 45)
    OP_4B(0x10, 0xFF)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 71300, 0, 600, 90)
    OP_4B(0x11, 0xFF)
    OP_68(72700, 1000, 4450, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(75000, 1000, 2500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0x9,
        (
            "#11PIt is useless!\x01",
            "I do not react even if I press the button!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PCut …\x01",
            "What's going on! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02105F#11PJust a bit, this is the interview\x01",
            "I can not do it! Is it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        "#02101F#5PRaines君、何とかしなさい！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    ChrTalk(
        0xD,
        "#12PMu, please do not speak ~!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x91)
    SetScenarioFlags(0x142, 5)
    SetScenarioFlags(0x22, 4)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_AEAF end

    def Function_59_B41F(): pass

    label("Function_59_B41F")

    Sleep(600)

    def lambda_B427():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B427)

    def lambda_B441():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B441)
    WaitChrThread(0xFE, 1)

    def lambda_B456():
        OP_95(0xFE, -51100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B456)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_59_B41F end

    def Function_60_B477(): pass

    label("Function_60_B477")


    def lambda_B47C():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B47C)

    def lambda_B496():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B496)
    WaitChrThread(0xFE, 1)

    def lambda_B4AB():
        OP_95(0xFE, -52700, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4AB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_60_B477 end

    def Function_61_B4CC(): pass

    label("Function_61_B4CC")

    Sleep(1200)

    def lambda_B4D4():
        OP_95(0xFE, -52000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4D4)

    def lambda_B4EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4EE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_61_B4CC end

    def Function_62_B506(): pass

    label("Function_62_B506")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B513():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B513)

    def lambda_B52D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B52D)
    WaitChrThread(0xFE, 1)

    def lambda_B542():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B542)
    WaitChrThread(0xFE, 1)

    def lambda_B560():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B560)
    WaitChrThread(0xFE, 1)

    def lambda_B57E():
        OP_95(0xFE, -53800, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B57E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Return()

    # Function_62_B506 end

    def Function_63_B5AA(): pass

    label("Function_63_B5AA")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B5BA():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5BA)

    def lambda_B5D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5D4)
    WaitChrThread(0xFE, 1)

    def lambda_B5E9():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5E9)
    WaitChrThread(0xFE, 1)

    def lambda_B607():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B607)
    WaitChrThread(0xFE, 1)

    def lambda_B625():
        OP_95(0xFE, -54200, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B625)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_63_B5AA end

    def Function_64_B64E(): pass

    label("Function_64_B64E")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B65E():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B65E)

    def lambda_B678():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B678)
    WaitChrThread(0xFE, 1)

    def lambda_B68D():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B68D)
    WaitChrThread(0xFE, 1)

    def lambda_B6AB():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6AB)
    WaitChrThread(0xFE, 1)

    def lambda_B6C9():
        OP_95(0xFE, -55100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6C9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_64_B64E end

    def Function_65_B6F2(): pass

    label("Function_65_B6F2")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_B702():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B702)

    def lambda_B71C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B71C)
    WaitChrThread(0xFE, 1)

    def lambda_B731():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B731)
    WaitChrThread(0xFE, 1)

    def lambda_B74F():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B74F)
    WaitChrThread(0xFE, 1)

    def lambda_B76D():
        OP_95(0xFE, -55800, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B76D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_65_B6F2 end

    def Function_66_B796(): pass

    label("Function_66_B796")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02000.itp")
    CreatePortrait(1, 16, 192, 528, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis519.itp")
    LoadChrToIndex("chr/ch27202.itc", 0x1E)
    LoadChrToIndex("chr/ch27302.itc", 0x1F)
    LoadChrToIndex("chr/ch32002.itc", 0x20)
    LoadChrToIndex("chr/ch32102.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch44900.itc", 0x23)
    LoadChrToIndex("chr/ch00002.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00302.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x27)
    LoadChrToIndex("chr/ch03002.itc", 0x28)
    LoadChrToIndex("chr/ch00202.itc", 0x29)
    SetChrChipByIndex(0x25, 0x22)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 271000, 0, 13000, 180)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 275200, 0, 13800, 225)
    SetChrChipByIndex(0x21, 0x1E)
    SetChrSubChip(0x21, 0x2)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 272800, 100, 10900, 270)
    SetChrChipByIndex(0x22, 0x1F)
    SetChrSubChip(0x22, 0x2)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 272800, 100, 8950, 270)
    SetChrChipByIndex(0x23, 0x20)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 272800, 100, 7000, 270)
    SetChrChipByIndex(0x24, 0x21)
    SetChrSubChip(0x24, 0x2)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 272800, 100, 5000, 270)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x27)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 269200, 100, 10900, 90)
    SetChrPos(0x102, 269200, 100, 8950, 90)
    SetChrPos(0x103, 269200, 100, 7000, 90)
    SetChrPos(0x104, 269200, 100, 5000, 90)
    SetChrPos(0x109, 269200, 100, 2950, 90)
    SetChrPos(0x105, 272800, 100, 2950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x1)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#00011FPhantom beast#4RGenji#\"- ─ ─?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(271000, 900, 1000, 0)
    MoveCamera(35, 33, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23000, 0)
    OP_68(271000, 900, 11000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(3500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_6F(0x79)
    Fade(500)
    OP_68(271000, 1300, 10000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x25,
        (
            "─ ─ Yes, you are right.\x02\x03",
            "It is hard to say that it is mere monsters,\x01",
            "A large, mysterious monster ……\x02\x03",
            "Such existence, across the crossbell\x01",
            "It is supposed to be discovered.\x02",
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
    OP_93(0x26, 0x5A, 0x1F4)
    Sleep(500)
    OP_68(271300, 2000, 10320, 1500)
    MoveCamera(30, 11, 0, 1500)
    SetCameraDistance(20500, 1500)

    def lambda_BC1E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_BC1E)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x1, 0xA, 0x0, 0x0)
    OP_79(0x11)

    def lambda_BC42():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_BC42)
    Sleep(100)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x23,
        (
            "#11PAh……\x01",
            "It is the one we saw!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PAfter all, before stabbing the stop\x01",
            "I let it escape … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10101F#12P#NThese monsters are … ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00206F#12P#NSuch information is\x01",
            "Although it was flowing … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x26,
        (
            "#5P── It's not only that.\x01",
            "Other types have also been confirmed.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x26, 0x5A, 0x1F4)
    Sleep(500)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0xB, 0x14, 0x0, 0x0)
    OP_79(0x11)
    Sleep(1500)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x15, 0x1E, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#N#00007FTh-This is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#N#00101FIt appeared in the old mine …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#12P#NHey hey, did you come back again? Is it?\x02",
    )

    CloseMessageWindow()
    OP_93(0x26, 0xE1, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x26,
        (
            "#5PThe other day, the same type things\x01",
            "It appears in the mountainous areas in the north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PTo that Scott\x01",
            "It has already been exterminated.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(271560, 1300, 9270, 1200)
    MoveCamera(40, 19, 0, 1200)
    SetCameraDistance(21500, 1200)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00006FIs that so……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10105F#12P#NMaybe by two people\x01",
            "Did you get rid of it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x21, 0x1)
    Sleep(100)
    SetChrSubChip(0x22, 0x0)
    Sleep(200)

    ChrTalk(
        0x21,
        (
            "#5POh, poke surprised\x01",
            "I managed to beat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#5PThis is from you too\x01",
            "Thanks for the information being circulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#11PIt's just a strange response.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11PThe way in which Arts works is different\x01",
            "It faded away as if to shine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108Falso……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#6P#N… and when we fought\x01",
            "Look exactly the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10303F#12P#NBut what is the mountainous area … …\x02\x03",
            "#10301FThis time it appeared \"outdoors\", did not it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C198():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_C198)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x21, 0x2)
    Sleep(50)
    SetChrSubChip(0x22, 0x2)
    WaitChrThread(0x25, 2)
    Sleep(150)

    ChrTalk(
        0x25,
        (
            "#02006F#5PYes, as before.\x01",
            "\"Tower\" and \"monastery\" etc.\x01",
            "Unusual places are confirmed.\x02\x03",
            "Apparently for some reason\x01",
            "If \"distortion of the place\" occurs\x01",
            "I guess it is … …\x02\x03",
            "#02001FBut, these \"phantom beasts\" are\x01",
            "Also in mountains and lakes\x01",
            "It's emerging.\x02\x03",
            "Perhaps the \"distortion of the place\"\x01",
            "Even outdoors like that\x01",
            "It may be appearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#12P#NSounds like that … ….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        "#11PIt is a story not to be shy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PSo, we\x01",
            "Why did you call here?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(273530, 1300, 11920, 1500)
    MoveCamera(40, 14, 0, 1500)
    OP_6E(450, 1500)
    SetCameraDistance(22580, 1500)
    OP_71(0x11, 0x1F, 0x28, 0x0, 0x0)
    OP_79(0x11)
    OP_6F(0x79)

    ChrTalk(
        0x26,
        (
            "#5POh, responding to these eidolons\x01",
            "For both the guild and the Special Affairs Support Division\x01",
            "I want to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PSince independence advocacy was done,\x01",
            "At Belgard and Tangram arms\x01",
            "Somewhat strained state continues …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PUntil at least the referendum vote is over\x01",
            "I want to concentrate on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F#N……I understand.\x01",
            "I will underwrite it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#12PRegarding sharing\x01",
            "Even if you leave it to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#02004F#5PYeah, I will hand over the data\x01",
            "I will leave it to you.\x02\x03",
            "#02001FAnd …\x01",
            "I'd like to ask for identification of \"cause\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x21, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x22, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x23, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x24, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#12P#N#00205FCause … …?\x02\x03",
            "#00200FWhy did such a \"beast\"\x01",
            "Have you suddenly appeared?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x25,
        (
            "#02003F#5PYeah, the evolution of the monster\x01",
            "From a long time ago in a certain cycle\x01",
            "I am awake, but ….\x02\x03",
            "#02001FRegarding this \"phantom beast\"\x01",
            "\"Abnormal circumstances\" out of that\x01",
            "It will not be an exaggeration to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PDefinitely\x01",
            "There should be some cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PGenerate \"distortion of the place\"\x01",
            "A large monstrat of common sense is out\x01",
            "There is only cause to show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#6P#NWell, certainly.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#11PBet on the name of the guild\x01",
            "Let's keep track of it.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_66_B796 end

    def Function_67_C8A5(): pass

    label("Function_67_C8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC0A")
    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0xD, 0xFF)
    Fade(500)
    OP_68(32470, 1500, -1390, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17510, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 30440, 0, -1390, 90)
    SetChrPos(0x1, 29160, 0, -2400, 90)
    SetChrPos(0x2, 29770, 0, 10, 90)
    SetChrPos(0x3, 28400, 0, -990, 90)
    SetChrPos(0x4, 27880, 0, 10, 90)
    SetChrPos(0x5, 28070, 0, -2600, 90)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "So …\x01",
            "As I have said many times\x01",
            "The press reporters can not pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PWell, but now I'm taking a break … …\x01",
            "Somehow, is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6PYes, anything other than taking pictures\x01",
            "I will not do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6PThat's right, but to a senior … ….\x02",
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
        0x101,
        (
            "#6P#00012FEven though I know it is not good\x01",
            "You are going.\x02\x03",
            "#00003FI tried to break through forcedly\x01",
            "It seems I do not feel like ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FThis also reporter sex#2RSaka#What'll we do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FTentatively …\x01",
            "I heard that I can not pass here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x9, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1, 5)
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x5)
    Jump("loc_CC8A")

    label("loc_CC0A")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Before the elevator floor\x01",
            "Reporters are pushing.\x02\x03",
            "For a while,\x01",
            "I can not get through this place.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x4)

    label("loc_CC8A")

    Return()

    # Function_67_C8A5 end

    def Function_68_CC8B(): pass

    label("Function_68_CC8B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF08")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FBy the way, during the meeting\x01",
            "Apart from the elevator in front\x01",
            "Did not you use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, for security reasons\x01",
            "That was supposed to be the case.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_CE27")

    ChrTalk(
        0x103,
        (
            "#00200FLike the emergency staircase,\x01",
            "Also here by the power net\x01",
            "It seems to be controlled and managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, it seems so.\x02\x03",
            "#00000FWell, when you move\x01",
            "Let's use the front elevator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF00")

    label("loc_CE27")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, opening and closing of the lock\x01",
            "With the power net\x01",
            "It seems to be controlled and managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, Kusufusaki is Orkistor's\x01",
            "Security is a place.\x02\x03",
            "#00000FWell, when you move\x01",
            "Let's use the front elevator.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF00")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_CF77")

    label("loc_CF08")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x02\x03",
            "During the meeting, this elevator\x01",
            "It seems that it can not be used.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CF77")

    TalkEnd(0xFF)
    Return()

    # Function_68_CC8B end

    def Function_69_CF7B(): pass

    label("Function_69_CF7B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Emergency stairs shutter\x01",
            "It is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001FIs this the 33rd floor direction?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FCompletely during the meeting\x01",
            "封鎖するというIt was a story.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_D0E4")

    ChrTalk(
        0x103,
        (
            "#00200FLike an elevator,\x01",
            "This is also a power net\x01",
            "It seems to be controlled, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPerfect security\x01",
            "It was impossible - was it?\x02\x03",
            "#00001FIn the unlikely event\x01",
            "I suppose I should assume.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D19D")

    label("loc_D0E4")


    ChrTalk(
        0x103,
        (
            "#00200FShutter lock\x01",
            "With the power net\x01",
            "It seems to be controlled, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPerfect security\x01",
            "It was impossible - was it?\x02\x03",
            "#00001FIn the unlikely event\x01",
            "I suppose I should assume.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D19D")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_D20E")

    label("loc_D1A5")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Emergency stairs shutter\x01",
            "It is tightly closed.\x02\x03",
            "During the meeting, to the next floor\x01",
            "I do not seem to be able to come and go.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D20E")

    TalkEnd(0xFF)
    Return()

    # Function_69_CF7B end

    def Function_70_D212(): pass

    label("Function_70_D212")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_70_D212 end

    SaveToFile()

Try(main)
