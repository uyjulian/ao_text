from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Receptionist Lilie",     # 1
        "Receptionist Viola",     # 2
        "Chief Morett",           # 3
        "Tajik",                  # 4
        "Patrol Officer Thibaud", # 5
        "Receptionist Lanfei",    # 6
        "Chief Roberts",          # 7
        "Researcher David",       # 8
        "Researcher Clay",        # 9
        "Mrs. Margaret",          # 10
        "Vice Chief Pierre",      # 11
        "Noｱl",                  # 12
        "Wazy",                   # 13
        "Rixia",                  # 14
        "Detective Dudley",       # 15
        "Policeman",              # 16
        "City Hall Staffer",      # 17
        "City Hall Staffer",      # 18
        "Citizen",                # 19
        "Citizen",                # 20
        "Tourist",                # 21
        "Citizen",                # 22
        "Trader Rizel",           # 23
        "Patrol Officer Gigio",   # 24
        "Grace",                  # 25
        "Reins",                  # 26
        "Jona",                   # 27
        "Mayor Dieter",           # 28
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
        "Function_6_ED2",          # 06, 6
        "Function_7_ED6",          # 07, 7
        "Function_8_1E04",         # 08, 8
        "Function_9_1E08",         # 09, 9
        "Function_10_2AFA",        # 0A, 10
        "Function_11_2AFE",        # 0B, 11
        "Function_12_38A1",        # 0C, 12
        "Function_13_38A5",        # 0D, 13
        "Function_14_3961",        # 0E, 14
        "Function_15_3D54",        # 0F, 15
        "Function_16_4C59",        # 10, 16
        "Function_17_4D17",        # 11, 17
        "Function_18_4E70",        # 12, 18
        "Function_19_4EC6",        # 13, 19
        "Function_20_4F1A",        # 14, 20
        "Function_21_4F6A",        # 15, 21
        "Function_22_4FF8",        # 16, 22
        "Function_23_5565",        # 17, 23
        "Function_24_55F7",        # 18, 24
        "Function_25_56D9",        # 19, 25
        "Function_26_579F",        # 1A, 26
        "Function_27_5841",        # 1B, 27
        "Function_28_5BC9",        # 1C, 28
        "Function_29_5C81",        # 1D, 29
        "Function_30_5DF3",        # 1E, 30
        "Function_31_5E5C",        # 1F, 31
        "Function_32_5F9A",        # 20, 32
        "Function_33_6992",        # 21, 33
        "Function_34_6DB6",        # 22, 34
        "Function_35_720E",        # 23, 35
        "Function_36_7290",        # 24, 36
        "Function_37_74F1",        # 25, 37
        "Function_38_77B3",        # 26, 38
        "Function_39_79DC",        # 27, 39
        "Function_40_7BE8",        # 28, 40
        "Function_41_7CF1",        # 29, 41
        "Function_42_7CF8",        # 2A, 42
        "Function_43_9542",        # 2B, 43
        "Function_44_9586",        # 2C, 44
        "Function_45_998F",        # 2D, 45
        "Function_46_99C3",        # 2E, 46
        "Function_47_9A14",        # 2F, 47
        "Function_48_A074",        # 30, 48
        "Function_49_A409",        # 31, 49
        "Function_50_AA3F",        # 32, 50
        "Function_51_AABD",        # 33, 51
        "Function_52_ABDB",        # 34, 52
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
            "It's a car magazine,\x01",
            ""Fast Running Mach".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x370, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECE")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Cool\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x370, 1)

    label("loc_ECE")

    TalkEnd(0xFF)
    Return()

    # Function_5_E25 end

    def Function_6_ED2(): pass

    label("Function_6_ED2")

    Call(0, 7)
    Return()

    # Function_6_ED2 end

    def Function_7_ED6(): pass

    label("Function_7_ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE8")
    Call(0, 48)
    Return()

    label("loc_EE8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1017")

    ChrTalk(
        0x8,
        (
            "For now, it was decided that\x01",
            "management of Orchis Tower will\x01",
            "be led by Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's still a lot of confusion...\x01",
            "But the fact that this building is a\x01",
            "place for the people hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I look forward to\x01",
            "working with all of you\x01",
            "in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10A0")

    label("loc_1017")


    ChrTalk(
        0x8,
        (
            "The fact that this\x01",
            "building is a place for\x01",
            "the people hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I look forward to\x01",
            "working with all of you\x01",
            "in the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A0")

    Jump("loc_1E00")

    label("loc_10A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_10B3")
    Jump("loc_1E00")

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_1E00")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_122E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119B")

    ChrTalk(
        0x8,
        (
            "A charity event for city\x01",
            "reconstruction is being held\x01",
            "today at City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a lot to prepare\x01",
            "to make everyone smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all should\x01",
            "participate if you have\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1229")

    label("loc_119B")


    ChrTalk(
        0x8,
        (
            "But even so... I was\x01",
            "surprised at the speed at\x01",
            "which IBC was restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It made me realize the\x01",
            "magnificence of orbal\x01",
            "net technology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1229")

    Jump("loc_1E00")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138E")

    ChrTalk(
        0x8,
        (
            "It's only natural, but... It\x01",
            "seems uneasiness is spreading\x01",
            "amongst the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can only answer\x01",
            "vaguely questions about\x01",
            "the incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Of course the CGF, but also\x01",
            "the mayor and chairman and\x01",
            "doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, right now, we staffers\x01",
            "need only believe in everyone\x01",
            "and do everything we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1462")

    label("loc_138E")


    ChrTalk(
        0x8,
        (
            "To bring this situation to a close, both\x01",
            "the Mayor and the Chairman, in addition\x01",
            "to the CGF, are doing their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, right now, we staffers\x01",
            "need only believe in everyone\x01",
            "and do everything we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1462")

    Jump("loc_1E00")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_15F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1531")

    ChrTalk(
        0x8,
        (
            "A citizen's forum with the theme\x01",
            "of "state Independence" will be\x01",
            "held today at City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The program has some open\x01",
            "seats, so please\x01",
            "participate if interested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15ED")

    label("loc_1531")


    ChrTalk(
        0x8,
        (
            "If you hold that card I gave\x01",
            "you over the elevator panel,\x01",
            "you'll be able to go to 40F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is valid for only a month and\x01",
            "disposable, so please dispose of\x01",
            "it when you're finished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15ED")

    Jump("loc_1E00")

    label("loc_15F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1788")

    ChrTalk(
        0x8,
        (
            "Welcome. If you have a\x01",
            "question on the train\x01",
            "accident, I can help you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Rail service has been temporarily\x01",
            "suspended due to the train accident\x01",
            "near West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Furthermore, the cause is being\x01",
            "investigated, and we do not have an ETA\x01",
            "for restoration of service at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those hurrying to the\x01",
            "Empire or Republic, please\x01",
            "use a bus or airship.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_180D")

    label("loc_1788")


    ChrTalk(
        0x8,
        (
            "Those hurrying to the\x01",
            "Empire or Republic, please\x01",
            "use a bus or airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If necessary, we can\x01",
            "prepare a ticket for you\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_180D")

    Jump("loc_1E00")

    label("loc_1812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")

    ChrTalk(
        0x8,
        (
            "At present, we are considering\x01",
            "various plans to promote cultural\x01",
            "exchange in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A Crossbell sightseeing PR corner or an\x01",
            "international culture study corner, or maybe\x01",
            "a shop with foreign specialty goods...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All of us staff members work\x01",
            "hard to bring the citizens more\x01",
            "useful services every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please look forward to\x01",
            "future developments at\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A51")

    label("loc_19AE")


    ChrTalk(
        0x8,
        (
            "At present, we are considering\x01",
            "various plans to promote cultural\x01",
            "exchange in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please look forward to\x01",
            "future developments at\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A51")

    Jump("loc_1E00")

    label("loc_1A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B5C")

    ChrTalk(
        0x8,
        "Welcome to Orchis Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At this integrated reception\x01",
            "desk, we guide visitors to\x01",
            "anything they may need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please feel free to ask about any of our\x01",
            "services, including tourist information,\x01",
            "medical care or social services.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C29")

    label("loc_1B5C")


    ChrTalk(
        0x8,
        (
            "At this integrated reception\x01",
            "desk, we guide visitors to\x01",
            "anything they may need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please feel free to ask about any of our\x01",
            "services, including tourist information,\x01",
            "medical care or social services.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C29")

    Jump("loc_1E00")

    label("loc_1C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_1E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4C")

    ChrTalk(
        0x8,
        (
            "Hello everyone. This is\x01",
            "the Orchis Tower\x01",
            "integrated reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, all of the staff here, at the direction\x01",
            "of the security planning room, can handle any\x01",
            "kind of business you may have today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need anything,\x01",
            "please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E00")

    label("loc_1D4C")


    ChrTalk(
        0x8,
        (
            "All of the staff here, at the direction\x01",
            "of the security planning room, can handle\x01",
            "any kind of business you may have today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need anything,\x01",
            "please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E00")

    TalkEnd(0x8)
    Return()

    # Function_7_ED6 end

    def Function_8_1E04(): pass

    label("Function_8_1E04")

    Call(0, 9)
    Return()

    # Function_8_1E04 end

    def Function_9_1E08(): pass

    label("Function_9_1E08")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(
        0x9,
        (
            "It seems all of those\x01",
            "monsters that appeared in\x01",
            "the city have disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was really scared when\x01",
            "I was locked inside the\x01",
            "tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The damage wasn't even that\x01",
            "great, but I never want to\x01",
            "go through that again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F96")

    label("loc_1F06")


    ChrTalk(
        0x9,
        (
            "I was really scared when\x01",
            "I was locked inside the\x01",
            "tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The damage wasn't even that\x01",
            "great, but I never want to\x01",
            "go through that again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F96")

    Jump("loc_2AF6")

    label("loc_1F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1FA9")
    Jump("loc_2AF6")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FB7")
    Jump("loc_2AF6")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F5")

    ChrTalk(
        0x9,
        (
            "When the attack hit and I was\x01",
            "heading to the basement shelter, I\x01",
            "saw the conflict in the plaza...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As for the scene with the\x01",
            "armed group closing in, I\x01",
            "can only say it was scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thankfully this building escaped\x01",
            "damage somehow, but... I really\x01",
            "didn't think I'd live through it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21B1")

    label("loc_20F5")


    ChrTalk(
        0x9,
        (
            "As for the scene with the\x01",
            "armed group closing in, I\x01",
            "can only say it was scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thankfully this building escaped\x01",
            "damage somehow, but... I really\x01",
            "didn't think I'd live through it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    Jump("loc_2AF6")

    label("loc_21B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_238A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D3")

    ChrTalk(
        0x9,
        (
            "The noisy situation at St.\x01",
            "Ursula Hospital has\x01",
            "continued since last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of the large number\x01",
            "of patients, they're short\x01",
            "on staff and supplies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I think of the men and\x01",
            "women fighting at the scene, I\x01",
            "have great respect for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2385")

    label("loc_22D3")


    ChrTalk(
        0x9,
        (
            "At present, the city is working\x01",
            "to support the hospital in\x01",
            "various ways, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I think of the men and\x01",
            "women fighting at the scene, I\x01",
            "have great respect for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2385")

    Jump("loc_2AF6")

    label("loc_238A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2469")

    ChrTalk(
        0x9,
        (
            "Almost everyone forced to\x01",
            "stay here due to the train\x01",
            "accident left this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll discuss reparations later,\x01",
            "but... For now, I'm glad the accident\x01",
            "recovery didn't drag on too long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_250C")

    label("loc_2469")


    ChrTalk(
        0x9,
        (
            "We'll have to think about\x01",
            "reparations for the train\x01",
            "accident in the future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For now, I'm just glad\x01",
            "the accident recovery\x01",
            "didn't drag on too long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250C")

    Jump("loc_2AF6")

    label("loc_2511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_25BE")

    ChrTalk(
        0x9,
        (
            "I just received word. They\x01",
            "said transport of the injured\x01",
            "passengers is complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's a relief... Next,\x01",
            "we need to worry about\x01",
            "the accident scene.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF6")

    label("loc_25BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2721")

    ChrTalk(
        0x9,
        (
            "Everyone, do you know\x01",
            "the meaning of Orchis\x01",
            "Tower's name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Orchis is from "orchid"... A\x01",
            "beautiful flower in which a single\x01",
            "flower sits atop a single stalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, this building\x01",
            "is like a single flower that\x01",
            "stretches to the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. Thinking about it\x01",
            "that way, it's a fitting\x01",
            "name, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27DD")

    label("loc_2721")


    ChrTalk(
        0x9,
        (
            "Orchis is from "orchid"... A\x01",
            "beautiful flower in which a single\x01",
            "flower sits atop a single stalk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, this building\x01",
            "is like a single flower that\x01",
            "stretches to the sky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DD")

    Jump("loc_2AF6")

    label("loc_27E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A3")

    ChrTalk(
        0x9,
        (
            "Welcome. This is the reception\x01",
            "window for all kinds of\x01",
            "administrative services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is the place for\x01",
            "utility payments and change\x01",
            "of address notifications.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_294F")

    label("loc_28A3")


    ChrTalk(
        0x9,
        (
            "You can go to City Meeting\x01",
            "Hall as well for most services\x01",
            "offered at this window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Getting here is a bit\x01",
            "difficult, so please feel free\x01",
            "make use of those as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294F")

    Jump("loc_2AF6")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_2AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A45")

    ChrTalk(
        0x9,
        (
            "The main session will\x01",
            "finally start in another\x01",
            "hour, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "During the conference, I\x01",
            "will be here handling\x01",
            "communications, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How to say it... When I\x01",
            "think about this event,\x01",
            "I get nervous somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AF6")

    label("loc_2A45")


    ChrTalk(
        0x9,
        (
            "The main session starts in one\x01",
            "hour... and the heads of state\x01",
            "will be coming for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*. It's not like I have\x01",
            "an important job, but I'm\x01",
            "nervous for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF6")

    TalkEnd(0x9)
    Return()

    # Function_9_1E08 end

    def Function_10_2AFA(): pass

    label("Function_10_2AFA")

    Call(0, 11)
    Return()

    # Function_10_2AFA end

    def Function_11_2AFE(): pass

    label("Function_11_2AFE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C11")

    ChrTalk(
        0xA,
        (
            "Most of the staff and State\x01",
            "Guard that were arrested in\x01",
            "Orchis Tower have been released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're dealing mostly\x01",
            "with their abandoned\x01",
            "positions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's especially in times like\x01",
            "these that we must work to\x01",
            "properly support the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CDF")

    label("loc_2C11")


    ChrTalk(
        0xA,
        (
            "We're dealing mostly with the positions\x01",
            "of the staff and the State Guard who\x01",
            "were arrested in Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's especially in times like\x01",
            "these that we must work to\x01",
            "properly support the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDF")

    Jump("loc_389D")

    label("loc_2CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2CF2")
    Jump("loc_389D")

    label("loc_2CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D00")
    Jump("loc_389D")

    label("loc_2D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E03")

    ChrTalk(
        0xA,
        (
            "Arios MacLaine... He's a\x01",
            "real hero of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I saw him attacking the\x01",
            "armed group. It was so\x01",
            "amazing, it's indescribable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a wild idea, but if we have\x01",
            "him, we needn't fear the major\x01",
            "powers... It's really true.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E9A")

    label("loc_2E03")


    ChrTalk(
        0xA,
        (
            "Arios MacLaine... He's a\x01",
            "real hero of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a wild idea, but if we have\x01",
            "him, we needn't fear the major\x01",
            "powers... It's really true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9A")

    Jump("loc_389D")

    label("loc_2E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_30BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE2")

    ChrTalk(
        0xA,
        (
            "Based on what I've\x01",
            "heard, the CGF aren't\x01",
            "doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If there are more injured,\x01",
            "we'll have to think of\x01",
            "sending in the police, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On the other hand, city\x01",
            "defenses can't be\x01",
            "neglected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've tried everything, but a\x01",
            "solution based on dialogue and\x01",
            "negotiation just won't come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30B9")

    label("loc_2FE2")


    ChrTalk(
        0xA,
        (
            "We've tried everything, but a\x01",
            "solution based on dialogue and\x01",
            "negotiation just won't come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's hard to directly support them, but\x01",
            "we of General Affairs Section One are\x01",
            "focusing on all sorts of operations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    Jump("loc_389D")

    label("loc_30BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3242")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BA")

    ChrTalk(
        0xA,
        (
            "*sigh*. It's a relief that\x01",
            "restoration of the rail line was\x01",
            "completed yesterday somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the trains had\x01",
            "stopped, reparations\x01",
            "would have skyrocketed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We owe this to the CGF,\x01",
            "who worked all through\x01",
            "the night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_323D")

    label("loc_31BA")


    ChrTalk(
        0xA,
        (
            "If the trains had\x01",
            "stopped, reparations\x01",
            "would have skyrocketed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We owe this to the CGF,\x01",
            "who worked all through\x01",
            "the night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323D")

    Jump("loc_389D")

    label("loc_3242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3330")

    ChrTalk(
        0xA,
        (
            "We of course received\x01",
            "word of the train\x01",
            "accident quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're also replying\x01",
            "quickly to inquiries\x01",
            "from all over the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're now preparing\x01",
            "information and alternative\x01",
            "transportation methods.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33BA")

    label("loc_3330")


    ChrTalk(
        0xA,
        (
            "Even so, train accidents\x01",
            "are rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Crossbell railroad is a\x01",
            "straight line with good visibility,\x01",
            "so accidents rarely occur...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BA")

    Jump("loc_389D")

    label("loc_33BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_348D")

    ChrTalk(
        0xA,
        (
            "On this office's opening day, there\x01",
            "was a commotion over sightseeing\x01",
            "guides by the entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha. It was fun watching the\x01",
            "dumbfounded expressions on\x01",
            "visitors' faces on opening day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_389D")

    label("loc_348D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_369D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_360E")

    ChrTalk(
        0xA,
        (
            "Oh, you guys are the Special Support Section\x01",
            "that participated in the security detail for\x01",
            "the trade conference, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm. This is a good chance, so\x01",
            "I'll explain it to you. This\x01",
            "is the administration window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I handle public records\x01",
            "requests, policy inquiries\x01",
            "and like right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, please let me know\x01",
            "if you ever need\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3698")

    label("loc_360E")


    ChrTalk(
        0xA,
        (
            "This window is for\x01",
            "dealing with\x01",
            "administrative matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I handle public records\x01",
            "requests, policy inquiries\x01",
            "and like right here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3698")

    Jump("loc_389D")

    label("loc_369D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_389D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F3")

    ChrTalk(
        0xA,
        (
            "Management and administration of Orchis Tower\x01",
            "is an important responsibility of General\x01",
            "Affairs Section One, of which I am a member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It was our job to prepare the\x01",
            "conference and waiting rooms\x01",
            "for the main session today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're finally done now, but...\x01",
            "We were very busy until just a\x01",
            "little while ago.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_389D")

    label("loc_37F3")


    ChrTalk(
        0xA,
        (
            "*sigh*. Anyway, I'm glad\x01",
            "we finished in time for\x01",
            "the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Though we can't lose focus until\x01",
            "the end, all that's left is to\x01",
            "wait for the conference to start.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_389D")

    TalkEnd(0xA)
    Return()

    # Function_11_2AFE end

    def Function_12_38A1(): pass

    label("Function_12_38A1")

    Call(0, 13)
    Return()

    # Function_12_38A1 end

    def Function_13_38A5(): pass

    label("Function_13_38A5")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Cancel\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3908")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3908")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3928")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3958")

    label("loc_3928")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_393C")
    Jump("loc_3958")

    label("loc_393C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3958")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_3958")

    Jump("loc_38B2")

    label("loc_395D")

    TalkEnd(0xD)
    Return()

    # Function_13_38A5 end

    def Function_14_3961(): pass

    label("Function_14_3961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3AF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4D")

    ChrTalk(
        0xD,
        (
            "IBC's business is\x01",
            "suspended... Half the staff\x01",
            "are standing by at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As someone who has worked for\x01",
            "IBC for many years, the arrest\x01",
            "of Mr. Dieter is too shocking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We have to get through\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3AEC")

    label("loc_3A4D")


    ChrTalk(
        0xD,
        (
            "Even with IBC operations\x01",
            "suspended, we can still perform\x01",
            "the sepith exchange service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please feel free to\x01",
            "speak with me when\x01",
            "you're ready to use it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEC")

    Jump("loc_3D53")

    label("loc_3AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C85")

    ChrTalk(
        0x102,
        (
            "#00100FHello Lanfei.\x02\x03",
            "It looks like you've\x01",
            "settled in after\x01",
            "relocating the window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well if it isn't Lady\x01",
            "Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. This too is thanks to\x01",
            "Acting President Mariabell and\x01",
            "the Technology Division staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Over half our staff have\x01",
            "resumed their normal duties\x01",
            "here in Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there is anything you\x01",
            "need, please feel free\x01",
            "to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3D53")

    label("loc_3C85")


    ChrTalk(
        0xD,
        (
            "At present IBC is moving\x01",
            "operations into this\x01",
            "Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please feel free to use the\x01",
            "sepith exchange service as\x01",
            "you have until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there is anything you\x01",
            "need, please feel free\x01",
            "to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D53")

    Return()

    # Function_14_3961 end

    def Function_15_3D54(): pass

    label("Function_15_3D54")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E13")

    ChrTalk(
        0xFE,
        (
            "Separated families and\x01",
            "friends are meeting up\x01",
            "again one by one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a terrible situation...\x01",
            "But in times like these we\x01",
            "must be with our loved ones.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E91")

    label("loc_3E13")


    ChrTalk(
        0xFE,
        (
            "By the way, your broken\x01",
            "orbal car was carried\x01",
            "outside earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like it was\x01",
            "well-cared for. My\x01",
            "condolences.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E91")

    Jump("loc_4C55")

    label("loc_3E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3EA4")
    Jump("loc_4C55")

    label("loc_3EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3EB2")
    Jump("loc_4C55")

    label("loc_3EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_40DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4022")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower got through the\x01",
            "attack safely somehow thanks\x01",
            "to the great efforts of Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC building... It\x01",
            "literally disappeared\x01",
            "without a trace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were hardly any\x01",
            "civilian casualties, but even\x01",
            "Arc-en-Ciel was involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if it was a warning\x01",
            "or something, but something like\x01",
            "this can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40D6")

    label("loc_4022")


    ChrTalk(
        0xFE,
        (
            "There were hardly any\x01",
            "civilian casualties, but even\x01",
            "Arc-en-Ciel was involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if it was a warning\x01",
            "or something, but something like\x01",
            "this can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D6")

    Jump("loc_4C55")

    label("loc_40DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_41C7")

    ChrTalk(
        0xFE,
        (
            "I seems both the mayor and chairman\x01",
            "have been working ever since last night\x01",
            "on a way to deal with the occupation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What can we do about the situation?\x01",
            "Anyway, we have to stay focused and\x01",
            "prepare for an emergency.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C55")

    label("loc_41C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_43D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4323")

    ChrTalk(
        0xFE,
        (
            "Though they're not the same as\x01",
            "the monster that caused the\x01",
            "train accident yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about the\x01",
            "cryptids that have been\x01",
            "appearing often recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard mysterious blue\x01",
            "flowers have been confirmed\x01",
            "near where they've appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What does this mean?\x01",
            "That there'll be even\x01",
            "more accidents?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43D0")

    label("loc_4323")


    ChrTalk(
        0xFE,
        (
            "Because we don't know the details,\x01",
            "we can't say for sure that\x01",
            "cryptids won't appear in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really quite\x01",
            "strange... Anyhow, we\x01",
            "can't let down our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D0")

    Jump("loc_4C55")

    label("loc_43D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4463")

    ChrTalk(
        0xFE,
        (
            "An orbal train\x01",
            "derailment, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the cause is\x01",
            "being investigated, but...\x01",
            "Could it be terrorists again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C55")

    label("loc_4463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_467D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C5")

    ChrTalk(
        0xFE,
        (
            "Though I'm a police\x01",
            "officer, I'm treated here\x01",
            "like one of the city staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I'm able\x01",
            "to use the cafe and dining\x01",
            "hall that's for staff only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The place is halfway up the\x01",
            "building. IBC is even further\x01",
            "above that, near the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, although the\x01",
            "view is great, I feel\x01",
            "sorry for the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4678")

    label("loc_45C5")


    ChrTalk(
        0xFE,
        (
            "However, they're saying the\x01",
            "cafe will be opened to the\x01",
            "citizens as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know when it'll\x01",
            "happen, but when it does, I'm\x01",
            "sure it'll be a popular spot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4678")

    Jump("loc_4C55")

    label("loc_467D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4764")

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't the\x01",
            "Special Support Section.\x01",
            "Welcome to Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business\x01",
            "here, please ask at the\x01",
            "front reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Visitors can't do\x01",
            "anything here until they\x01",
            "do that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47E5")

    label("loc_4764")


    ChrTalk(
        0xFE,
        (
            "If you have business\x01",
            "here, please ask at the\x01",
            "front reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Visitors can't do\x01",
            "anything here until they\x01",
            "do that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E5")

    Jump("loc_4C55")

    label("loc_47EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_4C55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE2")

    ChrTalk(
        0xFE,
        (
            "To think Mayor Dieter's showing you\x01",
            "around the venue personally. That's\x01",
            "the Special Support Section for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So the rumor that you guys\x01",
            "were the mayor's favorites\x01",
            "was true after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, what are you trying\x01",
            "to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not the case\x01",
            "that I'm jealous. No\x01",
            "offense intended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, I'm rooting\x01",
            "for you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our roles are different, but\x01",
            "I'm glad we got the chance\x01",
            "to work together like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FI feel like people have\x01",
            "a much higher opinion of\x01",
            "us than half a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FOh yeah. We were called names\x01",
            "like "fake bracers" and\x01",
            ""trained monkeys" back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. Members of an\x01",
            "organization disparage each\x01",
            "other quite a bit, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Indeed there were\x01",
            "people who called you\x01",
            "that back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But you can relax. I don't\x01",
            "think there's anyone who\x01",
            "would say those things now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that aside, let's\x01",
            "both do our best today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 0)
    Jump("loc_4C55")

    label("loc_4BE2")


    ChrTalk(
        0xFE,
        (
            "Our roles are different,\x01",
            "but I'm glad we got this\x01",
            "chance to work together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's both do our best\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C55")

    TalkEnd(0xFE)
    Return()

    # Function_15_3D54 end

    def Function_16_4C59(): pass

    label("Function_16_4C59")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, when it rains, you\x01",
            "can't even go outside to get\x01",
            "some fresh air during a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But this entrance is a\x01",
            "pretty nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An open ceiling like\x01",
            "this is the best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_4C59 end

    def Function_17_4D17(): pass

    label("Function_17_4D17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DED")

    ChrTalk(
        0xFE,
        (
            "12:00―― Nothing\x01",
            "especially out of the\x01",
            "ordinary, they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No sign of terrorists\x01",
            "have been detected as\x01",
            "yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just where are those\x01",
            "guys planning to invade\x01",
            "from, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E6C")

    label("loc_4DED")


    ChrTalk(
        0xFE,
        (
            "No sign of terrorists\x01",
            "have been detected as\x01",
            "yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just where are those\x01",
            "guys planning to invade\x01",
            "from, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6C")

    TalkEnd(0xFE)
    Return()

    # Function_17_4D17 end

    def Function_18_4E70(): pass

    label("Function_18_4E70")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Umm, entry to the VIP room\x01",
            "is prohibited until the\x01",
            "appointed time, right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4E70 end

    def Function_19_4EC6(): pass

    label("Function_19_4EC6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Yeah, exactly. It goes\x01",
            "without saying, but we're\x01",
            "way ahead of schedule.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_4EC6 end

    def Function_20_4F1A(): pass

    label("Function_20_4F1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2F")
    Call(0, 29)
    Jump("loc_4F66")

    label("loc_4F2F")


    ChrTalk(
        0xFE,
        (
            "Y-You guys... Get out of\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm busy now!\x02",
    )

    CloseMessageWindow()

    label("loc_4F66")

    TalkEnd(0xFE)
    Return()

    # Function_20_4F1A end

    def Function_21_4F6A(): pass

    label("Function_21_4F6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7F")
    Call(0, 31)
    Jump("loc_4FF4")

    label("loc_4F7F")


    ChrTalk(
        0xFE,
        (
            "Chief Roberts came too, and\x01",
            "we were able to get the orbal\x01",
            "network trouble resolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, that's one down.\x02",
    )

    CloseMessageWindow()

    label("loc_4FF4")

    TalkEnd(0xFE)
    Return()

    # Function_21_4F6A end

    def Function_22_4FF8(): pass

    label("Function_22_4FF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50EE")

    ChrTalk(
        0xFE,
        (
            "It looked like a little girl\x01",
            "entered the elevator to the\x01",
            "roof a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think she was the\x01",
            "Secretary of Defense's\x01",
            "daughter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Huge Tree that\x01",
            "appeared in Marshlands\x01",
            "is indeed concerning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_51A0")

    label("loc_50EE")


    ChrTalk(
        0xFE,
        (
            "It looked like the Secretary of\x01",
            "Defense's daughter entered the elevator\x01",
            "to the roof a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Huge Tree that\x01",
            "appeared in Marshlands\x01",
            "is indeed concerning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A0")

    Jump("loc_5561")

    label("loc_51A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_51B3")
    Jump("loc_5561")

    label("loc_51B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51C1")
    Jump("loc_5561")

    label("loc_51C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_524F")

    ChrTalk(
        0xFE,
        (
            "The Empire, of course,\x01",
            "are the ones backing\x01",
            ""Red Constellation"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. That's something we\x01",
            "absolutely can't\x01",
            "forgive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_524F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_529F")

    ChrTalk(
        0xFE,
        (
            ""Red Constellation"...\x01",
            "It seems they're not\x01",
            "your usual guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_529F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_END)), "loc_5323")

    ChrTalk(
        0xFE,
        (
            "Everyone, thank you for\x01",
            "your hard work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're going upstairs,\x01",
            "please use the elevators\x01",
            "by the entrance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_5323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53A6")

    ChrTalk(
        0xFE,
        (
            "Hmm. Rainy weather\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, according to the\x01",
            "forecast on the orbal net,\x01",
            "it'll be sunny this afternoon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_53A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_542F")

    ChrTalk(
        0xFE,
        (
            "Hmm. Train accidents are\x01",
            "rare in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The derailment must've\x01",
            "cost so much... Just\x01",
            "what happened, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_542F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54C2")

    ChrTalk(
        0xFE,
        (
            "No matter what you say\x01",
            "about Orchis Tower, this\x01",
            "spacious room is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's a\x01",
            "luxuriously constructed\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_54C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5558")

    ChrTalk(
        0xFE,
        (
            "They say the Orchis Tower\x01",
            "elevators are the fastest\x01",
            "on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because they barely\x01",
            "shake at all, you hardly\x01",
            "notice it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5561")

    label("loc_5558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5561")

    label("loc_5561")

    TalkEnd(0xFE)
    Return()

    # Function_22_4FF8 end

    def Function_23_5565(): pass

    label("Function_23_5565")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wow, amazing... So this\x01",
            "is the Orchis Tower\x01",
            "entrance, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I almost feel like we're\x01",
            "time travelers from a\x01",
            "science fiction novel.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_5565 end

    def Function_24_55F7(): pass

    label("Function_24_55F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5665")

    ChrTalk(
        0xFE,
        (
            "I heard from the staff.\x01",
            "They said there was a\x01",
            "derailment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What could be the cause?\x02",
    )

    CloseMessageWindow()
    Jump("loc_56D5")

    label("loc_5665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_56D5")

    ChrTalk(
        0xFE,
        (
            "It's my first time here,\x01",
            "but this really is an\x01",
            "amazing room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels out of place,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D5")

    TalkEnd(0xFE)
    Return()

    # Function_24_55F7 end

    def Function_25_56D9(): pass

    label("Function_25_56D9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To think a cool, high-tech\x01",
            "building like this is City Hall\x01",
            "just knocks your socks off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Disturbances over the independence\x01",
            "proposal aside, I might want to\x01",
            "move to Crossbell someday.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_56D9 end

    def Function_26_579F(): pass

    label("Function_26_579F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm. It seems City Hall\x01",
            "is a bit busy dealing\x01",
            "with the attack on Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll return home\x01",
            "immediately after finishing\x01",
            "my business here...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_579F end

    def Function_27_5841(): pass

    label("Function_27_5841")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5AA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B9")

    ChrTalk(
        0xFE,
        (
            "I heard both the president, who was\x01",
            "also President of the state, and the\x01",
            "acting president have disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This will have a large impact on stock prices\x01",
            "going forward... IBC will probably lose its\x01",
            "position as the biggest company on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to watch how things go\x01",
            "for a while, until the next\x01",
            "IBC president is chosen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5AA2")

    label("loc_59B9")


    ChrTalk(
        0xFE,
        (
            "This will have a large impact on stock prices\x01",
            "going forward... IBC will probably lose its\x01",
            "position as the biggest company on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to watch how things go\x01",
            "for a while, until the next\x01",
            "IBC president is chosen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AA2")

    Jump("loc_5BC5")

    label("loc_5AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5AB5")
    Jump("loc_5BC5")

    label("loc_5AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BC5")

    ChrTalk(
        0xFE,
        (
            "I can't believe we've been\x01",
            "backing up customer data at\x01",
            "Orchis Tower for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's IBC for you...\x01",
            "They have great crisis\x01",
            "management abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems their achievements\x01",
            "supporting economies throughout\x01",
            "the continent aren't just talk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BC5")

    TalkEnd(0xFE)
    Return()

    # Function_27_5841 end

    def Function_28_5BC9(): pass

    label("Function_28_5BC9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BDE")
    Call(0, 29)
    Jump("loc_5C7D")

    label("loc_5BDE")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "...As punishment for worrying\x01",
            "me, I'm cutting your pocket\x01",
            "money for next month by half.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        "A-Anything but that!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)

    label("loc_5C7D")

    TalkEnd(0xFE)
    Return()

    # Function_28_5BC9 end

    def Function_29_5C81(): pass

    label("Function_29_5C81")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "Goodness. People like\x01",
            "you make me worry far\x01",
            "too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "B-But, Margaret.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "As Vice Chief, this is a\x01",
            "time when I have to\x01",
            "stand up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "You always say things\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Because you suddenly do things\x01",
            "that aren't like you, you get\x01",
            "involved in things like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...S-Sorry.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5DE2")

    ChrTalk(
        0x101,
        (
            "#00012F(S-She's harsh as\x01",
            "always.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE2")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_29_5C81 end

    def Function_30_5DF3(): pass

    label("Function_30_5DF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E08")
    Call(0, 31)
    Jump("loc_5E58")

    label("loc_5E08")


    ChrTalk(
        0xFE,
        (
            "It's a good feeling\x01",
            "working with my partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's begin immediately.\x02",
    )

    CloseMessageWindow()

    label("loc_5E58")

    TalkEnd(0xFE)
    Return()

    # Function_30_5DF3 end

    def Function_31_5E5C(): pass

    label("Function_31_5E5C")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        (
            "Alright, let's start the\x01",
            "orbal net check right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Because of the blue mist when those monsters were\x01",
            "wandering around, it was hard to establish comm\x01",
            "links. It may have affected the system as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Okay, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Then, first up is a\x01",
            "functional check of the\x01",
            "tower terminals.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_31_5E5C end

    def Function_32_5F9A(): pass

    label("Function_32_5F9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_66CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BB")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Tio... You're heading to\x01",
            "that Huge Tree, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything were to happen to\x01",
            "you, Tio... When I think that,\x01",
            "I get torn apart inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...Chief, you don't need\x01",
            "to─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ah, that's right! How\x01",
            "about I take an orbal\x01",
            "staff and accompany you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how to operate an\x01",
            "orbal staff, and in battle I can\x01",
            "support Tio with support crafts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, yes, that would be\x01",
            "great! Now that that's\x01",
            "decided, the preparations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211FYou're too annoying, so\x01",
            "no thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61CB")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_61CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61F1")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_61F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6217")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_623D")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_623D")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F(...They're the same as\x01",
            "always.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F...Chief, please don't\x01",
            "worry too much.\x02\x03",
            "#00202FI'll return in one piece\x01",
            "with KeA and everyone.\x02\x03",
            "And in the end, your\x01",
            "role is here, in this\x01",
            "city of chaos, Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "T-Tio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That's right, it's as\x01",
            "Tio says. I'll focus on\x01",
            "my work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In return, promise me\x01",
            "this. That you'll\x01",
            "definitely return safely!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 3)
    Jump("loc_66C5")

    label("loc_63BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65FC")

    ChrTalk(
        0xFE,
        (
            "That aside... The Ouroboros\x01",
            "professor and that white\x01",
            "doll already left, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FYes... To be honest, I\x01",
            "never want to see them\x01",
            "again.\x02\x03",
            "#00211FCompared to them, you're\x01",
            "a thousand times better,\x01",
            "Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-Tio! (*moved to\x01",
            "tears*...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(It's weird that he's so\x01",
            "happy after being compared\x01",
            "to Novartis, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But Aions, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F...Chief? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ahaha, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(It seems to have the same\x01",
            "root word as the Aeon System\x01",
            "we developed, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(...It's a coincidence,\x01",
            "right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_66C5")

    label("loc_65FC")


    ChrTalk(
        0xFE,
        (
            "I'll wait here for you\x01",
            "all to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd really like to go with\x01",
            "you, but... Since Tio rejected\x01",
            "it, I've got no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In return, promise me\x01",
            "this. That you'll\x01",
            "definitely return safely!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C5")

    Jump("loc_698E")

    label("loc_66CA")

    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68FF")

    ChrTalk(
        0xFE,
        (
            "Hmm. Normally, I would have liked\x01",
            "to have more detailed information\x01",
            "about the Marshlands, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Aaah, it's all so\x01",
            "sudden that now I've\x01",
            "gotten worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think Tio would be\x01",
            "deployed in such a\x01",
            "strange place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt's to bring those\x01",
            "bracers back home\x01",
            "safely.\x02\x03",
            "Just wait here, and\x01",
            "don't worry too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio... You've really\x01",
            "become a good person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And you were so small when you\x01",
            "first came to the foundation...\x01",
            "Oooh, I think I could cry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F...How annoying. Please\x01",
            "don't cry in a place\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_698E")

    label("loc_68FF")


    ChrTalk(
        0xFE,
        (
            "I can't help but worry,\x01",
            "sending Tio into a strange\x01",
            "place like that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're a good person,\x01",
            "Tio. I'm sure you'll be\x01",
            "all right!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698E")

    TalkEnd(0xFE)
    Return()

    # Function_32_5F9A end

    def Function_33_6992(): pass

    label("Function_33_6992")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AE2")

    ChrTalk(
        0x22,
        (
            "#02302FOh yeah... You guys have a "Pom!"\x01",
            "account, right?\x02\x03",
            "#02304FHehe. Since I'm here, I think I'll gift\x01",
            "you with Master Jona's account.\x02\x03",
            "#02302FIf you think you can win against me,\x01",
            "who's been involved since the development\x01",
            "stage, just go ahead and try.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Jona's Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_6DB2")

    label("loc_6AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D23")

    ChrTalk(
        0x22,
        (
            "#02306FWalking all over the place in\x01",
            "this rain sure is tiring.\x02\x03",
            "#02300FBefore going back to Foundation\x01",
            "branch, I'll have to laze around\x01",
            "to my heart's content, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHey now... There's an\x01",
            "elevator, so it's not that\x01",
            "much exercise, right?\x02\x03",
            "#00001FGetting insufficient\x01",
            "exercise isn't good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt can't be helped. Jona\x01",
            "has weak child syndrome.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x22,
        (
            "#02310FW-What? That syndrome...\x02\x03",
            "#02306FHmph, whatever... If you're\x01",
            "going to the Marshlands,\x01",
            "you'd best get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we will. Thanks\x01",
            "for your help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_6DB2")

    label("loc_6D23")


    ChrTalk(
        0x22,
        (
            "#02303FI'll head back after\x01",
            "I'll have lazed around\x01",
            "to my heart's content.\x02\x03",
            "#02301FYou guys should get\x01",
            "going to the Marshlands\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB2")

    TalkEnd(0xFE)
    Return()

    # Function_33_6992 end

    def Function_34_6DB6(): pass

    label("Function_34_6DB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_707C")

    ChrTalk(
        0x20,
        (
            "#02100FAh, Lloyd and friends.\x01",
            "You guys look busy as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAre you guys here for\x01",
            "congressional coverage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02109FYou're good! We're here to\x01",
            "cover the vote on a new bill.\x02\x03",
            "While I'm at it, I plan to ask\x01",
            "a bunch of congresspeople their\x01",
            "opinions on state independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see. That would be\x01",
            "perfect politics\x01",
            "material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02106FYes, exactly.\x02\x03",
            "The political sphere is\x01",
            "boring these days due to\x01",
            "lack of scandal.\x02\x03",
            "#02102FHmm. I wonder where I\x01",
            "can find some good\x01",
            "gossip material?\x02",
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
        (
            "#00006FSo that's what you're\x01",
            "worried about, huh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 7)
    Jump("loc_720A")

    label("loc_707C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_713A")

    ChrTalk(
        0x20,
        (
            "#02106FDon't misunderstand. The lack of\x01",
            "scandal is a good thing. But, there\x01",
            "hasn't been much gossip lately.\x02\x03",
            "#02102FHmm. I wonder where I can find some\x01",
            "good material.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_71ED")

    label("loc_713A")


    ChrTalk(
        0x20,
        (
            "#02100FAh, that's right. If you've collected the\x01",
            "gourmet recommendations material, call me\x01",
            "at the news agency reception desk, ok?\x02\x03",
            "#02109FI'll leave it to you guys then♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 5)

    label("loc_71ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_720A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_720A")
    ClearScenarioFlags(0x0, 5)

    label("loc_720A")

    TalkEnd(0xFE)
    Return()

    # Function_34_6DB6 end

    def Function_35_720E(): pass

    label("Function_35_720E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Grace... I hope she doesn't\x01",
            "ask the congresspeople\x01",
            "anything weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, acting as her\x01",
            "safety device is tough.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_720E end

    def Function_36_7290(): pass

    label("Function_36_7290")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_729D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74ED")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7344")

    ChrTalk(
        0x13,
        (
            "#10100FForming the party,\x01",
            "right? Roger that!\x02",
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
    Jump("loc_74E8")

    label("loc_7344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7358")
    Jump("loc_74E8")

    label("loc_7358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746D")

    ChrTalk(
        0x13,
        (
            "#10100FIt's badly damaged... but it\x01",
            "looks like its various\x01",
            "functions are still working.\x02\x03",
            "Once this situation is\x01",
            "settled, I definitely want\x01",
            "to repair it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FRight... Let's ask Chief\x01",
            "Roberts and Master\x01",
            "Guillaume for help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_74E8")

    label("loc_746D")


    ChrTalk(
        0x13,
        (
            "#10100FIt look like its\x01",
            "functions are still\x01",
            "working.\x02\x03",
            "Once this situation is\x01",
            "settled, I definitely\x01",
            "want to repair it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74E8")

    Jump("loc_729D")

    label("loc_74ED")

    TalkEnd(0xFE)
    Return()

    # Function_36_7290 end

    def Function_37_74F1(): pass

    label("Function_37_74F1")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77AF")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7599")

    ChrTalk(
        0x14,
        (
            "#10400FHehe. Changing the\x01",
            "party?\x02",
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
    Jump("loc_77AA")

    label("loc_7599")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75AD")
    Jump("loc_77AA")

    label("loc_75AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77AA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E4")

    ChrTalk(
        0x14,
        (
            "#10406FA fresh supply of troops no\x01",
            "matter how many are\x01",
            "defeated...\x02\x03",
            "Man, how troublesome.\x02\x03",
            "#10401FAt this rate, the guys outside\x01",
            "are just going to get\x01",
            "exhausted. Shouldn't we hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FYes. Let's hurry and\x01",
            "reach "uncle", and get\x01",
            "him to stop all of this!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_77AA")

    label("loc_76E4")


    ChrTalk(
        0x14,
        (
            "#10406FA fresh supply of troops no\x01",
            "matter how many are defeated...\x01",
            "Man, what a troublesome opponent.\x02\x03",
            "#10401FAt this rate, the guys outside\x01",
            "are just going to get exhausted.\x01",
            "Shouldn't we hurry?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77AA")

    Jump("loc_74FE")

    label("loc_77AF")

    TalkEnd(0xFE)
    Return()

    # Function_37_74F1 end

    def Function_38_77B3(): pass

    label("Function_38_77B3")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785C")

    ChrTalk(
        0x15,
        (
            "#10702FYes, let's change\x01",
            "members.\x02",
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
    Jump("loc_79D3")

    label("loc_785C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7870")
    Jump("loc_79D3")

    label("loc_7870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_796D")

    ChrTalk(
        0x15,
        (
            "#10703FThere's no sign of\x01",
            "enemies in the lobby for\x01",
            "now, but...\x02\x03",
            "We had best stay on our\x01",
            "guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThat's definitely a\x01",
            "possibility... We're\x01",
            "counting on you, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#10702FYes, leave it to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_79D3")

    label("loc_796D")


    ChrTalk(
        0x15,
        (
            "#10703FJust in case, I think\x01",
            "it's best to search the\x01",
            "surroundings.\x02\x03",
            "#10701FBe careful, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79D3")

    Jump("loc_77C0")

    label("loc_79D8")

    TalkEnd(0xFE)
    Return()

    # Function_38_77B3 end

    def Function_39_79DC(): pass

    label("Function_39_79DC")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BE4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA5")

    ChrTalk(
        0x16,
        (
            "#00600FYou're changing the\x01",
            "party? ...Hurry up and\x01",
            "choose already.\x02",
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
    Jump("loc_7BDF")

    label("loc_7AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AB9")
    Jump("loc_7BDF")

    label("loc_7AB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BDF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B9F")

    ChrTalk(
        0x16,
        (
            "#00603FAs planned, two members will stand\x01",
            "by here and protect the entrance\x01",
            "in case the worst happens.\x02\x03",
            "#00601F...C'mon, quit dawdling. You guys\x01",
            "should get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...Sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7BDF")

    label("loc_7B9F")


    ChrTalk(
        0x16,
        (
            "#00601F...C'mon, quit dawdling.\x01",
            "You guys should get\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BDF")

    Jump("loc_79E9")

    label("loc_7BE4")

    TalkEnd(0xFE)
    Return()

    # Function_39_79DC end

    def Function_40_7BE8(): pass

    label("Function_40_7BE8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C4E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This elevator is heading\x01",
            "to other floors and shows\x01",
            "no sign of stopping.\x07\x00\x02",
        )
    )

    Jump("loc_7CE9")

    label("loc_7C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C90")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x07\x00\x02",
        )
    )

    Jump("loc_7CE9")

    label("loc_7C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7CE9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This elevator is heading\x01",
            "to other floors and shows\x01",
            "no sign of stopping.\x07\x00\x02",
        )
    )


    label("loc_7CE9")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_7BE8 end

    def Function_41_7CF1(): pass

    label("Function_41_7CF1")

    Sound(160, 0, 100, 0)
    Return()

    # Function_41_7CF1 end

    def Function_42_7CF8(): pass

    label("Function_42_7CF8")

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

    def lambda_7ED7():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7ED7)
    Sleep(200)

    def lambda_7EF4():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7EF4)
    Sleep(200)

    def lambda_7F11():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7F11)
    Sleep(200)

    def lambda_7F2E():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7F2E)
    Sleep(200)

    def lambda_7F4B():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7F4B)
    Sleep(200)

    def lambda_7F68():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7F68)
    Sleep(100)

    def lambda_7F85():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F85)
    Sleep(300)

    def lambda_7F99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7F99)
    Sleep(200)

    def lambda_7FAD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7FAD)
    Sleep(600)

    def lambda_7FC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7FC1)
    Sleep(200)

    def lambda_7FD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7FD5)
    Sleep(300)

    def lambda_7FE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7FE9)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#11PIncredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PIt's luxurious, yet\x01",
            "high-tech...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PIt feels even more\x01",
            "futuristic than even the\x01",
            "IBC building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PEvery floor is connected\x01",
            "to the orbal network, if\x01",
            "I'm not mistaken.\x02\x03",
            "#00200FThere's also a realtime\x01",
            "data link with IBC for\x01",
            "stock price data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PYes. It seems it was\x01",
            ""uncle's" idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PI see. Only a banker\x01",
            "would think of something\x01",
            "like that.\x02",
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
            "#00000F#5PAlright then. All that's\x01",
            "left is to wait until\x01",
            "Dudley comes.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_823D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_823D)
    Sleep(50)

    def lambda_824D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_824D)
    Sleep(50)

    def lambda_825D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_825D)
    Sleep(50)

    def lambda_826D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_826D)
    Sleep(50)

    def lambda_827D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_827D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        (
            "#6P#00102FThere's hardly any visitors\x01",
            "today, so let's wait on the\x01",
            "sofa over there.\x02",
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
            "#1KSame day, 12:00─\x02",
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
        "Man's Voice",
        "#3454V#30W#11A─So you came.\x02",
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

    def lambda_84D6():

        label("loc_84D6")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_84D6")

    QueueWorkItem2(0x101, 2, lambda_84D6)
    Sleep(50)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 5000, 0, 6500, 270)

    def lambda_850F():

        label("loc_850F")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_850F")

    QueueWorkItem2(0x102, 2, lambda_850F)
    Sleep(50)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5000, 0, 7600, 270)

    def lambda_8542():

        label("loc_8542")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8542")

    QueueWorkItem2(0x103, 2, lambda_8542)
    Sleep(50)

    def lambda_8557():

        label("loc_8557")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8557")

    QueueWorkItem2(0x104, 2, lambda_8557)
    Sleep(50)

    def lambda_856C():

        label("loc_856C")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_856C")

    QueueWorkItem2(0x105, 2, lambda_856C)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 5000, 0, 8700, 270)

    def lambda_859C():
        OP_95(0xFE, 4500, 0, 8700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_859C)
    WaitChrThread(0x109, 1)

    def lambda_85BA():

        label("loc_85BA")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_85BA")

    QueueWorkItem2(0x109, 2, lambda_85BA)
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
        "#00000F#5PDetective Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00104FThanks for your hard\x01",
            "work.\x02",
        )
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
            "It's exactly noon─\x02\x03",
            "The conference begins at 13:00.\x02\x03",
            "The heads of state arrive in 30\x01",
            "minutes.\x02",
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
        "#00001F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00101FAnd, where are we going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12P#00606FI wanted to show you\x01",
            "around the meeting area\x01",
            "myself, but...\x02\x03",
            "I'm here to tell you that\x01",
            "someone unexpected will\x01",
            "be doing it instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PSomeone unexpected...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)

    NpcTalk(
        0x23,
        "Man's Voice",
        (
            "─Hello, ladies and\x01",
            "gentlemen. Thank you for\x01",
            "coming.\x02",
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

    def lambda_8945():
        OP_95(0xFE, 7800, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8945)

    def lambda_895F():

        label("loc_895F")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_895F")

    QueueWorkItem2(0x101, 2, lambda_895F)

    def lambda_8971():

        label("loc_8971")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8971")

    QueueWorkItem2(0x102, 2, lambda_8971)

    def lambda_8983():

        label("loc_8983")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8983")

    QueueWorkItem2(0x103, 2, lambda_8983)

    def lambda_8995():

        label("loc_8995")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8995")

    QueueWorkItem2(0x104, 2, lambda_8995)

    def lambda_89A7():

        label("loc_89A7")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_89A7")

    QueueWorkItem2(0x109, 2, lambda_89A7)

    def lambda_89B9():

        label("loc_89B9")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_89B9")

    QueueWorkItem2(0x105, 2, lambda_89B9)

    def lambda_89CB():

        label("loc_89CB")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_89CB")

    QueueWorkItem2(0x16, 2, lambda_89CB)
    WaitChrThread(0x23, 1)
    TurnDirection(0x23, 0x101, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00011FMayor Dieter!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F"Uncle"!\x02",
    )

    CloseMessageWindow()

    def lambda_8A1A():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8A1A)
    Sleep(1000)
    Fade(500)
    OP_68(4000, 900, 6200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_8A6A():
        OP_96(0xFE, 0x898, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8A6A)
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
            "It's been half a month, Elie and\x01",
            "Lloyd.\x02\x03",
            "Wazy and Noｱl...\x02\x03",
            "Oh, and Randy and Tio. Long time\x01",
            "no see.\x02",
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
        "#00309F#5PHaha, same here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00204FNice to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PBut, why are you here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PIt's just before the\x01",
            "conference starts.\x01",
            "Aren't you busy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#12P#02804FPreparations have been complete\x01",
            "for a while. We just have to\x01",
            "wait for the leaders to arrive.\x02\x03",
            "#02800FFor a change of pace, I thought\x01",
            "I'd show you guys around for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x16, 500)
    Sleep(150)

    ChrTalk(
        0x23,
        (
            "#02800F#11PDudley, is that all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#6P#00606FHmph... If the mayor\x01",
            "says so.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x16,
        (
            "#6P#00600F─Everyone, please. Don't\x01",
            "be rude to the mayor.\x02\x03",
            "And once you're done,\x01",
            "come to the security\x01",
            "planning room on 34F.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 500)

    ChrTalk(
        0x101,
        "#5P#00000FUnderstood.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x23, 500)
    Sleep(300)

    ChrTalk(
        0x16,
        (
            "#6P#00603FAlright then, Mr. Mayor.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02800F#11PYeah, thanks.\x02",
    )

    CloseMessageWindow()

    def lambda_8E55():

        label("loc_8E55")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8E55")

    QueueWorkItem2(0x101, 2, lambda_8E55)

    def lambda_8E67():

        label("loc_8E67")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8E67")

    QueueWorkItem2(0x102, 2, lambda_8E67)

    def lambda_8E79():

        label("loc_8E79")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8E79")

    QueueWorkItem2(0x103, 2, lambda_8E79)

    def lambda_8E8B():

        label("loc_8E8B")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8E8B")

    QueueWorkItem2(0x104, 2, lambda_8E8B)

    def lambda_8E9D():

        label("loc_8E9D")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8E9D")

    QueueWorkItem2(0x109, 2, lambda_8E9D)

    def lambda_8EAF():

        label("loc_8EAF")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8EAF")

    QueueWorkItem2(0x105, 2, lambda_8EAF)

    def lambda_8EC1():

        label("loc_8EC1")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8EC1")

    QueueWorkItem2(0x23, 2, lambda_8EC1)
    OP_92(0x16, 0x0, 0x8FC, 0x1F4)
    OP_68(1000, 900, 2200, 3000)

    def lambda_8EF1():
        OP_95(0xFE, 0, 0, 2300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8EF1)
    WaitChrThread(0x16, 1)

    def lambda_8F0F():
        OP_95(0xFE, 0, 0, -5000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8F0F)
    Sleep(2000)
    Sound(107, 0, 100, 0)

    def lambda_8F32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8F32)
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
            "#02804FHaha. He's a capable\x01",
            "detective but a bit\x01",
            "inflexible.\x02\x03",
            "#02800FAlthough with his job,\x01",
            "that might be a virtue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, the demon of\x01",
            "Section One does have\x01",
            "his dignity.\x02",
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
            "#6P#02805FWhoops, I forgot to say the\x01",
            "most important thing...\x02\x03",
            "#02809F─Ladies and gentlemen of the\x01",
            "Special Support Section,\x01",
            "welcome to Orchis Tower!\x02\x03",
            "Come now, follow me!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91AA():

        label("loc_91AA")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_91AA")

    QueueWorkItem2(0x101, 2, lambda_91AA)

    def lambda_91BC():

        label("loc_91BC")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_91BC")

    QueueWorkItem2(0x102, 2, lambda_91BC)

    def lambda_91CE():

        label("loc_91CE")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_91CE")

    QueueWorkItem2(0x103, 2, lambda_91CE)

    def lambda_91E0():

        label("loc_91E0")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_91E0")

    QueueWorkItem2(0x104, 2, lambda_91E0)

    def lambda_91F2():

        label("loc_91F2")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_91F2")

    QueueWorkItem2(0x109, 2, lambda_91F2)

    def lambda_9204():

        label("loc_9204")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_9204")

    QueueWorkItem2(0x105, 2, lambda_9204)
    OP_92(0x23, 0x1B58, 0x3E8, 0x1F4)
    OP_68(6500, 1000, 3000, 3000)

    def lambda_9234():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9234)
    WaitChrThread(0x23, 1)

    def lambda_9252():
        OP_95(0xFE, 12000, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9252)
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
        (
            "#00302F#5PHaha, he's the same as\x01",
            "ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FOnly Mariabell's father\x01",
            "could be like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FW-Well, looks like he's going\x01",
            "to show us around since he's\x01",
            "here for the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000FYeah. Shall we accept\x01",
            "his offer?\x02",
        )
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_94B1")
    Jump("loc_94B6")

    label("loc_94B1")

    OP_29(0x71, 0x4, 0x40)

    label("loc_94B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_94C7")
    Jump("loc_94CC")

    label("loc_94C7")

    OP_29(0x72, 0x4, 0x40)

    label("loc_94CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_94DD")
    Jump("loc_94E2")

    label("loc_94DD")

    OP_29(0x77, 0x4, 0x40)

    label("loc_94E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_94F3")
    Jump("loc_94F8")

    label("loc_94F3")

    OP_29(0x79, 0x4, 0x40)

    label("loc_94F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9509")
    Jump("loc_950E")

    label("loc_9509")

    OP_29(0x7A, 0x4, 0x40)

    label("loc_950E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_951F")
    Jump("loc_9524")

    label("loc_951F")

    OP_29(0x7B, 0x4, 0x40)

    label("loc_9524")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9535")
    Jump("loc_953A")

    label("loc_9535")

    OP_29(0x7C, 0x4, 0x40)

    label("loc_953A")

    OP_1B(0x0, 0x0, 0x33)
    EventEnd(0x5)
    Return()

    # Function_42_7CF8 end

    def Function_43_9542(): pass

    label("Function_43_9542")


    def lambda_9547():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9547)
    WaitChrThread(0x16, 1)

    def lambda_9565():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9565)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x0, 0x1F4)
    Return()

    # Function_43_9542 end

    def Function_44_9586(): pass

    label("Function_44_9586")

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
        (
            "#6P#10105FThere's even three\x01",
            "elevators...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWow, how luxurious.\x02",
    )

    CloseMessageWindow()

    def lambda_96EA():
        OP_97(0x102, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_96EA)
    Sleep(50)

    def lambda_9707():
        OP_97(0x101, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9707)
    Sleep(50)

    def lambda_9724():
        OP_97(0x104, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9724)
    Sleep(50)

    def lambda_9741():
        OP_97(0x103, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9741)
    Sleep(50)

    def lambda_975E():
        OP_97(0x105, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_975E)
    Sleep(50)

    def lambda_977B():
        OP_97(0x109, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_977B)
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
            "#02804F#11PWell, the building IS 40\x01",
            "floors tall.\x02\x03",
            "#02800FIf you include the\x01",
            "private elevators, there\x01",
            "are six in all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FThat's incredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#02803F#11PNow then, it's not like I can show you\x01",
            "every floor. This tour will be limited\x01",
            "to the meeting-related floors.\x02\x03",
            "#02800FFirst, let's head to the security\x01",
            "planning room on 34F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PPlease do.\x02",
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

    # Function_44_9586 end

    def Function_45_998F(): pass

    label("Function_45_998F")

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

    # Function_45_998F end

    def Function_46_99C3(): pass

    label("Function_46_99C3")


    def lambda_99C8():
        OP_95(0xFE, 81000, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99C8)
    WaitChrThread(0xFE, 1)

    def lambda_99E6():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99E6)
    Sleep(500)

    def lambda_9A03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A03)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_99C3 end

    def Function_47_9A14(): pass

    label("Function_47_9A14")

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

    def lambda_9B44():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9B44)
    Sleep(200)

    def lambda_9B61():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9B61)
    Sleep(200)

    def lambda_9B7E():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9B7E)
    Sleep(200)

    def lambda_9B9B():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9B9B)
    Sleep(200)

    def lambda_9BB8():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9BB8)
    Sleep(200)

    def lambda_9BD5():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9BD5)
    SetCameraDistance(18500, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(100)

    def lambda_9C0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9C0A)
    Sleep(300)

    def lambda_9C1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9C1E)
    Sleep(200)

    def lambda_9C32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9C32)
    Sleep(600)

    def lambda_9C46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9C46)
    Sleep(200)

    def lambda_9C5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9C5A)
    Sleep(300)

    def lambda_9C6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9C6E)
    Sound(803, 2, 100, 0)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_9CA4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9CA4)
    Sleep(50)

    def lambda_9CB4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9CB4)
    Sleep(50)

    def lambda_9CC4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9CC4)
    Sleep(50)

    def lambda_9CD4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9CD4)
    Sleep(50)

    def lambda_9CE4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9CE4)

    ChrTalk(
        0x101,
        "#00005F#11POh...\x02",
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
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey. Where are you guys?\x02\x03",
            "We just finished\x01",
            "preparing our equipment.\x02",
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
            "#00004FWe just arrived at the\x01",
            "tower entrance.\x02\x03",
            "#00000FShould we just head up\x01",
            "to the roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah. If you ask the\x01",
            "receptionist, they'll give\x01",
            "you an elevator access card.\x02\x03",
            "So get up here already.\x02",
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
            "#00002FUnderstood. And thanks\x01",
            "for your hard work.\x02",
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
        "#11P#00202FLooks like he's ready.\x02",
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
            "#00000F#5PYeah. Let's speak to the\x01",
            "receptionist for an access card\x01",
            "and then head to the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FIt's raining, so we\x01",
            "shouldn't make them wait\x01",
            "too long.\x02",
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

    # Function_47_9A14 end

    def Function_48_A074(): pass

    label("Function_48_A074")

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
        "#5PWelcome to Orchis Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAh, you're the Special\x01",
            "Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYes. Will you issue us\x01",
            "an authentication card?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYes, here you go.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x35E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#5PPut that card in elevator\x01",
            "panel and it will take you\x01",
            "directly to the 40F top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt is valid for only a month and\x01",
            "disposable, so please dispose of\x01",
            "it when you're finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PR-Roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10112F(That's kind of\x01",
            "amazing...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P(Yeah. It's even more\x01",
            "advanced than the IBC\x01",
            "building...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302F(The building itself is\x01",
            "basically just a giant mass\x01",
            "of the latest tech, right?)\x02",
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

    # Function_48_A074 end

    def Function_49_A409(): pass

    label("Function_49_A409")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A429")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_A429")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43D")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_A43D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A451")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_A451")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A465")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_A465")

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
            "#12P#10104F...It's fine. All\x01",
            "systems functioning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FI see... We really rely\x01",
            "on this thing a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6P...I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI want to maintain it\x01",
            "properly later.\x02",
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

    def lambda_A730():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_A730)
    Sleep(30)

    def lambda_A740():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A740)
    Sleep(30)

    def lambda_A750():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_A750)
    Sleep(30)

    def lambda_A760():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A760)
    Sleep(30)

    def lambda_A770():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A770)
    Sleep(30)

    def lambda_A780():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A780)
    Sleep(30)

    def lambda_A790():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A790)
    Sleep(30)

    def lambda_A7A0():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A7A0)
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
        (
            "#5P#10708F...Looks like they're\x01",
            "still coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401FIt seems they can\x01",
            "generate an unlimited\x01",
            "number of them.\x02",
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
            "#5P#00306FThere's no time. Let's\x01",
            "head for the elevators.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(
        0x10A,
        (
            "#6P#00603FAs planned, two people\x01",
            "will stand by here.\x02\x03",
            "#00600FYou choose, Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)

    def lambda_A92B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A92B)
    Sleep(30)

    def lambda_A93B():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A93B)
    Sleep(30)

    def lambda_A94B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A94B)
    Sleep(30)

    def lambda_A95B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A95B)
    Sleep(30)

    def lambda_A96B():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_A96B)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        "#11P#00001FRoger that.\x02",
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

    # Function_49_A409 end

    def Function_50_AA3F(): pass

    label("Function_50_AA3F")

    EventBegin(0x1)
    OP_4B(0x1F, 0xFF)
    TurnDirection(0x1F, 0x0, 500)

    ChrTalk(
        0x1F,
        (
            "Do you have an\x01",
            "authentication card?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "If not, you can't use\x01",
            "the elevator.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 74460, 0, 1270, 180)
    OP_93(0x1F, 0xB4, 0x0)
    OP_4C(0x1F, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_50_AA3F end

    def Function_51_AABD(): pass

    label("Function_51_AABD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB6B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The sound of\x01",
            "intermittent gunfire can\x01",
            "be heard from the plaza.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001FEveryone's been fighting\x01",
            "for us this whole time.\x02\x03",
            "Let's hurry forward!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABC7")

    ChrTalk(
        0x101,
        (
            "#00001FLet's not keep the mayor\x01",
            "waiting too long. Let's\x01",
            "hurry after him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC7")

    SetChrPos(0x0, -290, 0, -3540, 0)
    EventEnd(0x4)
    Return()

    # Function_51_AABD end

    def Function_52_ABDB(): pass

    label("Function_52_ABDB")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ABED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD6B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_AC56")
    MenuCmd(1, 0, "Rest in Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AC56")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACE6")

    ChrTalk(
        0x101,
        (
            "#00001F...There's no need to move it\x01",
            "right now. Let's repair it\x01",
            "after the incident's resolved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD66")

    label("loc_ACE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5C")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_AD1F")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_AD37")

    label("loc_AD1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AD32")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_AD37")

    label("loc_AD32")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_AD37")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD66")

    label("loc_AD5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD66")

    Jump("loc_ABED")

    label("loc_AD6B")

    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_52_ABDB end

    SaveToFile()

Try(main)
