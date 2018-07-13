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
        "Master Sgt. Giselle",    # 20
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
        "Function_4_1446",         # 04, 4
        "Function_5_188A",         # 05, 5
        "Function_6_1C46",         # 06, 6
        "Function_7_25C3",         # 07, 7
        "Function_8_27E7",         # 08, 8
        "Function_9_28F0",         # 09, 9
        "Function_10_2A8B",        # 0A, 10
        "Function_11_2BE6",        # 0B, 11
        "Function_12_3066",        # 0C, 12
        "Function_13_32B7",        # 0D, 13
        "Function_14_34C5",        # 0E, 14
        "Function_15_3743",        # 0F, 15
        "Function_16_38CF",        # 10, 16
        "Function_17_3F55",        # 11, 17
        "Function_18_40BD",        # 12, 18
        "Function_19_44F0",        # 13, 19
        "Function_20_465C",        # 14, 20
        "Function_21_4941",        # 15, 21
        "Function_22_4AAE",        # 16, 22
        "Function_23_4BA5",        # 17, 23
        "Function_24_4D87",        # 18, 24
        "Function_25_53A2",        # 19, 25
        "Function_26_556A",        # 1A, 26
        "Function_27_59B5",        # 1B, 27
        "Function_28_5F76",        # 1C, 28
        "Function_29_61C4",        # 1D, 29
        "Function_30_61F3",        # 1E, 30
        "Function_31_69C8",        # 1F, 31
        "Function_32_6A48",        # 20, 32
        "Function_33_6A81",        # 21, 33
        "Function_34_6ACC",        # 22, 34
        "Function_35_7646",        # 23, 35
        "Function_36_764D",        # 24, 36
        "Function_37_7676",        # 25, 37
        "Function_38_796C",        # 26, 38
        "Function_39_79DC",        # 27, 39
        "Function_40_7A31",        # 28, 40
        "Function_41_7AC0",        # 29, 41
        "Function_42_7B15",        # 2A, 42
        "Function_43_7B6A",        # 2B, 43
        "Function_44_7BBF",        # 2C, 44
        "Function_45_7C14",        # 2D, 45
        "Function_46_7C69",        # 2E, 46
        "Function_47_9504",        # 2F, 47
        "Function_48_954E",        # 30, 48
        "Function_49_959F",        # 31, 49
        "Function_50_95F4",        # 32, 50
        "Function_51_9649",        # 33, 51
        "Function_52_969E",        # 34, 52
        "Function_53_96F3",        # 35, 53
        "Function_54_9748",        # 36, 54
        "Function_55_979D",        # 37, 55
        "Function_56_9A78",        # 38, 56
        "Function_57_9D53",        # 39, 57
        "Function_58_C174",        # 3A, 58
        "Function_59_C6DC",        # 3B, 59
        "Function_60_C734",        # 3C, 60
        "Function_61_C789",        # 3D, 61
        "Function_62_C7C3",        # 3E, 62
        "Function_63_C867",        # 3F, 63
        "Function_64_C90B",        # 40, 64
        "Function_65_C9AF",        # 41, 65
        "Function_66_CA53",        # 42, 66
        "Function_67_DC8F",        # 43, 67
        "Function_68_E0CF",        # 44, 68
        "Function_69_E415",        # 45, 69
        "Function_70_E71A",        # 46, 70
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
            "It looks like the reporters have finally\x01",
            "given up on trying to get to the floor above.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. I don't know if it's\x01",
            "because of their job or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pushiness of reporters is the same\x01",
            "no matter what country you go to.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_126F")

    label("loc_11E4")


    ChrTalk(
        0xFE,
        (
            "*sigh*. I don't know if it's\x01",
            "because of their job or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The pushiness of reporters is the same\x01",
            "no matter what country you go to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126F")

    Jump("loc_1442")

    label("loc_1274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1282")
    Jump("loc_1442")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(
        0xFE,
        (
            "This is the waiting room for\x01",
            "journalists from all countries.\x02",
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
            "Everyone is gathered inside. Please,\x01",
            "feel free to enter and confirm that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1442")

    label("loc_1397")


    ChrTalk(
        0xFE,
        (
            "This is the waiting room for\x01",
            "journalists from all countries.\x02",
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

    label("loc_1442")

    TalkEnd(0xFE)
    Return()

    # Function_3_10DF end

    def Function_4_1446(): pass

    label("Function_4_1446")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_145A")
    Call(0, 6)
    Jump("loc_1886")

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CC")

    ChrTalk(
        0xC,
        (
            "#02100FOh, Lloyd and friends. It looks\x01",
            "like the security's all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FFine. Well, at least it is right now.\x02\x03",
            "How is your coverage\x01",
            "going, Miss Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02102FUh uh, about that. Thankfully,\x01",
            "we're getting great results.\x02\x03",
            "By the way, I'm thinking of writing a\x01",
            "more positive article than I thought.\x02\x03",
            "#02109FIt would be nice if I had more material\x01",
            "aimed at the general public, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FUmm, I think I understand, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FPlease don't show up anywhere\x01",
            "you're not supposed to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02104FIt's fine! In that\x01",
            "department, Reins will be―\x02\x03",
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
        "#00106F(Yes, I'm worried too...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 1)
    Jump("loc_185F")

    label("loc_17CC")


    ChrTalk(
        0xC,
        (
            "#02109FI'll be sure to\x01",
            "follow the rules.\x02\x03",
            "#02100FNow then, I think I'll head to\x01",
            "the break room after getting in\x01",
            "contact with the news agency.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185F")

    Jump("loc_1886")

    label("loc_1864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1883")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_1883")

    Call(0, 5)

    label("loc_1886")

    TalkEnd(0xFE)
    Return()

    # Function_4_1446 end

    def Function_5_188A(): pass

    label("Function_5_188A")

    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1D")

    ChrTalk(
        0xC,
        (
            "#02100FAnd, what about Mr. Nial\x01",
            "and Dorothy coming here?\x02",
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
            "It's not a good situation\x01",
            "over there, in its own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02103FI see. It's between those\x01",
            "nationalists and extremists, right?\x02\x03",
            "#02101FI happened to hear that maybe\x01",
            "they'll do some kind of move\x01",
            "during the Trade Conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hu hu. You too aren't being\x01",
            "a reporter just for show, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I have indeed heard that. \x01",
            "There's no hard evidence, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(So Miss Grace knows\x01",
            "even that...)\x02",
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
    Jump("loc_1C3D")

    label("loc_1B1D")


    ChrTalk(
        0xC,
        (
            "#02100FThat's right, Miss Noticia. \x01",
            "If you run into Mr. Nial, please\x01",
            "tell him the following for me.\x02\x03",
            ""Congratulations on winning\x01",
            "the Fulitzer Prize. I will be\x01",
            "taking the next one for sure."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh. I heard you\x01",
            "were an acquaintance\x01",
            "of Nial's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, I'll be sure to tell him.\x02",
    )

    CloseMessageWindow()

    label("loc_1C3D")

    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_5_188A end

    def Function_6_1C46(): pass

    label("Function_6_1C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E34")

    ChrTalk(
        0x1F,
        (
            "#11505FI see. So Mr. Beardy-Bear is\x01",
            "of the coffee faction, huh.\x02\x03",
            "#11500FI think you'd get along with the Chancellor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02200FHmm. Does His Grace drink coffee often?\x02",
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
        "#02109FUh uh. Indeed, it makes sense.\x02",
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
            "#00206F(Yes... \x01",
            "It's quite intense.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 2)
    Jump("loc_25C2")

    label("loc_1E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2248")

    ChrTalk(
        0xC,
        (
            "#02104FHmm. Chancellor Osborne is of\x01",
            "the coffee faction, you said...\x02\x03",
            "#02100FThen, which are you, Mr. Lechter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11510FHmm. If I had to say, I myself\x01",
            "am of the black tea faction.\x02\x03",
            "#11500FBut... What are you planning, asking the\x01",
            "preferences of a mere Second Secretary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FWeeell, since you don quite the\x01",
            "generous mask, I was thinking to\x01",
            "try to get something before the others...\x02\x03",
            "#02102FAfter all, a handsome man and beautiful woman\x01",
            "alone are enough to make a fine article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11509FHa ha, I see. I'm\x01",
            "happy to hear that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 0)), scpexpr(EXPR_END)), "loc_2154")

    ChrTalk(
        0x101,
        (
            "#00006F(Hmm. I feel like this conversation\x01",
            "is an obvious front.)\x02\x03",
            "#00001F(It seems Miss Grace too\x01",
            "figured out Mr. Lechter\x01",
            "to a certain degree...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu. I guess they're mixing truth\x01",
            "and lies to sound each other out?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2240")

    label("loc_2154")


    ChrTalk(
        0x101,
        (
            "#00006F(Hmm. I feel like this conversation\x01",
            "is an obvious front.)\x02\x03",
            "#00001F(I'm sure Miss Grace too\x01",
            "knows that Lechter isn't\x01",
            "just some secretary...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu. I guess they're mixing truth\x01",
            "and lies to sound each other out?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2240")

    SetScenarioFlags(0x1C1, 3)
    Jump("loc_25C2")

    label("loc_2248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E3")

    ChrTalk(
        0x1F,
        (
            "#11501FThat's right. Actually,\x01",
            "there's something I want to\x01",
            "discuss with Mr. Beardy-Bear.\x02",
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
            "#11506FAh, just some worries\x01",
            "about my workplace.\x02\x03",
            "I'd like to ask the opinion\x01",
            "of Mr. Beardy-Bear, famous\x01",
            "for his work on human rights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02202FI see... Well it's obviously\x01",
            "impossible now, though.\x02\x03",
            "If you like, please contact\x01",
            "my office another time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lawyer Ian presented Secretary\x01",
            "Lechter with his business card.\x07\x00\x02",
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
            "#00001F(I see. So he's expanding his\x01",
            "personal connections in this way.)\x02",
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
    Jump("loc_25C2")

    label("loc_24E3")


    ChrTalk(
        0x1F,
        "#11500FAnd, Mr. Beardy-Bear...\x02",
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
            "#00003F(...We can't listen to the entire\x01",
            "conversation of these three.)\x02\x03",
            "(Let's not intrude any more\x01",
            "than we already have.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C2")

    Return()

    # Function_6_1C46 end

    def Function_7_25C3(): pass

    label("Function_7_25C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_264A")

    ChrTalk(
        0xFE,
        (
            "*sigh*, I knew it was too much to\x01",
            "try and sneak onto the VIP floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Even so, I wonder\x01",
            "where Senior went?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E3")

    label("loc_264A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2658")
    Jump("loc_27E3")

    label("loc_2658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_27E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2677")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_2677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2748")

    ChrTalk(
        0xFE,
        (
            "Liberl News ace camerawoman\x01",
            "Dorothy Hyatt...\x02",
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
            "As a cameraman, I would love\x01",
            "to speak with her, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_27E3")

    label("loc_2748")


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
            "to travel between Ruan\x01",
            "and the capital, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E3")

    TalkEnd(0xFE)
    Return()

    # Function_7_25C3 end

    def Function_8_27E7(): pass

    label("Function_8_27E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_28CA")

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
            "Liberal and Remiferia see\x01",
            "stimulation of the continental\x01",
            "economy as positive, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EC")

    label("loc_28CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_28EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E9")
    TalkEnd(0xFE)
    Call(0, 34)
    Return()

    label("loc_28E9")

    Call(0, 5)

    label("loc_28EC")

    TalkEnd(0xFE)
    Return()

    # Function_8_27E7 end

    def Function_9_28F0(): pass

    label("Function_9_28F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_29C3")

    ChrTalk(
        0xFE,
        (
            "Hmm. It's very unusual for the\x01",
            "two major powers to compromise\x01",
            "this much on state proposals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, it is the case that state interests\x01",
            "are directly connection to their own, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A87")

    label("loc_29C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DE")
    Call(0, 10)
    Jump("loc_2A87")

    label("loc_29DE")


    ChrTalk(
        0xFE,
        (
            "But, this Orchis Tower is a\x01",
            "completely unthinkable building.\x02",
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

    label("loc_2A87")

    TalkEnd(0xFE)
    Return()

    # Function_9_28F0 end

    def Function_10_2A8B(): pass

    label("Function_10_2A8B")


    ChrTalk(
        0x15,
        (
            "Once again, I am Thompson\x01",
            "of Ardent Press.\x02",
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
        "Yes. I'm still inexperienced, though.\x02",
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
            "Our countries may be different and there's\x01",
            "no competition― Let's work together today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Ha ha, I agree. I look forward\x01",
            "to working with you, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_10_2A8B end

    def Function_11_2BE6(): pass

    label("Function_11_2BE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB8")

    ChrTalk(
        0xFE,
        (
            "*sigh*. The conference's first\x01",
            "half has finally died down.\x02",
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
        "The main event has yet to begin.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2D27")

    label("loc_2CB8")


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
        "The main event has yet to begin.\x02",
    )

    CloseMessageWindow()

    label("loc_2D27")

    Jump("loc_3062")

    label("loc_2D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2F8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EEC")
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's right, they said all countries\x01",
            "gave their consent on that issue too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now, to report that to the main office...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(It looks like he's contacting\x01",
            "someone via ENIGMA.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Most likely, his fellow\x01",
            "reporters are outside the tower.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu. The play-by-play of\x01",
            "the Trade Conference, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F(How to say this... That must be difficult work.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2F86")

    label("loc_2EEC")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "That's right, they said all countries\x01",
            "gave their consent on that issue too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now, to report that to the main office...\x02",
    )

    CloseMessageWindow()

    label("loc_2F86")

    Jump("loc_3062")

    label("loc_2F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3062")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA6")
    Call(0, 12)
    Jump("loc_3062")

    label("loc_2FA6")


    ChrTalk(
        0xFE,
        (
            "Hu hu. If you're saying that, then\x01",
            "President Rocksmith too is...\x02",
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
            "I felt a confident style more\x01",
            "than what I usually get from\x01",
            "the Tyrell News' articles.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3062")

    TalkEnd(0xFE)
    Return()

    # Function_11_2BE6 end

    def Function_12_3066(): pass

    label("Function_12_3066")

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
            "There are many conferences between two \x01",
            "countries, but this time includes Crossbell \x01",
            "and its four neighboring states...\x02",
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
            "Today is a\x01",
            "historical first.\x02",
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

    # Function_12_3066 end

    def Function_13_32B7(): pass

    label("Function_13_32B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3381")

    ChrTalk(
        0xFE,
        (
            "It's too bad we can't get coverage\x01",
            "from the VIP floor... But there's still\x01",
            "plenty of chances for getting material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to go over the outline\x01",
            "of questions I want to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C1")

    label("loc_3381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_338F")
    Jump("loc_34C1")

    label("loc_338F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_34C1")

    ChrTalk(
        0xFE,
        (
            "In various areas, the Crossbell Police\x01",
            "are often seen as incompetent, but..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on the security in this building, \x01",
            "I get the contrary impression that they're \x01",
            "actually an outstanding organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The problem isn't the people but the state\x01",
            "structure... You can strongly feel it..\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C1")

    TalkEnd(0xFE)
    Return()

    # Function_13_32B7 end

    def Function_14_34C5(): pass

    label("Function_14_34C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3562")

    ChrTalk(
        0xFE,
        (
            "Now then, in the meanwhile, it looks\x01",
            "like break time is already over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to start preparing for\x01",
            "the conference's second half.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373F")

    label("loc_3562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_368C")

    ChrTalk(
        0xFE,
        (
            "Regarding the economics-related agreements,\x01",
            "I can only say I'm amazed at the results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might be because Mayor Dieter, \x01",
            "who made the proposals,\x01",
            "is also the IBC president.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Economic development will promote continental\x01",
            "security... I feel it's not necessarily a fantasy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_373F")

    label("loc_368C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_373F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A7")
    Call(0, 12)
    Jump("loc_373F")

    label("loc_36A7")


    ChrTalk(
        0xFE,
        (
            "Even so... Chancellor Osborne's\x01",
            "intensity is the real thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not like looking at a photo of him.\x01",
            "It feels like I understood many things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_373F")

    TalkEnd(0xFE)
    Return()

    # Function_14_34C5 end

    def Function_15_3743(): pass

    label("Function_15_3743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_37B4")

    ChrTalk(
        0xFE,
        (
            "Break time will be over soon... I guess I should\x01",
            "buy something to drink while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38CB")

    label("loc_37B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_37C2")
    Jump("loc_38CB")

    label("loc_37C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_38CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37DD")
    Call(0, 10)
    Jump("loc_38CB")

    label("loc_37DD")


    ChrTalk(
        0xFE,
        (
            "Yes, on good weather days,\x01",
            "you already clearly see that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the tower, you can say\x01",
            "that the amount of tourists visiting\x01",
            "Altair City has slightly increased too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This tower will have an\x01",
            "amazing impact on the economy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CB")

    TalkEnd(0xFE)
    Return()

    # Function_15_3743 end

    def Function_16_38CF(): pass

    label("Function_16_38CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_39BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38ED")
    Call(0, 17)
    Jump("loc_39BA")

    label("loc_38ED")


    ChrTalk(
        0x17,
        (
            "#00600FOh, you guys, huh.\x02\x03",
            "Although there's still some\x01",
            "time, you should visit each\x01",
            "of the heads of state ASAP.\x02\x03",
            "I don't think I have to say this, but it's\x01",
            "not the case that you can keep them waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BA")

    Jump("loc_3F51")

    label("loc_39BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E96")

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
            "#00100FSo you can get a view of the entire\x01",
            "security detail on this monitor.\x02",
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
            "#00203FSecurity cameras... Starting from IBC, \x01",
            "it is a technology that has begun to be\x01",
            "used in orbal stores and other places.\x02\x03",
            "#00200FThere is a lot more of\x01",
            "them here, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou talk about it like it's no big deal,\x01",
            "but it's really amazing technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, they might eventually use them to\x01",
            "keep an eye on areas outside the city, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHmm. That's a sensitive matter. It'll depend \x01",
            "on whether the understanding of the citizens\x01",
            "will be secured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603F...Anyway, being able to use\x01",
            "them is definitely convenient.\x02\x03",
            "#00601FBesides monitoring for potential terrorists, if\x01",
            "they do strike, all we can do is respond before\x01",
            "they cause trouble, or immediately afterwards.\x02\x03",
            "For that reason, we mustn't overlook\x01",
            "even the most trivial information.\x02\x03",
            "If you see anything, report it at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FAlright, roger that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 5)
    Call(0, 36)
    Jump("loc_3F51")

    label("loc_3E96")


    ChrTalk(
        0x17,
        (
            "#00603FWe're in constant contact with the surrounding \x01",
            "areas, and no conspicuous problems have \x01",
            "occurred as of yet.\x02\x03",
            "#00600FYou all, continue your patrols\x01",
            "of the appropriate floors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F51")

    TalkEnd(0xFE)
    Return()

    # Function_16_38CF end

    def Function_17_3F55(): pass

    label("Function_17_3F55")

    OP_4B(0x17, 0xFF)
    OP_4B(0x1A, 0xFF)

    ChrTalk(
        0x17,
        (
            "#00600FCaptain Grant, how is your\x01",
            "company doing at present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Naturally, all of us are standing by\x01",
            "keeping in check our nervousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "After all, our duty is to be ready\x01",
            "for emergencies at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#00603FI see. That's reassuring.\x02\x03",
            "#00601FNow then, about the force's deployment\x01",
            "for the conference's second half―\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    OP_4C(0x1A, 0xFF)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x1A, 0x10)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_17_3F55 end

    def Function_18_40BD(): pass

    label("Function_18_40BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_42C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F5")

    ChrTalk(
        0xFE,
        (
            "At present, no abnormalities detected\x01",
            "both within and outside of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "According to the surveillance team,\x01",
            "neither the "Red Constellation" nor\x01",
            ""Heiyue" show any signs of action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I say it's the calm before the storm?\x01",
            "...I can't help but think it's ominous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_42BF")

    label("loc_41F5")


    ChrTalk(
        0xFE,
        (
            "According to the surveillance team,\x01",
            "neither the "Red Constellation" nor\x01",
            ""Heiyue" show any signs of action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I say it's the calm before the storm?\x01",
            "...I can't help but think it's ominous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BF")

    Jump("loc_44EC")

    label("loc_42C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_44EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4411")

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
    Jump("loc_44EC")

    label("loc_4411")


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
            "There's practically the full power of\x01",
            "Crossbell behind this security structure...\x01",
            "For this reason, mistakes won't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44EC")

    TalkEnd(0xFE)
    Return()

    # Function_18_40BD end

    def Function_19_44F0(): pass

    label("Function_19_44F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_459A")

    ChrTalk(
        0xFE,
        (
            "To think we've continued security operations\x01",
            "for this long without information coming in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just where are those\x01",
            "terrorists hiding themselves?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4658")

    label("loc_459A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4658")

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

    label("loc_4658")

    TalkEnd(0xFE)
    Return()

    # Function_19_44F0 end

    def Function_20_465C(): pass

    label("Function_20_465C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A0")

    ChrTalk(
        0xFE,
        (
            "No matter whether it's during break or during the\x01",
            "conference, our security activities don't change.\x02",
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
            "There are several possible patterns. We'll\x01",
            "have to see how things go and play it by ear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_485D")

    label("loc_47A0")


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
            "There are several possible patterns. We'll\x01",
            "have to see how things go and play it by ear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_485D")

    Jump("loc_493D")

    label("loc_4862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_493D")

    ChrTalk(
        0xFE,
        (
            "When looking at the monitors like this,\x01",
            "it transpires the fact that everyone is\x01",
            "doing their security job seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Terrorists, huh... It would be nice if\x01",
            "their presence was proved unfounded.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_493D")

    TalkEnd(0xFE)
    Return()

    # Function_20_465C end

    def Function_21_4941(): pass

    label("Function_21_4941")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A12")

    ChrTalk(
        0xFE,
        (
            "We of the Guard\x01",
            "Section are handling\x01",
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
            "If the worst happens, I'm confident\x01",
            "we're as capable as the CGF.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4AAA")

    label("loc_4A12")


    ChrTalk(
        0xFE,
        (
            "Because we of the Guard\x01",
            "Section train for emergencies\x01",
            "through actual combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the worst happens, I'm confident\x01",
            "we're as capable as the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAA")

    TalkEnd(0xFE)
    Return()

    # Function_21_4941 end

    def Function_22_4AAE(): pass

    label("Function_22_4AAE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Normally, we're responsible for securing\x01",
            "important government facilities and\x01",
            "bodyguarding various dignitaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival was the same,\x01",
            "but handling international events like\x01",
            "these is one of our most important jobs.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_4AAE end

    def Function_23_4BA5(): pass

    label("Function_23_4BA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BC3")
    Call(0, 17)
    Jump("loc_4CB4")

    label("loc_4BC3")


    ChrTalk(
        0xFE,
        (
            "Hmm. If they don't show up during break time,\x01",
            "they will during the climax of the conference's\x01",
            "second half or after that, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's no use\x01",
            "overthinking things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, when the time\x01",
            "arrives, we'll be\x01",
            "ready to do our best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB4")

    Jump("loc_4D83")

    label("loc_4CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD4")
    Call(0, 24)
    Jump("loc_4D83")

    label("loc_4CD4")


    ChrTalk(
        0xFE,
        (
            "Still, it's a mere detail, but this room\x01",
            "is too unmanageable for just two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say... Orchis Tower\x01",
            "is in a whole other league\x01",
            "compared to everything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D83")

    TalkEnd(0xFE)
    Return()

    # Function_23_4BA5 end

    def Function_24_4D87(): pass

    label("Function_24_4D87")

    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    TurnDirection(0x1B, 0x0, 500)

    ChrTalk(
        0x109,
        "#10100FCaptain Grant, thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHello, nice job there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Master Sergeant Seeker and Sergeant Orlando, huh.\x02",
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
            "#10100FIt's true that I'm on temporary transfer, but\x01",
            "please just call me by whatever's easiest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHa ha. Anything's fine by me too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIs it just the\x01",
            "two of you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "Yes, we must have regard to the \x01",
            "heads of state and the press corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "It was decided the CGF should avoid\x01",
            "exposure as much as possible,\x01",
            "so we're minimally deployed.\x02",
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
            "#10101FYes, it's out of consideration \x01",
            "for the two major powers.\x02\x03",
            "Although armaments are limited by the\x01",
            "autonomous state law, the CGF is is an\x01",
            "organ equivalent to a so-called military...\x02\x03",
            "Although within limits, a large amount of\x01",
            "the budget is used to maintain the units\x01",
            "and for armaments expansion and so on.\x02\x03",
            "#10108FBecause of that, it would be a topic\x01",
            "on which to be easily criticized in\x01",
            "a conference like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FI see... \x01",
            "So that is why you are trying\x01",
            "to stay out of sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, diplomacy sure\x01",
            "is a difficult thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well, that's certainly true,\x01",
            "but a little excessive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "In the end, this is\x01",
            "just for appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Instead, a whole company\x01",
            "is on the floor below, ready\x01",
            "to move out at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "All of us will be here right away if something\x01",
            "happens, so there's no need to worry.\x02",
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
        "#00101FWe'll be counting on you then.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    SetScenarioFlags(0x1C1, 6)
    Call(0, 36)
    Return()

    # Function_24_4D87 end

    def Function_25_53A2(): pass

    label("Function_25_53A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5440")

    ChrTalk(
        0xFE,
        (
            "Now that the conference is half over,\x01",
            "the situation seems unchanged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to sense terrorist\x01",
            "movements before they act, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5566")

    label("loc_5440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_545B")
    Call(0, 24)
    Jump("loc_5566")

    label("loc_545B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F8")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Master Sergeant Noｱl, let's both do\x01",
            "everything we can today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Leave the floor security to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5566")

    label("loc_54F8")

    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Master Sergeant Noｱl, let's both do\x01",
            "everything we can today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Leave the floor security to us.\x02",
    )

    CloseMessageWindow()

    label("loc_5566")

    TalkEnd(0xFE)
    Return()

    # Function_25_53A2 end

    def Function_26_556A(): pass

    label("Function_26_556A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_557B")
    Jump("loc_59B1")

    label("loc_557B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_59B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5596")
    Call(0, 27)
    Jump("loc_59B1")

    label("loc_5596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D9")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5631")
    Jump("loc_567B")

    label("loc_5631")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5651")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_567B")

    label("loc_5651")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5671")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_567B")

    label("loc_5671")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_567B")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0x101,
        (
            "#00001FCome to think of it,\x01",
            "Vice Chief, what about the "guy"\x01",
            "you were talking about before...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I'm interested in that too.\x01",
            "Could he be a suspicious character?\x02",
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
            "Hey, this has nothing\x01",
            "to do with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "G-Get back to work, on the double!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FY-Yes sir, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Don't tell me he was\x01",
            "thinkin' of his wife...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(He certainly is a hen-pecked husband.\x01",
            "...There must be some circumstances.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Right... \x01",
            "Let's keep this quiet.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1C2, 0)
    SetChrSubChip(0xB, 0x0)
    Jump("loc_59B1")

    label("loc_58D9")

    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        "Grr... Every single one of them...\x02",
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

    label("loc_59B1")

    TalkEnd(0xFE)
    Return()

    # Function_26_556A end

    def Function_27_59B5(): pass

    label("Function_27_59B5")

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
            "Mrgrr, to think that guy...\x01",
            "No, I'm positive that something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005F(W-Who is "that guy"...?)\x02\x03",
            "#00000FUmm, Vice Chief Pierre?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Huh!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        "I-It's the Special Support Section, of all people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Do you have business with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FVice Chief, what are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FH-Hey, Tio――\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "I'm not doing anything...except serving\x01",
            "as the chief of security planning!!\x02",
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
            "#10300FCome to think of it, I remember reading\x01",
            "your name on some materials we were given.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...I see. I didn't study the documents enough\x02",
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
            "#00106FWe should have\x01",
            "told you before.\x02",
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
            "#10302FHu hu, you're the security planning chief,\x01",
            "so why aren't you in the planning room?\x02\x03",
            "Are you here on break then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmph. I gave Dudley full\x01",
            "command authority on site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because of that, staying\x01",
            "there would mean getting\x01",
            "in the way and be awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You may think it was selfish of me, but...\x01",
            "I'm a superior who knows what he does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A-Anyway...\x01",
            "Make sure not to get\x01",
            "in Dudley's way.\x02",
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

    # Function_27_59B5 end

    def Function_28_5F76(): pass

    label("Function_28_5F76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5F8A")
    Call(0, 6)
    Jump("loc_61C0")

    label("loc_5F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_61B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60EC")

    ChrTalk(
        0x8,
        (
            "#02203FHmm. Even disregarding the details,\x01",
            "to be called by both heads of state...\x02\x03",
            "#02200FI'm sure you're nervous, but chances\x01",
            "like this don't come by often.\x02\x03",
            "Even just experiencing their auras from up \x01",
            "close should be a good experience for you.\x02",
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
        "#00100FExcuse us then, Mr. Grimwood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_61B2")

    label("loc_60EC")


    ChrTalk(
        0x8,
        (
            "#02200FI felt it at the conference too, but even just\x01",
            "experiencing their auras from up close\x01",
            "should be a good experience for you.\x02\x03",
            "Don't think about unnecessary\x01",
            "things, and just go visit them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61B2")

    Jump("loc_61C0")

    label("loc_61B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_61C0")

    label("loc_61C0")

    TalkEnd(0xFE)
    Return()

    # Function_28_5F76 end

    def Function_29_61C4(): pass

    label("Function_29_61C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_61D8")
    Call(0, 6)
    Jump("loc_61EF")

    label("loc_61D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_61E6")
    Jump("loc_61EF")

    label("loc_61E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_61EF")

    label("loc_61EF")

    TalkEnd(0xFE)
    Return()

    # Function_29_61C4 end

    def Function_30_61F3(): pass

    label("Function_30_61F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_62AA")

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
        "I feel like it's not a normal atmosphere.\x02",
    )

    CloseMessageWindow()
    Jump("loc_69C4")

    label("loc_62AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_6347")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I wonder\x01",
            "where Vice Chief Pierre went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He hasn't been back for awhile. Did\x01",
            "he go to the security planning room?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69C4")

    label("loc_6347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_69C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63F1")

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
        "...I can't help but be worried about him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_69C4")

    label("loc_63F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694B")

    ChrTalk(
        0xFE,
        (
            "Guys, it looks like you spoke\x01",
            "with Vice Chief Pierre.\x02",
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
            "wasn't as mean a\x01",
            "person before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see. Mean, huh... Well, I\x01",
            "guess that can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, there's two\x01",
            "people in the police with\x01",
            "the title of Vice Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the previous police chief\x01",
            "was dismissed, the other Vice\x01",
            "Chief was appointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThat's certainly how it went down.\x02\x03",
            "We never agreed\x01",
            "with him, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, the new chief... \x01",
            "He's actually Vice Chief Pierre's\x01",
            "junior. Did you know that?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThe new chief is...Vice Chief's junior?\x02",
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
            "imagine what Mr. Pierre\x01",
            "thinks of the chief right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To put it bluntly, I think it was\x01",
            "a reasonable HR decision, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, he's the same Vice Chief... On top\x01",
            "of that, being passed by his subordinate\x01",
            "might be more than he can bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. Certainly, it's\x01",
            "natural to feel that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, because of that, he's having\x01",
            "it pretty rough in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, you all too, please widen you\x01",
            "minds when dealing with him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if you got\x01",
            "scolded, I think he\x01",
            "worries about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-I see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C2, 1)
    Jump("loc_69C4")

    label("loc_694B")


    ChrTalk(
        0xFE,
        (
            "Vice Chief Pierre must have it\x01",
            "tough, despite the appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He can be critical, but\x01",
            "we have to bear it too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69C4")

    TalkEnd(0xFE)
    Return()

    # Function_30_61F3 end

    def Function_31_69C8(): pass

    label("Function_31_69C8")

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

    # Function_31_69C8 end

    def Function_32_6A48(): pass

    label("Function_32_6A48")

    TalkBegin(0xFE)
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Understood... \x01",
            "Quickly and reliably.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_32_6A48 end

    def Function_33_6A81(): pass

    label("Function_33_6A81")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now then, the lunchboxes...\x01",
            "*sigh*, finally, something to eat.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_6A81 end

    def Function_34_6ACC(): pass

    label("Function_34_6ACC")

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
        "Nice work everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02110FLloyd and company! You came!\x02\x03",
            "#02102FMaaan, the conference\x01",
            "has finally started, eh?\x02\x03",
            "The leaders of Crossbell State and the four\x01",
            "surrounding countries are all present! It's\x01",
            "an unprecedented international conference!\x02\x03",
            "And to top it off, it's being held\x01",
            "at Orchis Tower, the continent's\x01",
            "very first skyscraper...\x02\x03",
            "#02109FWith this much excitement and\x01",
            "tension, your big sis' heart here\x01",
            "is gonna burst any second now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FExcitement aside, \x01",
            "I don't see you being\x01",
            "tense at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FYeah, you are the\x01",
            "same old Miss Grace.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x103, 500)

    ChrTalk(
        0xC,
        (
            "#02105FAh, Tio! Even though it's been awhile,\x01",
            "you're relentless right out of the gate.\x02\x03",
            "#02104FWell, I admit I'm more\x01",
            "thrilled than excited...\x01",
            "But that aside.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    ChrTalk(
        0xC,
        (
            "#02100FI'll introduce you, Miss Noticia. \x01",
            "They're the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I see. I saw you in the papers.\x01",
            "Uh uh, you look even more amazing in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm Noticia from Liberl News.\x01",
            "Thank you for your help today.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#00000FWe're happy to be of service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FThe Liberl News―― It's the\x01",
            "largest paper in the Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, and they're also the hot topic\x01",
            "in the business for another reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "They're famous for having the reporters who\x01",
            "won last year's Fulitzer Prize among their staff.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7175")

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, that's the prize that Mr. Nielsen\x01",
            "was awarded a long time ago, right?\x02\x03",
            "They say it's given to the most\x01",
            "outstanding journalist each year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71EB")

    label("loc_7175")


    ChrTalk(
        0x105,
        (
            "#12P#10300FThe Fulitzer Prize...\x02\x03",
            "If I recall, it's an award to\x01",
            "honor the most outstanding\x01",
            "journalist each year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71EB")


    ChrTalk(
        0xE,
        "#5PUh uh, you know it well.\x02",
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
            "#5PThey're the ace reporter and genius\x01",
            "cameraman of our news service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FOh, so last year's winners\x01",
            "were from Liberl News.\x02",
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
        "#5PYes, it's as you suspect.\x02",
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
            "#6P#00203FI see... They sound\x01",
            "like amazing reporters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02109FYeah. We can't lose\x01",
            "to them again.\x02\x03",
            "#02103FAll reporters long for the Fulitzer\x01",
            "Prize at least once in their careers...\x02\x03",
            "To get that prize of tomorrow, it's\x01",
            "critical to go out and get that scoop\x01",
            "each and every day. Especially today!\x02\x03",
            "#02110FAnd so Reins,\x01",
            "you've got to do your best to not\x01",
            "get outmaneuvered by the others!\x02",
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
            "#6P#00106F(I hope she\x01",
            "behaves herself,\x01",
            "though...)\x02",
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

    # Function_34_6ACC end

    def Function_35_7646(): pass

    label("Function_35_7646")

    Sound(160, 0, 100, 0)
    Return()

    # Function_35_7646 end

    def Function_36_764D(): pass

    label("Function_36_764D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7675")
    SetScenarioFlags(0x146, 3)

    label("loc_7675")

    Return()

    # Function_36_764D end

    def Function_37_7676(): pass

    label("Function_37_7676")

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

    def lambda_7836():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7836)
    Sleep(50)

    def lambda_7846():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7846)
    Sleep(50)

    def lambda_7856():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7856)
    Sleep(50)

    def lambda_7866():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7866)
    Sleep(50)

    def lambda_7876():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7876)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#5P#00102F#10AAmazing...\x02",
    )

    CloseMessageWindow()
    OP_68(79000, 1000, -2700, 2000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_78DF():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78DF)
    Sleep(300)

    def lambda_78FC():
        OP_93(0xFE, 0xB4, 0x15E)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_78FC)

    def lambda_7909():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7909)
    Sleep(300)

    def lambda_7926():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7926)
    Sleep(300)

    def lambda_7943():
        OP_97(0xFE, 0x12C, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7943)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_7676 end

    def Function_38_796C(): pass

    label("Function_38_796C")

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

    # Function_38_796C end

    def Function_39_79DC(): pass

    label("Function_39_79DC")


    def lambda_79E1():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79E1)

    def lambda_79FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79FB)
    WaitChrThread(0xFE, 1)

    def lambda_7A10():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A10)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_39_79DC end

    def Function_40_7A31(): pass

    label("Function_40_7A31")


    def lambda_7A36():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A36)

    def lambda_7A50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A50)
    WaitChrThread(0xFE, 1)

    def lambda_7A65():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A65)
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

    # Function_40_7A31 end

    def Function_41_7AC0(): pass

    label("Function_41_7AC0")


    def lambda_7AC5():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AC5)

    def lambda_7ADF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7ADF)
    WaitChrThread(0xFE, 1)

    def lambda_7AF4():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AF4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_41_7AC0 end

    def Function_42_7B15(): pass

    label("Function_42_7B15")


    def lambda_7B1A():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B1A)

    def lambda_7B34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B34)
    WaitChrThread(0xFE, 1)

    def lambda_7B49():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B49)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_42_7B15 end

    def Function_43_7B6A(): pass

    label("Function_43_7B6A")


    def lambda_7B6F():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B6F)

    def lambda_7B89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B89)
    WaitChrThread(0xFE, 1)

    def lambda_7B9E():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B9E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_43_7B6A end

    def Function_44_7BBF(): pass

    label("Function_44_7BBF")


    def lambda_7BC4():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BC4)

    def lambda_7BDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7BDE)
    WaitChrThread(0xFE, 1)

    def lambda_7BF3():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BF3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_44_7BBF end

    def Function_45_7C14(): pass

    label("Function_45_7C14")


    def lambda_7C19():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C19)

    def lambda_7C33():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C33)
    WaitChrThread(0xFE, 1)

    def lambda_7C48():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C48)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_45_7C14 end

    def Function_46_7C69(): pass

    label("Function_46_7C69")

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
        "#10109F#5PWhaaa...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#5PWhat a view...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PMan, this is the best scenery!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02809F#5PHa ha, it seems you're all satisfied.\x02\x03",
            "#02800F──This is 34F. Once the international\x01",
            "conference begins, staff will be\x01",
            "standing by on this floor.\x02\x03",
            "#02800FAlright then. Shall we\x01",
            "have a look around?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EA1():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7EA1)
    Sleep(50)

    def lambda_7EB1():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7EB1)
    Sleep(50)

    def lambda_7EC1():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7EC1)
    Sleep(50)

    def lambda_7ED1():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7ED1)
    Sleep(50)

    def lambda_7EE1():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7EE1)
    Sleep(50)

    def lambda_7EF1():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7EF1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)

    def lambda_7F16():

        label("loc_7F16")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7F16")

    QueueWorkItem2(0x101, 2, lambda_7F16)

    def lambda_7F28():

        label("loc_7F28")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7F28")

    QueueWorkItem2(0x102, 2, lambda_7F28)

    def lambda_7F3A():

        label("loc_7F3A")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7F3A")

    QueueWorkItem2(0x103, 2, lambda_7F3A)

    def lambda_7F4C():

        label("loc_7F4C")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7F4C")

    QueueWorkItem2(0x109, 2, lambda_7F4C)

    def lambda_7F5E():

        label("loc_7F5E")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7F5E")

    QueueWorkItem2(0x105, 2, lambda_7F5E)

    def lambda_7F70():

        label("loc_7F70")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_7F70")

    QueueWorkItem2(0x104, 2, lambda_7F70)

    ChrTalk(
        0x101,
        "#12P#00002FYes, please lead the way.\x02",
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

    def lambda_7FDE():
        OP_97(0x105, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7FDE)
    Sleep(100)

    def lambda_7FFB():
        OP_97(0x103, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7FFB)
    Sleep(100)

    def lambda_8018():
        OP_97(0x104, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8018)
    Sleep(100)

    def lambda_8035():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8035)
    Sleep(100)

    def lambda_8052():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8052)
    Sleep(100)

    def lambda_806F():
        OP_97(0x102, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_806F)
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

    def lambda_81BD():
        OP_95(0xFE, 8500, 0, -1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_81BD)

    def lambda_81D7():
        OP_96(0xFE, 0x2968, 0xFFFFFDA8, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_81D7)

    def lambda_81F1():
        OP_97(0x101, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_81F1)
    Sleep(50)

    def lambda_820E():
        OP_97(0x102, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_820E)
    Sleep(50)

    def lambda_822B():
        OP_97(0x103, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_822B)
    Sleep(50)

    def lambda_8248():
        OP_97(0x104, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8248)
    Sleep(50)

    def lambda_8265():
        OP_97(0x109, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8265)
    Sleep(50)

    def lambda_8282():
        OP_97(0x105, 0xFFFF9688, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8282)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_82A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_82A8)
    Sleep(50)

    def lambda_82BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_82BC)
    Sleep(500)

    def lambda_82D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_82D0)
    Sleep(50)

    def lambda_82E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_82E4)
    OP_0D()
    WaitChrThread(0x20, 1)
    OP_93(0x20, 0x2D, 0x1F4)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)

    ChrTalk(
        0x20,
        (
            "#6P#02803FThat's the security planning room.\x01",
            "The press room is right next door.\x02\x03",
            "#02800FIn the case of a terrorist infiltration, \x01",
            "a Guardian Force company\x01",
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
            "#00300F#11PI bet they hand-picked the\x01",
            "best the CGF has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#11PI wonder if Miss Grace is\x01",
            "part of the press corps.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)

    ChrTalk(
        0x20,
        (
            "#6P#02805FOh, you mean the\x01",
            "Crossbell Times reporter?\x02\x03",
            "#02804FI remember she was on the list,\x01",
            "so she'll probably be here.\x02\x03",
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
            "#11P#00106FSometimes, there're even rude\x01",
            "reporters who slip past security\x01",
            "for assault interviews.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FMore precisely, Miss Grace is the\x01",
            "number one reporter in that category.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYeah. Even if you find her,\x01",
            "she can't be stopped.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x10E, 0x1F4)

    def lambda_8693():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8693)

    def lambda_86AD():
        OP_97(0x101, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_86AD)
    Sleep(50)

    def lambda_86CA():
        OP_97(0x102, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_86CA)
    Sleep(50)

    def lambda_86E7():
        OP_97(0x103, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_86E7)
    Sleep(50)

    def lambda_8704():
        OP_97(0x104, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8704)
    Sleep(50)

    def lambda_8721():
        OP_97(0x109, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8721)
    Sleep(50)

    def lambda_873E():
        OP_97(0x105, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_873E)
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

    def lambda_8866():
        OP_97(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8866)

    def lambda_8880():
        OP_98(0xFE, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8880)

    def lambda_889A():
        OP_97(0x101, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_889A)
    Sleep(50)

    def lambda_88B7():
        OP_97(0x102, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_88B7)
    Sleep(50)

    def lambda_88D4():
        OP_97(0x103, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_88D4)
    Sleep(50)

    def lambda_88F1():
        OP_97(0x104, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_88F1)
    Sleep(50)

    def lambda_890E():
        OP_97(0x109, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_890E)
    Sleep(50)

    def lambda_892B():
        OP_97(0x105, 0x0, 0x0, 0x3E80, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_892B)
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

    def lambda_89B4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_89B4)
    Sleep(50)

    def lambda_89C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_89C4)

    def lambda_89D1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_89D1)
    Sleep(50)

    def lambda_89E1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_89E1)

    def lambda_89EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_89EE)
    Sleep(50)

    def lambda_89FE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_89FE)
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
            "#02804FThis is the break room I've prepared\x01",
            "for those involved in the conference.\x02\x03",
            "#02800FDuring breaks, please feel\x01",
            "free to make use of it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C2A():
        TurnDirection(0x101, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8C2A)
    Sleep(50)

    def lambda_8C3A():
        TurnDirection(0x102, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8C3A)
    Sleep(50)

    def lambda_8C4A():
        TurnDirection(0x103, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8C4A)
    Sleep(50)

    def lambda_8C5A():
        TurnDirection(0x104, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8C5A)
    Sleep(50)

    def lambda_8C6A():
        TurnDirection(0x109, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8C6A)
    Sleep(50)

    def lambda_8C7A():
        TurnDirection(0x105, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8C7A)
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
            "#6P#00109F*giggle*, maybe we \x01",
            "should have tea later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02809FNow then, I think it's time\x01",
            "I showed you the next floor.\x02",
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

    def lambda_8E31():
        OP_95(0xFE, -13000, 0, 1800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8E31)

    def lambda_8E4B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_8E4B)

    def lambda_8E65():
        OP_97(0x101, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E65)
    Sleep(50)

    def lambda_8E82():
        OP_97(0x102, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E82)
    Sleep(50)

    def lambda_8E9F():
        OP_97(0x103, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E9F)
    Sleep(50)

    def lambda_8EBC():
        OP_97(0x104, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8EBC)
    Sleep(50)

    def lambda_8ED9():
        OP_97(0x109, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8ED9)
    Sleep(50)

    def lambda_8EF6():
        OP_97(0x105, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8EF6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x20, 1)

    def lambda_8F1E():
        OP_95(0xFE, -14800, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8F1E)
    WaitChrThread(0x27, 1)
    OP_6B(0xFF)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_8F58():

        label("loc_8F58")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8F58")

    QueueWorkItem2(0x101, 2, lambda_8F58)
    WaitChrThread(0x102, 0)

    def lambda_8F6E():

        label("loc_8F6E")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8F6E")

    QueueWorkItem2(0x102, 2, lambda_8F6E)
    WaitChrThread(0x103, 0)

    def lambda_8F84():

        label("loc_8F84")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8F84")

    QueueWorkItem2(0x103, 2, lambda_8F84)
    WaitChrThread(0x104, 0)

    def lambda_8F9A():

        label("loc_8F9A")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_8F9A")

    QueueWorkItem2(0x104, 2, lambda_8F9A)
    WaitChrThread(0x20, 1)

    def lambda_8FB0():
        OP_95(0xFE, -17600, 0, 0, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8FB0)
    Sleep(300)
    Sound(103, 0, 100, 0)

    def lambda_8FD3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_8FD3)
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
            "#12P#00005FThese are...\x01",
            "Emergency stairs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FIt looks like the ones going\x01",
            "down are sealed, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02803F#5PNormally, you can go down\x01",
            "to 1F using these stairs.\x02\x03",
            "#02801FHowever, during the\x01",
            "conference, all floors except\x01",
            "34F, 35F and 36F will be sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI see. \x01",
            "So it's for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FBut, what will you do in\x01",
            "the event of an earthquake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02806F#5PIn that case, all emergency\x01",
            "stairs will automatically open.\x02\x03",
            "#02800FWell, they say perfect\x01",
            "security is impossible, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... \x01",
            "We'll need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00208F...It seems there is a need to\x01",
            "think of hacking countermeasures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02804F#5PNow then. Since we're here,\x01",
            "let's use the stairs.\x02\x03",
            "#02800FWelcome to 35F──\x01",
            "The international conference floor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_7C69 end

    def Function_47_9504(): pass

    label("Function_47_9504")

    OP_92(0xFE, 0x128E0, 0x0, 0x1F4)

    def lambda_9516():
        OP_95(0xFE, 76000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9516)
    WaitChrThread(0xFE, 1)

    def lambda_9534():
        OP_95(0xFE, 68000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9534)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_9504 end

    def Function_48_954E(): pass

    label("Function_48_954E")


    def lambda_9553():
        OP_95(0xFE, -14800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9553)
    WaitChrThread(0xFE, 1)

    def lambda_9571():
        OP_95(0xFE, -17600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9571)
    Sleep(300)

    def lambda_958E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_958E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_954E end

    def Function_49_959F(): pass

    label("Function_49_959F")


    def lambda_95A4():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95A4)

    def lambda_95BE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_95BE)
    WaitChrThread(0xFE, 1)

    def lambda_95D3():
        OP_95(0xFE, -55000, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95D3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_49_959F end

    def Function_50_95F4(): pass

    label("Function_50_95F4")


    def lambda_95F9():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95F9)

    def lambda_9613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9613)
    WaitChrThread(0xFE, 1)

    def lambda_9628():
        OP_95(0xFE, -53500, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9628)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_50_95F4 end

    def Function_51_9649(): pass

    label("Function_51_9649")


    def lambda_964E():
        OP_95(0xFE, -52000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_964E)

    def lambda_9668():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9668)
    WaitChrThread(0xFE, 1)

    def lambda_967D():
        OP_95(0xFE, -54500, 0, -1100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_967D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_51_9649 end

    def Function_52_969E(): pass

    label("Function_52_969E")


    def lambda_96A3():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96A3)

    def lambda_96BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_96BD)
    WaitChrThread(0xFE, 1)

    def lambda_96D2():
        OP_95(0xFE, -53000, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96D2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_52_969E end

    def Function_53_96F3(): pass

    label("Function_53_96F3")


    def lambda_96F8():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96F8)

    def lambda_9712():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9712)
    WaitChrThread(0xFE, 1)

    def lambda_9727():
        OP_95(0xFE, -51500, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9727)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_53_96F3 end

    def Function_54_9748(): pass

    label("Function_54_9748")


    def lambda_974D():
        OP_95(0xFE, -51000, 0, -1000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_974D)

    def lambda_9767():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9767)
    WaitChrThread(0xFE, 1)

    def lambda_977C():
        OP_95(0xFE, -51500, 0, -900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_977C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_54_9748 end

    def Function_55_979D(): pass

    label("Function_55_979D")

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
            "#11P#00000FAlright... \x01",
            "This completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make\x01",
            "another loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTrue...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor and the\x01",
            "Chairman are doing their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the "Blood and Iron\x01",
            "Chancellor" and President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should ask someone\x01",
            "about it during the break.\x02",
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

    # Function_55_979D end

    def Function_56_9A78(): pass

    label("Function_56_9A78")

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
            "#11P#00000FAlright... \x01",
            "This completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make\x01",
            "another loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTrue...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor and the\x01",
            "Chairman are doing their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the "Blood and Iron\x01",
            "Chancellor" and President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should ask someone\x01",
            "about it during the break.\x02",
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

    # Function_56_9A78 end

    def Function_57_9D53(): pass

    label("Function_57_9D53")

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
            "#02205F#5PI see... Because of the current situation,\x01",
            "all of you are assisting with security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00002FYeah... Though honestly, it might\x01",
            "just be for peace of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PNo, no, you guys made a huge showing in the\x01",
            "mayoral assassination attempt incident.\x02\x03",
            "#02200FIt's very reassuring knowing\x01",
            "that you are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00104FThank you for saying so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00302FHa ha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#11PLawyer Ian, how is\x01",
            "the conference going?\x02\x03",
            "It hasn't seemed rough\x01",
            "thus far, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PWell, so far so good.\x02\x03",
            "The respective nations have already\x01",
            "agreed to several trade deals.\x02\x03",
            "#02200FIt seems Mayor Dieter won't have\x01",
            "called this conference for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102F*giggle*, is that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10109FThat makes me feel a little better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FBut you said "so far so good." Is there\x01",
            "something you're concerned about?\x02",
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
        "#11P#00001F...Well, is there?\x02",
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
            "#02203F#5PHmm. I'm not sure if I should be\x01",
            "saying this as an observer, but...\x02\x03",
            "The first half has been almost all trade,\x01",
            "finance, and other economy-related proposals.\x02\x03",
            "#02201F──But the second half is comprised of\x01",
            "proposals from each country's head of state.\x02\x03",
            "And what's more, it seems the\x01",
            "security of Crossbell will come up.\x02",
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
            "#12P#00301F...Security, eh? Then that means\x01",
            "military force will enter the equation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FBut, wasn't that "Non-Aggression\x01",
            "Pact" signed two years ago?\x02",
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
            "in that "Non-Aggression Pact".\x02\x03",
            "#02201FIn addition, it's certain\x01",
            "that a new security\x01",
            "framework is needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106F...Certainly. My grandfather\x01",
            "is worried about that, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#11PThen, they just need to sign a new\x01",
            "treaty involving Crossbell as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right. A framework where solving\x01",
            "international conflicts through use of\x01",
            "military force is prohibited, just like\x01",
            "in the Non-Aggression Pact──\x02\x03",
            "#10105F───Ah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FI see... Crossbell\x01",
            "is not a "nation".\x02\x03",
            "#00008FIt is recognized by the Empire and\x01",
            "Republic only as an "autonomous state".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PThat's right. I'm saying that Crossbell\x01",
            "lacks the national sovereignty necessary\x01",
            "to enter into an "international treaty".\x02\x03",
            "Even if economic "agreements" are made, that alone\x01",
            "does not give standing to enter into "treaties".\x02\x03",
            "#02201FSo now you see. That's the reason discussion of\x01",
            "Crossbell's security is so terribly dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FThat's quite complex. I feel\x01",
            "like I understand now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11PExcuse me, may I\x01",
            "ask something?\x02\x03",
            "#00203FThere are other autonomous\x01",
            "states besides Crossbell.\x02\x03",
            "Leman, Ord,\x01",
            "North Ambria...\x02\x03",
            "#00200FIs it true that those autonomous states\x01",
            "also cannot agree to treaties?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02210F#5PNo, that's not the case.\x02\x03",
            "#02200FIt's true that each of them\x01",
            "have their own reasons for\x01",
            "not having formed a nation.\x02\x03",
            "However, for each of them an equal\x01",
            "sovereignity was recognized in the form\x01",
            "of an assignement from a "suzerain state".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FA suzerain state...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#00103FThose other autonomous states are definitely\x01",
            "different from Crossbell in that regard.\x02\x03",
            "#00101FThose statuses were recognized\x01",
            "by the "Holy Nation of Arteria".\x02",
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
            "#6P#10305FThe Holy Nation of Arteria is the\x01",
            "seat of the Septian Church, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00104FYes. Though their territory is small,\x01",
            "they have religious authority...\x02\x03",
            "#00100FMany autonomous states and free cities\x01",
            "were established relying on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FHowever, Crossbell is recognized as an\x01",
            ""autonomous state" by the Empire and Republic...\x02\x03",
            "#00001FIt's almost as if we have\x01",
            "two suzerain states.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FYes. And historically, that fact has\x01",
            "pulled us into various disasters.\x02\x03",
            "If Crossbell was given even a \x01",
            "little sovereignty, the situation\x01",
            "would slightly change.\x02\x03",
            "#00106F...But if it's those two countries that\x01",
            "have to agree on it, it'll never happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108F...No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#11PIt makes you want to give up, doesn't it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5P──Getting back to the main issue, it\x01",
            "seems the Chancellor and the President\x01",
            "each have their own security proposals.\x02\x03",
            "Naturally, the terms regarding each\x01",
            "of the countries aren't the same.\x02\x03",
            "#02201FThe Chairman and Mayor will need\x01",
            "to be vigilant and emphasize that.\x02",
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
            "#02210F#5PHa ha, sorry. It seems\x01",
            "I've made you worry.\x02\x03",
            "#02200FWell, Chairman MacDowell is\x01",
            "used to this sort of things.\x02\x03",
            "And it seems Mayor Dieter\x01",
            "has some kind of plan.\x02",
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
        "#11P#00105FWhat could it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F#5PAh, well I haven't heard\x01",
            "the details myself, but──\x02",
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
        "#11P#00000F──Excuse me.\x02",
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
            "#3455V#30W──Bannings. \x01",
            "The press conference is over.\x02\x03",
            "#3456VThe heads of state headed to 36F.\x01",
            "Where're you guys?\x02",
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
            "#00005FAh, right. We're in\x01",
            "the 34F break room.\x02\x03",
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
            "──It seems each of them would like to\x01",
            "speak with you directly during the break.\x02",
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
            "#00011F#4SWha──!?\x02",
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
            "Being who they are, I can't\x01",
            "very well turn them down.\x02\x03",
            "I want you to visit each\x01",
            "leader's room during the break.\x02\x03",
            "The deepest room in the left wing is the President's\x01",
            "and the one deepest in the right in the Chancellor's.\x02",
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
            "#00006FW-Wait a minute!\x01",
            "Why in the world...\x02\x03",
            "#00011FIt's way too much responsibility!\x02",
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
            "──Don't be naｼve, Bannings.\x02\x03",
            "Isn't this a good chance to look\x01",
            "into the motives of both sides?\x02",
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
            "#00003F...I understand. We'll head\x01",
            "for their rooms right away.\x02",
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
            "In case shit hits the fan, leave everything\x01",
            "to Elie. She's used to dealing with VIPs.\x02\x03",
            "Once you're finished, come report to me.\x02",
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
            "#00001FRoger...!\x02",
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
            "#12P#00305FYou were all over the place.\x01",
            "Is something goin' on?\x02",
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
            "Lloyd explained they had received invitations to speak\x01",
            "with Chancellor Osborne and President Rocksmith.\x07\x00\x02",
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
        "#6P#10305FWow, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PIt seems it is\x01",
            "no joke...\x02",
        )
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
            "#11P#00006FThat's not it... It's just that there're friends\x01",
            "of ours among each of the leaders' staffs.\x02\x03",
            "#00008FThey might have taken an\x01",
            "interest in us due to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FI see... \x01",
            "That's probably it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F...Even if that's the reason,\x01",
            "it's not like we can refuse.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00006FYou're right. Let's head to the left\x01",
            "and right wings deepest rooms on 36F.\x02\x03",
            "#00001FWe're visiting with them immediately.\x02",
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
        "#12P#10101FY-Yes sir!\x02",
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

    # Function_57_9D53 end

    def Function_58_C174(): pass

    label("Function_58_C174")

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
        "#6PW-What the heck!?\x02",
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
            "#11PI-It's no good! Even if I push the\x01",
            "button, there's no response!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PUgh... What the heck\x01",
            "is happening here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#02105F#11PHey! What about\x01",
            "my scoop!?\x02",
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
        "#12PP-Please, don't ask the impossible!\x02",
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

    # Function_58_C174 end

    def Function_59_C6DC(): pass

    label("Function_59_C6DC")

    Sleep(600)

    def lambda_C6E4():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6E4)

    def lambda_C6FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C6FE)
    WaitChrThread(0xFE, 1)

    def lambda_C713():
        OP_95(0xFE, -51100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C713)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_59_C6DC end

    def Function_60_C734(): pass

    label("Function_60_C734")


    def lambda_C739():
        OP_95(0xFE, -51000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C739)

    def lambda_C753():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C753)
    WaitChrThread(0xFE, 1)

    def lambda_C768():
        OP_95(0xFE, -52700, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C768)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_60_C734 end

    def Function_61_C789(): pass

    label("Function_61_C789")

    Sleep(1200)

    def lambda_C791():
        OP_95(0xFE, -52000, 0, -1000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C791)

    def lambda_C7AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C7AB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_61_C789 end

    def Function_62_C7C3(): pass

    label("Function_62_C7C3")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C7D0():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C7D0)

    def lambda_C7EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C7EA)
    WaitChrThread(0xFE, 1)

    def lambda_C7FF():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C7FF)
    WaitChrThread(0xFE, 1)

    def lambda_C81D():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C81D)
    WaitChrThread(0xFE, 1)

    def lambda_C83B():
        OP_95(0xFE, -53800, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C83B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(300)
    Return()

    # Function_62_C7C3 end

    def Function_63_C867(): pass

    label("Function_63_C867")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C877():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C877)

    def lambda_C891():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C891)
    WaitChrThread(0xFE, 1)

    def lambda_C8A6():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8A6)
    WaitChrThread(0xFE, 1)

    def lambda_C8C4():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8C4)
    WaitChrThread(0xFE, 1)

    def lambda_C8E2():
        OP_95(0xFE, -54200, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8E2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_63_C867 end

    def Function_64_C90B(): pass

    label("Function_64_C90B")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C91B():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C91B)

    def lambda_C935():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C935)
    WaitChrThread(0xFE, 1)

    def lambda_C94A():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C94A)
    WaitChrThread(0xFE, 1)

    def lambda_C968():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C968)
    WaitChrThread(0xFE, 1)

    def lambda_C986():
        OP_95(0xFE, -55100, 0, 700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C986)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_64_C90B end

    def Function_65_C9AF(): pass

    label("Function_65_C9AF")

    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C9BF():
        OP_95(0xFE, -51500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C9BF)

    def lambda_C9D9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C9D9)
    WaitChrThread(0xFE, 1)

    def lambda_C9EE():
        OP_95(0xFE, -55500, 0, 13000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C9EE)
    WaitChrThread(0xFE, 1)

    def lambda_CA0C():
        OP_95(0xFE, -55500, 0, 2500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA0C)
    WaitChrThread(0xFE, 1)

    def lambda_CA2A():
        OP_95(0xFE, -55800, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA2A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_65_C9AF end

    def Function_66_CA53(): pass

    label("Function_66_CA53")

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
        "#00011F"Cryptids"──you say?\x02",
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
            "──Yes, exactly.\x02\x03",
            "I'm hesitant to call them\x01",
            "simple monsters, as they\x01",
            "are large and mysterious.\x02\x03",
            "Monsters like that are\x01",
            "appearing all over Crossbell.\x02",
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

    def lambda_CED6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_CED6)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_71(0x11, 0x1, 0xA, 0x0, 0x0)
    OP_79(0x11)

    def lambda_CEFA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_CEFA)
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
            "#11PAh... \x01",
            "It's what we saw!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "#11PIn the end, it ran away before\x01",
            "we could finish it off...\x02",
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
            "#00206F#12P#NSuch information\x01",
            "has come in, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x26,
        (
            "#5P──That's not all. Other\x01",
            "types have been detected.\x02",
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
        "#6P#N#00007FT-That's!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#N#00101FThe thing that appeared in the old abandoned mine!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00307F#12P#NHey now, it showed up again!?\x02",
    )

    CloseMessageWindow()
    OP_93(0x26, 0xE1, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x26,
        (
            "#5PA few days ago, one of the same type\x01",
            "appeared in the northern mountain district.\x02",
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
            "#10105F#12P#NYou beat it with\x01",
            "just the two of you?\x02",
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
            "#5PYeah, we took it by surprise\x01",
            "and managed to defeat it.\x02",
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
        "#11PIt's just, it had a very strange response.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#11PArts had different effects on it and\x01",
            "it disappeared into a beam of light.\x02",
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
            "#00303F#6P#N...It seems exactly like \x01",
            "when we fought it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10303F#12P#NSpeaking of the mountain region...\x02\x03",
            "#10301FDid it appear outdoors this time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D49F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_D49F)
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
            "only in abnormal places like\x01",
            "the "Tower" or "Temple".\x02\x03",
            "We presume they spring forth\x01",
            "from "spatial distortions"\x01",
            "for some reason...\x02\x03",
            "#02001FHowever, these "Cryptids"\x01",
            "appeared in the mountain\x01",
            "and Marshlands areas.\x02\x03",
            "It's possible that these\x01",
            ""spatial distortions" are appearing\x01",
            "in such outdoor places as well.\x02",
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
        "#11PThat's the last thing I wanted to hear.\x02",
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
            "#5PYes. We are requesting the Bracer Guild\x01",
            "and the Special Support Section both\x01",
            "to deal with these Cryptids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PEver since the independence proposal,\x01",
            "the gates of Bellguard and Tangram have\x01",
            "been continuously in a state of high alert...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PWe've got to maintain that at least\x01",
            "until the referendum is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F#N...Understood. \x01",
            "Allow us to accept, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x21,
        (
            "#12PShould we decide how to divide\x01",
            "things amongst ourselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#02004F#5PYes. I'll provide you the data\x01",
            "and then leave it to you.\x02\x03",
            "#02001FAnd... If possible, I'd like you\x01",
            "to find the specific "cause."\x02",
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
            "#12P#N#00205FCause...?\x02\x03",
            "#00200FYou mean why those "Cryptids"\x01",
            "have suddenly appeared?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x25,
        (
            "#02003F#5PYes. For a long time,\x01",
            "monsters have appeared\x01",
            "in fixed cycles, but..\x02\x03",
            "#02001FIt's no exaggeration to say these\x01",
            ""Cryptids" represent an "abnormal\x01",
            "situation" with respect to those cycles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5P──There must be some\x01",
            "sort of cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x26,
        (
            "#5PWe mean the cause of these \x01",
            ""spatial distortions" that give rise\x01",
            "to these unusually large monsters.\x02",
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
            "#11PBy the name of the Guild,\x01",
            "I swear we'll solve this.\x02",
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

    # Function_66_CA53 end

    def Function_67_DC8F(): pass

    label("Function_67_DC8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E03C")
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
            "#12PBut we're on break right now...\x01",
            "Can't you...you know...somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6PYes. Except for pictures,\x01",
            "we won't do anything else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6PThat's right. If not, Senior will...\x02",
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
            "#6P#00012FThey'll go even though they\x01",
            "know it's not allowed.\x02\x03",
            "#00003FIt doesn't seem like they'll\x01",
            "forcibly break through though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10112FThat's just how reporters are, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FAnyway... It doesn't look\x01",
            "like we're getting through.\x02",
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
    Jump("loc_E0CE")

    label("loc_E03C")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reporters are blocking the\x01",
            "way to the elevator floor.\x02\x03",
            "It doesn't seem like you'll be\x01",
            "able to pass for awhile.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 29470, 0, -1200, 270)
    EventEnd(0x4)

    label("loc_E0CE")

    Return()

    # Function_67_DC8F end

    def Function_68_E0CF(): pass

    label("Function_68_E0CF")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E39F")
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
            "the ones in the front, huh.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_E29D")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the emergency\x01",
            "stairs, it seems these too are\x01",
            "controlled via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, looks that way.\x02\x03",
            "#00000FWhatever. When we need to move, \x01",
            "let's use the elevators in the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E397")

    label("loc_E29D")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, it seems the\x01",
            "lock mechanism is controlled\x01",
            "via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, I should expect that much from\x01",
            "the Orchis Tower security system.\x02\x03",
            "#00000FWhatever. When we need to move, \x01",
            "let's use the elevator in the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E397")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_E411")

    label("loc_E39F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x02\x03",
            "It seems you can't use this elevator\x01",
            "during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E411")

    TalkEnd(0xFF)
    Return()

    # Function_68_E0CF end

    def Function_69_E415(): pass

    label("Function_69_E415")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E695")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs' shutter\x01",
            "is firmly shut.\x07\x00\x02",
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
            "sealed during the conference.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_E5B7")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the elevator, \x01",
            "it seems these too are\x01",
            "controlled via the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPerfect security is impossible―\x01",
            "I remember hearing that.\x02\x03",
            "#00001FWe've got to keep that in the\x01",
            "back of our minds, just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E68D")

    label("loc_E5B7")


    ChrTalk(
        0x103,
        (
            "#00200FIt seems the shutter\x01",
            "lock is controlled\x01",
            "via the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FPerfect security is impossible―\x01",
            "I remember hearing that.\x02\x03",
            "#00001FWe've got to keep that in the\x01",
            "back of our minds, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E68D")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_E716")

    label("loc_E695")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs'\x01",
            "shutter is firmly shut.\x02\x03",
            "It seems you can't proceed to the next\x01",
            "floor during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E716")

    TalkEnd(0xFF)
    Return()

    # Function_69_E415 end

    def Function_70_E71A(): pass

    label("Function_70_E71A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_70_E71A end

    SaveToFile()

Try(main)
