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
        "Function_7_14DC",         # 07, 7
        "Function_8_2D55",         # 08, 8
        "Function_9_2D64",         # 09, 9
        "Function_10_4ECF",        # 0A, 10
        "Function_11_4FD4",        # 0B, 11
        "Function_12_5DF9",        # 0C, 12
        "Function_13_6C02",        # 0D, 13
        "Function_14_7653",        # 0E, 14
        "Function_15_773B",        # 0F, 15
        "Function_16_7830",        # 10, 16
        "Function_17_8573",        # 11, 17
        "Function_18_86C6",        # 12, 18
        "Function_19_A95F",        # 13, 19
        "Function_20_B27D",        # 14, 20
        "Function_21_B955",        # 15, 21
        "Function_22_C107",        # 16, 22
        "Function_23_CC59",        # 17, 23
        "Function_24_CC7F",        # 18, 24
        "Function_25_D639",        # 19, 25
        "Function_26_DDBC",        # 1A, 26
        "Function_27_E123",        # 1B, 27
        "Function_28_E5DC",        # 1C, 28
        "Function_29_F07D",        # 1D, 29
        "Function_30_F74E",        # 1E, 30
        "Function_31_10A52",       # 1F, 31
        "Function_32_10D6D",       # 20, 32
        "Function_33_10E78",       # 21, 33
        "Function_34_10F82",       # 22, 34
        "Function_35_110DA",       # 23, 35
        "Function_36_111F4",       # 24, 36
        "Function_37_115A6",       # 25, 37
        "Function_38_118DD",       # 26, 38
        "Function_39_11B91",       # 27, 39
        "Function_40_1231C",       # 28, 40
        "Function_41_12417",       # 29, 41
        "Function_42_125D4",       # 2A, 42
        "Function_43_127B6",       # 2B, 43
        "Function_44_128FC",       # 2C, 44
        "Function_45_12DF6",       # 2D, 45
        "Function_46_14590",       # 2E, 46
        "Function_47_14BDC",       # 2F, 47
        "Function_48_15D6B",       # 30, 48
        "Function_49_15D7E",       # 31, 49
        "Function_50_1658D",       # 32, 50
        "Function_51_17287",       # 33, 51
        "Function_52_17ED9",       # 34, 52
        "Function_53_18AB8",       # 35, 53
        "Function_54_18C08",       # 36, 54
        "Function_55_18CF1",       # 37, 55
        "Function_56_19084",       # 38, 56
        "Function_57_191E1",       # 39, 57
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
            "My, everyone, that thing\x01",
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
            "#00005FUmm, you mean this?\x02\x03",
            "#00000FWe thought it was something good when\x01",
            "we got it, but until now we couldn't\x01",
            "figure out any way to use it...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed the\x01",
            "fragment to Rebecca.\x07\x00\x02",
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
            "This is a quartz fragment that can\x01",
            "repair damaged memory quartz. The people\x01",
            "from forensics were looking for this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you have that, it should\x01",
            "be possible to analyze a part\x01",
            "of the cult's terminal data.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B6")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DF")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1208")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_1208")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_122E")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_122E")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FT-Then... We'll be able to\x01",
            "read the parts obscured by\x01",
            "Joachim Gｸnther...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. Only a portion of\x01",
            "it though, it seems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think we'll have immediate\x01",
            "results, so, may I send this\x01",
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CB")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x1, 3)
    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_13E2")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                          # 0
            "Show Combat Notebook\x01",          # 1
            "Check Cult Terminal Data\x01",      # 2
            "Hand Over Fragments\x01",           # 3
            "Cancel\x01",                        # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_1441")

    label("loc_13E2")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                          # 0
            "Show Combat Notebook\x01",          # 1
            "Check Cult Terminal Data\x01",      # 2
            "Cancel\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1441")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1441")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    Jump("loc_14C6")

    label("loc_146F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1493")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Call(0, 16)
    Jump("loc_14C6")

    label("loc_1493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B4")
    Call(0, 10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14C6")

    label("loc_14B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C6")
    Call(0, 9)

    label("loc_14C6")

    Jump("loc_135B")

    label("loc_14CB")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    Return()

    # Function_6_F51 end

    def Function_7_14DC(): pass

    label("Function_7_14DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(
        0x8,
        (
            "Everyone... Thank you\x01",
            "for your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FGood morning, Rebecca.\x01",
            "You're back at HQ, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, Officer Kate, Mr. Raymond\x01",
            "and the others have returned to\x01",
            "their normal duties as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since it was decided we'll\x01",
            "be outside of the State\x01",
            "Guard's chain of command...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At present, we're\x01",
            "currently working to bring\x01",
            "each post under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FThat's nice to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. This is thanks to\x01",
            "all of you.\x02",
        )
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
            "Tell her to leave the reception\x01",
            "desk to me and that I will devote\x01",
            "myself to helping everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1782")

    ChrTalk(
        0x109,
        (
            "#10102FHaha, understood. I'll\x01",
            "be sure to tell her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BB")

    label("loc_1782")


    ChrTalk(
        0x103,
        (
            "#00202FHaha, understood. We'll\x01",
            "be sure to tell her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17FD")

    ChrTalk(
        0x10A,
        (
            "#00600FRebecca, please take\x01",
            "care of HQ.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1826")

    label("loc_17FD")


    ChrTalk(
        0x101,
        (
            "#00000FRebecca, we leave HQ to\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1826")


    ChrTalk(
        0x8,
        (
            "Yes. I will work hard\x01",
            "for the citizens' sake\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alert situation will\x01",
            "continue, but... Please,\x01",
            "do your best as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 3)
    Jump("loc_1A43")

    label("loc_18B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A6")

    ChrTalk(
        0x8,
        (
            "Police HQ is working to\x01",
            "bring the situation under\x01",
            "control at every post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please tell Fran that\x01",
            "I'll devote myself to\x01",
            "helping everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alert situation will\x01",
            "continue, but... Please,\x01",
            "do your best as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1A43")

    label("loc_19A6")


    ChrTalk(
        0x8,
        (
            "We at HQ are doing\x01",
            "everything we can to bring\x01",
            "the situation under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The alert situation will\x01",
            "continue, but... Please,\x01",
            "do your best as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    Jump("loc_2D54")

    label("loc_1A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A56")
    Jump("loc_2D54")

    label("loc_1A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B50")

    ChrTalk(
        0x8,
        (
            "This morning, men from the\x01",
            "State Guard suddenly entered\x01",
            "HQ and ordered us to stand by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was so sudden that I\x01",
            "was confused as to what\x01",
            "to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, for now I can\x01",
            "only wait for the\x01",
            "meeting to finish.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1BD3")

    label("loc_1B50")


    ChrTalk(
        0x8,
        (
            "It was so sudden that I\x01",
            "was confused as to what\x01",
            "to do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, for now I can\x01",
            "only wait for the\x01",
            "meeting to finish.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD3")

    Jump("loc_2D54")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BE6")
    Jump("loc_2D54")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1CB5")

    ChrTalk(
        0x8,
        (
            "Mr. Dudley had a grim expression on his\x01",
            "face today as well... It looks like the\x01",
            "situation is less than stellar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If at all possible, I'd\x01",
            "like to find a solution\x01",
            "other than war, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D54")

    label("loc_1CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DD5")

    ChrTalk(
        0x8,
        (
            "Because of the CGF, the\x01",
            "transcontinental rail service was\x01",
            "fully restored as of this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since they managed to finish in time for\x01",
            "the first train, it all ended without\x01",
            "any changes to the service schedule...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel this was due to\x01",
            "the tenacity of the CGF.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D54")

    label("loc_1DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1EC8")

    ChrTalk(
        0x8,
        (
            "We immediately received many\x01",
            "inquiries from all over the\x01",
            "place due to the train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've already begun dealing with transferring\x01",
            "the passengers, but... If this situation\x01",
            "continues, it will really be troublesome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D54")

    label("loc_1EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F91")

    ChrTalk(
        0x8,
        (
            ""Pleroma Grass"... A Gnosis\x01",
            "ingredient appeared in the cult\x01",
            "database as well, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For such a thing to suddenly be\x01",
            "spotted throughout Crossbell...\x01",
            "I wonder what's going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D54")

    label("loc_1F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_212D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D1")

    ChrTalk(
        0x8,
        (
            "Everyone, it appears your next\x01",
            "mission will be a joint\x01",
            "operation with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Who would have thought that the day\x01",
            "would come when we carry out a request\x01",
            "shoulder-to-shoulder with the guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, you truly do\x01",
            "always surprise me. I\x01",
            "mean that in a good way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2128")

    label("loc_20D1")


    ChrTalk(
        0x8,
        (
            "Like Fran says, I think the\x01",
            "cryptids are tough opponents...\x01",
            "Please, do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2128")

    Jump("loc_2D54")

    label("loc_212D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_22AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221F")

    ChrTalk(
        0x8,
        (
            "Chief Sergei is already\x01",
            "standing by at security\x01",
            "countermeasures HQ on 2F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The conference opening\x01",
            "hour is drawing near,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The first hurdle is for\x01",
            "the heads of state to\x01",
            "safely enter the venue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_22A7")

    label("loc_221F")


    ChrTalk(
        0x8,
        (
            "The conference opening\x01",
            "hour is drawing near,\x01",
            "however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The first hurdle is for\x01",
            "the heads of state to\x01",
            "safely enter the venue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A7")

    Jump("loc_2D54")

    label("loc_22AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2361")

    ChrTalk(
        0x8,
        (
            "Both Fran and I went to look at\x01",
            "Orchis Tower on our breaks...\x01",
            "Its presence was overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is truly a fitting\x01",
            "structure to be\x01",
            "Crossbell's new landmark.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D54")

    label("loc_2361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2690")

    ChrTalk(
        0x8,
        (
            "The current security system is\x01",
            "built upon an unprecedented\x01",
            "partnership of police and CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was thought to be impossible\x01",
            "to build such system with a\x01",
            "traditional organization, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The biggest cause of it could be\x01",
            "said to be Commander Sonya who has\x01",
            "significant knowledge of the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Hmm, Rebecca really is a\x01",
            "beauty...)\x02\x03",
            "#00309F(The glasses are the same, but the\x01",
            "impression I get from Commander\x01",
            "Sonya is totally different.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(*sigh*, Randy... I'll\x01",
            "tell the Commander, you\x01",
            "know?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#00305F(N-No, that was just a\x01",
            "figure of speech...)\x02\x03",
            "#00309F(Maaan. Rebecca is a beauty\x01",
            "but she can't hold a candle\x01",
            "to Commander Sonya...)\x02",
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
    Jump("loc_275D")

    label("loc_2690")


    ChrTalk(
        0x8,
        (
            "The current security system is\x01",
            "built upon an unprecedented\x01",
            "partnership of police and CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The biggest cause of it could be\x01",
            "said to be Commander Sonya who has\x01",
            "significant knowledge of the police.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275D")

    Jump("loc_2D54")

    label("loc_2762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_29D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2917")

    ChrTalk(
        0x8,
        (
            "With the dismissal of the previous chief of\x01",
            "police, the police hierarchy changed greatly\x01",
            "following Mayor Dieter's assumption of office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are many new\x01",
            "difficulties, but even so, I\x01",
            "feel we're making progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hereafter, I think that expectations from\x01",
            "you all are going to become greater and\x01",
            "greater, but please do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On our end, we will\x01",
            "support you with\x01",
            "everything we have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_29D3")

    label("loc_2917")


    ChrTalk(
        0x8,
        (
            "Hereafter, I think that expectations from\x01",
            "you all are going to become greater and\x01",
            "greater, but please do your very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On our end, we will\x01",
            "support you with\x01",
            "everything we have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D3")

    Jump("loc_2D54")

    label("loc_29D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_END)), "loc_2C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB4")

    ChrTalk(
        0x8,
        (
            "There is an increasing\x01",
            "trend of reports about new\x01",
            "types monsters as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We want to gather a little more info on\x01",
            "them both for understanding the situation\x01",
            "and for implementing security measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I have until now, I'll give you\x01",
            "small rewards as you fill in the\x01",
            "notebook. I'm counting on all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition, you can\x01",
            "check the cult terminal\x01",
            "data here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please ask me whenever\x01",
            "you'd like to check it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2C71")

    label("loc_2BB4")


    ChrTalk(
        0x8,
        (
            "Regarding the Combat Notebook reports,\x01",
            "you will be awarded some compensation.\x01",
            "Please, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In addition, please ask\x01",
            "me if you want to check\x01",
            "the cult terminal data.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C71")

    Jump("loc_2D54")

    label("loc_2C76")


    ChrTalk(
        0x8,
        (
            "Haha. Nevertheless, a collaboration\x01",
            "request from Section One... Everyone, you\x01",
            "have made quite a name for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As someone who has been keeping\x01",
            "an eye on the Support Section's\x01",
            "activities, I am deeply moved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D54")

    Return()

    # Function_7_14DC end

    def Function_8_2D55(): pass

    label("Function_8_2D55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_2D63")
    SetScenarioFlags(0x1, 3)

    label("loc_2D63")

    Return()

    # Function_8_2D55 end

    def Function_9_2D64(): pass

    label("Function_9_2D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_2DEE")

    ChrTalk(
        0x8,
        (
            "My, you've brought me a\x01",
            ""fragment".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order to analyze the cult\x01",
            "terminal data, do you mind\x01",
            "if I send it to forensics?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEE")


    ChrTalk(
        0x101,
        "#00000FNo, please go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, please wait a\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_2E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D9D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_4D98")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECE")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information\x01",
            "Terminal Data: "About The\x01",
            "Cult" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2ECE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F32")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information\x01",
            "Terminal Data: "About The\x01",
            "Cult" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2F32")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F94")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2F94")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF6")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2FF6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392E")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 1 Information\x01",
            "Terminal Data: "About The\x01",
            "Cult" page 4 decrypted!\x07\x00\x02",
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
            "No. 1 Information Terminal\x01",
            "Data: "About The Cult"\x01",
            "completely decrypted!\x07\x00\x02",
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
            "#5PAll data from the information\x01",
            "terminal No. 1 has been\x01",
            "completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDo you want to check it\x01",
            "immediately?\x02",
        )
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
            "#5P...About this data... It\x01",
            "appears it is an entry\x01",
            "regarding the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA creed that denies the\x01",
            "Goddess... It is really\x01",
            "unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes... However, it fits\x01",
            "with Joachim Gｸnther's\x01",
            "testimony.\x02\x03",
            "#00001FAlso, this word, D...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3430")

    ChrTalk(
        0x103,
        (
            "#12P#00203FIt's the word indicating the True\x01",
            "God they believed in instead of\x01",
            "the Goddess, right?\x02\x03",
            "#00201FWe've already ascertained that\x01",
            "the "G" in the D∴G Cult's name\x01",
            "stands for true wisdom, Gnosis...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_33D8")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm. We can now say\x01",
            "we've finally confirmed\x01",
            "the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342B")

    label("loc_33D8")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHmm. We can now say\x01",
            "we've finally confirmed\x01",
            "the meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342B")

    Jump("loc_3552")

    label("loc_3430")


    ChrTalk(
        0x103,
        (
            "#12P#00200FIt's the word indicating the True\x01",
            "God they believed in instead of\x01",
            "the Goddess, right?\x02\x03",
            "#00201FWe've already ascertained that\x01",
            "the "G" in the D∴G Cult's name\x01",
            "stands for true wisdom, Gnosis...\x02\x03",
            "With this, it seems we can now\x01",
            "say we've finally confirmed the\x01",
            "meaning of "D∴G".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3552")


    ChrTalk(
        0x102,
        (
            "#12P#00108FBut... I'm sure that Professor\x01",
            "Joachim referred to KeA as the\x01",
            "one who would become a "God".\x02\x03",
            "Then, "D" could be also a word\x01",
            "to indicate KeA, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3670")

    ChrTalk(
        0x109,
        (
            "#12P#10101FJoachim Gｸnther... How\x01",
            "much did he know...?\x02\x03",
            "...We can't figure it\x01",
            "out with just this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3767")

    label("loc_3670")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3700")

    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F...We can't figure it\x01",
            "out with just this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3767")

    label("loc_3700")


    ChrTalk(
        0x104,
        (
            "#12P#00301FThat Joachim bastard...\x01",
            "How much did he know...?\x02\x03",
            "With just this, we still\x01",
            "don't know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3767")


    ChrTalk(
        0x101,
        (
            "#12P#00001FIt also seems that even\x01",
            "Ernest didn't get the whole\x01",
            "story from Joachim...\x02\x03",
            "#00003FIf we could have arrested\x01",
            "him... I just keep thinking\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_387F")

    ChrTalk(
        0x8,
        (
            "#5P...In any case, if we keep\x01",
            "decrypting the data like this, I\x01",
            "think we may learn many things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_392E")

    label("loc_387F")


    ChrTalk(
        0x8,
        (
            "#5P...In any case, if we keep\x01",
            "decrypting the data like this, I\x01",
            "think we may learn many things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_392E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3990")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 3 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3990")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FC")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" page 1 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_39FC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4369")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 2 Information\x01",
            "Terminal Data: "About\x01",
            "Gnosis" page 4 decrypted!\x07\x00\x02",
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
            "No. 2 Information Terminal\x01",
            "Data: "About Gnosis"\x01",
            "completely decrypted!\x07\x00\x02",
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
            "#5PAll data from the information\x01",
            "terminal No. 2 has been\x01",
            "completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDo you want to check it\x01",
            "immediately?\x02",
        )
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
            "#5P...About this data... It\x01",
            "appears the details of\x01",
            "that Gnosis are recorded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA drug with the effect of increasing physical\x01",
            "abilities, responsiveness and furthermore, it\x01",
            "draws out one's latent abilities as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt even causes the phenomenon\x01",
            "called Demonize... It's a\x01",
            "drug full of mysteries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FBecause the plant called Pleroma\x01",
            "Grass used as raw ingredient grows\x01",
            "in colonies in the Marshlands...\x02\x03",
            "It seems certain that Joachim went\x01",
            "there to collect his supply of it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E75")

    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data\x01",
            "there's a passage saying\x01",
            "that Gnosis...\x02\x03",
            "is a drug needed to\x01",
            "revive their so-called\x01",
            "True God "D".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FHonestly, what I'm\x01",
            "hearing is complete\x01",
            "nonsense, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F39")

    label("loc_3E75")


    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, in the data\x01",
            "there's a passage saying\x01",
            "that Gnosis...\x02\x03",
            "is a drug needed to\x01",
            "revive their so-called\x01",
            "True God "D".\x02\x03",
            "#00108FHonestly, what I'm\x01",
            "hearing is complete\x01",
            "nonsense, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F39")


    ChrTalk(
        0x103,
        (
            "#12P#00201FEven so, the Cult continued to\x01",
            "research Gnosis with its "rituals"\x01",
            "over the span of even 500 years...\x02\x03",
            "#00203F...I was fortunate to be saved by\x01",
            "Guy, but there were a large number\x01",
            "of victims over those many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FAnd he referred to them\x01",
            "as "some sacrifices"...\x02\x03",
            "Those guys were really\x01",
            "beyond help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_417D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_40DF")

    ChrTalk(
        0x105,
        (
            "#12P#10403F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_411E")

    label("loc_40DF")


    ChrTalk(
        0x105,
        (
            "#12P#10303F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_411E")


    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah... Although the cult\x01",
            "disappeared, we might\x01",
            "still need to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4206")

    label("loc_417D")


    ChrTalk(
        0x101,
        (
            "#12P#00003F...Also, even Wald was\x01",
            "taking Gnosis recently.\x02\x03",
            "#00001FAlthough the cult\x01",
            "disappeared, we might\x01",
            "still need to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4206")


    ChrTalk(
        0x102,
        (
            "#12P#00101FYes... Really.\x02\x03",
            "Not only Gnosis, we\x01",
            "police must keep drugs\x01",
            "like this under control.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42CF")

    ChrTalk(
        0x8,
        "#5PYes, I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...I think this is all\x01",
            "regarding Gnosis for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4369")

    label("loc_42CF")


    ChrTalk(
        0x8,
        "#5PYes, I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...I think this is all\x01",
            "regarding Gnosis for\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PLet's try to decrypt the\x01",
            "remaining "fragments" as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4369")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D5")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" page 2 decrypted!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43D5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D98")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" page 3 decrypted!\x07\x00\x02",
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
            "No. 3 Information Terminal\x01",
            "Data: "About The Divine\x01",
            "Child" completely decrypted!\x07\x00\x02",
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
            "#5PAll data from the information\x01",
            "terminal No. 3 has been\x01",
            "completely analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDo you want to check it\x01",
            "immediately?\x02",
        )
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
            "#5PThis content... Is it\x01",
            "about KeA who you were\x01",
            "sheltering at the SSS...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FKeA was created by the Crois clan\x01",
            "500 years ago... She was presented\x01",
            "to the Cult as a religious figure.\x02\x03",
            "As the Divine Child, their God's\x01",
            "vessel, who continued to slumber\x01",
            "in a "Cradle"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...Even the Cult members\x01",
            "didn't know the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWithout even knowing that they were\x01",
            "manipulated in the shadows for the Crois\x01",
            "Clan's true goal, they kept looking for\x01",
            "a fantasy they called their True God...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47D7")

    ChrTalk(
        0x106,
        (
            "#12P#10708F...In a way, I pity\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4840")

    label("loc_47D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4816")

    ChrTalk(
        0x109,
        (
            "#12P#10108F...In a way, I pity\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4840")

    label("loc_4816")


    ChrTalk(
        0x105,
        (
            "#12P#10408F...In a way, I pity\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4840")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A0")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FThinking about what they\x01",
            "did, I have no sympathy\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_495A")

    label("loc_48A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4904")

    ChrTalk(
        0x105,
        (
            "#12P#10403FThinking about what they\x01",
            "did, there is no room\x01",
            "for compassion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_495A")

    label("loc_4904")


    ChrTalk(
        0x109,
        (
            "#12P#10103FThinking about what they\x01",
            "did, there is no room\x01",
            "for compassion, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_495A")


    ChrTalk(
        0x101,
        (
            "#12P#00001FPutting the cult aside, KeA\x01",
            "is completely innocent.\x02\x03",
            "#00003FEven if she is an existence\x01",
            "created for the Crois Clan's\x01",
            "goals...\x02\x03",
            "Even if she possesses\x01",
            "miraculous abilities... Those\x01",
            "things don't matter.\x02\x03",
            "That child who woke up before\x01",
            "our eyes was a genuine,\x01",
            "normal little girl.\x02\x03",
            "#00001FAnd yet, she was locked up\x01",
            "all alone in a place like\x01",
            "that for hundreds of years...\x02\x03",
            "And now, Mariabell and Lawyer\x01",
            "Ian are trying to use her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F...No matter the\x01",
            "circumstances, like hell\x01",
            "we're gonna forgive 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...With this, the cult's\x01",
            "data has been completely\x01",
            "analyzed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI don't know the detailed\x01",
            "circumstances of the incident\x01",
            "you are involved in, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI understand how\x01",
            "precious KeA is to you\x01",
            "all so much it hurts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPlease...do your very\x01",
            "best. I will be rooting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThanks, Rebecca.\x02\x03",
            "#00003FWe'll bring KeA back with our\x01",
            "own hands.\x02\x03",
            "#00001FEven to create a future where\x01",
            "our precious KeA... When that\x01",
            "child can live smiling...!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D70")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_4D70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D89")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4D89")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    TalkEnd(0x8)

    label("loc_4D98")

    Jump("loc_2E3E")

    label("loc_4D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECE")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PIf you obtain any other\x01",
            ""fragments", please\x01",
            "bring them to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPlease also feel free to ask\x01",
            "me whenever you'd like to\x01",
            "check the decrypted data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4EAF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_4EAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4EC8")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4EC8")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_4ECE")

    Return()

    # Function_9_2D64 end

    def Function_10_4ECF(): pass

    label("Function_10_4ECF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4ED9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FD3")
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
            "[Cancel]\x01",                      # 3
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
        (0, "loc_4F86"),
        (1, "loc_4F94"),
        (2, "loc_4FA2"),
        (3, "loc_4FB0"),
        (SWITCH_DEFAULT, "loc_4FBF"),
    )


    label("loc_4F86")

    Sound(72, 0, 100, 0)
    Call(0, 11)
    Jump("loc_4FCE")

    label("loc_4F94")

    Sound(72, 0, 100, 0)
    Call(0, 12)
    Jump("loc_4FCE")

    label("loc_4FA2")

    Sound(72, 0, 100, 0)
    Call(0, 13)
    Jump("loc_4FCE")

    label("loc_4FB0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FCE")

    label("loc_4FBF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FCE")

    label("loc_4FCE")

    Jump("loc_4ED9")

    label("loc_4FD3")

    Return()

    # Function_10_4ECF end

    def Function_11_4FD4(): pass

    label("Function_11_4FD4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51FB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01",
            "─My name is Joachim Gｸnther, High Priest of the "D∴G\x01",
            "Cult". Six years ago, our Cult was almost completely\x01",
            "destroyed due to the actions of many powers, the\x01",
            "bracers included. However, for certain reasons, only\x01",
            "I evaded harm and was able to escape safely to this\x01",
            "land of ■. I had survived in order to accomplish the\x01",
            "Cult's ambition thanks to the great ■'s guidance. For\x01",
            "when the time comes─ I have decided to record data in\x01",
            "each terminal as material for writing new Testaments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_53FF")

    label("loc_51FB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Cult]\x01",
            "─My name is Joachim Gｸnther, High Priest of the "D∴G\x01",
            "Cult". Six years ago, our Cult was almost completely\x01",
            "destroyed due to the actions of many powers, the\x01",
            "bracers included. However, for certain reasons, only I\x01",
            "evaded harm and was able to escape safely to this land\x01",
            "of origin. I had survived in order to accomplish the\x01",
            "Cult's ambition thanks to the great D's guidance. For\x01",
            "when the time comes─ I have decided to record data in\x01",
            "each terminal as material for writing new Testaments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_53FF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFirst, I will speak of our Cult's origins. To do that,\x01",
            "I will need to look back at the annoying history this\x01",
            "Zemuria Continent has followed.  ─Approximately 1200\x01",
            "years ago, due to the Great Collapse, order and an\x01",
            "advanced civilization were lost,  and the Dark Ages\x01",
            "where war and poverty ruled, were brought forth. Then,\x01",
            "the weary people committed a grave error. Cajoled by\x01",
            "the words of imbeciles who had suddenly appeared, they\x01",
            "ended up accepting the selfish order they had invented.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5816")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words─ The foolish ■■ and the "■ of ■■", the\x01",
            "symbol of their faith. With their order, the Dark Ages\x01",
            "died, and that faith readily spread throughout the\x01",
            "continent... I want you to consider this carefully. If it\x01",
            "is true that a "■" exists, shouldn't she bestow equal\x01",
            "salvation to everyone? However, even to this very day, the\x01",
            "notion of inequity still exists and people never cease to\x01",
            "lose their lives due to disasters and misfortunes. So the\x01",
            ""■" chooses who to save? That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5A41")

    label("loc_5816")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn other words─ The foolish Septian Church and the\x01",
            ""Goddess of the Sky", the symbol of their faith. With\x01",
            "their order, the Dark Ages died, and that faith readily\x01",
            "spread throughout the continent... I want you to consider\x01",
            "this carefully. If it is true that a "Goddess" exists,\x01",
            "shouldn't she bestow equal salvation to everyone?\x01",
            "However, even to this very day, the notion of inequity\x01",
            "still exists and people never cease to lose their lives\x01",
            "due to disasters and misfortunes. So the "Goddess"\x01",
            "chooses who to save? That is too ludicrous an idea.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5A41")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C01")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretense\x01",
            "in order for the "■■" to acquire power. There is no way\x01",
            "something like a "■" exists. Our predecessors, having\x01",
            "arrived at that truth, set out on a long journey in order\x01",
            "to meet a "■■".  Then, when the era changed to the Middle\x01",
            "Ages, they finally found it. ■■■■, ■■■■■■■ lying in the\x01",
            "depths of this land... "■"─ That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5DE5")

    label("loc_5C01")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SIn the end, she is nothing more than an invented pretense in\x01",
            "order for the "Septian Church" to acquire power. There is no\x01",
            "way something like a "Goddess" exists. Our predecessors,\x01",
            "having arrived at that truth, set out on a long journey in\x01",
            "order to meet a "True God".  Then, when the era changed to\x01",
            "the Middle Ages, they finally found it. A long-asleep\x01",
            "existence, harboring a great power in its body, lying in the\x01",
            "depths of this land... "D"─ That is how it was called.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5DE5")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_4FD4 end

    def Function_12_5DF9(): pass

    label("Function_12_5DF9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5FB2")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01",
            "Gnosis... It is a secret drug which uses Pleroma Grass as\x01",
            "an ingredient, a ■■ said to ■■■■. As for its mixing method,\x01",
            "■■■■■■■. By taking it, physical ability and responsiveness\x01",
            "increase, and furthermore, it has the effect of drawing out\x01",
            "the user's latent abilities. ■■■■■■■■■. ■■■■■■■■■. "Gnosis"\x01",
            "is a drug to ■ the ■'s ■ with "■"'s ■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_616E")

    label("loc_5FB2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About Gnosis]\x01",
            "Gnosis... It is a secret drug which uses Pleroma Grass\x01",
            "as an ingredient, a legendary plant said to bloom atop\x01",
            "septium veins. As for its mixing method, it goes along\x01",
            "with "D". By taking it, physical ability and\x01",
            "responsiveness increase, and furthermore, it has the\x01",
            "effect of drawing out the user's latent abilities.\x01",
            "However, that is only the beginning. "Gnosis" is a\x01",
            "drug to link the user's mind with "D"'s spirit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_616E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62F0")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy ■ with the ■'s ■, "■" is able to store ■ and ■.\x01",
            "Sooner or later, when that ■ leads to ■, "■" will ■■■■.\x01",
            "Furthermore, there was room for improvement in "Gnosis".\x01",
            "■■■■■■■■■■■■■, it is ■■■■■■ to "■".  ■■■■■ since then,\x01",
            "our Cult has researched a far more effective "Gnosis"...\x01",
            "And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_64BB")

    label("loc_62F0")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SBy unifying with the user's mind, "D" is able to store\x01",
            "knowledge and grow. Sooner or later, when that knowledge\x01",
            "leads to wisdom, "D" will revive. Furthermore, there was\x01",
            "room for improvement in "Gnosis". When the user's\x01",
            "abilities are forced to the limit and drawn out, it is\x01",
            "possible to supply far more knowledge to "D". In the 500\x01",
            "years since then, our Cult has researched a far more\x01",
            "effective "Gnosis"... And repeated the so-called "ritual."\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_64BB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6657")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a ■■ to ■ we ■■■■■■■, we were close to\x01",
            "perfecting "Gnosis", but a miscalculation arose.\x01",
            "Because the experiments were on a large scale, bracers\x01",
            "and other authorities smelled our existence. That was\x01",
            "connected to the destruction of all lodges as well as\x01",
            "the Cult itself. What foolishness, I say. For our "■■"\x01",
            "to ■■■■, some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_67FA")

    label("loc_6657")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, at a speed incomparable to when we started 500\x01",
            "years ago, we were close to perfecting "Gnosis", but\x01",
            "a miscalculation arose.  Because the experiments\x01",
            "were on a large scale, bracers and other authorities\x01",
            "smelled our existence. That was connected to the\x01",
            "destruction of all lodges as well as the Cult\x01",
            "itself. What foolishness, I say. For our "True God"\x01",
            "to revive, some sacrifices are indispensable...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_67FA")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69E3")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly recovered the\x01",
            "experimental data and came to this land of ■, Crossbell.\x01",
            "As for the "Pleroma Grass" which is a "Gnosis" ingredient,\x01",
            "since it ■ in the ■■ in the ■■ of ■, I had no ■ problems.\x01",
            "Also, in the depths of this "Fort of Sun", there is a\x01",
            "research facility ■ by ■■■ and it is furnished with much\x01",
            "high-tech equipment. Thus, blessed with such a research\x01",
            "environment, I finally completed the secret drug─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6BEE")

    label("loc_69E3")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI, from a destroyed lodge, secretly recovered the\x01",
            "experimental data and came to this land of origin,\x01",
            "Crossbell. As for the "Pleroma Grass" which is a "Gnosis"\x01",
            "ingredient, since it grows in the Marshlands in the southern\x01",
            "part of Crossbell, I had no supply problems. Also, in the\x01",
            "depths of this "Fort of Sun", there is a research facility\x01",
            "built by Middles Ages alchemists and it is furnished with\x01",
            "much high-tech equipment. Thus, blessed with such a research\x01",
            "environment, I finally completed the secret drug─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6BEE")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_12_5DF9 end

    def Function_13_6C02(): pass

    label("Function_13_6C02")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D84")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01",
            "Crossbell is considered by our D∴G Cult to be our ■\x01",
            "and ■■■. The ■ is because it is the place where the\x01",
            "Divine Child ■■■■■. ■■■ of the "■■", the Divine\x01",
            "Child is a ■■■■ D∴G Cult. ■■■■■ Fort of Sun■,\x01",
            "■■■■■■■■■. ■■ ■■■■■■■■■■ ■■■■■■ Fort of Sun■■■■■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F75")

    label("loc_6D84")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S[About The Divine Child]\x01",
            "Crossbell is considered by our D∴G Cult to be our HQ and\x01",
            "land of origin. The reason is because it is the place\x01",
            "where the Divine Child was inherited by our founders. As\x01",
            "the vessel of the True God, the Divine Child is a symbolic\x01",
            "existence for our D∴G Cult. Continuing to sleep in the\x01",
            "Fort of Sun's basement, it has the aspect of a young human\x01",
            "maiden. She is said to be waiting for the moment of her\x01",
            "awakening at the altar of the Fort of Sun for 500 years.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6F75")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70F5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a ■ to be able to ■■■■... It is hard to believe\x01",
            "she is a being of this world. However, I really saw\x01",
            "her with my eyes. A ■■■■■■■■ ■■ a ■ called the "■■"─\x01",
            "I saw her ■■.  As for the "■■", it is an "Artifact"\x01",
            "which the ■■, based on the ■■ they were ■, ■. In this\x01",
            "case, even ■■■■ ■■■■, is only something natural.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_72CE")

    label("loc_70F5")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFor a human to be able to live that long... It is hard to\x01",
            "believe she is a being of this world. However, I really saw\x01",
            "her with my eyes. A young girl who continues sleeping like\x01",
            "she is dozing inside a globe called the "Divine Cradle"─ I\x01",
            "saw her divine figure. As for the "Divine Cradle", it is an\x01",
            ""Artifact" which the cult predecessors, based on alchemy\x01",
            "skills they were researching, made. In this case, it is\x01",
            "only natural to call this phenomenon a wonder.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_72CE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7457")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe Divine Child ■■■■■ ■■■■■■■■■■■ ■ Gnosis since\x01",
            "■■■■■. ──When she ■ "■", the Divine Child will ■■, and\x01",
            "she will ■ "■", the ■■. Then, ■■'s ■ and ■ will be ■ in\x01",
            ""■" and each person will be released from the spell of\x01",
            "the "■"  This is the prophecy our D∴G Cult predecessors\x01",
            "left to us and the ambition we must fulfill─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_763F")

    label("loc_7457")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThe Divine Child is regarded to have accumulated in her body\x01",
            "what could be said to be infinite knowledge through Gnosis\x01",
            "since the era she was born.  ─When she obtains "wisdom", the\x01",
            "Divine Child will wake up, and she will become "D", the True\x01",
            "God. Then, all people's wills and souls will be consolidated\x01",
            "in "D" and each person will be released from the spell of\x01",
            "the "Goddess".  This is the prophecy our D∴G Cult\x01",
            "predecessors left to us and the ambition we must fulfill─\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_763F")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_13_6C02 end

    def Function_14_7653(): pass

    label("Function_14_7653")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7678")
    SetChrPos(0xFE, 40, 40, 12610, 0)
    Jump("loc_772C")

    label("loc_7678")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_769D")
    SetChrPos(0xFE, -1000, 40, 12400, 0)
    Jump("loc_772C")

    label("loc_769D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76C2")
    SetChrPos(0xFE, 1140, 40, 12400, 0)
    Jump("loc_772C")

    label("loc_76C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76E7")
    SetChrPos(0xFE, 110, 0, 11010, 0)
    Jump("loc_772C")

    label("loc_76E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_770C")
    SetChrPos(0xFE, -950, 0, 10770, 0)
    Jump("loc_772C")

    label("loc_770C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772C")
    SetChrPos(0xFE, 1080, 0, 10720, 0)

    label("loc_772C")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_7653 end

    def Function_15_773B(): pass

    label("Function_15_773B")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_775B")
    BeginChrThread(0x101, 1, 0, 14)

    label("loc_775B")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7772")
    BeginChrThread(0x102, 1, 0, 14)

    label("loc_7772")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7789")
    BeginChrThread(0x103, 1, 0, 14)

    label("loc_7789")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77A0")
    BeginChrThread(0x104, 1, 0, 14)

    label("loc_77A0")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77B7")
    BeginChrThread(0x109, 1, 0, 14)

    label("loc_77B7")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77CE")
    BeginChrThread(0x105, 1, 0, 14)

    label("loc_77CE")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77E5")
    BeginChrThread(0x106, 1, 0, 14)

    label("loc_77E5")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77FC")
    BeginChrThread(0x10A, 1, 0, 14)

    label("loc_77FC")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7816")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_7816")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_782F")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_782F")

    Return()

    # Function_15_773B end

    def Function_16_7830(): pass

    label("Function_16_7830")

    ClearScenarioFlags(0x1, 6)
    ClearScenarioFlags(0x1, 7)
    ClearScenarioFlags(0x2, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7843")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A66")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7882")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_7882")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78B6")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_78B6")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78EA")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_78EA")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791E")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_791E")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7952")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_7952")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7986")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_7986")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79BA")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_79BA")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79EE")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_7A61")

    label("loc_79EE")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A25")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Jump("loc_7A61")

    label("loc_7A25")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A5C")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_7A61")

    label("loc_7A5C")

    Jump("loc_7A66")

    label("loc_7A61")

    Jump("loc_7843")

    label("loc_7A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_83E4")
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
            "Oh, everyone... It looks\x01",
            "like you have filled in the\x01",
            "Combat Notebook quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Since I would like to taken\x01",
            "down the monster information,\x01",
            "may I have a look at it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#12PYes, please do.\x02",
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
            "I'll return your\x01",
            "notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is your\x01",
            "compensation this time.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C8B")

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
    Jump("loc_7F8D")

    label("loc_7C8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CE1")

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
    Jump("loc_7F8D")

    label("loc_7CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D37")

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
    Jump("loc_7F8D")

    label("loc_7D37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D8D")

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
    Jump("loc_7F8D")

    label("loc_7D8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DE3")

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
    Jump("loc_7F8D")

    label("loc_7DE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E39")

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
    Jump("loc_7F8D")

    label("loc_7E39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8F")

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
    Jump("loc_7F8D")

    label("loc_7E8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EE5")

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
    Jump("loc_7F8D")

    label("loc_7EE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F3B")

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
    Jump("loc_7F8D")

    label("loc_7F3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F8D")

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

    label("loc_7F8D")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FC3")
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
    Jump("loc_7FF0")

    label("loc_7FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FF0")
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

    label("loc_7FF0")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_811D")

    ChrTalk(
        0x8,
        (
            "Please stop by when you\x01",
            "have gathered additional\x01",
            "monster information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, we will.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80B1")

    ChrTalk(
        0x102,
        "#12P#0100FWe'll come again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8118")

    label("loc_80B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80E7")

    ChrTalk(
        0x103,
        "#12P#0200FWe'll come again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8118")

    label("loc_80E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8118")

    ChrTalk(
        0x104,
        "#12P#0300FWe'll come again!\x02",
    )

    CloseMessageWindow()

    label("loc_8118")

    Jump("loc_837C")

    label("loc_811D")


    ChrTalk(
        0x8,
        (
            "It looks like you have gathered plenty\x01",
            "of new type monster information as\x01",
            "well. Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this, I think that our\x01",
            "security measures will become\x01",
            "even more perfect from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHaha...we're honored to\x01",
            "have been of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. We really are in\x01",
            "your debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And so, please allow me to give\x01",
            "you a special reward this time.\x01",
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
            "I will pray for your\x01",
            "success from now on as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you need anything\x01",
            "else, please visit me\x01",
            "again whenever you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_837C")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_8393")
    ClearScenarioFlags(0x1, 5)

    label("loc_8393")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83AC")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_83AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83C5")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_83C5")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_8572")

    label("loc_83E4")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84BC")

    ChrTalk(
        0x8,
        (
            "Since I think we already have\x01",
            "enough information at HQ, let\x01",
            "us end the investigation here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I may need your assistance again\x01",
            "in the future. I will be counting\x01",
            "on you when that time comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8572")

    label("loc_84BC")


    ChrTalk(
        0x8,
        (
            "It looks like you've\x01",
            "been collecting Combat\x01",
            "Notebook information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you have gathered a little more\x01",
            "information, please show it to me. I\x01",
            "will take down the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8572")

    Return()

    # Function_16_7830 end

    def Function_17_8573(): pass

    label("Function_17_8573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_859C")
    Call(0, 18)
    Jump("loc_86BD")

    label("loc_859C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85B7")
    Call(0, 18)
    Jump("loc_86BD")

    label("loc_85B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85CD")
    Call(0, 18)
    Jump("loc_86BD")

    label("loc_85CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85E3")
    Call(0, 18)
    Jump("loc_86BD")

    label("loc_85E3")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "#01900FEveryone, do you know about\x01",
            "the orbal game "Pom!"?\x02\x03",
            "#01909FHaha. Actually, I started\x01",
            "playing it too. If you like,\x01",
            "exchange accounts with me.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Fran's Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    TalkEnd(0x9)

    label("loc_86BD")

    Jump("loc_86C5")

    label("loc_86C2")

    Call(0, 18)

    label("loc_86C5")

    Return()

    # Function_17_8573 end

    def Function_18_86C6(): pass

    label("Function_18_86C6")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_86D7")
    Jump("loc_A95B")

    label("loc_86D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_86E5")
    Jump("loc_A95B")

    label("loc_86E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88BD")
    SoundLoad(803)

    ChrTalk(
        0x9,
        (
            "#01901FE-Everyone, the\x01",
            "situation has gotten\x01",
            "serious, yes?\x02\x03",
            "Police HQ has been busy\x01",
            "ever since this morning\x01",
            "as well...\x02",
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
            "#01903FYes, this is Crossbell\x01",
            "Police...\x02\x03",
            "#01901FYes, yes...\x02\x03",
            "That's right, since last\x01",
            "night, to settle the\x01",
            "situation, the CGF...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(She really does look\x01",
            "busy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Right. We've got to do\x01",
            "what we can as well.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 7)
    OP_24(0x323)
    Jump("loc_8971")

    label("loc_88BD")

    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is talking at the\x01",
            "receiver.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01901FYes, yes...\x02\x03",
            "#01908F...I'm terribly sorry. Concerning\x01",
            "the real identity of the armed\x01",
            "group, it's not clear yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8971")

    Jump("loc_A95B")

    label("loc_8976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_8A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8991")
    Call(0, 21)
    Jump("loc_8A6D")

    label("loc_8991")


    ChrTalk(
        0x9,
        (
            "#01900FLike I told you before, I've\x01",
            "readied an orbal boat for you\x01",
            "at the Waterfront Area jetty.\x02\x03",
            "#01904FA mechanic should be near\x01",
            "there. Please, go have a\x01",
            "look!\x02\x03",
            "#01900FPlease be careful when going\x01",
            "there, everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A6D")

    Jump("loc_A95B")

    label("loc_8A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_8E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3F")

    ChrTalk(
        0x9,
        (
            "#01900FEveryone, thank you very much for all\x01",
            "your hard work yesterday.\x02\x03",
            "It seems you had great achievements,\x01",
            "be it about the Ouroboros organization\x01",
            "or the cause of the train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, well, actually we\x01",
            "didn't do anything\x01",
            "special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThat's right. The people who worked\x01",
            "all night long dealing with the\x01",
            "accident had it way tougher than us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FEven so, you all continued your\x01",
            "investigation activities until rather\x01",
            "late yesterday evening, didn't you.\x02\x03",
            "#01902FPlease, watch out for your health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FThank you very much for\x01",
            "your concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FWell you're probably busy\x01",
            "too, so you shouldn't\x01",
            "push yourself either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes, roger that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 0)
    Jump("loc_8E0B")

    label("loc_8D3F")


    ChrTalk(
        0x9,
        (
            "#01900FIt appears you received\x01",
            "a few support requests\x01",
            "as well today...\x02\x03",
            "Please, do your best on\x01",
            "them without pushing\x01",
            "yourselves.\x02\x03",
            "On my end, I will take\x01",
            "good care of myself and\x01",
            "try not to overdo it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0B")

    Jump("loc_A95B")

    label("loc_8E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_9083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F93")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is talking at the\x01",
            "receiver.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01903FYes, yes...\x02\x03",
            "#01901F...I'm terribly sorry. The cause\x01",
            "of the accident is currently\x01",
            "under investigation...\x02\x03",
            "And there is no ETA for\x01",
            "resumption of service at this\x01",
            "time, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(It looks like she's\x01",
            "dealing with the train\x01",
            "accident.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yes, she looks busy.\x01",
            "Let's not disturb her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_907E")

    label("loc_8F93")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fran is talking at the\x01",
            "receiver.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01903FYes, yes...\x02\x03",
            "#01901F...I'm terribly sorry. The cause\x01",
            "of the accident is currently\x01",
            "under investigation...\x02\x03",
            "And there is no ETA for\x01",
            "resumption of service at this\x01",
            "time, either...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_907E")

    Jump("loc_A95B")

    label("loc_9083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_92DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91B1")

    ChrTalk(
        0x9,
        (
            "#01903FAzure flowers, and also\x01",
            "cryptids...\x02\x03",
            "#01901FI get an ominous impression from\x01",
            "them somehow, but anyway, all we\x01",
            "can do is everything we can.\x02\x03",
            "Umm, everyone, please be careful\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYou too Fran. Thanks for\x01",
            "your support.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_92D5")

    label("loc_91B1")


    ChrTalk(
        0x9,
        (
            "#01903FI am getting an ominous impression\x01",
            "somehow from both the state of tension\x01",
            "due to the independence proposal and\x01",
            "the current strange situation.\x02\x03",
            "#01901FI think overthinking them can't be\x01",
            "helped, but...\x02\x03",
            "Anyway, I also think that I have to\x01",
            "properly complete the work in front of\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92D5")

    Jump("loc_A95B")

    label("loc_92DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_967D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95DC")

    ChrTalk(
        0x9,
        (
            "#01901FEveryone... I'm told that you're\x01",
            "dealing with the Cryptids?\x02\x03",
            "The same as the one that was in\x01",
            "the old abandoned mine, they\x01",
            "appear to be strange monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we don't know anything about\x01",
            "them, do we. For now, we'll try to\x01",
            "proceed with the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F? Are you worried about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FAh, yes. I heard that\x01",
            "Cryptids are quite strong...\x01",
            "I don't want you to get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYes, that's right.\x02\x03",
            "#10100FHowever, we won't push\x01",
            "ourselves too hard, so you\x01",
            "don't have worry so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FYes... I see.\x02\x03",
            "Also, you're the veteran\x01",
            "Special Support Section,\x01",
            "after all.\x02\x03",
            "#01909FFran Seeker, having faith\x01",
            "in your success in battle,\x01",
            "will wait for your report!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHaha. Thanks Fran.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 1)
    Jump("loc_9678")

    label("loc_95DC")


    ChrTalk(
        0x9,
        (
            "#01902FEveryone, please be\x01",
            "careful during your\x01",
            "cryptid investigation.\x02\x03",
            "Fran Seeker, having faith\x01",
            "in your success in battle,\x01",
            "will wait for your report!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9678")

    Jump("loc_A95B")

    label("loc_967D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9933")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9698")
    Call(0, 20)
    Jump("loc_992E")

    label("loc_9698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_985B")

    ChrTalk(
        0x9,
        (
            "#01900FCaptain Julia has an\x01",
            "dignified air and she's cool\x01",
            "and... I really admire her!\x02\x03",
            "#01909FWell, I think big sis is\x01",
            "cooler, though.㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, what do I have\x01",
            "to do with you...\x02\x03",
            "#10101FIf other fans of Captain\x01",
            "Julia heard you, they'd\x01",
            "get angry for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, I wonder. It seems that,\x01",
            "like Captain Julia, you have\x01",
            "quite a few fans yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FOh, that's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FG-Give me a break...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_992E")

    label("loc_985B")


    ChrTalk(
        0x9,
        (
            "#01900FToday's Orchis Tower security detail\x01",
            "doesn't happen every day, so I wanted\x01",
            "to be assigned there as well...\x02\x03",
            "#01906FI wanted to see the dignified and\x01",
            "cool Captain Julia and big sis during\x01",
            "the detail!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_992E")

    Jump("loc_A95B")

    label("loc_9933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B8E")
    TurnDirection(0x9, 0x109, 0)

    ChrTalk(
        0x9,
        (
            "#01902FAh, Noｱl.\x02\x03",
            "You took part in the unveiling\x01",
            "ceremony security detail,\x01",
            "right? ...How was it? Amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes, that's right.\x02\x03",
            "Especially Princess\x01",
            "Klaudia and Captain Julia\x01",
            "from Liberl were amaz...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01905FD-Did you see them up\x01",
            "close!?\x02\x03",
            "#01906FOoh, how nice. But only\x01",
            "you did. That's no fair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha, sorry Fran. I'll\x01",
            "make up for it somehow\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha. Then naturally, this\x01",
            "means Fran is a Captain\x01",
            "Julia fan as well, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Hmm, what can I say.\x01",
            "The world's men are\x01",
            "losing ground.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 6)
    Jump("loc_9BF1")

    label("loc_9B8E")


    ChrTalk(
        0x9,
        (
            "#01902FPrincess Klaudia and\x01",
            "even Captain Julia!\x02\x03",
            "How nice. I wanted to\x01",
            "see them up close too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BF1")

    Jump("loc_A95B")

    label("loc_9BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9F19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E6D")

    ChrTalk(
        0x9,
        (
            "#01902FHaha. The trade conference will finally\x01",
            "start tomorrow.\x02\x03",
            "Heads of state from all neighboring\x01",
            "countries will gather, there's the Orchis\x01",
            "Tower unveiling... My heart is racing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FJeez, you aren't a child anymore, so\x01",
            "don't just say such thoughtless things\x01",
            "and concentrate on your job, ok?\x02\x03",
            "#10106FYou're going to busier than usual\x01",
            "throughout the conference too, you\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01900FYou're right, and that's\x01",
            "exactly why I have to\x01",
            "find enjoyment in it.\x02\x03",
            "You should too, Noｱl.\x01",
            "You're always too\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe, you can say that\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FW-Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FAhaha...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 7)
    Jump("loc_9F14")

    label("loc_9E6D")


    ChrTalk(
        0x9,
        (
            "#01902FIt's true that I'll be busy with\x01",
            "work, but my heart is racing since\x01",
            "it will be such a big event.\x02\x03",
            "#01909FHaha, I'm looking forward to\x01",
            "tomorrow's ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F14")

    Jump("loc_A95B")

    label("loc_9F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_9FD3")

    ChrTalk(
        0x9,
        (
            "#01901FAccording to Mayor Bickson's, it\x01",
            "appears that something strange is\x01",
            "occurring inside the old mine.\x02\x03",
            "It's not known what is strange,\x01",
            "but... Please, do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A95B")

    label("loc_9FD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FEE")
    Call(0, 19)
    Jump("loc_A24F")

    label("loc_9FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A18D")

    ChrTalk(
        0x9,
        (
            "#01906FAah, I'm really glad I'm\x01",
            "able to call you "big\x01",
            "sis".\x02\x03",
            "#01902FNow it appears that I\x01",
            "can focus on my job\x01",
            "without reservation.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106FW-Was it that much of an\x01",
            "obstacle before...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    ChrTalk(
        0x9,
        (
            "#01901FI mean, to me, it's a\x01",
            "life-or-death matter!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Aah, enough. Workplace\x01",
            "decorum is a thing, you\x01",
            "know...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(D-Don't worry about it,\x01",
            "Noｱl.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A24F")

    label("loc_A18D")


    ChrTalk(
        0x9,
        (
            "#01902FHaha, now I'll be able\x01",
            "to focus on my job\x01",
            "without reservation.\x02",
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
        (
            "#10106F(Jeez. I'm just not\x01",
            "going to say\x01",
            "anything...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A24F")

    Jump("loc_A95B")

    label("loc_A254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A95B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7B9")

    ChrTalk(
        0x9,
        (
            "#01900FHaha. At any rate, the SSS's\x01",
            "activities have finally\x01",
            "restarted, haven't they?\x02\x03",
            "#01909FAs your assigned operator, I\x01",
            "am especially moved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha. Getting back to the\x01",
            "Support Section is new kind\x01",
            "of feeling even for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, that's right.\x01",
            "We get to work with you\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FYes. I'm passionate about being your\x01",
            "operator as well!\x02\x03",
            "#01906FWhen you were on break, I had a hard\x01",
            "time dealing with the incessant\x01",
            "requests from the citizens...\x02\x03",
            "#01902FI was really looking forward\x01",
            "resuming operations with you all.\x02\x03",
            "#01909F...Also, I finally get to work with\x01",
            "with big sis!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00009FHaha... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FJeez, Fran... How many times do I have to\x01",
            "tell you not to call me big sis?\x02\x03",
            "#10101FListen. Even if we are sisters, because\x01",
            "we're in the same workplace you have to\x01",
            "keep a minimum amount of decorum in mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#01906FOoh... I'm sorry.\x02\x03",
            "#01908FB-But, maybe I won't be\x01",
            "able to get used t...\x02",
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
        (
            "#10302FHaha. What a strict big\x01",
            "sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FA-Anyway...\x02\x03",
            "#01900FWhen Tio and Randy join\x01",
            "later, you'll be invincible.\x02\x03",
            "#01902FHaha. From the bottom of my\x01",
            "heart, I look forward to\x01",
            "when you'll all be together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, I feel the same.\x02\x03",
            "#00002FThen... Fran, please\x01",
            "take good care of us\x01",
            "once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes, sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 1)
    Jump("loc_A95B")

    label("loc_A7B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8A3")

    ChrTalk(
        0x9,
        (
            "#01902FHaha. Being able to work with\x01",
            "all of you again makes me\x01",
            "passionate about my job too.\x02\x03",
            "#01909FI also get to work with big\x01",
            "si...*cough* Noｱl!\x02",
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
        "#00012F(Haha, now now...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A95B")

    label("loc_A8A3")


    ChrTalk(
        0x9,
        (
            "#01900FI think a lot of requests are\x01",
            "going to come to the renewed\x01",
            "Support Section from now on.\x02\x03",
            "#01909FPlease allow me to steadily\x01",
            "support you as your operator\x01",
            "like I did before!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A95B")

    TalkEnd(0x9)
    Return()

    # Function_18_86C6 end

    def Function_19_A95F(): pass

    label("Function_19_A95F")

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
            "#01900FAh, you came just at the\x01",
            "right time!\x02\x03",
            "#01901FActually, I have a very\x01",
            "important thing to discuss\x01",
            "with big si... with Noｱl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FW-What's wrong Fran? You\x01",
            "have such a pained look\x01",
            "on your face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01908FListen............\x02\x03",
            "#01906F...Is it calling you "big\x01",
            "sis" at the workplace bad\x01",
            "no matter what?\x02",
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
            "#12P#10106FA-And I was thinking what the\x01",
            "problem could be...\x02\x03",
            "#10101F...Ahem. I've explained it many\x01",
            "times since my transfer to the\x01",
            "Support Section was decided, right?\x02\x03",
            "#10103FI told you that because we're in\x01",
            "the same workplace you must keep in\x01",
            "mind a bare minimum of decorum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01905FB-But, big si... No,\x01",
            "Noｱ...\x02\x03",
            "#01906FAah, I can't do that! I\x01",
            "can't get used to it no\x01",
            "matter what!\x02",
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

    def lambda_AD95():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD95)
    Sleep(50)

    def lambda_ADA5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADA5)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00012FW-Well... Noｱl. It's not\x01",
            "something to be so\x01",
            "strict about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, that's right. When Fran\x01",
            "says "Noｱl" I feel it's too\x01",
            "formal...\x02\x03",
            "#00100FA way of address she's not used in\x01",
            "times communication is urgently\x01",
            "needed could be inefficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FT-That could also be\x01",
            "true, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01902FS-See...! Everyone is\x01",
            "saying that!\x02\x03",
            "#01909FIsn't "big sis" all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, being a little lenient\x01",
            "seems to match with the\x01",
            "Support Section stance, right?\x02\x03",
            "#10302FI mean, that's how it feels,\x01",
            "starting with the chief.\x02",
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
        (
            "#5P#00006F(I have nothing to say\x01",
            "back to that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F...*sigh*, well, it\x01",
            "can't be helped. If\x01",
            "everyone says so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FHooray! Then it's\x01",
            "decided!\x02\x03",
            "#01900FEhehe, thank you very\x01",
            "much, everyone!\x02\x03",
            "#01904FAhem, then...\x02\x01",
            "#01909FIt's a pleasure working\x01",
            "with you, big sis㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10101FA-At least, Fran... Don't\x01",
            "mix personal affairs with\x01",
            "official business...\x02",
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
        (
            "#12P#10106F(S-She doesn't get it at\x01",
            "all...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Haha. Noｱl is no match\x01",
            "for Fran either.)\x02",
        )
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

    # Function_19_A95F end

    def Function_20_B27D(): pass

    label("Function_20_B27D")

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
            "#01900FAh, Tio! You're finally\x01",
            "back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes, fortunately.\x02\x03",
            "#00204FNice to be working with\x01",
            "you again, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FHaha, likewise.\x02\x03",
            "#01900FAnyway, with this, the\x01",
            "Special Support Section\x01",
            "members are all together!\x02\x03",
            "I'm expecting even\x01",
            "greater results from all\x01",
            "of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, thanks Fran. We'll\x01",
            "do our very best.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01905FOh, that's right... I\x01",
            "have to thank you again!\x02\x03",
            "#01900FYou got Captain Julia's\x01",
            "autograph for me, right\x01",
            "sis!?\x02\x03",
            "#01909FThank you so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FAhaha, don't worry about\x01",
            "it.\x02\x03",
            "#10106FI feel bad you didn't\x01",
            "get to speak with her...\x02\x03",
            "#10100FI'll give it you another\x01",
            "time, when things are\x01",
            "calmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FOkay! I can't wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. Come to think of it,\x01",
            "Elie and Noｱl got them\x01",
            "yesterday on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. Both the crown\x01",
            "princess and Captain Julia\x01",
            "are really quite generous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHeh, and I assume you're\x01",
            "a fan of Captain Julia\x01",
            "as well, Fran?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FBut of course!\x02\x03",
            "#01900FCaptain Julia has an\x01",
            "dignified air and she's cool\x01",
            "and... I really admire her!\x02\x03",
            "#01909FWell, I think you're even\x01",
            "cooler, sis㈱\x02",
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
            "#12P#10111FH-Hey now!\x02\x03",
            "#10106FF-Fran! Why do you have\x01",
            "to go and say things\x01",
            "like that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHaha. To Fran, Noｱl is\x01",
            "the best no matter what,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHmm, that's just what\x01",
            "you'd expect, huh...\x02",
        )
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

    # Function_20_B27D end

    def Function_21_B955(): pass

    label("Function_21_B955")

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
            "#01905FAh, everyone...\x02\x03",
            "#01900FLike I told you before, I've\x01",
            "readied an orbal boat for you\x01",
            "at the Waterfront Area jetty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thanks Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FWe'll use it right away.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#01903FIt appears you're going to the\x01",
            "Marshlands to look for those\x01",
            "bracers, but...\x02\x03",
            "#01908FUmm, will you be all right? It's\x01",
            "the place where two bracers, who\x01",
            "are nearly A-rank, went missing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FFran...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FSorry to make you\x01",
            "worry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906F*sigh*, it'd be nice if\x01",
            "even I could do something\x01",
            "in times like these...\x02\x03",
            "#01900FUmm, if you want, would\x01",
            "you like to take Ban Ban\x01",
            "with you as a charm?\x02",
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
        (
            "#12P#00005FIf I remember correctly,\x01",
            "Ban Ban is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FUmm... It's a bear\x01",
            "plushie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FWhen you hug it, it\x01",
            "greatly calms you!\x02\x03",
            "#01900FBig sis, you do it too\x01",
            "sometimes when no one is\x01",
            "watching, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#12P#10111FWha!? I-I'd never do\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01901FI feel an overwhelming sorrow sending\x01",
            "Ban Ban to such a dangerous place, but\x01",
            "if it's for your sake, everyone...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No, we're fine... For now, please calm\x01",
            "down.\x02\x03",
            "#00002FHaha, but thanks for the thought though.\x01",
            "I was feeling a little uneasy, but thanks\x01",
            "to you now I feel relaxed, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe. This is where Fran\x01",
            "shines.\x02\x03",
            "#10309FWe were also able to\x01",
            "catch a glimpse of\x01",
            "Noｱl's private life.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10106F(Ooh, that Fran! I'll\x01",
            "remember this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FAhaha, I'm glad, then.\x02\x03",
            "#01900FPlease be careful when\x01",
            "going there, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!\x02",
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

    # Function_21_B955 end

    def Function_22_C107(): pass

    label("Function_22_C107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C125")
    Call(0, 47)
    Return()

    label("loc_C125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C136")
    Jump("loc_CC55")

    label("loc_C136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C144")
    Jump("loc_CC55")

    label("loc_C144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C1DC")

    ChrTalk(
        0xFE,
        (
            "We'll do whatever we have to\x01",
            "to remove Red Constellation\x01",
            "from Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please do everything\x01",
            "that you can on your end\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC55")

    label("loc_C1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C1EA")
    Jump("loc_CC55")

    label("loc_C1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1F8")
    Jump("loc_CC55")

    label("loc_C1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C602")

    ChrTalk(
        0xFE,
        "Phew, this feels nice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(That bottle Emma is\x01",
            "holding... Is it a\x01",
            "supplement or something...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Looks like it... Could\x01",
            "she be really tired?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, "Sporitan X"...\x02\x03",
            "It appears you're\x01",
            "drinking quite the\x01",
            "punchy thing...\x02",
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
            "It can't be helped, I\x01",
            "pulled an all nighter\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, so what? Do you want to say\x01",
            "it's such a strange thing for me\x01",
            "to be drinking a supplement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Answer me... Detective\x01",
            "Lloyd Bannings!\x02",
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
        (
            "#00006FNo, I didn't say\x01",
            "anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hmph... There's no\x01",
            "problem then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, can you\x01",
            "allow yourselves to\x01",
            "dawdle here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean... You should be doing as\x01",
            "many of your support requests or\x01",
            "whatever as possible.\x02",
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
        (
            "#10302F(Hehe, how unlucky for\x01",
            "you.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(...You're one to talk.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x171, 6)
    Jump("loc_C664")

    label("loc_C602")


    ChrTalk(
        0xFE,
        (
            "Anyhow, you should be out\x01",
            "doing support requests,\x01",
            "not dawdling around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's all.\x02",
    )

    CloseMessageWindow()

    label("loc_C664")

    Jump("loc_CC55")

    label("loc_C669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C677")
    Jump("loc_CC55")

    label("loc_C677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C685")
    Jump("loc_CC55")

    label("loc_C685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C8B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6AD")
    Call(0, 30)
    Jump("loc_C76B")

    label("loc_C6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6BF")
    Call(0, 31)
    Jump("loc_C76B")

    label("loc_C6BF")


    ChrTalk(
        0xFE,
        (
            "Mr. Dudley expects from\x01",
            "the Support Section to\x01",
            "act in a support role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you think hard about what\x01",
            "that means, you should know what\x01",
            "to do... I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C76B")

    Jump("loc_C8AD")

    label("loc_C770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C83E")

    ChrTalk(
        0xFE,
        (
            "Section One will continue\x01",
            "tracking Lechter Arundel\x01",
            "and Kilika Rouran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are the major powers scheming...?\x01",
            "We can't even guess at present, but we\x01",
            "must continue to investigate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_C8AD")

    label("loc_C83E")


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

    label("loc_C8AD")

    Jump("loc_CC55")

    label("loc_C8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CC3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB97")

    ChrTalk(
        0xFE,
        (
            "Detective Bannings...\x01",
            "How are your support\x01",
            "requests going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, well... For now\x01",
            "we're doing them at our\x01",
            "usual pace.\x02",
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
            "the final checks on the Orchis Tower\x01",
            "security system for the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Section Chief Sergei will be making all\x01",
            "kinds of adjustments at the countermeasures\x01",
            "HQ on 2F for the entire day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...You all have your own\x01",
            "work to focus on, don't\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's exactly why you\x01",
            "shouldn't say "at our\x01",
            "usual pace".\x02",
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
            "#10302F(Hehe, always the same\x01",
            "strict woman.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Hmm, when she doesn't\x01",
            "speak, she's quite the\x01",
            "beauty though...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Randy... That's not the\x01",
            "problem here...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 0)
    Jump("loc_CC39")

    label("loc_CB97")


    ChrTalk(
        0xFE,
        (
            "Both Mr. Dudley and Section Chief\x01",
            "Sergei are devoting their utmost\x01",
            "abilities toward their duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...You all have your own\x01",
            "work to focus on, don't\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC39")

    Jump("loc_CC55")

    label("loc_CC3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_CC4C")
    Jump("loc_CC55")

    label("loc_CC4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_CC55")

    label("loc_CC55")

    TalkEnd(0xFE)
    Return()

    # Function_22_C107 end

    def Function_23_CC59(): pass

    label("Function_23_CC59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC78")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC78")
    Call(0, 52)
    Return()

    label("loc_CC78")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_23_CC59 end

    def Function_24_CC7F(): pass

    label("Function_24_CC7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CC90")
    Jump("loc_D635")

    label("loc_CC90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC9E")
    Jump("loc_D635")

    label("loc_CC9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CEDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDE1")

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
            "Anyhow, at present, Section Two is\x01",
            "working hard supporting Section One,\x01",
            "turning a blind eye to all other cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spies entering Crossbell... We're in the\x01",
            "middle of sorting every little bit of intel,\x01",
            "especially about that Imperial spy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_CED7")

    label("loc_CDE1")


    ChrTalk(
        0xFE,
        (
            "Anyhow, at present, Section Two is\x01",
            "working hard supporting Section One,\x01",
            "turning a blind eye to all other cases.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Spies entering Crossbell... We're in the\x01",
            "middle of sorting every little bit of intel,\x01",
            "especially about that Imperial spy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CED7")

    Jump("loc_D635")

    label("loc_CEDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D0F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D057")

    ChrTalk(
        0xFE,
        "Gnosis...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First of all, as an established tactic,\x01",
            "we were planning to search starting\x01",
            "with Revache supply routes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We simply had a hunch\x01",
            "that it was unlikely to\x01",
            "come in from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway, at the\x01",
            "present stage, it's no use\x01",
            "dwelling upon hypotheses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, we can only\x01",
            "intently crush every\x01",
            "possibility one by one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D0ED")

    label("loc_D057")


    ChrTalk(
        0xFE,
        (
            "Well, anyway, at the\x01",
            "present stage, it's no use\x01",
            "dwelling upon hypotheses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, we can only\x01",
            "intently crush every\x01",
            "possibility one by one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0ED")

    Jump("loc_D635")

    label("loc_D0F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D100")
    Jump("loc_D635")

    label("loc_D100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D2BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D1E2")

    ChrTalk(
        0xFE,
        (
            "Although the Support Section\x01",
            "helped, it seems Raymond did\x01",
            "his best yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's really an unbelievable\x01",
            "that while chasing the fake brand trader\x01",
            "he'd run into terrorist remnants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2B9")

    label("loc_D1E2")


    ChrTalk(
        0xFE,
        (
            "Although Heiyue acted behind the\x01",
            "scenes, it seems Raymond did his\x01",
            "best by himself yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's really an unbelievable\x01",
            "that while chasing the fake brand trader\x01",
            "he'd run into terrorist remnants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2B9")

    Jump("loc_D635")

    label("loc_D2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D3AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2D9")
    Call(0, 25)
    Jump("loc_D3A8")

    label("loc_D2D9")


    ChrTalk(
        0xFE,
        (
            "It was decided that Section Two will be\x01",
            "taking on a few jobs that are normally\x01",
            "within the scope of Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the situation is\x01",
            "what it is. It's really all\x01",
            "hands on deck at this point.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A8")

    Jump("loc_D635")

    label("loc_D3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_D3BB")
    Jump("loc_D635")

    label("loc_D3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_D3C9")
    Jump("loc_D635")

    label("loc_D3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D3D7")
    Jump("loc_D635")

    label("loc_D3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3F2")
    Call(0, 26)
    Jump("loc_D443")

    label("loc_D3F2")


    ChrTalk(
        0xA,
        (
            "Reckless young men, huh?\x01",
            "Man, what's the fun in\x01",
            "causing trouble for others?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D443")

    Jump("loc_D635")

    label("loc_D448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D463")
    Call(0, 27)
    Jump("loc_D635")

    label("loc_D463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5B2")

    ChrTalk(
        0xFE,
        (
            "Well, whatever. We'll be\x01",
            "counting on you if something\x01",
            "comes up in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We of Section Two are\x01",
            "expecting great things\x01",
            "from you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FS-Sir.\x02\x03",
            "(It makes me truly happy\x01",
            "to hear him say\x01",
            "something like that.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Yes. I too feel that\x01",
            "we've received a certain\x01",
            "amount of recognition.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D635")

    label("loc_D5B2")


    ChrTalk(
        0xFE,
        (
            "Well, we'll be counting\x01",
            "on you if anything else\x01",
            "comes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We of Section Two are\x01",
            "expecting great things\x01",
            "from you as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D635")

    TalkEnd(0xFE)
    Return()

    # Function_24_CC7F end

    def Function_25_D639(): pass

    label("Function_25_D639")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Hey, if it isn't the\x01",
            "SSS.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        (
            "#00603FI had a feeling you guys\x01",
            "were going to show up.\x02\x03",
            "#00600FI'm told you've taken on\x01",
            "the Cryptid investigation,\x01",
            "is that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. As expected, you\x01",
            "have sharp ears.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 500)

    ChrTalk(
        0xC,
        (
            "#00603FHmph. It's an official request\x01",
            "from the CGF after all. It's only\x01",
            "natural I receive info about it...\x02\x03",
            "#00600FFrom what I've heard, they're\x01",
            "opponents that can't be gauged\x01",
            "with common sense.\x02\x03",
            "In battle, you'll need to do your\x01",
            "very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThanks for the warning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEven so... You look quite\x01",
            "busy with\x01",
            "counterintelligence work...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Well, a thing like the\x01",
            "independence proposal was\x01",
            "said out loud, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're in a situation where one spy after\x01",
            "the next is being sent by every nation in\x01",
            "Zemuria to find out what we're going to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We have our hands full with\x01",
            "many spies who are just\x01",
            "simply trying to learn that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FA-Are there really so\x01",
            "many...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        (
            "#00601F...In addition, there's the\x01",
            "actions of Red Constellation and\x01",
            "Heiyue as well.\x02\x03",
            "And it's also obvious that we\x01",
            "can't let our guard down dealing\x01",
            "with crimes other than theirs.\x02\x03",
            "#00603FThe current situation is such\x01",
            "that there's truly any number of\x01",
            "cases that must be dealt with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, the situation being what it is, it was\x01",
            "decided that Section Two will undertake a few\x01",
            "jobs normally within the scope of Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because of that, we were\x01",
            "having a little business\x01",
            "meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see... So that's what\x01",
            "you were talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHow to say it... It seems\x01",
            "like it's a tough situation\x01",
            "in a lot of different ways.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 500)

    ChrTalk(
        0xC,
        (
            "#00603FHmph. No matter how restricted\x01",
            "your hand, you've got to play\x01",
            "it as best you can.\x02\x03",
            "#00601FAt any rate, you all must\x01",
            "complete your assigned duties\x01",
            "as well.\x02\x03",
            "The Cryptid case isn't a\x01",
            "problem that can be ignored.\x02",
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

    # Function_25_D639 end

    def Function_26_DDBC(): pass

    label("Function_26_DDBC")

    OP_4B(0xA, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0xA,
        (
            "By the way, about those young men\x01",
            "from the recklessly driven car...\x01",
            "You arrested them yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well, we couldn't leave\x01",
            "things as they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Although it's regrettable\x01",
            "that they were punished\x01",
            "with only a fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "In any case, if you think about the fact\x01",
            "that we haven't seen them in the city\x01",
            "today, maybe it had a small effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sigh*, I hope that's\x01",
            "the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Honestly, if they weren't\x01",
            "foreigners we could've held them in\x01",
            "custody and severely punished them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I guess we can\x01",
            "expect that stuff from\x01",
            "future legislation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Right. Well, for now we\x01",
            "can only do things the\x01",
            "hard way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_E0CA")

    ChrTalk(
        0x101,
        (
            "#00001F(It appears they're\x01",
            "talking about those\x01",
            "three boys.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(It seems like it. I hope\x01",
            "they don't recklessly\x01",
            "drive again...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E10D")

    label("loc_E0CA")


    ChrTalk(
        0x101,
        (
            "#00001F(Yesterday, huh...? Did\x01",
            "something happen in the\x01",
            "city?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E10D")

    SetScenarioFlags(0x13E, 7)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_26_DDBC end

    def Function_27_E123(): pass

    label("Function_27_E123")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Oh, you've got some\x01",
            "fresh personnel with\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Could they be the\x01",
            "rumored new SSS members?\x02",
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
            "And that means that\x01",
            "you're Noｱl from the\x01",
            "CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Muhuhu. If you like, why\x01",
            "don't we get some tea or\x01",
            "something together next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. She says "I'm\x01",
            "sorry."\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Huh...\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "Wait, you there. You're\x01",
            "Wazy Hemisphere of the\x01",
            "Testaments.\x02",
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
            "...My, seeing you up\x01",
            "close, you have quite\x01",
            "the pretty face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, you think so?\x02\x03",
            "#10304FIt's too bad though,\x01",
            "because it looks like\x01",
            "you're not my type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "R-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Wait, why do I have\x01",
            "to be snubbed by a man!?\x02",
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
            "...Jeez, I was listening in\x01",
            "silence, but you're spouting\x01",
            "nothing but nonsense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You too. Follow the\x01",
            "Support Section's example\x01",
            "and grow up a little!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Or if you like, shall I arrange\x01",
            "for you to make a fresh start\x01",
            "at police academy again?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "Inspectooor, please,\x01",
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

    # Function_27_E123 end

    def Function_28_E5DC(): pass

    label("Function_28_E5DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E7F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E779")

    ChrTalk(
        0xFE,
        (
            "Hey, listen to this! They say\x01",
            "that Inspector Donovan will\x01",
            "be reinstated very soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Filling in the hole the inspector\x01",
            "left was difficult in many ways,\x01",
            "but now I'll finally be free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHaha, I'm happy for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI wonder what the\x01",
            "inspector would do if he\x01",
            "heard you say that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "W-Whoops, you're right.\x01",
            "...Keep it a secret, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_E7EF")

    label("loc_E779")


    ChrTalk(
        0xFE,
        (
            "When the inspector comes\x01",
            "back, Section Two will\x01",
            "have some peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alllright, I've got to\x01",
            "my best until then!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E7EF")

    Jump("loc_F079")

    label("loc_E7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_E802")
    Jump("loc_F079")

    label("loc_E802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E8C8")

    ChrTalk(
        0xFE,
        (
            "To be suddenly included in\x01",
            "the State Guard without\x01",
            "any prior notice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't say it out loud, but it's a\x01",
            "real nice case of despotism.\x01",
            "...*sigh*, what the heck is going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F079")

    label("loc_E8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E8D6")
    Jump("loc_F079")

    label("loc_E8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E9D2")

    ChrTalk(
        0xFE,
        (
            "It seems that the Empire\x01",
            "has already denied taking\x01",
            "part in this crime, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, they're looking\x01",
            "for a way to have\x01",
            "negotiations in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because they're doing that,\x01",
            "there's no doubt they're\x01",
            "after some kind of goal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F079")

    label("loc_E9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EA59")

    ChrTalk(
        0xFE,
        (
            "Where did Wald Wales get\x01",
            "his Gnosis...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you suppose it wasn't\x01",
            "via Revache, then just\x01",
            "how did he acquire it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F079")

    label("loc_EA59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EA67")
    Jump("loc_F079")

    label("loc_EA67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ED91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_ECCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC78")

    ChrTalk(
        0xFE,
        (
            "Aah, you guys. Thanks so\x01",
            "much for your help\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right, by the way. Last night\x01",
            "that old lady appeared in my dreams.\x01",
            "For some reason, she was chasing me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, thanks to that I\x01",
            "couldn't get much sleep.\x02",
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
            "#00006F(Now that he's told us this, I\x01",
            "think we'll be seeing her in our\x01",
            "dreams too for some reason.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(...Let's do our best to\x01",
            "try and forget her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_ECC7")

    label("loc_EC78")


    ChrTalk(
        0xFE,
        (
            "In any case, thank you\x01",
            "very much for yesterday.\x01",
            "You really helped me out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECC7")

    Jump("loc_ED8C")

    label("loc_ECCC")


    ChrTalk(
        0xFE,
        (
            "*sigh*, yesterday I had\x01",
            "a really unpleasant\x01",
            "dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was a dream where I\x01",
            "was chased by the grandma\x01",
            "I arrested yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*shiver*, rethinking\x01",
            "about it, I start to\x01",
            "sweat badly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED8C")

    Jump("loc_F079")

    label("loc_ED91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_ED9F")
    Jump("loc_F079")

    label("loc_ED9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_EDAD")
    Jump("loc_F079")

    label("loc_EDAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EDBB")
    Jump("loc_F079")

    label("loc_EDBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EDC9")
    Jump("loc_F079")

    label("loc_EDC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_EFB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF09")

    ChrTalk(
        0xFE,
        (
            "*sigh*. These days, tensions\x01",
            "at HQ are always very high. I\x01",
            "really can't stand it anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although pressure from congressmen and\x01",
            "the top brass has decreased for now,\x01",
            "the state has a heap of problems...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, I wonder when in\x01",
            "the world I'll be able to\x01",
            "take it easy a little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_EFB4")

    label("loc_EF09")


    ChrTalk(
        0xFE,
        (
            "Well, at any rate, I can only\x01",
            "do my best to support to Mayor\x01",
            "Dieter's political reforms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope we get a salary\x01",
            "increase for for the\x01",
            "conference... Just kidding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFB4")

    Jump("loc_F079")

    label("loc_EFB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F079")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFD4")
    Call(0, 27)
    Jump("loc_F079")

    label("loc_EFD4")


    ChrTalk(
        0xFE,
        (
            "*sigh*, once again the\x01",
            "Inspector touched a sore\x01",
            "spot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to get my act together a\x01",
            "little more too... It's just that\x01",
            "I can't change my personality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F079")

    TalkEnd(0xFE)
    Return()

    # Function_28_E5DC end

    def Function_29_F07D(): pass

    label("Function_29_F07D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F08E")
    Jump("loc_F74A")

    label("loc_F08E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F09C")
    Jump("loc_F74A")

    label("loc_F09C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F35E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F28E")

    ChrTalk(
        0xC,
        (
            "#00600FIt's you, huh.\x02\x03",
            "#00603F...I heard about Orlando.\x01",
            "It seems things have\x01",
            "become really troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYes. However, we'll\x01",
            "bring him back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603FHmph, I see. I've got nothing to say,\x01",
            "then.\x02\x03",
            "#00600FAnyway, the situation is what it is.\x01",
            "Of course there's a whole load of\x01",
            "work I'd like to push on you as well.\x02\x03",
            "For that reason as well, go resolve\x01",
            "this problem with your colleague at\x01",
            "once.\x02",
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
    Jump("loc_F359")

    label("loc_F28E")


    ChrTalk(
        0xC,
        (
            "#00603FAfter I'm finished with the business\x01",
            "meeting, I intend to head to the mayor's\x01",
            "office to discuss countermeasures.\x02\x03",
            "#00600FAnyway, you guys should take care of\x01",
            "whatever you need to do at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F359")

    Jump("loc_F74A")

    label("loc_F35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F36C")
    Jump("loc_F74A")

    label("loc_F36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F37A")
    Jump("loc_F74A")

    label("loc_F37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F388")
    Jump("loc_F74A")

    label("loc_F388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3A3")
    Call(0, 25)
    Jump("loc_F453")

    label("loc_F3A3")


    ChrTalk(
        0xC,
        (
            "#00600FWe currently have a huge pile of\x01",
            "cases, but... At any rate, leave\x01",
            "the counterespionage to us.\x02\x03",
            "You need only think of carrying\x01",
            "out your own duties to the very\x01",
            "end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F453")

    Jump("loc_F74A")

    label("loc_F458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F466")
    Jump("loc_F74A")

    label("loc_F466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F48E")
    Call(0, 30)
    Jump("loc_F552")

    label("loc_F48E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4A0")
    Call(0, 31)
    Jump("loc_F552")

    label("loc_F4A0")


    ChrTalk(
        0xC,
        (
            "#00603FOn my end, I intend to stay here\x01",
            "for a while to keep a watchful eye\x01",
            "on intel from across the state.\x02\x03",
            "#00600FTell me directly if anything\x01",
            "happens. Contact me anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F552")

    Jump("loc_F720")

    label("loc_F557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6B8")

    ChrTalk(
        0xFE,
        (
            "#00603FThe Imperial Army Intelligence Division\x01",
            "and the Republican Rocksmith Agency...\x01",
            "They're not opponents to be taken lightly.\x02\x03",
            "If those two were in contact... There\x01",
            "can't be any doubt that they're plotting\x01",
            "something in secret.\x02\x03",
            "#00600FAnyway, for now we can only do what we can\x01",
            "as police.\x02\x03",
            "Contact me if anything else happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_F720")

    label("loc_F6B8")


    ChrTalk(
        0xFE,
        (
            "#00600FAnyway, for now we can\x01",
            "only do what we can as\x01",
            "police.\x02\x03",
            "Contact me if anything\x01",
            "else happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F720")

    Jump("loc_F74A")

    label("loc_F725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F733")
    Jump("loc_F74A")

    label("loc_F733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F741")
    Jump("loc_F74A")

    label("loc_F741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F74A")

    label("loc_F74A")

    TalkEnd(0xFE)
    Return()

    # Function_29_F07D end

    def Function_30_F74E(): pass

    label("Function_30_F74E")

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
        "#00600F#2PYou guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P...Need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PYes... There's something\x01",
            "we absolutely must\x01",
            "report to Section One.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reported that Kilika and\x01",
            "Lechter showed up in the\x01",
            "city.\x02",
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
            "Key figures of both the Imperial\x01",
            "Army Intelligence Division and the\x01",
            "Rocksmith Agency in the city...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PDudley, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6P...What do you think about\x01",
            "this?\x02\x03",
            "The trade conference is\x01",
            "tomorrow and spies from the\x01",
            "two major powers showed up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PIt's unlikely to be a\x01",
            "coincidence, isn't it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHehe. They both said\x01",
            "they're here on\x01",
            "vacation, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PIt's obviously way too\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2PThey must have some reason for\x01",
            "being here.\x02\x03",
            "#00600FHowever, if anything, I'd say you\x01",
            "should have been able to sense that\x01",
            "since you spoke with them directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#12P...You might be right\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#2P...And so, I'll ask you,\x01",
            "Bannings. Why do you think they\x01",
            "showed up in the city?\x02\x03",
            "#00603FIn the conversations you had\x01",
            "with them, how they got here...\x01",
            "There must be a hint somewhere.\x02\x03",
            "#00600FI don't care if you guess, just\x01",
            "tell me.\x02",
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
            "Why have Kilika and Lechter\x01",
            "showed up in the city?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "To guard their head of state\x01",      # 0
            "A breather and shopping\x01",           # 1
            "Secret talks\x01",                      # 2
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
        (0, "loc_FD8F"),
        (1, "loc_FF24"),
        (2, "loc_100CC"),
        (SWITCH_DEFAULT, "loc_10122"),
    )


    label("loc_FD8F")


    ChrTalk(
        0x101,
        (
            "#00001F#6PTo guard their head of state,\x01",
            "perhaps?\x02\x03",
            "#00003FThey'd need to understand the\x01",
            "layout of Crossbell City, in case\x01",
            "something happens, or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2P...That's unlikely.\x02\x03",
            "#00600FSecurity is outside a spy's jurisdiction,\x01",
            "and both of them visited Crossbell some\x01",
            "months ago in the first place.\x02\x03",
            "They'd have no need to do that at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PThat does make sense...\x02",
    )

    CloseMessageWindow()
    Jump("loc_10122")

    label("loc_FF24")


    ChrTalk(
        0x101,
        (
            "#00001F#6P...Could they really be\x01",
            "here for R&R, just like\x01",
            "they said?\x02\x03",
            "#00003FThough with the approaching\x01",
            "trade conference, it's hard\x01",
            "to say definitively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2P...That's impossible.\x02\x03",
            "#00600FThinking about the way they\x01",
            "evaded you, it could be nothing\x01",
            "more than a simple disguise.\x02\x03",
            "#00606F*sigh*, oh brother... I thought\x01",
            "you'd have done a little\x01",
            "better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PW-Wait a moment. Umm, in\x01",
            "that case...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10122")

    label("loc_100CC")

    OP_2C(0xA3, 0x1)

    ChrTalk(
        0x101,
        (
            "#00001F#6P...I think it's possible\x01",
            "they were trying to talk\x01",
            "in secret.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10122")

    label("loc_10122")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1019D")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00001F#6PThat's right, maybe... I\x01",
            "think those two were\x01",
            "trying to talk in secret.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1019D")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10217():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10217)
    Sleep(50)

    def lambda_10227():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10227)
    Sleep(50)

    def lambda_10237():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10237)
    Sleep(50)

    def lambda_10247():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10247)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0xD,
        "#5PSecret talks... you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#2PHmm... What makes you\x01",
            "say that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWitnesses first spotted each of them\x01",
            "in Waterfront Area.\x02\x03",
            "#00001FBefore we started pursuing them,\x01",
            "they were both in the same district.\x01",
            "I can't think that's a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#5PYes... That's right.\x02\x03",
            "#00100FA tour of IBC in Waterfront\x01",
            "Area by the President has been\x01",
            "planned since yesterday...\x02\x03",
            "It's possible IBC was a\x01",
            "convenient place to meet for\x01",
            "secret discussions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PEven the Mishy event being\x01",
            "held then might have been\x01",
            "good cover for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PThey met in secret, in the guises\x01",
            "of taking a breather and shopping\x01",
            "for the President, respectively...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5P...Everything seems to\x01",
            "line up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PBut if they discussed\x01",
            "something in secret,\x01",
            "what did they discuss?\x02\x03",
            "To begin with, shouldn't\x01",
            "the Empire and Republic\x01",
            "be enemies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5P...It's not out of the question.\x02\x03",
            "#00103FBecause of the cult incident, many\x01",
            "Imperial and Republican faction\x01",
            "congressmen have been ousted...\x02\x03",
            "And because of cooperation between the new\x01",
            "mayor and chairman, Crossbell gradually\x01",
            "started to have an influential voice.\x02\x03",
            "#00101FIn a situation like this... Neither the\x01",
            "Empire nor the Republic would leave things\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#12PI see, so the major\x01",
            "powers interests are\x01",
            "aligned on that point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00608F#2PI can't confirm it, but...\x01",
            "It's certain there's something\x01",
            "going on behind closed doors.\x02\x03",
            "#00603F...That's all I can say at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1082E():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1082E)
    Sleep(50)

    def lambda_1083E():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1083E)
    Sleep(50)

    def lambda_1084E():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1084E)
    Sleep(50)

    def lambda_1085E():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1085E)
    Sleep(50)

    def lambda_1086E():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1086E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0xD,
        (
            "#5PSection One will continue\x01",
            "tracking Lechter Arundel\x01",
            "and Kilika Rouran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PNice work on that\x01",
            "report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PWell, we're just happy\x01",
            "we could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PI hope tomorrow's\x01",
            "conference ends without\x01",
            "incident, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2PWe can only do the best\x01",
            "we can.\x02\x03",
            "#00601FContact me if anything\x01",
            "else happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PAlright. Thank you very\x01",
            "much.\x02",
        )
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

    # Function_30_F74E end

    def Function_31_10A52(): pass

    label("Function_31_10A52")

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
            "#00600FYou guys, huh. Did\x01",
            "anything happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo. Nothing yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603FI see... But don't let your guard\x01",
            "down.\x02\x03",
            "I think you felt it too, but the\x01",
            "whole city is a little on edge on\x01",
            "account of the VIPs' visit.\x02\x03",
            "#00600FIf there was something out of the\x01",
            "ordinary, it would be easy to miss\x01",
            "it in this kind of atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYou're certainly right\x01",
            "about that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHehe. We must be\x01",
            "vigilant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBy the way Dudley, are\x01",
            "you going to stay here\x01",
            "for a while?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "#00603FMore or less. In any case, I plan to be\x01",
            "on duty here at HQ until the VIPs' visit\x01",
            "to the Arc-en-Ciel theatre begins.\x02\x03",
            "#00600FTell me directly if anything happens.\x01",
            "Contact me anytime.\x02",
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

    # Function_31_10A52 end

    def Function_32_10D6D(): pass

    label("Function_32_10D6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10D7E")
    Jump("loc_10E74")

    label("loc_10D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10DA7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10DA2")

    ChrTalk(
        0x11,
        "...Tch...\x02",
    )

    CloseMessageWindow()

    label("loc_10DA2")

    Jump("loc_10E74")

    label("loc_10DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_10DB5")
    Jump("loc_10E74")

    label("loc_10DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10E74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DDC")
    Call(0, 33)
    Jump("loc_10E74")

    label("loc_10DDC")

    ClearChrFlags(0x11, 0x10)

    ChrTalk(
        0x11,
        (
            "Given that you can only fine\x01",
            "us if you arrest us, you're\x01",
            "working way too hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hehe, do you police want\x01",
            "to earn pocket money\x01",
            "that badly?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E74")

    TalkEnd(0xFE)
    Return()

    # Function_32_10D6D end

    def Function_33_10E78(): pass

    label("Function_33_10E78")


    ChrTalk(
        0xF,
        (
            "Well then... Where are\x01",
            "you living at present?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmph, we have no\x01",
            "obligation to answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Although, it's a place commoners\x01",
            "like you wouldn't be able to\x01",
            "live... I'll just say that.\x02",
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
        (
            "#00001F(H-Hang in there,\x01",
            "Frantz...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_33_10E78 end

    def Function_34_10F82(): pass

    label("Function_34_10F82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10F93")
    Jump("loc_110D6")

    label("loc_10F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1100F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1100A")

    ChrTalk(
        0x12,
        (
            "A suspension, a driving\x01",
            "license suspensiooon?\x02",
        )
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

    label("loc_1100A")

    Jump("loc_110D6")

    label("loc_1100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1101D")
    Jump("loc_110D6")

    label("loc_1101D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_110D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_110D6")

    ChrTalk(
        0x12,
        (
            "You guys... Weren't you\x01",
            "who put together the\x01",
            "barricade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hmph, what shallow thinking. If\x01",
            "you get too carried away, nothing\x01",
            "good will come of it, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110D6")

    TalkEnd(0xFE)
    Return()

    # Function_34_10F82 end

    def Function_35_110DA(): pass

    label("Function_35_110DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_110EB")
    Jump("loc_111F0")

    label("loc_110EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11184")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1117F")

    ChrTalk(
        0x13,
        (
            "*sigh*, we got too\x01",
            "carried away this\x01",
            "time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "The car was totaled too.\x01",
            "We should do as we're\x01",
            "told for a little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1117F")

    Jump("loc_111F0")

    label("loc_11184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11192")
    Jump("loc_111F0")

    label("loc_11192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_111F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_111F0")

    ChrTalk(
        0x13,
        (
            "*sigh*, I want to go home\x01",
            "already. This questioning\x01",
            "is getting old.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111F0")

    TalkEnd(0xFE)
    Return()

    # Function_35_110DA end

    def Function_36_111F4(): pass

    label("Function_36_111F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11212")
    Call(0, 38)
    Jump("loc_11270")

    label("loc_11212")


    ChrTalk(
        0xFE,
        (
            "Frankly, I feel like I'm still\x01",
            "dreaming, but... Really, I\x01",
            "wonder what's going to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11270")

    Jump("loc_115A2")

    label("loc_11275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11283")
    Jump("loc_115A2")

    label("loc_11283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11291")
    Jump("loc_115A2")

    label("loc_11291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_113D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_113CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11361")

    ChrTalk(
        0xE,
        (
            "You really did a great\x01",
            "job handling the\x01",
            "reckless driving case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please leave these kids\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We'll be counting on you\x01",
            "if we need anything in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_113C6")

    label("loc_11361")


    ChrTalk(
        0xE,
        (
            "Please leave these kids\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "We'll be counting on you\x01",
            "if we need anything in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113C6")

    Jump("loc_113CB")

    label("loc_113CB")

    Jump("loc_115A2")

    label("loc_113D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_113DE")
    Jump("loc_115A2")

    label("loc_113DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_113EC")
    Jump("loc_115A2")

    label("loc_113EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_113FA")
    Jump("loc_115A2")

    label("loc_113FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11408")
    Jump("loc_115A2")

    label("loc_11408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11416")
    Jump("loc_115A2")

    label("loc_11416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11424")
    Jump("loc_115A2")

    label("loc_11424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11432")
    Jump("loc_115A2")

    label("loc_11432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_115A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_115A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1154A")
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
        (
            "How about reflecting on\x01",
            "it a little!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmph, don't be such a\x01",
            "hothead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Reflecting,\x01",
            "reflecting... There, I\x01",
            "reflected on it.\x02",
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
    Jump("loc_1159D")

    label("loc_1154A")


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
        (
            "How about reflecting on\x01",
            "it a little!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1159D")

    Jump("loc_115A2")

    label("loc_115A2")

    TalkEnd(0xFE)
    Return()

    # Function_36_111F4 end

    def Function_37_115A6(): pass

    label("Function_37_115A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1167C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115C4")
    Call(0, 38)
    Jump("loc_11677")

    label("loc_115C4")


    ChrTalk(
        0xFE,
        (
            "Nevertheless... The\x01",
            "President's speech seemed\x01",
            "like a declaration of war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though we have the State\x01",
            "Guard, I can't think they'd be\x01",
            "able to oppose the major powers...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11677")

    Jump("loc_118D9")

    label("loc_1167C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1168A")
    Jump("loc_118D9")

    label("loc_1168A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11752")

    ChrTalk(
        0xFE,
        (
            "The night has finally passed,\x01",
            "but... The situation's only\x01",
            "growing worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, although I'm from the Patrol\x01",
            "Division, I plan to focus even more\x01",
            "on what I can do from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D9")

    label("loc_11752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11817")

    ChrTalk(
        0xF,
        (
            "It's still hard to say that\x01",
            "we've become able to strictly\x01",
            "punish foreigners, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This case is an important step\x01",
            "as well. We police must do our\x01",
            "best without losing heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118D9")

    label("loc_11817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11825")
    Jump("loc_118D9")

    label("loc_11825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11833")
    Jump("loc_118D9")

    label("loc_11833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11841")
    Jump("loc_118D9")

    label("loc_11841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1184F")
    Jump("loc_118D9")

    label("loc_1184F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1185D")
    Jump("loc_118D9")

    label("loc_1185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1186B")
    Jump("loc_118D9")

    label("loc_1186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11879")
    Jump("loc_118D9")

    label("loc_11879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_118D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11894")
    Call(0, 33)
    Jump("loc_118D9")

    label("loc_11894")

    ClearChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "(Where are these guys'\x01",
            "bad personalities coming\x01",
            "from...!?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118D9")

    TalkEnd(0xFE)
    Return()

    # Function_37_115A6 end

    def Function_38_118DD(): pass

    label("Function_38_118DD")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(
        0xE,
        (
            "Ah, Lloyd. Things have\x01",
            "gotten serious.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "Did you hear anything at\x01",
            "the Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAh, no, nothing...\x02\x03",
            "#00001FWe're still waiting for\x01",
            "chief to contact us with\x01",
            "the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I understand, it's the\x01",
            "same here at the Patrol\x01",
            "Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I heard we'll get an official\x01",
            "notification as soon as the\x01",
            "conference ends, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Really, we can't even\x01",
            "guess what's going to\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Anyhow, all we can do\x01",
            "for now is follow the\x01",
            "developments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Guys, you seem to be\x01",
            "acting somehow on your\x01",
            "own terms...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "How should I put it... Be\x01",
            "careful to not attract the\x01",
            "attention of the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x18F, 6)
    Return()

    # Function_38_118DD end

    def Function_39_11B91(): pass

    label("Function_39_11B91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_11BA2")
    Jump("loc_12318")

    label("loc_11BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11BB0")
    Jump("loc_12318")

    label("loc_11BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_11D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CAB")

    ChrTalk(
        0xFE,
        (
            "The police force has been split\x01",
            "in half. One half is on standby\x01",
            "as support personnel for the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other half will\x01",
            "reinforce city patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Precisely because of\x01",
            "these hard times, we\x01",
            "must support each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_11D23")

    label("loc_11CAB")


    ChrTalk(
        0xFE,
        (
            "We can't have only the\x01",
            "CGF shed blood, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What good are we police\x01",
            "if we can't help during\x01",
            "hard times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D23")

    Jump("loc_12318")

    label("loc_11D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11DD5")

    ChrTalk(
        0xFE,
        (
            "They're troublesome kids,\x01",
            "but they're relatively\x01",
            "complaint today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard Kate shouted in that\x01",
            "thundering voice of hers...\x01",
            "Perhaps it was effective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12318")

    label("loc_11DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11DE6")
    Call(0, 40)
    Jump("loc_12318")

    label("loc_11DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11DF4")
    Jump("loc_12318")

    label("loc_11DF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11E02")
    Jump("loc_12318")

    label("loc_11E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11E10")
    Jump("loc_12318")

    label("loc_11E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11EBA")

    ChrTalk(
        0xFE,
        (
            "Well, the unveiling ceremony\x01",
            "is over and I can finally\x01",
            "take a short breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Phew. As expected,\x01",
            "nothing is better than\x01",
            "coffee for a short break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12318")

    label("loc_11EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11EC8")
    Jump("loc_12318")

    label("loc_11EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_11F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EE3")
    Call(0, 26)
    Jump("loc_11F60")

    label("loc_11EE3")


    ChrTalk(
        0xFE,
        (
            "Hmm. That too could be\x01",
            "called self-assertion, I\x01",
            "believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Isn't the party who\x01",
            "suffers trouble the one\x01",
            "who bears it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F60")

    Jump("loc_12318")

    label("loc_11F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_12318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121D1")

    ChrTalk(
        0xFE,
        (
            "Oh, it's you. There's some\x01",
            "new faces, but you're still\x01",
            "the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So that means you've\x01",
            "finally resumed your\x01",
            "activities, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thankfully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHmm, you're chief of the\x01",
            "Patrol Division, I\x01",
            "presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FUmm, pleased to meet\x01",
            "you.\x02",
        )
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
            "Hmm. Anyhow, it looks like\x01",
            "you've got quite the interesting\x01",
            "ensemble of talented people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well in any case, we're\x01",
            "expecting great things\x01",
            "from you all, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on you'll have\x01",
            "to go over your section\x01",
            "fence and work non-stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FYes, thank you very\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 3)
    Jump("loc_12318")

    label("loc_121D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1225A")

    ChrTalk(
        0x14,
        (
            "Hmm, even so, some\x01",
            "troublesome kids have\x01",
            "arrived, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well, it'll be fine if I\x01",
            "leave them to Kate and\x01",
            "Frantz.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12318")

    label("loc_1225A")


    ChrTalk(
        0xFE,
        (
            "Phew! After I drink\x01",
            "this, I'll have to go to\x01",
            "back to the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man oh man. These days, I have to put\x01",
            "up with one meeting after the next with\x01",
            "my body on the verge of retirement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12318")

    TalkEnd(0xFE)
    Return()

    # Function_39_11B91 end

    def Function_40_1231C(): pass

    label("Function_40_1231C")

    OP_4B(0x14, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)

    ChrTalk(
        0x14,
        (
            "When trains from the\x01",
            "Republic come, we'll have\x01",
            "deal with transfers again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "From now on, you guys will\x01",
            "be acting as support at\x01",
            "the station and airport.\x02",
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
        (
            "We'll head to those\x01",
            "locations at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_40_1231C end

    def Function_41_12417(): pass

    label("Function_41_12417")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_124E2")

    ChrTalk(
        0xFE,
        (
            "As the Patrol Division,\x01",
            "we've resumed patrols in\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's also the possibility this\x01",
            "confusion will negatively impact security.\x01",
            "We've got to be careful on our patrols.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125D0")

    label("loc_124E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_124F0")
    Jump("loc_125D0")

    label("loc_124F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_125C4")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking we'd get a\x01",
            "break after finally repairing HQ, we\x01",
            "got included in the State Guard...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I'm a soldier...\x01",
            "As you might expect, I can't\x01",
            "go along with that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125D0")

    label("loc_125C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_125D0")
    Call(0, 40)

    label("loc_125D0")

    TalkEnd(0xFE)
    Return()

    # Function_41_12417 end

    def Function_42_125D4(): pass

    label("Function_42_125D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12696")

    ChrTalk(
        0xFE,
        (
            "Section Chief Joe Ridge headed to the\x01",
            "police academy to deal with the\x01",
            "aftermath after the State Guard left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With our Section Chief\x01",
            "away, we've got to guard\x01",
            "the place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127B2")

    label("loc_12696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_126A4")
    Jump("loc_127B2")

    label("loc_126A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1277C")

    ChrTalk(
        0xFE,
        (
            "Just when I was thinking I could have\x01",
            "a break after finally restoring HQ, we\x01",
            "got included in the State Guard...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on, I'm a soldier...\x01",
            "As you might expect, I can't\x01",
            "go along with that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127B2")

    label("loc_1277C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1278A")
    Jump("loc_127B2")

    label("loc_1278A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12798")
    Jump("loc_127B2")

    label("loc_12798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_127A6")
    Jump("loc_127B2")

    label("loc_127A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_127B2")
    Call(0, 40)

    label("loc_127B2")

    TalkEnd(0xFE)
    Return()

    # Function_42_125D4 end

    def Function_43_127B6(): pass

    label("Function_43_127B6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think you already heard about it, but it was\x01",
            "decided that the police will be reorganized\x01",
            "into a unit under the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An explanation of the new\x01",
            "structure to those responsible is\x01",
            "underway in the 2F meeting room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone, please wait in the\x01",
            "detached building until\x01",
            "instructions come from the top.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_127B6 end

    def Function_44_128FC(): pass

    label("Function_44_128FC")

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

    def lambda_12987():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12987)
    Sleep(50)

    def lambda_129A4():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_129A4)
    Sleep(50)

    def lambda_129C1():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_129C1)
    Sleep(50)

    def lambda_129DE():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_129DE)
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
            "You're the people of the\x01",
            "Special SUpport Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think you already heard about it, but it was\x01",
            "decided that the police will be reorganized\x01",
            "into a unit under the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "An explanation of the new\x01",
            "structure to those responsible is\x01",
            "underway in the 2F meeting room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone, please wait in the\x01",
            "detached building until\x01",
            "instructions come from the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You're still free to move about\x01",
            "on 1F, but please refrain from\x01",
            "any unnecessary behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please understand that you can\x01",
            "be taken into custody if your\x01",
            "behavior is deemed suspicious.\x02",
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
        (
            "#12P#00108F(He's really coercive\x01",
            "somehow...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F(Yeah, but it's extremely\x01",
            "unlikely someone will\x01",
            "ineptly defy him.)\x02",
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

    # Function_44_128FC end

    def Function_45_12DF6(): pass

    label("Function_45_12DF6")

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
            "And then─ It was several days before the\x01",
            "heads of state would enter Crossbell and\x01",
            "Orchis Tower would be unveiled.\x02\x03",
            "The Support Section was summoned to the\x01",
            "police HQ conference room.\x07\x00\x02",
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
            "─We'll use the following structure\x01",
            "for the three days starting\x01",
            "tomorrow.\x02\x03",
            "The Guardian Force has already\x01",
            "started inspections at Bellguard\x01",
            "and Tangram gates as well as the\x02\x03",
            "national borders.\x02\x03",
            "Section Chief Joe Ridge and\x01",
            "Inspector Donovan are in charge of\x01",
            "the city.\x02",
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
            "#5PYes, and all members of the\x01",
            "Patrol Division have been\x01",
            "assigned patrols within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PWe'll be on high alert\x01",
            "until the meeting's\x01",
            "over.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#5PSection Two will focus\x01",
            "primarily on the station,\x01",
            "airport and trade boundaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAll of our personnel will\x01",
            "be on alert until the end\x01",
            "of the conference as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FSection One is in charge of\x01",
            "security HQ.\x02\x03",
            "#00600FI'd brag that we're able to\x01",
            "deal with every emergency\x01",
            "we can think of, but...\x02",
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
            "#12P#01003F...Even the strictest of\x01",
            "security measures is by\x01",
            "no means perfect.\x02\x03",
            "#01000FThat's where we come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00604FYes. As I've said, Chief Sergei will\x01",
            "be in charge of public relations and\x01",
            "assigned to police HQ.\x02\x03",
            "#00602FI'd also like to ask you to handle\x01",
            "communications with the Guardian\x01",
            "Force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01006FMan, you drive your men\x01",
            "hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHaha, well anyway, it's\x01",
            "because you've stuck your nose\x01",
            "in a lot of different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt'll be a stronger\x01",
            "security structure if we\x01",
            "put you in our blind spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PYeah. You really live up\x01",
            "to your reputation as\x01",
            ""Sergei the Rear".\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#12P#01005FLeave me alone, that was\x01",
            "a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FSergei The Rear...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHaha... I see why he's\x01",
            "called that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x1)
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#11P#01006FI'm telling you, that\x01",
            "was a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x19, 0x2)
    Sleep(200)

    ChrTalk(
        0x19,
        (
            "#12P#01000FAnd... Are you okay with\x01",
            "these guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FYes, I don't mind.\x02\x03",
            "#00600FI think we'll use them\x01",
            "as a reserve squad for a\x01",
            "little while.\x02",
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
        "#10105FReserve, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FWe'll continue our normal support\x01",
            "activities. And if something\x01",
            "happens, we'll provide backup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00606FYeah, exactly.\x02\x03",
            "The Bracer Guild will do the same,\x01",
            "but we can't fully rely on them.\x02\x03",
            "#00601FAlso... Now that those guys have\x01",
            "entered Crossbell, I want insurance\x01",
            "against unexpected situations.\x02",
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
        (
            "#00303F─Red Constellation,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#00601FYes...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "#00603FThe Red Constellation jaeger\x01",
            "corps...\x02\x03",
            "Said to be one of the\x01",
            "strongest jaeger corps in\x01",
            "western Zemuria.\x02\x03",
            "#00601FWe've confirmed that a large\x01",
            "number of their members have\x01",
            "entered Crossbell.\x02\x03",
            "By the way, they had a\x01",
            "conflict with Heiyue in the\x01",
            "Republic about a year ago.\x02",
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
        (
            "#5PHmm, so they're a\x01",
            "dangerous lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PCould they be planning on\x01",
            "continuing that conflict with\x01",
            "Heiyue, here in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FNo. Normally, jaeger corps act\x01",
            "based on mira alone.\x02\x03",
            "Although there was a prior\x01",
            "conflict, that doesn't mean\x01",
            "it's a reason to start another.\x02\x03",
            "#00600FIsn't that right, Orlando?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F...I guess.\x02\x03",
            "#00303FDifferently from the mafia, who place\x01",
            "importance on territory, to jaegers,\x01",
            "mira and battlefields are everything.\x02\x03",
            "Yesterday's enemy is today's ally...\x01",
            "That could be an everyday occurrence\x01",
            "for them.\x02\x03",
            "#00300FIn that sense, they probably aren't\x01",
            "hung up over the previous conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10304FHehe. If that's the\x01",
            "case, then a mystery\x01",
            "arises.\x02\x03",
            "#10302FNamely, the reason Red\x01",
            "Constellation has\x01",
            "entered Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11P#00606FSection One is looking into\x01",
            "it, but we haven't been able\x01",
            "to confirm their motives yet.\x02\x03",
            "#00601FHowever, it's certain they're\x01",
            "receiving support from the\x01",
            "Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FMaybe they're trying to\x01",
            "do something related to\x01",
            "the trade conference...\x02\x03",
            "#00101FPerhaps they're trying\x01",
            "to stop the rise of the\x01",
            "Republic-aligned Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01006FWell, either of those are possibilities.\x02\x03",
            "#01000FIn any case, they're an element that can't\x01",
            "be ignored with respect to the conference.\x01",
            "There can't be any doubt about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FYes, naturally.\x02\x03",
            "#00600F...By the way, it appears Red\x01",
            "Constellation has been stretching\x01",
            "their legs in Crossbell's outskirts.\x02\x03",
            "I'd like to get a feel for their\x01",
            "actions by going to each of the\x01",
            "places they've been sighted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FUnderstood.\x02\x03",
            "#00001FWe'll gather intel on Red\x01",
            "Constellation while taking care\x01",
            "of our support requests, then.\x02",
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
            "#6P#00100FWe'll back up the other sections\x01",
            "if anything happens, so don't\x01",
            "hesitate to contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PYeah, we're counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PWe'll be counting on\x01",
            "you, then.\x02",
        )
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

    # Function_45_12DF6 end

    def Function_46_14590(): pass

    label("Function_46_14590")

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

    def lambda_14613():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14613)
    Sleep(50)

    def lambda_14630():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14630)
    Sleep(50)

    def lambda_1464D():
        OP_98(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1464D)
    Sleep(50)

    def lambda_1466A():
        OP_98(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1466A)
    Sleep(50)
    SetCameraDistance(20430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hello everyone.\x02",
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
        (
            "#5P#01902FOh, hey guys! And big\x01",
            "sis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FI told you not to call\x01",
            "me that while we're on\x01",
            "duty, didn't I?\x02",
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

    def lambda_147E1():
        OP_98(0x101, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_147E1)
    Sleep(50)

    def lambda_147FE():
        OP_98(0x102, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_147FE)
    Sleep(50)

    def lambda_1481B():
        OP_98(0x109, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1481B)
    Sleep(50)

    def lambda_14838():
        OP_98(0x105, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14838)
    Sleep(50)
    TurnDirection(0x9, 0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, thanks for your\x01",
            "hard work, Rebecca.\x02",
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
            "Ahaha. The Special\x01",
            "Support Section is hard\x01",
            "at work already, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Will you be starting on\x01",
            "today's support requests\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes. We have new members,\x01",
            "so we'll do them while\x01",
            "patrolling the city.\x02\x03",
            "We're here for Section\x01",
            "One's request. Where is\x01",
            "Detective Emma?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's waiting for you in\x01",
            "the conference room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A request from Section\x01",
            "One... You've made quite\x01",
            "the name for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somehow, I'm deeply\x01",
            "moved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo, you've got it all\x01",
            "wrong...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha, well, we'll be fine as\x01",
            "long as it's not something\x01",
            "unreasonable being forced on us.\x02",
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
            "#12P#00001FA-Anyway, let's at least\x01",
            "hear what Detective Emma\x01",
            "has to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#01909FGood luck everyone~.\x02",
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

    # Function_46_14590 end

    def Function_47_14BDC(): pass

    label("Function_47_14BDC")

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
            "Detective Bannings...\x01",
            "You're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FThanks, Detective. You\x01",
            "were a big help to me\x01",
            "back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If you mean your training\x01",
            "at Section One, it wasn't\x01",
            "my intention to aid you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the end, I was merely\x01",
            "following Mr. Dudley's\x01",
            "orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't mean to be rude but... I'm at a loss\x01",
            "at your refusal of an appointment to Section\x01",
            "One, instead of returning to the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FS-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F(Looks like a lot\x01",
            "happened...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100F(The other sections seem\x01",
            "to want Lloyd for\x01",
            "themselves, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well anyway, let's get\x01",
            "down to business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Can I assume you're here\x01",
            "because you're going to\x01",
            "help us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes, of course.\x02\x03",
            "#00001F...I understand Lechter\x01",
            "Arundel has entered\x01",
            "Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "That's what we believe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...But even now, that\x01",
            "information is still\x01",
            "unconfirmed.\x02",
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
            "#12P#00105FYou can't confirm his\x01",
            "location?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The intel saying that he\x01",
            "entered Crossbell is\x01",
            "unreliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There are reports of someone like\x01",
            "him... But when we try to track them\x01",
            "down, they disappear like a mirage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's likely he's sensing\x01",
            "our movements and\x01",
            "evading capture.\x02",
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
        (
            "#12P#10106FHe's quite the\x01",
            "formidable opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell if it really is\x01",
            "him, then I'm not\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And so, I want you to\x01",
            "confirm whether Lechter\x01",
            "Arundel is really here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Did he really enter\x01",
            "Crossbell? Or was that\x01",
            "just false information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If possible, I also want you to\x01",
            "confirm his identity as an Imperial\x01",
            "army officer and government secretary.\x02",
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
            "You came in contact with\x01",
            ""him" several times\x01",
            "previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I decided to bet on\x01",
            "that.\x02",
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
        "#12P#00012FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha. For an elite, your\x01",
            "response is unexpectedly\x01",
            "flexible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Ugh... We're out of\x01",
            "options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If I split our forces we could capture him, but if\x01",
            "handled poorly it could cause an international incident.\x01",
            "There are other drawbacks to consider as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "...If Mr. Dudley were\x01",
            "here, I wouldn't have\x01",
            "asked you.\x02",
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
            "#12P#00005FBy the way... Where is\x01",
            "Mr. Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yesterday evening, he headed\x01",
            "to Liberl for a trade\x01",
            "conference security briefing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think he'll be back\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FHe seems rather busy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That's why I want this\x01",
            "handled before he gets\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Because he's the kind of person\x01",
            "that'd take on something like this no\x01",
            "matter how tired he is from his trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FThat does sound like\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FUnderstood. We'll accept\x01",
            "the request.\x02\x03",
            "#00000FFor starters... Do you\x01",
            "know where Captain\x01",
            "Lechter was spotted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmm... I don't know if\x01",
            "it's accurate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But we did get intel\x01",
            "that he was seen on Back\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FBack Street... So near\x01",
            "the old Revache\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha, seems like a place\x01",
            "he'd visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FUnderstood. We'll begin\x01",
            "our investigation at\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'll be standing by at Section One,\x01",
            "so please have the receptionist call\x01",
            "for me when it's time to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, if you'll excuse\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_15A00():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A00)

    def lambda_15A0D():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A0D)

    def lambda_15A1A():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15A1A)

    def lambda_15A27():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15A27)
    OP_68(-57500, 1500, 16430, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_15A79():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15A79)

    def lambda_15A86():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A86)

    def lambda_15A93():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15A93)

    def lambda_15AA0():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15AA0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#11P#00006F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FShe must have helped you\x01",
            "a great deal with your\x01",
            "Section One training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah. She's strict, but\x01",
            "taught me carefully and\x01",
            "thoroughly.\x02\x03",
            "#00004FHow to put it... I think\x01",
            "she's way too serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHaha, I get that feeling\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, girls like that\x01",
            "are only seeking\x01",
            "comfort.\x02\x03",
            "#10302FHaha, maybe I should\x01",
            "invite her for some\x01",
            "drinks tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FNow look here...\x02\x03",
            "#00000FAnyway, let's look for\x01",
            "this Lechter.\x02\x03",
            "Let's start looking on\x01",
            "Back Street.\x02",
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
            "Quest [Imperial\x01",
            "Secretary Identity\x01",
            "Check]\x07\x00",
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

    # Function_47_14BDC end

    def Function_48_15D6B(): pass

    label("Function_48_15D6B")

    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(400)
    Sound(104, 0, 100, 0)
    Return()

    # Function_48_15D6B end

    def Function_49_15D7E(): pass

    label("Function_49_15D7E")

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
            "─Nice work. Looks like\x01",
            "you found some answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThough I couldn't believe he\x01",
            "told us he's from the\x01",
            "intelligence division so easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "According to what we know, we're\x01",
            "confident he's not restricted to\x01",
            "intelligence activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But with this, we now\x01",
            "have a rough idea of how\x01",
            "long he's staying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The result was better\x01",
            "than I expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHaha, I'm happy to hear\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHaha. So a certain someone\x01",
            "putting out their body\x01",
            "bore fruit after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00113FI didn't put anything\x01",
            "out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Anyway, I'm also worried\x01",
            "about that girl who was\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Did it seem like she was\x01",
            "Captain Lechter's\x01",
            "subordinate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FNo, I don't think so.\x02\x03",
            "#00008FShe's too young to be an\x01",
            "intelligence officer and\x01",
            "too innocent.\x02\x03",
            "#00001FAlthough she didn't seem\x01",
            "like a normal civilian\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right. Her\x01",
            "movements were\x01",
            "incredibly quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "─Understood. Section One\x01",
            "will keep tabs on that\x01",
            "girl as well, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then, I'll excuse\x01",
            "myself. Good work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo problem. Please feel\x01",
            "free to contact us if\x01",
            "you ever need our help.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_162AE():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_162AE)

    def lambda_162BB():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_162BB)

    def lambda_162C8():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_162C8)

    def lambda_162D5():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_162D5)
    OP_68(-57300, 1500, 16880, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_16327():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16327)

    def lambda_16334():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16334)

    def lambda_16341():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16341)

    def lambda_1634E():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1634E)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00006FPhew... We somehow\x01",
            "managed to live up to\x01",
            "her expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F...*sigh*, you're\x01",
            "right...\x02\x03",
            "#00108FBut that girl... Whoever\x01",
            "could she be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FThat's right... She was deceiving\x01",
            "us with her attitude, but I don't\x01",
            "think she's a normal traveller.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAn intelligence officer of a\x01",
            "major power, and an innocent\x01",
            "and wild girl, huh...\x02\x03",
            "#10304FHehe. This is getting pretty\x01",
            "interesting.\x02",
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
            "Quest [Imperial Sec'y\x01",
            "Background Check]\x07\x00\x01",
            "completed!\x02",
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

    # Function_49_15D7E end

    def Function_50_1658D(): pass

    label("Function_50_1658D")

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

    def lambda_16620():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16620)
    Sleep(50)

    def lambda_1663D():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1663D)
    Sleep(50)

    def lambda_1665A():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1665A)
    Sleep(50)

    def lambda_16677():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16677)
    Sleep(300)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "Oh... It looks like you\x01",
            "guys are done.\x02",
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

    def lambda_16737():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16737)
    Sleep(50)

    def lambda_16754():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16754)
    Sleep(50)

    def lambda_16771():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16771)
    Sleep(50)

    def lambda_1678E():
        OP_97(0xFE, 0x3E8, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1678E)
    WaitChrThread(0x101, 1)

    def lambda_167AC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_167AC)
    WaitChrThread(0x109, 1)

    def lambda_167BD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_167BD)
    WaitChrThread(0x102, 1)

    def lambda_167CE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_167CE)
    WaitChrThread(0x105, 1)

    def lambda_167DF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_167DF)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah. We reported in\x01",
            "just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. That's one case\x01",
            "closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha. Nice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that you've restarted the Support Section, I\x01",
            "think a lot of requests will be coming your way\x01",
            "from here on out, so please do your best on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FThanks, Rebecca.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAs a new member I'm\x01",
            "still inexperienced, but\x01",
            "I'll do my very best.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "By the way, everyone.\x01",
            "Have you been using your\x01",
            "new Combat Notebook?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lloyd, you should have\x01",
            "received it when you\x01",
            "trained with Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAh, now that you mention\x01",
            "it... I am using it.\x02\x03",
            "#00004FWhen we record more info in\x01",
            "the notebook, we should\x01",
            "report to you. Is that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, that would really\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Reports of new monster\x01",
            "types have been\x01",
            "increasing lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We want to gather a little more info on\x01",
            "them both for understanding the situation\x01",
            "and for implementing security measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I have until now, I'll give you\x01",
            "small rewards as you fill in the\x01",
            "notebook. I'm counting on all of you.\x02",
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
            "#12P#10100FSo it might make sense\x01",
            "to periodically stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha. I'll be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And... there's one more\x01",
            "thing I need to tell\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's about the terminal\x01",
            "data you found during\x01",
            "the cult incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yesterday, it finally\x01",
            "became possible to\x01",
            "analyze it.\x02",
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

    def lambda_16D89():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16D89)
    Sleep(50)

    def lambda_16D99():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16D99)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#6P#10305FHm? What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16DD8():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16DD8)
    Sleep(50)

    def lambda_16DE8():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16DE8)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003F...During the cult incident, we\x01",
            "obtained certain data from terminals\x01",
            "in the Fort of Sun.\x02\x03",
            "It's data about the D∴G Cult that\x01",
            "appears to have been recorded by\x01",
            "Joachim Gunther himself.\x02\x03",
            "#00008FSome of the data was intentionally\x01",
            "deleted, making it impossible to\x01",
            "decipher. So we sent it to forensics.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00001FCould it be that you've\x01",
            "recovered the deleted\x01",
            "parts?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16F80():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16F80)
    Sleep(50)

    def lambda_16F90():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16F90)
    Sleep(50)

    def lambda_16FA0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16FA0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "No, but according to\x01",
            "forensics, there's still\x01",
            "hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm told fragments of the\x01",
            "damaged data remain within\x01",
            "the memory quartz, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To analyze them completely,\x01",
            "it will take a considerable\x01",
            "amount of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FI see...\x02\x03",
            "#10108FI thought we'd finally be able\x01",
            "to understand the unclear\x01",
            "parts of that incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...For now, it seems we\x01",
            "can only wait patiently.\x02\x03",
            "#00000FRebecca, thanks for\x01",
            "filling us in on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha. You're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For now, if you just ask me,\x01",
            "you can check the terminal\x01",
            "data whenever you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll let you know\x01",
            "whenever there's been any\x01",
            "progress on the analysis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FRight. Thanks for your\x01",
            "help.\x02",
        )
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

    # Function_50_1658D end

    def Function_51_17287(): pass

    label("Function_51_17287")

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
            "Alright then, I need to\x01",
            "ask you a few questions\x01",
            "for the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Umm, what are your\x01",
            "names?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "John Doe. ("fiddle\x01",
            "fiddle")\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "John Smith. ("scratch\x01",
            "scratch")\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hmph, do we have any\x01",
            "obligation to answer?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "Y-You!! Stop screwing\x01",
            "around already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Now now, Frantz. Calm\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Hmph, a warning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Lame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Man. This is why you're\x01",
            "commoners.\x02",
        )
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
            "#10101FWe're punishing them\x01",
            "with only a fine!?\x02",
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
            "It's true that bare minimum\x01",
            "traffic regulations are\x01",
            "enshrined in state law, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Since they're Calvardian,\x01",
            "we can't punish them too\x01",
            "severely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Although they'll receive a\x01",
            "stern warning today, they'll\x01",
            "be released immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I thought that might\x01",
            "be the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHmm. It looks like you\x01",
            "were expecting this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17799():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17799)
    Sleep(50)

    def lambda_177A9():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_177A9)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00108FSomething similar happened before.\x02\x03",
            "In the fake brand trader incident, the\x01",
            "criminal received only a warning,\x01",
            "deportation and a one-month entry ban.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FNow that you mention\x01",
            "it... that did happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...Now that "uncle" has become mayor,\x01",
            "revisions to state law have accelerated,\x01",
            "but...\x02\x03",
            "As things are, many parts of it haven't\x01",
            "been touched.\x02\x03",
            "#00101FThe fact that foreigners can't be severely\x01",
            "punished is said to be a "strain" Crossbell\x01",
            "has struggled with for many years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man...\x02\x03",
            "Then, was this whole\x01",
            "case a waste of time?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F...No, it wasn't.\x02\x03",
            "#00000FEven though this has happened\x01",
            "many times before, none of the\x01",
            "cases were a wasted effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I don't think this case\x01",
            "was a waste either.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17AA8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17AA8)
    Sleep(50)

    def lambda_17AB8():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17AB8)
    Sleep(100)

    ChrTalk(
        0xE,
        (
            "They won't engage in any more\x01",
            "reckless driving for the rest\x01",
            "of the day, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...I think we'll confront\x01",
            "many barriers like this\x01",
            "one going forward.\x02\x03",
            "#00000FAll the more reason to\x01",
            "face them head-on,\x01",
            "without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYou're right... I have\x01",
            "to do my best as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThen, I guess I'll have\x01",
            "to conduct myself in as\x01",
            "cool a way as possible.\x02\x03",
            "#10302FOtherwise, you guys\x01",
            "might get too passionate\x01",
            "and go crazy, yeah?\x02",
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
            "#00106FWazy... He put it so\x01",
            "nicely, and you had to\x01",
            "throw cold water on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, whatever.\x02\x03",
            "#00000FThen, Officer Kate...\x01",
            "Can we leave the rest to\x01",
            "you?\x02",
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
            "You were a big help today.\x01",
            "I look forward to working\x01",
            "with you in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FThanks. We feel the\x01",
            "same.\x02",
        )
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
            "Quest [Stopping a\x01",
            "Reckless Driver]\x07\x00\x01",
            "completed!\x02",
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

    # Function_51_17287 end

    def Function_52_17ED9(): pass

    label("Function_52_17ED9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189D3")
    OP_0D()

    ChrTalk(
        0x10,
        (
            "*sigh*, Margaret...\x01",
            "Why!?!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "It's not like you fall\x01",
            "for a man like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "A-Anyway, I have to do\x01",
            "something before I lose\x01",
            "her for good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Vice Chief Pierre...\x01",
            "You don't see him here\x01",
            "too often.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(Looks like he's worried\x01",
            "about something...)\x02",
        )
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
            "Y-You... How long have\x01",
            "you been standing\x01",
            "there!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "N-No way. You heard me\x01",
            "talking to myself just\x01",
            "now, didn't you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FW-Well... We didn't hear\x01",
            "the details, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F"Margaret" and "fall for\x01",
            "a man" were the parts we\x01",
            "heard, though.\x02",
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
            "#10302FHehe, is that the name\x01",
            "of your favorite\x01",
            "hostess, Vice Chief?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "D-Don't say such\x01",
            "scandalous things!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Margaret is... It's the\x01",
            "name of my lady!!\x02",
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
            "...Well, ever since I lost my wedding ring\x01",
            "and got passed over for Chief of Police,\x01",
            "she's gotten harder to deal with...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "...Wait, did I have to\x01",
            "put those things so\x01",
            "bluntly!?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18573")
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
            "#1K◆The "Searching for the\x01",
            "Ring" Quest in ZnK?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",        # 0
            "[Cleared]\x01",          # 1
            "[Not Cleared]\x01",      # 2
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
        (0, "loc_1855A"),
        (1, "loc_1855F"),
        (2, "loc_18569"),
        (SWITCH_DEFAULT, "loc_18573"),
    )


    label("loc_1855A")

    Jump("loc_18573")

    label("loc_1855F")

    OP_29(0x15, 0x4, 0x10)
    Jump("loc_18573")

    label("loc_18569")

    OP_29(0x15, 0x3, 0x10)
    Jump("loc_18573")

    label("loc_18573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18628")

    ChrTalk(
        0x101,
        (
            "#00003F(Come to think of it, the\x01",
            "Vice Chief is famous for\x01",
            "being a henpecked husband.)\x02\x03",
            "#00008F(The reason the Vice Chief\x01",
            "is worried could be related\x01",
            "to that.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_186B5")

    label("loc_18628")


    ChrTalk(
        0x101,
        (
            "#00003F(The Vice Chief... He\x01",
            "seems to be a henpecked\x01",
            "husband.)\x02\x03",
            "#00008F(The reason the Vice\x01",
            "Chief is worried could\x01",
            "be related to that.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186B5")


    ChrTalk(
        0x10,
        (
            "...Hmph, it can't be helped.\x01",
            "Desperate times call for\x01",
            "desperate measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Ladies and gentlemen of the Special\x01",
            "Support Section! I'm giving you an\x01",
            "absolute secret mission!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FSecret mission, you say?\x01",
            "What ever could you\x01",
            "mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "U-Uhhm, to be frank... I\x01",
            "want to ask you to\x01",
            "investigate my wife.\x02",
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
        "#00305FI-Investigate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FUsing one's position in private\x01",
            "matters is against the police\x01",
            "code of conduct, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Who cares about the\x01",
            "details! I'm at the end\x01",
            "of my rope here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't care if you deal with\x01",
            "it as one of your "requests"\x01",
            "or whatever! How about that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FH-Hmm... (What should we\x01",
            "do?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A99")

    label("loc_189D3")

    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "Ladies and gentlemen of the\x01",
            "SSS! I want to give you an\x01",
            "absolute secret mission!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I don't care if you deal with it as\x01",
            "one of your "requests" or whatever!\x01",
            "Well, can you take it on!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A99")

    Call(0, 53)
    OP_4C(0x10, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12540, 0, 14410, 0)
    EventEnd(0x5)
    Return()

    # Function_52_17ED9 end

    def Function_53_18AB8(): pass

    label("Function_53_18AB8")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B0E")
    Call(0, 54)
    Jump("loc_18C07")

    label("loc_18B0E")


    ChrTalk(
        0x101,
        (
            "#00006FI'm sorry... We have\x01",
            "work to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I-I see... It can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Then, take care of it at\x01",
            "once and return here!!\x01",
            "...All right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FW-We'll see what we can\x01",
            "do.\x02",
        )
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

    label("loc_18C07")

    Return()

    # Function_53_18AB8 end

    def Function_54_18C08(): pass

    label("Function_54_18C08")


    ChrTalk(
        0x101,
        (
            "#00001FI-I understand. You seem\x01",
            "troubled... Can we hear\x01",
            "the whole story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Oh, really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Good. That being the\x01",
            "case, talking here won't\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Follow me to my office.\x01",
            "We'll discuss details\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_54_18C08 end

    def Function_55_18CF1(): pass

    label("Function_55_18CF1")

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
            "#00306FMan. In the end, we\x01",
            "ended up accepting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWell, the Vice Chief is\x01",
            "worried about his\x01",
            "wife...\x02\x03",
            "It might be a good idea\x01",
            "to stick with this until\x01",
            "we learn the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F*sigh*, it can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThen, where do we check\x01",
            "first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLet's first try going to the\x01",
            "Central Square restaurant.\x02\x03",
            "Our alleged host and the vice\x01",
            "chief's wife often meet up there.\x01",
            "Maybe we can ask them directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, I guess that's all\x01",
            "right.\x02\x03",
            "#10309FThen, shall we go\x01",
            "immediately?㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Looks like he's\x01",
            "enjoying this...)\x02",
        )
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
            "Quest [The Vice Chief's\x01",
            "Request]\x07\x00",
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

    # Function_55_18CF1 end

    def Function_56_19084(): pass

    label("Function_56_19084")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_190E7")

    ChrTalk(
        0x101,
        (
            "#00000F...We don't have any\x01",
            "business on the floors\x01",
            "above. Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191CD")

    label("loc_190E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1917D")
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
            "Everyone, please wait\x01",
            "for orders in the\x01",
            "meeting room on 1F.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xB4, 0x0)
    OP_4C(0x16, 0xFF)
    Jump("loc_191CD")

    label("loc_1917D")


    ChrTalk(
        0x101,
        (
            "#00000F...We don't have any\x01",
            "business on the floors\x01",
            "above. Let's not enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191CD")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_56_19084 end

    def Function_57_191E1(): pass

    label("Function_57_191E1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_57_191E1 end

    SaveToFile()

Try(main)
