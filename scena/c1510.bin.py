from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1510.bin",                # FileName
        "c1510",                    # MapName
        "c1510",                    # Location
        0x00AB,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 171, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1510",                  # 0
        "Receptionist Reirier",         # 1
        "Receptionist Viola",         # 2
        "Mollet chief",           # 3
        "Tajik",                 # 4
        "Tivo policing",           # 5
        "Receptionist Lanfi",         # 6
        "Roberts boss",           # 7
        "Researcher David",         # 8
        "Researcher Clay",           # 9
        "Mrs. Margaret",       # 10
        "Pierre deputy director",         # 11
        "Noel",                 # 12
        "Waji",                   # 13
        "Lisha",               # 14
        "Dudley investigator",         # 15
        "Policeman",                   # 16
        "City official staff",             # 17
        "City official staff",             # 18
        "Citizen",                   # 19
        "Citizen",                   # 20
        "tourist",                 # 21
        "Citizen",                   # 22
        "Trade quotient rezero",           # 23
        "Zejo policing officer",           # 24
        "Grace",               # 25
        "Raines",               # 26
        "Yona",                   # 27
        "Mayor of Dieter",         # 28
    ))

    AddCharChip((
        "chr/ch30500.itc",                   # 00
        "chr/ch28200.itc",                   # 01
        "chr/ch27400.itc",                   # 02
        "chr/ch30000.itc",                   # 03
        "chr/ch27600.itc",                   # 04
        "chr/ch28000.itc",                   # 05
        "chr/ch28102.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch21102.itc",                   # 08
        "chr/ch32300.itc",                   # 09
        "chr/ch33002.itc",                   # 0A
        "chr/ch27802.itc",                   # 0B
        "chr/ch06002.itc",                   # 0C
        "chr/ch28100.itc",                   # 0D
        "chr/ch27900.itc",                   # 0E
        "chr/ch29300.itc",                   # 0F
        "chr/ch32800.itc",                   # 10
        "chr/ch44000.itc",                   # 11
        "chr/ch02900.itc",                   # 12
        "chr/ch03100.itc",                   # 13
        "chr/ch03200.itc",                   # 14
        "chr/ch00900.itc",                   # 15
        "chr/ch06400.itc",                   # 16
        "chr/ch29400.itc",                   # 17
        "chr/ch06102.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       1000,    21600,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(8000,    1000,    17959,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294959296, 1000,    17959,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294952376, 150,     2880,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(2819,    0,       4294964886, 270,  261,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1500,    1000,    21600,   180,  385,  0x0, 0,   14,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294960527, 0,       2619,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(4294963477, 0,       4409,    180,  389,  0x0, 0,   23,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294963477, 0,       3019,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(7719,    0,       1889,    315,  389,  0x0, 0,   17,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(6719,    0,       2890,    135,  389,  0x0, 0,   22,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(4294967007, 0,       6699,    45,   389,  0x0, 0,   18,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(4294964687, 0,       4294966506, 180,  389,  0x0, 0,   19,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(4294963836, 0,       3950,    270,  389,  0x0, 0,   20,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(1830,    0,       4294965706, 180,  453,  0x0, 0,   21,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(3000,    0,       8380,    180,  385,  0x0, 0,   3,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(4294951217, 0,       589,     270,  385,  0x0, 0,   4,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294949717, 0,       589,     90,   385,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4280,    0,       7480,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(5179,    150,     6250,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(4294964027, 0,       4619,    0,    389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294952376, 150,     2880,    180,  389,  0x0, 0,   10,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5179,    150,     6250,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(78250,   0,       2650,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294952376, 150,     2880,    180,  389,  0x0, 0,   12,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(4294952376, 150,     1080,    0,    389,  0x0, 0,   13,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(5150,    0,       7150,    270,  389,  0x0, 0,   24,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 50,  74.94999694824219,     4.0,                   -1.0,                  20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -24.983333587646484,   -1.3333333730697632,   0.20000000298023224,   1.0])

    DeclActor(0,       1000,    20000,   1500,    0,       2500,    21600,   0x007E, 0,  6,  0x0000)
    DeclActor(6750,    1000,    18000,   1700,    8000,    2500,    17960,   0x007E, 0,  8,  0x0000)
    DeclActor(4294960546, 1000,    18000,   1700,    4294959296, 2500,    17960,   0x007E, 0,  10, 0x0000)
    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  40, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  40, 0x0000)
    DeclActor(4294954776, 0,       3040,    1200,    4294954776, 0,       3040,    0x007C, 0,  5,  0x0000)
    DeclActor(1500,    1000,    20000,   1500,    1500,    2500,    21600,   0x007E, 0,  12, 0x0000)
    DeclActor(1420,    0,       8550,    1500,    1420,    2000,    8550,    0x007C, 0,  52, 0x0000)

    ChipFrameInfo(1648, 0)                                       # 0

    ScpFunction((
        "Function_0_670",          # 00, 0
        "Function_1_720",          # 01, 1
        "Function_2_7FE",          # 02, 2
        "Function_3_A87",          # 03, 3
        "Function_4_CE4",          # 04, 4
        "Function_5_E25",          # 05, 5
        "Function_6_EC4",          # 06, 6
        "Function_7_EC8",          # 07, 7
        "Function_8_1CD1",         # 08, 8
        "Function_9_1CD5",         # 09, 9
        "Function_10_28E2",        # 0A, 10
        "Function_11_28E6",        # 0B, 11
        "Function_12_357D",        # 0C, 12
        "Function_13_3581",        # 0D, 13
        "Function_14_3643",        # 0E, 14
        "Function_15_3A05",        # 0F, 15
        "Function_16_47DB",        # 10, 16
        "Function_17_488F",        # 11, 17
        "Function_18_49AA",        # 12, 18
        "Function_19_49FF",        # 13, 19
        "Function_20_4A46",        # 14, 20
        "Function_21_4AAE",        # 15, 21
        "Function_22_4B47",        # 16, 22
        "Function_23_5030",        # 17, 23
        "Function_24_50AE",        # 18, 24
        "Function_25_517F",        # 19, 25
        "Function_26_5219",        # 1A, 26
        "Function_27_5296",        # 1B, 27
        "Function_28_5515",        # 1C, 28
        "Function_29_55BF",        # 1D, 29
        "Function_30_5752",        # 1E, 30
        "Function_31_57BE",        # 1F, 31
        "Function_32_58DC",        # 20, 32
        "Function_33_6281",        # 21, 33
        "Function_34_665F",        # 22, 34
        "Function_35_6A58",        # 23, 35
        "Function_36_6AC0",        # 24, 36
        "Function_37_6CF8",        # 25, 37
        "Function_38_6FA7",        # 26, 38
        "Function_39_71D2",        # 27, 39
        "Function_40_73CC",        # 28, 40
        "Function_41_74C8",        # 29, 41
        "Function_42_74CF",        # 2A, 42
        "Function_43_8C7B",        # 2B, 43
        "Function_44_8CBF",        # 2C, 44
        "Function_45_909E",        # 2D, 45
        "Function_46_90D2",        # 2E, 46
        "Function_47_9123",        # 2F, 47
        "Function_48_974B",        # 30, 48
        "Function_49_9AA9",        # 31, 49
        "Function_50_A0CE",        # 32, 50
        "Function_51_A15F",        # 33, 51
        "Function_52_A26B",        # 34, 52
    ))


    def Function_0_670(): pass

    label("Function_0_670")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6A8"),
        (1, "loc_6B4"),
        (2, "loc_6C0"),
        (3, "loc_6CC"),
        (4, "loc_6D8"),
        (5, "loc_6E4"),
        (6, "loc_6F0"),
        (SWITCH_DEFAULT, "loc_6FC"),
    )


    label("loc_6A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_6FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_708")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_708")

    label("loc_71F")

    Return()

    # Function_0_670 end

    def Function_1_720(): pass

    label("Function_1_720")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FD")
    OP_95(0xFE, 3000, 0, -850, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -4000, 0, -850, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -4000, 0, 8380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -500, 0, 8380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 3000, 0, 8380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_1_720")

    label("loc_7FD")

    Return()

    # Function_1_720 end

    def Function_2_7FE(): pass

    label("Function_2_7FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_828")
    ClearScenarioFlags(0x25, 1)
    Call(0, 41)

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_892")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0xB)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_865")
    SetChrFlags(0x12, 0x10)

    label("loc_865")

    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_888")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_888")

    ClearChrFlags(0xE, 0x80)
    Jump("loc_A2B")

    label("loc_892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8BC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x1F, 0x80)
    Call(0, 4)
    Jump("loc_A2B")

    label("loc_8BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E3")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x1F, 0x80)
    Jump("loc_A2B")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_90C")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0xB)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    Jump("loc_A2B")

    label("loc_90C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_930")
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1D, 0xA)
    SetChrSubChip(0x1D, 0x0)
    EndChrThread(0x1D, 0x0)
    SetChrBattleFlags(0x1D, 0x4)
    Jump("loc_A2B")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_98E")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_989")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3810, 0, 8039, 135)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x22, 0x18)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)

    label("loc_989")

    Jump("loc_A2B")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9B2")
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    Jump("loc_A2B")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9D6")
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x8)
    SetChrSubChip(0x1B, 0x0)
    EndChrThread(0x1B, 0x0)
    SetChrBattleFlags(0x1B, 0x4)
    Jump("loc_A2B")

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A04")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x20, 0xC)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_A2B")

    label("loc_A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_A2B")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x1F, 0x80)

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A3F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 42)
    Jump("loc_A51")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A51")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x2, 2)
    Event(0, 49)

    label("loc_A51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A70")
    Event(0, 44)
    Jump("loc_A86")

    label("loc_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A86")
    SetMapFlags(0x10000000)
    Event(0, 47)

    label("loc_A86")

    Return()

    # Function_2_7FE end

    def Function_3_A87(): pass

    label("Function_3_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9B")
    Sound(130, 1, 40, 0)

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_AB5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 2)
    Jump("loc_AC7")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AC7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC7")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1D")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)

    label("loc_B1D")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B41")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B54")
    OP_1B(0x0, 0x0, 0x33)

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B67")
    OP_1B(0x0, 0x0, 0x33)

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBB")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_C05")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C34")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_C90")

    label("loc_C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C73")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    Jump("loc_C90")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C90")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_C90")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CA6")
    OP_66(0x6, 0x1)
    Jump("loc_CCD")

    label("loc_CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CC0")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jump("loc_CCD")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CCD")
    OP_66(0x6, 0x1)

    label("loc_CCD")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE3")
    OP_66(0x7, 0x1)

    label("loc_CE3")

    Return()

    # Function_3_A87 end

    def Function_4_CE4(): pass

    label("Function_4_CE4")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearScenarioFlags(0x2, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_D44")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    SetChrPos(0x13, 3630, 0, 5580, 180)
    Jump("loc_D41")

    label("loc_D30")

    SetChrPos(0x13, 2410, 0, 6050, 180)

    label("loc_D41")

    SetScenarioFlags(0x2, 3)

    label("loc_D44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_D8D")
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")
    SetChrPos(0x14, 3630, 0, 5580, 180)
    Jump("loc_D8A")

    label("loc_D79")

    SetChrPos(0x14, 2410, 0, 6050, 180)

    label("loc_D8A")

    SetScenarioFlags(0x2, 3)

    label("loc_D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_DD6")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC2")
    SetChrPos(0x15, 3630, 0, 5580, 180)
    Jump("loc_DD3")

    label("loc_DC2")

    SetChrPos(0x15, 2410, 0, 6050, 180)

    label("loc_DD3")

    SetScenarioFlags(0x2, 3)

    label("loc_DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_E24")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E10")
    SetChrPos(0x16, 3630, 0, 5580, 180)
    Jump("loc_E21")

    label("loc_E10")

    SetChrPos(0x16, 2410, 0, 6050, 180)

    label("loc_E21")

    SetScenarioFlags(0x2, 3)

    label("loc_E24")

    Return()

    # Function_4_CE4 end

    def Function_5_E25(): pass

    label("Function_5_E25")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine \"Freewheeler Mach\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('凉爽色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC0")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Cool color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('凉爽色彩', 1)

    label("loc_EC0")

    TalkEnd(0xFF)
    Return()

    # Function_5_E25 end

    def Function_6_EC4(): pass

    label("Function_6_EC4")

    Call(0, 7)
    Return()

    # Function_6_EC4 end

    def Function_7_EC8(): pass

    label("Function_7_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDA")
    Call(0, 48)
    Return()

    label("loc_EDA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD7")

    ChrTalk(
        0x8,
        (
            "For the time being, the Orkis Tower\x01",
            "Under the leadership of McDowell\x01",
            "It was decided to be managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although there are still many confusion …\x01",
            "ここがCitizenのためのビルであることに\x01",
            "There is no change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please continue to\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1050")

    label("loc_FD7")


    ChrTalk(
        0x8,
        (
            "Orkis Tower\x01",
            "Citizenのためのビルであることに\x01",
            "There is no change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please continue to\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1050")

    Jump("loc_1CCD")

    label("loc_1055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1063")
    Jump("loc_1CCD")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1071")
    Jump("loc_1CCD")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(
        0x8,
        (
            "本日、Citizen会館では街の復興を\x01",
            "Support charity event\x01",
            "We are holding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone can smile,\x01",
            "Many such projects\x01",
            "Because we are preparing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have time to spare\x01",
            "Everyone please join us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E9")

    label("loc_1161")


    ChrTalk(
        0x8,
        (
            "Even so ……\x01",
            "To the early recovery of IBC\x01",
            "It was truly amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Technology of a power net\x01",
            "Even wonderfulness\x01",
            "It will be noticed again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E9")

    Jump("loc_1CCD")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_140D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1350")

    ChrTalk(
        0x8,
        (
            "Naturally ……\x01",
            "Citizenの皆さんの間にもかなり\x01",
            "It seems that shakes are spreading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the question of the incident etc,\x01",
            "Only by necessarily ambiguous things\x01",
            "I can not answer … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not only the guards, as well as the mayor and chairman\x01",
            "I will do my utmost to do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway now I believe in you,\x01",
            "Our staff too\x01",
            "I just do my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1408")

    label("loc_1350")


    ChrTalk(
        0x8,
        (
            "For the convergence of the situation,\x01",
            "Not only the guards, as well as the mayor and chairman\x01",
            "I will do my utmost to do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway now I believe in you,\x01",
            "Our staff too\x01",
            "I just do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1408")

    Jump("loc_1CCD")

    label("loc_140D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_157F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D3")

    ChrTalk(
        0x8,
        (
            "本日は、Citizen会館にて\x01",
            "The theme of 'independence of national independence'\x01",
            "Citizenフォーラムが開催中です。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Depending on the program\x01",
            "Since there seems to be some vacant seats,\x01",
            "If you are interested please join us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157A")

    label("loc_14D3")


    ChrTalk(
        0x8,
        (
            "The card you handed out\x01",
            "When holding over the panel inside the elevator\x01",
            "You can go up to the top floor 40F directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is disposable only effective for 1 month\x01",
            "Please use it freely after use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157A")

    Jump("loc_1CCD")

    label("loc_157F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170A")

    ChrTalk(
        0x8,
        (
            "Welcome.\x01",
            "If it was an inquiry about a train accident\x01",
            "I will show you around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Currently occurred in the West Crossbell Highway\x01",
            "Transcontinental railroad under the influence of a train accident\x01",
            "I temporarily stop running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The cause is still under investigation,\x01",
            "Regarding the prospect of recovery\x01",
            "It is in a state not attached at the present time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hurry towards the Empire and the Republic\x01",
            "If you are heading for a bus or airport\x01",
            "Please use it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179B")

    label("loc_170A")


    ChrTalk(
        0x8,
        (
            "Hurry towards the Empire and the Republic\x01",
            "If you are heading for a bus or airport\x01",
            "Please use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need it, this one\x01",
            "We will arrange tickets as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179B")

    Jump("loc_1CCD")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1918")

    ChrTalk(
        0x8,
        (
            "Currently, in Crossbell City with other countries\x01",
            "To promote cultural exchange\x01",
            "We are studying and studying various projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Crossbell's tourist PR corner and\x01",
            "Corner learning about foreign cultures and history,\x01",
            "Shops gathering local products from each country ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Citizenの皆様に、より有意義な\x01",
            "To provide services\x01",
            "All the staff struggle hard on a daily basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Orkis Tower\x01",
            "Please look forward to future developments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19B3")

    label("loc_1918")


    ChrTalk(
        0x8,
        (
            "Currently, in Crossbell City with other countries\x01",
            "To promote cultural exchange\x01",
            "We are studying and studying various projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Orkis Tower\x01",
            "Please look forward to future developments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B3")

    Jump("loc_1CCD")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAF")

    ChrTalk(
        0x8,
        "Welcome to the Orkis Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this general receptionist,\x01",
            "According to customer's consultation content\x01",
            "We have various guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From sightseeing information, medical and welfare etc.\x01",
            "Citizen生活に関するご相談まで、\x01",
            "Please contact us for anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B6B")

    label("loc_1AAF")


    ChrTalk(
        0x8,
        (
            "In this general receptionist,\x01",
            "According to customer's consultation content\x01",
            "I will do various guidance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From sightseeing information, medical and welfare etc.\x01",
            "Citizen生活に関するご相談まで、\x01",
            "Please contact us for anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6B")

    Jump("loc_1CCD")

    label("loc_1B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_1CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C50")

    ChrTalk(
        0x8,
        (
            "Everyone, thanks for your hard work.\x01",
            "こちらはThe Orkis Tower\x01",
            "It is a comprehensive receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Today all the staff,\x01",
            "According to instructions from the security office\x01",
            "We are going to hit various kinds of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When there is something,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CCD")

    label("loc_1C50")


    ChrTalk(
        0x8,
        (
            "All the staff today,\x01",
            "According to instructions from the security office\x01",
            "We are going to hit various kinds of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When there is something,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCD")

    TalkEnd(0x8)
    Return()

    # Function_7_EC8 end

    def Function_8_1CD1(): pass

    label("Function_8_1CD1")

    Call(0, 9)
    Return()

    # Function_8_1CD1 end

    def Function_9_1CD5(): pass

    label("Function_9_1CD5")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC5")

    ChrTalk(
        0x9,
        (
            "The creatures that appeared in the city,\x01",
            "It seems that all of them disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was also trapped in the tower\x01",
            "I really felt horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For the time being\x01",
            "I heard that it was not, never again\x01",
            "I do not want to feel this way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E5C")

    label("loc_1DC5")


    ChrTalk(
        0x9,
        (
            "I was also trapped in the tower\x01",
            "I really felt horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For the time being\x01",
            "I heard that it was not, never again\x01",
            "I do not want to feel this way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5C")

    Jump("loc_28DE")

    label("loc_1E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1E6F")
    Jump("loc_28DE")

    label("loc_1E6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E7D")
    Jump("loc_28DE")

    label("loc_1E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F90")

    ChrTalk(
        0x9,
        (
            "When I was attacked, I went to the basement\x01",
            "When you are evacuating in the open space\x01",
            "A collision occurred ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The sight that the armed group is approaching,\x01",
            "Anyway, it's awful\x01",
            "There was not a word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Fortunately this building\x01",
            "Somewhat safe … …\x01",
            "I really did not feel alive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2034")

    label("loc_1F90")


    ChrTalk(
        0x9,
        (
            "The sight that the armed group is approaching,\x01",
            "Anyway, it's awful\x01",
            "There was not a word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Fortunately this building\x01",
            "Somewhat safe … …\x01",
            "I really did not feel alive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2034")

    Jump("loc_28DE")

    label("loc_2039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_21EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2142")

    ChrTalk(
        0x9,
        (
            "If you are Ursula Hospital\x01",
            "It has been a bit noisy since last night\x01",
            "It seems that the situation is going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because the number of patients is enormous,\x01",
            "In the first place, human hands and various materials\x01",
            "It is a story that it is not enough ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am fighting hard on the scene\x01",
            "Given your hardships,\x01",
            "My head just falls.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E6")

    label("loc_2142")


    ChrTalk(
        0x9,
        (
            "Today, the city gives all the power\x01",
            "Various support measures for hospitals\x01",
            "I am taking it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am fighting hard on the scene\x01",
            "Given your hardships,\x01",
            "My head just falls.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E6")

    Jump("loc_28DE")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CC")

    ChrTalk(
        0x9,
        (
            "To the autonomous province due to the train accident\x01",
            "People who had been forced to stay\x01",
            "You seem to have started almost this morning, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Problems of compensation etc are future talks ……\x01",
            "For the time being, the restoration of the accident\x01",
            "It was really nice without prolonging it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_235F")

    label("loc_22CC")


    ChrTalk(
        0x9,
        (
            "Depending on the cause of the train accident\x01",
            "On the issue of compensation in the future\x01",
            "I have to think about it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For the time being, the restoration of the accident\x01",
            "It was really nice without prolonging it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235F")

    Jump("loc_28DE")

    label("loc_2364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2415")

    ChrTalk(
        0x9,
        (
            "I got in touch with you,\x01",
            "Transportation of injured passengers\x01",
            "It is said that it was done without any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tentatively I am relieved … …\x01",
            "I am worried about the scene of the accident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28DE")

    label("loc_2415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2559")

    ChrTalk(
        0x9,
        (
            "everyone is,\x01",
            "The meaning of the Orkis Tower's name\x01",
            "Do you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Orchis \"Orchid\" ……\x01",
            "One flower blooms on one stem\x01",
            "It is about beautiful flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words,\x01",
            "This building goes straight in the sky\x01",
            "Is it a growing one flower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huhu, if you think so\x01",
            "Do not you think it is the perfect name?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25FF")

    label("loc_2559")


    ChrTalk(
        0x9,
        (
            "Orchis \"Orchid\" ……\x01",
            "One flower blooms on one stem\x01",
            "It is about beautiful flowers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words,\x01",
            "This building goes straight in the sky\x01",
            "Is it a growing one flower?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FF")

    Jump("loc_28DE")

    label("loc_2604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_274C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B1")

    ChrTalk(
        0x9,
        (
            "Welcome,\x01",
            "This is the procedure of various administrative procedures\x01",
            "It is a reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Public fee payment and\x01",
            "Address change notification\x01",
            "Please use here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2747")

    label("loc_26B1")


    ChrTalk(
        0x9,
        (
            "We are dealing with this window\x01",
            "手続きの大半はCitizen会館でも\x01",
            "We accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can go to here\x01",
            "If you are in trouble, there are also people there\x01",
            "Please use it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2747")

    Jump("loc_28DE")

    label("loc_274C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_28DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283A")

    ChrTalk(
        0x9,
        (
            "In another hour,\x01",
            "The plenary session is about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "During the meeting, I am here\x01",
            "Mainly contact various staff of city officials\x01",
            "I'm planning to serve you ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What shall I say,\x01",
            "When thinking that it is involved in this and other events\x01",
            "I feel somewhat nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28DE")

    label("loc_283A")


    ChrTalk(
        0x9,
        (
            "Plenary meeting in one hour … …\x01",
            "Besides, after a while\x01",
            "Leaders are here … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I have another great job\x01",
            "I do not mean to,\x01",
            "I feel somewhat nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DE")

    TalkEnd(0x9)
    Return()

    # Function_9_1CD5 end

    def Function_10_28E2(): pass

    label("Function_10_28E2")

    Call(0, 11)
    Return()

    # Function_10_28E2 end

    def Function_11_28E6(): pass

    label("Function_11_28E6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")

    ChrTalk(
        0xA,
        (
            "It was restrained within the Orkis Tower\x01",
            "Staff members and defense forces were released all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Mostly in a rough workplace\x01",
            "In the state of post hoc processing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it is such a time,\x01",
            "Citizenのために\x01",
            "I have to work firmly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A7C")

    label("loc_29D0")


    ChrTalk(
        0xA,
        (
            "It was restrained within the Orkis Tower\x01",
            "Staff and defense forces are mostly workplaces\x01",
            "In the state of post hoc processing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because it is such a time,\x01",
            "Citizenのために\x01",
            "I have to work firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7C")

    Jump("loc_3579")

    label("loc_2A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A8F")
    Jump("loc_3579")

    label("loc_2A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A9D")
    Jump("loc_3579")

    label("loc_2A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB5")

    ChrTalk(
        0xA,
        (
            "Arios McRae …\x01",
            "He is indeed the hero of this crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I wonder how he cuts into an armed group\x01",
            "I saw this with my eyes, but only as wonderful\x01",
            "It was an unusual activity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it is an unexpected idea,\x01",
            "If he were there, the two major powers are not afraid … …\x01",
            "It really seemed so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C4A")

    label("loc_2BB5")


    ChrTalk(
        0xA,
        (
            "Arios McRae …\x01",
            "He is indeed the hero of this crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it is an unexpected idea,\x01",
            "If he were there, the two major powers are not afraid … …\x01",
            "It really seemed so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4A")

    Jump("loc_3579")

    label("loc_2C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D91")

    ChrTalk(
        0xA,
        (
            "If it's a story that I heard, apparently\x01",
            "The situation of the guard does not look good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the damage will expand further\x01",
            "Policeman隊の投入も考えられるけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just because of the defense of the city\x01",
            "It can not be dismissed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It seems that I am doing my best at each place now,\x01",
            "Dialogue and negotiation settlement\x01",
            "I have to make it realized whatever it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E49")

    label("loc_2D91")


    ChrTalk(
        0xA,
        (
            "It seems that I am doing my best at each place now,\x01",
            "Dialogue and negotiation settlement\x01",
            "I have to make it realized whatever it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It is difficult to contribute directly,\x01",
            "Our general affairs department person also\x01",
            "I will focus on various tasks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E49")

    Jump("loc_3579")

    label("loc_2E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_300A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F62")

    ChrTalk(
        0xA,
        (
            "Well, but the restoration of the railway\x01",
            "Somehow ended within yesterday\x01",
            "I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the train was stopped,\x01",
            "For various types of compensation for crossbell\x01",
            "It seems that it was growing up to the blue sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It worked all night.\x01",
            "I can not sleep with my legs facing the guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3005")

    label("loc_2F62")


    ChrTalk(
        0xA,
        (
            "If the train was stopped,\x01",
            "For various types of compensation for crossbell\x01",
            "It seems that it increased to the blue sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It worked all night.\x01",
            "I can not sleep with my legs facing the guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3005")

    Jump("loc_3579")

    label("loc_300A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3188")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F2")

    ChrTalk(
        0xA,
        (
            "To inform the occurrence of a train accident\x01",
            "Of course this person\x01",
            "I received it promptly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Also inquiries from various fields\x01",
            "In a situation where it arrives quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now replace the leadership\x01",
            "Guide and arranging for transportation and transportation\x01",
            "I'm just going where I am.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3183")

    label("loc_30F2")


    ChrTalk(
        0xA,
        (
            "Anyway it's a train accident\x01",
            "There are things that are rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The crossbell railway\x01",
            "Because the line of sight is good in line\x01",
            "Although accidents rarely happen ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3183")

    Jump("loc_3579")

    label("loc_3188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_324A")

    ChrTalk(
        0xA,
        (
            "The opening day of the city hall is open to the public\x01",
            "Citizenたちでこのエントランスが\x01",
            "Please be crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Huhu, I first entered the building\x01",
            "The expression that people seemed to be overwhelmed by\x01",
            "It was pleasant to watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3579")

    label("loc_324A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338A")

    ChrTalk(
        0xA,
        (
            "Oh, you guys at the trade meeting\x01",
            "He was in charge of security\x01",
            "Is not it a mission support department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, it's a good opportunity\x01",
            "I will explain, but this is\x01",
            "Be on the point of contacting the administration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Request for disclosure of various materials,\x01",
            "Inquiries to policies,\x01",
            "I accept it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, if something happens\x01",
            "You should always listen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_340B")

    label("loc_338A")


    ChrTalk(
        0xA,
        (
            "This is about the administration\x01",
            "It is a window for handling correspondence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Request for disclosure of various materials,\x01",
            "Inquiries to policies,\x01",
            "I accept it here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340B")

    Jump("loc_3579")

    label("loc_3410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_3579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F9")

    ChrTalk(
        0xA,
        (
            "Management and operation of the Orkis Tower\x01",
            "It is an important task of our general affairs department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Used for today's plenary session\x01",
            "Preparing the conference hall and various waiting rooms\x01",
            "It is our job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now I finally calmed down … …\x01",
            "I was busy until a while ago.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3579")

    label("loc_34F9")


    ChrTalk(
        0xA,
        (
            "Well, anyway a variety of things\x01",
            "It was nice to be in time for the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can not get rid of it until the end, but\x01",
            "Just waiting for the meeting to start.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3579")

    TalkEnd(0xA)
    Return()

    # Function_11_28E6 end

    def Function_12_357D(): pass

    label("Function_12_357D")

    Call(0, 13)
    Return()

    # Function_12_357D end

    def Function_13_3581(): pass

    label("Function_13_3581")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_358E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To exchange money\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35EA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_35EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360A")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_363A")

    label("loc_360A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_361E")
    Jump("loc_363A")

    label("loc_361E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_363A")

    Jump("loc_358E")

    label("loc_363F")

    TalkEnd(0xD)
    Return()

    # Function_13_3581 end

    def Function_14_3643(): pass

    label("Function_14_3643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_37BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3733")

    ChrTalk(
        0xD,
        (
            "IBC work also suspended ……\x01",
            "Half of staff members\x01",
            "We are staying at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As a person who worked for a long time at a bank\x01",
            "Dieter's restraint\x01",
            "It's too shocking ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We got over it too\x01",
            "You must go and see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_37BA")

    label("loc_3733")


    ChrTalk(
        0xD,
        (
            "IBC business but is stopped,\x01",
            "Cashing services of Sepisu only\x01",
            "We will continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Feel free to use when using\x01",
            "Please give a voice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BA")

    Jump("loc_3A04")

    label("loc_37BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394B")

    ChrTalk(
        0x102,
        (
            "#00100FGood work, Ranfi.\x02\x03",
            "Apparently the person who relocates the window\x01",
            "Oita, you seem to be calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "This is Ellie, this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, this one too\x01",
            "With the skill of Mr. Maríbel Governor\x01",
            "Thanks to excellent technical department staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "More than half of the staff,\x01",
            "In another building here\x01",
            "I am resuming normal work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please feel free to\x01",
            "Please tell me anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3A04")

    label("loc_394B")


    ChrTalk(
        0xD,
        (
            "IBC for the time being at this Orkis Tower\x01",
            "We will do business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Regarding the cash service of Sepis\x01",
            "Because you can use it as it is now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please feel free to\x01",
            "Please tell me anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A04")

    Return()

    # Function_14_3643 end

    def Function_15_3A05(): pass

    label("Function_15_3A05")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD0")

    ChrTalk(
        0xFE,
        (
            "Families and friends who were separated\x01",
            "It seems that we meet again one by one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a serious thing but … ….\x01",
            "After all these times, with important people\x01",
            "You must stay with me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B4C")

    label("loc_3AD0")


    ChrTalk(
        0xFE,
        (
            "By the way it was broken a little while ago\x01",
            "I brought the guided vehicle out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems she treated it carefully,\x01",
            "Please do it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B4C")

    Jump("loc_47D7")

    label("loc_3B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3B5F")
    Jump("loc_47D7")

    label("loc_3B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3B6D")
    Jump("loc_47D7")

    label("loc_3B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBB")

    ChrTalk(
        0xFE,
        (
            "The Orkis Tower,\x01",
            "Thanks to Arios' success\x01",
            "Something was okay … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "IBC building … literally\x01",
            "It disappeared without a trace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of the damage of civilians\x01",
            "It's a story though\x01",
            "Get involved in the alkane shell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know the show or something,\x01",
            "Whatever happens to such a thing\x01",
            "You can not be allowed to be forgiven.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D65")

    label("loc_3CBB")


    ChrTalk(
        0xFE,
        (
            "Most of the damage of civilians\x01",
            "It's a story though\x01",
            "Get involved in the alkane shell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know the show or something,\x01",
            "Whatever happens to such a thing\x01",
            "You can not be allowed to be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D65")

    Jump("loc_47D7")

    label("loc_3D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(
        0xFE,
        (
            "Both the mayor and the chairman have been staying since last night\x01",
            "In response to occupation cases\x01",
            "It looks like you are busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now for us in this situation\x01",
            "What you can do … … just prepare for emergencies\x01",
            "Is not it only to be distracted?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D7")

    label("loc_3E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F46")

    ChrTalk(
        0xFE,
        (
            "I caused a train accident yesterday\x01",
            "It's a story that things are different things ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it has appeared frequently these days\x01",
            "The existence of a phantom beast is still worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Near them,\x01",
            "I do not know well Blue flowers\x01",
            "It seems to have been confirmed, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is this …?\x01",
            "I wonder if it is a harbinger of further change?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FE0")

    label("loc_3F46")


    ChrTalk(
        0xFE,
        (
            "As I do not know the details,\x01",
            "Elephant beasts appear in the city\x01",
            "I can not say that it is not there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a creepy thing ….\x01",
            "In any case to be alert\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE0")

    Jump("loc_47D7")

    label("loc_3FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4058")

    ChrTalk(
        0xFE,
        "Driving train derailment accident, or …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that I am investigating the cause now,\x01",
            "I guess it is not terrorism … ….?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D7")

    label("loc_4058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C3")

    ChrTalk(
        0xFE,
        (
            "I am a police officer,\x01",
            "It is equivalent to city staff here\x01",
            "Treatment is guaranteed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So that's in the building\x01",
            "Cafe and dining room for staff only\x01",
            "You can use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The location is in the middle of the building,\x01",
            "Still more than the rooftop of IBC\x01",
            "It's in a high position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway the scenery is the best,\x01",
            "何だかCitizenの皆さんに対して\x01",
            "I feel sorry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_426D")

    label("loc_41C3")


    ChrTalk(
        0xFE,
        (
            "However, the cafe should preferably\x01",
            "早めにCitizenに開放しようという\x01",
            "The talk has also been raised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know when it will be,\x01",
            "It is always popular when that happens\x01",
            "I think it will be a spot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426D")

    Jump("loc_47D7")

    label("loc_4272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4347")

    ChrTalk(
        0xFE,
        (
            "Oh, it is a special affairs support department.\x01",
            "Welcome to Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have something to do\x01",
            "Ask the front receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "External humans\x01",
            "First we have to talk over there,\x01",
            "I can not do anything here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43C4")

    label("loc_4347")


    ChrTalk(
        0xFE,
        (
            "If you have something to do\x01",
            "Ask the front receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "External humans\x01",
            "First we have to talk over there,\x01",
            "I can not do anything here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C4")

    Jump("loc_47D7")

    label("loc_43C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_47D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4769")

    ChrTalk(
        0xFE,
        (
            "Mayor of Dieterから直接\x01",
            "To be able to guide the venue,\x01",
            "I'm a staff member of the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumors that the mayor's favorite\x01",
            "After all it was true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FEr, what is that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, never in a shit\x01",
            "I am not saying that\x01",
            "Do not get me wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I personally\x01",
            "Please support yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The place of holding is different,\x01",
            "In this way you can work together\x01",
            "I am pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F… what the heck,\x01",
            "It is a very different from half a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FThat's the first time you're a \"fake starter\"\x01",
            "It's a monkey monkey,\x01",
            "Because it is talking about being told variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, much from inside\x01",
            "It was stuck down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, surely before that\x01",
            "Some people are saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, now nobody\x01",
            "There is no one to say in such a way\x01",
            "I think that you can be relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway\x01",
            "Let 's do our best hard today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 0)
    Jump("loc_47D7")

    label("loc_4769")


    ChrTalk(
        0xFE,
        (
            "The place of holding is different,\x01",
            "Working with you guys\x01",
            "I am pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let 's do our best hard today.\x02",
    )

    CloseMessageWindow()

    label("loc_47D7")

    TalkEnd(0xFE)
    Return()

    # Function_15_3A05 end

    def Function_16_47DB(): pass

    label("Function_16_47DB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, as it is raining\x01",
            "I will not breathe out of the outside air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, but this entrance is\x01",
            "It's quite a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter what, the height of this ceiling is\x01",
            "It's open and cool.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_47DB end

    def Function_17_488F(): pass

    label("Function_17_488F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493C")

    ChrTalk(
        0xFE,
        (
            "12: 00--\x01",
            "Especially no abnormality was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The shadow reminiscent of terrorists\x01",
            "I do not feel the current situation yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From where the hell are you from\x01",
            "I wonder if they intend to enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49A6")

    label("loc_493C")


    ChrTalk(
        0xFE,
        (
            "The shadow reminiscent of terrorists\x01",
            "I do not feel the current situation yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From where the hell are you from\x01",
            "I wonder if they intend to enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A6")

    TalkEnd(0xFE)
    Return()

    # Function_17_488F end

    def Function_18_49AA(): pass

    label("Function_18_49AA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well then,\x01",
            "From that time to the VIP room\x01",
            "Is it meant to be off limits?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_49AA end

    def Function_19_49FF(): pass

    label("Function_19_49FF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, that's it.\x01",
            "Naturally, preparation is early and early\x01",
            "I will pass it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_49FF end

    def Function_20_4A46(): pass

    label("Function_20_4A46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5B")
    Call(0, 29)
    Jump("loc_4AAA")

    label("loc_4A5B")


    ChrTalk(
        0xFE,
        (
            "Kimitachi, you guys …\x01",
            "Eee, go over there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am busy right now!\x02",
    )

    CloseMessageWindow()

    label("loc_4AAA")

    TalkEnd(0xFE)
    Return()

    # Function_20_4A46 end

    def Function_21_4AAE(): pass

    label("Function_21_4AAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC3")
    Call(0, 31)
    Jump("loc_4B43")

    label("loc_4AC3")


    ChrTalk(
        0xFE,
        (
            "Roberts bossも来てくれてるし、\x01",
            "Trouble with conductivity net\x01",
            "You can handle anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, let's do it alone.\x02",
    )

    CloseMessageWindow()

    label("loc_4B43")

    TalkEnd(0xFE)
    Return()

    # Function_21_4AAE end

    def Function_22_4B47(): pass

    label("Function_22_4B47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C25")

    ChrTalk(
        0xFE,
        (
            "A little girl a while ago\x01",
            "To the elevator heading to the rooftop\x01",
            "I seem to have gone on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That girl surely,\x01",
            "It should have been the daughter of Secretary of Defense ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, it appeared in a wetland\x01",
            "I wonder if \"Taiki\" is concerned.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4CB6")

    label("loc_4C25")


    ChrTalk(
        0xFE,
        (
            "A little while ago, the daughter of the Secretary of Defense\x01",
            "To the elevator heading to the rooftop\x01",
            "I seem to have gone on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, it appeared in a wetland\x01",
            "I wonder if \"Taiki\" is concerned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB6")

    Jump("loc_502C")

    label("loc_4CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4CC9")
    Jump("loc_502C")

    label("loc_4CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CD7")
    Jump("loc_502C")

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D40")

    ChrTalk(
        0xFE,
        (
            "Behind the \"red constellation\"\x01",
            "Of course, the Imperial Government … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, it is not a tolerable story.\x02",
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D89")

    ChrTalk(
        0xFE,
        (
            "\"Red constellation\" … again\x01",
            "It sounds like they are not ordinary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_END)), "loc_4DF4")

    ChrTalk(
        0xFE,
        "Everyone, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When going to the upper floor, just before the entrance\x01",
            "Please use the elevator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4E67")

    ChrTalk(
        0xFE,
        "Hmm, is the weather today rainy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, according to the power net\x01",
            "It is said that it will clear up in the afternoon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F04")

    ChrTalk(
        0xFE,
        (
            "Hmm, with crossbells\x01",
            "It is unusual for a train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Derail means that the load\x01",
            "That means it took just that … ….\x01",
            "What on earth is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F8A")

    ChrTalk(
        0xFE,
        (
            "Whatever the Orkis Tower said\x01",
            "This spacious space is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, really,\x01",
            "I think that it is a luxuriously built building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_4F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5023")

    ChrTalk(
        0xFE,
        (
            "The Orkis Tower\x01",
            "At the present time the speed of the elevator\x01",
            "It is a touch with the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because there is almost no shake,\x01",
            "I can not really feel it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502C")

    label("loc_5023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_502C")

    label("loc_502C")

    TalkEnd(0xFE)
    Return()

    # Function_22_4B47 end

    def Function_23_5030(): pass

    label("Function_23_5030")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Huh, that's amazing ……\x01",
            "これがThe Orkis Tower\x01",
            "Entrance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It comes out as if it were a science fiction novel\x01",
            "I feel like I am a future person.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_5030 end

    def Function_24_50AE(): pass

    label("Function_24_50AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_511B")

    ChrTalk(
        0xFE,
        (
            "I asked the staff,\x01",
            "Anything a train\x01",
            "Did you derail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What on earth is the cause?\x02",
    )

    CloseMessageWindow()
    Jump("loc_517B")

    label("loc_511B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_517B")

    ChrTalk(
        0xFE,
        (
            "Auntie first time came, but\x01",
            "It is really amazing space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel somewhat out of place.\x02",
    )

    CloseMessageWindow()

    label("loc_517B")

    TalkEnd(0xFE)
    Return()

    # Function_24_50AE end

    def Function_25_517F(): pass

    label("Function_25_517F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is cool\x01",
            "Why is a high-tech building a city hall?\x01",
            "It is quite severe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of the independent advocacy,\x01",
            "Someday I may like to immigrate to the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_517F end

    def Function_26_5219(): pass

    label("Function_26_5219")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, under the incident of Mainz\x01",
            "The city government seems to be a bit noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Early place, finish errands\x01",
            "I suppose I should go home early ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_5219 end

    def Function_27_5296(): pass

    label("Function_27_5296")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5396")

    ChrTalk(
        0xFE,
        (
            "IBC, the president who was president\x01",
            "Daughter who was acting as president\x01",
            "It seems that it has gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that it will have a great impact on future stock price … …\x01",
            "The capital strength of the continent will not be shaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until the next president is decided,\x01",
            "I guess I will see a state for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5422")

    label("loc_5396")


    ChrTalk(
        0xFE,
        (
            "It seems that it will have a great impact on future stock price … …\x01",
            "The capital strength of the continent will not be shaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until the next president is decided,\x01",
            "I guess I will see a state for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5422")

    Jump("loc_5511")

    label("loc_5427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5435")
    Jump("loc_5511")

    label("loc_5435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5511")

    ChrTalk(
        0xFE,
        (
            "No way, from a while ago\x01",
            "Customer information to Orkis Tower\x01",
            "I was backing up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ideal for IBC …\x01",
            "It's a great deal of crisis management ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Over the years the continental economy\x01",
            "The achievements that we have supported\x01",
            "It sounds like it was not Date.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5511")

    TalkEnd(0xFE)
    Return()

    # Function_27_5296 end

    def Function_28_5515(): pass

    label("Function_28_5515")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552A")
    Call(0, 29)
    Jump("loc_55BB")

    label("loc_552A")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "…… As a worrying cross,\x01",
            "Pocket money for next month is 50 cut.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        "Okay, I am sorry about that …!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)

    label("loc_55BB")

    TalkEnd(0xFE)
    Return()

    # Function_28_5515 end

    def Function_29_55BF(): pass

    label("Function_29_55BF")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "In fact, you are a\x01",
            "It took extra care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "But, but Margaret.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "After all, as Deputy Director of the police,\x01",
            "The time to stand up\x01",
            "I have it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Such as usual\x01",
            "It should be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Because I do things that suddenly do not suit,\x01",
            "It is caught up in such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "…… Su, sorry.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5741")

    ChrTalk(
        0x101,
        "#00012F(Oh, it's as grave as ever … …)\x02",
    )

    CloseMessageWindow()

    label("loc_5741")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_29_55BF end

    def Function_30_5752(): pass

    label("Function_30_5752")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5767")
    Call(0, 31)
    Jump("loc_57BA")

    label("loc_5767")


    ChrTalk(
        0xFE,
        (
            "After all I am working with Aibo\x01",
            "I feel good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Shall I start swimming?\x02",
    )

    CloseMessageWindow()

    label("loc_57BA")

    TalkEnd(0xFE)
    Return()

    # Function_30_5752 end

    def Function_31_57BE(): pass

    label("Function_31_57BE")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        (
            "Well then, immediately on the power of the net\x01",
            "Let's check.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It was a blue moya when the monster was walking around,\x01",
            "Communication was getting harder to connect.\x01",
            "The system may have been affected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Ok, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Then, first from the terminal of the tower\x01",
            "Would you like to test the operation?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_31_57BE end

    def Function_32_58DC(): pass

    label("Function_32_58DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD8")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Tio … …\x01",
            "You're heading for that \"big tree\", is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Tio has anything ……\x01",
            "If you think so, your body will be torn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F…… Chief, not too worried - ─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Hah, that's right!\x01",
            "I also have a magician to you guys\x01",
            "How about going with you! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the mechanism of the magician,\x01",
            "Support craft in battle\x01",
            "You may be able to help Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes yeah, that is good!\x01",
            "Once you decide so, prepare ready … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211FIt's fine as it's too usable.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ADE")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5ADE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B04")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B2A")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B50")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B50")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F(… as usual …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F…… Chief, do not worry too much\x01",
            "Do not overdo it.\x02\x03",
            "#00202FAlong with you and Kea,\x01",
            "I'm sure I will return safely.\x02\x03",
            "Besides, the role of the boss is\x01",
            "I wonder if it is in the city that is confusing to the last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Te, Tio … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……Yeah,\x01",
            "If Tio said so ……\x01",
            "I will concentrate on working here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead, promise me.\x01",
            "I will definitely come home safely!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 3)
    Jump("loc_5FE5")

    label("loc_5CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F21")

    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "Doctor with \"association\"\x01",
            "You say you left with a white doll?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FYeah … honestly and again\x01",
            "I do not want to get involved.\x02\x03",
            "#00211FCompared to such a person, the chief is\x01",
            "It seems like Mashi about 1000 times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Te, Tio! (Ji-din ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(To be compared only with\x01",
            "It seems delicious whether it is nice … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But \"Iron\"? ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F… …. Chief?\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ahaha, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(I am developing it with \"Eion system\" and\x01",
            "It sounds like the same etymology … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(… … It is a coincidence, is not it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5FE5")

    label("loc_5F21")


    ChrTalk(
        0xFE,
        (
            "Here I am\x01",
            "I am waiting for everyone's return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually I want to follow ….\x01",
            "If Tio declined it\x01",
            "As it can not be helped indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Instead, promise me.\x01",
            "I will definitely come home safely!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE5")

    Jump("loc_627D")

    label("loc_5FEA")

    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F6")

    ChrTalk(
        0xFE,
        (
            "Well, if it is true\x01",
            "Detailed situation of wetlands\x01",
            "I wish I knew … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Oh, somewhat suddenly\x01",
            "I got worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a strange place\x01",
            "To send Tio you …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FMen's fighters\x01",
            "It is to take it back safely.\x02\x03",
            "Do not worry too much about your boss\x01",
            "Please wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio … …\x01",
            "It became really good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I came to the Foundation so much\x01",
            "Even though it was small …\x01",
            "Uh, I cried somehow ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F…… Because it is annoying,\x01",
            "Seriously crying in such a place\x01",
            "stop it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_627D")

    label("loc_61F6")


    ChrTalk(
        0xFE,
        (
            "In an unfamiliar place\x01",
            "To send out Tio,\x01",
            "I can not help worrying … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio also became fine.\x01",
            "Surely it's okay! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_627D")

    TalkEnd(0xFE)
    Return()

    # Function_32_58DC end

    def Function_33_6281(): pass

    label("Function_33_6281")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B9")

    ChrTalk(
        0x22,
        (
            "#02302FThat reminds me … …\x01",
            "\"Pomutto! Account\x01",
            "You have it?\x02\x03",
            "#02304Fフフン、折角だからこのYona様の\x01",
            "I will give you an account.\x02\x03",
            "#02302FI was involved from the development stage\x01",
            "If you can win, try winning.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『Yonaのアカウント』\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_665B")

    label("loc_63B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65E9")

    ChrTalk(
        0x22,
        (
            "#02306FStormola walking in the rain,\x01",
            "I was getting tired after all.\x02\x03",
            "#02300FBefore returning to the branch of the Foundation\x01",
            "I should say I'm da.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FCome on … …\x01",
            "There is no elevator to the rooftop.\x01",
            "You did not have such a big exercise, did you?\x02\x03",
            "#00001FIt is not good to have too little exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F仕方ありません、Yonaは\x01",
            "Moyager's syndrome#6Rsyndrome#Therefore.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x22,
        (
            "#02310FHey, what is it,\x01",
            "The syndrome is …\x02\x03",
            "#02306FHun, exactly ….\x01",
            "If you go to a wetland\x01",
            "I can not go wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I will let you.\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_665B")

    label("loc_65E9")


    ChrTalk(
        0x22,
        (
            "#02303FI can not stop thinking\x01",
            "Let's say I'm going home after dandelion.\x02\x03",
            "#02301Fアンタらも、If you go to a wetland\x01",
            "I can not go wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665B")

    TalkEnd(0xFE)
    Return()

    # Function_33_6281 end

    def Function_34_665F(): pass

    label("Function_34_665F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6905")

    ChrTalk(
        0x20,
        (
            "#02100FOh, Lloyd guys.\x01",
            "You look as busy as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FGraceさんたちは\x01",
            "Is it Congress's interview or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02109FYour opinion, this time newly voted\x01",
            "In an interview about the bill ~.\x02\x03",
            "In addition, from various lawmakers\x01",
            "For each state against national independence\x01",
            "I'm planning to ask some ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIndeed, social stuff is also\x01",
            "It is a feeling in the middle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02106FYes, that's right.\x02\x03",
            "The direction of the political world also recently\x01",
            "There is little scandal\x01",
            "I mean boring … …\x02\x03",
            "#02102FWell, somewhere\x01",
            "Good gossip story\x01",
            "I wonder if they are not rolling?\x02",
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
        "#00006FIs there worrying … ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 7)
    Jump("loc_6A54")

    label("loc_6905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B8")

    ChrTalk(
        0x20,
        (
            "#02106FThere are few scandals\x01",
            "It's good to be good,\x01",
            "Recently gossip story is weak, is not it ~.\x02\x03",
            "#02102FWell, somewhere good story\x01",
            "I wonder if they are not rolling?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A37")

    label("loc_69B8")


    ChrTalk(
        0x20,
        (
            "#02100FOh, that's right.\x01",
            "Once a sticky gourmet is gathered\x01",
            "Please call at the receptionist of the correspondent.\x02\x03",
            "#02109FWell then, I asked for your best regards ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 5)

    label("loc_6A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6A54")
    ClearScenarioFlags(0x0, 5)

    label("loc_6A54")

    TalkEnd(0xFE)
    Return()

    # Function_34_665F end

    def Function_35_6A58(): pass

    label("Function_35_6A58")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grace先輩……議員の方に\x01",
            "I do not have to ask strange things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The role of safety equipment is also serious.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_6A58 end

    def Function_36_6AC0(): pass

    label("Function_36_6AC0")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ACD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B76")

    ChrTalk(
        0x13,
        (
            "#10100FIt is a member organization, is not it?\x01",
            "OK!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_6CEF")

    label("loc_6B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B8A")
    Jump("loc_6CEF")

    label("loc_6B8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C89")

    ChrTalk(
        0x13,
        (
            "#10100FIt is broken gently but ….\x01",
            "Various functions seem to be alive.\x02\x03",
            "Once things are settled down,\x01",
            "I surely want to repair it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FI agree……\x01",
            "Roberts bossやギヨーム親方にも\x01",
            "Let me help you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_6CEF")

    label("loc_6C89")


    ChrTalk(
        0x13,
        (
            "#10100FVarious functions seem to be alive.\x02\x03",
            "Once things are settled down,\x01",
            "I surely want to repair it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CEF")

    Jump("loc_6ACD")

    label("loc_6CF4")

    TalkEnd(0xFE)
    Return()

    # Function_36_6AC0 end

    def Function_37_6CF8(): pass

    label("Function_37_6CF8")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FA3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA9")

    ChrTalk(
        0x14,
        "#10400FHuh, you change your members?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_6F9E")

    label("loc_6DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DBD")
    Jump("loc_6F9E")

    label("loc_6DBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF0")

    ChrTalk(
        0x14,
        (
            "#10406FEven if you defeat it or defeat it,\x01",
            "New people innocently come up … …\x02\x03",
            "Whew, troublesome things\x01",
            "It was used.\x02\x03",
            "#10401FAs long as you are going outside\x01",
            "It will only be exhausted … …\x01",
            "Should I hurry up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FYes, get to your uncle early\x01",
            "I have to stop doing like this … !.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_6F9E")

    label("loc_6EF0")


    ChrTalk(
        0x14,
        (
            "#10406FEven if you defeat it or defeat it,\x01",
            "New people innocently come up … …\x01",
            "Boy, it is a troublesome person.\x02\x03",
            "#10401FAs long as you are going outside\x01",
            "It will only be exhausted … …\x01",
            "Should I hurry up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9E")

    Jump("loc_6D05")

    label("loc_6FA3")

    TalkEnd(0xFE)
    Return()

    # Function_37_6CF8 end

    def Function_38_6FA7(): pass

    label("Function_38_6FA7")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71CE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705C")

    ChrTalk(
        0x15,
        "#10702FYes, you change members.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_71C9")

    label("loc_705C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7070")
    Jump("loc_71C9")

    label("loc_7070")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7165")

    ChrTalk(
        0x15,
        (
            "#10703FFor now, in this lobby\x01",
            "There is no sign of the enemy … …\x02\x03",
            "It is better not to neglect vigilance\x01",
            "Looks nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FShould I have enough in the unlikely event …\x01",
            "頼むぜ、Lishaちゃん。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#10702FWell, leave it to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_71C9")

    label("loc_7165")


    ChrTalk(
        0x15,
        (
            "#10703FJust to be sure, around\x01",
            "Those who care about it\x01",
            "Looks nice.\x02\x03",
            "#10701FPlease also take care of everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71C9")

    Jump("loc_6FB4")

    label("loc_71CE")

    TalkEnd(0xFE)
    Return()

    # Function_38_6FA7 end

    def Function_39_71D2(): pass

    label("Function_39_71D2")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "Party organization\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7298")

    ChrTalk(
        0x16,
        (
            "#00600FDo you change members?\x01",
            "… … Choose quickly.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 4)
    OP_0D()
    Jump("loc_73C3")

    label("loc_7298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72AC")
    Jump("loc_73C3")

    label("loc_72AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7381")

    ChrTalk(
        0x16,
        (
            "#00603FAs a meeting,\x01",
            "In case of emergency\x01",
            "We will keep the entrance with two people waiting.\x02\x03",
            "#00601F…… Now, do not hold back.\x01",
            "You should go quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F……Yes!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_73C3")

    label("loc_7381")


    ChrTalk(
        0x16,
        (
            "#00601F…… Now, do not hold back.\x01",
            "You ought to go quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C3")

    Jump("loc_71DF")

    label("loc_73C8")

    TalkEnd(0xFE)
    Return()

    # Function_39_71D2 end

    def Function_40_73CC(): pass

    label("Function_40_73CC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7427")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator\x01",
            "It seems that it is in use on another floor,\x01",
            "There is no sign of stopping.\x07\x00\x02",
        )
    )

    Jump("loc_74C0")

    label("loc_7427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7472")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x07\x00\x02",
        )
    )

    Jump("loc_74C0")

    label("loc_7472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_74C0")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator\x01",
            "It seems that it is in use on another floor,\x01",
            "There is no sign of stopping.\x07\x00\x02",
        )
    )


    label("loc_74C0")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_73CC end

    def Function_41_74C8(): pass

    label("Function_41_74C8")

    Sound(160, 0, 100, 0)
    Return()

    # Function_41_74C8 end

    def Function_42_74CF(): pass

    label("Function_42_74CF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch05600.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    SoundLoad(3454)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    SetChrPos(0x101, 400, 0, -6100, 0)
    SetChrPos(0x102, -1200, 0, -6900, 0)
    SetChrPos(0x103, 1200, 0, -6900, 0)
    SetChrPos(0x104, 1200, 0, -8500, 0)
    SetChrPos(0x109, -1200, 0, -8500, 0)
    SetChrPos(0x105, -400, 0, -9300, 0)
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
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 15500, 0, 1000, 270)
    OP_4B(0x16, 0xFF)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 15500, 0, 1000, 270)
    OP_68(0, 4500, 17500, 0)
    MoveCamera(27, 5, 0, 0)
    OP_6E(690, 0)
    SetCameraDistance(27000, 0)
    OP_68(0, 2000, 7500, 7000)
    MoveCamera(23, 5, 0, 7000)
    FadeToBright(2000, 0)
    Sleep(4000)

    def lambda_76AE():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_76AE)
    Sleep(200)

    def lambda_76CB():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_76CB)
    Sleep(200)

    def lambda_76E8():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_76E8)
    Sleep(200)

    def lambda_7705():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7705)
    Sleep(200)

    def lambda_7722():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7722)
    Sleep(200)

    def lambda_773F():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_773F)
    Sleep(100)

    def lambda_775C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_775C)
    Sleep(300)

    def lambda_7770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7770)
    Sleep(200)

    def lambda_7784():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7784)
    Sleep(600)

    def lambda_7798():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7798)
    Sleep(200)

    def lambda_77AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_77AC)
    Sleep(300)

    def lambda_77C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_77C0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#11PAmazing\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PSomehow, luxurious\x01",
            "It feels like hi-tech …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PBeyond IBC Building\x01",
            "It is a futuristic atmosphere, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PCertainly on the whole floor of the building\x01",
            "The power net should be drawn.\x02\x03",
            "#00200FBecause it is also linked with IBC\x01",
            "Data such as stock price index\x01",
            "Can you refer in real time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PYeah, that is where\x01",
            "It looks like an uncle's idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PIndeed, unique to bankers\x01",
            "It is a conception.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(670, 1000, -1310, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17580, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#5PAll right, then\x01",
            "Until Dudley comes\x01",
            "Will you keep me waiting?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A18():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7A18)
    Sleep(50)

    def lambda_7A28():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7A28)
    Sleep(50)

    def lambda_7A38():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A38)
    Sleep(50)

    def lambda_7A48():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7A48)
    Sleep(50)

    def lambda_7A58():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7A58)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#6P#00102FThere are no ordinary guests today,\x01",
            "On that sofa\x01",
            "Let me wait.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_68(4500, 900, 7600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 3300, 0, 6700, 90)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrPos(0x102, 5200, 50, 6500, 270)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5200, 50, 7600, 270)
    SetChrPos(0x104, 2700, 0, 7700, 90)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, 5200, 50, 8700, 270)
    SetChrPos(0x105, 3000, 0, 9100, 135)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KSame day, 12: 00 -\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7111", 0)
    SetCameraDistance(18500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x16, 0x80)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x16,
        "Voice of a man",
        "#3454V#30W#11A─ ─ Are you coming?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 43)

    def lambda_7CAB():

        label("loc_7CAB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7CAB")

    QueueWorkItem2(0x101, 2, lambda_7CAB)
    Sleep(50)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 5000, 0, 6500, 270)

    def lambda_7CE4():

        label("loc_7CE4")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7CE4")

    QueueWorkItem2(0x102, 2, lambda_7CE4)
    Sleep(50)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5000, 0, 7600, 270)

    def lambda_7D17():

        label("loc_7D17")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D17")

    QueueWorkItem2(0x103, 2, lambda_7D17)
    Sleep(50)

    def lambda_7D2C():

        label("loc_7D2C")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D2C")

    QueueWorkItem2(0x104, 2, lambda_7D2C)
    Sleep(50)

    def lambda_7D41():

        label("loc_7D41")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D41")

    QueueWorkItem2(0x105, 2, lambda_7D41)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 5000, 0, 8700, 270)

    def lambda_7D71():
        OP_95(0xFE, 4500, 0, 8700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7D71)
    WaitChrThread(0x109, 1)

    def lambda_7D8F():

        label("loc_7D8F")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_7D8F")

    QueueWorkItem2(0x109, 2, lambda_7D8F)
    Sleep(300)
    Fade(500)
    OP_68(10500, 900, 1000, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(4000, 900, 6200, 4500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00000F#5PMr. Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00104FIs cheers for good work.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x16, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x16,
        (
            "Currently, just around noon ──\x02\x03",
            "The commerce meeting begins\x01",
            "It is 13:00.\x02\x03",
            "After 30 minutes\x01",
            "The leaders will come.\x02",
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

    ChrTalk(
        0x101,
        "#00001F#5PI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FSo, our people\x01",
            "Which way to head?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12P#00606FIf true, I will move around the hall\x01",
            "I intended to guide you lightly … …\x02\x03",
            "An unexpected person tells you\x01",
            "Offered to show me around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PAn unexpected person …\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)

    NpcTalk(
        0x23,
        "Male voice",
        (
            "── Hi everyone.\x01",
            "You came often.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(7800, 1000, 1000, 3000)
    MoveCamera(75, 21, 0, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_8103():
        OP_95(0xFE, 7800, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8103)

    def lambda_811D():

        label("loc_811D")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_811D")

    QueueWorkItem2(0x101, 2, lambda_811D)

    def lambda_812F():

        label("loc_812F")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_812F")

    QueueWorkItem2(0x102, 2, lambda_812F)

    def lambda_8141():

        label("loc_8141")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8141")

    QueueWorkItem2(0x103, 2, lambda_8141)

    def lambda_8153():

        label("loc_8153")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8153")

    QueueWorkItem2(0x104, 2, lambda_8153)

    def lambda_8165():

        label("loc_8165")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8165")

    QueueWorkItem2(0x109, 2, lambda_8165)

    def lambda_8177():

        label("loc_8177")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8177")

    QueueWorkItem2(0x105, 2, lambda_8177)

    def lambda_8189():

        label("loc_8189")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8189")

    QueueWorkItem2(0x16, 2, lambda_8189)
    WaitChrThread(0x23, 1)
    TurnDirection(0x23, 0x101, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FMayor of Dieter！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105Funcle……!\x02",
    )

    CloseMessageWindow()

    def lambda_81E2():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_81E2)
    Sleep(1000)
    Fade(500)
    OP_68(4000, 900, 6200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_8232():
        OP_96(0xFE, 0x898, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8232)
    WaitChrThread(0x23, 1)
    OP_93(0x23, 0x0, 0x1F4)
    EndChrThread(0x16, 0x2)
    EndChrThread(0x101, 0x2)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x23,
        (
            "It's been half a month ago,\x01",
            "Eli, Lloyd.\x02\x03",
            "Waji君にNoel君に……\x02\x03",
            "Oops, with Randy\x01",
            "Did you see Tio for a long time?\x02",
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
        0x104,
        "#00309F#5PHaha, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00204Flong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PBut why is your uncle … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PJust before the trade meeting\x01",
            "Are not you busy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#12P#02804FIf you are ready finish it\x01",
            "Then just wait for the leaders.\x02\x03",
            "#02800FYou guys also change your mood\x01",
            "I thought I'd let you show me around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x16, 500)
    Sleep(150)

    ChrTalk(
        0x23,
        "#02800F#11PDo not you mind, Dudley?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#6P#00606FFu … … If the mayor says so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x16,
        (
            "#6P#00600F─ ─ you guys\x01",
            "Do not be rude to the mayor.\x02\x03",
            "Also, once you are guided\x01",
            "Come to the security office of 34F.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 500)

    ChrTalk(
        0x101,
        "#5P#00000FOK.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x23, 500)
    Sleep(300)

    ChrTalk(
        0x16,
        "#6P#00603FSo mayor, later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02800F#11POh, I beg you to do my best.\x02",
    )

    CloseMessageWindow()

    def lambda_85DD():

        label("loc_85DD")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_85DD")

    QueueWorkItem2(0x101, 2, lambda_85DD)

    def lambda_85EF():

        label("loc_85EF")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_85EF")

    QueueWorkItem2(0x102, 2, lambda_85EF)

    def lambda_8601():

        label("loc_8601")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8601")

    QueueWorkItem2(0x103, 2, lambda_8601)

    def lambda_8613():

        label("loc_8613")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8613")

    QueueWorkItem2(0x104, 2, lambda_8613)

    def lambda_8625():

        label("loc_8625")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8625")

    QueueWorkItem2(0x109, 2, lambda_8625)

    def lambda_8637():

        label("loc_8637")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8637")

    QueueWorkItem2(0x105, 2, lambda_8637)

    def lambda_8649():

        label("loc_8649")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8649")

    QueueWorkItem2(0x23, 2, lambda_8649)
    OP_92(0x16, 0x0, 0x8FC, 0x1F4)
    OP_68(1000, 900, 2200, 3000)

    def lambda_8679():
        OP_95(0xFE, 0, 0, 2300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8679)
    WaitChrThread(0x16, 1)

    def lambda_8697():
        OP_95(0xFE, 0, 0, -5000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8697)
    Sleep(2000)
    Sound(107, 0, 100, 0)

    def lambda_86BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_86BA)
    WaitChrThread(0x16, 1)
    Sound(107, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x23, 0x2)
    SetChrFlags(0x16, 0x80)
    StopBGM(0xFA0)

    ChrTalk(
        0x23,
        (
            "#02804FHe is a competent investigator\x01",
            "There is a place where there is little flexibility.\x02\x03",
            "#02800FFrom his position,\x01",
            "I wonder if that is also a virtue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PHa ha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, as an investigation department of demon\x01",
            "I guess there is also dignity.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(3500, 1000, 6000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 3100, 0, 6700, 180)
    SetChrPos(0x104, 2100, 0, 7500, 180)
    SetChrPos(0x105, 2700, 0, 9100, 180)
    SetChrPos(0x102, 5000, 0, 6500, 225)
    SetChrPos(0x103, 4600, 0, 7600, 180)
    SetChrPos(0x109, 4300, 0, 8700, 180)
    OP_0D()
    OP_93(0x23, 0x0, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7550", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x23,
        (
            "#6P#02805FOops, the important thing\x01",
            "I forgot to say … …\x02\x03",
            "#02809F── Many of the support department,\x01",
            "Welcome to \"Orkis Tower\"!\x02\x03",
            "Come along, Come on!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_890F():

        label("loc_890F")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_890F")

    QueueWorkItem2(0x101, 2, lambda_890F)

    def lambda_8921():

        label("loc_8921")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8921")

    QueueWorkItem2(0x102, 2, lambda_8921)

    def lambda_8933():

        label("loc_8933")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8933")

    QueueWorkItem2(0x103, 2, lambda_8933)

    def lambda_8945():

        label("loc_8945")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8945")

    QueueWorkItem2(0x104, 2, lambda_8945)

    def lambda_8957():

        label("loc_8957")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8957")

    QueueWorkItem2(0x109, 2, lambda_8957)

    def lambda_8969():

        label("loc_8969")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8969")

    QueueWorkItem2(0x105, 2, lambda_8969)
    OP_92(0x23, 0x1B58, 0x3E8, 0x1F4)
    OP_68(6500, 1000, 3000, 3000)

    def lambda_8999():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8999)
    WaitChrThread(0x23, 1)

    def lambda_89B7():
        OP_95(0xFE, 12000, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_89B7)
    WaitChrThread(0x23, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x23, 0x2)
    SetChrFlags(0x23, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(3500, 1000, 7600, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
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
        0x104,
        "#00302F#5PHaha, as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FAs expected, Mr.\x01",
            "There is only a father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FWell, okay\x01",
            "It seems like to show me around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FOh, are you willing to speechless words?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    SetChrPos(0x0, 3500, 0, 7600, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetScenarioFlags(0x141, 7)
    OP_29(0xA4, 0x4, 0x2)
    OP_29(0xA4, 0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8BEA")
    Jump("loc_8BEF")

    label("loc_8BEA")

    OP_29(0x71, 0x4, 0x40)

    label("loc_8BEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C00")
    Jump("loc_8C05")

    label("loc_8C00")

    OP_29(0x72, 0x4, 0x40)

    label("loc_8C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C16")
    Jump("loc_8C1B")

    label("loc_8C16")

    OP_29(0x77, 0x4, 0x40)

    label("loc_8C1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C2C")
    Jump("loc_8C31")

    label("loc_8C2C")

    OP_29(0x79, 0x4, 0x40)

    label("loc_8C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C42")
    Jump("loc_8C47")

    label("loc_8C42")

    OP_29(0x7A, 0x4, 0x40)

    label("loc_8C47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C58")
    Jump("loc_8C5D")

    label("loc_8C58")

    OP_29(0x7B, 0x4, 0x40)

    label("loc_8C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C6E")
    Jump("loc_8C73")

    label("loc_8C6E")

    OP_29(0x7C, 0x4, 0x40)

    label("loc_8C73")

    OP_1B(0x0, 0x0, 0x33)
    EventEnd(0x5)
    Return()

    # Function_42_74CF end

    def Function_43_8C7B(): pass

    label("Function_43_8C7B")


    def lambda_8C80():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8C80)
    WaitChrThread(0x16, 1)

    def lambda_8C9E():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8C9E)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x0, 0x1F4)
    Return()

    # Function_43_8C7B end

    def Function_44_8CBF(): pass

    label("Function_44_8CBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrPos(0x101, 72000, 0, -600, 90)
    SetChrPos(0x102, 72000, 0, 500, 90)
    SetChrPos(0x103, 70900, 0, -300, 90)
    SetChrPos(0x104, 70900, 0, 800, 90)
    SetChrPos(0x109, 69800, 0, -600, 90)
    SetChrPos(0x105, 69800, 0, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 80500, 0, 1800, 270)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    OP_68(87000, 900, 2000, 0)
    MoveCamera(53, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_68(75000, 900, 1000, 5000)
    SetCameraDistance(19000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#6P#10105FThree elevators ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWell, it is truly loud.\x02",
    )

    CloseMessageWindow()

    def lambda_8E21():
        OP_97(0x102, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E21)
    Sleep(50)

    def lambda_8E3E():
        OP_97(0x101, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E3E)
    Sleep(50)

    def lambda_8E5B():
        OP_97(0x104, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8E5B)
    Sleep(50)

    def lambda_8E78():
        OP_97(0x103, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E78)
    Sleep(50)

    def lambda_8E95():
        OP_97(0x105, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E95)
    Sleep(50)

    def lambda_8EB2():
        OP_97(0x109, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8EB2)
    Sleep(1000)
    Fade(500)
    OP_68(79200, 1000, 2000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x23,
        (
            "#02804F#11PWell, it's 40 stories above the ground.\x02\x03",
            "#02800FAfter inserting a dedicated elevator\x01",
            "A total of six are in operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FThat's amazing, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#02803F#11PWell, all floors\x01",
            "Because I can not give you guidance,\x01",
            "Let's limit it to conference related floors.\x02\x03",
            "#02800FThe first floor is the 34th floor with security office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PThank you.\x02",
    )

    CloseMessageWindow()
    OP_92(0x23, 0x13C68, 0xCE4, 0x1F4)
    BeginChrThread(0x23, 3, 0, 46)
    Sleep(1000)
    BeginChrThread(0x101, 0, 0, 45)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("c1520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_8CBF end

    def Function_45_909E(): pass

    label("Function_45_909E")

    BeginChrThread(0x101, 3, 0, 46)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 46)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 46)
    Sleep(900)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 46)
    Sleep(900)
    BeginChrThread(0x105, 3, 0, 46)
    Return()

    # Function_45_909E end

    def Function_46_90D2(): pass

    label("Function_46_90D2")


    def lambda_90D7():
        OP_95(0xFE, 81000, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90D7)
    WaitChrThread(0xFE, 1)

    def lambda_90F5():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90F5)
    Sleep(500)

    def lambda_9112():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9112)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_90D2 end

    def Function_47_9123(): pass

    label("Function_47_9123")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(0, 1000, -1700, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 400, 0, -6100, 0)
    SetChrPos(0x102, -1200, 0, -6900, 0)
    SetChrPos(0x103, 1200, 0, -6900, 0)
    SetChrPos(0x104, 1200, 0, -8500, 0)
    SetChrPos(0x109, -1200, 0, -8500, 0)
    SetChrPos(0x105, -400, 0, -9300, 0)
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

    def lambda_9253():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9253)
    Sleep(200)

    def lambda_9270():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9270)
    Sleep(200)

    def lambda_928D():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_928D)
    Sleep(200)

    def lambda_92AA():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_92AA)
    Sleep(200)

    def lambda_92C7():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_92C7)
    Sleep(200)

    def lambda_92E4():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_92E4)
    SetCameraDistance(18500, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(100)

    def lambda_9319():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9319)
    Sleep(300)

    def lambda_932D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_932D)
    Sleep(200)

    def lambda_9341():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9341)
    Sleep(600)

    def lambda_9355():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9355)
    Sleep(200)

    def lambda_9369():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9369)
    Sleep(300)

    def lambda_937D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_937D)
    Sound(803, 2, 100, 0)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_93B3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93B3)
    Sleep(50)

    def lambda_93C3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_93C3)
    Sleep(50)

    def lambda_93D3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_93D3)
    Sleep(50)

    def lambda_93E3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_93E3)
    Sleep(50)

    def lambda_93F3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93F3)

    ChrTalk(
        0x101,
        "#00005F#11POops ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Yonaの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hello, you guys now?\x02\x03",
            "This is the\x01",
            "When the installation is finished.\x02",
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
            "#00004FOh, just tower\x01",
            "I have just come to the entrance.\x02\x03",
            "#00000FShould we go to the rooftop as it is?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Yonaの声")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, for the reception desk for the elevator\x01",
            "I heard that he will give me an authorization card.\x02\x03",
            "Come up at last.\x02",
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
            "#00002FI understood, I'm tired.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        "#11P#00202FI guess the preparation is done.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0xB5, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00000F#5POh, borrow certification card at reception\x01",
            "Let's go up to the rooftop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FIt is also raining.\x01",
            "You had better not let me wait too long.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, 0, 0, -1500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 3)
    OP_29(0xA9, 0x1, 0x2)
    ClearMapFlags(0x10000000)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_47_9123 end

    def Function_48_974B(): pass

    label("Function_48_974B")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 2100, 20000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 0, 1000, 19000, 0)
    SetChrPos(0x102, -2300, 1000, 18200, 45)
    SetChrPos(0x103, -2000, 1000, 17400, 45)
    SetChrPos(0x104, 800, 1000, 17600, 0)
    SetChrPos(0x109, -500, 1000, 17600, 0)
    SetChrPos(0x105, -200, 1000, 16500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PWelcome to the Orkis Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, are those from the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYes, you need an authorization card\x01",
            "Can you issue it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYes, it will be here.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '临时认证卡片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('临时认证卡片', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#5PI'm going to use that card\x01",
            "When holding over the panel inside the elevator\x01",
            "You can go up to the top floor 40F directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBecause it is disposable only effective for 1 month\x01",
            "Please use it freely after use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11POK, OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112F(Something is amazing, is not it? …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P(Oh, than the IBC building\x01",
            "I do not want to go further … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302F(Truly the latest technology\x01",
            "Where is the catamaran? )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 0, 1000, 17500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 4)
    SetScenarioFlags(0x2, 1)
    EventEnd(0x5)
    Return()

    # Function_48_974B end

    def Function_49_9AA9(): pass

    label("Function_49_9AA9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC9")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_9AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ADD")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_9ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AF1")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_9AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B05")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_9B05")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x101, 700, 0, 5800, 45)
    SetChrPos(0x102, 600, 0, 7100, 90)
    SetChrPos(0x103, -500, 0, 6100, 45)
    SetChrPos(0x104, -600, 0, 7400, 90)
    SetChrPos(0x109, 3300, 0, 6300, 0)
    SetChrPos(0x105, -1700, 0, 7500, 90)
    SetChrPos(0x106, -600, 0, 9200, 135)
    SetChrPos(0x10A, -1700, 0, 5300, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(0, 500, -2500, 0)
    MoveCamera(25, 35, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_68(1000, 500, 7500, 7000)
    MoveCamera(60, 35, 0, 7000)
    SetCameraDistance(17000, 7000)
    PlayBGM("ed7302", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(3000, 1300, 9000, 0)
    MoveCamera(15, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(16500, 3500)
    OP_6F(0x79)
    Fade(500)
    OP_68(1400, 1300, 7400, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15680, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10104F……It's okay.\x01",
            "Various functions are alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FReally……\x01",
            "Do not take care of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6P… That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FLater on properly\x01",
            "I would like to repair it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1700, 1000, 2000)
    SetCameraDistance(17500, 2000)
    Sleep(300)
    OP_25(0x82, 0x32)
    Sleep(200)
    OP_25(0x82, 0x3C)
    Sleep(300)

    def lambda_9DCB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_9DCB)
    Sleep(30)

    def lambda_9DDB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9DDB)
    Sleep(30)

    def lambda_9DEB():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_9DEB)
    Sleep(30)

    def lambda_9DFB():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9DFB)
    Sleep(30)

    def lambda_9E0B():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9E0B)
    Sleep(30)

    def lambda_9E1B():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9E1B)
    Sleep(30)

    def lambda_9E2B():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9E2B)
    Sleep(30)

    def lambda_9E3B():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9E3B)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x106,
        "#5P#10708F… … It looks like it will still continue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401FWell, inexhaustible newer\x01",
            "It seems to get boiled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_25(0x82, 0x32)
    Fade(500)
    OP_68(970, 1300, 6970, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15680, 0)
    OP_0D()
    OP_25(0x82, 0x28)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#5P#00306FTime goes on ……\x01",
            "Finally with an elevator\x01",
            "Let's say it's going to rise.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(
        0x10A,
        (
            "#6P#00603FAs the meeting,\x01",
            "Here two people wait.\x02\x03",
            "#00600FChoose, Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)

    def lambda_9FBB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9FBB)
    Sleep(30)

    def lambda_9FCB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9FCB)
    Sleep(30)

    def lambda_9FDB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9FDB)
    Sleep(30)

    def lambda_9FEB():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9FEB)
    Sleep(30)

    def lambda_9FFB():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_9FFB)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        "#11P#00001FIt is okay.\x02",
    )

    CloseMessageWindow()
    StopSound(130, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    SetChrPos(0x0, 60, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    Call(0, 4)
    SetScenarioFlags(0x1A6, 0)
    OP_29(0xB1, 0x1, 0x9)
    OP_66(0x7, 0x1)
    OP_1B(0x0, 0x0, 0x33)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7302")
    ReplaceBGM("ed7352", "ed7302")
    ReplaceBGM("ed7550", "ed7302")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(130, 2, 40, 0)
    EventEnd(0x5)
    Return()

    # Function_49_9AA9 end

    def Function_50_A0CE(): pass

    label("Function_50_A0CE")

    EventBegin(0x1)
    OP_4B(0x1F, 0xFF)
    TurnDirection(0x1F, 0x0, 500)

    ChrTalk(
        0x1F,
        "Do you have an authentication card?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "カードがなければ、The elevator\x01",
            "You can not use it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 74460, 0, 1270, 180)
    OP_93(0x1F, 0xB4, 0x0)
    OP_4C(0x1F, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_50_A0CE end

    def Function_51_A15F(): pass

    label("Function_51_A15F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A203")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Intermittent from the square\x01",
            "I hear the sound of shooting and sword firing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001FWhile doing this now\x01",
            "Everyone is fighting.\x02\x03",
            "- Hurry and proceed!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A257")

    ChrTalk(
        0x101,
        (
            "#00001FI can not let the mayor wait so much.\x01",
            "- Let's chase after early.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A257")

    SetChrPos(0x0, -290, 0, -3540, 0)
    EventEnd(0x4)
    Return()

    # Function_51_A15F end

    def Function_52_A26B(): pass

    label("Function_52_A26B")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A27D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3E9")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_A2E8")
    MenuCmd(1, 0, "Take a break with a driving car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2E8")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A364")

    ChrTalk(
        0x101,
        (
            "#00001F…… There is no need to forcibly move it now.\x01",
            "I will repair it if the incident settles down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3E4")

    label("loc_A364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3DA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_A39D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_A3B5")

    label("loc_A39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A3B0")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_A3B5")

    label("loc_A3B0")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_A3B5")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3E4")

    label("loc_A3DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3E4")

    Jump("loc_A27D")

    label("loc_A3E9")

    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_52_A26B end

    SaveToFile()

Try(main)
