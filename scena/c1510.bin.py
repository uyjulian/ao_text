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
        "Function_6_ED8",          # 06, 6
        "Function_7_EDC",          # 07, 7
        "Function_8_1E1A",         # 08, 8
        "Function_9_1E1E",         # 09, 9
        "Function_10_2B34",        # 0A, 10
        "Function_11_2B38",        # 0B, 11
        "Function_12_39C1",        # 0C, 12
        "Function_13_39C5",        # 0D, 13
        "Function_14_3A7F",        # 0E, 14
        "Function_15_3EA0",        # 0F, 15
        "Function_16_4DD1",        # 10, 16
        "Function_17_4EA2",        # 11, 17
        "Function_18_4FF5",        # 12, 18
        "Function_19_5056",        # 13, 19
        "Function_20_50AC",        # 14, 20
        "Function_21_50FC",        # 15, 21
        "Function_22_5196",        # 16, 22
        "Function_23_5713",        # 17, 23
        "Function_24_57A5",        # 18, 24
        "Function_25_5885",        # 19, 25
        "Function_26_594E",        # 1A, 26
        "Function_27_59F2",        # 1B, 27
        "Function_28_5D9A",        # 1C, 28
        "Function_29_5E59",        # 1D, 29
        "Function_30_5FDD",        # 1E, 30
        "Function_31_6046",        # 1F, 31
        "Function_32_618F",        # 20, 32
        "Function_33_6BA1",        # 21, 33
        "Function_34_6FEB",        # 22, 34
        "Function_35_7463",        # 23, 35
        "Function_36_74EB",        # 24, 36
        "Function_37_7749",        # 25, 37
        "Function_38_7A29",        # 26, 38
        "Function_39_7C71",        # 27, 39
        "Function_40_7E66",        # 28, 40
        "Function_41_7F6F",        # 29, 41
        "Function_42_7F76",        # 2A, 42
        "Function_43_9817",        # 2B, 43
        "Function_44_985B",        # 2C, 44
        "Function_45_9C63",        # 2D, 45
        "Function_46_9C97",        # 2E, 46
        "Function_47_9CE8",        # 2F, 47
        "Function_48_A351",        # 30, 48
        "Function_49_A6E3",        # 31, 49
        "Function_50_AD1F",        # 32, 50
        "Function_51_AD9D",        # 33, 51
        "Function_52_AEBD",        # 34, 52
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
            "There is a car magazine, "Fast Running Mach".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x370, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED4")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Cool Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x370, 1)

    label("loc_ED4")

    TalkEnd(0xFF)
    Return()

    # Function_5_E25 end

    def Function_6_ED8(): pass

    label("Function_6_ED8")

    Call(0, 7)
    Return()

    # Function_6_ED8 end

    def Function_7_EDC(): pass

    label("Function_7_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEE")
    Call(0, 48)
    Return()

    label("loc_EEE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101D")

    ChrTalk(
        0x8,
        (
            "For now, it was decided\x01",
            "management of Orchis Tower will\x01",
            "be led by Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There is still a lot of confusion...\x01",
            "But the fact that this building is a\x01",
            "place for the people hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I look forward to working with\x01",
            "all of you in the future too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10AA")

    label("loc_101D")


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
            "I look forward to working with\x01",
            "all of you in the future too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    Jump("loc_1E16")

    label("loc_10AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_10BD")
    Jump("loc_1E16")

    label("loc_10BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10CB")
    Jump("loc_1E16")

    label("loc_10CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_123F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AB")

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
            "Many things have been\x01",
            "prepared to make\x01",
            "everyone smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You all should participate\x01",
            "if you have time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_123A")

    label("loc_11AB")


    ChrTalk(
        0x8,
        (
            "But even so... \x01",
            "I was surprised at the speed\x01",
            "at which IBC was restored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It made me realize\x01",
            "the magnificence of\x01",
            "orbal net technology.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123A")

    Jump("loc_1E16")

    label("loc_123F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1474")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139B")

    ChrTalk(
        0x8,
        (
            "It's something obvious, but...\x01",
            "Uneasiness is spreading\x01",
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
            "Of course the CGF, but also the Mayor\x01",
            "and Chairman are doing their best.\x02",
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
    Jump("loc_146F")

    label("loc_139B")


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

    label("loc_146F")

    Jump("loc_1E16")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_15F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153D")

    ChrTalk(
        0x8,
        (
            "A civic forum with the theme of state\x01",
            "independence is being held\x01",
            "today at the City Meeting Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The program has some\x01",
            "open seats, so please\x01",
            "participate if interested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F3")

    label("loc_153D")


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
            "It is good for one month and disposable,\x01",
            "so please discard it when you are finished.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F3")

    Jump("loc_1E16")

    label("loc_15F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1823")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1794")

    ChrTalk(
        0x8,
        (
            "Welcome. If you have a\x01",
            "question on the train accident, \x01",
            "I can help you here.\x02",
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
            "If you are hurrying to the\x01",
            "Empire or Republic, please\x01",
            "use a bus or airship.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_181E")

    label("loc_1794")


    ChrTalk(
        0x8,
        (
            "If you are hurrying to the\x01",
            "Empire or Republic, please\x01",
            "use a bus or airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If necessary, we can prepare\x01",
            "a ticket for you here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181E")

    Jump("loc_1E16")

    label("loc_1823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BF")

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
            "Please look forward to future\x01",
            "developments at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A62")

    label("loc_19BF")


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
            "Please look forward to future\x01",
            "developments at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A62")

    Jump("loc_1E16")

    label("loc_1A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6D")

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
    Jump("loc_1C3A")

    label("loc_1B6D")


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

    label("loc_1C3A")

    Jump("loc_1E16")

    label("loc_1C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_1E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D62")

    ChrTalk(
        0x8,
        (
            "Good work, everyone.\x01",
            "This is the Orchis Tower\x01",
            "integrated reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, all of the staff here, at the direction\x01",
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
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E16")

    label("loc_1D62")


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

    label("loc_1E16")

    TalkEnd(0x8)
    Return()

    # Function_7_EDC end

    def Function_8_1E1A(): pass

    label("Function_8_1E1A")

    Call(0, 9)
    Return()

    # Function_8_1E1A end

    def Function_9_1E1E(): pass

    label("Function_9_1E1E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F29")

    ChrTalk(
        0x9,
        (
            "It seems all of those monsters that\x01",
            "appeared in the city have disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was really scared when I too\x01",
            "was locked inside the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems the damage wasn't even\x01",
            "that great, but I never want to\x01",
            "go through that again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FC6")

    label("loc_1F29")


    ChrTalk(
        0x9,
        (
            "I was really scared when I too\x01",
            "was locked inside the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems the damage wasn't even\x01",
            "that great, but I never want to\x01",
            "go through that again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC6")

    Jump("loc_2B30")

    label("loc_1FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1FD9")
    Jump("loc_2B30")

    label("loc_1FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FE7")
    Jump("loc_2B30")

    label("loc_1FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2127")

    ChrTalk(
        0x9,
        (
            "At the time of the attack,  when I was\x01",
            "heading to the basement shelter,\x01",
            "I saw a conflict in the plaza...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As for the scene with the\x01",
            "armed group closing in, \x01",
            "I can only say it was scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thankfully this building was\x01",
            "safe somehow, but... I really\x01",
            "didn't think I'd live through it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21DE")

    label("loc_2127")


    ChrTalk(
        0x9,
        (
            "As for the scene with the\x01",
            "armed group closing in, \x01",
            "I can only say it was scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thankfully this building was\x01",
            "safe somehow, but... I really\x01",
            "didn't think I'd live through it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DE")

    Jump("loc_2B30")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_23CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2300")

    ChrTalk(
        0x9,
        (
            "The noisy situation at\x01",
            "St. Ursula Hospital has\x01",
            "continued since last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of the large number\x01",
            "of patients, they're short\x01",
            "of staff and supplies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I think of the men and\x01",
            "women fighting at the scene,\x01",
            "I have great respect for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23CA")

    label("loc_2300")


    ChrTalk(
        0x9,
        (
            "At present, we're using all our resources\x01",
            "and taking many kind of supporting\x01",
            "measures for the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I think of the men and\x01",
            "women fighting at the scene,\x01",
            "I have great respect for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CA")

    Jump("loc_2B30")

    label("loc_23CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2551")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AE")

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
            "We'll discuss reparations later, but...\x01",
            "For now, I'm glad the accident\x01",
            "recovery didn't drag on too long.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_254C")

    label("loc_24AE")


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
            "For now, I'm glad the accident\x01",
            "recovery didn't drag on too long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254C")

    Jump("loc_2B30")

    label("loc_2551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_25FA")

    ChrTalk(
        0x9,
        (
            "I just received word. They\x01",
            "said transport of injured\x01",
            "passengers is complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's a relief... Next, we need\x01",
            "to worry about the accident scene.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B30")

    label("loc_25FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275F")

    ChrTalk(
        0x9,
        (
            "Everyone, do you\x01",
            "know the meaning of\x01",
            "Orchis Tower's name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Orchis is from "orchid"... \x01",
            "A beautiful flower in which a single\x01",
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
            "Uh uh. Thinking about it that way,\x01",
            "it's a fitting name, don't you agree?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_281C")

    label("loc_275F")


    ChrTalk(
        0x9,
        (
            "Orchis is from "orchid"... \x01",
            "A beautiful flower in which a single\x01",
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

    label("loc_281C")

    Jump("loc_2B30")

    label("loc_2821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2999")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E2")

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
    Jump("loc_2994")

    label("loc_28E2")


    ChrTalk(
        0x9,
        (
            "Also, you can go to City Meeting\x01",
            "Hall as well for most services\x01",
            "offered at this window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Getting here is a bit\x01",
            "difficult, so please feel\x01",
            "free to use their services too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2994")

    Jump("loc_2B30")

    label("loc_2999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_2B30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A85")

    ChrTalk(
        0x9,
        (
            "The main session will finally\x01",
            "start in another hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "During the conference,\x01",
            "I will be here handling\x01",
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
    Jump("loc_2B30")

    label("loc_2A85")


    ChrTalk(
        0x9,
        (
            "The main session's in another\x01",
            "hour... And the heads of state\x01",
            "will be coming for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*. It's not like I'm\x01",
            "doing an important job,\x01",
            "but I'm nervous somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B30")

    TalkEnd(0x9)
    Return()

    # Function_9_1E1E end

    def Function_10_2B34(): pass

    label("Function_10_2B34")

    Call(0, 11)
    Return()

    # Function_10_2B34 end

    def Function_11_2B38(): pass

    label("Function_11_2B38")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4C")

    ChrTalk(
        0xA,
        (
            "Most of the staff and State Guard that were\x01",
            "arrested in Orchis Tower have been released.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We were mostly dealing with\x01",
            "their neglected positions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Especially because of times\x01",
            "like these, we must work to\x01",
            "properly support the citizens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D1F")

    label("loc_2C4C")


    ChrTalk(
        0xA,
        (
            "About the staff and the State Guard who\x01",
            "were arrested in Orchis Tower, we're\x01",
            "mostly dealing with their positions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Especially because of times\x01",
            "like these, we must work to\x01",
            "properly support the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1F")

    Jump("loc_39BD")

    label("loc_2D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D32")
    Jump("loc_39BD")

    label("loc_2D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D40")
    Jump("loc_39BD")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4D")

    ChrTalk(
        0xA,
        (
            "Arios MacLaine...\x01",
            "He's the real hero of Crossbell.\x02",
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
            "It's a wild idea, but if we have him, \x01",
            "we needn't fear the two major\x01",
            "powers... I really thought so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EEE")

    label("loc_2E4D")


    ChrTalk(
        0xA,
        (
            "Arios MacLaine...\x01",
            "He's the real hero of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's a wild idea, but if we have him, \x01",
            "we needn't fear the two major\x01",
            "powers... I really thought so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEE")

    Jump("loc_39BD")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_311F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303B")

    ChrTalk(
        0xA,
        (
            "Based on what I've heard,\x01",
            "the CGF aren't doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If there are more injured, they're\x01",
            "thinking of sending in the police, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On the other hand, city\x01",
            "defenses can't be neglected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They've tried everything, but a\x01",
            "solution based on dialogue and\x01",
            "negotiation just won't go through.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_311A")

    label("loc_303B")


    ChrTalk(
        0xA,
        (
            "They've tried everything, but a\x01",
            "solution based on dialogue and\x01",
            "negotiation just won't go through.\x02",
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

    label("loc_311A")

    Jump("loc_39BD")

    label("loc_311F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325A")

    ChrTalk(
        0xA,
        (
            "*sigh*. It's a relief that\x01",
            "restoration of the rail line was\x01",
            "somehow completed yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the trains had remained stopped like that,\x01",
            "every sort of compensation claims would've\x01",
            "come skyrocketing towards Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We owe this to the CGF, who\x01",
            "worked all through the night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_331C")

    label("loc_325A")


    ChrTalk(
        0xA,
        (
            "If the trains had remained stopped like that,\x01",
            "every sort of compensation claims would've\x01",
            "come skyrocketing towards Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We owe this to the CGF, who\x01",
            "worked all through the night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331C")

    Jump("loc_39BD")

    label("loc_3321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_34EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344E")

    ChrTalk(
        0xA,
        (
            "Of course we too\x01",
            "received word of the\x01",
            "train accident quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're also replying quickly to inquiries\x01",
            "from all over the places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're now preparing emergency information\x01",
            "and arrangements about transfer and transport\x01",
            "methods alternative to the orbal railway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_34E9")

    label("loc_344E")


    ChrTalk(
        0xA,
        (
            "Even so, a train accident...\x01",
            "Rare things happen too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Crossbell railway is a\x01",
            "straight line with good visibility,\x01",
            "so accidents rarely occur...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E9")

    Jump("loc_39BD")

    label("loc_34EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_35BD")

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
            "Uh uh. It was fun watching the\x01",
            "dumbfounded expressions on\x01",
            "visitors' faces on opening day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BD")

    label("loc_35BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3746")

    ChrTalk(
        0xA,
        (
            "Oh, you guys are that Special Support\x01",
            "Section participating in the security detail\x01",
            "for the Trade Conference today, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm. This is a good chance,\x01",
            "so I'll explain it to you. This\x01",
            "is the administration window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I handle public records\x01",
            "requests, policy inquiries\x01",
            "and the likes right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, please let me know\x01",
            "if you ever need anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37D5")

    label("loc_3746")


    ChrTalk(
        0xA,
        (
            "This window is for dealing\x01",
            "with administrative matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I handle public records\x01",
            "requests, policy inquiries\x01",
            "and the likes right here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D5")

    Jump("loc_39BD")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_39BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3913")

    ChrTalk(
        0xA,
        (
            "Management and administration of Orchis Tower is an\x01",
            "important responsibility of General Affairs Section One.\x02",
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
            "We're finally done now, but... \x01",
            "We were very busy just a little while ago.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39BD")

    label("loc_3913")


    ChrTalk(
        0xA,
        (
            "*sigh*. Anyway, I'm glad we\x01",
            "finished in time for the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Though we can't lose focus until the end, all\x01",
            "that's left is to wait for the conference to start.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BD")

    TalkEnd(0xA)
    Return()

    # Function_11_2B38 end

    def Function_12_39C1(): pass

    label("Function_12_39C1")

    Call(0, 13)
    Return()

    # Function_12_39C1 end

    def Function_13_39C5(): pass

    label("Function_13_39C5")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A26")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3A26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A46")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A76")

    label("loc_3A46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5A")
    Jump("loc_3A76")

    label("loc_3A5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A76")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_3A76")

    Jump("loc_39D2")

    label("loc_3A7B")

    TalkEnd(0xD)
    Return()

    # Function_13_39C5 end

    def Function_14_3A7F(): pass

    label("Function_14_3A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B80")

    ChrTalk(
        0xD,
        (
            "IBC's business is suspended too...\x01",
            "And also half the staff are\x01",
            "standing by at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "As someone who has worked for \x01",
            "IBC for many years, the arrest of\x01",
            "Mr. Dieter is too much of a shock...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We have to get\x01",
            "through this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3C20")

    label("loc_3B80")


    ChrTalk(
        0xD,
        (
            "Even with IBC operations\x01",
            "suspended, we can still perform\x01",
            "the Sepith exchange service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please feel free to speak with\x01",
            "me when you are ready to use it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C20")

    Jump("loc_3E9F")

    label("loc_3C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD0")

    ChrTalk(
        0x102,
        (
            "#00100FGood work, Miss Lanfei.\x02\x03",
            "It looks like you've settled in\x01",
            "after relocating the window desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "My my, if it isn't Lady Elie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. This too is thanks to\x01",
            "Acting President Mariabell and\x01",
            "the technology division staff.\x02",
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
            "If there is anything you need,\x01",
            "please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FWe will, and thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3E9F")

    label("loc_3DD0")


    ChrTalk(
        0xD,
        (
            "At present, IBC is moving\x01",
            "operations into this Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Please feel free to use the Sepith\x01",
            "exchange service as you have until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If there is anything you need,\x01",
            "please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9F")

    Return()

    # Function_14_3A7F end

    def Function_15_3EA0(): pass

    label("Function_15_3EA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5F")

    ChrTalk(
        0xFE,
        (
            "Separated families and friends\x01",
            "are meeting up again one by one.\x02",
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
    Jump("loc_3FF1")

    label("loc_3F5F")


    ChrTalk(
        0xFE,
        (
            "By the way, your broken orbal car\x01",
            "was carried outside earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like you treated it very well,\x01",
            "so I really sympathize with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF1")

    Jump("loc_4DCD")

    label("loc_3FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4004")
    Jump("loc_4DCD")

    label("loc_4004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4012")
    Jump("loc_4DCD")

    label("loc_4012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4181")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower got through the\x01",
            "attack safely somehow thanks\x01",
            "to the great efforts of Mr. Arios...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC building... It literally\x01",
            "disappeared without a trace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were hardly any\x01",
            "civilian casualties, but even\x01",
            "Arc-en-ciel was involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if it was a warning\x01",
            "or something, but such a\x01",
            "thing can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_422E")

    label("loc_4181")


    ChrTalk(
        0xFE,
        (
            "There were hardly any\x01",
            "civilian casualties, but even\x01",
            "Arc-en-ciel was involved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if it was a warning\x01",
            "or something, but such a\x01",
            "thing can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422E")

    Jump("loc_4DCD")

    label("loc_4233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_431F")

    ChrTalk(
        0xFE,
        (
            "I seems both the Mayor and Chairman\x01",
            "have been working ever since last night\x01",
            "on a way to deal with the occupation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What can we do about the situation?\x01",
            "Anyway, we have to stay focused\x01",
            "and prepare for an emergency.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCD")

    label("loc_431F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_452E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447C")

    ChrTalk(
        0xFE,
        (
            "Though they're not the same as the monster\x01",
            "that caused the train accident yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about the Cryptids that\x01",
            "have been appearing often recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard mysterious azure\x01",
            "flowers have been confirmed\x01",
            "near where they've appeared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What does this mean? That\x01",
            "there'll be even more accidents?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4529")

    label("loc_447C")


    ChrTalk(
        0xFE,
        (
            "Because we don't know the details,\x01",
            "we can't say for sure that\x01",
            "Cryptids won't appear in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really quite strange...\x01",
            "Anyhow, we can't\x01",
            "let down our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4529")

    Jump("loc_4DCD")

    label("loc_452E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_45BC")

    ChrTalk(
        0xFE,
        "An orbal train derailment, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the cause is being investigated,\x01",
            "but... Could it be terrorists again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DCD")

    label("loc_45BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4728")

    ChrTalk(
        0xFE,
        (
            "Though I'm a police officer,\x01",
            "I'm treated here like one\x01",
            "of their staff members.\x02",
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
            "building. Even so, it's located\x01",
            "higher than the IBC's roof...\x02",
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
    Jump("loc_47D5")

    label("loc_4728")


    ChrTalk(
        0xFE,
        (
            "Anyway, there're also talks\x01",
            "to open the cafe to citizens\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know when it'll happen, \x01",
            "but when it does, I'm sure\x01",
            "it'll be a popular spot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47D5")

    Jump("loc_4DCD")

    label("loc_47DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C1")

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't the Special Support\x01",
            "Section. Welcome to Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business here, please\x01",
            "ask at the front reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Visitors can't do\x01",
            "anything here until\x01",
            "they do that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4942")

    label("loc_48C1")


    ChrTalk(
        0xFE,
        (
            "If you have business here, please\x01",
            "ask at the front reception desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Visitors can't do\x01",
            "anything here until\x01",
            "they do that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4942")

    Jump("loc_4DCD")

    label("loc_4947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_END)), "loc_4DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D5A")

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
            "So the rumor that you guys were the\x01",
            "mayor's favorites was true after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUmm, what can we say about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's not the\x01",
            "case that I'm jealous.\x01",
            "No offense intended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because, personally, \x01",
            "I'm rooting for you guys.\x02",
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
            "#00202F...Somehow I feel like people have a much \x01",
            "higher opinion of us than half a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FOh yeah. We were called names\x01",
            "like "fake Bracers" and\x01",
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
            "#10302FHu hu. Members of an organization\x01",
            "disparage each other quite a bit, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha. Indeed there were people\x01",
            "who called you that back then.\x02",
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
        "#00000FYes, agreed.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 0)
    Jump("loc_4DCD")

    label("loc_4D5A")


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
        "Let's both do our best today.\x02",
    )

    CloseMessageWindow()

    label("loc_4DCD")

    TalkEnd(0xFE)
    Return()

    # Function_15_3EA0 end

    def Function_16_4DD1(): pass

    label("Function_16_4DD1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*, when it rains, you can't even go\x01",
            "outside to get some fresh air for a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, this entrance is\x01",
            "a pretty nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the height of this\x01",
            "ceiling is frankly the best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_4DD1 end

    def Function_17_4EA2(): pass

    label("Function_17_4EA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F75")

    ChrTalk(
        0xFE,
        (
            "12:00―― Nothing especially\x01",
            "out of the ordinary, they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No sign of terrorists have\x01",
            "been detected yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just where are those guys planning\x01",
            "to invade from, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FF1")

    label("loc_4F75")


    ChrTalk(
        0xFE,
        (
            "No sign of terrorists have\x01",
            "been detected yet, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just where are those guys planning\x01",
            "to invade from, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF1")

    TalkEnd(0xFE)
    Return()

    # Function_17_4EA2 end

    def Function_18_4FF5(): pass

    label("Function_18_4FF5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Umm, entry to the VIP room\x01",
            "is prohibited beginning from\x01",
            "the conference start, right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4FF5 end

    def Function_19_5056(): pass

    label("Function_19_5056")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Yeah, exactly. It goes\x01",
            "without saying we have\x01",
            "to hasten the preparations.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_5056 end

    def Function_20_50AC(): pass

    label("Function_20_50AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C1")
    Call(0, 29)
    Jump("loc_50F8")

    label("loc_50C1")


    ChrTalk(
        0xFE,
        (
            "Y-You guys...\x01",
            "Get out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm busy now!\x02",
    )

    CloseMessageWindow()

    label("loc_50F8")

    TalkEnd(0xFE)
    Return()

    # Function_20_50AC end

    def Function_21_50FC(): pass

    label("Function_21_50FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5111")
    Call(0, 31)
    Jump("loc_5192")

    label("loc_5111")


    ChrTalk(
        0xFE,
        (
            "Chief Roberts came too, and\x01",
            "we were able to get the orbal\x01",
            "net trouble resolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I guess that's one problem down.\x02",
    )

    CloseMessageWindow()

    label("loc_5192")

    TalkEnd(0xFE)
    Return()

    # Function_21_50FC end

    def Function_22_5196(): pass

    label("Function_22_5196")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5292")

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
            "I think she was the Secretary\x01",
            "of Defense's daughter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The "huge tree" that appeared in the\x01",
            "Marshlands is indeed concerning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_534B")

    label("loc_5292")


    ChrTalk(
        0xFE,
        (
            "It looked like the Secretary of Defense's \x01",
            "daughter entered the elevator to the\x01",
            "roof a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The "huge tree" that appeared in the\x01",
            "Marshlands is indeed concerning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_534B")

    Jump("loc_570F")

    label("loc_5350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_535E")
    Jump("loc_570F")

    label("loc_535E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_536C")
    Jump("loc_570F")

    label("loc_536C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_53FE")

    ChrTalk(
        0xFE,
        (
            "The Empire, of course, are the ones\x01",
            "backing the "Red Constellation"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm. That's something we absolutely can't forgive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_53FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5453")

    ChrTalk(
        0xFE,
        (
            "The "Red Constellation"... \x01",
            "It seems they're not your usual guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_5453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_END)), "loc_54C3")

    ChrTalk(
        0xFE,
        "Good job, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're going upstairs, please\x01",
            "use the elevators by the entrance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_54C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_554A")

    ChrTalk(
        0xFE,
        "Hmm. Rainy weather today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, according to the forecast on the\x01",
            "orbal network, it'll be sunny this afternoon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_554A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_55CC")

    ChrTalk(
        0xFE,
        (
            "Hmm. Train accidents\x01",
            "are rare in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A derailment must've\x01",
            "cost so much... What\x01",
            "happened, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_55CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5668")

    ChrTalk(
        0xFE,
        (
            "No matter what you say about Orchis\x01",
            "Tower, this open airspace is amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me, I think it's a luxuriously\x01",
            "constructed building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_5668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5706")

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
            "Because they hardly shake at all, \x01",
            "you can hardly realize that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570F")

    label("loc_5706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_570F")

    label("loc_570F")

    TalkEnd(0xFE)
    Return()

    # Function_22_5196 end

    def Function_23_5713(): pass

    label("Function_23_5713")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wow, amazing... So\x01",
            "this is the Orchis\x01",
            "Tower entrance, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I almost feel like we're time travelers\x01",
            "from a science fiction novel.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_5713 end

    def Function_24_57A5(): pass

    label("Function_24_57A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5813")

    ChrTalk(
        0xFE,
        (
            "I heard from the\x01",
            "staff. They said there\x01",
            "was a derailment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What could the cause be?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5881")

    label("loc_5813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5881")

    ChrTalk(
        0xFE,
        (
            "It's my first time here, but\x01",
            "this really is an amazing room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I feel out of place, somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_5881")

    TalkEnd(0xFE)
    Return()

    # Function_24_57A5 end

    def Function_25_5885(): pass

    label("Function_25_5885")

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
            "The disturbance over the independence proposal\x01",
            "aside, I might want to move to Crossbell someday.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_5885 end

    def Function_26_594E(): pass

    label("Function_26_594E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm. It seems City Hall is a bit in\x01",
            "confusion due to the attack on Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll return home immediately\x01",
            "after finishing my business here...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_594E end

    def Function_27_59F2(): pass

    label("Function_27_59F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B75")

    ChrTalk(
        0xFE,
        (
            "I heard both the President, who was also\x01",
            "the IBC President, and the Acting President,\x01",
            "his daughter, have disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This will have a large impact on stock prices \x01",
            "going forward... IBC will probably lose its position \x01",
            "as the biggest company on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to watch how things go for awhile,\x01",
            "until the next IBC President is chosen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5C5F")

    label("loc_5B75")


    ChrTalk(
        0xFE,
        (
            "This will have a large impact on stock prices \x01",
            "going forward... IBC will probably lose its position \x01",
            "as the biggest company on the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to watch how things go for awhile,\x01",
            "until the next IBC President is chosen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C5F")

    Jump("loc_5D96")

    label("loc_5C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5C72")
    Jump("loc_5D96")

    label("loc_5C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D96")

    ChrTalk(
        0xFE,
        (
            "I can't believe they've been\x01",
            "backing up customer data at\x01",
            "Orchis Tower for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's IBC for you... They have\x01",
            "great crisis management abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems their achievement of having\x01",
            "supported the continent economy over\x01",
            "many years is not mere talk at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D96")

    TalkEnd(0xFE)
    Return()

    # Function_27_59F2 end

    def Function_28_5D9A(): pass

    label("Function_28_5D9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DAF")
    Call(0, 29)
    Jump("loc_5E55")

    label("loc_5DAF")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "...As punishment for worrying me, I'm cutting\x01",
            "your pocket money for next month by half.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        "P-Please, spare me that...!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)

    label("loc_5E55")

    TalkEnd(0xFE)
    Return()

    # Function_28_5D9A end

    def Function_29_5E59(): pass

    label("Function_29_5E59")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x11,
        (
            "Goodness. People like you\x01",
            "make me worry far too much.\x02",
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
            "As the police Vice Chief,\x01",
            "there're time when I\x01",
            "have to stand up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Isn't that what you\x01",
            "should always do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Because you suddenly do things you're not use to,\x01",
            "you get involved in situations like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...S-Sorry.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5FCC")

    ChrTalk(
        0x101,
        "#00012F(S-She's harsh as always...)\x02",
    )

    CloseMessageWindow()

    label("loc_5FCC")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_29_5E59 end

    def Function_30_5FDD(): pass

    label("Function_30_5FDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF2")
    Call(0, 31)
    Jump("loc_6042")

    label("loc_5FF2")


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

    label("loc_6042")

    TalkEnd(0xFE)
    Return()

    # Function_30_5FDD end

    def Function_31_6046(): pass

    label("Function_31_6046")

    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0x10,
        (
            "Alright, let's start the orbal \x01",
            "net check right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "With the monsters wandering around at the time of the blue mist,\x01",
            "it was getting harder to establish communication links.\x01",
            "It may have affected the system too.\x02",
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
            "Then, first up is a function\x01",
            "check of the tower terminals.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_31_6046 end

    def Function_32_618F(): pass

    label("Function_32_618F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_68BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65B6")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Tio... You're heading to\x01",
            "that "huge tree", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything were to happen to you, Tio...\x01",
            "When I think that, I get torn apart inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F...Chief, you don't need to──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ah, that's right! \x01",
            "How about I take an orbal\x01",
            "staff and accompany you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand how to operate an\x01",
            "orbal staff, and in battle I could\x01",
            "support you with support Crafts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, yes, that would be great! \x01",
            "Now that that's decided, let's prepare imm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211FToo annoying, so no thanks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63C2")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_63C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E8")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_63E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_640E")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_640E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6434")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6434")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F(...They're the same as always.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F...Chief, please\x01",
            "don't worry too much.\x02\x03",
            "#00202FI will return all in one piece\x01",
            "with everyone and KeA.\x02\x03",
            "And in the end, Chief, your role is here,\x01",
            "in this city in chaos.\x02",
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
            "...That's right, \x01",
            "it's as you says. I'll\x01",
            "focus on my work here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In return, promise me that...\x01",
            "You'll definitely return safely!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 3)
    Jump("loc_68B8")

    label("loc_65B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F5")

    ChrTalk(
        0xFE,
        (
            "That aside... The "Society"'s\x01",
            "Doctor and that white doll\x01",
            "already left, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FYes... To be honest, I never\x01",
            "want to see him again.\x02\x03",
            "#00211FCompared to him, you are a\x01",
            "thousand times better, Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "T-Tio! (*moved to tears*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(It's weird that he's so happy after\x01",
            "being compared to Dr. Novartis...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But "Aions", huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F...Chief?\x01",
            "What's wrong?\x02",
        )
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
            "(It seems to have the same root word as\x01",
            "the "Aeon System" we developed, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(...It's a coincidence, right?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_68B8")

    label("loc_67F5")


    ChrTalk(
        0xFE,
        (
            "I'll wait here for\x01",
            "you all to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd really like to go with\x01",
            "you, but... Tio rejected it,\x01",
            "so I've got no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In return, promise me that...\x01",
            "You'll definitely return safely!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B8")

    Jump("loc_6B9D")

    label("loc_68BD")

    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B05")

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
            "...Aaah, it's all so sudden\x01",
            "that now I've become worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think Tio would be deployed\x01",
            "in such a mysterious place...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt's to bring those\x01",
            "Bracers back home safely.\x02\x03",
            "Please wait here and\x01",
            "don't worry too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tio... You've really\x01",
            "become a fine person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And you were so small when you\x01",
            "first came to the Foundation...\x01",
            "Ooh, now I'm crying for some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F...How annoying.\x01",
            "Please stop crying\x01",
            "in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_6B9D")

    label("loc_6B05")


    ChrTalk(
        0xFE,
        (
            "I can't help but worry,\x01",
            "sending Tio into a weird\x01",
            "place like that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've become a fine person too, Tio.\x01",
            "I'm sure you'll be all right!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9D")

    TalkEnd(0xFE)
    Return()

    # Function_32_618F end

    def Function_33_6BA1(): pass

    label("Function_33_6BA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF5")

    ChrTalk(
        0x22,
        (
            "#02302FOh yeah, guys...\x01",
            "You have a "Pom!"\x01",
            "account, right?\x02\x03",
            "#02304FHehe. Since I'm here, I think I'll gift\x01",
            "you with the great Jona's account.\x02\x03",
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
            ""Jona's Account"\x07\x00",
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_6FE7")

    label("loc_6CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F64")

    ChrTalk(
        0x22,
        (
            "#02306FWalking all over the place\x01",
            "in this rain sure is tiring.\x02\x03",
            "#02300FBefore going back to the Foundation's branch,\x01",
            "I'll have to laze around to my heart's content, eh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHey now... There's an elevator\x01",
            "going up to the roof, so you weren't\x01",
            "doing that much exercise, right?\x02\x03",
            "#00001FGetting insufficient exercise isn't good.\x02",
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
            "#02310FW-What's that...\x01",
            "That syndrome...\x02\x03",
            "#02306FHmph, whatever... If you're\x01",
            "going to the Marshlands,\x01",
            "you'd best get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we will. \x01",
            "Thanks for your help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_6FE7")

    label("loc_6F64")


    ChrTalk(
        0x22,
        (
            "#02303FAfter I'll have lazed around to\x01",
            "my heart's content, I'll go back.\x02\x03",
            "#02301FYou guys should get\x01",
            "going to the Marshlands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FE7")

    TalkEnd(0xFE)
    Return()

    # Function_33_6BA1 end

    def Function_34_6FEB(): pass

    label("Function_34_6FEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D1")

    ChrTalk(
        0x20,
        (
            "#02100FAh, Lloyd and friends.\x01",
            "You guys look busy as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAre you all here for\x01",
            "conference coverage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02109FVery perceptive. We're collecting material\x01",
            "regarding the newly voted bill.\x02\x03",
            "While I'm at it, I plan to ask\x01",
            "a bunch of congressmen their\x01",
            "opinions on state independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see, I feel like you are in the right\x01",
            "place to get society material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#02106FYes, exactly.\x02\x03",
            "The political sphere is\x01",
            "boring these days due\x01",
            "to lack of scandal.\x02\x03",
            "#02102FHmm. I wonder where\x01",
            "I can find some good\x01",
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
        "#00006FSo that's what you're worried about, huh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 7)
    Jump("loc_745F")

    label("loc_72D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738F")

    ChrTalk(
        0x20,
        (
            "#02106FDon't misunderstand. The lack of\x01",
            "scandal is a good thing. But, there\x01",
            "hasn't been much gossip lately.\x02\x03",
            "#02102FHmm. I wonder where I can\x01",
            "find some good material.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7442")

    label("loc_738F")


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

    label("loc_7442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_745F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_745F")
    ClearScenarioFlags(0x0, 5)

    label("loc_745F")

    TalkEnd(0xFE)
    Return()

    # Function_34_6FEB end

    def Function_35_7463(): pass

    label("Function_35_7463")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Senior Grace... I hope she doesn't ask\x01",
            "the congressmen anything weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, acting as her "safety device" is tough.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_7463 end

    def Function_36_74EB(): pass

    label("Function_36_74EB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7745")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759C")

    ChrTalk(
        0x13,
        (
            "#10100FChanging members,\x01",
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
    Jump("loc_7740")

    label("loc_759C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75B0")
    Jump("loc_7740")

    label("loc_75B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7740")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C5")

    ChrTalk(
        0x13,
        (
            "#10100FIt's badly damaged... But it looks like\x01",
            "its various functions are still working.\x02\x03",
            "Once this situation is settled,\x01",
            "I definitely want to repair it.\x02",
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
    Jump("loc_7740")

    label("loc_76C5")


    ChrTalk(
        0x13,
        (
            "#10100FIt look like its functions are still working.\x02\x03",
            "Once this situation is settled,\x01",
            "I definitely want to repair it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7740")

    Jump("loc_74F8")

    label("loc_7745")

    TalkEnd(0xFE)
    Return()

    # Function_36_74EB end

    def Function_37_7749(): pass

    label("Function_37_7749")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7756")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A25")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F5")

    ChrTalk(
        0x14,
        "#10400FHu hu, you're changing members?\x02",
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
    Jump("loc_7A20")

    label("loc_77F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7809")
    Jump("loc_7A20")

    label("loc_7809")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A20")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7956")

    ChrTalk(
        0x14,
        (
            "#10406FA fresh supply of troops no\x01",
            "matter how many are defeated...\x02\x03",
            "Oh boy, they're sure using\x01",
            "a troublesome thing.\x02\x03",
            "#10401FAt this rate, the guys outside\x01",
            "are just going to get exhausted. \x01",
            "Shouldn't we hurry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FYes. Let's hurry and reach "uncle"\x01",
            "and get him to stop this...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7A20")

    label("loc_7956")


    ChrTalk(
        0x14,
        (
            "#10406FA fresh supply of troops no\x01",
            "matter how many are defeated...\x01",
            "Oh boy, what a troublesome opponent.\x02\x03",
            "#10401FAt this rate, the guys outside\x01",
            "are just going to get exhausted. \x01",
            "Shouldn't we hurry?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A20")

    Jump("loc_7756")

    label("loc_7A25")

    TalkEnd(0xFE)
    Return()

    # Function_37_7749 end

    def Function_38_7A29(): pass

    label("Function_38_7A29")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C6D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD0")

    ChrTalk(
        0x15,
        "#10702FYes, let's change members.\x02",
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
    Jump("loc_7C68")

    label("loc_7AD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AE4")
    Jump("loc_7C68")

    label("loc_7AE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C68")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BF6")

    ChrTalk(
        0x15,
        (
            "#10703FThere's no sign of enemies\x01",
            "in this lobby for now, but...\x02\x03",
            "It would be best to\x01",
            "stay on our guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThat's definitely a possibility...\x01",
            "We're counting on you, dear Rixia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#10702FYes, please leave it to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C68")

    label("loc_7BF6")


    ChrTalk(
        0x15,
        (
            "#10703FJust in case, I think\x01",
            "we should be wary\x01",
            "of our surroundings.\x02\x03",
            "#10701FPlease be careful too, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C68")

    Jump("loc_7A36")

    label("loc_7C6D")

    TalkEnd(0xFE)
    Return()

    # Function_38_7A29 end

    def Function_39_7C71(): pass

    label("Function_39_7C71")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E62")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Quit\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D27")

    ChrTalk(
        0x16,
        (
            "#00600FChanging members?\x01",
            "...Just choose already.\x02",
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
    Jump("loc_7E5D")

    label("loc_7D27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D3B")
    Jump("loc_7E5D")

    label("loc_7D3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E1D")

    ChrTalk(
        0x16,
        (
            "#00603FAs planned, two members will\x01",
            "standby and protect the entrance\x01",
            "in case the worst happens.\x02\x03",
            "#00601F...C'mon, quit dawdling.\x01",
            "You guys should get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...Right!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7E5D")

    label("loc_7E1D")


    ChrTalk(
        0x16,
        (
            "#00601F...C'mon, quit dawdling.\x01",
            "You guys should get going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E5D")

    Jump("loc_7C7E")

    label("loc_7E62")

    TalkEnd(0xFE)
    Return()

    # Function_39_7C71 end

    def Function_40_7E66(): pass

    label("Function_40_7E66")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ECC")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator is heading to\x01",
            "another floor and shows\x01",
            "no sign of stopping.\x07\x00\x02",
        )
    )

    Jump("loc_7F67")

    label("loc_7ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F0E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x07\x00\x02",
        )
    )

    Jump("loc_7F67")

    label("loc_7F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F67")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator is heading to\x01",
            "another floor and shows\x01",
            "no sign of stopping.\x07\x00\x02",
        )
    )


    label("loc_7F67")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_40_7E66 end

    def Function_41_7F6F(): pass

    label("Function_41_7F6F")

    Sound(160, 0, 100, 0)
    Return()

    # Function_41_7F6F end

    def Function_42_7F76(): pass

    label("Function_42_7F76")

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

    def lambda_8155():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8155)
    Sleep(200)

    def lambda_8172():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8172)
    Sleep(200)

    def lambda_818F():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_818F)
    Sleep(200)

    def lambda_81AC():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_81AC)
    Sleep(200)

    def lambda_81C9():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_81C9)
    Sleep(200)

    def lambda_81E6():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_81E6)
    Sleep(100)

    def lambda_8203():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8203)
    Sleep(300)

    def lambda_8217():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8217)
    Sleep(200)

    def lambda_822B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_822B)
    Sleep(600)

    def lambda_823F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_823F)
    Sleep(200)

    def lambda_8253():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8253)
    Sleep(300)

    def lambda_8267():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8267)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00002F#11PIncredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PWhat to say, luxurious,\x01",
            "yet high-tech...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PIt feels even more futuristic\x01",
            "than the IBC building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PEvery floor is connected to the\x01",
            "orbal net, if I am not mistaken.\x02\x03",
            "#00200FThere is also a real-time\x01",
            "data link with IBC for\x01",
            "stock price data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PYes. It seems it\x01",
            "was "uncle"'s idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PI see. Only a banker would\x01",
            "think of something like that.\x02",
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
            "#00000F#5PAlright then. \x01",
            "All that's left is to wait\x01",
            "until Mr. Dudley comes.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84C4():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_84C4)
    Sleep(50)

    def lambda_84D4():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_84D4)
    Sleep(50)

    def lambda_84E4():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_84E4)
    Sleep(50)

    def lambda_84F4():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_84F4)
    Sleep(50)

    def lambda_8504():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8504)
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
            "#1KSame day, 12:00 AM──\x02",
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
        "#3454V#30W#11A──So you came.\x02",
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

    def lambda_8764():

        label("loc_8764")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8764")

    QueueWorkItem2(0x101, 2, lambda_8764)
    Sleep(50)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 5000, 0, 6500, 270)

    def lambda_879D():

        label("loc_879D")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_879D")

    QueueWorkItem2(0x102, 2, lambda_879D)
    Sleep(50)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 5000, 0, 7600, 270)

    def lambda_87D0():

        label("loc_87D0")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_87D0")

    QueueWorkItem2(0x103, 2, lambda_87D0)
    Sleep(50)

    def lambda_87E5():

        label("loc_87E5")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_87E5")

    QueueWorkItem2(0x104, 2, lambda_87E5)
    Sleep(50)

    def lambda_87FA():

        label("loc_87FA")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_87FA")

    QueueWorkItem2(0x105, 2, lambda_87FA)
    ClearChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 5000, 0, 8700, 270)

    def lambda_882A():
        OP_95(0xFE, 4500, 0, 8700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_882A)
    WaitChrThread(0x109, 1)

    def lambda_8848():

        label("loc_8848")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_8848")

    QueueWorkItem2(0x109, 2, lambda_8848)
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
        "#11P#00104FThank you for your hard work.\x02",
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
            "It's exactly noon──\x02\x03",
            "The Trade Conference\x01",
            "begins at 13:00.\x02\x03",
            "The heads of state should\x01",
            "arrive in 30 minutes.\x02",
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
        (
            "#11P#00101FAnd, where\x01",
            "are we going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#12P#00606FI wanted to show you around\x01",
            "the venue myself, but...\x02\x03",
            "I'm here to tell you that someone\x01",
            "unexpected will be doing it instead.\x02",
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
            "──Hello, ladies and gentlemen.\x01",
            "Thank you for coming.\x02",
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

    def lambda_8BDA():
        OP_95(0xFE, 7800, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8BDA)

    def lambda_8BF4():

        label("loc_8BF4")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8BF4")

    QueueWorkItem2(0x101, 2, lambda_8BF4)

    def lambda_8C06():

        label("loc_8C06")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8C06")

    QueueWorkItem2(0x102, 2, lambda_8C06)

    def lambda_8C18():

        label("loc_8C18")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8C18")

    QueueWorkItem2(0x103, 2, lambda_8C18)

    def lambda_8C2A():

        label("loc_8C2A")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8C2A")

    QueueWorkItem2(0x104, 2, lambda_8C2A)

    def lambda_8C3C():

        label("loc_8C3C")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8C3C")

    QueueWorkItem2(0x109, 2, lambda_8C3C)

    def lambda_8C4E():

        label("loc_8C4E")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8C4E")

    QueueWorkItem2(0x105, 2, lambda_8C4E)

    def lambda_8C60():

        label("loc_8C60")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_8C60")

    QueueWorkItem2(0x16, 2, lambda_8C60)
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
        "#00105F"Uncle"...!\x02",
    )

    CloseMessageWindow()

    def lambda_8CB2():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8CB2)
    Sleep(1000)
    Fade(500)
    OP_68(4000, 900, 6200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)

    def lambda_8D02():
        OP_96(0xFE, 0x898, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8D02)
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
            "It's been half a month, \x01",
            "Elie and Lloyd.\x02\x03",
            "Wazy and Noｱl...\x02\x03",
            "Oh, and Randy and Tio.\x01",
            "Long time no see.\x02",
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
        "#00309F#5PHa ha, been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00204FIt is nice to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PBut "uncle", why're you here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#5PIt's just before the Trade Conference starts.\x01",
            "Aren't you busy, mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#12P#02804FPreparations have been complete for awhile.\x01",
            "We just have to wait for the VIPs to arrive.\x02\x03",
            "#02800FFor a change of pace, I thought\x01",
            "I'd show you guys around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x16, 500)
    Sleep(150)

    ChrTalk(
        0x23,
        "#02800F#11PDudley, is that all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#6P#00606F*sigh*... If the mayor says so.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x16,
        (
            "#6P#00600F──Everyone, see that you\x01",
            "aren't rude to the mayor.\x02\x03",
            "And once you're done, come to the\x01",
            "security planning room on 34F.\x02",
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
        "#6P#00603FThen, mayor. See you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#02800F#11PYeah, thanks.\x02",
    )

    CloseMessageWindow()

    def lambda_90FA():

        label("loc_90FA")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_90FA")

    QueueWorkItem2(0x101, 2, lambda_90FA)

    def lambda_910C():

        label("loc_910C")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_910C")

    QueueWorkItem2(0x102, 2, lambda_910C)

    def lambda_911E():

        label("loc_911E")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_911E")

    QueueWorkItem2(0x103, 2, lambda_911E)

    def lambda_9130():

        label("loc_9130")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_9130")

    QueueWorkItem2(0x104, 2, lambda_9130)

    def lambda_9142():

        label("loc_9142")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_9142")

    QueueWorkItem2(0x109, 2, lambda_9142)

    def lambda_9154():

        label("loc_9154")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_9154")

    QueueWorkItem2(0x105, 2, lambda_9154)

    def lambda_9166():

        label("loc_9166")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_9166")

    QueueWorkItem2(0x23, 2, lambda_9166)
    OP_92(0x16, 0x0, 0x8FC, 0x1F4)
    OP_68(1000, 900, 2200, 3000)

    def lambda_9196():
        OP_95(0xFE, 0, 0, 2300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9196)
    WaitChrThread(0x16, 1)

    def lambda_91B4():
        OP_95(0xFE, 0, 0, -5000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_91B4)
    Sleep(2000)
    Sound(107, 0, 100, 0)

    def lambda_91D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_91D7)
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
            "#02804FHu hu. He's a capable detective but\x01",
            "a bit inflexible in some respects.\x02\x03",
            "#02800FAlthough with his job,\x01",
            "that might be a virtue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, as the "demon" of Crime Investigations\x01",
            "Section One, he does have his dignity.\x02",
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
            "#6P#02805FOh, I forgot to say the\x01",
            "most important thing...\x02\x03",
            "#02809F──Ladies and gentlemen of the Special\x01",
            "Support Section, welcome to "Orchis Tower"!\x02\x03",
            "Come now, follow me!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9480():

        label("loc_9480")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_9480")

    QueueWorkItem2(0x101, 2, lambda_9480)

    def lambda_9492():

        label("loc_9492")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_9492")

    QueueWorkItem2(0x102, 2, lambda_9492)

    def lambda_94A4():

        label("loc_94A4")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_94A4")

    QueueWorkItem2(0x103, 2, lambda_94A4)

    def lambda_94B6():

        label("loc_94B6")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_94B6")

    QueueWorkItem2(0x104, 2, lambda_94B6)

    def lambda_94C8():

        label("loc_94C8")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_94C8")

    QueueWorkItem2(0x109, 2, lambda_94C8)

    def lambda_94DA():

        label("loc_94DA")

        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_94DA")

    QueueWorkItem2(0x105, 2, lambda_94DA)
    OP_92(0x23, 0x1B58, 0x3E8, 0x1F4)
    OP_68(6500, 1000, 3000, 3000)

    def lambda_950A():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_950A)
    WaitChrThread(0x23, 1)

    def lambda_9528():
        OP_95(0xFE, 12000, 0, 1000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9528)
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
        "#00302F#5PHa ha, same as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FHe is no Miss Mariabell's\x01",
            "father for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00109FW-Well, looks like he's going to show us\x01",
            "around since he's here for the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FYeah. Shall we accept his kind offer?\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9786")
    Jump("loc_978B")

    label("loc_9786")

    OP_29(0x71, 0x4, 0x40)

    label("loc_978B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_979C")
    Jump("loc_97A1")

    label("loc_979C")

    OP_29(0x72, 0x4, 0x40)

    label("loc_97A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97B2")
    Jump("loc_97B7")

    label("loc_97B2")

    OP_29(0x77, 0x4, 0x40)

    label("loc_97B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97C8")
    Jump("loc_97CD")

    label("loc_97C8")

    OP_29(0x79, 0x4, 0x40)

    label("loc_97CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97DE")
    Jump("loc_97E3")

    label("loc_97DE")

    OP_29(0x7A, 0x4, 0x40)

    label("loc_97E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_97F4")
    Jump("loc_97F9")

    label("loc_97F4")

    OP_29(0x7B, 0x4, 0x40)

    label("loc_97F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_980A")
    Jump("loc_980F")

    label("loc_980A")

    OP_29(0x7C, 0x4, 0x40)

    label("loc_980F")

    OP_1B(0x0, 0x0, 0x33)
    EventEnd(0x5)
    Return()

    # Function_42_7F76 end

    def Function_43_9817(): pass

    label("Function_43_9817")


    def lambda_981C():
        OP_95(0xFE, 7000, 0, 1000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_981C)
    WaitChrThread(0x16, 1)

    def lambda_983A():
        OP_95(0xFE, 3500, 0, 4500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_983A)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x0, 0x1F4)
    Return()

    # Function_43_9817 end

    def Function_44_985B(): pass

    label("Function_44_985B")

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
        "#6P#10105FThere's even three elevators...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWow, how luxurious.\x02",
    )

    CloseMessageWindow()

    def lambda_99BF():
        OP_97(0x102, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_99BF)
    Sleep(50)

    def lambda_99DC():
        OP_97(0x101, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_99DC)
    Sleep(50)

    def lambda_99F9():
        OP_97(0x104, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_99F9)
    Sleep(50)

    def lambda_9A16():
        OP_97(0x103, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9A16)
    Sleep(50)

    def lambda_9A33():
        OP_97(0x105, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9A33)
    Sleep(50)

    def lambda_9A50():
        OP_97(0x109, 0x1770, 0x0, 0x4B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9A50)
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
            "#02804F#11PWell, the building IS 40 floors tall.\x02\x03",
            "#02800FIf you include the private\x01",
            "elevators, there're six in all.\x02",
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

    # Function_44_985B end

    def Function_45_9C63(): pass

    label("Function_45_9C63")

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

    # Function_45_9C63 end

    def Function_46_9C97(): pass

    label("Function_46_9C97")


    def lambda_9C9C():
        OP_95(0xFE, 81000, 0, 3300, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C9C)
    WaitChrThread(0xFE, 1)

    def lambda_9CBA():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CBA)
    Sleep(500)

    def lambda_9CD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CD7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_9C97 end

    def Function_47_9CE8(): pass

    label("Function_47_9CE8")

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

    def lambda_9E18():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9E18)
    Sleep(200)

    def lambda_9E35():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9E35)
    Sleep(200)

    def lambda_9E52():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9E52)
    Sleep(200)

    def lambda_9E6F():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9E6F)
    Sleep(200)

    def lambda_9E8C():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9E8C)
    Sleep(200)

    def lambda_9EA9():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9EA9)
    SetCameraDistance(18500, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(100)

    def lambda_9EDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9EDE)
    Sleep(300)

    def lambda_9EF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9EF2)
    Sleep(200)

    def lambda_9F06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F06)
    Sleep(600)

    def lambda_9F1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9F1A)
    Sleep(200)

    def lambda_9F2E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F2E)
    Sleep(300)

    def lambda_9F42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9F42)
    Sound(803, 2, 100, 0)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_9F78():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F78)
    Sleep(50)

    def lambda_9F88():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9F88)
    Sleep(50)

    def lambda_9F98():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F98)
    Sleep(50)

    def lambda_9FA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9FA8)
    Sleep(50)

    def lambda_9FB8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9FB8)

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
            "Hey. Where're you guys?\x02\x03",
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
            "#00004FWe just arrived at\x01",
            "the tower entrance.\x02\x03",
            "#00000FShould we just head up to the roof?\x02",
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
            "Yeah. If you ask the receptionist,\x01",
            "she'll give you an elevator access card.\x02\x03",
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
            "#00002FUnderstood. And thanks for your hard work.\x02",
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
        "#11P#00202FLooks like preparations are done.\x02",
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
            "#00000F#5PYeah. Let's speak to the receptionist for\x01",
            "an access card and then head to the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FIt's raining, so we shouldn't\x01",
            "make them wait too long.\x02",
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

    # Function_47_9CE8 end

    def Function_48_A351(): pass

    label("Function_48_A351")

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
        "#5PAh, you are the Special Support Section, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11PYes. Will you issue us\x01",
            "an access card?\x02",
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
            "#5PPut that card in the elevator\x01",
            "panel and you will be able to go\x01",
            "directly to the 40F top floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt is good for one month and disposable,\x01",
            "so please discard it when you are finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#11PU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112F(That's kind of amazing...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P(Yeah. It's even more advanced\x01",
            "than the IBC building...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302F(The building itself is basically just a\x01",
            "giant mass of the latest tech, right?)\x02",
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

    # Function_48_A351 end

    def Function_49_A6E3(): pass

    label("Function_49_A6E3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A703")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_A703")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A717")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_A717")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A72B")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_A72B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A73F")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_A73F")

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
            "#12P#10104F...It's fine.\x01",
            "All systems are functioning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FI see... We really \x01",
            "relied on her a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#6P...That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI want to repair\x01",
            "it properly later.\x02",
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

    def lambda_AA0D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_AA0D)
    Sleep(30)

    def lambda_AA1D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AA1D)
    Sleep(30)

    def lambda_AA2D():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_AA2D)
    Sleep(30)

    def lambda_AA3D():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA3D)
    Sleep(30)

    def lambda_AA4D():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AA4D)
    Sleep(30)

    def lambda_AA5D():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AA5D)
    Sleep(30)

    def lambda_AA6D():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AA6D)
    Sleep(30)

    def lambda_AA7D():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AA7D)
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
        "#5P#10708F...Looks like it's still going on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401FIt seems like they can generate\x01",
            "an unlimited number of them.\x02",
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
            "#5P#00306FThere's no time.\x01",
            "Let's head for\x01",
            "the elevators.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(
        0x10A,
        (
            "#6P#00603FAs planned, two people\x01",
            "will standby here.\x02\x03",
            "#00600FYou choose, Bannings.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)

    def lambda_AC0B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AC0B)
    Sleep(30)

    def lambda_AC1B():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AC1B)
    Sleep(30)

    def lambda_AC2B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC2B)
    Sleep(30)

    def lambda_AC3B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AC3B)
    Sleep(30)

    def lambda_AC4B():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_AC4B)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x101,
        "#11P#00001FUnderstood.\x02",
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

    # Function_49_A6E3 end

    def Function_50_AD1F(): pass

    label("Function_50_AD1F")

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
            "If not, you can't\x01",
            "use the elevator.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 74460, 0, 1270, 180)
    OP_93(0x1F, 0xB4, 0x0)
    OP_4C(0x1F, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_50_AD1F end

    def Function_51_AD9D(): pass

    label("Function_51_AD9D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE4C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The sounds of intermittent gunfire\x01",
            "can be heard from the plaza.\x02",
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

    label("loc_AE4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEA9")

    ChrTalk(
        0x101,
        (
            "#00001FLet's not keep the mayor waiting\x01",
            "too long. Let's hurry after them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEA9")

    SetChrPos(0x0, -290, 0, -3540, 0)
    EventEnd(0x4)
    Return()

    # Function_51_AD9D end

    def Function_52_AEBD(): pass

    label("Function_52_AEBD")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AECF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B04C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_AF38")
    MenuCmd(1, 0, "Rest in Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AF38")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFC7")

    ChrTalk(
        0x101,
        (
            "#00001F...There's no need to forcefully move it.\x01",
            "Let's repair it after the incident's resolved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B047")

    label("loc_AFC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B03D")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_B000")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_B018")

    label("loc_B000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_B013")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_B018")

    label("loc_B013")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_B018")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B047")

    label("loc_B03D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B047")

    Jump("loc_AECF")

    label("loc_B04C")

    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_52_AEBD end

    SaveToFile()

Try(main)
