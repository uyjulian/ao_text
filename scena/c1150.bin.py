from ScenarioHelper import *

def main():
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
        "Receptionist Rebecca",         # 1
        "Receptionist franc",           # 2
        "Donovan",           # 3
        "Raymond investigator",       # 4
        "Dudley investigator",         # 5
        "Emma investigator",             # 6
        "Kate policing",             # 7
        "Police investigation",           # 8
        "Pierre deputy director",         # 9
        "Yuri",                 # 10
        "Sykes",               # 11
        "Reggie",                 # 12
        "Mr. Joe Ridge",       # 13
        "Defense Forces soldier",             # 14
        "Defense Forces soldier",             # 15
        "Policeman",                   # 16
        "Policeman",                   # 17
        "Sergey Manager",           # 18
        "chair",                   # 19
        "chair",                   # 20
        "chair",                   # 21
        "chair",                   # 22
        "chair",                   # 23
        "chair",                   # 24
        "chair",                   # 25
        "chair",                   # 26
        "SE control",                 # 27
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
        "Function_7_14C4",         # 07, 7
        "Function_8_29FA",         # 08, 8
        "Function_9_2A09",         # 09, 9
        "Function_10_49EF",        # 0A, 10
        "Function_11_4AF6",        # 0B, 11
        "Function_12_5659",        # 0C, 12
        "Function_13_632C",        # 0D, 13
        "Function_14_6CA0",        # 0E, 14
        "Function_15_6D88",        # 0F, 15
        "Function_16_6E7D",        # 10, 16
        "Function_17_7B89",        # 11, 17
        "Function_18_7CED",        # 12, 18
        "Function_19_9C2A",        # 13, 19
        "Function_20_A4AB",        # 14, 20
        "Function_21_ABB8",        # 15, 21
        "Function_22_B30F",        # 16, 22
        "Function_23_BE00",        # 17, 23
        "Function_24_BE26",        # 18, 24
        "Function_25_C639",        # 19, 25
        "Function_26_CC3F",        # 1A, 26
        "Function_27_CF1C",        # 1B, 27
        "Function_28_D3A3",        # 1C, 28
        "Function_29_DD0A",        # 1D, 29
        "Function_30_E2F9",        # 1E, 30
        "Function_31_F476",        # 1F, 31
        "Function_32_F73B",        # 20, 32
        "Function_33_F83B",        # 21, 33
        "Function_34_F943",        # 22, 34
        "Function_35_FA5F",        # 23, 35
        "Function_36_FB77",        # 24, 36
        "Function_37_FEE9",        # 25, 37
        "Function_38_1019C",       # 26, 38
        "Function_39_103E9",       # 27, 39
        "Function_40_10A0C",       # 28, 40
        "Function_41_10AE1",       # 29, 41
        "Function_42_10C4D",       # 2A, 42
        "Function_43_10DC6",       # 2B, 43
        "Function_44_10EC4",       # 2C, 44
        "Function_45_1132D",       # 2D, 45
        "Function_46_127E0",       # 2E, 46
        "Function_47_12D62",       # 2F, 47
        "Function_48_13DFA",       # 30, 48
        "Function_49_13E0D",       # 31, 49
        "Function_50_14568",       # 32, 50
        "Function_51_151EE",       # 33, 51
        "Function_52_15DCB",       # 34, 52
        "Function_53_168D8",       # 35, 53
        "Function_54_16A26",       # 36, 54
        "Function_55_16B23",       # 37, 55
        "Function_56_16EA1",       # 38, 56
        "Function_57_16FE6",       # 39, 57
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_12FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FE")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, everyone\x01",
            "That which you have is … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps, \"fragment\"\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEr, is this about that?\x02\x03",
            "#00000FAlthough I got it,\x01",
            "It is not used any more\x01",
            "I did not understand ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is in Rebecca\x01",
            "I showed fragments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "Well, after all … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is because the person in the district judgment section was looking for\x01",
            "Damaged memory crystals#8RMemory Quartz#For repairing\x01",
            "It is a piece of crystal that can be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With that,\x01",
            "Part of the organization's terminal data\x01",
            "It should be able to analyze.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1196")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_1196")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BF")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E8")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_11E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_120E")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_120E")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FWell then, then …\x01",
            "By Joachim Günter\x01",
            "To be able to read hidden sentences …! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, in part\x01",
            "I heard there is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think that results will come out soon,\x01",
            "Even when \"fragment\" is used for discrimination\x01",
            "Is it OK?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 9)
    TalkEnd(0x8)
    Return()

    label("loc_12FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1321")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_1321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_1336")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x1, 3)
    Call(0, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_13C8")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                        # 0
            "Show battle notebook\x01",                # 1
            "Confirm terminal data of the cult\x01",      # 2
            "Passing fragments\x01",              # 3
            "quit\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_1429")

    label("loc_13C8")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",                        # 0
            "Show battle notebook\x01",                # 1
            "Confirm terminal data of the cult\x01",      # 2
            "quit\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1429")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1457")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)
    Jump("loc_14AE")

    label("loc_1457")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 6)
    Call(0, 16)
    Jump("loc_14AE")

    label("loc_147B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149C")
    Call(0, 10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AE")

    label("loc_149C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    Call(0, 9)

    label("loc_14AE")

    Jump("loc_1340")

    label("loc_14B3")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    Return()

    # Function_6_F51 end

    def Function_7_14C4(): pass

    label("Function_7_14C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1873")

    ChrTalk(
        0x8,
        "Everyone … … Good job everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Rebecca, thanks for your hard work.\x01",
            "You returned to the headquarters, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, Kate and others\x01",
            "Raymonds also\x01",
            "I returned to normal work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From the command line of the Defense Forces\x01",
            "I am going to be out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Currently it is original, in each arrangement\x01",
            "Towards the recovery of the situation\x01",
            "We are dealing with each direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FHmm, that was good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, thanks to everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… … That's right, to the franc\x01",
            "Could you tell it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Leave the reception of the police,\x01",
            "To concentrate on everyone's help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1720")

    ChrTalk(
        0x109,
        (
            "#10102FHuhu, I understand.\x01",
            "I will tell it properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175A")

    label("loc_1720")


    ChrTalk(
        0x103,
        (
            "#00202FHuhu, I understand.\x01",
            "I will tell it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A5")

    ChrTalk(
        0x10A,
        (
            "#00600FRebecca, if you are headquarters\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E3")

    label("loc_17A5")


    ChrTalk(
        0x101,
        (
            "#00000FRebecca, too, the headquarters\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E3")


    ChrTalk(
        0x8,
        (
            "Yes, for the citizens as well\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The situation that still remains intact continues … …\x01",
            "Please do your best also there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CC, 3)
    Jump("loc_19D2")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194A")

    ChrTalk(
        0x8,
        (
            "警察本部も、Towards the recovery of the situation\x01",
            "I correspond to each direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To franc, to help everyone\x01",
            "Please tell him / her to concentrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The situation that still remains intact continues … …\x01",
            "Please do your best also there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_19D2")

    label("loc_194A")


    ChrTalk(
        0x8,
        (
            "警察本部も、Towards the recovery of the situation\x01",
            "It is in the midst of full efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The situation that still remains intact continues … …\x01",
            "Please do your best also there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D2")

    Jump("loc_29F9")

    label("loc_19D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E5")
    Jump("loc_29F9")

    label("loc_19E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADB")

    ChrTalk(
        0x8,
        (
            "Suddenly towards the headquarters this morning\x01",
            "Several people came by the defense army\x01",
            "I was ordered to wait as it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Too suddenly,\x01",
            "How to figure out what to do\x01",
            "Confused ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, now that the meeting ends\x01",
            "There is no choice but to wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1B5A")

    label("loc_1ADB")


    ChrTalk(
        0x8,
        (
            "Too suddenly,\x01",
            "How to figure out what to do\x01",
            "Confused ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, now that the meeting ends\x01",
            "There is no choice but to wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5A")

    Jump("loc_29F9")

    label("loc_1B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B6D")
    Jump("loc_29F9")

    label("loc_1B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C28")

    ChrTalk(
        0x8,
        (
            "Mr. Dudley is also very much today\x01",
            "I had a steep expression … …\x01",
            "It seems that the situation is not good at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At any rate, a solution other than battle\x01",
            "I would like you to have a headline ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D19")

    ChrTalk(
        0x8,
        (
            "Thanks to the guards,\x01",
            "Transcontinental railway operates from this morning\x01",
            "I was able to completely resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because somehow it was in time for the first train,\x01",
            "Especially without changing the operation schedule\x01",
            "I have finished ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed,\x01",
            "It is a place like the obsession of the guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DD9")

    ChrTalk(
        0x8,
        (
            "In response to a train accident,\x01",
            "Various from various directions\x01",
            "We have received your inquiries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "transfer#4RLooking back#Transportation correspondence is also\x01",
            "It has already begun … …\x01",
            "If this situation continues, it is troublesome for fluffy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(
        0x8,
        (
            "\"Pleomorphic grass\" …\x01",
            "It was also in the cult's database\x01",
            "Gnostic stuff, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Such a suddenly crossbell\x01",
            "I can not find it all over the place ……\x01",
            "What on earth is going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F69")

    ChrTalk(
        0x8,
        (
            "In your next mission,\x01",
            "I heard that you will be fighting with the Association of Assault Horsemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehuu, you should just line up with the guild\x01",
            "It will not be long before the day will come …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To everyone, really\x01",
            "It always amazes me in a good sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_1FBF")

    label("loc_1F69")


    ChrTalk(
        0x8,
        (
            "As Franc says,\x01",
            "I think that the opponent of a phantom beast is hard … …\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBF")

    Jump("loc_29F9")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2097")

    ChrTalk(
        0x8,
        (
            "In the security measures headquarters on the second floor\x01",
            "既にSergey Managerが待機しています。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also the start time of the plenary session\x01",
            "I finally approached it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all,\x01",
            "It is safe to enter the hall\x01",
            "It is the first gateway.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2110")

    label("loc_2097")


    ChrTalk(
        0x8,
        (
            "Also the start time of the plenary session\x01",
            "I finally approached it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all,\x01",
            "It is safe to enter the hall\x01",
            "It is the first gateway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2110")

    Jump("loc_29F9")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21CC")

    ChrTalk(
        0x8,
        (
            "Both me and Fran\x01",
            "I went to see the Orkis Tower … …\x01",
            "That power was overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed, the new Crossbell\x01",
            "It is a building suitable for landmarks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_21CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_256F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B4")

    ChrTalk(
        0x8,
        (
            "This security system,\x01",
            "Police and security guards never used\x01",
            "It is built under cooperation system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In traditional organizations,\x01",
            "To build up the structure so far\x01",
            "I think it was impossible … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The biggest factor is\x01",
            "I have a great understanding of the police\x01",
            "It can be said that there is Sonja command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, I guess\x01",
            "Rebecca is beautiful. )\x02\x03",
            "#00309F(Even with the same glasses, it passed the prime\x01",
            "It is very different from Sonja command. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Huh, Randy senior … ….\x01",
            "You can tell the commander? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#00305F(No, no now\x01",
            "A word of words … …)\x02\x03",
            "#00309F(No, Rebecca is also a beautiful person\x01",
            "Do not be enemy of Sonya command. )\x02",
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
    Jump("loc_256A")

    label("loc_24B4")


    ChrTalk(
        0x8,
        (
            "This security system,\x01",
            "Police and security guards never used\x01",
            "It is built under cooperation system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The biggest factor is\x01",
            "I have a great understanding of the police\x01",
            "It can be said that there is Sonja command.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256A")

    Jump("loc_29F9")

    label("loc_256F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_274E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26BC")

    ChrTalk(
        0x8,
        (
            "When the former director was dismissed,\x01",
            "Since the inauguration of Mayor Dieter,\x01",
            "The police system has also changed a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are many new difficulties, too,\x01",
            "I still realize that I am moving forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, expectations for everyone\x01",
            "I think that it will become bigger and bigger\x01",
            "Please do your best, by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also do our best\x01",
            "Because I will support it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2749")

    label("loc_26BC")


    ChrTalk(
        0x8,
        (
            "From now on, expectations for everyone\x01",
            "I think that it will become bigger and bigger\x01",
            "Please do your best, by all means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also do our best\x01",
            "Because I will support it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2749")

    Jump("loc_29F9")

    label("loc_274E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 7)), scpexpr(EXPR_END)), "loc_2965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B8")

    ChrTalk(
        0x8,
        (
            "Also report on the new demon\x01",
            "There is a tendency to increase … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For understanding the actual condition of them and for safety measures\x01",
            "I want as much information as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As before, step by step\x01",
            "Because some allowance will be paid,\x01",
            "どうかThank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, the data of the cult's terminal\x01",
            "You can check it here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When confirming\x01",
            "Please tell me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2960")

    label("loc_28B8")


    ChrTalk(
        0x8,
        (
            "Regarding report of battle notebook\x01",
            "Because some allowance will be paid,\x01",
            "どうかThank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, data of the terminal of the cult\x01",
            "When confirming\x01",
            "Please tell me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2960")

    Jump("loc_29F9")

    label("loc_2965")


    ChrTalk(
        0x8,
        (
            "Huhu, even so\x01",
            "I would like to request cooperation from section 1\x01",
            "You guys also got a lot of success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Activities of the Special Affairs Support Division\x01",
            "As one of those I have seen\x01",
            "Something is deep emotional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F9")

    Return()

    # Function_7_14C4 end

    def Function_8_29FA(): pass

    label("Function_8_29FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_2A08")
    SetScenarioFlags(0x1, 3)

    label("loc_2A08")

    Return()

    # Function_8_29FA end

    def Function_9_2A09(): pass

    label("Function_9_2A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_2AA7")

    ChrTalk(
        0x8,
        (
            "Oh, \"Fragment\"\x01",
            "You brought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To analyze the terminal data of the cult,\x01",
            "Even when \"fragment\" is used for discrimination\x01",
            "Is it OK?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA7")


    ChrTalk(
        0x101,
        "#00000Fええ、Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well then, please wait a moment.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_2B00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D1")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_END)), "loc_48CC")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber('结晶碎片', 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B88")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "01 th information terminal data\x01",
            "I analyzed page 1 of \"About the cult\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2B88")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE4")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "01 th information terminal data\x01",
            "I analyzed page 3 of \"About the cult\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2BE4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C46")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 1 of \"About Gnostic\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2C46")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA8")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 2 of \"About Gnostic\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2CA8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_356C")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "01 th information terminal data\x01",
            "I analyzed page 4 of \"About the cult\"!\x07\x00\x02",
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
            "01 th information terminal data\x01",
            "Completed analysis of \"About the cult\"!\x07\x00\x02",
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
            "#5PAll data of the 01 th information terminal\x01",
            "The analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWould you like to check it now?\x02",
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
            "#5P…… In this data,\x01",
            "An outline on the cult\x01",
            "It seems to have been described.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDoctrine of denial of the goddess … ….\x01",
            "I really can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes …\x01",
            "Joachim Günter's\x01",
            "I also agree with the testimony.\x02\x03",
            "#00001FAnd this word \"D\" …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30A3")

    ChrTalk(
        0x103,
        (
            "#12P#00203FThey believed on behalf of the goddess\x01",
            "It is a word pointing to \"true God\".\x02\x03",
            "#00201FD∴ G \"G\" in the name of the organization\x01",
            "\"True wisdom#10RGnosis#\"To point to\x01",
            "It is already located … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_304E")

    ChrTalk(
        0x105,
        (
            "#12P#10403FHmm, this also means \"D∴ G\"\x01",
            "I heard that it is finally found out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309E")

    label("loc_304E")


    ChrTalk(
        0x105,
        (
            "#12P#10303FHmm, this also means \"D∴ G\"\x01",
            "I heard that it is finally found out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309E")

    Jump("loc_31AC")

    label("loc_30A3")


    ChrTalk(
        0x103,
        (
            "#12P#00200FThey believed on behalf of the goddess\x01",
            "It is a word pointing to \"true God\".\x02\x03",
            "#00201FD∴ G \"G\" in the name of the organization\x01",
            "\"True wisdom#10RGnosis#\"To point to\x01",
            "It is already located … …\x02\x03",
            "This also means \"D∴ G\"\x01",
            "It can be said that it finally turned out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AC")


    ChrTalk(
        0x102,
        (
            "#12P#00108FBut … … Dr. Joachim,\x01",
            "Ka'a thing\x01",
            "You were saying \"the Godhead\", are not you?\x02\x03",
            "Then, \"D\" is\x01",
            "As for words pointing to Ka'aa\x01",
            "It will become … ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D4")

    ChrTalk(
        0x109,
        (
            "#12P#10101FJoachim Günter\x01",
            "How far did you know … ….\x02\x03",
            "…… I do not know yet by just this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33BA")

    label("loc_32D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_335C")

    ChrTalk(
        0x104,
        (
            "#12P#00301FJoachim's bastard\x01",
            "How far did you know … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F…… I do not know yet by just this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33BA")

    label("loc_335C")


    ChrTalk(
        0x104,
        (
            "#12P#00301FJoachim's bastard\x01",
            "How far did you know … ….\x02\x03",
            "I can not tell by just this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BA")


    ChrTalk(
        0x101,
        (
            "#12P#00001FErnest also from Joachim\x01",
            "I was listening to everything\x01",
            "It seems not to be ……\x02\x03",
            "#00003FIf he could be arrested … …\x01",
            "Do not keep thinking so.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34C6")

    ChrTalk(
        0x8,
        (
            "#5P…… Anyway, in this condition\x01",
            "If you analyze data,\x01",
            "I think that various things will be visible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356C")

    label("loc_34C6")


    ChrTalk(
        0x8,
        (
            "#5P…… Anyway, in this condition\x01",
            "If you analyze data,\x01",
            "I think that various things will be visible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe remaining \"fragment\" is also\x01",
            "Let's try it for analysis.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_356C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35CE")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 3 of \"About Gnostic\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_35CE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362A")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "03 th information terminal data\x01",
            "I analyzed page 1 of \"About Miko\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_362A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F50")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "02 th information terminal data\x01",
            "I analyzed page 4 of \"About Gnostic\"!\x07\x00\x02",
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
            "02 th information terminal data\x01",
            "Completed analysis of \"About Gnostic\"!\x07\x00\x02",
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
            "#5PAll data of the 02 th information terminal\x01",
            "The analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWould you like to check it now?\x02",
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
            "#5P…… In this data,\x01",
            "About that \"Gnostic\"\x01",
            "It seems that details are written.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PImprove physical ability and sensitivity,\x01",
            "Even potential potential\x01",
            "Drug with efficacy to withdraw … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt is called phenomenon such as \"demonization\"\x01",
            "It is quite a mystery drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FIt was used as raw material\x01",
            "Plants called \"Pleroma grass\"\x01",
            "Because it was clustered in a wetland … …\x02\x03",
            "Joachim puts the material in wetland belt\x01",
            "Things that seem to have gone to collect\x01",
            "It seems that there is no mistake in the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A20")

    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, Gnostic is included in the data\x01",
            "A true God that they say … …\x02\x03",
            "That is, to restore \"D\"\x01",
            "There is a passage that is drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FTo be honest, to a stupid story\x01",
            "I can hear it ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADB")

    label("loc_3A20")


    ChrTalk(
        0x102,
        (
            "#12P#00101FAlso, Gnostic is included in the data\x01",
            "A true God that they say … …\x02\x03",
            "That is, to restore \"D\"\x01",
            "There is a passage that is drug.\x02\x03",
            "#00108FTo be honest, to a stupid story\x01",
            "I can hear it ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADB")


    ChrTalk(
        0x103,
        (
            "#12P#00201FStill, the cult has for 500 years\x01",
            "In the form of \"ritual\"\x01",
            "I have been studying Gnostic … …\x02\x03",
            "#00203F…… I am lucky to Mr. Guy\x01",
            "I was rescued, but until now\x01",
            "There seems to be a considerable number of victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FI thought it was \"some sacrifice\"\x01",
            "I'm talking about you ….\x02\x03",
            "They are like guys who really help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C79")

    ChrTalk(
        0x105,
        (
            "#12P#10403F…… Also, recently Waldo\x01",
            "You were taking Gnostic, are not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC9")

    label("loc_3C79")


    ChrTalk(
        0x105,
        (
            "#12P#10303F…… Also, recently Waldo\x01",
            "You were taking Gnostic, are not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CC9")


    ChrTalk(
        0x101,
        (
            "#12P#00001FOh … … Although the cult has gone,\x01",
            "We may still need attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAE")

    label("loc_3D22")


    ChrTalk(
        0x101,
        (
            "#12P#00003F…… Also, recently Waldo\x01",
            "I was taking Gnostic.\x02\x03",
            "#00001FAlthough the cult has disappeared,\x01",
            "We may still need attention.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAE")


    ChrTalk(
        0x102,
        (
            "#12P#00101FYeah … That's really true.\x02\x03",
            "Not limited to Gnostic,\x01",
            "Such drugs, our police\x01",
            "You have to get it under control.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('结晶碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EA0")

    ChrTalk(
        0x8,
        "#5PYes, I really think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P… for the time being about Gnostic\x01",
            "Is it such a place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F50")

    label("loc_3EA0")


    ChrTalk(
        0x8,
        "#5PYes, I really think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P… for the time being about Gnostic\x01",
            "Is it such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe remaining \"fragment\" is also\x01",
            "Let's try it for analysis.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_3F50")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FAC")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "03 th information terminal data\x01",
            "I analyzed page 2 of \"About Miko\"!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3FAC")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48CC")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "03 th information terminal data\x01",
            "I analyzed page 3 of \"About Miko\"!\x07\x00\x02",
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
            "03 th information terminal data\x01",
            "I completed the analysis of \"About Miko\"!\x07\x00\x02",
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
            "#5PAll data of the 03th information terminal\x01",
            "The analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWould you like to check it now?\x02",
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
            "#5PThis content,\x01",
            "It was protected by support section\x01",
            "Kaoru's … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F５００年前、クロchair家によって\x01",
            "Keya was born … ….\x01",
            "It was given to the cult as object of religion.\x02\x03",
            "The chest#4RCradle#\"Asleep on,\x01",
            "As a \"God's Child\" \"Child\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Human beings of the cult also have truth\x01",
            "You probably did not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203Fクロchair家の真の目的のために\x01",
            "Without knowing that it was guided by shadows,\x01",
            "I continued seeking the illusion of \"true God\" …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_431C")

    ChrTalk(
        0x106,
        "#12P#10708F…… In a sense, they are pathetic people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4393")

    label("loc_431C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4364")

    ChrTalk(
        0x109,
        "#12P#10108F…… In a sense, they are pathetic people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4393")

    label("loc_4364")


    ChrTalk(
        0x105,
        "#12P#10408F… … In a sense, pathetic people.\x02",
    )

    CloseMessageWindow()

    label("loc_4393")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43EA")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FThinking about what they came up with\x01",
            "I do not even feel sympathy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4493")

    label("loc_43EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4447")

    ChrTalk(
        0x105,
        (
            "#12P#10403FThinking about what they came up with\x01",
            "There is no room for sympathy though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4493")

    label("loc_4447")


    ChrTalk(
        0x109,
        (
            "#12P#10103FThinking about what they came up with\x01",
            "There is no room for sympathy … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4493")


    ChrTalk(
        0x101,
        (
            "#12P#00001FRegardless of cults ……\x01",
            "There must have been no sin in Ka'aa.\x02\x03",
            "#00003F例えクロchair家の目的のために\x01",
            "Even if it was a made existence ……\x02\x03",
            "Even a magical ability\x01",
            "Even if I have … …\x01",
            "Such a thing has nothing to do with it.\x02\x03",
            "That girl that awakens in front of us\x01",
            "It should be genuine, ordinary girl.\x02\x03",
            "#00001FEven so, for hundreds of years like that\x01",
            "It's been locked in alone … …\x02\x03",
            "Now also with Mr. Marybele\x01",
            "By Professor Ian\x01",
            "It is about to be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F…… Regardless of circumstances,\x01",
            "Absolutely I can not forgive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P…… For now, the cult's data\x01",
            "これで全てThe analysis is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI am about as much as you guys\x01",
            "I am not familiar with detailed circumstances … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFor everyone, Mr.\x01",
            "That it is a very important existence\x01",
            "I understand it painfully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPlease … Good luck.\x01",
            "I will support you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThank you, Rebecca.\x02\x03",
            "#00003FAbsolutely with our hands,\x01",
            "I will get back Ka'aa.\x02\x03",
            "#00001FOur precious kea … …\x01",
            "That child can spend herself with a smile\x01",
            "To make a future … ….!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_48A4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_48A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_48BD")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_48BD")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    TalkEnd(0x8)

    label("loc_48CC")

    Jump("loc_2B00")

    label("loc_48D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49EE")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PAlso, if you get \"fragments\"\x01",
            "Please bring it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PEven when checking the analyzed data\x01",
            "Please tell us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -240, 0, 11060, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49CF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_49CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49E8")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_49E8")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_49EE")

    Return()

    # Function_9_2A09 end

    def Function_10_49EF(): pass

    label("Function_10_49EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AF5")
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
            "【About the cult】\x01",            # 0
            "【About Gnostic】\x01",      # 1
            "【About Miko】\x01",            # 2
            "【quit】\x01",                  # 3
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
        (0, "loc_4AA8"),
        (1, "loc_4AB6"),
        (2, "loc_4AC4"),
        (3, "loc_4AD2"),
        (SWITCH_DEFAULT, "loc_4AE1"),
    )


    label("loc_4AA8")

    Sound(72, 0, 100, 0)
    Call(0, 11)
    Jump("loc_4AF0")

    label("loc_4AB6")

    Sound(72, 0, 100, 0)
    Call(0, 12)
    Jump("loc_4AF0")

    label("loc_4AC4")

    Sound(72, 0, 100, 0)
    Call(0, 13)
    Jump("loc_4AF0")

    label("loc_4AD2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AF0")

    label("loc_4AE1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AF0")

    label("loc_4AF0")

    Jump("loc_49F9")

    label("loc_4AF5")

    Return()

    # Function_10_49EF end

    def Function_11_4AF6(): pass

    label("Function_11_4AF6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CBD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the cult\"\x01\x01",
            "── My name is Joachim Günter.\x01",
            "It is an executive priest belonging to the \"D∴G organization\".\x01",
            "Six years ago, with the hands of many forces, including hushman\x01",
            "Our group fell into destruction.\x01",
            "However, I alone escaped the hardship,\x01",
            "I was able to surmount to this land of ■■.\x01",
            "By the guidance of the great \"■\"\x01",
            "I have been a long time to make ambitions for the cult.\x01",
            "Any time that comes - ─\x01",
            "As a document to write a new scripture\x01",
            "Data is recorded in each terminal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4E5E")

    label("loc_4CBD")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the cult\"\x01\x01",
            "── My name is Joachim Günter.\x01",
            "It is an executive priest belonging to the \"D∴G organization\".\x01",
            "Six years ago, with the hands of many forces, including hushman\x01",
            "Our group fell into destruction.\x01",
            "However, I alone escaped the hardship,\x01",
            "I could survive to the land of this origin.\x01",
            "By the guidance of the great \"D\"\x01",
            "I have been a long time to make ambitions for the cult.\x01",
            "Any time that comes - ─\x01",
            "As a document to write a new scripture\x01",
            "Data is recorded in each terminal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4E5E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SFirst, let's talk about the origins of our cult.\x01",
            "To this end, the continent of Zemria followed\x01",
            "It is necessary to look back on the abominable history.\x01\x01",
            "── About 1,200 years ago by the \"Great Collapse\"\x01",
            "The continent has lost advanced civilization and order,\x01",
            "The \"dark era\" which dominates war and poverty has come.\x01",
            "And the people who are exhausted\x01",
            "I made a big mistake.\x01\x01",
            "Suddenly misled by the foolish comments of the foolish people,\x01",
            "The autonomous order created by them\x01",
            "It has accepted it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51A5")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThat is - __- stupid\x01",
            "It is \"■ ■ ■\" which is a symbol of faith.\x01",
            "By their order the \"dark era\" will end,\x01",
            "That faith quickly spread throughout the continent … …\x01\x01",
            "Please think carefully.\x01",
            "If truly \"■ ■\" exists\x01",
            "Should everyone receive equal salvation?\x01",
            "However, the concept of disparity still remains,\x01",
            "Those who lose their lives due to disasters and misfortunes are also followed.\x01\x01",
            "Does \"■ ■\" choose people to save?\x01",
            "Is not that a foolish story?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_534C")

    label("loc_51A5")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThat is ─ ─ a foolish seven chaos church\x01",
            "It is a \"goddess of the sky\" symbolizing faith.\x01",
            "By their order the \"dark era\" will end,\x01",
            "That faith quickly spread throughout the continent … …\x01\x01",
            "Please think carefully.\x01",
            "If it is true that \"goddess\" exists\x01",
            "Should everyone receive equal salvation?\x01",
            "However, the concept of disparity still remains,\x01",
            "Those who lose their lives due to disasters and misfortunes are also followed.\x01\x01",
            "Does \"Goddess\" choose a human being to save?\x01",
            "Is not that a foolish story?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_534C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54D2")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SAfter all, because ■■■■ gains authority\x01",
            "It is nothing but a virtual image created.\x01",
            "It can not exist, such as \"■ ■\".\x01\x01",
            "Our predecessors who arrived at the truth,\x01",
            "I got on a long journey to encounter \"■ ■ ■ ■\".\x01\x01",
            "And when the times change to the Middle Ages,\x01",
            "At last they found it.\x01",
            "In the depths of this place ■ ■■■■■■■■■\x01",
            "■■■■■■■■■■■■■■■ ……\x01\x01",
            "\"■\" ── It was called so.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5645")

    label("loc_54D2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SAfter all, the seven chaos church gets authority\x01",
            "It is nothing but a virtual image created.\x01",
            "\"Goddess\" etc, such as existence can not exist.\x01\x01",
            "Our predecessors who arrived at the truth,\x01",
            "I entered a long journey to encounter \"true god\".\x01\x01",
            "And when the times change to the Middle Ages,\x01",
            "At last they found it.\x01",
            "With deep inside of this place, with a long sleep\x01",
            "Presence of great power in his body ……\x01\x01",
            "\"D\" ── It was called so.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5645")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_4AF6 end

    def Function_12_5659(): pass

    label("Function_12_5659")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_580E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About Gnostic\"\x01\x01",
            "\"Gnostic\" … … that,\x01",
            "■■■■■■■■ ■■■■■,\x01",
            "It is a secret medicine made from \"praroma grass\" as a raw material.\x01\x01",
            "The preparation method is: ■■■■■■■■■,\x01",
            "By enhancing physical ability and responsiveness by taking it,\x01",
            "Furthermore it has an efficacy to bring out even potential potential.\x01",
            "■■■■■■■■■■■■■■■■■.\x01",
            "■■■■■■■■■■■■■■■.\x01",
            "\"Gnostic\", the ■ ■ ■ ■ ■\x01",
            "It is a ■ ■ ■ ■ ■ ■ ■ medicine to ■ ■ ■ of \"■ ■\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_599D")

    label("loc_580E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About Gnostic\"\x01\x01",
            "\"Gnostic\" … … that,\x01",
            "Legendary plants that bloom on the seventy -\x01",
            "It is a secret medicine made from \"praroma grass\" as a raw material.\x01\x01",
            "The mixing method is transmitted together with \"D\"\x01",
            "By enhancing physical ability and responsiveness by taking it,\x01",
            "Furthermore it has an efficacy to bring out even potential potential.\x01",
            "But they are merely mockets.\x01",
            "The true power of this medicine was another.\x01",
            "\"Gnostic\", the spirit of the recipients\x01",
            "It is a medicine to connect to the \"D\" heart.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_599D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B3B")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"■ ■\" By ■ ■ ■ ■ ■ ■ ■\x01",
            "It has the property of storing ■ and ■ ■.\x01",
            "When either of those ■ ■ \"■ ■\" reached,\x01",
            "\"■\" means to ■ ■.\x01\x01",
            "In addition, \"Gnostic\"\x01",
            "There was room for improvement.\x01",
            "■■■■■■■■■■■■■■■■■,\x01",
            "■■■■■■■ to \"■\" ■ ■■■■■.\x01\x01",
            "Then, ■■■■■■■, our group is\x01",
            "A study on \"Gnostic\" which is more effective ……\x01",
            "We have repeated so-called \"ceremonies\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5CC6")

    label("loc_5B3B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"D\" by integrating the spirit of the recipients\x01",
            "It has the property of accumulating knowledge and growing up.\x01",
            "When that knowledge reached \"wisdom\"\x01",
            "\"D\" is resurrected.\x01\x01",
            "In addition, \"Gnostic\"\x01",
            "There was room for improvement.\x01",
            "If you can withdraw the ability of the recipient to the limit,\x01",
            "You can supply more knowledge to \"D\".\x01\x01",
            "For 500 years, my group\x01",
            "A study on \"Gnostic\" which is more effective ……\x01",
            "We have repeated so-called \"ceremonies\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5CC6")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E58")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, with ■■■ of ■■■■■\x01",
            "■■■■■■■■■■■■\x01",
            "\"Gnostic\" approached completion,\x01",
            "Miscalculation will occur at the first step.\x01\x01",
            "By increasing the scale of the experiment\x01",
            "Having been felt in existence by hooked guys and other forces,\x01",
            "To the extinction of each lodge, and the cult itself\x01",
            "It was connected.\x01\x01",
            "It is inevitable to say that it is a foolish thing.\x01",
            "For ■■ of \"■■■■\"\x01",
            "Although somewhat sacrifice is a provision … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_5FD7")

    label("loc_5E58")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SThen, when it was 500 years ago when it was launched\x01",
            "At comparable speed\x01",
            "\"Gnostic\" approached completion,\x01",
            "Miscalculation will occur at the first step.\x01\x01",
            "By increasing the scale of the experiment\x01",
            "Having been felt in existence by hooked guys and other forces,\x01",
            "To the extinction of each lodge, and the cult itself\x01",
            "It was connected.\x01\x01",
            "It is inevitable to say that it is a foolish thing.\x01",
            "For the resurrection of \"the true God\"\x01",
            "Although somewhat sacrifice is a provision … …\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5FD7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6181")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI am from a devastated lodge\x01",
            "We collected the experiment data secretly,\x01",
            "It reached the cross-bell belt of this ■.\x01\x01",
            "It is a material of \"Gnostic\"\x01",
            "\"Pleroma grass\" is a ■■■■■■■\x01",
            "Because it is ■ ■ ■ ■ ■,\x01",
            "There was nothing troubled by ■■■■■.\x01",
            "Also, the depth of this \"Fort of the Sun\"\x01",
            "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ research facilities,\x01",
            "It has many advanced facilities.\x01",
            "Thus I got a blessed research environment\x01",
            "Finally I finished this prescription ─ ─.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6318")

    label("loc_6181")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SI am from a devastated lodge\x01",
            "We collected the experiment data secretly,\x01",
            "It reached the earth crossbell of this origin.\x01\x01",
            "It is a material of \"Gnostic\"\x01",
            "\"Pleroma grass\" is the southern part of Crossbell\x01",
            "Because it is clustered in wetlands,\x01",
            "There was nothing to worry about procuring materials.\x01",
            "Also, the depth of this \"Fort of the Sun\"\x01",
            "It is a research facility built by a medieval alchemist,\x01",
            "It has many advanced facilities.\x01",
            "Thus I got a blessed research environment\x01",
            "Finally I finished this prescription ─ ─.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6318")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_12_5659 end

    def Function_13_632C(): pass

    label("Function_13_632C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64EF")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the Son\"\x01\x01",
            "This crossbell is our \"D∴G organization\"\x01",
            "In addition to being ■■■, it is set as ■■■■.\x01",
            "That's the \"child\"\x01",
            "That's why it is ■■■■■■■■■■■■■.\x01\x01",
            "\"Son\" is \"■ ■■■\" ■■■■■■■\x01",
            "■■ \"D∴G Church\" ■■■■■■■■■■.\x01",
            "\"Fort of the Sun\" ■■■■■■■■■■■■,\x01",
            "■■■■■■■■■■■■■■■■■,\x01",
            "■■■■■■■ \"Fort of the Sun\" ■■■■\x01",
            "It is ■■■■■■■■■■■■■■.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_668C")

    label("loc_64EF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"About the Son\"\x01\x01",
            "This crossbell is our \"D∴G organization\"\x01",
            "It is the home base and the place of origin.\x01",
            "The reason is that \"Child\"\x01",
            "It is a place that has been inherited from the founder.\x01\x01",
            "\"Son\" is the substitution of the \"true God\"\x01",
            "It is a symbol of our \"D∴G organization\".\x01",
            "It keeps sleeping in the basement of \"The Fort of the Sun\"\x01",
            "At first glance it is a girl of a human being,\x01",
            "In the altar of \"Fort of the Sun\" for 500 years\x01",
            "He is waiting for the awakening time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_668C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_681C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S■ ■ ■ ■ ■ ■ ■ so much,\x01",
            "It will be an incredible story for those who are alive.\x01\x01",
            "But I saw it with my own eyes.\x01",
            "In ■ of ■ ■ ■ ■ ■ ■ ■ called\x01",
            "■■■■■■■■■■■■■■ ──\x01",
            "That shit divine ■ ■.\x01\x01",
            "\"■■■■■\" means \"ancient relics\"\x01",
            "Based on the ■ ■ ■ ■ ■ ■ ■ ■ ■\x01",
            "It is ■■■■■■■■■■■■■■■.\x01",
            "Then, even this ■■■■■■■■■■\x01",
            "There is no mystery.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_69A5")

    label("loc_681C")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2SHuman beings live so much time,\x01",
            "It will be an incredible story for those who are alive.\x01\x01",
            "But I saw it with my own eyes.\x01",
            "\"Holy One Pillar#4RCradle#In a sphere called\x01",
            "A girl keeps sleeping like a slumber ----\x01",
            "Its Shinto shrine.\x01\x01",
            "\"Sacred throne\", \"ancient relics\"\x01",
            "Based on the technique of the alchemists I was studying\x01",
            "It was created by the predecessors of the cult.\x01",
            "Then, even as a phenomenon which is also called this miracle\x01",
            "There is no mystery.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_69A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B22")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"Son\" is from ■■■■■■\x01",
            "\"Gnostic\" as ■■■, ■■■■■■■\x01",
            "■■■■■■■■■■■■■.\x01\x01",
            "── \"■■\" ■■■■■ \"Son\" is ■■■,\x01",
            "It will be ■■■■ \"■\" ■ ■■.\x01",
            "And ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■\x01",
            "It is done under the \"■ ■\"\x01",
            "Release people from the spell of \"■ ■\".\x01\x01",
            "That was left by the predecessor of our \"D∴G Church\"\x01",
            "It is a prophecy, an ambition to be formed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6C8C")

    label("loc_6B22")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S\"Son\" was born and from the times\x01",
            "Through \"Gnostic\", you can say infinite\x01",
            "It is said that you have lodged knowledge.\x01\x01",
            "── When it reaches \"wisdom\", \"Son\" wakes up,\x01",
            "It will be a true god \"D\".\x01",
            "And the intention and soul of all people\x01",
            "It is consolidated under \"D\"\x01",
            "Unleash people from the spell of \"goddess\".\x01\x01",
            "That was left by the predecessor of our \"D∴G Church\"\x01",
            "It is a prophecy, an ambition to be formed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6C8C")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_13_632C end

    def Function_14_6CA0(): pass

    label("Function_14_6CA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC5")
    SetChrPos(0xFE, 40, 40, 12610, 0)
    Jump("loc_6D79")

    label("loc_6CC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CEA")
    SetChrPos(0xFE, -1000, 40, 12400, 0)
    Jump("loc_6D79")

    label("loc_6CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D0F")
    SetChrPos(0xFE, 1140, 40, 12400, 0)
    Jump("loc_6D79")

    label("loc_6D0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D34")
    SetChrPos(0xFE, 110, 0, 11010, 0)
    Jump("loc_6D79")

    label("loc_6D34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D59")
    SetChrPos(0xFE, -950, 0, 10770, 0)
    Jump("loc_6D79")

    label("loc_6D59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D79")
    SetChrPos(0xFE, 1080, 0, 10720, 0)

    label("loc_6D79")

    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_6CA0 end

    def Function_15_6D88(): pass

    label("Function_15_6D88")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DA8")
    BeginChrThread(0x101, 1, 0, 14)

    label("loc_6DA8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DBF")
    BeginChrThread(0x102, 1, 0, 14)

    label("loc_6DBF")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DD6")
    BeginChrThread(0x103, 1, 0, 14)

    label("loc_6DD6")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DED")
    BeginChrThread(0x104, 1, 0, 14)

    label("loc_6DED")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E04")
    BeginChrThread(0x109, 1, 0, 14)

    label("loc_6E04")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1B")
    BeginChrThread(0x105, 1, 0, 14)

    label("loc_6E1B")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E32")
    BeginChrThread(0x106, 1, 0, 14)

    label("loc_6E32")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E49")
    BeginChrThread(0x10A, 1, 0, 14)

    label("loc_6E49")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E63")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_6E63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E7C")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_6E7C")

    Return()

    # Function_15_6D88 end

    def Function_16_6E7D(): pass

    label("Function_16_6E7D")

    ClearScenarioFlags(0x1, 6)
    ClearScenarioFlags(0x1, 7)
    ClearScenarioFlags(0x2, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B3")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ECF")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6ECF")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F03")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F03")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F37")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F37")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F6B")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F6B")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6F9F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FD3")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_6FD3")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7007")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_7007")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_703B")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    Jump("loc_70AE")

    label("loc_703B")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7072")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x1, 7)
    Jump("loc_70AE")

    label("loc_7072")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A9")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_70AE")

    label("loc_70A9")

    Jump("loc_70B3")

    label("loc_70AE")

    Jump("loc_6E90")

    label("loc_70B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7A46")
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
            "Oh, everyone ……\x01",
            "Combat notebook\x01",
            "It seems that Oita is getting buried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to refrain from the monster's information\x01",
            "Would you mind letting me see it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#12PYeah, pleased.\x02",
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
            "I will return the notebook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This will be for this time.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B6")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received one.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 1)
    Jump("loc_762D")

    label("loc_72B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7319")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "1000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received two.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 2)
    Jump("loc_762D")

    label("loc_7319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Three, received.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 3)
    Jump("loc_762D")

    label("loc_737C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73DF")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "2000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received four.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 4)
    Jump("loc_762D")

    label("loc_73DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7442")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received five.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 5)
    Jump("loc_762D")

    label("loc_7442")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A5")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "3000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 6 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 6)
    Jump("loc_762D")

    label("loc_74A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7508")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 7 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 7)
    Jump("loc_762D")

    label("loc_7508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756B")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "4000 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received eight.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 8)
    Jump("loc_762D")

    label("loc_756B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75CE")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４500 Mira\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 9 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 9)
    Jump("loc_762D")

    label("loc_75CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_762D")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "5000 mirrors\x07\x00",
            "Received.\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 10 pieces.\x02",
        )
    )

    AddItemNumber('Ｕ材料', 10)

    label("loc_762D")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7669")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣布料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received two.\x02",
        )
    )

    AddItemNumber('神圣布料', 2)
    CloseMessageWindow()
    Jump("loc_769A")

    label("loc_7669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_769A")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣布料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    AddItemNumber('神圣布料', 1)
    CloseMessageWindow()

    label("loc_769A")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77D7")

    ChrTalk(
        0x8,
        (
            "And if the monster's information gathers\x01",
            "Please drop in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_775F")

    ChrTalk(
        0x102,
        "#12P#0100FI will bother you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_775F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7796")

    ChrTalk(
        0x103,
        "#12P#0200FI will also bother you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_77D2")

    label("loc_7796")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77D2")

    ChrTalk(
        0x104,
        "#12P#0300FI will also let you interfere.\x02",
    )

    CloseMessageWindow()

    label("loc_77D2")

    Jump("loc_79DE")

    label("loc_77D7")


    ChrTalk(
        0x8,
        (
            "Information on the new demons\x01",
            "You seem to have gathered enough.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This also means future safety measures\x01",
            "I think that it can be made more thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FHaha … … it is an honor to serve you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, you guys really\x01",
            "I am indebted to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, this time\x01",
            "Special remuneration will be given as well.\x01",
            "Please accept it.\x02",
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
            "10000 Mira\x07\x00",
            "Received.\x02",
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
            "Your success in the future\x01",
            "I pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something again\x01",
            "You can come anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79DE")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_79F5")
    ClearScenarioFlags(0x1, 5)

    label("loc_79F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A0E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A27")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_7A27")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_7B88")

    label("loc_7A46")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AFD")

    ChrTalk(
        0x8,
        (
            "Information gathered at headquarters is also\x01",
            "I think that it is sufficient already,\x01",
            "Survey will be done so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also something to ask of you\x01",
            "There may be.\x01",
            "At that time I would appreciate your favor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B88")

    label("loc_7AFD")


    ChrTalk(
        0x8,
        (
            "The content of the fighting notebook is also\x01",
            "It seems they are getting collected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If more information gathers\x01",
            "Please show me.\x01",
            "Because you have me refrain from the information.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B88")

    Return()

    # Function_16_6E7D end

    def Function_17_7B89(): pass

    label("Function_17_7B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB2")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BCD")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BE3")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BF9")
    Call(0, 18)
    Jump("loc_7CE4")

    label("loc_7BF9")

    TalkBegin(0x9)

    ChrTalk(
        0x9,
        (
            "#01900FEveryone, \"Pomutto! \"\x01",
            "Do you know the guiding game?\x02\x03",
            "#01909FHuhu, in fact, I also started.\x01",
            "Please exchange your account if you do not mind.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Account of Franc\"\x07\x00",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    TalkEnd(0x9)

    label("loc_7CE4")

    Jump("loc_7CEC")

    label("loc_7CE9")

    Call(0, 18)

    label("loc_7CEC")

    Return()

    # Function_17_7B89 end

    def Function_18_7CED(): pass

    label("Function_18_7CED")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7CFE")
    Jump("loc_9C26")

    label("loc_7CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7D0C")
    Jump("loc_9C26")

    label("loc_7D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB9")
    SoundLoad(803)

    ChrTalk(
        0x9,
        (
            "#01901FMi, everyone,\x01",
            "It became a serious thing.\x02\x03",
            "The police headquarters, too,\x01",
            "From this morning all the time …\x02",
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
        "#01905FOh, I'm sorry -\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    OP_24(0x323)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x9,
        (
            "#01903FYes, here Crossbell Police -\x02\x03",
            "#01901FYes, yes …\x02\x03",
            "Yes, from last night\x01",
            "The guard on the convergence of the situation -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(It looks like I'm busy with running water … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yes, we also\x01",
            "Let's do what we should do. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 7)
    OP_24(0x323)
    Jump("loc_7F65")

    label("loc_7EB9")

    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The franc is communicating with the communicator.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01901FYes, yes …\x02\x03",
            "#01908F……I'm sorry.\x01",
            "Regarding the identity of the armed group\x01",
            "What is clear yet …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F65")

    Jump("loc_9C26")

    label("loc_7F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_END)), "loc_8063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F85")
    Call(0, 21)
    Jump("loc_805E")

    label("loc_7F85")


    ChrTalk(
        0x9,
        (
            "#01900FAs I mentioned earlier,\x01",
            "Derivative boat at the dock of the port area\x01",
            "I arranged it.\x02\x03",
            "#01904FA mechanic in the vicinity\x01",
            "Since it is supposed to come,\x01",
            "Please visit there ~!\x02\x03",
            "#01900FPlease be careful and go, everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_805E")

    Jump("loc_9C26")

    label("loc_8063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_83A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82EC")

    ChrTalk(
        0x9,
        (
            "#01900FEveryone, Yesterday\x01",
            "I really appreciate your work ~.\x02\x03",
            "As for organization called \"association\"\x01",
            "Even if it causes the train accident,\x01",
            "It sounds like you were carer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo, actually it's a big deal\x01",
            "I did not do it though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, even in response to the accident\x01",
            "Those who worked overnight were\x01",
            "I guess it was very difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FStill, yesterday everyone also\x01",
            "Searching activity quite late at night\x01",
            "It continued, did not it?\x02\x03",
            "#01902FRepeatedly,\x01",
            "Please be careful about physical condition management.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202FThank you for your concern.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FWell, I guess the busy days are the same,\x01",
            "Do not push your frank too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FOk, got it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 0)
    Jump("loc_839E")

    label("loc_82EC")


    ChrTalk(
        0x9,
        (
            "#01900FToday's new support request\x01",
            "Seems that some are coming … …\x02\x03",
            "Even strongly, no wonder\x01",
            "Please do your best on the range.\x02\x03",
            "I also do self-management firmly,\x01",
            "Because I try to avoid impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839E")

    Jump("loc_9C26")

    label("loc_83A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_85CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8502")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The franc is communicating with the communicator.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01903FYes, yes …\x02\x03",
            "#01901F……I'm sorry.\x01",
            "Regarding the cause of the accident\x01",
            "I am investigating now … ….\x02\x03",
            "Regarding the time of restoration\x01",
            "As of now it is something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FApparently the train accident\x01",
            "It seems to be doing correspondence. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(Yeah, I'm getting busy,\x01",
            "You better not interfere. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_85C6")

    label("loc_8502")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The franc is communicating with the communicator.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#01903FYes, yes …\x02\x03",
            "#01901F……I'm sorry.\x01",
            "Regarding the cause of the accident\x01",
            "I am investigating now … ….\x02\x03",
            "Regarding the time of restoration\x01",
            "As of now it is something ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85C6")

    Jump("loc_9C26")

    label("loc_85CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_87BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86E3")

    ChrTalk(
        0x9,
        (
            "#01903FBlue flower, and a phantom beast ……\x02\x03",
            "#01901FI feel somewhat impressed by him\x01",
            "Anyway, we can do what we can\x01",
            "You have no choice but to do.\x02\x03",
            "Um, what about you guys\x01",
            "Please be careful now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FFuran also supports you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_87B7")

    label("loc_86E3")


    ChrTalk(
        0x9,
        (
            "#01903FIt is called tension state by independent advocacy,\x01",
            "This is called abnormal situation,\x01",
            "I receive some sinister impression.\x02\x03",
            "#01901FEven if you think too much\x01",
            "I think that it is useless … …\x02\x03",
            "Anyway I also worked before my eyes\x01",
            "I will definitely go and do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B7")

    Jump("loc_9C26")

    label("loc_87BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A5D")

    ChrTalk(
        0x9,
        (
            "#01901FEveryone …… whatever \"phantom beast\"\x01",
            "You seem to be taking action?\x02\x03",
            "Just as I was at the old mine,\x01",
            "It seems to be a strange monster, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I do not know yet\x01",
            "All that is done.\x01",
            "I will go ahead with the survey for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FIs it? Is something anxious about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FOh yeah, Illusion animals are pretty\x01",
            "I heard the story is tough … …\x01",
            "You do not want me to get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYeah, well.\x02\x03",
            "#10100FBut I will not overdo it,\x01",
            "Do not worry too much so do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FYes … That's right.\x02\x03",
            "And what about you guys?\x01",
            "It is a mission support department of Bachamachi.\x02\x03",
            "#01909FFran · Seeker,\x01",
            "Believe in your good fight\x01",
            "I would like to wait for the report!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FThank you,\x01",
            "Fran? -chan.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 1)
    Jump("loc_8AE3")

    label("loc_8A5D")


    ChrTalk(
        0x9,
        (
            "#01902FEveryone, survey of phantom beasts,\x01",
            "Please be careful and go.\x02\x03",
            "Fran · Seeker,\x01",
            "Believe in your good fight\x01",
            "Because I will wait for the report!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AE3")

    Jump("loc_9C26")

    label("loc_8AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B03")
    Call(0, 20)
    Jump("loc_8D4E")

    label("loc_8B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C98")

    ChrTalk(
        0x9,
        (
            "#01900FAssistant Yulia is drinking\x01",
            "Very cool …\x01",
            "I really adore you ~.\x02\x03",
            "#01909FWell, older sister is\x01",
            "I think that it is cool\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHa, this kid … …\x02\x03",
            "#10101FWhen other Fan fans of Juria listen\x01",
            "I think I'm definitely getting angry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, how about something?\x01",
            "If you are like Assistant Yulia\x01",
            "Although it seems to have a fairly good fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FRight ~, is not it ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FDo not bother me …\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8D4E")

    label("loc_8C98")


    ChrTalk(
        0x9,
        (
            "#01900FToday's security of Orkis Tower,\x01",
            "Because it's a corner so too I\x01",
            "I want to be assigned to you ~.\x02\x03",
            "#01906FIt is dignified and it is very good-looking\x01",
            "Assistant Yulia and her sister,\x01",
            "I wanted to see how to guard ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D4E")

    Jump("loc_9C26")

    label("loc_8D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F70")
    TurnDirection(0x9, 0x109, 0)

    ChrTalk(
        0x9,
        (
            "#01902FOh, older sister.\x02\x03",
            "You participated in the security of the unveiling ceremony, right?\x01",
            "- How was it, was it amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes, it is already.\x02\x03",
            "Especially in the Kingdom of Libert\x01",
            "With Princess Claudia\x01",
            "Associate Julia is wonderful -\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01905FWell, I saw you so close! Is it?\x02\x03",
            "#01906FWow, nice.\x01",
            "My sister is only cynical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha, sorry france.\x01",
            "I will make it up to you with something next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Hell, Franc is naturally\x01",
            "Is it a fans of Assistant Yulia? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Well, what kind of situation is it?\x01",
            "A man of the world stands upright. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 6)
    Jump("loc_8FD3")

    label("loc_8F70")


    ChrTalk(
        0x9,
        (
            "#01902FTo Princess Claudia -\x01",
            "Also, Assistant Yulia … …!\x02\x03",
            "Okay, me too\x01",
            "I wanted to see you nearby.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FD3")

    Jump("loc_9C26")

    label("loc_8FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91EA")

    ChrTalk(
        0x9,
        (
            "#01902FHuhu, at last from tomorrow\x01",
            "The trade meeting will start.\x02\x03",
            "Heads from various countries gathered,\x01",
            "There is an unveiling ceremony for the Orchis Tower ……\x01",
            "I am excited at something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI am not a child anymore\x01",
            "Do not say only carefree\x01",
            "Stay focused on work?\x02\x03",
            "#10106FFrancs during the conference\x01",
            "You are busier than usual, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01900FThat's right, but that's why\x01",
            "I have to find fun.\x02\x03",
            "Onee - in -\x01",
            "It is always too serious ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHuh, I can say it certainly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FWow, you are …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FHaha ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x148, 7)
    Jump("loc_9270")

    label("loc_91EA")


    ChrTalk(
        0x9,
        (
            "#01902FCertainly my work is busy,\x01",
            "Such a big event is\x01",
            "It is somewhat exciting ~ is not it ~.\x02\x03",
            "#01909FHehe, I'm looking forward to the ceremony tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9270")

    Jump("loc_9C26")

    label("loc_9275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_9338")

    ChrTalk(
        0x9,
        (
            "#01901FIn the story of Mayor of Vixen,\x01",
            "Okay, the inside of the old mine is strange\x01",
            "I heard he is getting turned on.\x02\x03",
            "What is wrong is\x01",
            "I do not quite understand it … ….\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C26")

    label("loc_9338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_9591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9353")
    Call(0, 19)
    Jump("loc_958C")

    label("loc_9353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D9")

    ChrTalk(
        0x9,
        (
            "#01906FHey ~, Onee\x01",
            "I got to call\x01",
            "It was really good ~.\x02\x03",
            "#01902FWith this without heart\x01",
            "For operation\x01",
            "It is likely to concentrate ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10106FAnd the more I hurt my work\x01",
            "I was sick … ….?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    ChrTalk(
        0x9,
        (
            "#01901FBecause, for me\x01",
            "It is a life and death problem ~! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Oh, now, courtesy at work … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(No, noon noel.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_958C")

    label("loc_94D9")


    ChrTalk(
        0x9,
        (
            "#01902FHehe, with this\x01",
            "For operation\x01",
            "It is likely to concentrate ~.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x109, 500)

    ChrTalk(
        0x9,
        (
            "#01909FGood luck with your work today,\x01",
            "Onee sister\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(I will not say anything anymore ……)\x02",
    )

    CloseMessageWindow()

    label("loc_958C")

    Jump("loc_9C26")

    label("loc_9591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A97")

    ChrTalk(
        0x9,
        (
            "#01900FHuhu, even so\x01",
            "Activities of the mission support department finally\x01",
            "It was restarted ~ is not it ~.\x02\x03",
            "#01909FAs an operator\x01",
            "As I was involved\x01",
            "The impression is also one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha, we also\x01",
            "What I came back to the support department\x01",
            "I will realize again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuh, you are right.\x01",
            "Also with Fran\x01",
            "I can do my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FYes, for operation\x01",
            "It's like getting fever ~!\x02\x03",
            "#01906FWhile you are off,\x01",
            "Citizen's request was also enthusiastic\x01",
            "It was a hard time to deal with ……\x02\x03",
            "#01902FThe restart of activities of this support section,\x01",
            "I was really looking forward to it ~.\x02\x03",
            "#01909F… and finally, with my older sister\x01",
            "I can work together!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00009FHaha … I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FAlready, Fran …\x01",
            "My sister is useless\x01",
            "How many times are you going to make it say?\x02\x03",
            "#10101FGood? How much sister\x01",
            "Because the workplace is the same\x01",
            "I must say the least ceremony.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#01906FOoh … I'm sorry.\x02\x03",
            "#01908FBut, I do not get used to it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10103FThat's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHaha, it is a tough sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FAnd anyway ~ …\x02\x03",
            "#01900FAfterwards with Tio\x01",
            "If Randy joins\x01",
            "It is no longer an enemy.\x02\x03",
            "#01902FHuhu, you all gather\x01",
            "I can hardly wait for it from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I feel the same.\x02\x03",
            "#00002FWell then……\x01",
            "Regards, once again, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 1)
    Jump("loc_9C26")

    label("loc_9A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B7F")

    ChrTalk(
        0x9,
        (
            "#01902FHaha, I can work with you again\x01",
            "The enthusiasm also enters operation.\x02\x03",
            "#01909FSister …. Kohon.\x01",
            "Noel, I can work with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Already this kid … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Well, alright ……)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9C26")

    label("loc_9B7F")


    ChrTalk(
        0x9,
        (
            "#01900FIn resuming activities of the support department,\x01",
            "A lot of requests from now\x01",
            "I think that it comes in.\x02\x03",
            "#01909FAs before, as an operator\x01",
            "I will support you firmly ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C26")

    TalkEnd(0x9)
    Return()

    # Function_18_7CED end

    def Function_19_9C2A(): pass

    label("Function_19_9C2A")

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
            "#01900FOh, exactly where it is ~!\x02\x03",
            "#01901FActually, Sister …… Noel,\x01",
            "I have an important story, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWell, what's wrong?\x01",
            "Such a serious face ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01908Fyou know what…………………………………\x02\x03",
            "#01906F…… by all means, at work\x01",
            "You should not call \"older sister\"?\x02",
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
        "#00006F#12PGokutama ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FWhat do you think is something ……\x02\x03",
            "#10101F…… Kohon.\x01",
            "When I am dispatched to the support department\x01",
            "You explained it over and over?\x02\x03",
            "#10103FBecause the workplace is the same\x01",
            "It is said that we can not afford the minimum courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01905FBut, sister ……\x01",
            "It is not Noel ……\x02\x03",
            "#01906FAhhh, it is no use!\x01",
            "How I can not get used to it ~!\x02",
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

    def lambda_9FDB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FDB)
    Sleep(50)

    def lambda_9FEB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FEB)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#00012FWell, well … … Noel.\x01",
            "To make it tighter so far\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FHehe, that's right.\x01",
            "When Mr. Fran said \"Noel\"\x01",
            "I feel like I am too overwhelmed … ….\x02\x03",
            "#00100FIf it is an unfamiliar way of calling at the time of urgent contact,\x01",
            "I wonder if it will be inefficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FWell, it may be so ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01902FHo!\x01",
            "Everyone is saying this way!\x02\x03",
            "#01909F\"Oya-chan\" is a good one, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, if you are a little ur\x01",
            "In the stance of the support department\x01",
            "Do not you agree?\x02\x03",
            "#10302FBecause, see, from the section chief\x01",
            "I feel like that.\x02",
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
        "#5P#00006F(I can not reply to that point …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106F…… Ha, it can not be helped.\x01",
            "If everyone is saying that … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FHooray~! Well then it's a rule!\x02\x03",
            "#01900FEven, everyone\x01",
            "Thank you~!\x02\x03",
            "#01904FKohon, then then …\x02\x01",
            "#01909FOnee, please refresh me\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10101FBut, Fran.\x01",
            "Even if public and private confusion alone … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909F分かってるって、Onee sister\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106F(But, I do not know absolutely … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(No, Noel has no form in Fran.\x02",
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

    # Function_19_9C2A end

    def Function_20_A4AB(): pass

    label("Function_20_A4AB")

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
            "#01900FOh, Tio!\x01",
            "It seems they finally came home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYeah, thanks to you.\x02\x03",
            "#00204FFran, sorry again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FHuhu, this is it ~.\x02\x03",
            "#01900FAnyway, in this\x01",
            "Everyone at the Special Affairs Division\x01",
            "You became a full member ~!\x02\x03",
            "I expect more success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FThank you, Fran.\x01",
            "I will make my best effort.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01905FOh ….\x01",
            "I have to say thank you again!\x02\x03",
            "#01900FOnee-san, Assigned by Assassin Yulia\x01",
            "You got me a minute too ~!\x02\x03",
            "#01909FThank you so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FAh, because you do not mind.\x02\x03",
            "#10106FI just talked to the face only\x01",
            "I'm sorry for Fran. ….\x02\x03",
            "#10100FI will hand it over when I calm down next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01909FYes, I am looking forward to it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FSpeaking of which I said yesterday at Arseille\x01",
            "Ellie and Noel got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, Princess Hime and Assistant Yulia\x01",
            "It was truly a broad mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00302FHa ha, after all Fran-chan\x01",
            "Are you a fan of Mr. Julia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01904FOf course!\x02\x03",
            "#01900FAssistant Yulia is drinking\x01",
            "Very cool …\x01",
            "I really adore you ~.\x02\x03",
            "#01909FWell, even my older sister is still\x01",
            "ダントツにI think that it is cool\x02",
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
            "#12P#10111FJust … … hey … …!\x02\x03",
            "#10106FWhat a terrible thing to do\x01",
            "I'm telling you, Fran. …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, for Fran\x01",
            "No matter what\x01",
            "Noel is the most like you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FWell, it is truly …\x02",
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

    # Function_20_A4AB end

    def Function_21_ABB8(): pass

    label("Function_21_ABB8")

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
            "#01905FOh, everyone ……\x02\x03",
            "#01900FAs I mentioned earlier,\x01",
            "Derivative boat at the dock of the port area\x01",
            "I arranged it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, thanks, Fran.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYou can use it immediately.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#01903FIn order to search for hoarders\x01",
            "It seems to be heading to wetlands … …\x02\x03",
            "#01908FIs that okay, is not it ~ ……?\x01",
            "A hypocenter who can reach Class A,\x01",
            "A place where two people are missing …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00200FMr. Fran. ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FSorry, I'm worried … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01906FHa, at this time also to me\x01",
            "I wish I could do something ……\x02\x03",
            "#01900FUm, good luck charm\x01",
            "Will you take Bang Bang?\x02",
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
        "#12P#00005FYou mean Bang Bang …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FEr …\x01",
            "It is a bear's stuffed animal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FI feel relaxed when I embrace ~!\x02\x03",
            "#01900FWhen neither your sister nor anyone is watching\x01",
            "Sometimes you do it ~!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#12P#10111FA little! Is it?\x01",
            "Oh, that's what I meant …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01901FIn places where Bang Bang may be in danger\x01",
            "It is the thought of the bowel to send in,\x01",
            "Good for everyone … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo, no, well …\x01",
            "Let me calm down for the time being.\x02\x03",
            "#00002FHaha, but I am grateful.\x01",
            "Although I was a bit uneasy,\x01",
            "I feel I could relax somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, this is the true value of Fran.\x02\x03",
            "#10309FNoel's private was a glimpse.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#12P#10106F(Uu, if it francs\x01",
            "Please remember later … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01909FHaha, I wish it had been.\x02\x03",
            "#01900FPlease be careful and go, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAh!\x02",
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

    # Function_21_ABB8 end

    def Function_22_B30F(): pass

    label("Function_22_B30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B32D")
    Call(0, 47)
    Return()

    label("loc_B32D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B33E")
    Jump("loc_BDFC")

    label("loc_B33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B34C")
    Jump("loc_BDFC")

    label("loc_B34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B3DF")

    ChrTalk(
        0xFE,
        (
            "The red constellation,\x01",
            "With all the power of Crossbell\x01",
            "I will exclude it anyhow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You too, to ourselves\x01",
            "Please do what you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDFC")

    label("loc_B3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B3ED")
    Jump("loc_BDFC")

    label("loc_B3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B3FB")
    Jump("loc_BDFC")

    label("loc_B3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7DC")

    ChrTalk(
        0xFE,
        "It looks stained, does not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Bin that Emma has,\x01",
            "Is that nutrient or something …? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(It looks like … ….\x01",
            "Are you very tired? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, \"Sporitan X\" -\x02\x03",
            "Especially something punchy\x01",
            "You seem to be drinking.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FWa, you -\x02",
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
            "So it's all-night long.\x01",
            "It can not be helped!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or is it?\x01",
            "I drink nutritional drinks\x01",
            "Are you saying so funny?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Answer--\x01",
            "Lloyd · Bannings investigator!\x02",
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
        "#00006FNo, I do not have anything else …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh, huh ……\x01",
            "It means that there is no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyways,\x01",
            "You guys are in such a place\x01",
            "Can I sell oil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That … … with support requests\x01",
            "You should do more than one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F(Huh, it was kind of a disaster.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(… … You do not say.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x171, 6)
    Jump("loc_B844")

    label("loc_B7DC")


    ChrTalk(
        0xFE,
        (
            "Anyway, at this place\x01",
            "Do not sell oil and request assistance\x01",
            "You should do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "- The talk is over.\x02",
    )

    CloseMessageWindow()

    label("loc_B844")

    Jump("loc_BDFC")

    label("loc_B849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B857")
    Jump("loc_BDFC")

    label("loc_B857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B865")
    Jump("loc_BDFC")

    label("loc_B865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_BA96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B88D")
    Call(0, 30)
    Jump("loc_B933")

    label("loc_B88D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B89F")
    Call(0, 31)
    Jump("loc_B933")

    label("loc_B89F")


    ChrTalk(
        0xFE,
        (
            "Mr. Dudley\x01",
            "What I'm expecting from the support department\x01",
            "It is an activity as a soldier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you think about its meaning\x01",
            "You should see what you should do … …\x01",
            "I have asked for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B933")

    Jump("loc_BA91")

    label("loc_B938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA04")

    ChrTalk(
        0xFE,
        (
            "Rector Arundole,\x01",
            "About Kirika · Lowe\x01",
            "Let 's continue marking in the investigation department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What are the major powers planning … …\x01",
            "Although I can not measure it at the present moment,\x01",
            "I have to investigate strongly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_BA91")

    label("loc_BA04")


    ChrTalk(
        0xFE,
        (
            "Rector Arundole,\x01",
            "About Kirika · Lowe\x01",
            "Please leave it to the Investigation One Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys, once you\x01",
            "You should return to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA91")

    Jump("loc_BDFC")

    label("loc_BA96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BDE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD4B")

    ChrTalk(
        0xFE,
        (
            "Bannings investigator ……\x01",
            "Is the job of request for assistance smooth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah well … for the time being\x01",
            "I do it at the usual pace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……Is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Mr. Dudley\x01",
            "At the Orkis Tower at the plenary session\x01",
            "We are finalizing the security system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sergey Managerも本日一杯は\x01",
            "We plan to adjust each direction at the measures headquarters on the second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… …. You too,\x01",
            "It is to tighten your mind and come to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That '\x01",
            "Not saying the usual pace#22R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#Well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, it is consent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Huh, as usual\x01",
            "It is a hurting older sister. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, I'm silent.\x01",
            "I'm pretty pretty. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Randy seniors,\x01",
            "Such a problem … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 0)
    Jump("loc_BDE0")

    label("loc_BD4B")


    ChrTalk(
        0xFE,
        (
            "ダドリーさんもSergey Managerも\x01",
            "Maximize the power you can possess\x01",
            "I am in charge of duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… …. You too,\x01",
            "It is to tighten your mind and come to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDE0")

    Jump("loc_BDFC")

    label("loc_BDE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_BDF3")
    Jump("loc_BDFC")

    label("loc_BDF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_BDFC")

    label("loc_BDFC")

    TalkEnd(0xFE)
    Return()

    # Function_22_B30F end

    def Function_23_BE00(): pass

    label("Function_23_BE00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE1F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE1F")
    Call(0, 52)
    Return()

    label("loc_BE1F")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_23_BE00 end

    def Function_24_BE26(): pass

    label("Function_24_BE26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BE37")
    Jump("loc_C635")

    label("loc_BE37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE45")
    Jump("loc_C635")

    label("loc_BE45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C00A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF4B")

    ChrTalk(
        0xFE,
        (
            "It was terrible\x01",
            "It became a troublesome thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being, in the second section,\x01",
            "Close your eyes to all other issues\x01",
            "I am trying to support the department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The intelligence worker entering the crossbell …\x01",
            "Especially from the end of the information of the empire's intelligence agent\x01",
            "I am in the middle of washing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C005")

    label("loc_BF4B")


    ChrTalk(
        0xFE,
        (
            "For the time being, in the second section,\x01",
            "Close your eyes to all other issues\x01",
            "I am trying to support the department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The intelligence worker entering the crossbell …\x01",
            "Especially from the end of the information of the empire's intelligence agent\x01",
            "I am in the middle of washing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C005")

    Jump("loc_C635")

    label("loc_C00A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C1BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C142")

    ChrTalk(
        0xFE,
        "Gnostic ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "First off,\x01",
            "From the route of Rubatse\x01",
            "I plan to hit it again … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, from there\x01",
            "The possibility of flowing is low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, at any stage now\x01",
            "Even though I think about it, it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, one by one\x01",
            "It seems to only crush it surely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C1B8")

    label("loc_C142")


    ChrTalk(
        0xFE,
        (
            "Well, at any stage now\x01",
            "Even though I think about it, it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, one by one\x01",
            "It seems to only crush it surely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1B8")

    Jump("loc_C635")

    label("loc_C1BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1CB")
    Jump("loc_C635")

    label("loc_C1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C368")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C2A1")

    ChrTalk(
        0xFE,
        (
            "Even though the support department cooperated,\x01",
            "Raymond's guy yesterday\x01",
            "It seemed quite good for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But chasing fake brand quoters\x01",
            "After encountering the remnants of terrorists,\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C363")

    label("loc_C2A1")


    ChrTalk(
        0xFE,
        (
            "Although the black moon was moving behind the scenes,\x01",
            "Raymond's guy was alone yesterday\x01",
            "It seemed quite good for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But chasing fake brand quoters\x01",
            "After encountering the remnants of terrorists,\x01",
            "I can not believe it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C363")

    Jump("loc_C635")

    label("loc_C368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C40B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C383")
    Call(0, 25)
    Jump("loc_C406")

    label("loc_C383")


    ChrTalk(
        0xFE,
        (
            "Originally the work of the section of one department\x01",
            "Some are two people\x01",
            "It is supposed to take over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway this situation.\x01",
            "It is exactly the structure of total mobilization.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C406")

    Jump("loc_C635")

    label("loc_C40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_C419")
    Jump("loc_C635")

    label("loc_C419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_C427")
    Jump("loc_C635")

    label("loc_C427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C435")
    Jump("loc_C635")

    label("loc_C435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_C49D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C450")
    Call(0, 26)
    Jump("loc_C498")

    label("loc_C450")


    ChrTalk(
        0xA,
        (
            "Orbitless young people ……\x01",
            "Want to annoy human beings\x01",
            "What is fun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C498")

    Jump("loc_C635")

    label("loc_C49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_C635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4B8")
    Call(0, 27)
    Jump("loc_C635")

    label("loc_C4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5C7")

    ChrTalk(
        0xFE,
        (
            "Well, anyway.\x01",
            "When something happens in the future\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To you, we also have the investigation department two\x01",
            "I'm expecting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYes.\x02\x03",
            "(Something like that\x01",
            "I am purely glad. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F(Yeah, we too\x01",
            "It feels like it has been accepted. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C635")

    label("loc_C5C7")


    ChrTalk(
        0xFE,
        (
            "ま、When something happens in the future\x01",
            "どうかI'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To you, we also have the investigation department two\x01",
            "I'm expecting you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C635")

    TalkEnd(0xFE)
    Return()

    # Function_24_BE26 end

    def Function_25_C639(): pass

    label("Function_25_C639")

    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        "You seem to be a special support department.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        (
            "#00603FWho are you thinking?\x02\x03",
            "#00600FWhatever the \"phantom beast\"\x01",
            "You seem to have undertaken the investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, yes, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHuh, I heard ear quickly.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x105, 500)

    ChrTalk(
        0xC,
        (
            "#00603FHun, it's an official request of the guard.\x01",
            "Of course the information flows … …\x02\x03",
            "#00600FAs far as I hear the story, apparently in common sense\x01",
            "It seems like an unmeasured opponent.\x02\x03",
            "When engaged,\x01",
            "You should at best enter the spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you for your advice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEven so ……\x01",
            "There is a work of counterintelligence\x01",
            "It seems pretty busy, is not it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    ChrTalk(
        0xA,
        (
            "Well, there is no proposal for independence\x01",
            "I'm done loudly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Trying to explore the trend of crossbell,\x01",
            "Intelligence agents from continent countries one after another\x01",
            "It is a situation that is being sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "That's it, simply\x01",
            "Just try to grasp\x01",
            "There are as many intelligence agents as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FIs that so?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x109, 500)

    ChrTalk(
        0xC,
        (
            "#00601F…… In addition, \"Red constellation\" and\x01",
            "There is also a trend of \"black moon\".\x02\x03",
            "Needless to say,\x01",
            "To respond to crimes other than those\x01",
            "I can not pull out my hand.\x02\x03",
            "#00603FFor cases to be addressed,\x01",
            "It is exactly how much it exists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, there are circumstances like that\x01",
            "Some of the work of the section of department\x01",
            "二課でIt is supposed to take over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By that, with a little\x01",
            "I had a meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see……\x01",
            "I was talking about that kind of story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWhat kind?\x01",
            "It seems to be a tough situation in various ways.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x104, 500)

    ChrTalk(
        0xC,
        (
            "#00603FHuh, even how\x01",
            "Whether the hand is limited\x01",
            "I just do what I should do.\x02\x03",
            "#00601FAnyway, you also\x01",
            "It is to fulfill a given role.\x02\x03",
            "Even if it's a matter of \"phantom beast\", about\x01",
            "It is not a problem that can be left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetScenarioFlags(0x16A, 2)
    Return()

    # Function_25_C639 end

    def Function_26_CC3F(): pass

    label("Function_26_CC3F")

    OP_4B(0xA, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0xA,
        (
            "by the way,\x01",
            "I am a young man of a runaway car of the example … …\x01",
            "You said you were arrested yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Well, I can not let it go down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Because it is only a fine punishment\x01",
            "It looked like I was not holding it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Tentatively for the time being, in the city\x01",
            "Considering what you do not see, a bit\x01",
            "I wonder if there was an effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I hope that it will be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Geez, he must be a foreigner\x01",
            "It is also possible to hold down and hold down\x01",
            "I could do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, that part is about the future improvement of law\x01",
            "Is expectation a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "That's right, oh well.\x01",
            "Ugili can do things on the path\x01",
            "I just do it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_CEC8")

    ChrTalk(
        0x101,
        (
            "#00001FApparently,\x01",
            "It seems to be the story of that three people. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(Looks like, dangerous driving is\x01",
            "I do not want you to do it again … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF06")

    label("loc_CEC8")


    ChrTalk(
        0x101,
        (
            "#00001F(Yesterday, or ……\x01",
            "Did something happen in the city? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF06")

    SetScenarioFlags(0x13E, 7)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_26_CC3F end

    def Function_27_CF1C(): pass

    label("Function_27_CF1C")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        (
            "Oh, something fresh happens\x01",
            "It seems to be mixed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Perhaps they are rumors\x01",
            "Are you a new member of the Special Affairs Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        (
            "That means,\x01",
            "You are a guard Noel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Muhuu, if you do not mind\x01",
            "How about even having a cup of tea together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FLet me see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FUnfortunately, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Heck …\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 500)

    ChrTalk(
        0xB,
        (
            "You are such a\x01",
            "Waj · Hemisphere of Testament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… What do you mean, looking closer?\x01",
            "You have a pretty beautiful face ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuhu, is it so?\x02\x03",
            "#10304FBut unfortunately, I do not care about you\x01",
            "It looks like it's not a type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, that's right ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "- Why are they male?\x01",
            "I have to dent it!\x02",
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
            "…… Well, I'd have to listen silently\x01",
            "Do not be silly saying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ome too, the support department\x01",
            "Go and learn from these people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What if also from the police school\x01",
            "Shall I arrange to be able to get out?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    ChrTalk(
        0xB,
        (
            "Mr. Guard, that's it\x01",
            "Please be patient for me.\x02",
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

    # Function_27_CF1C end

    def Function_28_D3A3(): pass

    label("Function_28_D3A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D58D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D522")

    ChrTalk(
        0xFE,
        (
            "Hello, please listen.\x01",
            "もうすぐDonovanが\x01",
            "I will return to the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To fill the hole of the police station\x01",
            "There were many difficulties, too,\x01",
            "This seems to be released at last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FIt was good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIf the policeman asked me such a thing\x01",
            "It seems to be overlooked.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Oops, that's right.\x01",
            "… … Try to be naughty ~ ~?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D588")

    label("loc_D522")


    ChrTalk(
        0xFE,
        (
            "If the police came back\x01",
            "The second section of the investigation is also safe ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay then, until then,\x01",
            "I have to do my best ~!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D588")

    Jump("loc_DD06")

    label("loc_D58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D59B")
    Jump("loc_DD06")

    label("loc_D59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D647")

    ChrTalk(
        0xFE,
        (
            "Without prior notice\x01",
            "Suddenly came\x01",
            "I thought that I incorporated it into the Defense Force … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not say it out loud,\x01",
            "It is also a good place to get ridiculous.\x01",
            "…… Huh, what the hell are you doing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD06")

    label("loc_D647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D655")
    Jump("loc_DD06")

    label("loc_D655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D72C")

    ChrTalk(
        0xFE,
        (
            "Empire has already been involved in the crime\x01",
            "It seems to deny, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still somehow under the water\x01",
            "I'm trying to find out if I can negotiate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a kind of weakness,\x01",
            "There is no doubt that there is something in it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD06")

    label("loc_D72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D7C0")

    ChrTalk(
        0xFE,
        (
            "Waldo Valles\x01",
            "Where did you get Gnostic ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it were not via Rubathe,\x01",
            "Where on earth will it be?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD06")

    label("loc_D7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D7CE")
    Jump("loc_DD06")

    label("loc_D7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DA76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D9CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D989")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys.\x01",
            "Yesterday was really saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh yeah, that's right. Yesterday night\x01",
            "An old lady came out in my dream.\x01",
            "Somehow it's chased after me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks, thanks\x01",
            "I did not sleep well.\x02",
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
            "#00006F(If you say so,\x01",
            "You seem to be dreaming like this. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F(… good luck and forget.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_D9C9")

    label("loc_D989")


    ChrTalk(
        0xFE,
        (
            "Anyways,\x01",
            "Thank you so much yesterday.\x01",
            "Thanks, I was saved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C9")

    Jump("loc_DA71")

    label("loc_D9CE")


    ChrTalk(
        0xFE,
        (
            "Fuu, yesterday was awesome\x01",
            "Have a bad dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the grandmother who was taken away yesterday\x01",
            "It's a dream chase … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sawako, when you think back\x01",
            "I'm getting a bad sweat ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA71")

    Jump("loc_DD06")

    label("loc_DA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DA84")
    Jump("loc_DD06")

    label("loc_DA84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DA92")
    Jump("loc_DD06")

    label("loc_DA92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_DAA0")
    Jump("loc_DD06")

    label("loc_DAA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DAAE")
    Jump("loc_DD06")

    label("loc_DAAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_DC62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBBA")

    ChrTalk(
        0xFE,
        (
            "In the head office within this place\x01",
            "Please leave the air awful.\x01",
            "I will definitely come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pressure from lawmakers and upper part\x01",
            "Although it is decreasing for a while,\x01",
            "The problem of autonomous province is pile up … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, when will it be a little\x01",
            "I guess I will be able to enjoy it ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_DC5D")

    label("loc_DBBA")


    ChrTalk(
        0xFE,
        (
            "Well, for the time being\x01",
            "Mr. Dieter's political reform\x01",
            "We have to support our hearts and try our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Afterwards Congressional raising salary\x01",
            "I will be happy if you do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC5D")

    Jump("loc_DD06")

    label("loc_DC62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_DD06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC7D")
    Call(0, 27)
    Jump("loc_DD06")

    label("loc_DC7D")


    ChrTalk(
        0xFE,
        (
            "Well, to the police station again\x01",
            "I got a hurting point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am a little more\x01",
            "I think I want to be firm … …\x01",
            "I can not repair personality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD06")

    TalkEnd(0xFE)
    Return()

    # Function_28_D3A3 end

    def Function_29_DD0A(): pass

    label("Function_29_DD0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DD1B")
    Jump("loc_E2F5")

    label("loc_DD1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DD29")
    Jump("loc_E2F5")

    label("loc_DD29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DF8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEDC")

    ChrTalk(
        0xC,
        (
            "#00600FYou guys.\x02\x03",
            "#00603F…… I heard the story of Orlando.\x01",
            "Apparently it is troublesome\x01",
            "It seems that it is getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYeah, but I will definitely bring it back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603FHuh, is that so?\x01",
            "Then there is nothing to say.\x02\x03",
            "#00600FAnyway, this is the situation now.\x01",
            "The work you want to impose on you\x01",
            "Naturally it is like a mountain.\x02\x03",
            "For that,\x01",
            "What are the problems of fellows?\x01",
            "Come quickly and solve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FMr. Dudley …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 3)
    Jump("loc_DF89")

    label("loc_DEDC")


    ChrTalk(
        0xC,
        (
            "#00603FOnce I have made arrangements,\x01",
            "Go to the mayor's place and take the next measures\x01",
            "We are planning to talk.\x02\x03",
            "#00600FAnyway, you also need to do\x01",
            "Get along fast enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF89")

    Jump("loc_E2F5")

    label("loc_DF8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DF9C")
    Jump("loc_E2F5")

    label("loc_DF9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DFAA")
    Jump("loc_E2F5")

    label("loc_DFAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DFB8")
    Jump("loc_E2F5")

    label("loc_DFB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E05F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFD3")
    Call(0, 25)
    Jump("loc_E05A")

    label("loc_DFD3")


    ChrTalk(
        0xC,
        (
            "#00600FAlthough the matter is in a mountainous situation,\x01",
            "Anyway, let's leave custody here.\x02\x03",
            "You guys have to do your job\x01",
            "It is to think only about what to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E05A")

    Jump("loc_E2F5")

    label("loc_E05F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E06D")
    Jump("loc_E2F5")

    label("loc_E06D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E2D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E095")
    Call(0, 30)
    Jump("loc_E123")

    label("loc_E095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A7")
    Call(0, 31)
    Jump("loc_E123")

    label("loc_E0A7")


    ChrTalk(
        0xC,
        (
            "#00603FMy person, for a while here\x01",
            "We are planning to keep an eye on the information in each direction.\x02\x03",
            "#00600FIf there is something you can do it directly.\x01",
            "Please come and contact us anytime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E123")

    Jump("loc_E2CB")

    label("loc_E128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E256")

    ChrTalk(
        0xFE,
        (
            "#00603FWith the Imperial Army Information Bureau,\x01",
            "Lock Smith institution in the Republic ……\x01",
            "Both are those you can not respect.\x02\x03",
            "When the two are in contact with each other … …\x01",
            "There is some movement under the water\x01",
            "I do not think he will make a mistake.\x02\x03",
            "#00600FAnyway, now as the police\x01",
            "There is nothing more than to do what I can do.\x02\x03",
            "If there is something again\x01",
            "Please contact here as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E2CB")

    label("loc_E256")


    ChrTalk(
        0xFE,
        (
            "#00600FAnyway, now as the police\x01",
            "There is nothing more than to do what I can do.\x02\x03",
            "If there is something again\x01",
            "Please contact here as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2CB")

    Jump("loc_E2F5")

    label("loc_E2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E2DE")
    Jump("loc_E2F5")

    label("loc_E2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_E2EC")
    Jump("loc_E2F5")

    label("loc_E2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_E2F5")

    label("loc_E2F5")

    TalkEnd(0xFE)
    Return()

    # Function_29_DD0A end

    def Function_30_E2F9(): pass

    label("Function_30_E2F9")

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
        "#00600F#2PYou guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P…… Do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PYeah …… by all means to the investigation one section\x01",
            "There was something I wanted to report.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Kirika and Lecter\x01",
            "I reported that it appeared in the city.\x02",
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
            "#00603F#2P……got it.\x02\x03",
            "Imperial Army Information Bureau and Lock Smith Agency,\x01",
            "An important person in both institutions in the city …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PMr. Dudley, this is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6P…… How do you see this case?\x02\x03",
            "At the timing we decided to hold the plenary session tomorrow\x01",
            "It is because an intelligence agent of two major countries appeared … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PIt is too good to be coincident …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHuhu, are you using them\x01",
            "I was saying it was a distraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#6PWell, you are too suspicious of fluff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2POf course, there is some speculation.\x02\x03",
            "#00600FBut, if anything\x01",
            "Because you are the one who talked to them directly\x01",
            "There should be something you can feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#12P…… It certainly might be so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00600F#2P…… Listen in reverse, Bannings.\x01",
            "For what they are,\x01",
            "Do you think it appeared in the city?\x02\x03",
            "#00603FConversation with them and moving route ……\x01",
            "There should have been a hint somewhere.\x02\x03",
            "#00600FYou guessed it, you should try saying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PThat's right.\x02",
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
            "Kirika and Lecter\x01",
            "Why did you appear in the city?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "For the security of the leaders\x01",          # 0
            "For relaxation and shopping\x01",      # 1
            "To talk to each other\x01",            # 2
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
        (0, "loc_E89A"),
        (1, "loc_E9FA"),
        (2, "loc_EB8B"),
        (SWITCH_DEFAULT, "loc_EBDC"),
    )


    label("loc_E89A")


    ChrTalk(
        0x101,
        (
            "#00001F#6PIs it because of the security of the leaders?\x02\x03",
            "#00003FFor the sake of time\x01",
            "Crossbell of the terrain in the city\x01",
            "I was grasping it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2P…… That possibility would be low.\x02\x03",
            "#00600FSecurity will be outside the jurisdiction of the intelligence agent,\x01",
            "As a matter of course they have been working for months\x01",
            "He was visiting Crossbell.\x02\x03",
            "Now check the terrain of the city\x01",
            "There is no necessity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYes, it certainly is …\x02",
    )

    CloseMessageWindow()
    Jump("loc_EBDC")

    label("loc_E9FA")


    ChrTalk(
        0x101,
        (
            "#00001F#6P…… Again, as they were saying,\x01",
            "Is it due to my relaxation and shopping?\x02\x03",
            "#00003FIn seeking a trade conference,\x01",
            "I can not say that I do not need it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2P…… That possibility would not exist.\x02\x03",
            "#00600FConsidering that it was torn down,\x01",
            "They should be merely a camouflage.\x02\x03",
            "#00606FWhew … ….\x01",
            "I thought I could do it a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#6PWait a moment, please.\x01",
            "Well then, then …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBDC")

    label("loc_EB8B")

    OP_2C(0xA3, 0x1)

    ChrTalk(
        0x101,
        (
            "#00001F#6P…… Two people had a place to talk with\x01",
            "I think there is a possibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBDC")

    label("loc_EBDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC5C")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00001F#6PThat's right, maybe …\x01",
            "Two people had a place to talk with\x01",
            "I think there is a possibility.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC5C")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_ECD6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ECD6)
    Sleep(50)

    def lambda_ECE6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ECE6)
    Sleep(50)

    def lambda_ECF6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ECF6)
    Sleep(50)

    def lambda_ED06():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ED06)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0xD,
        "#5PTalk … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00600F#2PHm … why do you think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PTheir first sighting information,\x01",
            "Both were obtained in the port area.\x02\x03",
            "#00001FBefore we start tracking,\x01",
            "Two people were in the same compartment …\x01",
            "I do not think this is coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#5PAh … … It certainly was.\x02\x03",
            "#00100FAt IBC in the port area\x01",
            "The president's visit from the previous day\x01",
            "It was scheduled … ….\x02\x03",
            "To wait for the purpose of talks\x01",
            "It might have been a convenient place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#6PIt was exactly held\x01",
            "Mitsushi event also\x01",
            "It's going to be a camouflage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PEach breath-away,\x01",
            "While disguising as president's shopping\x01",
            "I was quietly meeting …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5P…… Tsuji is likely to match.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PBut even if I say talk\x01",
            "What are you talking about?\x02\x03",
            "Initially, the Empire and the Republic\x01",
            "It should have been in confrontation\x01",
            "Was not there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5P…… That is not impossible.\x02\x03",
            "#00103FAccording to the previous cult incident,\x01",
            "Autonomous state legislature from the Imperial and Republic\x01",
            "Many of the members of the Diet failed … …\x02\x03",
            "Cooperation system between the new mayor and the new chairman\x01",
            "By building, crossbell is\x01",
            "I gradually have a voice.\x02\x03",
            "#00101FThis situation …… Empire and Republic\x01",
            "Things that can not be left alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#12PIndeed, in that respect the two major powers\x01",
            "The interests are consistent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00608F#2PI can not affirm but …\x01",
            "There is some movement under the water\x01",
            "I do not think he will make a mistake.\x02\x03",
            "#00603F…… Is it possible to say at this time?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F22D():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F22D)
    Sleep(50)

    def lambda_F23D():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F23D)
    Sleep(50)

    def lambda_F24D():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F24D)
    Sleep(50)

    def lambda_F25D():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F25D)
    Sleep(50)

    def lambda_F26D():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F26D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0xD,
        (
            "#5PRector Arundole,\x01",
            "About Kirika · Lowe\x01",
            "Let 's continue marking in the investigation department.\x02",
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
        "#00000F#6PNo, I'm pleased if you got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PTomorrow's plenary session ……\x01",
            "I hope it will not end unexpectedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603F#2PFor that, as a police now\x01",
            "There is nothing more than to do what I can do.\x02\x03",
            "#00601FIf there is something again\x01",
            "Please contact here as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6Pはい、Thank you.\x02",
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

    # Function_30_E2F9 end

    def Function_31_F476(): pass

    label("Function_31_F476")

    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xD, 0x101, 0)

    ChrTalk(
        0xD,
        "Bannings investigator.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 500)

    ChrTalk(
        0xC,
        (
            "#00600FYou guys.\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, especially now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00603FI see.\x01",
            "Do not get too caught up.\x02\x03",
            "I think that you also felt,\x01",
            "The whole city to visit VIP\x01",
            "It is in a state of emphasis a little.\x02\x03",
            "#00600FRegardless of any abnormality,\x01",
            "In such an atmosphere\x01",
            "It's a confusing thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101Findeed……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, often eye\x01",
            "I have to get over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBy the way, Mr. Dudley,\x01",
            "For a while\x01",
            "Are you coming?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "#00603FWell, for the time being, the leaders\x01",
            "Until the alkane shell theater begins\x01",
            "It is scheduled to be packed in the headquarters.\x02\x03",
            "#00600FIf there is something you can do it directly.\x01",
            "Please come and contact us anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, that's OK.\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_31_F476 end

    def Function_32_F73B(): pass

    label("Function_32_F73B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F74C")
    Jump("loc_F837")

    label("loc_F74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F780")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F77B")

    ChrTalk(
        0x11,
        "………… Chi …………\x02",
    )

    CloseMessageWindow()

    label("loc_F77B")

    Jump("loc_F837")

    label("loc_F780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F78E")
    Jump("loc_F837")

    label("loc_F78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F837")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7B5")
    Call(0, 33)
    Jump("loc_F837")

    label("loc_F7B5")

    ClearChrFlags(0x11, 0x10)

    ChrTalk(
        0x11,
        (
            "Even if you catch us\x01",
            "Even though I can only be given a fine,\x01",
            "It's too desperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Huh, the police so much\x01",
            "Do you want to earn pocket money?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F837")

    TalkEnd(0xFE)
    Return()

    # Function_32_F73B end

    def Function_33_F83B(): pass

    label("Function_33_F83B")


    ChrTalk(
        0xF,
        (
            "Well then……\x01",
            "The house you guys are now living in\x01",
            "Where is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hun, I do not have obligation to answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Well, to the common people like you\x01",
            "A place not to live at all … …\x01",
            "Just let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "(く, shit … …!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F(But, Ganbare Franz … …)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_33_F83B end

    def Function_34_F943(): pass

    label("Function_34_F943")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F954")
    Jump("loc_FA5B")

    label("loc_F954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F9B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F9AE")

    ChrTalk(
        0x12,
        "Disqualification …… Immediate suspension ah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "And it's one month …\x01",
            "Haha Ah ah ah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9AE")

    Jump("loc_FA5B")

    label("loc_F9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F9C1")
    Jump("loc_FA5B")

    label("loc_F9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FA5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FA5B")

    ChrTalk(
        0x12,
        (
            "You guys……\x01",
            "They guys who made barricades?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hun, working with Satoshi.\x01",
            "When I am getting very well\x01",
            "Why do not you match your eyes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5B")

    TalkEnd(0xFE)
    Return()

    # Function_34_F943 end

    def Function_35_FA5F(): pass

    label("Function_35_FA5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FA70")
    Jump("loc_FB73")

    label("loc_FA70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FB17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FB12")

    ChrTalk(
        0x13,
        (
            "Ha, this is the only time\x01",
            "It was truly overkill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "The car has become an Oshaka,\x01",
            "For quiet a while\x01",
            "It seems better to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB12")

    Jump("loc_FB73")

    label("loc_FB17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FB25")
    Jump("loc_FB73")

    label("loc_FB25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FB73")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FB73")

    ChrTalk(
        0x13,
        (
            "Oh, I should return home soon.\x01",
            "There is no interrogation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB73")

    TalkEnd(0xFE)
    Return()

    # Function_35_FA5F end

    def Function_36_FB77(): pass

    label("Function_36_FB77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FBE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB95")
    Call(0, 38)
    Jump("loc_FBE2")

    label("loc_FB95")


    ChrTalk(
        0xFE,
        (
            "To be honest I still feel like dreaming … …\x01",
            "I wonder what will become of the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBE2")

    Jump("loc_FEE5")

    label("loc_FBE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FBF5")
    Jump("loc_FEE5")

    label("loc_FBF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FC03")
    Jump("loc_FEE5")

    label("loc_FC03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_FD23")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FD1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCB9")

    ChrTalk(
        0xE,
        (
            "Control of runaway vehicles,\x01",
            "It was really hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As for these children,\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD19")

    label("loc_FCB9")


    ChrTalk(
        0xE,
        (
            "As for these children,\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD19")

    Jump("loc_FD1E")

    label("loc_FD1E")

    Jump("loc_FEE5")

    label("loc_FD23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FD31")
    Jump("loc_FEE5")

    label("loc_FD31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FD3F")
    Jump("loc_FEE5")

    label("loc_FD3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FD4D")
    Jump("loc_FEE5")

    label("loc_FD4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FD5B")
    Jump("loc_FEE5")

    label("loc_FD5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FD69")
    Jump("loc_FEE5")

    label("loc_FD69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FD77")
    Jump("loc_FEE5")

    label("loc_FD77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FD85")
    Jump("loc_FEE5")

    label("loc_FD85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FEE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FEE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8D")
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xE,
        (
            "What you did\x01",
            "It is a fine crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Why do not you reflect on it a little! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Huh, so do not get it wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Hansei Hansei ~.\x01",
            "Look, I regret it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "It is almost time.\x01",
            "I want you to return.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEE0")

    label("loc_FE8D")


    ChrTalk(
        0xE,
        (
            "What you did\x01",
            "It is a fine crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Why do not you reflect on it a little! Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_FEE0")

    Jump("loc_FEE5")

    label("loc_FEE5")

    TalkEnd(0xFE)
    Return()

    # Function_36_FB77 end

    def Function_37_FEE9(): pass

    label("Function_37_FEE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FF90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF07")
    Call(0, 38)
    Jump("loc_FF8B")

    label("loc_FF07")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "That presidential address\x01",
            "It's almost like declaration of war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how much you say defense forces\x01",
            "To be able to compete against two major powers\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF8B")

    Jump("loc_10198")

    label("loc_FF90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FF9E")
    Jump("loc_10198")

    label("loc_FF9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10039")

    ChrTalk(
        0xFE,
        (
            "At last it was overnight … …\x01",
            "The situation just got worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyways,\x01",
            "Even in the broad area crime prevention division\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10198")

    label("loc_10039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_100D9")

    ChrTalk(
        0xF,
        (
            "Foreigners strictly\x01",
            "It came to be regulated,\x01",
            "Although it is hard to say yet ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "This case is also an important step.\x01",
            "We can not beat the police\x01",
            "I hope you do your best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10198")

    label("loc_100D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_100E7")
    Jump("loc_10198")

    label("loc_100E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_100F5")
    Jump("loc_10198")

    label("loc_100F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10103")
    Jump("loc_10198")

    label("loc_10103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10111")
    Jump("loc_10198")

    label("loc_10111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1011F")
    Jump("loc_10198")

    label("loc_1011F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1012D")
    Jump("loc_10198")

    label("loc_1012D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1013B")
    Jump("loc_10198")

    label("loc_1013B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10156")
    Call(0, 33)
    Jump("loc_10198")

    label("loc_10156")

    ClearChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "(The poor character of these persons is\x01",
            "Where are you from ……! Is it? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10198")

    TalkEnd(0xFE)
    Return()

    # Function_37_FEE9 end

    def Function_38_1019C(): pass

    label("Function_38_1019C")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xE, 0x101, 0)

    ChrTalk(
        0xE,
        (
            "Oh, Lloyd.\x01",
            "It became a serious thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "At the support department\x01",
            "Did you ask something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh no, nothing …\x02\x03",
            "#00001FEven now I am still in charge of the section manager\x01",
            "I am waiting for contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I see,\x01",
            "Are we the same as the wide area crime prevention section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As soon as the meeting is concluded\x01",
            "I heard that a notice will be made ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Really, what will happen\x01",
            "There is no expectation at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Anyway now it's going on\x01",
            "Although it seems to be obligatory … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Lloyd something independently\x01",
            "You seem to be moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "What is it?\x01",
            "Not to be aware of Defense Forces\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x18F, 6)
    Return()

    # Function_38_1019C end

    def Function_39_103E9(): pass

    label("Function_39_103E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_103FA")
    Jump("loc_10A08")

    label("loc_103FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10408")
    Jump("loc_10A08")

    label("loc_10408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1053C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104C3")

    ChrTalk(
        0xFE,
        (
            "Policeman隊は半分に分けて、\x01",
            "One of the guards\x01",
            "Wait as a support person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other\x01",
            "I plan to move on touring the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it is difficult,\x01",
            "I will support each other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_10537")

    label("loc_104C3")


    ChrTalk(
        0xFE,
        (
            "Blood to the guard\x01",
            "I do not want to let it flow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not help you when I'm in pain\x01",
            "It is a story that what is police.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10537")

    Jump("loc_10A08")

    label("loc_1053C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_105D3")

    ChrTalk(
        0xFE,
        (
            "It seems to be troublesome children,\x01",
            "Relatively obediently today\x01",
            "I'm answering you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that Kate had a battle,\x01",
            "I guess it worked so well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A08")

    label("loc_105D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_105E4")
    Call(0, 40)
    Jump("loc_10A08")

    label("loc_105E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_105F2")
    Jump("loc_10A08")

    label("loc_105F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10600")
    Jump("loc_10A08")

    label("loc_10600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1060E")
    Jump("loc_10A08")

    label("loc_1060E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1067E")

    ChrTalk(
        0xFE,
        (
            "Well, the unveiling ceremony is over\x01",
            "I will finally give you a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after all\x01",
            "Pick up is limited to coffee.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A08")

    label("loc_1067E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1068C")
    Jump("loc_10A08")

    label("loc_1068C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1071C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106A7")
    Call(0, 26)
    Jump("loc_10717")

    label("loc_106A7")


    ChrTalk(
        0xFE,
        (
            "Well, that is what we call\x01",
            "I guess self-assertion is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The side suffering from annoyance\x01",
            "I did not endure it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10717")

    Jump("loc_10A08")

    label("loc_1071C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_10A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10917")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys.\x01",
            "There is also a new face, but it is a special affairs support section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Finally\x01",
            "Is that activity resumed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHmm, that kind of you\x01",
            "You are the section chief of the wide area crime prevention division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101Fあの、Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, sorry to bother you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, but quite\x01",
            "It seems that they gathered interesting talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, anyway,\x01",
            "I guess you'll expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on crossing the barriers of the division,\x01",
            "Janken you play an active part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 3)
    Jump("loc_10A08")

    label("loc_10917")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10994")

    ChrTalk(
        0x14,
        (
            "Hmm, even so\x01",
            "Nasty children came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well, Kate yourself\x01",
            "It will be okay if you leave it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A08")

    label("loc_10994")


    ChrTalk(
        0xFE,
        (
            "Well, after drinking this guy\x01",
            "I should return to the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, this place is a continuation of the meeting\x01",
            "I will bear to the body just before the retirement age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A08")

    TalkEnd(0xFE)
    Return()

    # Function_39_103E9 end

    def Function_40_10A0C(): pass

    label("Function_40_10A0C")

    OP_4B(0x14, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_4B(0x18, 0xFF)

    ChrTalk(
        0x14,
        (
            "When the train from Republic comes,\x01",
            "Also there is correspondence of transfer shipping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "From now on,\x01",
            "Toward the support of the station and the airport direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Ha ha, this is OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "We will head to the site immediately.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_4C(0x17, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_40_10A0C end

    def Function_41_10AE1(): pass

    label("Function_41_10AE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10B7F")

    ChrTalk(
        0xFE,
        (
            "Even in the wide area crime prevention section,\x01",
            "I resumed the patrol of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Great confusion to deteriorate security\x01",
            "There is also the possibility of influence.\x01",
            "You have to watch carefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C49")

    label("loc_10B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_10B8D")
    Jump("loc_10C49")

    label("loc_10B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10C3D")

    ChrTalk(
        0xFE,
        (
            "Finally restoration of headquarters finally\x01",
            "I thought it was a period of division\x01",
            "Incorporation into the Defense Forces, is … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am going now\x01",
            "It's a soldier …… frankly to fluffy\x01",
            "It is unlikely to be accepted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C49")

    label("loc_10C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10C49")
    Call(0, 40)

    label("loc_10C49")

    TalkEnd(0xFE)
    Return()

    # Function_41_10AE1 end

    def Function_42_10C4D(): pass

    label("Function_42_10C4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10CCE")

    ChrTalk(
        0xFE,
        (
            "Mr. Joe Ridgeは\x01",
            "The police school the defense army left\x01",
            "I headed for post-treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We have to defend our absence from the section manager.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10DC2")

    label("loc_10CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_10CDC")
    Jump("loc_10DC2")

    label("loc_10CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10D8C")

    ChrTalk(
        0xFE,
        (
            "Finally restoration of headquarters finally\x01",
            "I thought it was over\x01",
            "Incorporation into the Defense Forces, is … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am going now\x01",
            "It's a soldier …… frankly to fluffy\x01",
            "It is unlikely to be accepted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DC2")

    label("loc_10D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10D9A")
    Jump("loc_10DC2")

    label("loc_10D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10DA8")
    Jump("loc_10DC2")

    label("loc_10DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10DB6")
    Jump("loc_10DC2")

    label("loc_10DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_10DC2")
    Call(0, 40)

    label("loc_10DC2")

    TalkEnd(0xFE)
    Return()

    # Function_42_10C4D end

    def Function_43_10DC6(): pass

    label("Function_43_10DC6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think you have heard it already,\x01",
            "The police as an organization of the Defense Army\x01",
            "It was decided to be reorganized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Currently on the future system\x01",
            "To the responsible person in each direction in the conference room on the second floor\x01",
            "I am in a situation where I am explaining the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until you receive instructions from above,\x01",
            "Please wait at the branch building.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_10DC6 end

    def Function_44_10EC4(): pass

    label("Function_44_10EC4")

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

    def lambda_10F4F():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F4F)
    Sleep(50)

    def lambda_10F6C():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F6C)
    Sleep(50)

    def lambda_10F89():
        OP_98(0x103, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10F89)
    Sleep(50)

    def lambda_10FA6():
        OP_98(0x104, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10FA6)
    Sleep(50)
    SetCameraDistance(25000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, everyone ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x15, 0x101, 500)

    ChrTalk(
        0x15,
        "Gee\x02",
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
            "You\x01",
            "You are a member of the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think you have heard it already,\x01",
            "The police as an organization of the Defense Army\x01",
            "It was decided to be reorganized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Currently on the future system\x01",
            "To the responsible person in each direction in the conference room on the second floor\x01",
            "I am in a situation where I am explaining the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Until you receive instructions from above,\x01",
            "Please wait at the branch building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FHaha …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Although the movement within the first floor is free,\x01",
            "Please refrain from extra action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If judged to be suspicious,\x01",
            "The possibility to detain you\x01",
            "There is so, please understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FRyo, OK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F(Somehow, it is very intimidating … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F(Oh, but\x01",
            "It sounds like it will not go wrong. )\x02",
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

    # Function_44_10EC4 end

    def Function_45_1132D(): pass

    label("Function_45_1132D")

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
            "And ──\x01",
            "The leaders of each country entered the crossbell,\x01",
            "The day before the Orkis Tower is released.\x02\x03",
            "At the police headquarters countermeeting meeting place\x01",
            "Members of the support department were called.\x07\x00\x02",
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
            "Three days from tomorrow\x01",
            "It will be a security system of the trade council.\x02\x03",
            "Belgard, Tangram main gate and\x01",
            "Near the border it is already by the guard\x01",
            "A checking system is laid.\x02\x03",
            "Regarding the city, ──\x01",
            "Mr. Joe Ridge、Donovan。\x02",
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
            "#5PAh, the wide area crime prevention section gathers all the members\x01",
            "It is in a state I am hitting in the city patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PIt is full operation until the conference ends.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#5PThe second section is a station, airport, commercial area\x01",
            "I am particularly wary of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAgain until the end of the meeting\x01",
            "It is going to be hit by all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FThe security countermeasure headquarters\x01",
            "It is the situation that we are managing in the investigation department.\x02\x03",
            "#00600FAs far as possible emergency\x01",
            "I am proud that we can respond … …\x02",
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
            "#12P#01003F…… No matter how strict the security system is\x01",
            "It can never be perfect.\x02\x03",
            "#01000FSo support department#6RUchi#That is why it comes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00604FYeah, as you reported\x01",
            "Sergey Managerには渉外担当として\x01",
            "We will fill in the headquarters.\x02\x03",
            "#00602FAlso contact with the guard area\x01",
            "If you manage it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#12P#01006FWhew, human use was rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHaha, anyway in various places\x01",
            "I'm stuck in my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIn a way that pierced the blind spot\x01",
            "Establish a favorable investigation system … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5PWow.\x01",
            "\"搦#2RFrom#Sergei 's hand\x01",
            "It is said that the face is exciting.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0x0)
    Sleep(300)

    ChrTalk(
        0x19,
        "#12P#01005FPlease do not tell me, old story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002F\"搦#2RFrom#Are you Sergei '?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHehu ……\x01",
            "It is how it is called a process.\x02",
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
            "#12P#01000FSo …\x01",
            "Is not it good for Koitsu and others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FWell, I do not mind.\x02\x03",
            "#00600FFor them for a while as a military\x01",
            "I think I will move it.\x02",
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
        "#10105FWhat is a military force ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FWhile conducting ordinary support activities\x01",
            "If there is something backed up\x01",
            "Does it make it turnable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00606FOh, that's right.\x02\x03",
            "It is the same stance as the Association\x01",
            "It can not be relied upon by them.\x02\x03",
            "#00601Fin addition……\x01",
            "Such people#10R噵 噵 噵 噵 噵#Since it came in,\x01",
            "I want insurance for unexpected situations.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x1)

    ChrTalk(
        0x102,
        "#6P#00108FSuch guys …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F─ ─ It is \"Red constellation\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#00601FAh……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "#00603FHunting Corps \"Red constellation\" … ….\x02\x03",
            "In the western part of the continental continent\x01",
            "It is one of the best hunting corps.\x02\x03",
            "#00601FCurrently, many belonging members\x01",
            "Being in the crossbell\x01",
            "It has been confirmed.\x02\x03",
            "By the way, about a year ago,\x01",
            "That \"black moon#4RHayuue#In the direction of the Republic\x01",
            "It seems to have caused a large-scale conflict.\x02",
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
        "#5PHmmm, they are idolatry people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWhat is that, in this town with black moon\x01",
            "Are you going to continue the conflict?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FNo, basically the hunting soldiers\x01",
            "They are people who move by Mira.\x02\x03",
            "Although I was fighting in the past,\x01",
            "It is not a reason to fight again.\x02\x03",
            "#00600FThat's true, Orlando?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F─ ─ Well.\x02\x03",
            "#00303FUnlike the mafia that emphasizes territory\x01",
            "Mira and the battlefield are all in the hunting corps.\x02\x03",
            "The enemy of yesterday is the ally of today …\x01",
            "The reverse can also be found in everyday situations.\x02\x03",
            "#00300FIn that sense, the previous conflict\x01",
            "I guess it is not pulling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10304FHuff, then\x01",
            "Is there a mystery emerging?\x02\x03",
            "#10302FWhy \"red constellation\"\x01",
            "I wonder if I entered the crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11P#00606FI am exploring even one section\x01",
            "Its purpose has not been found out yet.\x02\x03",
            "#00601FJust to support the Imperial Government\x01",
            "It seems to be definitely received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FIn relation to the trade meeting\x01",
            "I am trying to do something ……\x02\x03",
            "#00101FOr of the Republic \"Black Moon\"\x01",
            "Are you aiming to keep the rise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#12P#01006FWell, it could be both.\x02\x03",
            "#01000FEither way, at a trade meeting\x01",
            "It is not an element that can be ignored\x01",
            "I do not think he will make a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P#00603FYes, of course.\x02\x03",
            "#00600F── By the way, \"red constellation\"\x01",
            "Also around the city of Crosbell\x01",
            "It seems that he has extended his legs several times.\x02\x03",
            "If you can go around the places\x01",
            "Please also look for trends around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F── I understand.\x02\x03",
            "#00001FIn response to the request for assistance,\x01",
            "We will collect information on \"Red constellation\".\x02",
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
            "#6P#00100FIf there is something\x01",
            "I will go to support each direction\x01",
            "Please contact me at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POh, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5PDo not hesitate to rely on me ~.\x02",
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

    # Function_45_1132D end

    def Function_46_127E0(): pass

    label("Function_46_127E0")

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

    def lambda_12863():
        OP_98(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12863)
    Sleep(50)

    def lambda_12880():
        OP_98(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12880)
    Sleep(50)

    def lambda_1289D():
        OP_98(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1289D)
    Sleep(50)

    def lambda_128BA():
        OP_98(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_128BA)
    Sleep(50)
    SetCameraDistance(20430, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Well, everyone.\x02",
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
        "#5P#01902FOh, everyone, Onee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FAlready, my sister in the workplace\x01",
            "Did not I say that it was useless?\x02",
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

    def lambda_12A24():
        OP_98(0x101, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A24)
    Sleep(50)

    def lambda_12A41():
        OP_98(0x102, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12A41)
    Sleep(50)

    def lambda_12A5E():
        OP_98(0x109, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12A5E)
    Sleep(50)

    def lambda_12A7B():
        OP_98(0x105, 0x0, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12A7B)
    Sleep(50)
    TurnDirection(0x9, 0x101, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#12P#00002FMr. Rebecca.\x01",
            "Good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FI was out of time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uhufu.\x01",
            "The mission support section, it is a restart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Immediately request assistance\x01",
            "始めてAre you coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, there are new members,\x01",
            "While turning around the city.\x02\x03",
            "I received a request from section 1\x01",
            "Where is Emma?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I will be waiting at the meeting room there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would like to request cooperation from section 1\x01",
            "You guys also got a lot of success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "ふふ、Something is deep emotional.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00012FNo, such a thing ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuff, impossible hardships\x01",
            "I hope not to be pressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FAlready, Wajima ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAnd anyway from Emma\x01",
            "Let's listen to the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#01909FPlease do your best~.\x02",
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

    # Function_46_127E0 end

    def Function_47_12D62(): pass

    label("Function_47_12D62")

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
            "Did you come …?\x01",
            "Bannings investigator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FWell, emma.\x01",
            "That passage became indebted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If it is about training at the first section\x01",
            "I have no intention of taking care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "To the last, Ms. Dudley\x01",
            "I just followed the instructions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The line is not bad, but …\x01",
            "Kicking the invitation to the first division to the support department\x01",
            "It is painful to understand that I returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FWell, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105F(It sounds like there were various … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100F(Certainly if it was Mr. Lloyd\x01",
            "It seems that other departments are also wanting. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh well.\x01",
            "Quickly, I will get into the main subject.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That I came here\x01",
            "If you can help me\x01",
            "Is it okay to think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes, of course.\x02\x03",
            "#00001F……anything,\x01",
            "That Rector Arend Doll\x01",
            "Do you mean you are entering a crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I am grasping it in the first lesson.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "… but, unfortunately\x01",
            "I have not decided yet.\x02",
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
        "#12P#00005FWhat does that mean …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FI can not confirm the location\x01",
            "Is it that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the first place you entered the crossbell\x01",
            "It is uncertain information to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "There is sighting information like that … …\x01",
            "However, when trying to pursue a footstep\x01",
            "It blurs like a hot fire … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Perhaps, sense this movement\x01",
            "I think that it is escaping trapping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013F……I see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FAnd, it is an outrageous person.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, if that older brother\x01",
            "That seems to be that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So to you\x01",
            "Lecta · Arend d'Or\x01",
            "I would like you to confirm the fact of stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Is he really entering the crossbell,\x01",
            "Or is it some kind of camouflage information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "If possible, the imperial officers,\x01",
            "Or as a clerk of the Imperial Government\x01",
            "I also would like to ask for identity confirmation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F……I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FBut why to us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "以前、You\x01",
            "I have contacted him a couple of times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I decided to bet on that.\x02",
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
        "#12P#00012FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FApart from Huff and Elite\x01",
            "It is a surprisingly flexible response, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Kogu … It can not be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Capturing is possible if you give manpower\x01",
            "If you do not do it well, it will be a diplomatic problem,\x01",
            "I have other cases as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "… … When Mr. Dudley arrives\x01",
            "Even though you did not ask you.\x02",
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
            "#12P#00005Fby the way……\x01",
            "Where is Mr. Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yesterday evening,\x01",
            "At a meeting of security at the trade council\x01",
            "I headed towards River.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I think that it will return tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYou look to be busy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "So, before he comes back\x01",
            "I would like to keep it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "No matter how tired from business trip\x01",
            "Because it is a person who underwrites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FCertainly Dudley's\x01",
            "That seems to work …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI understand.\x01",
            "I will underwrite it.\x02\x03",
            "#00000FTentatively …\x01",
            "Captain Rector in what area\x01",
            "Do you know what was witnessed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I agree……\x01",
            "True or false is not certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "In the vicinity of \"back street\"\x01",
            "I have information that I saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FAlleys …\x01",
            "Is it near the old Rubache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302FHuh, it looks like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FI understand.\x01",
            "I will start investigating quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I kindly request you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Because I am waiting in one department\x01",
            "Please call at reception at the time of reporting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Then, I will excuse you.\x02",
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_13AC2():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13AC2)

    def lambda_13ACF():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13ACF)

    def lambda_13ADC():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13ADC)

    def lambda_13AE9():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13AE9)
    OP_68(-57500, 1500, 16430, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_13B3B():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13B3B)

    def lambda_13B48():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13B48)

    def lambda_13B55():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13B55)

    def lambda_13B62():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13B62)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#11P#00006FFuu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FFor a long time in one department training\x01",
            "You seem to have been indebted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, the attitude is severe\x01",
            "They taught me carefully and carefully.\x02\x03",
            "#00004FWhat is it …?\x01",
            "I think that it is a serious person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FHuh, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, as much as that older sister\x01",
            "Though I am seeking healing.\x02\x03",
            "#10302FHuh, around this evening\x01",
            "Let's invite even if you drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYou know.\x02\x03",
            "#00000FAnyway hit it\x01",
            "Let's search for Lecter.\x02\x03",
            "First off from the back street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FYeah, let's go.\x02",
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
            "Quest 【Identification of Empire Clerk】\x07\x00",
            "I started!\x02",
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

    # Function_47_12D62 end

    def Function_48_13DFA(): pass

    label("Function_48_13DFA")

    Sleep(2500)
    Sound(103, 0, 100, 0)
    Sleep(400)
    Sound(104, 0, 100, 0)
    Return()

    # Function_48_13DFA end

    def Function_49_13E0D(): pass

    label("Function_49_13E0D")

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
            "── It was a hard time.\x01",
            "You seem to have grasped variously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes, certainly nothing\x01",
            "Until it is human being of information station\x01",
            "I did not think that I would admit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "…… In a place known here,\x01",
            "It is said that intelligence activities are not limited\x01",
            "You have confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "However, as a result of this,\x01",
            "I could roughly grasp it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "More than expected results\x01",
            "You seem to have raised it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002Fmy mother……\x01",
            "If you say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, someone stretched out my body\x01",
            "It is worthwhile to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00113FI am not stretched!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But that was accompanied\x01",
            "I also care about a girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Luther Captain's intelligence relations\x01",
            "Did you feel like a subordinate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… No, I think it's different.\x02\x03",
            "#00008FIt is too young for intelligence officials,\x01",
            "It is too innocent.\x02\x03",
            "#00001FHowever, even for ordinary civilians\x01",
            "I could not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101F……I agree.\x01",
            "My body was quick as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "─ ─ All right.\x01",
            "As for that girl, even one department person\x01",
            "Let's grasp the trend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I am with this.\x01",
            "Thank you for your help this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002Fいえ、If there is something again\x01",
            "Please do not hesitate to contact me.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xD, -58480, 0, 18800, 2000, 0x0)
    OP_95(0xD, -58480, 0, 15540, 2000, 0x0)

    def lambda_142ED():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_142ED)

    def lambda_142FA():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_142FA)

    def lambda_14307():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14307)

    def lambda_14314():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14314)
    OP_68(-57300, 1500, 16880, 1500)
    BeginChrThread(0x22, 1, 0, 48)
    OP_95(0xD, -60490, 0, 13540, 2000, 0x0)
    OP_95(0xD, -64970, 0, 12740, 2000, 0x0)
    OP_0D()
    SetChrFlags(0xD, 0x80)

    def lambda_14366():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14366)

    def lambda_14373():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14373)

    def lambda_14380():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14380)

    def lambda_1438D():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1438D)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#00006FFuu …\x01",
            "Have you managed to meet expectations somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F… … Haha, well … …\x02\x03",
            "#00108FAnyway, that girl ….\x01",
            "Who really is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI agree……\x01",
            "Although it was deceived by Nori\x01",
            "I do not think that it is an ordinary traveler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAccompany the information officers in the major powers\x01",
            "Innocent and unrestrained girl ……\x02\x03",
            "#10304FHuh, it is quite interesting.\x02",
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
            "Quest 【Identification of Empire Clerk】\x07\x00",
            "Achieved!\x02",
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

    # Function_49_13E0D end

    def Function_50_14568(): pass

    label("Function_50_14568")

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

    def lambda_145FB():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_145FB)
    Sleep(50)

    def lambda_14618():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14618)
    Sleep(50)

    def lambda_14635():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14635)
    Sleep(50)

    def lambda_14652():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14652)
    Sleep(300)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x8,
        (
            "Ah … everyone in the support department,\x01",
            "You seem to have finished your work.\x02",
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

    def lambda_14721():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14721)
    Sleep(50)

    def lambda_1473E():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1473E)
    Sleep(50)

    def lambda_1475B():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1475B)
    Sleep(50)

    def lambda_14778():
        OP_97(0xFE, 0x3E8, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14778)
    WaitChrThread(0x101, 1)

    def lambda_14796():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14796)
    WaitChrThread(0x109, 1)

    def lambda_147A7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_147A7)
    WaitChrThread(0x102, 1)

    def lambda_147B8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_147B8)
    WaitChrThread(0x105, 1)

    def lambda_147C9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_147C9)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah, I just got it\x01",
            "I finished the report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuff, for now\x01",
            "It is a place where I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, thanks for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the support department restarted in the future\x01",
            "I think whether there will be plenty of requests,\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FThank you,\x01",
            "Rebecca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FAs a new member\x01",
            "It is still immature yet ……\x01",
            "I want to work hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "By the way, everyone.\x01",
            "Do you use a new fight notebook?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When Mr. Lloyd gave a training at the department,\x01",
            "It should have been received ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, that's right ……\x01",
            "Yes, I will use it.\x02\x03",
            "#00004FWhen the notebook information increases,\x01",
            "If you report to Rebecca\x01",
            "Was it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, that will be helpful if you do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "特に最近は、Also report on the new demon\x01",
            "There is a tendency to increase … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For understanding the actual condition of them and for safety measures\x01",
            "I want as much information as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As before, step by step\x01",
            "Because some allowance will be paid,\x01",
            "どうかThank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FTo a certain extent, regularly\x01",
            "It seems better to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, I will be waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And … one more thing\x01",
            "I have to inform everyone\x01",
            "There is something that is not going to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We found out when you were a cult incident\x01",
            "It is the data of the terminal … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can finally analyze the other day\x01",
            "It seems that the possibility has come into view.\x02",
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
        "#12P#00105FIs it true? Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_14D30():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14D30)
    Sleep(50)

    def lambda_14D40():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14D40)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10305FHmm, what are you talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_14D72():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D72)
    Sleep(50)

    def lambda_14D82():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14D82)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00003F…… At the time of that cult's case,\x01",
            "From the terminal that was in \"Fort of the Sun\"\x01",
            "I got some data.\x02\x03",
            "About the \"D∴G organization\"\x01",
            "Joachim Günter himself\x01",
            "The data that seems to have said it is.\x02\x03",
            "#00008FA part of the sentence was intentionally erased\x01",
            "Because it was impossible to decipher,\x01",
            "I was using it for discrimination ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00001FPerhaps you can erase sentences\x01",
            "Did you recover?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14EEA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14EEA)
    Sleep(50)

    def lambda_14EFA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14EFA)
    Sleep(50)

    def lambda_14F0A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_14F0A)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "No, according to the discrimination section\x01",
            "It is said that it is still promising\x01",
            "It looks like a stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Memory crystal#8RMemory Quartz#Inside\x01",
            "The broken piece of damaged data\x01",
            "It is said that it existed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To fully analyze\x01",
            "It takes a lot of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FIs that so……\x02\x03",
            "#10108FThe unclear part of that incident\x01",
            "I will finally understand\x01",
            "I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… I just have to wait for the path so far\x01",
            "It may not be there.\x02\x03",
            "#00000FRebecca-san, let me know\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once, please tell\x01",
            "You can always store data on the terminal\x01",
            "Please check it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is progress in the analysis\x01",
            "I will inform you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100Fええ、Thank you.\x02",
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

    # Function_50_14568 end

    def Function_51_151EE(): pass

    label("Function_51_151EE")

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
            "Well then, I will get the record again\x01",
            "I wonder if you can answer the question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Um, what is your name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Nanashino Gombe. (Hosi Hoshi)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "John Smith. (Bolivoli)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Hun, you guys like you\x01",
            "Do you have obligation to answer?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "Oh, you guys! It is!\x01",
            "I can not stop playing … ….!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Mama, Franz.\x01",
            "I will calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Put, it is being warned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Dassey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Well, this is why ordinary people … …\x02",
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
            "#10101F…… They are given to them,\x01",
            "Is it only a fine penalty! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "…… I'm sorry though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Indeed autonomous state law,\x01",
            "Every rule on transportation\x01",
            "The minimum is maintained though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As they are republics,\x01",
            "I can not regulate rigidly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Today I will be strictly careful,\x01",
            "It will be released soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FAre you after all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHmm, somehow\x01",
            "You seem to have predicted?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1570A():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1570A)
    Sleep(50)

    def lambda_1571A():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1571A)
    Sleep(100)

    ChrTalk(
        0x102,
        (
            "#00108F…… Even before,\x01",
            "There was a similar thing.\x02\x03",
            "In the case of a fake brand trader,\x01",
            "Strict attention and one month\x01",
            "It was only an order to withdraw from autonomous province.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106Fby the way……\x01",
            "There was also such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F… … My uncle became a new mayor,\x01",
            "Movement to review autonomous state law also\x01",
            "I'm getting increasing, but ….\x02\x03",
            "Still the part that I can not reach yet\x01",
            "It is the current situation that there are many.\x02\x03",
            "#00101FNot being able to give out to foreigners strongly,\x01",
            "Crossbell has been holding for many years\x01",
            "It can be said to be one of \"distortion\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, fuck ……\x02\x03",
            "Well then, this time\x01",
            "To saying that it was a broken bone\x01",
            "Is it going to be?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00004F…… No, that's not it.\x02\x03",
            "#00000FSeveral times until now\x01",
            "There was a similar thing,\x01",
            "None of them was in vain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Of course this time,\x01",
            "I do not think it's useless.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_159F9():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_159F9)
    Sleep(50)

    def lambda_15A09():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A09)
    Sleep(100)

    ChrTalk(
        0xE,
        (
            "At least, no more today\x01",
            "Runaway vehicles never run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… Everywhere from now on\x01",
            "I think I will face such a wall.\x02\x03",
            "#00000FThat's why,\x01",
            "I will confront without giving up\x01",
            "I think that is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FI agree……\x01",
            "I have to work hard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FWell then, at best I am\x01",
            "Let me run cool\x01",
            "I should do it.\x02\x03",
            "#10302FYou guys are getting too hot\x01",
            "Do not let it run away.\x02",
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
            "#00106FWajima kunio ……\x01",
            "Even though I'm getting together\x01",
            "I will not water it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F… Well, oh well.\x02\x03",
            "#00000FWell then, Kate-senpai …\x01",
            "Can I leave it to the rest, is not it?\x02",
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
            "I was really saved today.\x01",
            "If there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes, I will be waiting.\x02",
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
            "Quest 【Crackdown on Runaway Car】\x07\x00",
            "Achieved!\x02",
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

    # Function_51_151EE end

    def Function_52_15DCB(): pass

    label("Function_52_15DCB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1681C")
    OP_0D()

    ChrTalk(
        0x10,
        (
            "Oh, Margaret ……\x01",
            "Why is this so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I can not get caught up with such a man\x01",
            "It does not seem like me … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "と、Anyways,\x01",
            "Before irrevocable\x01",
            "I have to manage somehow ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Director Pierre … ….\x01",
            "It is rare, in such a place. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F(It seems I am suffering something … …)\x02",
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
            "Kimi, you guys …\x01",
            "Since when have you been there! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, maybe I will tell you my monologue\x01",
            "I guess it was not heard! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FNo……\x01",
            "I have not heard it in detail though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FHow about Margaret,\x01",
            "Like being caught by such a man,\x01",
            "I heard it in part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Giggle\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuff, deputy director of warrant\x01",
            "Is that your hostess' name?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "Hi, what is wrong with people\x01",
            "Do not say it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Margaret is …\x01",
            "It's my wife's name! It is!\x02",
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
        "#10105FWaah, what about a wife …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs it about his wife?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "That's it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "…… Well, I lost the ring before,\x01",
            "After missing the position of the next Director\x01",
            "I got treated to be even more dangerous … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "…… Why did I do this?\x01",
            "You must speak frankly! Is it?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16478")
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
            "#1K◆ The first part \"Ring search quest\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",          # 0
            "【I am clearing】\x01",      # 1
            "【other than that】\x01",            # 2
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
        (0, "loc_1645F"),
        (1, "loc_16464"),
        (2, "loc_1646E"),
        (SWITCH_DEFAULT, "loc_16478"),
    )


    label("loc_1645F")

    Jump("loc_16478")

    label("loc_16464")

    OP_29(0x15, 0x4, 0x10)
    Jump("loc_16478")

    label("loc_1646E")

    OP_29(0x15, 0x3, 0x10)
    Jump("loc_16478")

    label("loc_16478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16509")

    ChrTalk(
        0x101,
        (
            "#00003FBy the way, deputy director … …\x01",
            "It was famous for a godfather. )\x02\x03",
            "#00008F(That is, now the Deputy Director\x01",
            "Is it also related to being troubled … …)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1657B")

    label("loc_16509")


    ChrTalk(
        0x101,
        (
            "#00003F(Deputy Director-General ……\x01",
            "It looks like a goddamn. )\x02\x03",
            "#00008F(That is, now the Deputy Director\x01",
            "Is it also related to being troubled … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1657B")


    ChrTalk(
        0x10,
        (
            "…… Eee, there is no choice.\x01",
            "In this case, you can not change your belly on your back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Managers of the Special Affairs Support Division!\x01",
            "Give you a secret mission! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FConfidential mission …?\x01",
            "What does that mean … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, yeah, well speaking … …\x01",
            "I would like to ask my wife's surroundings investigation.\x02",
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
        "#00305FThen, what about surroundings search …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FThe private operation of the department\x01",
            "I am contrary to the police's job rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "In this case, fine details do not matter!\x01",
            "I am also cluttered!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Whatever, to you guys\x01",
            "You can process it in the form of a request!\x01",
            "How about then! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, hmm … ….\x01",
            "(What should I do?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168B9")

    label("loc_1681C")

    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "Managers of the Special Affairs Support Division!\x01",
            "I want to give top secret tasks to you! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Whatever, to you guys\x01",
            "You can process it in the form of a request!\x01",
            "Would you please accept it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168B9")

    Call(0, 53)
    OP_4C(0x10, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12540, 0, 14410, 0)
    EventEnd(0x5)
    Return()

    # Function_52_15DCB end

    def Function_53_168D8(): pass

    label("Function_53_168D8")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【undertake】\x01",      # 0
            "【quit】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16936")
    Call(0, 54)
    Jump("loc_16A25")

    label("loc_16936")


    ChrTalk(
        0x101,
        (
            "#00006FExcuse me……\x01",
            "We also had a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Well, that's it … no use.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Then, instantly tidy up\x01",
            "To come back here!\x01",
            "……How nice! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FI will do my best.\x02",
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

    label("loc_16A25")

    Return()

    # Function_53_168D8 end

    def Function_54_16A26(): pass

    label("Function_54_16A26")


    ChrTalk(
        0x101,
        (
            "#00001FI understand.\x01",
            "Apparently it seems like you have problems … …\x01",
            "I will tell you about the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Huh …… Really? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "OK, if you do not\x01",
            "I do not want to talk here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Please come to the Deputy Director General Office.\x01",
            "Let's talk about it in detail!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_54_16A26 end

    def Function_55_16B23(): pass

    label("Function_55_16B23")

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
            "#00306FWhew.\x01",
            "In the end I decided to accept\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FWell, deputy director also wife\x01",
            "I wonder she is … ….\x02\x03",
            "Until you know the truth\x01",
            "Even if you go out with a drink\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FWell, it can not be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell then, at first\x01",
            "Where do you examine it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FFirst of all, in the central square\x01",
            "Let's go to a restaurant.\x02\x03",
            "People who are like hosts and wife of deputy director\x01",
            "It seems that I have met her recently,\x01",
            "You may be able to hear a direct talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, so\x01",
            "I guess it's OK.\x02\x03",
            "#10309FWell then, immediately\x01",
            "Let's go and let me know\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Somehow I am enjoying … ….)\x02",
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
            "Quest 【Request of deputy director】\x07\x00",
            "I started!\x02",
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

    # Function_55_16B23 end

    def Function_56_16EA1(): pass

    label("Function_56_16EA1")

    EventBegin(0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_16EF6")

    ChrTalk(
        0x101,
        (
            "#00000F…… There is no business on the upper floor.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FD2")

    label("loc_16EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16F90")
    OP_4B(0x16, 0xFF)
    TurnDirection(0x16, 0x0, 500)

    ChrTalk(
        0x16,
        (
            "Now the elevator is\x01",
            "We are prohibited from using it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Everyone, in the first floor conference room\x01",
            "Please wait for instructions.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0xB4, 0x0)
    OP_4C(0x16, 0xFF)
    Jump("loc_16FD2")

    label("loc_16F90")


    ChrTalk(
        0x101,
        (
            "#00000F…… There is no business on the upper floor.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FD2")

    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_56_16EA1 end

    def Function_57_16FE6(): pass

    label("Function_57_16FE6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_57_16FE6 end

    SaveToFile()

Try(main)
