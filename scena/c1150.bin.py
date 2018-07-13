from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1150.bin",                # FileName
        "c1150",                    # MapName
        "c1150",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 5000, 1500, 0, 0, 1, 24, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1150",                  # 0
        "Receptionist Rebecca",   # 1
        "Receptionist Fran",      # 2
        "Inspector Donovan",      # 3
        "Detective Raymond",      # 4
        "Detective Dudley",       # 5
        "Detective Emma",         # 6
        "Patrol Officer Kate",    # 7
        "Patrol Officer Frantz",  # 8
        "Vice Chief Pierre",      # 9
        "Yuri",                   # 10
        "Sykes",                  # 11
        "Reggie",                 # 12
        "Section Chief Joe Ridge",# 13
        "State Guard Soldier",    # 14
        "State Guard Soldier",    # 15
        "Policeman",              # 16
        "Policeman",              # 17
        "Chief Sergei",           # 18
        "Chair",                  # 19
        "Chair",                  # 20
        "Chair",                  # 21
        "Chair",                  # 22
        "Chair",                  # 23
        "Chair",                  # 24
        "Chair",                  # 25
        "Chair",                  # 26
        "SE制御",                 # 27
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch30600.itc",                   # 03
        "chr/ch30000.itc",                   # 04
        "chr/ch06400.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch44102.itc",                   # 07
        "chr/ch47500.itc",                   # 08
        "chr/ch23600.itc",                   # 09
        "chr/ch30002.itc",                   # 0A
        "chr/ch30300.itc",                   # 0B
        "chr/ch30200.itc",                   # 0C
        "chr/ch41400.itc",                   # 0D
        "chr/ch41500.itc",                   # 0E
        "chr/ch00900.itc",                   # 0F
    ))

    DeclNpc(4294967196, 0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(4294841917, 0,       19520,   0,    453,  0x0, 0,   2,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 0,   37,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   7,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   9,   0,   255, 255, 0,   35,  255,  0)
    DeclNpc(4294909247, 0,       15899,   90,   389,  0x0, 0,   6,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   43,  255,  0)
    DeclNpc(4294954887, 0,       19770,   180,  389,  0x0, 0,   14,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   4,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(2990,    0,       11810,   270,  389,  0x0, 0,   4,   0,   0,   0,   0,   42,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 56,  -12.699999809265137,   18.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.4350004196167,      0.1428571492433548,    1.0])
    DeclEvent(0x0000, 0, 50,  -8.260000228881836,    10.029999732971191,    -0.5,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.130000114440918,     -2.507499933242798,    0.1428571492433548,    1.0])

    DeclActor(4294967196, 0,       14400,   1100,    4294967196, 1500,    15400,   0x007E, 0,  5,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  17, 0x0000)
    DeclActor(4294957446, 0,       16000,   1000,    4294957446, 1500,    16000,   0x007C, 0,  57, 0x0000)
    DeclActor(4294957446, 0,       13750,   1000,    4294957446, 1500,    13750,   0x007C, 0,  57, 0x0000)

    ChipFrameInfo(1536, 0)                                       # 0

    ScpFunction((
        "Function_0_600",          # 00, 0
        "Function_1_6B8",          # 01, 1
        "Function_2_6E3",          # 02, 2
        "Function_3_736",          # 03, 3
        "Function_4_E7A",          # 04, 4
        "Function_5_F4D",          # 05, 5
        "Function_6_F51",          # 06, 6
        "Function_7_14DE",         # 07, 7
        "Function_8_2DB8",         # 08, 8
        "Function_9_2DC7",         # 09, 9
        "Function_10_4FCC",        # 0A, 10
        "Function_11_50CF",        # 0B, 11
        "Function_12_5F41",        # 0C, 12
        "Function_13_6DD8",        # 0D, 13
        "Function_14_7884",        # 0E, 14
        "Function_15_796C",        # 0F, 15
        "Function_16_7A61",        # 10, 16
        "Function_17_87E0",        # 11, 17
        "Function_18_8933",        # 12, 18
        "Function_19_AC3F",        # 13, 19
        "Function_20_B54E",        # 14, 20
        "Function_21_BC6E",        # 15, 21
        "Function_22_C446",        # 16, 22
        "Function_23_CFF8",        # 17, 23
        "Function_24_D01E",        # 18, 24
        "Function_25_D9F6",        # 19, 25
        "Function_26_E16B",        # 1A, 26
        "Function_27_E4C5",        # 1B, 27
        "Function_28_E98B",        # 1C, 28
        "Function_29_F464",        # 1D, 29
        "Function_30_FB40",        # 1E, 30
        "Function_31_10F20",       # 1F, 31
        "Function_32_11237",       # 20, 32
        "Function_33_11345",       # 21, 33
        "Function_34_1145B",       # 22, 34
        "Function_35_115AF",       # 23, 35
        "Function_36_116D0",       # 24, 36
        "Function_37_11A75",       # 25, 37
        "Function_38_11DD3",       # 26, 38
        "Function_39_120A7",       # 27, 39
        "Function_40_1287E",       # 28, 40
        "Function_41_1297C",       # 29, 41
        "Function_42_12B55",       # 2A, 42
        "Function_43_12D2F",       # 2B, 43
        "Function_44_12E9F",       # 2C, 44
        "Function_45_133C3",       # 2D, 45
        "Function_46_14C94",       # 2E, 46
        "Function_47_15306",       # 2F, 47
        "Function_48_16582",       # 30, 48
        "Function_49_16595",       # 31, 49
        "Function_50_16E23",       # 32, 50
        "Function_51_17C34",       # 33, 51
        "Function_52_18978",       # 34, 52
        "Function_53_19605",       # 35, 53
        "Function_54_19760",       # 36, 54
        "Function_55_1985D",       # 37, 55
        "Function_56_19C0E",       # 38, 56
        "Function_57_19D6D",       # 39, 57
    ))


    def Function_0_600(): pass

    label("Function_0_600")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_640"),
        (1, "loc_64C"),
        (2, "loc_658"),
        (3, "loc_664"),
        (4, "loc_670"),
        (5, "loc_67C"),
        (6, "loc_688"),
        (SWITCH_DEFAULT, "loc_694"),
    )


    label("loc_640")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_64C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_658")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_664")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_670")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_67C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_688")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_694")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_6A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6A0")

    label("loc_6B7")

    Return()

    # Function_0_600 end

    def Function_1_6B8(): pass

    label("Function_1_6B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E2")
    OP_94(0xFE, 0xFFFF8508, 0x24CC, 0xFFFF93C2, 0x288C, 0x3E8)
    Sleep(300)
    Jump("Function_1_6B8")

    label("loc_6E2")

    Return()

    # Function_1_6B8 end

    def Function_2_6E3(): pass

    label("Function_2_6E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_735")
    OP_95(0x10, -57300, 0, 20000, 2000, 0x0)
    Sleep(500)
    OP_93(0x10, 0xB4, 0x2EE)
    Sleep(500)
    OP_95(0x10, -57300, 0, 16000, 2000, 0x0)
    Sleep(500)
    OP_93(0x10, 0x0, 0x2EE)
    Sleep(500)
    Jump("Function_2_6E3")

    label("loc_735")

    Return()

    # Function_2_6E3 end

    def Function_3_736(): pass

    label("Function_3_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_78B")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, -57400, 0, 16210, 0)
    SetChrPos(0x18, -57420, 0, 18000, 180)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7AD")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_838")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -69670, 30, 19510, 315)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -70670, 0, 20710, 135)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -57400, 0, 16210, 0)
    ClearChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -57420, 0, 18000, 180)
    ClearChrFlags(0xE, 0x40)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_B69")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_85A")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B69")

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8F2")
    SetChrPos(0xA, -121660, 0, 18190, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -56800, 0, 16000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -58000, 30, 15910, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -58210, 0, 18000, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xF, -56700, 0, 18000, 180)
    Jump("loc_B69")

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_922")
    SetChrPos(0xA, -12180, 0, 7890, 270)
    SetChrPos(0xB, -13680, 0, 7890, 90)
    Jump("loc_B69")

    label("loc_922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_990")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57400, 0, 16000, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -56700, 0, 18000, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -58210, 0, 18000, 180)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x18, 0x10)
    Jump("loc_B69")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9EA")
    SetChrPos(0xA, -121550, 0, 18180, 90)
    SetChrPos(0xB, -125380, 0, 19520, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E5")
    SetChrFlags(0xD, 0x10)

    label("loc_9E5")

    Jump("loc_B69")

    label("loc_9EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A24")
    SetChrPos(0xA, -57400, 0, 16210, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -57420, 0, 18000, 180)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A3C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B69")

    label("loc_A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A9B")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -57400, 0, 16210, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -57420, 0, 18000, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -10590, 0, 15740, 90)
    SetChrFlags(0xB, 0x80)
    Jump("loc_B69")

    label("loc_A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ACE")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B28")
    SetChrPos(0xA, -57400, 0, 16210, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57420, 0, 18000, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B12")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_B12")

    SetChrPos(0xB, -125380, 0, 19520, 0)
    Jump("loc_B69")

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B69")
    SetChrPos(0xA, -11040, 0, 13810, 225)
    SetChrPos(0xB, -12290, 0, 12530, 45)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -10590, 0, 15740, 90)

    label("loc_B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B84")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB5")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -11040, 0, 13810, 90)

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE5")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -57300, 0, 18750, 270)

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CEA")
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124800, 0, 18080, 135)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x40)

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_DE3")
    SetChrChipByIndex(0x11, 0x7)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    BeginChrThread(0x12, 0, 0, 0)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    BeginChrThread(0x14, 0, 0, 0)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124800, 0, 18080, 135)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    ClearChrFlags(0xF, 0x40)

    label("loc_DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_DF7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 45)
    Jump("loc_E50")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_E0B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 49)
    Jump("loc_E50")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_E1F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 51)
    Jump("loc_E50")

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_E33")
    ClearScenarioFlags(0x22, 3)
    Event(0, 55)
    Jump("loc_E50")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_E50")
    ClearScenarioFlags(0x22, 4)
    SetChrPos(0x0, -12810, 0, 14970, 180)

    label("loc_E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E79")
    SetMapFlags(0x10000000)
    Event(0, 46)

    label("loc_E79")

    Return()

    # Function_3_736 end

    def Function_4_E7A(): pass

    label("Function_4_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBF")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EFA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_EFA")

    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F28")
    OP_65(0x1, 0x1)

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3A")
    OP_65(0x0, 0x1)

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4C")
    OP_65(0x0, 0x1)

    label("loc_F4C")

    Return()

    # Function_4_E7A end

    def Function_5_F4D(): pass

    label("Function_5_F4D")

    Call(0, 6)
    Return()

    # Function_5_F4D end

    def Function_6_F51(): pass

    label("Function_6_F51")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_1319")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1319")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "My, everyone, what\x01",
            "you have with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could it be a\x01",
            ""fragment"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUhhm, you mean this?\x02\x03",
            "#00000FWe thought it was something\x01",
            "good when we got it, but until now\x01",
            "we didn't figure a way to use it...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the fragment to Rebecca.\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "My, as I thought...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is a Quartz fragment that can\x01",
            "repair the damaged Memory Quartzes.\x01",
            "The people from forensics were looking for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have that, it should\x01",
            "be possible to analyze a part\x01",
            "of the Cult's terminals data.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B1")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DA")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1203")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_1203")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1229")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_1229")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FT-Then...\x01",
            "We can be able to read the parts that\x01",
            "were concealed by Joachim Gｸnther...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, it seems only\x01",
            "a part, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think we will have immediate\x01",
            "results, so, can I send this\x01",
            ""fragment" to forensics?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 9)
    TalkEnd(0x8)
    Return()

    label("loc_1319")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133C")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_133C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1351")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_1351")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_135B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CD")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x1, 3)
    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_13E3")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                             # 0
            "Show Combat Notebook\x01",             # 1
            "Check Cult's Terminals Data\x01",      # 2
            "Hand Over Fragments\x01",              # 3
            "Quit\x01",                             # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_1443")

    label("loc_13E3")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                             # 0
            "Show Combat Notebook\x01",             # 1
            "Check Cult's Terminals Data\x01",      # 2
            "Quit\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1443")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1443")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1471")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    Jump("loc_14C8")

    label("loc_1471")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1495")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Call(0, 16)
    Jump("loc_14C8")

    label("loc_1495")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B6")
    Call(0, 10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14C8")

    label("loc_14B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C8")
    Call(0, 9)

    label("loc_14C8")

    Jump("loc_135B")

    label("loc_14CD")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    Return()

    # Function_6_F51 end

    def Function_7_14DE(): pass

    label("Function_7_14DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E8")

    ChrTalk(
        0x8,
        "Everyone...thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGood morning, Miss Rebecca.\x01",
            "You have returned to HQ, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, Miss Kate, Mr. Raymond\x01",
            "and the others too have returned\x01",
            "to their normal duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since it was decided to be left out\x01",
            "from the State Guard chain of command...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At present, we are dealing in all\x01",
            "directions to cope with the situation\x01",
            "by rearranging all our resources.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHm, that's nice to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, it is thanks to you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Oh, right, could you\x01",
            "tell this to Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tell her to leave the reception to me and\x01",
            "that I will devote myself to help everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A0")

    ChrTalk(
        0x109,
        (
            "#10102FUh uh, understood.\x01",
            "I'll properly tell her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DA")

    label("loc_17A0")


    ChrTalk(
        0x103,
        (
            "#00202FHu hu, understood.\x01",
            "We will properly tell her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(
        0x10A,
        (
            "#00600FRebecca, please take \x01",
            "care of headquarters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1855")

    label("loc_1827")


    ChrTalk(
        0x101,
        (
            "#00000FMiss Rebecca, we\x01",
            "leave HQ to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1855")


    ChrTalk(
        0x8,
        (
            "Yes. I will make efforts even\x01",
            "for the citizens' sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alert situation is going to continue, but...\x01",
            "Please, do your best too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 3)
    Jump("loc_1A6C")

    label("loc_18E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CF")

    ChrTalk(
        0x8,
        (
            "Police HQ is dealing in all directions\x01",
            "to cope with the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please tell Fran I will devote\x01",
            "myself to help everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alert situation is going to continue, but...\x01",
            "Please, do your best too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1A6C")

    label("loc_19CF")


    ChrTalk(
        0x8,
        (
            "Police HQ is working with all its\x01",
            "resources to cope with the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alert situation is going to continue, but...\x01",
            "Please, do your best too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6C")

    Jump("loc_2DB7")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A7F")
    Jump("loc_2DB7")

    label("loc_1A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B90")

    ChrTalk(
        0x8,
        (
            "This morning, all of a sudden some\x01",
            "men from the State Guard entered\x01",
            "HQ and ordered to be on standby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was so sudden that I\x01",
            "was in confusion about\x01",
            "what to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At any rate, for now I can only\x01",
            "wait for the meeting to finish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1C1C")

    label("loc_1B90")


    ChrTalk(
        0x8,
        (
            "It was so sudden that I\x01",
            "was in confusion about\x01",
            "what to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At any rate, for now I can only\x01",
            "wait for the meeting to finish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1C")

    Jump("loc_2DB7")

    label("loc_1C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C2F")
    Jump("loc_2DB7")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D03")

    ChrTalk(
        0x8,
        (
            "Today too Mr. Dudley had an\x01",
            "impregnable facial expression...\x01",
            "It looks like the situation is less than stellar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would like a different solution from\x01",
            "a war at all costs was chosen, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB7")

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E4F")

    ChrTalk(
        0x8,
        (
            "Because of the CGF people, the\x01",
            "transcontinental railroad service could\x01",
            "be perfectly resumed from this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since they somehow managed to make it in\x01",
            "time for the first train, it all ended without\x01",
            "doing special changes to the service schedule...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel sure that this too was\x01",
            "due to the CGF tenacity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB7")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1F3A")

    ChrTalk(
        0x8,
        (
            "Due to the train accident\x01",
            "we immediately received many\x01",
            "inquiries from all quarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have already begun dealing\x01",
            "with transferring passengers, but...\x01",
            "If this situation continues, it will really be troublesome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB7")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2017")

    ChrTalk(
        0x8,
        (
            ""Pleroma Grass"...\x01",
            "A Gnosis basic ingredient that was\x01",
            "present in the Cult database, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For such a thing to suddenly be\x01",
            "spotted in every place in Crossbell...\x01",
            "I wonder if something is going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB7")

    label("loc_2017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_21A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2146")

    ChrTalk(
        0x8,
        (
            "Everyone, due to your next mission, it\x01",
            "appears you will do a joint with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, who could have thought that the\x01",
            "day would come to carry out a request\x01",
            "shoulder-to-shoulder with the Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, you really, always,\x01",
            "impress in a good sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_219E")

    label("loc_2146")


    ChrTalk(
        0x8,
        (
            "Like Fran says, I think that\x01",
            "Cryptids are tough opponents...\x01",
            "Please, do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219E")

    Jump("loc_2DB7")

    label("loc_21A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_233C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A4")

    ChrTalk(
        0x8,
        (
            "Chief Sergei is already waiting for you\x01",
            "at security countermeasures HQ on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Conference opening hour\x01",
            "is drawing near, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all, the first hurdle\x01",
            "is for the VIPs to safely\x01",
            "enter inside the venue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2337")

    label("loc_22A4")


    ChrTalk(
        0x8,
        (
            "The Conference opening hour\x01",
            "is drawing near, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all, the first hurdle\x01",
            "is for the VIPs to safely\x01",
            "enter inside the venue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2337")

    Jump("loc_2DB7")

    label("loc_233C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23EE")

    ChrTalk(
        0x8,
        (
            "Both Fran and I went to look at\x01",
            "Orchis Tower on our breaks...\x01",
            "That presence was overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Truly an appropriate building to\x01",
            "be Crossbell new landmark.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB7")

    label("loc_23EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272A")

    ChrTalk(
        0x8,
        (
            "The current security system\x01",
            "is build upon an unprecedented\x01",
            "partnership of Police and CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was thought to be impossible\x01",
            "to build this much of a system\x01",
            "with traditional organizations, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The biggest cause of that could be\x01",
            "said to be Commander Sonya who\x01",
            "has significant knowledge of the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Uuhhm, Miss Rebecca\x01",
            "is really a beauty...)\x02\x03",
            "#00309F(Similar glasses, but the impression\x01",
            "is largely different from Commander\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(*sigh*, senior Randy...\x01",
            "I'll tell the Commander, you know?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#00305F(N-No, that just now\x01",
            "was a figure of speech...)\x02\x03",
            "#00309F(Maaan, Miss Rebecca is a beauty but she  \x01",
            "can't hold a candle to Commander Sonya...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 7)
    Jump("loc_27F9")

    label("loc_272A")


    ChrTalk(
        0x8,
        (
            "The current security system\x01",
            "is build upon an unprecedented\x01",
            "partnership of Police and CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The biggest cause of that could be\x01",
            "said to be Commander Sonya who\x01",
            "has significant knowledge of the police.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F9")

    Jump("loc_2DB7")

    label("loc_27FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A3")

    ChrTalk(
        0x8,
        (
            "With the previous director dismissal,\x01",
            "after Mayor Dieter assumption of office\x01",
            "the police system too greatly changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are very many new difficulties,\x01",
            "but I realize we are making progresses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hereafter, I think that expectations\x01",
            "from you all are going to become greater and\x01",
            "greater, but by all means, please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We too will support you with\x01",
            "everything we have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2A60")

    label("loc_29A3")


    ChrTalk(
        0x8,
        (
            "Hereafter, I think that expectations\x01",
            "from you all are going to become greater and\x01",
            "greater, but by all means, please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We too will support you with\x01",
            "everything we have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A60")

    Jump("loc_2DB7")

    label("loc_2A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2DB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_END)), "loc_2CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C21")

    ChrTalk(
        0x8,
        (
            "There is an increasing trend of reports\x01",
            "about new type monsters too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What we want is as much information as possible to grasp\x01",
            "their actual conditions and for security measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, I am counting on you.\x01",
            "You will be gradually awarded some\x01",
            "compensation as it has been until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition, here you can check\x01",
            "the Cult terminals data too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you want to check,\x01",
            "please ask me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2CE6")

    label("loc_2C21")


    ChrTalk(
        0x8,
        (
            "Regarding the Combat Notebook reports,\x01",
            "you will be awarded some compensation.\x01",
            "Please, I am counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition, in case you want to\x01",
            "check the Cult terminals data,\x01",
            "please ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE6")

    Jump("loc_2DB7")

    label("loc_2CEB")


    ChrTalk(
        0x8,
        (
            "Uh uh, nevertheless,\x01",
            "a collaboration request from Section One...\x01",
            "Everyone, you have made a name for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As one of the persons who\x01",
            "has seen the SSS activities,\x01",
            "somehow I am deeply moved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB7")

    Return()

    # Function_7_14DE end

    def Function_8_2DB8(): pass

    label("Function_8_2DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_2DC6")
    SetScenarioFlags(0x1, 3)

    label("loc_2DC6")

    Return()

    # Function_8_2DB8 end

    def Function_9_2DC7(): pass

    label("Function_9_2DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_2E54")

    ChrTalk(
        0x8,
        (
            "My, you have brought\x01",
            "me a "fragment".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order to analyze the Cult\x01",
            "terminals data, do you mind\x01",
            "if I send it to forensics?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E54")


    ChrTalk(
        0x101,
        "#00000FNo, please do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Then, please wait a moment.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_2EA1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EAE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_4EA9")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F31")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2F31")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F95")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2F95")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF7")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2FF7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3059")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3059")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39CE")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" page 4 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information Terminal Data:\x01",
            ""About The Cult" completely decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PAll data from the information terminal No. 1\x01",
            "has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PDo you want to check it immediately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FYes, please.\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 11)

    ChrTalk(
        0x8,
        (
            "#5P...About this data...\x01",
            "It appears it is an entry\x01",
            "regarding the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA creed that denies the Goddess...\x01",
            "It is really unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes...however, it\x01",
            "fits in with Joachim\x01",
            "Gｸnther's testimony.\x02\x03",
            "#00001FAlso, this word, "D"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0x103,
        (
            "#12P#00203FIt's the word indicating the "True God" they\x01",
            "believed in instead of the Goddess, right?\x02\x03",
            "#00201FWe have already ascertained that\x01",
            "the "G" in the D∴G Cult name\x01",
            "stands for true wisdom, "Gnosis"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3452")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHm, now it seems we can say that we finally\x01",
            "confirmed even the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B4")

    label("loc_3452")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHm, now it seems we can say that we finally\x01",
            "confirmed even the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B4")

    Jump("loc_35E2")

    label("loc_34B9")


    ChrTalk(
        0x103,
        (
            "#12P#00200FIt's the word indicating the "True God" they\x01",
            "believed in instead of the Goddess, right?\x02\x03",
            "#00201FWe have already ascertained that\x01",
            "the "G" in the D∴G Cult name\x01",
            "stands for true wisdom, "Gnosis"...\x02\x03",
            "With this, it seems we can say that we finally\x01",
            "confirmed even the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E2")


    ChrTalk(
        0x102,
        (
            "#12P#00108FBut...I'm sure that Professor\x01",
            "Joachim referred to KeA as the\x01",
            "person who would become a "God".\x02\x03",
            "Then, "D" could be also a\x01",
            "word to indicate KeA, but...\x01\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3706")

    ChrTalk(
        0x109,
        (
            "#12P#10101FJoachim Gｸnther...\x01",
            "How much did he know...\x02\x03",
            "...We can't figure it out with just this yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FE")

    label("loc_3706")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3799")

    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F...We can't figure it out with just this yet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37FE")

    label("loc_3799")


    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...\x02\x03",
            "We can't get it with just this yet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FE")


    ChrTalk(
        0x101,
        (
            "#12P#00001FIt also seems that even Mr.\x01",
            "Ernest didn't hear the whole\x01",
            "story from Joachim...\x02\x03",
            "#00003FIf we could have arrested him...\x01",
            "It keeps make you think like that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3923")

    ChrTalk(
        0x8,
        (
            "#5P...In any case, if we decrypt\x01",
            "the data at this rate, I think we\x01",
            "may understand many things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3923")


    ChrTalk(
        0x8,
        (
            "#5P...In any case, if we decrypt\x01",
            "the data at this rate, I think we\x01",
            "may understand many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_39CE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A30")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3A30")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9C")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3A9C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_440A")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" page 4 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information Terminal Data:\x01",
            ""About Gnosis" completely decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PAll data from the information terminal No. 2\x01",
            "has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PDo you want to check it immediately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FYes, please.\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 12)

    ChrTalk(
        0x8,
        (
            "#5P...About this data...\x01",
            "It appears there are recorded\x01",
            "details about that "Gnosis".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA drug that has the effect to increase\x01",
            "physical abilities, responsiveness and\x01",
            "furthermore, it draws out latent abilities too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PEven the phenomenon called "Demonize"...\x01",
            "It's a drug full of mysteries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FBecause the plant called "Pleroma Grass"\x01",
            "used as raw ingredient grows in colonies\x01",
            "in the Marshlands...\x02\x03",
            "It seems certain that Joachim\x01",
            "was going to collect supplies\x01",
            "in that place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F15")

    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data there's a\x01",
            "passage saying that Gnosis...\x02\x03",
            "Is a drug needed to revive their\x01",
            "so-called True God..."D", I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FFrankly, what I'm hearing\x01",
            "is an absurd story...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD8")

    label("loc_3F15")


    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data there's a\x01",
            "passage saying that Gnosis\x02\x03",
            "is a drug needed to revive their\x01",
            "so-called True God..."D", I mean.\x02\x03",
            "#00108FFrankly, what I'm hearing\x01",
            "is an absurd story...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD8")


    ChrTalk(
        0x103,
        (
            "#12P#00201FEven so, the Cult continued to\x01",
            "research Gnosis with "rituals"\x01",
            "over the span of even 500 years...\x02\x03",
            "#00203F...I was fortunate to be saved\x01",
            "by Mr. Guy, but there have been\x01",
            "quite many victims until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FAnd he phrased that as\x01",
            ""some sacrifices"...\x02\x03",
            "What a really pathetic lot.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4164")

    ChrTalk(
        0x105,
        (
            "#12P#10403F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41A3")

    label("loc_4164")


    ChrTalk(
        0x105,
        (
            "#12P#10303F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41A3")


    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah...although the Cult has disappeared,\x01",
            "maybe we still need to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4292")

    label("loc_4205")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02\x03",
            "#00001FAlthough the Cult has disappeared,\x01",
            "maybe we still need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4292")


    ChrTalk(
        0x102,
        (
            "#12P#00101FYes...really.\x02\x03",
            "Not only Gnosis, we police\x01",
            "must properly supervise\x01",
            "drugs like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4367")

    ChrTalk(
        0x8,
        "#5PYes, I agree too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...For the present, I think\x01",
            "this is all regarding Gnosis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_440A")

    label("loc_4367")


    ChrTalk(
        0x8,
        "#5PYes, I agree too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...For the present, I think\x01",
            "this is all regarding Gnosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" too.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_440A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4476")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4476")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA9")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal Data:\x01",
            ""About The Divine Child" completely decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    SetScenarioFlags(0x12A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PAll data from the information terminal No. 3\x01",
            "has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PDo you want to check it immediately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FYes, please.\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 13)

    ChrTalk(
        0x8,
        (
            "#5PThis content...\x01",
            "Is it about KeA who you were\x01",
            "sheltering at the SSS...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FKeA was created by the\x01",
            "Crois Clan 500 years ago...\x01",
            "She was presented to the Cult as a religious figure.\x02\x03",
            "As the "Divine Child", their God's vessel,\x01",
            "who keeps slumbering in a "Cradle"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...Even the Cult members didn't\x01",
            "know anything about the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWithout even knowing that they were manipulated\x01",
            "in the shadows for the Crois Clan true goal, they\x01",
            "kept looking for a fantasy called "True God"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4888")

    ChrTalk(
        0x106,
        "#12P#10708F...In a certain sense, they're pitiful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4913")

    label("loc_4888")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D5")

    ChrTalk(
        0x109,
        "#12P#10108F...In a certain sense, they're pitiful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4913")

    label("loc_48D5")


    ChrTalk(
        0x105,
        "#12P#10408F...In a certain sense, they're a pitiful lot.\x02",
    )

    CloseMessageWindow()

    label("loc_4913")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_496E")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FThinking about what they did,\x01",
            "I don't even pity them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A23")

    label("loc_496E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49D2")

    ChrTalk(
        0x105,
        (
            "#12P#10403FThinking about what they did,\x01",
            "I have no room for pitying them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A23")

    label("loc_49D2")


    ChrTalk(
        0x109,
        (
            "#12P#10103FThinking about what they did,\x01",
            "I have no room for pitying them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A23")


    ChrTalk(
        0x101,
        (
            "#12P#00001FPutting the Cult aside,\x01",
            "KeA is completely innocent.\x02\x03",
            "#00003FEven if she's an existence created\x01",
            "for the Crois Clan's goals...\x02\x03",
            "Even if she possesses\x01",
            "miraculous abilities...\x01",
            "Those things don't matter.\x02\x03",
            "That child who woke up before our eyes\x01",
            "was a genuine, normal little girl.\x02\x03",
            "#00001FAnd yet, she was locked up all alone in\x01",
            "a place like that for hundreds of years...\x02\x03",
            "And now, Miss Mariabell\x01",
            "and Lawyer Ian are trying \x01",
            "to use her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F...No matter the circumstances,\x01",
            "like hell we're gonna forgive 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...For the present, with this the Cult\x01",
            "data has been completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI don't know the detailed circumstances\x01",
            "of this incident you are involved in, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI understand so much that it hurts\x01",
            "that Miss KeA is a very precious\x01",
            "existence for you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPlease...do your best.\x01",
            "I too will cheer for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThank you very much, Miss Rebecca.\x02\x03",
            "#00003FWe will bring KeA back\x01",
            "with our own hands.\x02\x03",
            "#00001FEven in order to create a future\x01",
            "where our precious KeA...\x01",
            "When that child can live smiling...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4E81")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_4E81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4E9A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4E9A")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    TalkEnd(0x8)

    label("loc_4EA9")

    Jump("loc_2EA1")

    label("loc_4EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FCB")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PIf you obtain another "fragment",\x01",
            "please bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPlease ask me again in case you want\x01",
            "to check the decrypted data too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4FAC")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_4FAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4FC5")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4FC5")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_4FCB")

    Return()

    # Function_9_2DC7 end

    def Function_10_4FCC(): pass

    label("Function_10_4FCC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50CE")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[About The Cult]\x01",              # 0
            "[About Gnosis]\x01",                # 1
            "[About The Divine Child]\x01",      # 2
            "[Quit]\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5081"),
        (1, "loc_508F"),
        (2, "loc_509D"),
        (3, "loc_50AB"),
        (SWITCH_DEFAULT, "loc_50BA"),
    )


    label("loc_5081")

    Sound(72, 0, 100, 0)
    Call(0, 11)
    Jump("loc_50C9")

    label("loc_508F")

    Sound(72, 0, 100, 0)
    Call(0, 12)
    Jump("loc_50C9")

    label("loc_509D")

    Sound(72, 0, 100, 0)
    Call(0, 13)
    Jump("loc_50C9")

    label("loc_50AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50C9")

    label("loc_50BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50C9")

    label("loc_50C9")

    Jump("loc_4FD6")

    label("loc_50CE")

    Return()

    # Function_10_4FCC end

    def Function_11_50CF(): pass

    label("Function_11_50CF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52F9")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01\x01",
            "──My name is Joachim Gｸnther,\x01",
            "High Priest of the "D∴G Cult".\x01",
            "Six years ago, our Cult was almost completely destructed \x01",
            "due to the actions of many powers, Bracers included.\x01",
            "However, only I avoided harm for certain reasons\x01",
            "and was able to escape safely to this land of ■.\x01",
            "I had survived in order to accomplish the Cult\x01",
            "ambition thanks to the great "■"'s guidance.\x01",
            "For when the time comes──\x01",
            "I have decided to record data in each terminal\x01",
            "as material for writing new Testaments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5500")

    label("loc_52F9")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01\x01",
            "──My name is Joachim Gｸnther,\x01",
            "High Priest of the "D∴G Cult".\x01",
            "Six years ago, our Cult was almost completely destructed \x01",
            "due to the actions of many powers, Bracers included.\x01",
            "However, only I avoided harm for certain reasons\x01",
            "and was able to escape safely to this land of origin.\x01",
            "I had survived in order to accomplish the Cult\x01",
            "ambition thanks to the great "D"'s guidance.\x01",
            "For when the time comes──\x01",
            "I have decided to record data in each terminal\x01",
            "as material for writing new Testaments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5500")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFirst, I will speak of our Cult's origins.\x01",
            "To do that, I will have to look back at the annoying\x01",
            "history this Zemuria Continent has followed.\x01\x01",
            "──Approximately 1200 years ago, due to the \x01",
            ""Great Collapse", order and an advanced\x01",
            "civilization were lost,  and the "Dark Ages" \x01",
            "where war and poverty  ruled, were brought forth.\x01",
            "Then, the weary people committed a grave error.\x01\x01",
            "Cajoled by the words of imbeciles who had\x01",
            "suddenly appeared, they ended up accepting\x01",
            "the selfish order they had invented.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5932")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words── The foolish ■■ and the\x01",
            ""■ of ■■", who is the symbol of their faith.\x01",
            "With their order, the "Dark Ages" died, and that\x01",
            "faith spread throughout the continent at once...\x01\x01",
            "I want you to think about this carefully.\x01",
            "If it is true that a "■" exists, shouldn't she\x01",
            "bestow equal salvation to everyone?\x01",
            "However, until this very day the notion of \x01",
            "disparities still exists and people never cease \x01",
            "to lose their lives due to disasters and misfortunes.\x01",
            "So the "■" chooses who to save?\x01",
            "That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5B6E")

    label("loc_5932")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words── The foolish Septian Church and the\x01",
            ""Goddess of the Sky", who is the symbol of their faith.\x01",
            "With their order, the "Dark Ages" died, and that\x01",
            "faith spread throughout the continent at once...\x01\x01",
            "I want you to think about this carefully.\x01",
            "If it is true that a "Goddess" exists, shouldn't she\x01",
            "bestow equal salvation to everyone?\x01",
            "However, until this very day the notion of \x01",
            "disparities still exists and people never cease \x01",
            "to lose their lives due to disasters and misfortunes.\x01",
            "So the "Goddess" chooses who to save?\x01",
            "That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5B6E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D3A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretence\x01",
            "in order for the "■■" to acquire power.\x01",
            "There is no way something like a "■" exists.\x01\x01",
            "Our predecessors, having arrived at that truth,\x01",
            "set on a long journey in order to meet a "■■".\x01\x01",
            "Then, at the time when the era changed\x01",
            "to the Middle Ages, they finally found it.\x01",
            "■■■■, ■■■■■■■\x01",
            "lying in the depths of this land...\x01\x01",
            ""■"── That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5F2D")

    label("loc_5D3A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretence\x01",
            "in order for the "Septian Church" to acquire power.\x01",
            "There is no way something like a "Goddess" exists.\x01\x01",
            "Our predecessors, having arrived at that truth,\x01",
            "set on a long journey in order to meet a "True God".\x01\x01",
            "Then, at the time when the era changed\x01",
            "to the Middle Ages, they finally found it.\x01",
            "An existence longly asleep, harboring in its body\x01",
            "a great power, lying in the depths of this land...\x01\x01",
            ""D"── That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5F2D")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_50CF end

    def Function_12_5F41(): pass

    label("Function_12_5F41")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_60FA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01\x01",
            ""Gnosis"... It is a secret drug which uses\x01",
            ""Pleroma Grass" as ingredient, a ■■\x01",
            "said to ■■■■.\x01",
            "As for its mixing method, ■■■■■■■.\x01",
            "By taking it, physical ability and responsiveness\x01",
            "increase, and furthermore, it has the effect of\x01",
            "drawing out the user's latent abilities.\x01",
            "■■■■■■■■■.\x01",
            "■■■■■■■■■.\x01",
            ""Gnosis" is a drug to ■ the\x01",
            "■'s ■ to "■"'s ■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_62F7")

    label("loc_60FA")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01\x01",
            ""Gnosis"... It is a secret drug which uses\x01",
            ""Pleroma Grass" as ingredient, a legendary\x01",
            "plant said to bloom above Septium Veins.\x01",
            "As for its mixing method, it goes along with "D".\x01",
            "By taking it, physical ability and responsiveness\x01",
            "increase, and furthermore, it has the effect of\x01",
            "drawing out the user's latent abilities.\x01",
            "However, those are nothing more than the beginning.\x01",
            "The true power of this drug laid somewhere else.\x01",
            ""Gnosis" is a drug to link the\x01",
            "user's mind to "D"'s spirit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_62F7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6480")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy ■ with the ■'s ■,\x01",
            ""■" is able to store ■ and ■.\x01",
            "Sooner or later, when that ■ will lead\x01",
            "to ■, "■" will ■■■■.\x01\x01",
            "Furthermore, there was room\x01",
            "for improvement in "Gnosis".\x01",
            "■■■■■■■■■■■■■,\x01",
            "it is ■■■■■■ to "■".\x01\x01",
            "■■■■■ since then, our Cult has\x01",
            "researched a way higher effective "Gnosis"...\x01",
            "And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_665E")

    label("loc_6480")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy unifying with the user's mind,\x01",
            ""D" is able to store knowledge and grow.\x01",
            "Sooner or later, when that knowledge will lead\x01",
            "to "wisdom", "D" will come back to life.\x01\x01",
            "Furthermore, there was room\x01",
            "for improvement in "Gnosis".\x01",
            "When the user's abilities are forced to the\x01",
            "limit and brought out, it is possible to supply\x01",
            "far more knowledge to "D".\x01",
            "For 500 years since then, our Cult has\x01",
            "researched a way higher effective "Gnosis"...\x01",
            "And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_665E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_680A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a ■■\x01",
            "to ■ we ■■■■■■■,\x01",
            "we were close to perfecting "Gnosis",\x01",
            "but a miscalculation arose.\x01\x01",
            "Because the experiments were on a large scale,\x01",
            "Bracers and other authorities smelled our existence\x01",
            "and that was connected to the destruction\x01",
            "of all the lodges as well as the Cult itself.\x01\x01",
            "What foolishness it was, I say.\x01",
            "For our "■■" to ■■■■,\x01",
            "some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_69CB")

    label("loc_680A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a speed incomparable\x01",
            "to when we had started 500 years ago,\x01",
            "we were close to perfecting "Gnosis",\x01",
            "but a miscalculation arose.\x01\x01",
            "Because the experiments were on a large scale,\x01",
            "Bracers and other authorities smelled our existence\x01",
            "and that was connected to the destruction\x01",
            "of all the lodges as well as the Cult itself.\x01\x01",
            "What foolishness it was, I say.\x01",
            "For our "True God" to come back to life,\x01",
            "some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_69CB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BB7")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly\x01",
            "recovered the experimental data and\x01",
            "came to this land of ■, Crossbell.\x01\x01",
            "As for the "Pleroma Grass" which is\x01",
            "a "Gnosis" ingredient, since it ■ in\x01",
            "the ■■ in the ■■\x01",
            "of ■, I had no ■ problems.\x01",
            "Also, in the depths of this "Fort of Sun", there is\x01",
            "a research facility ■ by ■■■\x01",
            "and it is furnished with many high-tech equipment.\x01",
            "Thus, blessed by having a research environment,\x01",
            "I finally completed the secret drug──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6DC4")

    label("loc_6BB7")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly\x01",
            "recovered the experimental data and\x01",
            "came to this land of origin, Crossbell.\x01\x01",
            "As for the "Pleroma Grass" which is\x01",
            "a "Gnosis" ingredient, since it grows in\x01",
            "the Marshlands in the southern part\x01",
            "of Crossbell, I had no supply problems.\x01",
            "Also, in the depths of this "Fort of Sun", there is\x01",
            "a research facility built by Middle Ages alchemists\x01",
            "and it is furnished with many high-tech equipment.\x01",
            "Thus, blessed by having a research environment,\x01",
            "I finally completed the secret drug──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6DC4")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_12_5F41 end

    def Function_13_6DD8(): pass

    label("Function_13_6DD8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F62")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01\x01",
            "Crossbell is considered by our "D∴G Cult"\x01",
            "our ■ and ■■■.\x01",
            "The ■ is because it is the place where\x01",
            "the "Divine Child" ■■■■■.\x01\x01",
            "■■■ of the "■■", the "Divine Child"\x01",
            "is a ■■■■ "D∴G Cult".\x01",
            "■■■■■ "Fort of Sun"■,\x01",
            "■■■■■■■■■. ■■\x01",
            "■■■■■■■■■■\x01",
            "■■■■■■ "Fort of Sun"■■■■■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7165")

    label("loc_6F62")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01\x01",
            "Crossbell is considered by our "D∴G Cult"\x01",
            "our headquarters and land of origin.\x01",
            "The reason is because it is the place where\x01",
            "the "Divine Child" was inherited by our founders.\x01\x01",
            "As the vessel of the "True God", the "Divine Child"\x01",
            "is a symbolic existence for our "D∴G Cult".\x01",
            "Continuing to sleep in the "Fort of Sun" basement,\x01",
            "it has the aspect of a young human maiden. It is\x01",
            "said she has been waiting for the moment to wake\x01",
            "up at the altar of the "Fort of Sun" for 500 years.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7165")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72E8")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a ■ to be able to ■■■■...\x01",
            "It is hard to believe she is a being of this world.\x01\x01",
            "However, I really saw her with my eyes.\x01",
            "A ■■■■■■■■\x01",
            "■■ a ■ called the "■■"──\x01",
            "I saw her ■■.\x01\x01",
            "As for the "■■", it is an "Artifact"\x01",
            "which the ■■, based on the\x01",
            "■■ they were ■, ■.\x01",
            "In this case, even ■■■■\x01",
            "■■■■, is only something natural.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_74E8")

    label("loc_72E8")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a human to be able to live that much time...\x01",
            "It is hard to believe she is a being of this world.\x01\x01",
            "However, I really saw her with my eyes.\x01",
            "A young girl who keeps sleeping like she is\x01",
            "dozing inside a globe called the "Divine Cradle"──\x01",
            "I saw her divine figure.\x01\x01",
            "As for the "Divine Cradle", it is an "Artifact"\x01",
            "which the Cult predecessors, based on the\x01",
            "alchemists skills they were researching, made.\x01",
            "In this case, even this phenomenon that should\x01",
            "be called a wonder, is only something natural.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_74E8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_767C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe "Divine Child" ■■■■■\x01",
            "■■■■■■■■■■■\x01",
            "■ "Gnosis" since ■■■■■.\x01\x01",
            "──When she ■ "■", the "Divine Child"\x01",
            "will ■■, and she will ■ "■", the ■■.\x01",
            "Then, ■■'s ■ and ■ will\x01",
            "be ■ in "■" and each person will \x01",
            "be released from the spell of the "■"\x01\x01",
            "This is the prophecy our "D∴G Cult"'s predecessors\x01",
            "left us and the ambition we must fulfill──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7870")

    label("loc_767C")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe "Divine Child" is regarded to have accumulated\x01",
            "in her body what could be said to be infinite knowledge\x01",
            "through "Gnosis" since the era she was born.\x01\x01",
            "──When she obtains "wisdom", the "Divine Child"\x01",
            "will wake up, and she will become "D", the True God.\x01",
            "Then, all people's wills and souls will\x01",
            "be consolidated in "D" and each person will \x01",
            "be released from the spell of the "Goddess".\x01\x01",
            "This is the prophecy our "D∴G Cult"'s predecessors\x01",
            "left us and the ambition we must fulfill──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7870")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_13_6DD8 end

    def Function_14_7884(): pass

    label("Function_14_7884")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78A9")
    SetChrPos(0xFE, 40, 40, 12610, 0)
    Jump("loc_795D")

    label("loc_78A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78CE")
    SetChrPos(0xFE, -1000, 40, 12400, 0)
    Jump("loc_795D")

    label("loc_78CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78F3")
    SetChrPos(0xFE, 1140, 40, 12400, 0)
    Jump("loc_795D")

    label("loc_78F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7918")
    SetChrPos(0xFE, 110, 0, 11010, 0)
    Jump("loc_795D")

    label("loc_7918")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_793D")
    SetChrPos(0xFE, -950, 0, 10770, 0)
    Jump("loc_795D")

    label("loc_793D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_795D")
    SetChrPos(0xFE, 1080, 0, 10720, 0)

    label("loc_795D")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_7884 end

    def Function_15_796C(): pass

    label("Function_15_796C")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_798C")
    BeginChrThread(0x101, 1, 0, 14)

    label("loc_798C")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79A3")
    BeginChrThread(0x102, 1, 0, 14)

    label("loc_79A3")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79BA")
    BeginChrThread(0x103, 1, 0, 14)

    label("loc_79BA")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79D1")
    BeginChrThread(0x104, 1, 0, 14)

    label("loc_79D1")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79E8")
    BeginChrThread(0x109, 1, 0, 14)

    label("loc_79E8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79FF")
    BeginChrThread(0x105, 1, 0, 14)

    label("loc_79FF")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A16")
    BeginChrThread(0x106, 1, 0, 14)

    label("loc_7A16")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A2D")
    BeginChrThread(0x10A, 1, 0, 14)

    label("loc_7A2D")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A47")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_7A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A60")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_7A60")

    Return()

    # Function_15_796C end

    def Function_16_7A61(): pass

    label("Function_16_7A61")

    ClearScenarioFlags(0x1, 6)
    ClearScenarioFlags(0x1, 7)
    ClearScenarioFlags(0x2, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C97")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB3")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7AB3")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AE7")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7AE7")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B1B")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7B1B")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B4F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7B4F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B83")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7B83")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB7")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7BB7")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BEB")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7BEB")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C1F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7C92")

    label("loc_7C1F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C56")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Jump("loc_7C92")

    label("loc_7C56")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C8D")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_7C92")

    label("loc_7C8D")

    Jump("loc_7C97")

    label("loc_7C92")

    Jump("loc_7A74")

    label("loc_7C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_863C")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_68(-340, 1540, 12370, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 15)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Oh, everyone...\x01",
            "It looks like you have considerably\x01",
            "filled the Combat Notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since I would like to note down the monster information,\x01",
            "I wonder if I could have a look at it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#12PYes, gladly.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Thank you very much.\x01",
            "I will return your notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is your compensation this time.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EC6")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x1 received.\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_81C8")

    label("loc_7EC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 received.\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_81C8")

    label("loc_7F1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F72")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 received.\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_81C8")

    label("loc_7F72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC8")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4 received.\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_81C8")

    label("loc_7FC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 received.\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_81C8")

    label("loc_801E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8074")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x6 received.\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_81C8")

    label("loc_8074")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80CA")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x7 received.\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_81C8")

    label("loc_80CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8120")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 received.\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_81C8")

    label("loc_8120")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8176")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4500 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x9 received.\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_81C8")

    label("loc_8176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C8")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "5000 mira\x07\x00",
            " received.\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 received.\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_81C8")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81FE")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 received.\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_822B")

    label("loc_81FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_822B")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_822B")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8363")

    ChrTalk(
        0x8,
        (
            "Please stop by when you have gathered\x01",
            "monsters information again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82F5")

    ChrTalk(
        0x102,
        "#12P#0100FWe will impose on you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_835E")

    label("loc_82F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_832D")

    ChrTalk(
        0x103,
        "#12P#0200FWe will come again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_835E")

    label("loc_832D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_835E")

    ChrTalk(
        0x104,
        "#12P#0300FWe'll come again!\x02",
    )

    CloseMessageWindow()

    label("loc_835E")

    Jump("loc_85D4")

    label("loc_8363")


    ChrTalk(
        0x8,
        (
            "It looks like you have gathered plenty\x01",
            "of new type monsters information too.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this, I think that our security measures\x01",
            "will become even more perfect from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FHa ha...we're honored to have been of help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, we are really indebted\x01",
            "towards you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And so, please allow me to give you\x01",
            "a special reward too for this time.\x01",
            "By all means, please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "10000 mira\x07\x00",
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    ChrTalk(
        0x8,
        (
            "I will pray for your activities\x01",
            "from now on too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need anything else, please\x01",
            "visit me again whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85D4")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_85EB")
    ClearScenarioFlags(0x1, 5)

    label("loc_85EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8604")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_8604")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_861D")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_861D")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_87DF")

    label("loc_863C")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_872A")

    ChrTalk(
        0x8,
        (
            "SInce I think that the information\x01",
            "gathered at HQ is already enough,\x01",
            "let us end the investigation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There could be something else\x01",
            "I will need you your assistance.\x01",
            "I will count on you when that time comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87DF")

    label("loc_872A")


    ChrTalk(
        0x8,
        (
            "It looks like you have been collecting\x01",
            "Combat Notebook contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you have gathered a little more\x01",
            "information, please show it to me.\x01",
            "I will note down the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87DF")

    Return()

    # Function_16_7A61 end

    def Function_17_87E0(): pass

    label("Function_17_87E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_892F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8809")
    Call(0, 18)
    Jump("loc_892A")

    label("loc_8809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8824")
    Call(0, 18)
    Jump("loc_892A")

    label("loc_8824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_883A")
    Call(0, 18)
    Jump("loc_892A")

    label("loc_883A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8850")
    Call(0, 18)
    Jump("loc_892A")

    label("loc_8850")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "#01900FEveryone, do you know of an\x01",
            "orbal game called "Pom!"?\x02\x03",
            "#01909FHu hu, actually I began playing it too.\x01",
            "If you want, let us exchange accounts.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            ""Fran's Account" obtained.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    TalkEnd(0x9)

    label("loc_892A")

    Jump("loc_8932")

    label("loc_892F")

    Call(0, 18)

    label("loc_8932")

    Return()

    # Function_17_87E0 end

    def Function_18_8933(): pass

    label("Function_18_8933")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8944")
    Jump("loc_AC3B")

    label("loc_8944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8952")
    Jump("loc_AC3B")

    label("loc_8952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B19")
    SoundLoad(803)

    ChrTalk(
        0x9,
        (
            "#01901FE-Everyone, the situation\x01",
            "has become serious, eh?\x02\x03",
            "Even police HQ has been\x01",
            "flurried non-stop since this morning...\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#01905FAh, excuse me...\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    OP_24(0x323)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x9,
        (
            "#01903FYes, Crossbell Police...\x02\x03",
            "#01901FYes, yes...\x02\x03",
            "That's right, since last night,\x01",
            "to settle the situation, the CGF...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(She really looks busy...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yes, let us do what\x01",
            "we can do too.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 7)
    OP_24(0x323)
    Jump("loc_8BD3")

    label("loc_8B19")

    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is conversating at the receiver.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01901FYes, yes...\x02\x03",
            "#01908F...I am terribly sorry.\x01",
            "Concerning the real identity of the\x01",
            "armed group, it's not clear yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BD3")

    Jump("loc_AC3B")

    label("loc_8BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_8CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BF3")
    Call(0, 21)
    Jump("loc_8CB5")

    label("loc_8BF3")


    ChrTalk(
        0x9,
        (
            "#01900FLike I told you before,\x01",
            "I arranged an orbal boat\x01",
            "at the Waterfront Area jetty.\x02\x03",
            "#01904FA mechanic should be near.\x01",
            "Please, go have a look there!\x01\x02\x03",
            "#01900FPlease be careful, everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB5")

    Jump("loc_AC3B")

    label("loc_8CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F9E")

    ChrTalk(
        0x9,
        (
            "#01900FEveryone, thank you very much\x01",
            "for all your hard work yesterday.\x02\x03",
            "It seems you had great achievements,\x01",
            "be it about the "Society" or even the\x01",
            "cause of the train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, well, the truth is that we\x01",
            "didn't do anything special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. In coping with the accident,\x01",
            "the people who worked all night\x01",
            "long had it way tougher than us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FEven so, you all too continued\x01",
            "investigation activities until\x01",
            "pretty late in the evening yesterday.\x02\x03",
            "#01902FPlease, be very considerate in\x01",
            "managing your health condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FThank you very much for your concern.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FWell, you should be likewise busy,\x01",
            "so sweet Fran, don't push yourself, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes, roger that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 0)
    Jump("loc_9070")

    label("loc_8F9E")


    ChrTalk(
        0x9,
        (
            "#01900FIt appears that today too you received\x01",
            "a few support requests...\x02\x03",
            "Please, do your best to\x01",
            "a reasonable extent.\x02\x03",
            "I will strictly keep myself in check too\x01",
            "with dedication so to not do the impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9070")

    Jump("loc_AC3B")

    label("loc_9075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_92ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91FF")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is conversating at the receiver.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01903FYes, yes...\x02\x03",
            "#01901F...I am terribly sorry.\x01",
            "The accident cause is currently\x01",
            "under investigation...\x02\x03",
            "Even about the service resume,\x01",
            "they are doing everything possible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(It looks like she's dealing\x01",
            "with the train accident.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yes, she looks busy, it's\x01",
            "better to not disturb her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_92E8")

    label("loc_91FF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is conversating at the receiver.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01903FYes, yes...\x02\x03",
            "#01901F...I am terribly sorry.\x01",
            "The accident cause is currently\x01",
            "under investigation...\x02\x03",
            "Even about the service resume,\x01",
            "they are doing everything possible...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92E8")

    Jump("loc_AC3B")

    label("loc_92ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9422")

    ChrTalk(
        0x9,
        (
            "#01903FAzure Flowers, and also Cryptids...\x02\x03",
            "#01901FSomehow they give an ominous impression,\x01",
            "but in any case, we can only do what we\x01",
            "can thoroughly.\x02\x03",
            "Uhm, everyone, please\x01",
            "be careful from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYou too Fran, do your best with support.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9553")

    label("loc_9422")


    ChrTalk(
        0x9,
        (
            "#01903FBoth the state of tension following the\x01",
            "independence proposal and the current abnormal\x01",
            "situation somehow give an ominous impression.\x02\x03",
            "#01901FI think it can't be helped thinking\x01",
            "about it too much, but...\x02\x03",
            "In any case, I think that I too have to deal\x01",
            "calmly with the work I have before my eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9553")

    Jump("loc_AC3B")

    label("loc_9558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9888")

    ChrTalk(
        0x9,
        (
            "#01901FEveryone... It appears that you somehow\x01",
            "can manage to deal with the "Cryptids".\x02\x03",
            "Like the one that was in the old abandoned mine,\x01",
            "they appear to be bizarre monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, they're nothing but incomprehensible\x01",
            "for now. In any case, we'll try to\x01",
            "progress with the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F? Is there something troubling you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FAh, yes, because I heard that\x01",
            "Cryptids are quite strong...\x01",
            "I don't want you to get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYes, you're right.\x02\x03",
            "#10100FHowever, we won't do the impossible,\x01",
            "so it's all right to not be worried that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FYes...I see.\x02\x03",
            "Also, you're the veteran Special\x01",
            "Support Section, after all.\x02\x03",
            "#01909FFran Seeker, having faith\x01",
            "in your success in battle,\x01",
            "will wait for your report!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, thanks,\x01",
            "sweet Fran.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 1)
    Jump("loc_9923")

    label("loc_9888")


    ChrTalk(
        0x9,
        (
            "#01902FEveryone, please pay attention\x01",
            "in your Cryptid investigation.\x02\x03",
            "Fran Seeker, having faith\x01",
            "in your success in battle,\x01",
            "will wait for your report!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9923")

    Jump("loc_AC3B")

    label("loc_9928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9943")
    Call(0, 20)
    Jump("loc_9BD6")

    label("loc_9943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B11")

    ChrTalk(
        0x9,
        (
            "#01900FCaptain Julia has an imperious\x01",
            "air and she's very cool...\x01",
            "I really admire her.\x02\x03",
            "#01909FWell, I think that big\x01",
            "sis is cooler, though.㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, what do I have to do with you...\x02\x03",
            "#10101FI think that if other fans of Captain Julia\x01",
            "heard you they'd get angry for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I wonder.\x01",
            "It seems that you too have quite\x01",
            "the fans like Captain Julia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FSee, that's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FG-Give me a break...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9BD6")

    label("loc_9B11")


    ChrTalk(
        0x9,
        (
            "#01900FToday's security at Orchis Tower\x01",
            "is a rare chance, so I too wanted\x01",
            "to be assigned there...\x02\x03",
            "#01906FI wanted to see the imperios and\x01",
            "cool Captain Julia and big sis\x01",
            "while doing security!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD6")

    Jump("loc_AC3B")

    label("loc_9BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9EA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3B")
    TurnDirection(0x9, 0x109, 0)

    ChrTalk(
        0x9,
        (
            "#01902FOh, big sis.\x02\x03",
            "You took part in the unveiling\x01",
            "ceremony security, right?\x01",
            "...How was it? Amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes, that's right.\x02\x03",
            "Especially Princess Klaudia\x01",
            "and Captain Julia from Liberl\x01",
            "were amaz...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01905FD-Did you see them so close!?\x02\x03",
            "#01906FUuh, how nice.\x01",
            "But only you did big sis, that's no fair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha, sorry Fran.\x01",
            "I'll make up for it with something next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha, of course this means that\x01",
            "Fran too is a Captain Julia fan, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Uhhm, what can I say,\x01",
            "men's society has lost its face.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 6)
    Jump("loc_9E9E")

    label("loc_9E3B")


    ChrTalk(
        0x9,
        (
            "#01902FPrincess Klaudia and\x01",
            "even Captain Julia...!\x02\x03",
            "How nice, I too wanted\x01",
            "to see them close.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E9E")

    Jump("loc_AC3B")

    label("loc_9EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A1E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A12E")

    ChrTalk(
        0x9,
        (
            "#01902FUh uh, finally the Trade Conference\x01",
            "is going to start tomorrow.\x02\x03",
            "VIPs from all countries are going to gather,\x01",
            "there's going to be the Orchis Tower inauguration...\x01",
            "Somehow my heart is racing fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FJeez, you aren't a child anymore,\x01",
            "so don't just say easygoing things\x01",
            "and concentrate on your job, ok?\x02\x03",
            "#10106FEven you Fran are going to be busier\x01",
            "than usual during the Conference, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01900FYou're right, and that's exactly why\x01",
            "I have to find enjoyment in it.\x02\x03",
            "You too big sis, you're\x01",
            "always too serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHu hu, you can say that for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FW-Wazy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FAhaha...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 7)
    Jump("loc_A1DB")

    label("loc_A12E")


    ChrTalk(
        0x9,
        (
            "#01902FI'm going to be busy with work for sure,\x01",
            "but since it's such a big event, \x01",
            "somehow my heart is racing fast.\x02\x03",
            "#01909FUh uh, I can't wait for tomorrow's ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1DB")

    Jump("loc_AC3B")

    label("loc_A1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_A29F")

    ChrTalk(
        0x9,
        (
            "#01901FAccording to Mayor Bickson's story,\x01",
            "it appears that something strange is\x01",
            "going on inside the old mine.\x02\x03",
            "It's not know what \x01",
            "is strange, but...\x01",
            "Please, do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC3B")

    label("loc_A29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2BA")
    Call(0, 19)
    Jump("loc_A521")

    label("loc_A2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A45D")

    ChrTalk(
        0x9,
        (
            "#01906FAah, I'm really glad\x01",
            "I could become able\x01",
            "to call you "big sis".\x02\x03",
            "#01902FNow it appears that I\x01",
            "can focus on my job\x01",
            "without reserve.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106FW-Was that so bad to be an\x01",
            "hindrance for your job...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    ChrTalk(
        0x9,
        (
            "#01901FBut! For me it's a\x01",
            "life-and-death matter!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Aah, enough, what about\x01",
            "decorum on the workplace...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(D-Don't mind it, Noｱl.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A521")

    label("loc_A45D")


    ChrTalk(
        0x9,
        (
            "#01902FUh uh, now it appears that\x01",
            "I can focus on my job\x01",
            "without reserve.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    ChrTalk(
        0x9,
        (
            "#01909FDo your best at work\x01",
            "today too, big sis㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Jeez, I just won't say anything anymore...)\x02",
    )

    CloseMessageWindow()

    label("loc_A521")

    Jump("loc_AC3B")

    label("loc_A526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_AC3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA87")

    ChrTalk(
        0x9,
        (
            "#01900FUh uh, at any rate, the\x01",
            "SSS activities have\x01",
            "finally restarted, eh?\x02\x03",
            "#01909FAs I'm involved with you\x01",
            "all as your operator, I\x01",
            "am especially moved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHa ha, even for us getting\x01",
            "back to the Support Section\x01",
            "is a kind of new feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, you're right.\x01",
            "We can work together\x01",
            "with Miss Fran again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FYes, I became keen\x01",
            "to this job!\x02\x03",
            "#01906FWhen you were on pause, I had \x01",
            "a hard time dealing with incessant\x01",
            "requests from the citizens...\x02\x03",
            "#01902FI was really looking forward to\x01",
            "you all resuming operations.\x02\x03",
            "#01909F...Also, I can finally\x01",
            "work with big sis!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00009FHa ha...I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FJeez, Fran...\x01",
            "How many times do you intend to make me\x01",
            "say that you don't have to call me big sis?\x02\x03",
            "#10101FListen, no matter if we're sisters,\x01",
            "because we're in the same workplace\x01",
            "you must bear in mind a minimum decorum.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#01906FUuh...I'm sorry.\x02\x03",
            "#01908FB-But, maybe I won't be able to get used t...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FYou will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHa ha, what a severe big sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FA-Anyway...\x02\x03",
            "#01900FWhen Tio and Mr.\x01",
            "Randy join later,\x01",
            "you'll be invincible.\x02\x03",
            "#01902FUh uh, I look forward from the bottom of\x01",
            "my heart to when you will all be together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, I feel the same too.\x02\x03",
            "#00002FThen... Fran, please\x01",
            "take good care of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 1)
    Jump("loc_AC3B")

    label("loc_AA87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB7C")

    ChrTalk(
        0x9,
        (
            "#01902FUh uh, being able to work together again with\x01",
            "you all makes me passionate about my job too.\x02\x03",
            "#01909FBig si...*cough*.\x01",
            "I can also work with Miss Noｱl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Jeez, this girl...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Ha ha, now now...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AC3B")

    label("loc_AB7C")


    ChrTalk(
        0x9,
        (
            "#01900FI think that a lot of requests are\x01",
            "going to come to the renewed \x01",
            "Support Section from now on.\x02\x03",
            "#01909FPlease allow me to give you steady\x01",
            "support as an operator like I did before!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC3B")

    TalkEnd(0x9)
    Return()

    # Function_18_8933 end

    def Function_19_AC3F(): pass

    label("Function_19_AC3F")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2550, 0, 12860, 0)
    SetChrPos(0x102, 3690, 0, 12840, 0)
    SetChrPos(0x109, 1950, 0, 11360, 0)
    SetChrPos(0x105, 3360, 0, 11340, 0)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#01900FAh, you came just at the right time!\x02\x03",
            "#01901FActually, I have a very important thing\x01",
            "to discuss with big si...with Miss Noｱl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FW-What's wrong Fran?\x01",
            "You have such a serious look...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01908FListen............\x02\x03",
            "#01906F...Is it calling you "big sis" on\x01",
            "the workplace bad no matter what?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#12P*shock*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FA-And I was thinking what could it be...\x02\x03",
            "#10101F...*cough*\x01",
            "I explained it many times when my transfer\x01",
            "to the Support Section was decided, right?\x02\x03",
            "#10103FI told you that because we're in the same workplace\x01",
            "you must bear in mind a minimum decorum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01905FB-But, big si...\x01",
            "No, Miss Noｱ...\x02\x03",
            "#01906FAah, I can't do that!\x01",
            "I can't get used to it no matter what!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_B05F():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B05F)
    Sleep(50)

    def lambda_B06F():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B06F)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00012FW-Well...Noｱl.\x01",
            "It's not something to be\x01",
            "so strict about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, that's right.\x01",
            "When Miss Fran says "Miss Noｱl"\x01",
            "I feel it's too formal...\x02\x03",
            "#00100FA way of calling she's not used to at a time\x01",
            "of an urgent communication could be inefficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FT-That could also be true, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01902FS-See...!\x01",
            "Even everyone is saying that!\x02\x03",
            "#01909FIsn't "big sis" all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, being a little lenient\x01",
            "seems to match with the\x01",
            "Support Section stance, right?\x02\x03",
            "#10302FYou see, it feels that way,\x01",
            "starting with the Chief.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00006F(I can't talk back on that point...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F...*sigh*, well, it can't be helped.\x01",
            "If everyone says so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FHooray! Then it's decided!\x02\x03",
            "#01900FEheheh, thank you very\x01",
            "much too, everyone!\x02\x03",
            "#01904F*cough*, then...\x02\x01",
            "#01909FIt's a pleasure working with you, big sis㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10101FA-At least, Fran... Don't mix personal\x01",
            "affairs with official business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FI know, big sis㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106F(S-She doesn't at all...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Ha ha, Noｱl too is no match for Fran.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x13F, 0)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_AC3F end

    def Function_20_B54E(): pass

    label("Function_20_B54E")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2400, 0, 12670, 0)
    SetChrPos(0x102, 3550, 0, 12670, 0)
    SetChrPos(0x103, 1360, 0, 12490, 0)
    SetChrPos(0x104, 1860, 0, 11200, 0)
    SetChrPos(0x109, 3040, 0, 11190, 0)
    SetChrPos(0x105, 4090, 0, 11380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#01900FAh, Tio!\x01",
            "You've finally come back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes, fortunately.\x02\x03",
            "#00204FMiss Fran, it's nice to be\x01",
            "working with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FUh uh, likewise.\x02\x03",
            "#01900FAt any rate, now the\x01",
            "SSS members are\x01",
            "all together!\x02\x03",
            "I'm expecting even more successes from you all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha, thank you Fran.\x01",
            "We'll do our very best.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01905FOh, that's right...\x01",
            "Let me thank you officially!\x02\x03",
            "#01900FBig sis, you got a sign from\x01",
            "Captain Julia for me too!\x02\x03",
            "#01909FThank you very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FAhaha, it's ok, don't mind it.\x02\x03",
            "#10106FI felt bad towards you for being the\x01",
            "only one to talk to her directly...\x02\x03",
            "#10100FI'll give it you another time,\x01",
            "when things are calmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes, I'm looking forward to it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, now that you mention it, Elie and\x01",
            "Noｱl got them yesterday on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, the crown princess and Captain Julia\x01",
            "too were really generous persons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHa ha, as expected, sweet Fran\x01",
            "is a fan of Captain Julia too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FBut of course!\x02\x03",
            "#01900FCaptain Julia has an imperious\x01",
            "air and she's cool and...\x01",
            "I really admire her!\x02\x03",
            "#01909FWell, even so I think that big\x01",
            "sis is the coolest by far㈱\x02",
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
        0x109,
        (
            "#12P#10111FH-Hey now...!\x02\x03",
            "#10106FW-Why do you have to say\x01",
            "such a grand thing, Fran...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, it appears that to\x01",
            "Miss Fran, Miss Noｱl is\x01",
            "the best no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FUhhm, typical of her...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x148, 5)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_20_B54E end

    def Function_21_BC6E(): pass

    label("Function_21_BC6E")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1300, 13270, 0)
    MoveCamera(49, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29370, 0)
    SetChrPos(0x101, 2400, 0, 12670, 0)
    SetChrPos(0x102, 3550, 0, 12670, 0)
    SetChrPos(0x103, 1360, 0, 12490, 0)
    SetChrPos(0x104, 1860, 0, 11200, 0)
    SetChrPos(0x109, 3040, 0, 11190, 0)
    SetChrPos(0x105, 4090, 0, 11380, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#01905FOh, everyone...\x02\x03",
            "#01900FLike I told you before, I\x01",
            "readied an orbal boat at\x01",
            "the Waterfront Area jetty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thank you Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FWe'll use it at once.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#01903FIt appears you're going to the Marshlands\x01",
            "to look for those Bracers, but...\x02\x03",
            "#01908FUhhm, are you going to be fine...?\x01",
            "It's the place where two Bracers, who are\x01",
            "about to reach A-rank, went missing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FMiss Fran...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FSorry to make you worry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906F*sigh*, how nice would be if in such\x01",
            "times even I could do something...\x02\x03",
            "#01900FUhmm, if you want, would you like\x01",
            "to take Ban Ban with you as a charm?\x02",
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
        0x101,
        "#12P#00005FIf I remember correctly, Ban Ban is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FEhm...\x01",
            "It's a bear plushy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FWhen you hug it, it greatly calms you down!\x02\x03",
            "#01900FBig sis, you do it too sometimes\x01",
            "when no one is watching you, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#12P#10111FWha!?\x01",
            "I-I'd never do that...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01901FI feel an overwhelming sorrow sending in\x01",
            "Ban Ban to a place that could be dangerous, \x01",
            "but if it's for your sake, everyone...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No, we're fine...\x01",
            "For now, please calm down.\x02\x03",
            "#00002FHa ha, but thanks for the thought though.\x01",
            "I was feeling a little uneasy, but thanks to\x01",
            "you now I feel I could relax somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, this is Fran's very true worth.\x02\x03",
            "#10309FWe were also able to catch a\x01",
            "glimpse of Noｱl's private life.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10106F(Uuh, Fran!\x01",
            "I'll remember this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FAhaha, then I'm glad.\x02\x03",
            "#01900FPlease be careful when going there, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x17B, 7)
    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3010, 0, 12380, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_BC6E end

    def Function_22_C446(): pass

    label("Function_22_C446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C464")
    Call(0, 47)
    Return()

    label("loc_C464")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C475")
    Jump("loc_CFF4")

    label("loc_C475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C483")
    Jump("loc_CFF4")

    label("loc_C483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C526")

    ChrTalk(
        0xFE,
        (
            "No matter what, we'll do all\x01",
            "we can to remove the Red \x01",
            "Constellation from Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You too, please devote yourselves\x01",
            "to what you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFF4")

    label("loc_C526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C534")
    Jump("loc_CFF4")

    label("loc_C534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C542")
    Jump("loc_CFF4")

    label("loc_C542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C9C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C94E")

    ChrTalk(
        0xFE,
        "*phew*, this feels nice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(The bottle Miss Emma is holding...\x01",
            "Is it a supplement or something...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(It looks so...\x01",
            "Could she be really tired?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, "Sporitan X"...\x02\x03",
            "It appears you're drinking \x01",
            "quite the punchy thing...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FW-Wazy...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "It can't be helped, I pulled\x01",
            "an all nighter after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, so what?\x01",
            "Do you want to say that it's such a strange\x01",
            "thing for me to be drinking a supplement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Answer me...\x01",
            "Detective Lloyd Bannings!\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FNo, I didn't say anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmph...\x01",
            "No problem then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, can you \x01",
            "allow yourselves to\x01",
            "loaf around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean... You should be doing as many\x01",
            "support requests or whatever as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F(Hu hu, how unlucky for you.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(...You're one to talk.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x171, 6)
    Jump("loc_C9C0")

    label("loc_C94E")


    ChrTalk(
        0xFE,
        (
            "At any rate, you should be doing\x01",
            "support requests without\x01",
            "loafing around in this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And that's all.\x02",
    )

    CloseMessageWindow()

    label("loc_C9C0")

    Jump("loc_CFF4")

    label("loc_C9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C9D3")
    Jump("loc_CFF4")

    label("loc_C9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C9E1")
    Jump("loc_CFF4")

    label("loc_C9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CC24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA09")
    Call(0, 30)
    Jump("loc_CAE1")

    label("loc_CA09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA1B")
    Call(0, 31)
    Jump("loc_CAE1")

    label("loc_CA1B")


    ChrTalk(
        0xFE,
        (
            "What Mr. Dudley is expecting\x01",
            "from the Support Section is an\x01",
            "activity as support corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you think well about what that means, \x01",
            "you should know what you should do...\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAE1")

    Jump("loc_CC1F")

    label("loc_CAE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBB0")

    ChrTalk(
        0xFE,
        (
            "Section One will keep\x01",
            "marking Lechter Arundel\x01",
            "and Kilika Rouran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What're the two major powers scheming...?\x01",
            "It's unfathomable at present, but\x01",
            "we must investigate assiduously.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_CC1F")

    label("loc_CBB0")


    ChrTalk(
        0xFE,
        (
            "Please leave Lechter\x01",
            "Arundel and Kilika\x01",
            "Rouran to Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should return to\x01",
            "your own duties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC1F")

    Jump("loc_CFF4")

    label("loc_CC24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CFDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF22")

    ChrTalk(
        0xFE,
        (
            "Detective Bannings... Is your\x01",
            "support requests job going well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, well...for now we're\x01",
            "doing it at our usual pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Mr. Dudley is performing\x01",
            "the final checks on the security system\x01",
            "for the conference at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Section Chief Sergei will be making all kind of adjustments\x01",
            "at the counter-measures HQ on 2F for the entire day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...You all too have to deal with work\x01",
            "focusing all your energies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly why you shouldn't\x01",
            "say "at our usual pace".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FY-Yes, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu, always the\x01",
            "same severe woman.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Uhhm, when she doesn't speak,\x01",
            "she's quite the beauty though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Senior Randy...\x01",
            "That's not the problem here...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 0)
    Jump("loc_CFD8")

    label("loc_CF22")


    ChrTalk(
        0xFE,
        (
            "Both Mr. Dudley and Section\x01",
            "Chief Sergei are dealing with duties\x01",
            "using the energies they have at maximum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...You all too have to deal with work\x01",
            "focusing all your energies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFD8")

    Jump("loc_CFF4")

    label("loc_CFDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CFEB")
    Jump("loc_CFF4")

    label("loc_CFEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CFF4")

    label("loc_CFF4")

    TalkEnd(0xFE)
    Return()

    # Function_22_C446 end

    def Function_23_CFF8(): pass

    label("Function_23_CFF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D017")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D017")
    Call(0, 52)
    Return()

    label("loc_D017")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_23_CFF8 end

    def Function_24_D01E(): pass

    label("Function_24_D01E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D02F")
    Jump("loc_D9F2")

    label("loc_D02F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D03D")
    Jump("loc_D9F2")

    label("loc_D03D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D28D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D189")

    ChrTalk(
        0xFE,
        (
            "Jeez, things have become\x01",
            "terribly dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, at present, at Section Two\x01",
            "we're working hard supporting Section One,\x01",
            "turning a blind eye to all other cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spies entering Crossbell...\x01",
            "We're in the middle of sorting every little bit \x01",
            "of intel, especially about the Empire spy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D288")

    label("loc_D189")


    ChrTalk(
        0xFE,
        (
            "In any case, at present, at Section Two\x01",
            "we're working hard supporting Section One,\x01",
            "turning a blind eye to all other cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spies entering Crossbell...\x01",
            "We're in the middle of sorting every little bit \x01",
            "of intel, especially about the Empire spy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D288")

    Jump("loc_D9F2")

    label("loc_D28D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D4AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D40F")

    ChrTalk(
        0xFE,
        "Gnosis...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First of all, as an established tactic, \x01",
            "we were planning to search from \x01",
            "Revache's routes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We simply had a hunch that the possibility\x01",
            "it came in from there was low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway, at the present stage, it's no\x01",
            "use even if we think about this or that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, we can only intently crush\x01",
            "every possibility one by one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D4A6")

    label("loc_D40F")


    ChrTalk(
        0xFE,
        (
            "Well, anyway, at the present stage, \x01",
            "it's no use dwelling upon hypothesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, we can only intently crush\x01",
            "every possibility one by one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A6")

    Jump("loc_D9F2")

    label("loc_D4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D4B9")
    Jump("loc_D9F2")

    label("loc_D4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D6AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D5C2")

    ChrTalk(
        0xFE,
        (
            "Although there was the Support Section\x01",
            "collaboration, it seems that Raymond\x01",
            "did quite his best yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's really an unbelievable\x01",
            "story that while chasing the fake brand\x01",
            "trader you ran into the terrorists' remnants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D6A7")

    label("loc_D5C2")


    ChrTalk(
        0xFE,
        (
            "Although the Heiyue acted in the back,\x01",
            "it seems that Raymond did quite\x01",
            "his best alone yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's really an unbelievable\x01",
            "story that while chasing the fake brand\x01",
            "trader he ran into the terrorists' remnants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6A7")

    Jump("loc_D9F2")

    label("loc_D6AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C7")
    Call(0, 25)
    Jump("loc_D794")

    label("loc_D6C7")


    ChrTalk(
        0xFE,
        (
            "It was decided to take over at Section Two \x01",
            "a few of the jobs that normally would be\x01",
            "of Section One sphere of action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the situation is this.\x01",
            "It's really a general mobilization system.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D794")

    Jump("loc_D9F2")

    label("loc_D799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D7A7")
    Jump("loc_D9F2")

    label("loc_D7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D7B5")
    Jump("loc_D9F2")

    label("loc_D7B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D7C3")
    Jump("loc_D9F2")

    label("loc_D7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7DE")
    Call(0, 26)
    Jump("loc_D832")

    label("loc_D7DE")


    ChrTalk(
        0xA,
        (
            "Wild youths, huh...?\x01",
            "Man, what's the fun in causing\x01",
            "troubles for other people?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D832")

    Jump("loc_D9F2")

    label("loc_D837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D9F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D852")
    Call(0, 27)
    Jump("loc_D9F2")

    label("loc_D852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D975")

    ChrTalk(
        0xFE,
        (
            "Well, whatever.\x01",
            "If something comes up again,\x01",
            "we'll count on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even we of Section Two are\x01",
            "expecting great things from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FS-Sir.\x02\x03",
            "(Somehow these kind of words\x01",
            "makes me truly happy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Yes. I feel that we too have\x01",
            "been recognised a lot.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D9F2")

    label("loc_D975")


    ChrTalk(
        0xFE,
        (
            "Well, if something comes up\x01",
            "again, we'll count on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even we of Section Two are\x01",
            "expecting great things from you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9F2")

    TalkEnd(0xFE)
    Return()

    # Function_24_D01E end

    def Function_25_D9F6(): pass

    label("Function_25_D9F6")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        "Hey, if it isn't the SSS.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        (
            "#00603FI thought who could it be and it was you.\x02\x03",
            "#00600FIt seems you have undertaken\x01",
            "the "Cryptid" investigation, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHu hu, as expected you have sharp ears.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 500)

    ChrTalk(
        0xC,
        (
            "#00603FHmph, it's an official request from\x01",
            "the CGF after all. It's only\x01",
            "natural I receive intel about it...\x02\x03",
            "#00600FFrom what I've heard, it appears\x01",
            "they're opponents that can't be\x01",
            "gauged with common sense.\x02\x03",
            "In battle, you will have\x01",
            "to do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you for your warning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEven so...\x01",
            "You look quite busy with\x01",
            "counterintelligence work...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Well, a thing like the independence\x01",
            "proposal was said out loud, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're in a situation where one spy after the\x01",
            "other are being sent by all the Zemurian\x01",
            "countries to find out Crossbell moves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We have our hands full with\x01",
            "many spies who're just\x01",
            "simply trying to grasp those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FA-Are they so many...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        (
            "#00601F...In addition, there're the "Red Constellation"\x01",
            "and "Heiyue" movements too.\x02\x03",
            "And it's also obvious that we\x01",
            "can't let our guard down dealing\x01",
            "with crimes other than theirs.\x02\x03",
            "#00603FThe current situation is that we truly have as\x01",
            "many cases as we want that must be coped with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, being the circumstances like that it was \x01",
            "decided to undertake at Section Two a few of\x01",
            "the jobs from Section One sphere of actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because of that, we were having\x01",
            "a little business meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see...\x01",
            "You were talking about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHow to say, seems the situation\x01",
            "is harsh due to many things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 500)

    ChrTalk(
        0xC,
        (
            "#00603FHmph, for instance, no matter\x01",
            "how much your hand is limited,\x01",
            "you must do what you must.\x02\x03",
            "#00601FAt any rate, you have to see through\x01",
            "the duties you were given too.\x02\x03",
            "The "Cryptids" case is not a problem\x01",
            "that can be left alone at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, roger that.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetScenarioFlags(0x16A, 2)
    Return()

    # Function_25_D9F6 end

    def Function_26_E16B(): pass

    label("Function_26_E16B")

    OP_4B(0xA, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0xA,
        (
            "By the way, about those youths\x01",
            "of that runaway vehicle...\x01",
            "You arrested them yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Well, we couldn't leave things as they were.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Although it's regrettable that it seems\x01",
            "they were just punished with a fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "In any case, if you think that today\x01",
            "you aren't seeing them in the city,\x01",
            "maybe that got a small effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "*sigh*, I hope that's the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Honestly, if they weren't foreigners\x01",
            "we could've held them in custody\x01",
            "and severely reprimanded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I guess we can expect that\x01",
            "stuff from the next legislation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Right. Well, for now\x01",
            "we can only do things\x01",
            "the hard way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_E469")

    ChrTalk(
        0x101,
        (
            "#00001F(It appears they're talking\x01",
            "about those three persons.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Likely. I don't want them to\x01",
            "drive recklessly again...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4AF")

    label("loc_E469")


    ChrTalk(
        0x101,
        (
            "#00001F(Yesterday, eh...?\x01",
            "Did some accident happen in the city?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4AF")

    SetScenarioFlags(0x13E, 7)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_26_E16B end

    def Function_27_E4C5(): pass

    label("Function_27_E4C5")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Oh, haven't you gotten some\x01",
            "fresh personnel with you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Could they be the rumored\x01",
            "new SSS members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, exactly.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        (
            "And that means that you're\x01",
            "Noｱl from the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Mwhuhuhu, if you like, why don't we get \x01",
            "some tea or something else together next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FE-Ehhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Eh...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "Wait, you there, you're Wazy\x01",
            "Hemisphere of the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...My, seeing you from up close,\x01",
            "you have quite the pretty face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, is that so?\x02\x03",
            "#10304FHowever, I'm sorry for you, but\x01",
            "it looks like you're not my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Wait, why must I be\x01",
            "snubbed by a man!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "...Jeez, I was listening in silence, but\x01",
            "you're spouting nothing but stupid things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You too, follow the Support Section\x01",
            "guys' example and grow up a little!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or if it suits you, should I arrange for you to\x01",
            "make a fresh start from Police Academy again?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "Inspectooor, please\x01",
            "anything but thaaat!\x02",
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
    OP_93(0xA, 0xE1, 0x0)
    OP_93(0xB, 0x2D, 0x0)
    SetScenarioFlags(0x13F, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_27_E4C5 end

    def Function_28_E98B(): pass

    label("Function_28_E98B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_EBC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB41")

    ChrTalk(
        0xFE,
        (
            "Hey, listen to this!\x01",
            "They say that Inspector Donovan will\x01",
            "be reinstated to the police very soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had so many hardships filling\x01",
            "in for the hole the Inspector left,\x01",
            "but now I'll finally be free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, I'm glad for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI wonder what the Inspector would do\x01",
            "if he heard you saying such a thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "W-Woops, you're right.\x01",
            "...Keep it a secret, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_EBBE")

    label("loc_EB41")


    ChrTalk(
        0xFE,
        (
            "When the Inspector comes back,\x01",
            "Section Two will have some peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright. Until then, I'll\x01",
            "have to do my best too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EBBE")

    Jump("loc_F460")

    label("loc_EBC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_EBD1")
    Jump("loc_F460")

    label("loc_EBD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_EC97")

    ChrTalk(
        0xFE,
        (
            "Suddenly to be included\x01",
            "in the State Guard without\x01",
            "any prior notice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't say it out loud, but it's\x01",
            "a real nice case of despotism.\x01",
            "...*sigh*, what the heck is going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F460")

    label("loc_EC97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ECA5")
    Jump("loc_F460")

    label("loc_ECA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EDB4")

    ChrTalk(
        0xFE,
        (
            "It seems that the Empire has already\x01",
            "denied to take part in the criminal act, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, somehow they're groping to\x01",
            "be able to have negotiations in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because they're doing such a thing,\x01",
            "there's no doubt they have some kind of aim.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F460")

    label("loc_EDB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EE45")

    ChrTalk(
        0xFE,
        (
            "Where did Wald Wales\x01",
            "get the Gnosis...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hypothetically, if it wasn't via Revache, \x01",
            "through what route did he acquire it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F460")

    label("loc_EE45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EE53")
    Jump("loc_F460")

    label("loc_EE53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F15D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F043")

    ChrTalk(
        0xFE,
        (
            "Aah, you guys.\x01",
            "Thank you very much for yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right, by the way. Last night that\x01",
            "old lady appeared in my dreams.\x01",
            "For some reason, she was chasing me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, thanks to that I\x01",
            "couldn't really sleep.\x02",
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
            "#00006F(Telling us this, somehow I think\x01",
            "we'll be seeing her in our dreams too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F(...Let's do our best and forget her.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_F08E")

    label("loc_F043")


    ChrTalk(
        0xFE,
        (
            "In any case, thank you very\x01",
            "much for yesterday.\x01",
            "You really helped me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F08E")

    Jump("loc_F158")

    label("loc_F093")


    ChrTalk(
        0xFE,
        (
            "*sigh*, yesterday I had\x01",
            "a really unpleasant dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a dream where I was chased by\x01",
            "the grandma I arrested yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*shiver*, rethinking about it,\x01",
            "I'm starting to sweat badly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F158")

    Jump("loc_F460")

    label("loc_F15D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F16B")
    Jump("loc_F460")

    label("loc_F16B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F179")
    Jump("loc_F460")

    label("loc_F179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F187")
    Jump("loc_F460")

    label("loc_F187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F195")
    Jump("loc_F460")

    label("loc_F195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F3A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2EA")

    ChrTalk(
        0xFE,
        (
            "*sigh*, these days the tension\x01",
            "in the HQ keeps being very high.\x01",
            "I really can't standing it anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although pressure from congressmen\x01",
            "and the top brass has decreased for now,\x01",
            "the autonomous state has a heap of problems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wonder when in the world\x01",
            "I'll be able to take it a little easy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_F39B")

    label("loc_F2EA")


    ChrTalk(
        0xFE,
        (
            "Well, at any rate, I can only do\x01",
            "my best as moral support to\x01",
            "Mayor Dieter's political reforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally, I hope we get a salary raise\x01",
            "at the Conference...just kidding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F39B")

    Jump("loc_F460")

    label("loc_F3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3BB")
    Call(0, 27)
    Jump("loc_F460")

    label("loc_F3BB")


    ChrTalk(
        0xFE,
        (
            "*sigh*, once again the Inspector\x01",
            "touched a sore point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too would like to get my\x01",
            "act together a little, but...\x01",
            "It's that I can't change my personality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F460")

    TalkEnd(0xFE)
    Return()

    # Function_28_E98B end

    def Function_29_F464(): pass

    label("Function_29_F464")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F475")
    Jump("loc_FB3C")

    label("loc_F475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F483")
    Jump("loc_FB3C")

    label("loc_F483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F65F")

    ChrTalk(
        0xC,
        (
            "#00600FYou all, huh?\x02\x03",
            "#00603F...I've heard about Orlando.\x01",
            "It seems things have \x01",
            "become really troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, however we'll bring him back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603FHmph, I see.\x01",
            "Then, I've got nothing to say.\x02\x03",
            "#00600FAnyway, this is the situation.\x01",
            "Of course there's a whole load of\x01",
            "work I'd like to push on you too.\x02\x03",
            "For that reason too, go\x01",
            "resolve this colleague\x01",
            "problem at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FMr. Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, of course we will!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 3)
    Jump("loc_F72C")

    label("loc_F65F")


    ChrTalk(
        0xC,
        (
            "#00603FAfter I'm finished with the business meeting,\x01",
            "I intend to head over to the mayor's place to\x01",
            "discuss about countermeasures.\x02\x03",
            "#00600FAnyway, you too, go take care\x01",
            "of what you have to do at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F72C")

    Jump("loc_FB3C")

    label("loc_F731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F73F")
    Jump("loc_FB3C")

    label("loc_F73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F74D")
    Jump("loc_FB3C")

    label("loc_F74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F75B")
    Jump("loc_FB3C")

    label("loc_F75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F826")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F776")
    Call(0, 25)
    Jump("loc_F821")

    label("loc_F776")


    ChrTalk(
        0xC,
        (
            "#00600FWe currently have a huge pile of cases, but...\x01",
            "At any rate, leave the counterespionage to us.\x02\x03",
            "You must only think to carry out\x01",
            "your own duties until the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F821")

    Jump("loc_FB3C")

    label("loc_F826")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F834")
    Jump("loc_FB3C")

    label("loc_F834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FB17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F85C")
    Call(0, 30)
    Jump("loc_F930")

    label("loc_F85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F86E")
    Call(0, 31)
    Jump("loc_F930")

    label("loc_F86E")


    ChrTalk(
        0xC,
        (
            "#00603FAs for me, I intend to stay here for a while to\x01",
            "keep a watchful eye on intel from all quarters.\x02\x03",
            "#00600FIf something happens, you can tell me directly.\x01",
            "Contact me whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F930")

    Jump("loc_FB12")

    label("loc_F935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA9B")

    ChrTalk(
        0xFE,
        (
            "#00603FThe Imperial Army Intelligence Division\x01",
            "and the Republic Rocksmith Agency...\x01",
            "Opponents to not make light of.\x02\x03",
            "If those two were in contact...\x01",
            "It seems there's no doubt that there're\x01",
            "some kind of secret movements.\x02\x03",
            "#00600FAnyway, for now we can only\x01",
            "do what we can as police.\x02\x03",
            "If something happens again,\x01",
            "you can contact me too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_FB12")

    label("loc_FA9B")


    ChrTalk(
        0xFE,
        (
            "#00600FAnyway, for now we can only\x01",
            "do what we can as police.\x02\x03",
            "If something happens again,\x01",
            "you can contact me too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB12")

    Jump("loc_FB3C")

    label("loc_FB17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FB25")
    Jump("loc_FB3C")

    label("loc_FB25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FB33")
    Jump("loc_FB3C")

    label("loc_FB33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FB3C")

    label("loc_FB3C")

    TalkEnd(0xFE)
    Return()

    # Function_29_F464 end

    def Function_30_FB40(): pass

    label("Function_30_FB40")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xC, 0x0)
    OP_4B(0xD, 0x0)
    OP_68(-59230, 1730, 14590, 0)
    MoveCamera(47, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23690, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -59000, 30, 14800, 45)
    SetChrPos(0x102, -58970, 30, 16280, 90)
    SetChrPos(0x104, -57950, 0, 14250, 0)
    SetChrPos(0x109, -59810, 30, 14920, 45)
    SetChrPos(0x105, -59060, 0, 13870, 45)
    OP_93(0xC, 0xE1, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xC,
        "#00600F#2PIt's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P...Do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PYes...there's something we absolutely\x01",
            "must report to Section One.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reported that Kilika and Lechter\x01",
            "showed up in the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#00603F#2P...I see.\x02\x03",
            "Both key figures of the Imperial Army Intelligence\x01",
            "Division and the Rocksmith Agency in the city...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PMr. Dudley, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6P...What do you think about this?\x02\x03",
            "Spies from the two major powers appearing\x01",
            "when the Conference is drawing near tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PIt's a very unlikely coincidence...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHu hu, although they said they're\x01",
            "here for an errand or recreation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PI-It's too suspicious, as you can imagine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2POf course they probably have an axe to grind.\x02\x03",
            "#00600FHowever, if anything I'd say that\x01",
            "you should be able to feel that\x01",
            "since you talked to them directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12P...Indeed, that could be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#2P...And so, I'll ask you, Bannings.\x01",
            "For what reason do you think\x01",
            "they showed up in the city?\x02\x03",
            "#00603FThere should've been some kind of hint in...\x01",
            "...Their conversations, the route they took...\x02\x03",
            "#00600FI don't mind conjectures, so just tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PL-Let's see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "What is the reason Kilika and\x01",
            "Lechter showed up in the city?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "VIPs Security\x01",                # 0
            "A Breather and Shopping\x01",      # 1
            "Private Talks\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_101A0"),
        (1, "loc_10345"),
        (2, "loc_10504"),
        (SWITCH_DEFAULT, "loc_10565"),
    )


    label("loc_101A0")


    ChrTalk(
        0x101,
        (
            "#00001F#6PFor VIPs security, perhaps?\x02\x03",
            "#00003FTo understand Crossbell City\x01",
            "topography in case of an\x01",
            "emergency or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2P...That possibility should be low.\x02\x03",
            "#00600FSecurity is out of spies jurisdiction,\x01",
            "and to begin with, they've been visiting\x01",
            "Crossbell since many months ago.\x02\x03",
            "They have no necessity to check\x01",
            "the city topography now of all times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PI-Indeed, it makes sense...\x02",
    )

    CloseMessageWindow()
    Jump("loc_10565")

    label("loc_10345")


    ChrTalk(
        0x101,
        (
            "#00001F#6P...Could it be really like they said,\x01",
            "to take a breather and do shopping?\x02\x03",
            "#00003FAlthough I can't surely say they\x01",
            "have no need to do it at the time of\x01",
            "attending at the Trade Conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2P...Probably that's not it.\x02\x03",
            "#00600FIf you think they gave you the slip,\x01",
            "it could be just a simple disguise.\x02\x03",
            "#00606F*sigh*, oh boy...\x01",
            "I thought you could've done a little better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PP-Please wait.\x01",
            "Ehhm, then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10565")

    label("loc_10504")

    OP_2C(0xA3, 0x1)

    ChrTalk(
        0x101,
        (
            "#00001F#6P...It's possible they were setting up\x01",
            "an opportunity for private talks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10565")

    label("loc_10565")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105EF")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00001F#6PRight, perhaps...\x01",
            "It's possible they were setting up\x01",
            "an opportunity for private talks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105EF")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10669():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10669)
    Sleep(50)

    def lambda_10679():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10679)
    Sleep(50)

    def lambda_10689():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10689)
    Sleep(50)

    def lambda_10699():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10699)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0xD,
        "#5PPrivate...talks?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00600F#2PHm...why do you think that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PThe very first eyewitness report was\x01",
            "obtained for both at the Waterfront Area.\x02\x03",
            "#00001FBefore we commenced pursuing them,\x01",
            "they both were in the same area...\x01",
            "I can't see that as a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#5PAh...yes, it was like that.\x02\x03",
            "#00100FAt IBC, located at Waterfront Area,\x01",
            "an inspection had been planned by\x01",
            "the President since the day before...\x02\x03",
            "It could've been a convenient place to\x01",
            "meet up with the purpose of private talks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PEven the Michey event that was\x01",
            "going on at that time could've\x01",
            "become a camouflage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PThey met in secret keeping each their\x01",
            "disguise;  taking a brief breather\x01",
            "and shopping for the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P...It seems they're coherent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PAt any rate, even if you say "private talks"...\x01",
            "What did they talk about?\x02\x03",
            "To begin with, shouldn't\x01",
            "the Empire and Republic\x01",
            "be antagonists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5P...It's something unthinkable.\x02\x03",
            "#00103FBecause of the Cult incident, many congressmen\x01",
            "of the Imperial and Republican factions lost\x01",
            "their standing...\x02\x03",
            "With the creation of a cooperative system between\x01",
            "the new mayor and the new chairman, Crossbell\x01",
            "gradually started to have an influential voice.\x02\x03",
            "#00101FSuch a situation...there's no way the Empire\x01",
            "and Republic would leave things like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#12PI see, in that aspect the two major\x01",
            "powers interests coincide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00608F#2PI can't affirm it, but...\x01",
            "It seems without doubt that there're\x01",
            "some kind of secret movements.\x02\x03",
            "#00603F...At present, I can say just this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10CE6():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10CE6)
    Sleep(50)

    def lambda_10CF6():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10CF6)
    Sleep(50)

    def lambda_10D06():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10D06)
    Sleep(50)

    def lambda_10D16():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10D16)
    Sleep(50)

    def lambda_10D26():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10D26)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0xD,
        (
            "#5PSection One will keep\x01",
            "marking Lechter Arundel\x01",
            "and Kilika Rouran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PThank you for your report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PNo, we're glad if it was of help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PTomorrow's conference...\x01",
            "I hope it ends without incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2PFor that too, we can only do\x01",
            "what we can as police, now.\x02\x03",
            "#00601FIf something happens again\x01",
            "you can contact me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_2C(0xA3, 0x1)
    OP_29(0xA3, 0x1, 0xD)
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -59320, 30, 14570, 45)
    SetScenarioFlags(0x1C7, 4)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_30_FB40 end

    def Function_31_10F20(): pass

    label("Function_31_10F20")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x101, 0)

    ChrTalk(
        0xD,
        "Detective Bannings.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        (
            "#00600FIt's you.\x01",
            "Something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, nothing in particular for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603FI see...however, do not\x01",
            "let your guard down.\x02\x03",
            "I think you felt it too, but the\x01",
            "whole city is in a little enlivened\x01",
            "situation for the VIPs visit.\x02\x03",
            "#00600FNo matter how unusual, but\x01",
            "in such atmosphere is\x01",
            "easy to make flukes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FIndeed, you're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, we must\x01",
            "be very vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBy the way, Mr. Dudley,\x01",
            "are you going to stay\x01",
            "here for a while?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "#00603FMore or less. In any case, I plan\x01",
            "to be on duty at HQ until the VIPs\x01",
            "visit to the Arc-en-ciel theatre begins.\x02\x03",
            "#00600FIf something happens, tell me in person.\x01",
            "Contact me whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, roger that.\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_31_10F20 end

    def Function_32_11237(): pass

    label("Function_32_11237")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11248")
    Jump("loc_11341")

    label("loc_11248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11271")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1126C")

    ChrTalk(
        0x11,
        "...Tsk...\x02",
    )

    CloseMessageWindow()

    label("loc_1126C")

    Jump("loc_11341")

    label("loc_11271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1127F")
    Jump("loc_11341")

    label("loc_1127F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_11341")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112A6")
    Call(0, 33)
    Jump("loc_11341")

    label("loc_112A6")

    ClearChrFlags(0x11, 0x10)

    ChrTalk(
        0x11,
        (
            "Since even if you arrest us\x01",
            "you can only give us a fine,\x01",
            "you're too desperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hu hu, does the police want to\x01",
            "earn pocket money that badly?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11341")

    TalkEnd(0xFE)
    Return()

    # Function_32_11237 end

    def Function_33_11345(): pass

    label("Function_33_11345")


    ChrTalk(
        0xF,
        (
            "Well then...\x01",
            "Where are you living\x01",
            "at present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hmph, we have no obligation to answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Although, it's a place common people\x01",
            "like you wouldn't be able to live in...\x01",
            "I'll just tell you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "(S-Shit...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(H-Hang in there, Frantz...)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_33_11345 end

    def Function_34_1145B(): pass

    label("Function_34_1145B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1146C")
    Jump("loc_115AB")

    label("loc_1146C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_114E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_114E3")

    ChrTalk(
        0x12,
        "A suspension, a driving license suspensiooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "And for one month too...\x01",
            "*siiiiiiiiiigh*.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114E3")

    Jump("loc_115AB")

    label("loc_114E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_114F6")
    Jump("loc_115AB")

    label("loc_114F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_115AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_115AB")

    ChrTalk(
        0x12,
        (
            "You guys...\x01",
            "Weren't you who put together the barricade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hmph, what shallow thinking.\x01",
            "If you get carried away too much,\x01",
            "nothing good will come to you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115AB")

    TalkEnd(0xFE)
    Return()

    # Function_34_1145B end

    def Function_35_115AF(): pass

    label("Function_35_115AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_115C0")
    Jump("loc_116CC")

    label("loc_115C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1166B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11666")

    ChrTalk(
        0x13,
        (
            "*sigh*, only this time we\x01",
            "got carried away too much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "The car also got ruined.\x01",
            "It seems it's better to stay\x01",
            "quiet for a little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11666")

    Jump("loc_116CC")

    label("loc_1166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11679")
    Jump("loc_116CC")

    label("loc_11679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_116CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_116CC")

    ChrTalk(
        0x13,
        (
            "*haah*, I want to go home quick.\x01",
            "Inquiries are tiresome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116CC")

    TalkEnd(0xFE)
    Return()

    # Function_35_115AF end

    def Function_36_116D0(): pass

    label("Function_36_116D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11751")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116EE")
    Call(0, 38)
    Jump("loc_1174C")

    label("loc_116EE")


    ChrTalk(
        0xFE,
        (
            "Frankly, I feel like I'm still dreaming, but...\x01",
            "Really, I wonder what's going to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1174C")

    Jump("loc_11A71")

    label("loc_11751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1175F")
    Jump("loc_11A71")

    label("loc_1175F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1176D")
    Jump("loc_11A71")

    label("loc_1176D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1189D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11834")

    ChrTalk(
        0xE,
        (
            "You really did a good job in\x01",
            "managing the runaway car case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please leave these\x01",
            "kids to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If something happens again,\x01",
            "we'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11893")

    label("loc_11834")


    ChrTalk(
        0xE,
        (
            "Please leave these\x01",
            "kids to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If something happens again,\x01",
            "we'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11893")

    Jump("loc_11898")

    label("loc_11898")

    Jump("loc_11A71")

    label("loc_1189D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_118AB")
    Jump("loc_11A71")

    label("loc_118AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_118B9")
    Jump("loc_11A71")

    label("loc_118B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_118C7")
    Jump("loc_11A71")

    label("loc_118C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_118D5")
    Jump("loc_11A71")

    label("loc_118D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_118E3")
    Jump("loc_11A71")

    label("loc_118E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_118F1")
    Jump("loc_11A71")

    label("loc_118F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_118FF")
    Jump("loc_11A71")

    label("loc_118FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_11A71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11A71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A18")
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xE,
        (
            "What you did is a\x01",
            "serious offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "What about reflecting on it a little!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hmph, don't be such a hothead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Reflecting, reflecting...\x01",
            "There, I reflected on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "By the way, I'd like you\x01",
            "let us go already.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_11A6C")

    label("loc_11A18")


    ChrTalk(
        0xE,
        (
            "What you did is a\x01",
            "serious offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "What about reflecting on it a little!?\x02",
    )

    CloseMessageWindow()

    label("loc_11A6C")

    Jump("loc_11A71")

    label("loc_11A71")

    TalkEnd(0xFE)
    Return()

    # Function_36_116D0 end

    def Function_37_11A75(): pass

    label("Function_37_11A75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A93")
    Call(0, 38)
    Jump("loc_11B51")

    label("loc_11A93")


    ChrTalk(
        0xFE,
        (
            "Nevertheless...\x01",
            "That President's speech seemed\x01",
            "like a proclamation of war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though we have the State Guard,\x01",
            "I can't think like they'd be able to\x01",
            "oppose the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B51")

    Jump("loc_11DCF")

    label("loc_11B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11B64")
    Jump("loc_11DCF")

    label("loc_11B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11C45")

    ChrTalk(
        0xFE,
        (
            "At last the night has passed, but...\x01",
            "The situation is only growing worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, although I'm from the District\x01",
            "Crime Prevention Section, from now on \x01",
            "I plan to focus even more on what I can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DCF")

    label("loc_11C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11D0E")

    ChrTalk(
        0xF,
        (
            "It's still hard to say that we\x01",
            "have become able to manage\x01",
            "foreigners strictly, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This case too, is an important step.\x01",
            "Even us police must do our\x01",
            "best without getting down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DCF")

    label("loc_11D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11D1C")
    Jump("loc_11DCF")

    label("loc_11D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11D2A")
    Jump("loc_11DCF")

    label("loc_11D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11D38")
    Jump("loc_11DCF")

    label("loc_11D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11D46")
    Jump("loc_11DCF")

    label("loc_11D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11D54")
    Jump("loc_11DCF")

    label("loc_11D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11D62")
    Jump("loc_11DCF")

    label("loc_11D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11D70")
    Jump("loc_11DCF")

    label("loc_11D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_11DCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D8B")
    Call(0, 33)
    Jump("loc_11DCF")

    label("loc_11D8B")

    ClearChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "(Where're these guys' bad\x01",
            "personalities coming from...!?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DCF")

    TalkEnd(0xFE)
    Return()

    # Function_37_11A75 end

    def Function_38_11DD3(): pass

    label("Function_38_11DD3")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(
        0xE,
        (
            "Ah, Lloyd.\x01",
            "What a serious situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "Did you hear anything\x01",
            "at the Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, no, nothing...\x02\x03",
            "#00001FWe're still waiting for the Chief\x01",
            "to contact us with the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I understand, it's the same here at the\x01",
            "District Crime Prevention Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It appears we're going to have a specific\x01",
            "notification as soon as the Conference ends, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Really, we can't fathom at\x01",
            "all what's going to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "In any case, we can only follow\x01",
            "the course of events...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Guys, you seem to be acting\x01",
            "somehow on your own terms...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "How should I put it, be careful\x01",
            "to not attract the attention of\x01",
            "the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x18F, 6)
    Return()

    # Function_38_11DD3 end

    def Function_39_120A7(): pass

    label("Function_39_120A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_120B8")
    Jump("loc_1287A")

    label("loc_120B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_120C6")
    Jump("loc_1287A")

    label("loc_120C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1224E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121CF")

    ChrTalk(
        0xFE,
        (
            "The police force has been split\x01",
            "in half. One part is on standby\x01",
            "as support personnel for the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other part will have to act\x01",
            "to strengthen city patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right because these are hard times,\x01",
            "we must support one another.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_12249")

    label("loc_121CF")


    ChrTalk(
        0xFE,
        (
            "We can't make only the \x01",
            "CGF shed blood, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What good is the police if we \x01",
            "can't help during hard times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12249")

    Jump("loc_1287A")

    label("loc_1224E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12303")

    ChrTalk(
        0xFE,
        (
            "They're troublesome kids,\x01",
            "but today they're replying\x01",
            "relatively obediently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems Kate was crying in a thundering voice...\x01",
            "Maybe that had a great effect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287A")

    label("loc_12303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12314")
    Call(0, 40)
    Jump("loc_1287A")

    label("loc_12314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12322")
    Jump("loc_1287A")

    label("loc_12322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12330")
    Jump("loc_1287A")

    label("loc_12330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1233E")
    Jump("loc_1287A")

    label("loc_1233E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_123E9")

    ChrTalk(
        0xFE,
        (
            "Well, the unveiling ceremony is over\x01",
            "and I can finally take a small breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*phew*, as expected, nothing is\x01",
            "better than coffee for a short rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287A")

    label("loc_123E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_123F7")
    Jump("loc_1287A")

    label("loc_123F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_12495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12412")
    Call(0, 26)
    Jump("loc_12490")

    label("loc_12412")


    ChrTalk(
        0xFE,
        (
            "Uhhm, that too could be called\x01",
            "self-assertion, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't the party who suffers trouble\x01",
            "the one who bears it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12490")

    Jump("loc_1287A")

    label("loc_12495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1287A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12731")

    ChrTalk(
        0xFE,
        (
            "Ooh, it's you. There're some new faces,\x01",
            "but you're still the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Does it mean that you're finally\x01",
            "going to resume activities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank goodness it's like you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHm, I presume you're the Section Chief of\x01",
            "the District Crime Prevention Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FPleased to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, at any rate, this looks like quite\x01",
            "the interesting ensemble of talented persons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at all events, they're expecting\x01",
            "great things from you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on you'll have to go over your\x01",
            "section fence and work non-stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 3)
    Jump("loc_1287A")

    label("loc_12731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_127BB")

    ChrTalk(
        0x14,
        (
            "Hmm, even so, some troublesome\x01",
            "kids have arrived, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well, it should be fine leaving\x01",
            "them to Kate and Frantz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1287A")

    label("loc_127BB")


    ChrTalk(
        0xFE,
        (
            "*phew*, after I drink this, I'll have\x01",
            "to go back to a meeting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Boy oh boy, these days I have to put up with a meeting\x01",
            "after the other with my body on the verge of retirement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1287A")

    TalkEnd(0xFE)
    Return()

    # Function_39_120A7 end

    def Function_40_1287E(): pass

    label("Function_40_1287E")

    OP_4B(0x14, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)

    ChrTalk(
        0x14,
        (
            "When trains from the Republic region come,\x01",
            "we'll have to deal again with transfers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "You, from now on, are to be heading as\x01",
            "support at the station and airport.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Sir, roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "We'll head to the sites at once.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_40_1287E end

    def Function_41_1297C(): pass

    label("Function_41_1297C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12A62")

    ChrTalk(
        0xFE,
        (
            "As the District Crime Prevention Section,\x01",
            "we have resumed patrols in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's also the possibility that the big confusion\x01",
            "effects the worsening of public security.\x01",
            "We must patrol being careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B51")

    label("loc_12A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12A70")
    Jump("loc_12B51")

    label("loc_12A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_12B45")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking I could\x01",
            "have a break after finally restoring HQ,\x01",
            "we got included in the State Guard...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I'm a soldier...\x01",
            "As you can expect, I \x01",
            "can't accept it meekly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B51")

    label("loc_12B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12B51")
    Call(0, 40)

    label("loc_12B51")

    TalkEnd(0xFE)
    Return()

    # Function_41_1297C end

    def Function_42_12B55(): pass

    label("Function_42_12B55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12C12")

    ChrTalk(
        0xFE,
        (
            "Section Chief Joe Ridge headed to\x01",
            "the Police Academy to deal with the\x01",
            "aftermath after the State Guard left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "With the Section Chief away, we must guard the place.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D2B")

    label("loc_12C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12C20")
    Jump("loc_12D2B")

    label("loc_12C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_12CF5")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking I could\x01",
            "have a break after finally restoring HQ,\x01",
            "we got included in the State Guard...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I'm a soldier...\x01",
            "As you can expect, I \x01",
            "can't accept it meekly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D2B")

    label("loc_12CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12D03")
    Jump("loc_12D2B")

    label("loc_12D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12D11")
    Jump("loc_12D2B")

    label("loc_12D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12D1F")
    Jump("loc_12D2B")

    label("loc_12D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12D2B")
    Call(0, 40)

    label("loc_12D2B")

    TalkEnd(0xFE)
    Return()

    # Function_42_12B55 end

    def Function_43_12D2F(): pass

    label("Function_43_12D2F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think you've already heard about it, but\x01",
            "it was decided for the police to be reshuffled \x01",
            "into a unique organisation of the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At present, an explanation about the\x01",
            "system from now on to all the responsible\x01",
            "parties is underway in the 2F meeting room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please wait in the detached building\x01",
            "until instructions from the top come.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_12D2F end

    def Function_44_12E9F(): pass

    label("Function_44_12E9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-950, 1500, 7780, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21800, 0)
    SetChrPos(0x101, -900, 40, 1900, 0)
    SetChrPos(0x102, 300, 40, 1900, 0)
    SetChrPos(0x103, -900, 40, 700, 0)
    SetChrPos(0x104, 300, 40, 700, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)

    def lambda_12F2A():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12F2A)
    Sleep(50)

    def lambda_12F47():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12F47)
    Sleep(50)

    def lambda_12F64():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12F64)
    Sleep(50)

    def lambda_12F81():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12F81)
    Sleep(50)
    SetCameraDistance(25000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Ah, everyone...\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)

    ChrTalk(
        0x15,
        "Oh...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-350, 1540, 12250, 0)
    SetCameraDistance(19950, 0)
    SetChrPos(0x15, 1000, 0, 13400, 180)
    SetChrPos(0x101, 0, 40, 11800, 0)
    SetChrPos(0x102, 2000, 40, 11800, 0)
    SetChrPos(0x103, -200, 40, 10300, 0)
    SetChrPos(0x104, 2200, 40, 10300, 0)
    OP_0D()

    ChrTalk(
        0x15,
        (
            "You are the people of the\x01",
            "Special SUpport Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think you've already heard about it, but\x01",
            "it was decided for the police to be reshuffled \x01",
            "into a unique organisation of the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "At present, an explanation about the\x01",
            "system from now on to all the responsible\x01",
            "parties is underway in the 2F meeting room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone, please wait in the detached building\x01",
            "until instructions from the top come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FY-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You're still free to move on 1F, but please\x01",
            "refrain from any unnecessary behaviour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please understand that you can\x01",
            "be taken into custody in case your\x01",
            "behaviour is deemed suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FR-Roger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F(Somehow he's really coercive...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F(Yeah, but it's extremely unlikely\x01",
            "someone will ineptly defy him.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrPos(0x15, 2990, 0, 11810, 270)
    SetScenarioFlags(0x18F, 7)
    ClearMapFlags(0x10000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_44_12E9F end

    def Function_45_133C3(): pass

    label("Function_45_133C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch02502.itc", 0x24)
    LoadChrToIndex("chr/ch30102.itc", 0x25)
    LoadChrToIndex("chr/ch30302.itc", 0x26)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis312.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis404.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -62750, 150, 16149, 0)
    SetChrPos(0x102, -65000, 150, 16149, 0)
    SetChrPos(0x104, -65000, 150, 19900, 180)
    SetChrPos(0x109, -67250, 150, 19900, 180)
    SetChrPos(0x105, -67250, 150, 16149, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0xF)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -57600, 0, 18000, 270)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x2)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x4)
    SetChrPos(0x19, -60500, 150, 16149, 0)
    OP_4B(0x14, 0xFF)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, -62750, 150, 19900, 180)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -60500, 150, 19900, 180)
    SetMapObjFrame(0xFF, "isu", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu_sd", 0x0, 0x1)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_78(0x3, 0x1A)
    OP_78(0x4, 0x1B)
    OP_78(0x5, 0x1C)
    OP_78(0x6, 0x1D)
    OP_78(0x7, 0x1E)
    OP_78(0x8, 0x1F)
    OP_78(0x9, 0x20)
    OP_78(0xA, 0x21)
    OP_49()
    SetChrPos(0x1A, -60500, 0, 15900, 0)
    OP_D5(0x1A, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1B, -60500, 0, 20100, 0)
    OP_D5(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1C, -62750, 0, 15900, 0)
    OP_D5(0x1C, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1D, -62750, 0, 20100, 0)
    OP_D5(0x1D, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x1E, -65000, 0, 15900, 0)
    OP_D5(0x1E, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x1F, -65000, 0, 20100, 0)
    OP_D5(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x20, -67250, 0, 15900, 0)
    OP_D5(0x20, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x21, -67250, 0, 20100, 0)
    OP_D5(0x21, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(-62500, 2200, 18000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Then──\x01",
            "The day before, VIPs from all countries were going to come\x01",
            "to Crossbell and Orchis Tower presented to the public.\x02\x03",
            "The Support Section members were called to the\x01",
            "counter-measures meeting at police headquarters.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(-62500, 1200, 18000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "──All that I said will make\x01",
            "the security system for the\x01",
            "Trade Conference...\x02\x03",
            "...For the next three days starting\x01",
            "tomorrow.\x02\x03",
            "An inspection system\x01",
            "has been already widely\x01",
            "imposed by the CGF...\x02\x03",
            "To the state borders of\x01",
            "Bellguard Gate and Tangram Gate.\x02\x03",
            "Regarding the city──\x01",
            "Section Chief Joe Ridge,\x01",
            "Inspector Donovan.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetChrSubChip(0x14, 0x0)
    Sleep(250)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x19, 0x0)

    ChrTalk(
        0x14,
        (
            "#5PYes. At the District Crime Prevention Section\x01",
            "all personnel will make patrols in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PUntil the conference ends, we'll be on full operation.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#5PAs for Section Two, we'll especially mainly guard\x01",
            "the train station, airport and commercial areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWe too will use all our personnel\x01",
            "until the conference is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FFurthermore, the security countermeasures\x01",
            "headquarters will be run by Section One.\x02\x03",
            "#00600FI'm self-confident that we can cope up\x01",
            "with every possible emergencies, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x2)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)

    ChrTalk(
        0x19,
        (
            "#12P#01003F...No matter how rigorous a security system is,\x01",
            "not one is absolutely perfect.\x02\x03",
            "#01000FAnd so that's where we come in, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00604FYes. Like I told you, I wish for Section Chief \x01",
            "Sergei to be on duty at the counter-measures \x01",
            "HQ in charge of public relations.\x02\x03",
            "#00602FAnd to take charge of communications\x01",
            "with the Crossbell Guardian Force too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#12P#01006FMan, you drive your men hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHa ha, at any rate, you have your\x01",
            "nose stuck in many different things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAnd you established a profitable investigation\x01",
            "structure in a way that covered a blind spot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PHm, hm.\x01",
            "You really lived up to your reputation\x01",
            "of "Sergei The Rear".\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    Sleep(300)

    ChrTalk(
        0x19,
        "#12P#01005FPlease, leave that old story be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002F"Sergei The Rear"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F*giggle*...\x01",
            "A fitting name.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x1)
    Sleep(300)

    ChrTalk(
        0x19,
        "#11P#01006FIt's an old story, old.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x19, 0x2)
    Sleep(200)

    ChrTalk(
        0x19,
        (
            "#12P#01000FSo...\x01",
            "Are you fine with these guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FYes, I don't mind.\x02\x03",
            "#00600FI think we'll use them as reserve\x01",
            "corps for a little while.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FReserve corps...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FWe'll keep doing our usual support\x01",
            "activities, but if something comes up,\x01",
            "we'll be shifted to back up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00606FYeah, exactly that.\x02\x03",
            "It's the same with the Bracer Guild, \x01",
            "but we can't fully rely on them.\x02\x03",
            "#00601FAlso...\x01",
            "Since those guys entered Crossbell,\x01",
            "I want an insurance for unforeseen situations.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)

    ChrTalk(
        0x102,
        "#6P#00108FThose guys...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F──The "Red Constellation", right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#00601FYeah...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "#00603FThe "Red Constellation" jaeger corps...\x02\x03",
            "Said to be one of the strongest jaeger\x01",
            "corps of the western Zemuria continent.\x02\x03",
            "#00601FAt present, it has been confirmed\x01",
            "that many of its members have\x01",
            "entered Crossbell.\x02\x03",
            "It also appears that, about one year ago, \x01",
            "they engaged in a large-scale conflict \x01",
            "with the "Heiyue" in the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    ChrTalk(
        0x14,
        "#5PHmm, dangerous guys they're.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PSo it means that they plan to continue\x01",
            "their conflict with the Heiyue in this city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FNo. Basically, jaegers are a bunch\x01",
            "of people who acts moved by mira.\x02\x03",
            "Although they had a quarrel with them before,\x01",
            "it doesn't mean it's a reason to have another.\x02\x03",
            "#00600FIsn't that right, Orlando?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F──I guess.\x02\x03",
            "#00303FDifferently from the mafia that takes\x01",
            "territoriality seriously, to jaegers\x01",
            "mira and battlefields are everything.\x02\x03",
            "Yesterday's enemy is today's ally...\x01",
            "That can also be an everyday occurrence.\x02\x03",
            "#00300FIn that sense, they probably aren't\x01",
            "draggin' on the previous conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10304FHu hu, if that's the case,\x01",
            "a mystery arises, right?\x02\x03",
            "#10302FAnd that's why the "Red Constellation"\x01",
            "has entered Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11P#00606FAlthough Section One is investigating that,\x01",
            "we haven't been able to confirm their goals yet.\x02\x03",
            "#00601FHowever, it seems certain that they're receiving\x01",
            "backing from the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FThey could be trying to do something\x01",
            "related to the Trade Conference...\x02\x03",
            "#00101FMaybe their aim is to suppress the\x01",
            "rise of the Republicans "Heiyue"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01006FWell, all it's possible.\x02\x03",
            "#01000FAt any rate, there's no mistake that\x01",
            "they're an element that can't be\x01",
            "ignored for the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FYes, naturally.\x02\x03",
            "#00600F──By the way, although they're the "Red\x01",
            "Constellation", it appears they've been stretching\x01",
            "their legs in Crossbell City environs many times.\x02\x03",
            "In case you're going around many places, I also \x01",
            "want you to investigate about their movements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F──Acknowledged.\x02\x03",
            "#00001FThen, while dealing with support requests,\x01",
            "we'll gather intel about the "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(50)
    SetChrSubChip(0x14, 0x0)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#6P#00100FIf anything happens we'll\x01",
            "go back up where necessary,\x01",
            "so please contact us anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PYeah, I'll be counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PI'll count on you as much as I can.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_E5(0xA)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
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
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_133C3 end

    def Function_46_14C94(): pass

    label("Function_46_14C94")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-690, 1400, 7180, 0)
    MoveCamera(34, 9, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0x101, -900, 40, 1900, 0)
    SetChrPos(0x102, 300, 40, 1900, 0)
    SetChrPos(0x109, -900, 40, 700, 0)
    SetChrPos(0x105, 300, 40, 700, 0)

    def lambda_14D17():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D17)
    Sleep(50)

    def lambda_14D34():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14D34)
    Sleep(50)

    def lambda_14D51():
        OP_98(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14D51)
    Sleep(50)

    def lambda_14D6E():
        OP_98(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14D6E)
    Sleep(50)
    SetCameraDistance(20430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "My, everyone.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x9,
        "#5P#01902FAh, everyone, big sis!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FGeez, didn't I tell you that calling me\x01",
            ""big sis" on the workplace is a no?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-900, 1540, 13080, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17870, 0)
    SetChrPos(0x101, -900, 40, 12200, 0)
    SetChrPos(0x102, 300, 40, 11800, 0)
    SetChrPos(0x109, -1200, 40, 10800, 0)
    SetChrPos(0x105, 500, 40, 10600, 0)

    def lambda_14EED():
        OP_98(0x101, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14EED)
    Sleep(50)

    def lambda_14F0A():
        OP_98(0x102, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14F0A)
    Sleep(50)

    def lambda_14F27():
        OP_98(0x109, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14F27)
    Sleep(50)

    def lambda_14F44():
        OP_98(0x105, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14F44)
    Sleep(50)
    TurnDirection(0x9, 0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha, thank you for your\x01",
            "hard work, Miss Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FLong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhuhu. The Special Support\x01",
            "Section is restarting, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are you starting with the\x01",
            "support requests immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, since we have new members, we'll\x01",
            "do them while patrolling around the city.\x02\x03",
            "We received a request from Section One.\x01",
            "Could you tell us where Miss Emma is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "She is in the conference room over there, waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A collaboration request from Section One...\x01",
            "Everyone, you have made a name for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, somehow I am deeply moved.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FNo, no way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, although it would be nice if we\x01",
            "wouldn't be forced some unreasonable demand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FHonestly, Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FA-Anyway, let's try listening to\x01",
            "what Miss Emma have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#01909FPlease do your best.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x130, 0)
    OP_29(0x66, 0x1, 0x0)
    SetChrPos(0x0, -350, 0, 12250, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_46_14C94 end

    def Function_47_15306(): pass

    label("Function_47_15306")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-57410, 1500, 17030, 0)
    MoveCamera(47, 35, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, -56800, 0, 17250, 0)
    SetChrPos(0x102, -57800, 0, 17000, 0)
    SetChrPos(0x109, -56800, 0, 16000, 0)
    SetChrPos(0x105, -57800, 0, 15750, 0)
    OP_4B(0xD, 0xFF)
    OP_93(0xD, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "So you're here...\x01",
            "Detective Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FG-Good morning, Miss Emma.\x01",
            "Thank you for all you did for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you mean the training at Section One,\x01",
            "it wasn't my intention to aid you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After all, I was just following\x01",
            "Mr. Dudley's orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The conditions weren't bad, but...\x01",
            "I'm at a loss to understand the fact that you refused an\x01",
            "invitation to Section One and went back to the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FI-I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105F(It looks like many things happened...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100F(It's true that in the case of Mr. Lloyd,\x01",
            "even other sections seem to want him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, well, let's forget it.\x01",
            "I'll immediately get to the point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Can I think that the fact \x01",
            "you came here means that\x01",
            "you are going to help us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes, naturally.\x02\x03",
            "#00001F...It seems that Lechter\x01",
            "Arundel has entered\x01",
            "Crossbell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "At Section One, we grasped that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...However, we haven't being able\x01",
            "to definitely confirm it until now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FWhat do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FIs it that you can't confirm\x01",
            "his whereabouts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the first place, the intel saying that\x01",
            "he entered Crossbell is uncertain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We have pseudo eyewitness reports...\x01",
            "However, when we try to track him down,\x01",
            "he becomes dim like a heat haze...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think that he's probably sensing\x01",
            "our moves and escaping seizure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013F...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FH-He's an incredible person.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, considering the guy he is,\x01",
            "it seems he'd be able to do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, I want you to confirm\x01",
            "if Lechter Arundel being here\x01",
            "is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Has he really entered Crossbell?\x01",
            "Or is it some kind of camouflaged intel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If possible, I also want to ask you to\x01",
            "confirm his identity as an Imperial Army\x01",
            "officer and Imperial government secretary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F...Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FHowever, why us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You came in contact with "him"\x01",
            "many times previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I decided to gamble on that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00012FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, despite being an elite, your\x01",
            "response is unexpectedly flexible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Gh...it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If I split our forces we could capture him, but\x01",
            "if handled poorly it could become a diplomatic issue.\x01",
            "I have to take into consideration even that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...If Mr. Dudley were here,\x01",
            "I wouldn't have asked you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FNow that you mention it...\x01",
            "Where is Mr. Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Last evening he headed to the Liberl\x01",
            "region for a security meeting\x01",
            "about the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I think he'll be back tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FHe seems to be busy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's why I want to have this cleared up\x01",
            "somehow before he comes back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "He's a person who'd end up undertaking\x01",
            "it even if a lot tired from a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FI-Indeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FRight, Mr. Dudley is\x01",
            "likely to be doing that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FAll right.\x01",
            "Let us undertake it then.\x02\x03",
            "#00000FIn any case...\x01",
            "Do you know where Captain\x01",
            "Lechter was spotted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let's see...\x01",
            "I don't know if it's true or false...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But we have intel saying that he\x01",
            "was seen at the "Back Street".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FBack Street...\x01",
            "Nearby where Revache was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHu hu, likely, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FUnderstood.\x01",
            "We'll go investigating at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Since I'll be on standby at Section One,\x01",
            "please call me at the reception for your report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Then, if you'll excuse me.\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_161FF():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_161FF)

    def lambda_1620C():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1620C)

    def lambda_16219():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16219)

    def lambda_16226():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16226)
    OP_68(-57500, 1500, 16430, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_16278():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16278)

    def lambda_16285():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16285)

    def lambda_16292():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16292)

    def lambda_1629F():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1629F)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#11P#00006F*phew*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt seems she did a lot for you during\x01",
            "your training at Section One, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah. She's very strict, but she\x01",
            "taught me carefully and thoroughly.\x02\x03",
            "#00004FHow to say...\x01",
            "I think she's too serious a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FEh eh, she looks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, girls like that\x01",
            "seek comfort.\x02\x03",
            "#10302FHu hu, perhaps should I try inviting\x01",
            "her out to drink tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FListen now...\x02\x03",
            "#00000FIn any case, let's give it a try\x01",
            "and search for Mr. Lechter.\x02\x03",
            "We start with the Back Street first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYes, let's go.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Empire Secretary Identity Check]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x130, 1)
    OP_29(0x66, 0x1, 0x1)
    SetChrPos(0x0, -56800, 0, 17500, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_47_15306 end

    def Function_48_16582(): pass

    label("Function_48_16582")

    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(400)
    Sound(104, 0, 100, 0)
    Return()

    # Function_48_16582 end

    def Function_49_16595(): pass

    label("Function_49_16595")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, -57300, 0, 18750, 180)
    OP_4B(0xD, 0xFF)
    OP_68(-57300, 1500, 17520, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -56800, 0, 17250, 0)
    SetChrPos(0x102, -57800, 0, 17000, 0)
    SetChrPos(0x109, -56800, 0, 16000, 0)
    SetChrPos(0x105, -57800, 0, 15750, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "──Good job.\x01",
            "It seems you came to know many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes, I didn't think to be able to even \x01",
            "easily confirm he's someone from \x01",
            "the intelligence agency...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...With what we know, I'm\x01",
            "confident that he isn't\x01",
            "restricted to intel activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At any rate, with this we were even able to\x01",
            "generally understand his staying period...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It appears you have produced more\x01",
            "results than I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha...\x01",
            "To think you're saying that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, it was worthy for a certain someone\x01",
            "to put her body on the line for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00113FI-I didn't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "At any rate, I'm also worried about\x01",
            "the girl who was accompanying him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Did you feel she was someone like an\x01",
            "intelligence subordinate of Captain Lechter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...No, I think she wasn't.\x02\x03",
            "#00008FShe was too young to be in the Intelligence\x01",
            "and she was too much simple-minded.\x02\x03",
            "#00001FAlthough she didn't look like\x01",
            "a normal civilian too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F...Right.\x01",
            "Her motions too were nimble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "──I understand.\x01",
            "About that girl...I'll let the people of\x01",
            "Section One to catch her movements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, I'll excuse myself.\x01",
            "Thank you very much for what you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, if something comes up again,\x01",
            "please feel free to contact us.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_16B56():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16B56)

    def lambda_16B63():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16B63)

    def lambda_16B70():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16B70)

    def lambda_16B7D():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16B7D)
    OP_68(-57300, 1500, 16880, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_16BCF():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16BCF)

    def lambda_16BDC():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16BDC)

    def lambda_16BE9():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16BE9)

    def lambda_16BF6():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16BF6)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00006F*phew*...\x01",
            "Somehow we answered her expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F...*sigh*, you're right...\x02\x03",
            "#00108FNevertheless, that girl...\x01",
            "I wonder who she really is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FRight...\x01",
            "We were easily deceived, but I can't\x01",
            "think she was a normal traveller.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAn innocent and rampant girl accompanying\x01",
            "a major power intelligence officer, eh...?\x02\x03",
            "#10304FHu hu, pretty pretty interesting.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Empire Secretary Identity Check]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x66, 0x1, 0x5)
    OP_29(0x66, 0x1, 0x6)
    OP_29(0x66, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x3)
    SetChrPos(0x0, -56800, 0, 17500, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_49_16595 end

    def Function_50_16E23(): pass

    label("Function_50_16E23")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(-4980, 1900, 10000, 0)
    MoveCamera(27, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20960, 0)
    SetChrPos(0x101, -5180, 0, 11860, 90)
    SetChrPos(0x102, -5660, 0, 10860, 90)
    SetChrPos(0x109, -6640, 0, 11950, 90)
    SetChrPos(0x105, -7250, 0, 10910, 90)
    OP_68(-1640, 1900, 10930, 3000)

    def lambda_16EB6():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16EB6)
    Sleep(50)

    def lambda_16ED3():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16ED3)
    Sleep(50)

    def lambda_16EF0():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16EF0)
    Sleep(50)

    def lambda_16F0D():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16F0D)
    Sleep(300)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "Ah...people from the Support Section,\x01",
            "it appears you have finished your job.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-710, 1500, 13250, 1500)
    MoveCamera(43, 24, 0, 1500)

    def lambda_16FF3():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16FF3)
    Sleep(50)

    def lambda_17010():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17010)
    Sleep(50)

    def lambda_1702D():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1702D)
    Sleep(50)

    def lambda_1704A():
        OP_97(0xFE, 0x3E8, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1704A)
    WaitChrThread(0x101, 1)

    def lambda_17068():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17068)
    WaitChrThread(0x109, 1)

    def lambda_17079():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17079)
    WaitChrThread(0x102, 1)

    def lambda_1708A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1708A)
    WaitChrThread(0x105, 1)

    def lambda_1709B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1709B)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00002FYes, we just finished\x01",
            "our report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, for now the\x01",
            "case is closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think that a lot of requests are going to be\x01",
            "dropped to the restarted Support Section\x01",
            "from now on, so please, do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FThank you very much,\x01",
            "Miss Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAs a new member, I'm\x01",
            "still immature, but..\x01",
            "Somehow, I want to do my best.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "By the way, everyone.\x01",
            "Have you been using your new Combat Notebook?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Lloyd, you should have received it\x01",
            "when you were training at Section One...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAh, now that you mention it...\x01",
            "Yes, I'm using it.\x02\x03",
            "#00004FWhen the information in the\x01",
            "notebook increase, it's ok to\x01",
            "report to you, Miss Rebecca?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, if you do that, you will be a real help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In particular, recently there has been an increase \x01",
            "trend of reports about new type monsters too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What we want is as much information as possible to grasp\x01",
            "their actual conditions and for security measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please, I am counting on you.\x01",
            "You will be gradually awarded some\x01",
            "compensation as it has been until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FTo some extent, it seems it would\x01",
            "be better to drop by periodically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, I will be waiting for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also...there is another thing\x01",
            "I have to inform you all about.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's about the terminals data you\x01",
            "discovered during the Cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It appears that the other day there was\x01",
            "finally the possibility to analyse it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#00105FR-Really!?\x02",
    )

    CloseMessageWindow()

    def lambda_176EE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_176EE)
    Sleep(50)

    def lambda_176FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_176FE)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10305FHm, what're you talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_1773C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1773C)
    Sleep(50)

    def lambda_1774C():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1774C)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003F...At the time of that Cult incident,\x01",
            "we obtained certain data from the\x01",
            "terminals at "The Fort of Sun".\x02\x03",
            "It's data believed to have been\x01",
            "recorded by Joachim Gｸnther\x01",
            "himself about the "D∴G Cult".\x02\x03",
            "#00008FBecause it was impossible to decipher because\x01",
            "part of the sentences were intentionally\x01",
            "deleted, it was sent to forensics...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00001FCould it be that it has been possible\x01",
            "to restore the deleted parts?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17912():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17912)
    Sleep(50)

    def lambda_17922():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17922)
    Sleep(50)

    def lambda_17932():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_17932)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "No, but according to forensics,\x01",
            "it appears that there are still\x01",
            "some chances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Fragments of the damaged\x01",
            "data in those Memory Quartz\x01",
            "were still present, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say that to completely analyze them\x01",
            "will take a considerable amount of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FI see...\x02\x03",
            "#10108FI thought that we had finally been\x01",
            "able to understand an unclear\x01",
            "part of that incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...For now, it seems we\x01",
            "can only wait patiently.\x02\x03",
            "#00000FThank you for letting us know,\x01",
            "Miss Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Uh uh, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ask me, I can let\x01",
            "you check the terminals\x01",
            "data whenever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After there has been progress in the\x01",
            "analysis, I will inform you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYes, please.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    SetScenarioFlags(0x130, 7)
    ModifyEventFlags(0, 1, 0x80)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_50_16E23 end

    def Function_51_17C34(): pass

    label("Function_51_17C34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-124920, 1500, 15840, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    LoadChrToIndex("chr/ch44102.itc", 0x1E)
    LoadChrToIndex("chr/ch47500.itc", 0x1F)
    LoadChrToIndex("chr/ch23600.itc", 0x20)
    LoadChrToIndex("chr/ch30100.itc", 0x21)
    LoadChrToIndex("chr/ch30002.itc", 0x22)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xE, -34500, 0, 18310, 180)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -122270, 100, 16550, 270)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -121780, 0, 18250, 225)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -121570, 0, 14770, 315)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -125880, 0, 12690, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xF, -125000, 100, 16550, 90)
    SetChrPos(0x101, -35350, 0, 16000, 0)
    SetChrPos(0x102, -34150, 0, 16000, 0)
    SetChrPos(0x109, -35350, 0, 14800, 0)
    SetChrPos(0x105, -34150, 0, 14800, 0)
    OP_4B(0x14, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "Well then, because I'm going to take an official\x01",
            "statement, could you answer my questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Uhhm, what are your names?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "John Doe. ("fiddle fiddle")\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "John Smith. ("scratch scratch")\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmph, do we have any obligation\x01",
            "to reply to a guy like you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "Y-You!!\x01",
            "Stop screwing around already...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Now now, Frantz.\x01",
            "Calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Pfft, you've been admonished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Lame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Oh boy, mere ordinary people...\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-35670, 1800, 15820, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20190, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10101F...We're punishing them\x01",
            "only with a fine!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "...Unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's true that regulations concerning\x01",
            "traffic were adjusted a minimum in\x01",
            "autonomous state law, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Since they're Republicans,\x01",
            "we can't deal with them severely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Today they'll receive a stern warning,\x01",
            "and they'll probably be released immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...As expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHm, it seems you were expecting\x01",
            "this to a certain extent?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18197():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18197)
    Sleep(50)

    def lambda_181A7():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_181A7)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00108F...Something like this\x01",
            "has already happened once.\x02\x03",
            "At the time of the fake brand trader incident,\x01",
            "she was only given a reprimand and an expulsion\x01",
            "order from the autonomous state of one month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FNow that you mention it...\x01",
            "Something like that happened too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...After "uncle" became the new mayor,\x01",
            "activities to reform autonomous state \x01",
            "law have increased too, however...\x02\x03",
            "Even so, there're untouched parts yet,\x01",
            "and many are still the same.\x02\x03",
            "#00101FEven the fact that a strong hand can't be taken\x01",
            "against foreigners can be said to be one of the\x01",
            ""distortions" Crossbell had had for many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FHm, oh boy...\x02\x03",
            "Then I guess that this\x01",
            "matter is going to turn\x01",
            "into a vain effort?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F...No, it won't.\x02\x03",
            "#00000FThe same thing happened many\x01",
            "times until now, but what was\x01",
            "done wasn't in vain at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even in this case I think\x01",
            "it hasn't been in vain.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18541():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18541)
    Sleep(50)

    def lambda_18551():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18551)
    Sleep(100)

    ChrTalk(
        0xE,
        (
            "At least, for today there aren't any\x01",
            "more runaway vehicles around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I think that from now on we'll\x01",
            "have to confront with such "barriers".\x02\x03",
            "#00000FThat's exactly why I think\x01",
            "it's very important to face\x01",
            "them without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYou're right...\x01",
            "I must do my best too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThen, I guess I'll try to\x01",
            "conduct myself in as\x01",
            "cool a way as possible.\x02\x03",
            "#10302FIn order to not make you go wild,\x01",
            "since you guys are too much passionate.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00106FOh, Wazy...\x01",
            "We finally wrapped this nicely\x01",
            "and you throw a wet banket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F...O-Oh, well.\x02\x03",
            "#00000FThen, senior Kate...\x01",
            "Can we leave the rest to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You really helped us today.\x01",
            "If something comes up again,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes, we look forward to it.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Runaway Vehicle Crackdown]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x69, 0x1, 0x0)
    OP_29(0x69, 0x1, 0x1)
    OP_29(0x69, 0x4, 0x10)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0x14, 0x40)
    OP_4C(0x14, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -34750, 0, 15400, 180)
    EventEnd(0x5)
    Return()

    # Function_51_17C34 end

    def Function_52_18978(): pass

    label("Function_52_18978")

    EventBegin(0x0)
    Fade(500)
    OP_68(-13030, 1500, 12910, 0)
    MoveCamera(27, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -12540, 0, 13210, 90)
    SetChrPos(0x102, -12540, 0, 14610, 135)
    SetChrPos(0x103, -13740, 0, 13610, 90)
    SetChrPos(0x104, -14000, 0, 14810, 135)
    SetChrPos(0x109, -15000, 0, 13400, 90)
    SetChrPos(0x105, -14100, 0, 12000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1950F")
    OP_0D()

    ChrTalk(
        0x10,
        (
            "*sigh*, Margaret...\x01",
            "Why did such a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It's not like you to get hooked\x01",
            "by a man like that...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "A-Anyway, I have to do\x01",
            "something before I can't \x01",
            "get her back anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Vice Chief Pierre...\x01",
            "It's rare seeing him here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F(It looks like he's troubled about something...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x10, 0x10E, 0x3E8)
    Sleep(50)

    ChrTalk(
        0x10,
        (
            "Y-You...\x01",
            "Since when have you been there!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "D-Don't tell me that you've heard\x01",
            "me speaking to myself now!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FW-Well...\x01",
            "We didn't hear the details, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAlthough we partially heard about\x01",
            "a Margaret or whoever getting\x01",
            "hooked by some kind of man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "*gulp*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, is that the name of your\x01",
            "favorite hostess, Vice Chief?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "D-Don't say such a\x01",
            "scandalous thing!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Margaret is...\x01",
            "It's the name of my lady!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FL-Lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FDo you mean your wife?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "That's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Well, I lost the wedding ring before,\x01",
            "and after I missed the new term director\x01",
            "position she has become harder to deal with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Wait, why do I have to frankly\x01",
            "say these kind of things!?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19066")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆How did the "Searching For The Ring" Quest go in ZnK?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
            "[Cleared]\x01",           # 1
            "[Other result]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1904D"),
        (1, "loc_19052"),
        (2, "loc_1905C"),
        (SWITCH_DEFAULT, "loc_19066"),
    )


    label("loc_1904D")

    Jump("loc_19066")

    label("loc_19052")

    OP_29(0x15, 0x4, 0x10)
    Jump("loc_19066")

    label("loc_1905C")

    OP_29(0x15, 0x3, 0x10)
    Jump("loc_19066")

    label("loc_19066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19144")

    ChrTalk(
        0x101,
        (
            "#00003F(Now that I think about it... The Vice Chief\x01",
            "was famous for being a henpecked husband.)\x02\x03",
            "#00008F(And that means that what the Vice Chief is\x01",
            "troubled over now too, could be related to that...?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191F1")

    label("loc_19144")


    ChrTalk(
        0x101,
        (
            "#00003F(The Vice Chief...\x01",
            "He seems to be a henpecked husband.)\x02\x03",
            "#00008F(And that means that what the Vice Chief is\x01",
            "troubled over now too, could be related to that...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191F1")


    ChrTalk(
        0x10,
        (
            "...Hmph, it can't be helped.\x01",
            "Now needs must when the devil drives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Ladies and gentlemen of the SSS!\x01",
            "I'm giving you an absolute secret mission!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FAbsolute...secret?\x01",
            "What could you mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "U-Uhhm, to be frank...\x01",
            "I want to ask you a background check on my wife.\x02",
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
        0x104,
        "#00305FB-Background check...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FMaking use of one's private post is\x01",
            "against police duties regulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Who cares about the details on this occasion!!\x01",
            "I'm under the pressure of necessity too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If it suits you, I won't mind if you deal with\x01",
            "it in the form of one of your "requests"!\x01",
            "What about that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FU-uhhm...\x01",
            "(What do we do?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_195E6")

    label("loc_1950F")

    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "Ladies and gentlemen of the SSS!\x01",
            "I want to give you an absolute secret mission!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If it suits you, I won't mind if you deal with it\x01",
            "in the form of one of your "requests"!\x01",
            "Can you please accept it!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195E6")

    Call(0, 53)
    OP_4C(0x10, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12540, 0, 14410, 0)
    EventEnd(0x5)
    Return()

    # Function_52_18978 end

    def Function_53_19605(): pass

    label("Function_53_19605")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Quit]\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19659")
    Call(0, 54)
    Jump("loc_1975F")

    label("loc_19659")


    ChrTalk(
        0x101,
        (
            "#00006FI'm sorry...\x01",
            "We already have a job to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I-I see...it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Then, take care of it at once\x01",
            "and return back here!!\x01",
            "...All right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FW-We'll see what we can do.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x174, 7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x10, 0x5A, 0x0)
    SetChrPos(0x0, -12540, 0, 1096611267, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_1975F")

    Return()

    # Function_53_19605 end

    def Function_54_19760(): pass

    label("Function_54_19760")


    ChrTalk(
        0x101,
        (
            "#00001FI-I understand.\x01",
            "It looks like you're troubled...\x01",
            "Can we hear the whole story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Ooh...really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Good. Being this the case,\x01",
            "talking here won't do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Follow me to my office.\x01",
            "I'll talk about the details there!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_54_19760 end

    def Function_55_1985D(): pass

    label("Function_55_1985D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0xFF)
    OP_68(-12660, 1500, 14950, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24690, 0)
    SetChrPos(0x101, -11960, 0, 15570, 225)
    SetChrPos(0x102, -11390, 0, 13820, 315)
    SetChrPos(0x103, -13360, 0, 16370, 135)
    SetChrPos(0x104, -14520, 0, 15460, 90)
    SetChrPos(0x109, -14300, 0, 13610, 90)
    SetChrPos(0x105, -12900, 0, 12810, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00306FHeck, in the end\x01",
            "we accepted it.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWell, the Vice Chief is\x01",
            "worried about his wife...\x02\x03",
            "It could be good to\x01",
            "get on with it until\x01",
            "we figure out the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F*sigh*, it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThen, where do we start\x01",
            "to investigate from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FFirst, let's try going to the\x01",
            "Central Square restaurant.\x02\x03",
            "It appears that recently that host-like man and\x01",
            "the Vice Chief's wife often see each other there.\x01",
            "Maybe we can ask directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I guess \x01",
            "it's all right.\x02\x03",
            "#10309FThen, should we go\x01",
            "immediately?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Somehow he's enjoying this...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [The Vice Chief's Request]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x84, 0x4, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x84, 0x4, 0x2)
    OP_29(0x84, 0x1, 0x0)
    SetScenarioFlags(0x175, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_55_1985D end

    def Function_56_19C0E(): pass

    label("Function_56_19C0E")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_19C72")

    ChrTalk(
        0x101,
        (
            "#00000F...We don't have any business on \x01",
            "the floors above. Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D59")

    label("loc_19C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19D08")
    OP_4B(0x16, 0xFF)
    TurnDirection(0x16, 0x0, 500)

    ChrTalk(
        0x16,
        (
            "Currently, using the\x01",
            "elevator is forbidden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Everyone, please wait for orders\x01",
            "in the meeting room at 1F.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xB4, 0x0)
    OP_4C(0x16, 0xFF)
    Jump("loc_19D59")

    label("loc_19D08")


    ChrTalk(
        0x101,
        (
            "#00000F...We don't have any business on \x01",
            "the floors above. Let's not enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D59")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_56_19C0E end

    def Function_57_19D6D(): pass

    label("Function_57_19D6D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_57_19D6D end

    SaveToFile()

Try(main)
