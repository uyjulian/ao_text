from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Lawyer Ian",             # 1
        "Policeman",              # 2
        "Policeman",              # 3
        "Vice Chief Pierre",      # 4
        "Grace",                  # 5
        "Reins",                  # 6
        "Reporter Noticia",       # 7
        "Reporter Claude",        # 8
        "Reporter Parker",        # 9
        "Imperial Chronicle Reporter",# 10
        "Policeman",              # 11
        "Policeman",              # 12
        "Policeman",              # 13
        "Reporter Thompson",      # 14
        "Tyrell News Reporter",   # 15
        "Detective Dudley",       # 16
        "Detective",              # 17
        "Detective",              # 18
        "Captain Grant",          # 19
        "Sgt. Major Giselle",     # 20
        "City Hall Staffer",      # 21
        "City Hall Staffer",      # 22
        "City Hall Staffer",      # 23
        "Secretary Lechter",      # 24
        "Mayor Dieter",           # 25
        "Bracer Scott",           # 26
        "Bracer Wenzel",          # 27
        "Bracer Ling",            # 28
        "Bracer Eolia",           # 29
        "Commander Sonya",        # 30
        "Vice Commander Douglas", # 31
        "Dummy",                  # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "椅子",                   # 35
        "椅子",                   # 36
        "食器",                   # 37
        "CGF Member",             # 38
        "CGF Member",             # 39
        "CGF Member",             # 40
        "CGF Member",             # 41
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
        "Function_4_144D",         # 04, 4
        "Function_5_1885",         # 05, 5
        "Function_6_1C1A",         # 06, 6
        "Function_7_256C",         # 07, 7
        "Function_8_278F",         # 08, 8
        "Function_9_2897",         # 09, 9
        "Function_10_2A2D",        # 0A, 10
        "Function_11_2B87",        # 0B, 11
        "Function_12_3008",        # 0C, 12
        "Function_13_325E",        # 0D, 13
        "Function_14_3465",        # 0E, 14
        "Function_15_36FB",        # 0F, 15
        "Function_16_3863",        # 10, 16
        "Function_17_3EB2",        # 11, 17
        "Function_18_4011",        # 12, 18
        "Function_19_4436",        # 13, 19
        "Function_20_45A2",        # 14, 20
        "Function_21_4836",        # 15, 21
        "Function_22_49A7",        # 16, 22
        "Function_23_4A9A",        # 17, 23
        "Function_24_4C6C",        # 18, 24
        "Function_25_525E",        # 19, 25
        "Function_26_541E",        # 1A, 26
        "Function_27_585A",        # 1B, 27
        "Function_28_5DD6",        # 1C, 28
        "Function_29_6001",        # 1D, 29
        "Function_30_6030",        # 1E, 30
        "Function_31_67E3",        # 1F, 31
        "Function_32_6863",        # 20, 32
        "Function_33_689B",        # 21, 33
        "Function_34_68E6",        # 22, 34
        "Function_35_7404",        # 23, 35
        "Function_36_740B",        # 24, 36
        "Function_37_7434",        # 25, 37
        "Function_38_7728",        # 26, 38
        "Function_39_7798",        # 27, 39
        "Function_40_77ED",        # 28, 40
        "Function_41_787C",        # 29, 41
        "Function_42_78D1",        # 2A, 42
        "Function_43_7926",        # 2B, 43
        "Function_44_797B",        # 2C, 44
        "Function_45_79D0",        # 2D, 45
        "Function_46_7A25",        # 2E, 46
        "Function_47_928B",        # 2F, 47
        "Function_48_92D5",        # 30, 48
        "Function_49_9326",        # 31, 49
        "Function_50_937B",        # 32, 50
        "Function_51_93D0",        # 33, 51
        "Function_52_9425",        # 34, 52
        "Function_53_947A",        # 35, 53
        "Function_54_94CF",        # 36, 54
        "Function_55_9524",        # 37, 55
        "Function_56_97FD",        # 38, 56
        "Function_57_9AD6",        # 39, 57
        "Function_58_BED7",        # 3A, 58
        "Function_59_C43A",        # 3B, 59
        "Function_60_C492",        # 3C, 60
        "Function_61_C4E7",        # 3D, 61
        "Function_62_C521",        # 3E, 62
        "Function_63_C5C5",        # 3F, 63
        "Function_64_C669",        # 40, 64
        "Function_65_C70D",        # 41, 65
        "Function_66_C7B1",        # 42, 66
        "Function_67_D9B6",        # 43, 67
        "Function_68_DDED",        # 44, 68
        "Function_69_E117",        # 45, 69
        "Function_70_E420",        # 46, 70
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_1274")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E4")

    ChrTalk(
        0xFE,
        (
            "It looks like the reporters\x01",
            "have finally given up on trying\x01",
            "to get to the floor above.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. I don't know if\x01",
            "it's because of their\x01",
            "job or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pushiness of reporters\x01",
            "is the same no matter what\x01",
            "country you go to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_126F")

    label("loc_11E4")


    ChrTalk(
        0xFE,
        (
            "*sigh*. I don't know if\x01",
            "it's because of their\x01",
            "job or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pushiness of reporters\x01",
            "is the same no matter what\x01",
            "country you go to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126F")

    Jump("loc_1449")

    label("loc_1274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1282")
    Jump("loc_1449")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139E")

    ChrTalk(
        0xFE,
        (
            "This is the waiting room\x01",
            "for both domestic and\x01",
            "foreign journalists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In general, reporters are not\x01",
            "allowed to leave the waiting room\x01",
            "while the conference is in session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone is gathered\x01",
            "inside. Please, feel free\x01",
            "to enter and confirm that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1449")

    label("loc_139E")


    ChrTalk(
        0xFE,
        (
            "This is the waiting room\x01",
            "for journalists from all\x01",
            "countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In general, reporters are not\x01",
            "allowed to leave the waiting room\x01",
            "while the conference is in session.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1449")

    TalkEnd(0xFE)
    Return()

    # Function_3_10DF end

    def Function_4_144D(): pass

    label("Function_4_144D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1461")
    Call(0, 6)
    Jump("loc_1881")

    label("loc_1461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_185F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C7")

    ChrTalk(
        0xC,
        (
            "#02100FOh, Lloyd and friends.\x01",
            "It looks like the\x01",
            "security's all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FWell, at least it is\x01",
            "right now.\x02\x03",
            "How is your coverage\x01",
            "going, Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02102FHaha, about that.\x01",
            "Thankfully, we're getting\x01",
            "great results.\x02\x03",
            "By the way, I'm thinking\x01",
            "of writing a more positive\x01",
            "article than I thought.\x02\x03",
            "#02109FIt would be nice if I had\x01",
            "more material aimed at the\x01",
            "general public, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FUmm, I think I\x01",
            "understand, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FPlease don't show up\x01",
            "anywhere you're not\x01",
            "supposed to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02104FIt's fine! In that\x01",
            "department, Reins will\x01",
            "be―\x02\x03",
            "#02101FNo, I mean we'll be sure\x01",
            "to follow the rules.\x02\x03",
            "#02109FSo you guys have nothin'\x01",
            "to worry about, right?\x02",
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
        "#00006F(*sigh*, I'm worried...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Yes, I'm worried\x01",
            "too...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 1)
    Jump("loc_185A")

    label("loc_17C7")


    ChrTalk(
        0xC,
        (
            "#02109FI'll be sure to follow the\x01",
            "rules.\x02\x03",
            "#02100FNow then, I think I'll head to\x01",
            "the break room after getting in\x01",
            "contact with the news agency.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185A")

    Jump("loc_1881")

    label("loc_185F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187E")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_187E")

    Call(0, 5)

    label("loc_1881")

    TalkEnd(0xFE)
    Return()

    # Function_4_144D end

    def Function_5_1885(): pass

    label("Function_5_1885")

    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFE")

    ChrTalk(
        0xC,
        (
            "#02100FAnd, what about Nial and\x01",
            "Dorothy coming here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, they had coverage they couldn't\x01",
            "get away from in the Republic and\x01",
            "couldn't come here right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's not a good\x01",
            "situation over there, in\x01",
            "its own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02103FI see. It's between those\x01",
            "nationalists and\x01",
            "extremists, right?\x02\x03",
            "#02101FI happened to hear that\x01",
            "both sides are going to see\x01",
            "how this conference goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. You don't call\x01",
            "yourself a reporter for\x01",
            "nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have indeed heard\x01",
            "that. There's no hard\x01",
            "evidence, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(So Grace knows even\x01",
            "that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Anyway, we've got to\x01",
            "continue our patrol.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1C11")

    label("loc_1AFE")


    ChrTalk(
        0xC,
        (
            "#02100FThat's right, Noticia. If you\x01",
            "run into Nial, please tell him\x01",
            "the following for me.\x02\x03",
            ""Congratulations on winning\x01",
            "the Fuelitzer Prize. I'll be\x01",
            "taking the next one for sure."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. I heard you were\x01",
            "an acquaintance of\x01",
            "Nial's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes, I'll be sure to\x01",
            "tell him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C11")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_5_1885 end

    def Function_6_1C1A(): pass

    label("Function_6_1C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E11")

    ChrTalk(
        0x1F,
        (
            "#11505FI see. So Mr. Beardy\x01",
            "Bear is of the coffee\x01",
            "faction, huh.\x02\x03",
            "#11500FI think you'd get along\x01",
            "with Chancellor Osborne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FHmm. The chancellor\x01",
            "drinks coffee often?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11503FYes. And black, to boot.\x02\x03",
            "#11502FI think that's why his eyes\x01",
            "are always ecstatically\x01",
            "wide awake like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#02202FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FHaha. Indeed, I can't\x01",
            "agree with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(T-This is an amazing\x01",
            "combination.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Yes... It's quite\x01",
            "dark.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 2)
    Jump("loc_256B")

    label("loc_1E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FE")

    ChrTalk(
        0xC,
        (
            "#02104FHmm. Chancellor Osborne\x01",
            "is of the coffee\x01",
            "faction, they said...\x02\x03",
            "#02100FThen, which are you,\x01",
            "Lechter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11510FHmm. If I had to say, I\x01",
            "myself am of the black tea\x01",
            "faction.\x02\x03",
            "#11500FBut... What are you planning,\x01",
            "asking the preferences of a\x01",
            "second-class secretary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FWeeell, since you don quite the\x01",
            "generous mask, I was thinking to try\x01",
            "to get something before the others...\x02\x03",
            "#02102FAfter all, a handsome man and\x01",
            "beautiful woman alone are enough to\x01",
            "make a fine article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11509FHaha, I see. I'm happy\x01",
            "to hear that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_END)), "loc_2124")

    ChrTalk(
        0x101,
        (
            "#00006F(Hmm. I feel like it's an\x01",
            "obvious front.)\x02\x03",
            "#00001F(It seems like Grace and\x01",
            "Lechter understood each other,\x01",
            "to a certain degree...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe. I guess they're\x01",
            "mixing truth and lies to\x01",
            "sound each other out?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F6")

    label("loc_2124")


    ChrTalk(
        0x101,
        (
            "#00006F(Hmm. I feel like it's\x01",
            "an obvious front.)\x02\x03",
            "#00001F(I'm sure Grace knows\x01",
            "that Lechter isn't just\x01",
            "some secretary...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe. I guess they're\x01",
            "mixing truth and lies to\x01",
            "sound each other out?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F6")

    SetScenarioFlags(0x1C1, 3)
    Jump("loc_256B")

    label("loc_21FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248C")

    ChrTalk(
        0x1F,
        (
            "#11501FThat's right. Actually,\x01",
            "there's something I want to\x01",
            "discuss with Mr. Beardy Bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02205FHmm, what's this about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11506FAh, just some worries about\x01",
            "my workplace.\x02\x03",
            "I'd like to ask the opinion\x01",
            "of Mr. Beardy Bear, famous\x01",
            "for his work on human rights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02202FI see... Well it's\x01",
            "obviously impossible\x01",
            "now, though.\x02\x03",
            "If you like, please\x01",
            "contact my office\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lawyer Ian presented\x01",
            "Secretary Lechter with\x01",
            "his business card.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x1F,
        "#11509FOh, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(I see. So he's\x01",
            "expanding his personal\x01",
            "connections.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Well, extroversion is a\x01",
            "necessary skill for\x01",
            "intelligence operatives.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 4)
    Jump("loc_256B")

    label("loc_248C")


    ChrTalk(
        0x1F,
        "#11500FAnd, Mr. Beardy Bear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02202FYes, that is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#02100FHmm, hmm, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(...We can't listen to\x01",
            "the entire conversation\x01",
            "of these three.)\x02\x03",
            "(Let's not intrude any\x01",
            "more than we already\x01",
            "have.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256B")

    Return()

    # Function_6_1C1A end

    def Function_7_256C(): pass

    label("Function_7_256C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_25F2")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I knew it was too\x01",
            "much to try and sneak\x01",
            "onto the VIP floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even so, I wonder\x01",
            "where Grace went?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278B")

    label("loc_25F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2600")
    Jump("loc_278B")

    label("loc_2600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_278B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_261F")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_261F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F0")

    ChrTalk(
        0xFE,
        (
            "Liberl News ace\x01",
            "camerawoman Dorothy\x01",
            "Hyatt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pictures she takes are\x01",
            "extremely vivid and\x01",
            "captivate all who view them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a cameraman, I would\x01",
            "love to speak with her,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_278B")

    label("loc_26F0")


    ChrTalk(
        0xFE,
        (
            "Hmm. Maybe I'll pay a\x01",
            "visit to Liberl News on\x01",
            "my next trip to Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll take a lot of time\x01",
            "to travel between Ruan and\x01",
            "the capital, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278B")

    TalkEnd(0xFE)
    Return()

    # Function_7_256C end

    def Function_8_278F(): pass

    label("Function_8_278F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2871")

    ChrTalk(
        0xFE,
        (
            "Well, even with the two countries'\x01",
            "motives, the results from the first\x01",
            "half of the conference were quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Liberl and Remiferia see\x01",
            "stimulation of the continental\x01",
            "economy as positive, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2893")

    label("loc_2871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2890")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2890")

    Call(0, 5)

    label("loc_2893")

    TalkEnd(0xFE)
    Return()

    # Function_8_278F end

    def Function_9_2897(): pass

    label("Function_9_2897")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2965")

    ChrTalk(
        0xFE,
        (
            "Hmm. It's very unusual for the\x01",
            "major powers to compromise\x01",
            "this much on state proposals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, it is the case that\x01",
            "state interests are directly\x01",
            "connected to their own, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A29")

    label("loc_2965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2980")
    Call(0, 10)
    Jump("loc_2A29")

    label("loc_2980")


    ChrTalk(
        0xFE,
        (
            "But, this Orchis Tower\x01",
            "is a completely\x01",
            "unthinkable building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's of course impossible to see\x01",
            "Remiferia, but can't you clearly\x01",
            "see the Republic's Altair City?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A29")

    TalkEnd(0xFE)
    Return()

    # Function_9_2897 end

    def Function_10_2A2D(): pass

    label("Function_10_2A2D")


    ChrTalk(
        0x15,
        (
            "Once again, I am\x01",
            "Thompson of Ardent\x01",
            "Press.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You're a Tyrell News\x01",
            "cameraman, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Yes. I'm still\x01",
            "inexperienced, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Ardent, you said. Then\x01",
            "you're from Remiferia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Our countries may be different\x01",
            "but there's no competition―\x01",
            "Let's work together today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, I agree. I look\x01",
            "forward to working with\x01",
            "you, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_10_2A2D end

    def Function_11_2B87(): pass

    label("Function_11_2B87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C56")

    ChrTalk(
        0xFE,
        (
            "*sigh*. The meeting's\x01",
            "first half has finally\x01",
            "died down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, the arguments in the\x01",
            "second half are sure to\x01",
            "be even more heated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The main event has yet\x01",
            "to begin.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2CC5")

    label("loc_2C56")


    ChrTalk(
        0xFE,
        (
            "The arguments in the\x01",
            "second half are sure to\x01",
            "be even more heated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The main event has yet\x01",
            "to begin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC5")

    Jump("loc_3004")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E85")
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's right, they said\x01",
            "all countries gave their\x01",
            "consent on that issue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, to report that to\x01",
            "the main office...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(It looks like he's\x01",
            "contacting someone via\x01",
            "ENIGMA.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Most likely, his fellow\x01",
            "reporters are outside\x01",
            "the tower.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hehe. The play-by-play\x01",
            "of the trade conference,\x01",
            "huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(How to say this... That\x01",
            "must be difficult work.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2F1B")

    label("loc_2E85")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's right, they said\x01",
            "all countries gave their\x01",
            "consent on that issue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, to report that to\x01",
            "the main office...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1B")

    Jump("loc_3004")

    label("loc_2F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3B")
    Call(0, 12)
    Jump("loc_3004")

    label("loc_2F3B")


    ChrTalk(
        0xFE,
        (
            "Haha. If you're saying\x01",
            "that, then Rocksmith is\x01",
            "a yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Seeing is believing―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In contrast to normal Tyrell News\x01",
            "articles, based on the impression I\x01",
            "got, I could feel his bold personality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3004")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B87 end

    def Function_12_3008(): pass

    label("Function_12_3008")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        (
            "Ah, well even so, everything\x01",
            "about this conference is\x01",
            "outside the norm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "There are many conferences between the two\x01",
            "countries, but this time includes Crossbell\x01",
            "and the four neighboring countries...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Also, to think that Chancellor\x01",
            "Osborne and President Rocksmith\x01",
            "decided to discuss things directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In addition, this is virtually\x01",
            "the first time the two men\x01",
            "have ever met face-to-face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Today is a historical\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Yeah, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Starting with your Imperial Chronicle,\x01",
            "reporters from all nations are gathered\x01",
            "here― And ready to cover the news!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_12_3008 end

    def Function_13_325E(): pass

    label("Function_13_325E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3320")

    ChrTalk(
        0xFE,
        (
            "It's too bad we can't get coverage\x01",
            "from the VIP floor... But there's\x01",
            "still plenty of chances for coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to go over the\x01",
            "outline of questions I\x01",
            "want to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3461")

    label("loc_3320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_332E")
    Jump("loc_3461")

    label("loc_332E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3461")

    ChrTalk(
        0xFE,
        (
            "In various areas, the\x01",
            "Crossbell Police are often\x01",
            "seen as incompetent, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on the security in this building, I\x01",
            "get the contrary impression that they're\x01",
            "actually an outstanding organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The problem isn't the people\x01",
            "but the structure of the\x01",
            "state... I feel that strongly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3461")

    TalkEnd(0xFE)
    Return()

    # Function_13_325E end

    def Function_14_3465(): pass

    label("Function_14_3465")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3505")

    ChrTalk(
        0xFE,
        (
            "Now then, while I was\x01",
            "hurrying, it looks like\x01",
            "break time's already over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to start preparing\x01",
            "for the conference's\x01",
            "second half.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_3505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_362F")

    ChrTalk(
        0xFE,
        (
            "Regarding the economics-\x01",
            "related agreements, I can only\x01",
            "say I'm amazed at the results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might be because Mayor\x01",
            "Dieter, who made the proposals,\x01",
            "is also the IBC President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Economic development will promote\x01",
            "continental security... I feel\x01",
            "it's not necessarily a fantasy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F7")

    label("loc_362F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_36F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364A")
    Call(0, 12)
    Jump("loc_36F7")

    label("loc_364A")


    ChrTalk(
        0xFE,
        (
            "Even so... Chancellor\x01",
            "Osborne's intensity is\x01",
            "the real thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's completely different from\x01",
            "looking at a photo of him. That makes\x01",
            "a lot of things fall into place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F7")

    TalkEnd(0xFE)
    Return()

    # Function_14_3465 end

    def Function_15_36FB(): pass

    label("Function_15_36FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_376C")

    ChrTalk(
        0xFE,
        (
            "Break time will be over soon...\x01",
            "I guess I should buy something\x01",
            "to drink while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_385F")

    label("loc_376C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_377A")
    Jump("loc_385F")

    label("loc_377A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_385F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3795")
    Call(0, 10)
    Jump("loc_385F")

    label("loc_3795")


    ChrTalk(
        0xFE,
        (
            "Yes, it's clear that\x01",
            "there's good weather\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, you can\x01",
            "almost count the number of\x01",
            "tourists visiting Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This tower will have an\x01",
            "amazing impact on the\x01",
            "economy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385F")

    TalkEnd(0xFE)
    Return()

    # Function_15_36FB end

    def Function_16_3863(): pass

    label("Function_16_3863")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_3953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3881")
    Call(0, 17)
    Jump("loc_394E")

    label("loc_3881")


    ChrTalk(
        0x17,
        (
            "#00600FOh, you guys, huh.\x02\x03",
            "Although there's still some\x01",
            "time, you should visit each of\x01",
            "the heads of state ASAP.\x02\x03",
            "I don't think I have to say\x01",
            "this, but it's not the case\x01",
            "that you can keep them waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394E")

    Jump("loc_3EAE")

    label("loc_3953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEA")

    ChrTalk(
        0x17,
        (
            "#00600FYou guys, huh.\x02\x03",
            "Is anything amiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNot right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSo you can get a view of\x01",
            "the entire security\x01",
            "detail on this monitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603FYeah. We can check on every important\x01",
            "point in Orchis Tower in real time,\x01",
            "conference room included, of course.\x02\x03",
            "#00600FThis building is equipped with the\x01",
            "latest security camera system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FSecurity cameras... IBC\x01",
            "and the Orbal Store have\x01",
            "started using them.\x02\x03",
            "#00200FThere's a lot more of\x01",
            "them here, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou talk about it like\x01",
            "it's no big deal, but it's\x01",
            "really amazing technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, they might eventually\x01",
            "use them to keep an eye on\x01",
            "areas outside the city, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHmm. That's a sensitive matter. It'll\x01",
            "depend on whether we can secure the\x01",
            "understanding of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603F...Anyway, being able to use them is definitely\x01",
            "convenient.\x02\x03",
            "#00601FBesides monitoring for potential terrorists, if\x01",
            "they do strike, all we can do is respond before\x01",
            "they cause trouble, or immediately afterwards.\x02\x03",
            "For that reason, we mustn't overlook even the\x01",
            "most trivial information.\x02\x03",
            "If you see anything, report it at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, roger.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 5)
    Call(0, 36)
    Jump("loc_3EAE")

    label("loc_3DEA")


    ChrTalk(
        0x17,
        (
            "#00603FWe're in constant contact with the\x01",
            "surrounding areas, and no conspicuous\x01",
            "problems have occurred as of yet.\x02\x03",
            "#00600FGuys, please continue your patrols of\x01",
            "the appropriate floors for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EAE")

    TalkEnd(0xFE)
    Return()

    # Function_16_3863 end

    def Function_17_3EB2(): pass

    label("Function_17_3EB2")

    OP_4B(0x17, 0xFF)
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0x17,
        (
            "#00600FCaptain Grant, how is\x01",
            "your company doing at\x01",
            "present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Naturally, all of us are\x01",
            "standing by on high\x01",
            "alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "After all, our duty is to\x01",
            "be ready for any kind of\x01",
            "emergency at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603FI see. That's reassuring.\x02\x03",
            "#00601FNow then, about the\x01",
            "force's deployment for the\x01",
            "conference's second half―\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    OP_4C(0x1A, 0xFF)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x1A, 0x10)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_17_3EB2 end

    def Function_18_4011(): pass

    label("Function_18_4011")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4141")

    ChrTalk(
        0xFE,
        (
            "At present, no abnormalities\x01",
            "detected both within and\x01",
            "outside of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to the surveillance team,\x01",
            "neither Red Constellation nor\x01",
            "Heiyue show any signs of action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I say it's the calm\x01",
            "before the storm? ...I can't\x01",
            "help but think it's ominous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4203")

    label("loc_4141")


    ChrTalk(
        0xFE,
        (
            "According to the surveillance team,\x01",
            "neither Red Constellation nor\x01",
            "Heiyue show any signs of action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I say it's the calm\x01",
            "before the storm? ...I can't\x01",
            "help but think it's ominous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4203")

    Jump("loc_4432")

    label("loc_4208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4355")

    ChrTalk(
        0xFE,
        (
            "We've set up a structure in this\x01",
            "security planning room to immediately\x01",
            "integrate information from all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Furthermore, although the terminals\x01",
            "here are limited, we're able to\x01",
            "connect to the database at police HQ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the need arises, we can\x01",
            "get information about\x01",
            "suspicious characters here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4432")

    label("loc_4355")


    ChrTalk(
        0xFE,
        (
            "In setting up the structure\x01",
            "here, we received full\x01",
            "cooperation from Mayor Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've put practically the full power of\x01",
            "Crossbell behind this security structure...\x01",
            "For this reason, mistakes won't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4432")

    TalkEnd(0xFE)
    Return()

    # Function_18_4011 end

    def Function_19_4436(): pass

    label("Function_19_4436")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_44E0")

    ChrTalk(
        0xFE,
        (
            "To think we've continued security\x01",
            "operations for this long without\x01",
            "information coming in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just where are those\x01",
            "terrorists hiding\x01",
            "themselves?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_459E")

    label("loc_44E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_459E")

    ChrTalk(
        0xFE,
        (
            "We haven't got wind of\x01",
            "any sign of terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the face of this perfect system, they\x01",
            "gave up on their plan... That would be\x01",
            "nice, but it's too optimistic, huh.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x19, 0x2)
    Return()

    label("loc_459E")

    TalkEnd(0xFE)
    Return()

    # Function_19_4436 end

    def Function_20_45A2(): pass

    label("Function_20_45A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_47A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E3")

    ChrTalk(
        0xFE,
        (
            "No matter whether it's during break\x01",
            "or during the conference, our\x01",
            "security activities don't change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Within this perfect system,\x01",
            "where and how are the terrorists\x01",
            "planning to break through...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are several possible\x01",
            "patterns. We'll have see how\x01",
            "things go and play it by ear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_479D")

    label("loc_46E3")


    ChrTalk(
        0xFE,
        (
            "Within this perfect system,\x01",
            "where and how are the terrorists\x01",
            "planning to break through...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are several possible\x01",
            "patterns. We'll have see how\x01",
            "things go and play it by ear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_479D")

    Jump("loc_4832")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4832")

    ChrTalk(
        0xFE,
        (
            "By using the monitors\x01",
            "like this, we can be\x01",
            "sure everyone is alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Terrorists, huh... It's\x01",
            "hard not to feel\x01",
            "anxious.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_4832")

    TalkEnd(0xFE)
    Return()

    # Function_20_45A2 end

    def Function_21_4836(): pass

    label("Function_21_4836")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4909")

    ChrTalk(
        0xFE,
        (
            "We of the Escort\x01",
            "Division are handling\x01",
            "Orchis Tower security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We train for emergencies\x01",
            "through actual combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the worst happens,\x01",
            "I'm confident we're as\x01",
            "capable as the CGF.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_49A3")

    label("loc_4909")


    ChrTalk(
        0xFE,
        (
            "Because we of the Escort\x01",
            "Division train for emergencies\x01",
            "through actual combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the worst happens,\x01",
            "I'm confident we're as\x01",
            "capable as the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A3")

    TalkEnd(0xFE)
    Return()

    # Function_21_4836 end

    def Function_22_49A7(): pass

    label("Function_22_49A7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Normally, we're responsible for securing\x01",
            "important government facilities and\x01",
            "guarding various dignitaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The anniversary festival was the same,\x01",
            "but handling international events like\x01",
            "these is one of our most important jobs.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_49A7 end

    def Function_23_4A9A(): pass

    label("Function_23_4A9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB8")
    Call(0, 17)
    Jump("loc_4B98")

    label("loc_4AB8")


    ChrTalk(
        0xFE,
        (
            "Hmm. If they don't show up during break\x01",
            "time, the turning point will be during\x01",
            "the conference's second half, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, maybe I'm\x01",
            "overthinking it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, when the time\x01",
            "arrives, we'll be ready\x01",
            "to do our best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B98")

    Jump("loc_4C68")

    label("loc_4B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB8")
    Call(0, 24)
    Jump("loc_4C68")

    label("loc_4BB8")


    ChrTalk(
        0xFE,
        (
            "It doesn't really matter,\x01",
            "but this room is really too\x01",
            "much for just two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it... Orchis Tower\x01",
            "is in a whole other league\x01",
            "compared to everything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C68")

    TalkEnd(0xFE)
    Return()

    # Function_23_4A9A end

    def Function_24_4C6C(): pass

    label("Function_24_4C6C")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    TurnDirection(0x1B, 0x0, 500)

    ChrTalk(
        0x109,
        (
            "#10100FCaptain Grant, thank you\x01",
            "for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHello, and the same.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Sergeant Seeker and\x01",
            "Sergeant Randy, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Ah, sorry. I forgot that\x01",
            "neither of you are assigned\x01",
            "to the CGF right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FIt's true that I'm on temporary\x01",
            "transfer, but please just call\x01",
            "me by whatever's easiest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha. Anything's fine by\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's just the two of you\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Yes, it's because the\x01",
            "heads of state and the\x01",
            "press corps are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "It was decided the CGF should avoid\x01",
            "exposure as much as possible, so\x01",
            "we're minimally deployed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FIn other words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes, it's out of consideration for the\x01",
            "major powers.\x02\x03",
            "The CGF is trying to hide the fact that\x01",
            "its arms are limited by state law from\x01",
            "the other militaries...\x02\x03",
            "Although it's within limits, it would\x01",
            "take a large amount of money to improve\x01",
            "or expand our units' equipment.\x02\x03",
            "#10108FBecause of that, it would be easy for\x01",
            "ridicule of the CGF to become a topic\x01",
            "at a conference like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see... So that's why\x01",
            "you're trying to stay\x01",
            "out of sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FMan. Diplomacy sure is a\x01",
            "difficult thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well, that's certainly\x01",
            "true, but I try not to\x01",
            "complain that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "In the end, this is just\x01",
            "for appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Instead, a whole company is\x01",
            "on the floor below, ready\x01",
            "to move out at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "All of us will be here right\x01",
            "away if something happens,\x01",
            "so there's no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FI see, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWe'll be counting on you\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x1C1, 6)
    Call(0, 36)
    Return()

    # Function_24_4C6C end

    def Function_25_525E(): pass

    label("Function_25_525E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5302")

    ChrTalk(
        0xFE,
        (
            "Now that the conference is\x01",
            "half over, the situation\x01",
            "seems to have changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to sense\x01",
            "terrorist movements\x01",
            "before they act, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_541A")

    label("loc_5302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_541A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_531D")
    Call(0, 24)
    Jump("loc_541A")

    label("loc_531D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B3")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Sergeant Noｱl, let's\x01",
            "both do everything we\x01",
            "can today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave the floor security\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, roger that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_541A")

    label("loc_53B3")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Sergeant Noｱl, let's\x01",
            "both do everything we\x01",
            "can today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave the floor security\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_541A")

    TalkEnd(0xFE)
    Return()

    # Function_25_525E end

    def Function_26_541E(): pass

    label("Function_26_541E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_542F")
    Jump("loc_5856")

    label("loc_542F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_544A")
    Call(0, 27)
    Jump("loc_5856")

    label("loc_544A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5783")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54E5")
    Jump("loc_552F")

    label("loc_54E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5505")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_552F")

    label("loc_5505")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5525")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_552F")

    label("loc_5525")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_552F")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0x101,
        (
            "#00001FCome to think of it,\x01",
            "Vice Chief, who were you\x01",
            "talking about just now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I'm interested in\x01",
            "that too. Could they be\x01",
            "a suspicious character?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hm? What will my wife...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "Hey, this has nothing to\x01",
            "do with you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Get back to work, on the\x01",
            "double!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FA-Alright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(I can't believe it. He\x01",
            "was thinking of his\x01",
            "wife.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(He certainly is a hen-pecked\x01",
            "husband. ...There must be\x01",
            "something between them.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Right... Let's keep\x01",
            "this quiet.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1C2, 0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_5856")

    label("loc_5783")

    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        (
            "Grr... Every single\x01",
            "person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Even I... Even I...\x02",
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

    label("loc_5856")

    TalkEnd(0xFE)
    Return()

    # Function_26_541E end

    def Function_27_585A(): pass

    label("Function_27_585A")

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
            "Hmm, could he be...? No,\x01",
            "I'm positive it's\x01",
            "something like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005F(W-Who is "he"?)\x02\x03",
            "#00000FUmm, Chief Pierre?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Yes!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "I-It's the Special\x01",
            "Support Section, of all\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Do you have business\x01",
            "with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FChief, what are you\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FH-Hey, Tio―\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "I'm not doing anything...\x01",
            "except serving as the chief\x01",
            "of security planning!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305FOh, is that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FCome to think of it, I\x01",
            "remember reading your name on\x01",
            "some materials we were given.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see. I didn't study\x01",
            "the documents enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Y-You...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F*sigh*, too late...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FI should have told you\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, but you're the security\x01",
            "planning chief. Why aren't\x01",
            "you in the planning room?\x02\x03",
            "You're here on break then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmph. I gave Dudley\x01",
            "full command authority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Intruding on a situation\x01",
            "like that is rather\x01",
            "difficult to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Think whatever you want...\x01",
            "As his boss, it's my job\x01",
            "to know these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway... Make sure not\x01",
            "to get in Dudley's way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FU-Understood.\x02",
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

    # Function_27_585A end

    def Function_28_5DD6(): pass

    label("Function_28_5DD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5DEA")
    Call(0, 6)
    Jump("loc_5FFD")

    label("loc_5DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F3C")

    ChrTalk(
        0x8,
        (
            "#02203FHmm. Even disregarding\x01",
            "the details, to be called\x01",
            "by both heads of state.\x02\x03",
            "#02200FI'm sure you're nervous,\x01",
            "but chances like this\x01",
            "don't come by often.\x02\x03",
            "I think even just taking\x01",
            "in their auras will be\x01",
            "good experience for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, it's as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FExcuse us then, Mr.\x01",
            "Grimwood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5FEF")

    label("loc_5F3C")


    ChrTalk(
        0x8,
        (
            "#02200FI felt it at the conference too,\x01",
            "but even just taking in their auras\x01",
            "should be good experience for you.\x02\x03",
            "Don't think about unnecessary\x01",
            "things, and just go visit them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FEF")

    Jump("loc_5FFD")

    label("loc_5FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5FFD")

    label("loc_5FFD")

    TalkEnd(0xFE)
    Return()

    # Function_28_5DD6 end

    def Function_29_6001(): pass

    label("Function_29_6001")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_6015")
    Call(0, 6)
    Jump("loc_602C")

    label("loc_6015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_6023")
    Jump("loc_602C")

    label("loc_6023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_602C")

    label("loc_602C")

    TalkEnd(0xFE)
    Return()

    # Function_29_6001 end

    def Function_30_6030(): pass

    label("Function_30_6030")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_60E7")

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but... A lot of\x01",
            "people with strange auras, starting\x01",
            "with Mr. Grimwood, have gathered here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like it's not a\x01",
            "normal atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67DF")

    label("loc_60E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_6185")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I\x01",
            "wonder where Vice Chief\x01",
            "Pierre went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't been back for a\x01",
            "while. Did he go to the\x01",
            "security planning room?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67DF")

    label("loc_6185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_67DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_622F")

    ChrTalk(
        0xFE,
        (
            "It looked like Vice Chief Pierre\x01",
            "was muttering something earlier.\x01",
            "I wonder if he's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't help but be\x01",
            "worried about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67DF")

    label("loc_622F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_676D")

    ChrTalk(
        0xFE,
        (
            "Guys, it looks like you\x01",
            "spoke with Vice Chief\x01",
            "Pierre.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is he all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FIt's hard to say whether\x01",
            "he's all right or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FWell, you could say he's\x01",
            "the same as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FBut I feel like he\x01",
            "wasn't as mean a person\x01",
            "before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see. Mean, huh...\x01",
            "Well, I guess that can't\x01",
            "be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, there's two\x01",
            "people in the police with\x01",
            "the title of vice chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the previous police chief\x01",
            "was dismissed, the other vice\x01",
            "chief was appointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThat's certainly how it\x01",
            "went down.\x02\x03",
            "We never agreed with\x01",
            "him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, the new chief... He's\x01",
            "practically Vice Chief Pierre's\x01",
            "junior. Did you know that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FThe chief is... the vice\x01",
            "chief's junior?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FI see, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I can only\x01",
            "imagine what Pierre thinks\x01",
            "of the chief right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To put it bluntly, I\x01",
            "think it was a reasonable\x01",
            "HR decision, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, he's the same vice chief... On top\x01",
            "of that, being passed by his subordinate\x01",
            "might be more than he can bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Certainly, it's\x01",
            "natural to feel that\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he's had it pretty\x01",
            "rough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say he opened his\x01",
            "heart when he came into\x01",
            "contact with you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you got scolded,\x01",
            "I think he worries about\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C2, 1)
    Jump("loc_67DF")

    label("loc_676D")


    ChrTalk(
        0xFE,
        (
            "Vice Chief Pierre must\x01",
            "have it tough if he\x01",
            "looks like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can be critical, but\x01",
            "we have to bear it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67DF")

    TalkEnd(0xFE)
    Return()

    # Function_30_6030 end

    def Function_31_67E3(): pass

    label("Function_31_67E3")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Listen up. There'll be a press\x01",
            "conference immediately after the first\x01",
            "half ends. Prepare the venue quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_31_67E3 end

    def Function_32_6863(): pass

    label("Function_32_6863")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Understood... Quickly\x01",
            "and reliably.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_32_6863 end

    def Function_33_689B(): pass

    label("Function_33_689B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now then, the\x01",
            "lunchboxes... *sigh*,\x01",
            "finally, something to eat.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_689B end

    def Function_34_68E6(): pass

    label("Function_34_68E6")

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
        "Good work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02110FLloyd and company! You came!\x02\x03",
            "#02102FAh, but the conference has finally started,\x01",
            "eh?\x02\x03",
            "The leaders of Crossbell State and the four\x01",
            "surrounding countries are all present! It's\x01",
            "an unprecedented international conference!\x02\x03",
            "And to top it off, it's being held at\x01",
            "Orchis Tower, the continent's very first\x01",
            "skyscraper!\x02\x03",
            "#02109FWith this must excitement and tension, this\x01",
            "girl's heart is gonna burst any second now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FExcitement aside, I\x01",
            "don't see how this is\x01",
            "tense at all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FYeah, you're the same\x01",
            "old Grace.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x103, 500)

    ChrTalk(
        0xC,
        (
            "#02105FAh, Tio! Even though it's been\x01",
            "a while, you're relentless\x01",
            "right out of the gate.\x02\x03",
            "#02104FI can't wait to write all of\x01",
            "this up... But that aside.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    ChrTalk(
        0xC,
        (
            "#02100FI'll introduce you,\x01",
            "Noticia. They are the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I see. I saw you in the\x01",
            "paper. Haha, you look\x01",
            "even better in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm Noticia from Liberl\x01",
            "News. Thanks for your\x01",
            "help today.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're happy to be of\x01",
            "service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThe Liberl News― It's\x01",
            "the largest paper in the\x01",
            "Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, and there's another\x01",
            "hot topic in the\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The reporters who won\x01",
            "the Fuelitzer Prize last\x01",
            "year are famous.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F38")

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha, that's the prize\x01",
            "that Nielsen was awarded\x01",
            "a long time ago, right?\x02\x03",
            "They say it's given to\x01",
            "the most outstanding\x01",
            "journalist each year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FAF")

    label("loc_6F38")


    ChrTalk(
        0x105,
        (
            "#12P#10300FThe Fuelitzer Prize...\x02\x03",
            "If I recall, it's an award to\x01",
            "honor the most outstanding\x01",
            "journalist each year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FAF")


    ChrTalk(
        0xE,
        "#5PHaha, you know it well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PBy the way, the names of\x01",
            "the winners were Nial\x01",
            "Burns and Dorothy Hyatt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PThey're the ace reporter\x01",
            "and genius cameraman of\x01",
            "our news agency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FOh, so last year's\x01",
            "winners were from Liberl\x01",
            "News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FPerhaps information related to the strange\x01",
            "phenomenon that occurred in Liberl last\x01",
            "year factored into the decision.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYes, it's as you\x01",
            "suspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PWell, strictly speaking, all\x01",
            "of their reporting up until\x01",
            "then factored in as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI see... They sound like\x01",
            "amazing reporters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FYeah. We can't lose to them again.\x02\x03",
            "#02103FAll reporters long for the Fuelitzer\x01",
            "Prize at least once in their\x01",
            "careers...\x02\x03",
            "To get that prize of tomorrow, it's\x01",
            "critical to go out and get that scoop\x01",
            "each and every day. Especially today!\x02\x03",
            "#02110FYou hear that Reins!? You've got to\x01",
            "do your best to outmaneuver the\x01",
            "others!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)

    ChrTalk(
        0xD,
        "Y-Yes ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Hmm... She's even more\x01",
            "fired up than usual.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F(I hope she behaves\x01",
            "herself, though...)\x02",
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

    # Function_34_68E6 end

    def Function_35_7404(): pass

    label("Function_35_7404")

    Sound(160, 0, 100, 0)
    Return()

    # Function_35_7404 end

    def Function_36_740B(): pass

    label("Function_36_740B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7433")
    SetScenarioFlags(0x146, 3)

    label("loc_7433")

    Return()

    # Function_36_740B end

    def Function_37_7434(): pass

    label("Function_37_7434")

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

    def lambda_75F4():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75F4)
    Sleep(50)

    def lambda_7604():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7604)
    Sleep(50)

    def lambda_7614():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7614)
    Sleep(50)

    def lambda_7624():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7624)
    Sleep(50)

    def lambda_7634():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7634)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#5P#00102F#10AAmazing!\x02",
    )

    CloseMessageWindow()
    OP_68(79000, 1000, -2700, 2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_769B():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_769B)
    Sleep(300)

    def lambda_76B8():
        OP_93(0xFE, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_76B8)

    def lambda_76C5():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76C5)
    Sleep(300)

    def lambda_76E2():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_76E2)
    Sleep(300)

    def lambda_76FF():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_76FF)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_7434 end

    def Function_38_7728(): pass

    label("Function_38_7728")

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

    # Function_38_7728 end

    def Function_39_7798(): pass

    label("Function_39_7798")


    def lambda_779D():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_779D)

    def lambda_77B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_77B7)
    WaitChrThread(0xFE, 1)

    def lambda_77CC():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77CC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_39_7798 end

    def Function_40_77ED(): pass

    label("Function_40_77ED")


    def lambda_77F2():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77F2)

    def lambda_780C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_780C)
    WaitChrThread(0xFE, 1)

    def lambda_7821():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7821)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#5P#00005F#8AAh...\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_40_77ED end

    def Function_41_787C(): pass

    label("Function_41_787C")


    def lambda_7881():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7881)

    def lambda_789B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_789B)
    WaitChrThread(0xFE, 1)

    def lambda_78B0():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_41_787C end

    def Function_42_78D1(): pass

    label("Function_42_78D1")


    def lambda_78D6():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78D6)

    def lambda_78F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_78F0)
    WaitChrThread(0xFE, 1)

    def lambda_7905():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7905)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_42_78D1 end

    def Function_43_7926(): pass

    label("Function_43_7926")


    def lambda_792B():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_792B)

    def lambda_7945():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7945)
    WaitChrThread(0xFE, 1)

    def lambda_795A():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_795A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_43_7926 end

    def Function_44_797B(): pass

    label("Function_44_797B")


    def lambda_7980():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7980)

    def lambda_799A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_799A)
    WaitChrThread(0xFE, 1)

    def lambda_79AF():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_44_797B end

    def Function_45_79D0(): pass

    label("Function_45_79D0")


    def lambda_79D5():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79D5)

    def lambda_79EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79EF)
    WaitChrThread(0xFE, 1)

    def lambda_7A04():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A04)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_45_79D0 end

    def Function_46_7A25(): pass

    label("Function_46_7A25")

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
        "#10109F#5PWhaaa~~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#5PWhat a view...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#5PMan, this is the best\x01",
            "scenery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02809F#5PHaha, it seems you're all\x01",
            "satisfied.\x02\x03",
            "#02800F─This is 34F. Once the\x01",
            "conference begins, staff will\x01",
            "be standing by on this floor.\x02\x03",
            "#02800FAlright then. Shall we have a\x01",
            "look around?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C4B():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7C4B)
    Sleep(50)

    def lambda_7C5B():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7C5B)
    Sleep(50)

    def lambda_7C6B():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7C6B)
    Sleep(50)

    def lambda_7C7B():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7C7B)
    Sleep(50)

    def lambda_7C8B():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7C8B)
    Sleep(50)

    def lambda_7C9B():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7C9B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    def lambda_7CC0():

        label("loc_7CC0")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7CC0")

    QueueWorkItem2(0x101, 2, lambda_7CC0)

    def lambda_7CD2():

        label("loc_7CD2")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7CD2")

    QueueWorkItem2(0x102, 2, lambda_7CD2)

    def lambda_7CE4():

        label("loc_7CE4")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7CE4")

    QueueWorkItem2(0x103, 2, lambda_7CE4)

    def lambda_7CF6():

        label("loc_7CF6")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7CF6")

    QueueWorkItem2(0x109, 2, lambda_7CF6)

    def lambda_7D08():

        label("loc_7D08")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7D08")

    QueueWorkItem2(0x105, 2, lambda_7D08)

    def lambda_7D1A():

        label("loc_7D1A")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7D1A")

    QueueWorkItem2(0x104, 2, lambda_7D1A)

    ChrTalk(
        0x101,
        (
            "#12P#00002FYes, please lead the\x01",
            "way.\x02",
        )
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

    def lambda_7D88():
        OP_97(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7D88)
    Sleep(100)

    def lambda_7DA5():
        OP_97(0x103, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7DA5)
    Sleep(100)

    def lambda_7DC2():
        OP_97(0x104, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7DC2)
    Sleep(100)

    def lambda_7DDF():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7DDF)
    Sleep(100)

    def lambda_7DFC():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7DFC)
    Sleep(100)

    def lambda_7E19():
        OP_97(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E19)
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

    def lambda_7F67():
        OP_95(0xFE, 8500, 0, -1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_7F67)

    def lambda_7F81():
        OP_96(0xFE, 0x2968, 0xFFFFFDA8, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7F81)

    def lambda_7F9B():
        OP_97(0x101, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7F9B)
    Sleep(50)

    def lambda_7FB8():
        OP_97(0x102, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7FB8)
    Sleep(50)

    def lambda_7FD5():
        OP_97(0x103, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7FD5)
    Sleep(50)

    def lambda_7FF2():
        OP_97(0x104, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7FF2)
    Sleep(50)

    def lambda_800F():
        OP_97(0x109, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_800F)
    Sleep(50)

    def lambda_802C():
        OP_97(0x105, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_802C)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_8052():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8052)
    Sleep(50)

    def lambda_8066():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8066)
    Sleep(500)

    def lambda_807A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_807A)
    Sleep(50)

    def lambda_808E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_808E)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x2D, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    ChrTalk(
        0x20,
        (
            "#6P#02803FThat is the security planning room.\x01",
            "The press room is right next door.\x02\x03",
            "#02800FIn the case of a terrorist\x01",
            "infiltration, a Guardian Force company\x01",
            "is standing by one floor below.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F#11PI heard about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PI bet they hand-picked\x01",
            "the best the CGF has to\x01",
            "offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PI wonder if Grace is\x01",
            "part of the press corps.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)

    ChrTalk(
        0x20,
        (
            "#6P#02805FOh, you mean the Crossbell Times\x01",
            "reporter?\x02\x03",
            "#02804FI remember she was on the list, so\x01",
            "she'll probably be here.\x02\x03",
            "#02800FBy the way, press are not to leave\x01",
            "this floor except during interviews\x01",
            "or the press conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F#11PI see, that's logical.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FSometimes, there are even rude\x01",
            "reporters who slip past security\x01",
            "for assault interviews.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FMore precisely, Grace is\x01",
            "the number one reporter\x01",
            "in that category.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah. Even if you find\x01",
            "her, she can't be\x01",
            "stopped.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x1F4)

    def lambda_8434():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8434)

    def lambda_844E():
        OP_97(0x101, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_844E)
    Sleep(50)

    def lambda_846B():
        OP_97(0x102, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_846B)
    Sleep(50)

    def lambda_8488():
        OP_97(0x103, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8488)
    Sleep(50)

    def lambda_84A5():
        OP_97(0x104, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_84A5)
    Sleep(50)

    def lambda_84C2():
        OP_97(0x109, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_84C2)
    Sleep(50)

    def lambda_84DF():
        OP_97(0x105, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_84DF)
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

    def lambda_8607():
        OP_97(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8607)

    def lambda_8621():
        OP_98(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8621)

    def lambda_863B():
        OP_97(0x101, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_863B)
    Sleep(50)

    def lambda_8658():
        OP_97(0x102, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8658)
    Sleep(50)

    def lambda_8675():
        OP_97(0x103, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8675)
    Sleep(50)

    def lambda_8692():
        OP_97(0x104, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8692)
    Sleep(50)

    def lambda_86AF():
        OP_97(0x109, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_86AF)
    Sleep(50)

    def lambda_86CC():
        OP_97(0x105, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_86CC)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x10E, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    ChrTalk(
        0x20,
        (
            "#02800F#11PI think I'll show you\x01",
            "this room, just in case.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-14000, 1000, 17400, 1000)
    FadeToDark(1000, 0, -1)

    def lambda_8755():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8755)
    Sleep(50)

    def lambda_8765():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8765)

    def lambda_8772():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8772)
    Sleep(50)

    def lambda_8782():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8782)

    def lambda_878F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_878F)
    Sleep(50)

    def lambda_879F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_879F)
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
        "#11P#10302FOh... How magnificent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00002FIt's like a break room,\x01",
            "but it's so open...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02804FThis is the break room I've\x01",
            "prepared for those involved\x01",
            "in the conference.\x02\x03",
            "#02800FDuring breaks, please feel\x01",
            "free to make use of it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_89CB():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_89CB)
    Sleep(50)

    def lambda_89DB():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_89DB)
    Sleep(50)

    def lambda_89EB():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_89EB)
    Sleep(50)

    def lambda_89FB():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_89FB)
    Sleep(50)

    def lambda_8A0B():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8A0B)
    Sleep(50)

    def lambda_8A1B():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8A1B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#6P#00004FWe will, and thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHaha, maybe we should\x01",
            "have tea later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02809FNow then, I think it's\x01",
            "time I showed you the\x01",
            "next floor.\x02",
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

    def lambda_8BCD():
        OP_95(0xFE, -13000, 0, 1800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8BCD)

    def lambda_8BE7():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8BE7)

    def lambda_8C01():
        OP_97(0x101, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8C01)
    Sleep(50)

    def lambda_8C1E():
        OP_97(0x102, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8C1E)
    Sleep(50)

    def lambda_8C3B():
        OP_97(0x103, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8C3B)
    Sleep(50)

    def lambda_8C58():
        OP_97(0x104, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8C58)
    Sleep(50)

    def lambda_8C75():
        OP_97(0x109, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8C75)
    Sleep(50)

    def lambda_8C92():
        OP_97(0x105, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8C92)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)

    def lambda_8CBA():
        OP_95(0xFE, -14800, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8CBA)
    WaitChrThread(0x27, 1)
    OP_6B(0xFF)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_8CF4():

        label("loc_8CF4")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8CF4")

    QueueWorkItem2(0x101, 2, lambda_8CF4)
    WaitChrThread(0x102, 0)

    def lambda_8D0A():

        label("loc_8D0A")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8D0A")

    QueueWorkItem2(0x102, 2, lambda_8D0A)
    WaitChrThread(0x103, 0)

    def lambda_8D20():

        label("loc_8D20")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8D20")

    QueueWorkItem2(0x103, 2, lambda_8D20)
    WaitChrThread(0x104, 0)

    def lambda_8D36():

        label("loc_8D36")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8D36")

    QueueWorkItem2(0x104, 2, lambda_8D36)
    WaitChrThread(0x20, 1)

    def lambda_8D4C():
        OP_95(0xFE, -17600, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8D4C)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_8D6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_8D6F)
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
            "#12P#00005FThese are... emergency\x01",
            "stairs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FIt looks like the ones\x01",
            "going down are sealed,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02803F#5PNormally, you can go down to\x01",
            "1F using these stairs.\x02\x03",
            "#02801FHowever, during the\x01",
            "conference, all floors except\x01",
            "34, 35 and 36F will be sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI see. So it's for\x01",
            "security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FBut, what will you do in\x01",
            "the event of an\x01",
            "earthquake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02806F#5PIn that case, all\x01",
            "emergency stairs will\x01",
            "automatically open.\x02\x03",
            "#02800FWell, they say perfect\x01",
            "security is impossible,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... We'll need to\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00208F...It seems there's a\x01",
            "need to think of hacking\x01",
            "countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02804F#5PNow then. Since we're\x01",
            "here, let's use the\x01",
            "stairs.\x02\x03",
            "#02800FWelcome to 35F─ The\x01",
            "conference floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_7A25 end

    def Function_47_928B(): pass

    label("Function_47_928B")

    OP_92(0xFE, 0x128E0, 0x0, 0x1F4)

    def lambda_929D():
        OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_929D)
    WaitChrThread(0xFE, 1)

    def lambda_92BB():
        OP_95(0xFE, 68000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92BB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_928B end

    def Function_48_92D5(): pass

    label("Function_48_92D5")


    def lambda_92DA():
        OP_95(0xFE, -14800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92DA)
    WaitChrThread(0xFE, 1)

    def lambda_92F8():
        OP_95(0xFE, -17600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_92F8)
    Sleep(300)

    def lambda_9315():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9315)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_92D5 end

    def Function_49_9326(): pass

    label("Function_49_9326")


    def lambda_932B():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_932B)

    def lambda_9345():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9345)
    WaitChrThread(0xFE, 1)

    def lambda_935A():
        OP_95(0xFE, -55000, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_935A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_49_9326 end

    def Function_50_937B(): pass

    label("Function_50_937B")


    def lambda_9380():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9380)

    def lambda_939A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_939A)
    WaitChrThread(0xFE, 1)

    def lambda_93AF():
        OP_95(0xFE, -53500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93AF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_50_937B end

    def Function_51_93D0(): pass

    label("Function_51_93D0")


    def lambda_93D5():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93D5)

    def lambda_93EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_93EF)
    WaitChrThread(0xFE, 1)

    def lambda_9404():
        OP_95(0xFE, -54500, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9404)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_51_93D0 end

    def Function_52_9425(): pass

    label("Function_52_9425")


    def lambda_942A():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_942A)

    def lambda_9444():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9444)
    WaitChrThread(0xFE, 1)

    def lambda_9459():
        OP_95(0xFE, -53000, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9459)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_52_9425 end

    def Function_53_947A(): pass

    label("Function_53_947A")


    def lambda_947F():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_947F)

    def lambda_9499():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9499)
    WaitChrThread(0xFE, 1)

    def lambda_94AE():
        OP_95(0xFE, -51500, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_94AE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_53_947A end

    def Function_54_94CF(): pass

    label("Function_54_94CF")


    def lambda_94D4():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_94D4)

    def lambda_94EE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_94EE)
    WaitChrThread(0xFE, 1)

    def lambda_9503():
        OP_95(0xFE, -51500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9503)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_94CF end

    def Function_55_9524(): pass

    label("Function_55_9524")

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
            "#11P#00000FAlright... This\x01",
            "completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make another\x01",
            "loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FRight...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor\x01",
            "and the Chairman are doing\x01",
            "their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the Blood\x01",
            "and Iron Chancellor and\x01",
            "President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should\x01",
            "ask someone about it\x01",
            "during the break.\x02",
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

    # Function_55_9524 end

    def Function_56_97FD(): pass

    label("Function_56_97FD")

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
            "#11P#00000FAlright... This\x01",
            "completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make another\x01",
            "loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FRight...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor\x01",
            "and the Chairman are doing\x01",
            "their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the Blood\x01",
            "and Iron Chancellor and\x01",
            "President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should\x01",
            "ask someone about it\x01",
            "during the break.\x02",
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

    # Function_56_97FD end

    def Function_57_9AD6(): pass

    label("Function_57_9AD6")

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
            "During this time, Lloyd and the others had\x01",
            "a chance to speak with Lawyer Ian, who had\x01",
            "started his break ahead of the others.\x07\x00\x02",
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
            "#02205F#5PI see... Because of the\x01",
            "current situation, all of you\x01",
            "are assisting with security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00002FYeah... Though honestly,\x01",
            "it might just be for\x01",
            "peace of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PNo, no, you guys made a huge\x01",
            "showing in the mayoral\x01",
            "assassination attempt incident.\x02\x03",
            "#02200FIt's very reassuring knowing\x01",
            "that you guys are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00104FThank you for saying\x01",
            "so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHaha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#11PLawyer Ian, how is the\x01",
            "conference going?\x02\x03",
            "It hasn't seemed rough\x01",
            "thus far, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PWell, so far so good.\x02\x03",
            "The respective nations\x01",
            "have already agreed to\x01",
            "several trade deals.\x02\x03",
            "#02200FIt seems Mayor Dieter\x01",
            "won't have called this\x01",
            "conference for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102FHaha, is that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FThat makes me feel a\x01",
            "little better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FBut you said "So far so\x01",
            "good." Is there something\x01",
            "you're concerned about?\x02",
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
        "#11P#00105FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00001F...Well is there?\x02",
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
            "#02203F#5PHmm. I'm not sure if I should\x01",
            "be saying this as an observer,\x01",
            "but...\x02\x03",
            "The first half has been almost\x01",
            "all trade, finance, and other\x01",
            "economy-related proposals.\x02\x03",
            "#02201F─But the second half is\x01",
            "comprised of proposals from\x01",
            "each country's head of state.\x02\x03",
            "And what's more, it seems the\x01",
            "security of Crossbell will\x01",
            "come up.\x02",
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
        "#11P#00013FThat's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F...Security, eh? Then\x01",
            "that means military force\x01",
            "will enter the equation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FBut, wasn't that Non-\x01",
            "Aggression Pact signed\x01",
            "two years ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PThe Queen of Liberl proposed it\x01",
            "due to the dangerous situation\x01",
            "in Crossbell at that time.\x02\x03",
            "And, neither Remiferia nor\x01",
            "Crossbell itself were involved\x01",
            "in that Non-Aggression Pact.\x02\x03",
            "#02201FIn addition, it's certain that\x01",
            "a new security framework is\x01",
            "needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106F...Certainly. My\x01",
            "grandfather is worried\x01",
            "about that, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#11PThen, they just need to\x01",
            "sign a new treaty involving\x01",
            "Crossbell as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right. A framework where solving\x01",
            "international conflicts through use of\x01",
            "military force is prohibited, just like\x01",
            "in the non-aggression pact.\x02\x03",
            "#10105F─Ah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FI see... Crossbell is not\x01",
            "a "nation".\x02\x03",
            "#00008FIt is recognized by the\x01",
            "Empire and Republic only\x01",
            "as an "autonomous state".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PThat's right. I'm saying that Crossbell\x01",
            "lacks the national sovereignty necessary\x01",
            "to enter into an "international treaty".\x02\x03",
            "Even if economic "agreements" are made,\x01",
            "that alone does not give standing to\x01",
            "enter into "treaties".\x02\x03",
            "#02201FSo now you see. That's the reason\x01",
            "discussion of Crossbell's security is so\x01",
            "terribly dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FThat's quite complex. I\x01",
            "feel like I understand\x01",
            "now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11PExcuse me, may I ask\x01",
            "something?\x02\x03",
            "#00203FThere are other\x01",
            "independent states\x01",
            "besides Crossbell.\x02\x03",
            "Lｳman, Ored, North\x01",
            "Ambria...\x02\x03",
            "#00200FIs it true that those\x01",
            "states also cannot agree\x01",
            "to treaties?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PNo, that's not the case.\x02\x03",
            "#02200FIt's true that each of those\x01",
            "states has its own reasons for\x01",
            "not having formed a nation.\x02\x03",
            "However, each of them has been\x01",
            "recognized by a "suzerain state"\x01",
            "as having equal soverignty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FSuzerain states...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00103FThose other autonomous states\x01",
            "are definitely different from\x01",
            "Crossbell in that regard.\x02\x03",
            "#00101FThose statuses were\x01",
            "recognized by the Holy Nation\x01",
            "of Arteria.\x02",
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
        "#00205F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10305FThe Holy Nation of Arteria\x01",
            "is the seat of the Septian\x01",
            "Church, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00104FYes. Though their territory\x01",
            "is small, they have\x01",
            "religious authority.\x02\x03",
            "#00100FMany independent states and\x01",
            "free cities rely on them to\x01",
            "become independent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FHowever, Crossbell is recognized\x01",
            "as a "autonomous state" by the\x01",
            "Empire and Republic.\x02\x03",
            "#00001FIt's almost as if we have two\x01",
            "suzerain states.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FYes. And historically, that\x01",
            "fact has pulled us into various\x01",
            "disasters.\x02\x03",
            "If Crossbell was given a little\x01",
            "more sovereignty, the situation\x01",
            "would change a little.\x02\x03",
            "#00106FBut if it's those two countries\x01",
            "that have to agree on it, it'll\x01",
            "never happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PIt makes you want to\x01",
            "give up, doesn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5P─Getting back to the main issue, it\x01",
            "seems the Chancellor and the President\x01",
            "each have their own security proposals.\x02\x03",
            "Naturally, the terms regarding each of\x01",
            "the countries aren't the same.\x02\x03",
            "#02201FThe chairman and mayor will need to be\x01",
            "vigilant and emphasize that.\x02",
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
            "#02210F#5PHaha, sorry. It seems\x01",
            "I've made you worry.\x02\x03",
            "#02200FWell, Chairman MacDowell\x01",
            "is used to this sort of\x01",
            "thing.\x02\x03",
            "And it seems Mayor\x01",
            "Dieter has some kind of\x01",
            "plan.\x02",
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
        "#11P#00005FA plan, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FWhat could it be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PAh, well I have haven't\x01",
            "heard the details\x01",
            "myself, but─\x02",
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
        "#11P#00000F─Excuse me.\x02",
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
            "#00008FSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3455V#30W─Bannings. The press\x01",
            "conference is over.\x02\x03",
            "#3456VThe heads of state are\x01",
            "heading for their 36F break\x01",
            "rooms. Where are you guys?\x02",
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
            "#00005FAh, right. We're in the\x01",
            "34F break room.\x02\x03",
            "#00001F...Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually, we got an offer\x01",
            "from both Chancellor Osborne\x01",
            "and President Rocksmith.\x02\x03",
            "─It seems each of them would\x01",
            "like to speak with you\x01",
            "directly during the break.\x02",
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
            "#00011F#4SWha...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Being who they are, I can't very\x01",
            "well turn them down.\x02\x03",
            "I want you to visit each leader's\x01",
            "room during the break.\x02\x03",
            "The deepest room in the left wing\x01",
            "is the President's and the one in\x01",
            "the right in the chancellor's.\x02",
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
            "#00006FW-Wait a minute! Why in\x01",
            "the world...\x02\x03",
            "#00011FIt's way too much\x01",
            "responsibility!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Don't be naｼve,\x01",
            "Bannings.\x02\x03",
            "Isn't this a good chance\x01",
            "to look into the motives\x01",
            "of both sides?\x02",
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
            "#00005F!!\x02\x03",
            "#00003F...I understand. We'll\x01",
            "head for their rooms\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you get into trouble, leave\x01",
            "everything to Elie. She's used\x01",
            "to dealing with VIPs.\x02\x03",
            "Once you're finished, come\x01",
            "report to me.\x02",
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
            "#00001FUnderstood!\x02",
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
        "#11P#00101FLloyd, that was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FYou were all over the\x01",
            "place. Is something\x01",
            "going on?\x02",
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
        "#5P#00003FYeah...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they had received\x01",
            "invitations to speak with Chancellor\x01",
            "Osborne and President Rocksmith.\x07\x00\x02",
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
        "#12P#10111FWhaaaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FWhoa, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11PIt seems it's no joke...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02205F#5PDear me... How surprising.\x02\x03",
            "#02210FIt seems the name of the\x01",
            "Special Support Section is more\x01",
            "well-known than I thought.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's not it... It's just that\x01",
            "there are friends of ours among\x01",
            "each of the leaders' staffs.\x02\x03",
            "#00008FThey might have taken an\x01",
            "interest in us due to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FI see... That's probably\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F...Even if that is the\x01",
            "reason, it's not like we\x01",
            "can refuse.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006FYou're right. Let's head to\x01",
            "the deepest rooms of the\x01",
            "left and right wings of 36F.\x02\x03",
            "#00001FWe're visiting with them\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#11PRoger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FY-Yes, sir!\x02",
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

    # Function_57_9AD6 end

    def Function_58_BED7(): pass

    label("Function_58_BED7")

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
        "#6PW-What's this!?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        "#12PW-Why did it suddenly...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)

    ChrTalk(
        0xB,
        "#12PWhat? What's happening!?\x02",
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
            "#11PIt's no good! Even if I\x01",
            "push the button, there's\x01",
            "no response!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PUgh... What the heck is\x01",
            "happening here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02105F#11PHey! What about my\x01",
            "scoop!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        "#02101F#5PReins, do something!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 500)

    ChrTalk(
        0xD,
        (
            "#12PP-Please don't ask the\x01",
            "impossible!\x02",
        )
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

    # Function_58_BED7 end

    def Function_59_C43A(): pass

    label("Function_59_C43A")

    Sleep(600)

    def lambda_C442():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C442)

    def lambda_C45C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C45C)
    WaitChrThread(0xFE, 1)

    def lambda_C471():
        OP_95(0xFE, -51100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C471)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_59_C43A end

    def Function_60_C492(): pass

    label("Function_60_C492")


    def lambda_C497():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C497)

    def lambda_C4B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C4B1)
    WaitChrThread(0xFE, 1)

    def lambda_C4C6():
        OP_95(0xFE, -52700, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4C6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_60_C492 end

    def Function_61_C4E7(): pass

    label("Function_61_C4E7")

    Sleep(1200)

    def lambda_C4EF():
        OP_95(0xFE, -52000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4EF)

    def lambda_C509():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C509)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_61_C4E7 end

    def Function_62_C521(): pass

    label("Function_62_C521")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C52E():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C52E)

    def lambda_C548():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C548)
    WaitChrThread(0xFE, 1)

    def lambda_C55D():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C55D)
    WaitChrThread(0xFE, 1)

    def lambda_C57B():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C57B)
    WaitChrThread(0xFE, 1)

    def lambda_C599():
        OP_95(0xFE, -53800, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C599)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Return()

    # Function_62_C521 end

    def Function_63_C5C5(): pass

    label("Function_63_C5C5")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C5D5():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C5D5)

    def lambda_C5EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C5EF)
    WaitChrThread(0xFE, 1)

    def lambda_C604():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C604)
    WaitChrThread(0xFE, 1)

    def lambda_C622():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C622)
    WaitChrThread(0xFE, 1)

    def lambda_C640():
        OP_95(0xFE, -54200, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C640)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_63_C5C5 end

    def Function_64_C669(): pass

    label("Function_64_C669")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C679():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C679)

    def lambda_C693():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C693)
    WaitChrThread(0xFE, 1)

    def lambda_C6A8():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6A8)
    WaitChrThread(0xFE, 1)

    def lambda_C6C6():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6C6)
    WaitChrThread(0xFE, 1)

    def lambda_C6E4():
        OP_95(0xFE, -55100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6E4)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_64_C669 end

    def Function_65_C70D(): pass

    label("Function_65_C70D")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C71D():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C71D)

    def lambda_C737():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C737)
    WaitChrThread(0xFE, 1)

    def lambda_C74C():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C74C)
    WaitChrThread(0xFE, 1)

    def lambda_C76A():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C76A)
    WaitChrThread(0xFE, 1)

    def lambda_C788():
        OP_95(0xFE, -55800, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C788)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_65_C70D end

    def Function_66_C7B1(): pass

    label("Function_66_C7B1")

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
        "#00011FCryptids, you say?\x02",
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
            "Yes, exactly.\x02\x03",
            "I'm hesitant to call them simple\x01",
            "monsters, as they are large and\x01",
            "mysterious.\x02\x03",
            "Monsters like that are appearing\x01",
            "all over Crossbell.\x02",
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

    def lambda_CC2C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_CC2C)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x1, 0xA, 0x0, 0x0)
    OP_79(0x11)

    def lambda_CC50():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_CC50)
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
            "#11PAh... So that's what I\x01",
            "saw!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PIn the end, it ran away\x01",
            "before we could finish\x01",
            "it off...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10101F#12P#NA monster like that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00206F#12P#NInformation like that\x01",
            "has come in, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x26,
        (
            "#5PThat's not all. Other\x01",
            "types have been\x01",
            "detected.\x02",
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
        "#6P#N#00007FT-This is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#6P#N#00101FThat thing that appeared\x01",
            "in the old mine!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#12P#NWhoa, it showed up\x01",
            "again!?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x26, 0xE1, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x26,
        (
            "#5PA few days ago, one of the\x01",
            "same type appeared in the\x01",
            "northern mountain district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PScott and Wenzel here\x01",
            "already exterminated it.\x02",
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
        "#6P#00006FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10105F#12P#NYou beat it with just\x01",
            "the two of you?\x02",
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
            "#5PYeah, we took it by\x01",
            "surprise and managed to\x01",
            "defeat it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#5PIt was all thanks to\x01",
            "these guys' info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11PIt's just, it had a very\x01",
            "strange response.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11POn top of arts' effect\x01",
            "on it, it disappeared\x01",
            "into a beam of light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FAs I thought...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#6P#NThat's what happened\x01",
            "when we fought it\x01",
            "exactly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10303F#12P#NSpeaking of the mountain\x01",
            "district...\x02\x03",
            "#10301FDid it appear outdoors\x01",
            "this time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D1EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D1EC)
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
            "#02006F#5PYes. Until now, they've been detected\x01",
            "only in places with spatial\x01",
            "distortions like the Tower or Temple.\x02\x03",
            "We think they appear only in these\x01",
            ""spatial distortions" for some\x01",
            "reason.\x02\x03",
            "#02001FHowever, these Cryptids appeared in\x01",
            "the mountain and marsh districts.\x02\x03",
            "It's possible that these "spatial\x01",
            "distortions" are appearing outdoors\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#12P#NN-No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x23,
        (
            "#11PThat's the last thing I\x01",
            "wanted to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PSo, that's the reason\x01",
            "you called us here?\x02",
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
            "#5PYes. We are requesting the Bracer\x01",
            "Guild and Special Support Section\x01",
            "both to deal with these cryptids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PEver since the independence proposal,\x01",
            "Bellguard and Tangram have been\x01",
            "continuously in a state of high alert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PWe've got to maintain\x01",
            "that at least until the\x01",
            "referendum is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F#NUnderstood. Allow us to\x01",
            "accept, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#12PShould we decide how to\x01",
            "divide things amongst\x01",
            "ourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#02004F#5PYes. I'll provide you\x01",
            "the data and then leave\x01",
            "it to you.\x02\x03",
            "#02001FAnd... If possible, I'd\x01",
            "like you to find the\x01",
            "specific "cause".\x02",
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
            "#12P#N#00205FCause?\x02\x03",
            "#00200FYou mean why those\x01",
            "Cryptids have suddenly\x01",
            "appeared?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x25,
        (
            "#02003F#5PYes. For a long time, monsters have\x01",
            "appeared in fixed cycles, but...\x02\x03",
            "#02001FIt's no exaggeration to say these\x01",
            "Cryptids represent an "abnormal\x01",
            "situation" with respect to those cycles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PThere must be some sort\x01",
            "of cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PWe mean the cause of these "spatial\x01",
            "distortions" that give rise to\x01",
            "these unusually large monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#6P#NI see.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#11PBy the name of the\x01",
            "guild, I swear we'll\x01",
            "solve this.\x02",
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

    # Function_66_C7B1 end

    def Function_67_D9B6(): pass

    label("Function_67_D9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD59")
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
            "How many times do I have to\x01",
            "tell you!? Members of the\x01",
            "press corps may not pass!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12PBut we're on break right\x01",
            "now... Can we look over\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6PYes. Except for\x01",
            "pictures, we haven't\x01",
            "done anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PThat's right. If not,\x01",
            "I'll get Grace...\x02",
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
        0x101,
        (
            "#6P#00012FThey'll go even though\x01",
            "they know it's not\x01",
            "allowed.\x02\x03",
            "#00003FIt doesn't seem like\x01",
            "they'll forcibly break\x01",
            "through though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FThat's just how\x01",
            "reporters are, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FAnyway... It doesn't\x01",
            "look like we're getting\x01",
            "through.\x02",
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
    Jump("loc_DDEC")

    label("loc_DD59")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reporters are blocking\x01",
            "the way to the elevator\x01",
            "floor.\x02\x03",
            "It doesn't seem like\x01",
            "you'll be able to pass\x01",
            "for a while.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x4)

    label("loc_DDEC")

    Return()

    # Function_67_D9B6 end

    def Function_68_DDED(): pass

    label("Function_68_DDED")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A1")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00005FThat's right. During the conference,\x01",
            "we can't use any elevators except\x01",
            "that first one, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It must be that way\x01",
            "for security reasons.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_DFAA")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the emergency\x01",
            "stairs, it seems this too is\x01",
            "controlled via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, looks that way.\x02\x03",
            "#00000FWhatever. When we need\x01",
            "to move, let's use that\x01",
            "first elevator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E099")

    label("loc_DFAA")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, it seems the\x01",
            "lock mechanism is controlled\x01",
            "via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, I should expect\x01",
            "that much from the Orchis\x01",
            "Tower security system.\x02\x03",
            "#00000FWhatever. When we need to\x01",
            "move, let's use that\x01",
            "first elevator.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E099")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_E113")

    label("loc_E0A1")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x02\x03",
            "It seems you can't use\x01",
            "this elevator during the\x01",
            "conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E113")

    TalkEnd(0xFF)
    Return()

    # Function_68_DDED end

    def Function_69_E117(): pass

    label("Function_69_E117")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E39B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs'\x01",
            "shutter is firmly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F33F is this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe were told it would be\x01",
            "sealed during the\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_E2BD")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the elevator, it\x01",
            "seems this these too are\x01",
            "controlled via the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPerfect security is\x01",
            "impossible― I remember\x01",
            "hearing that.\x02\x03",
            "#00001FWe've got to keep that\x01",
            "in the back of our\x01",
            "minds, just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E393")

    label("loc_E2BD")


    ChrTalk(
        0x103,
        (
            "#00200FIt seems the shutter\x01",
            "lock is controlled via\x01",
            "the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPerfect security is\x01",
            "impossible― I remember\x01",
            "hearing that.\x02\x03",
            "#00001FWe've got to keep that\x01",
            "in the back of our\x01",
            "minds, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E393")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_E41C")

    label("loc_E39B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs'\x01",
            "shutter is firmly shut.\x02\x03",
            "It seems you can't\x01",
            "proceed to the next floor\x01",
            "during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E41C")

    TalkEnd(0xFF)
    Return()

    # Function_69_E117 end

    def Function_70_E420(): pass

    label("Function_70_E420")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_70_E420 end

    SaveToFile()

Try(main)
