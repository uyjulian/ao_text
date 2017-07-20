from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r2000.bin",                # FileName
        "r2000",                    # MapName
        "r2000",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2000", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x11,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 1, 0, 2],
    )

    BuildStringList((
        "r2000",                  # 0
        "bus",                   # 1
        "Sister · Lease",       # 2
        "car",                     # 3
        "Steel Drew",           # 4
        "SE control",                 # 5
        "br2000",                 # 6
        "Cross Bell City",       # 7
        "Cross Bell Cathedral direction",   # 8
        "Mine town mining to Mainz",     # 9
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch76050.itc",               # 10
        "monster/ch76051.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294945217, 4294965296, 42080,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 19,  14.149999618530273,    30.399999618530273,    -1.0,                  729.0,                 [0.288675457239151,    -0.027777668088674545, 0.0,                   0.0,                   0.16666600108146667,   0.04811257869005203,   -0.0,                  0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   0.0,                   -9.15140438079834,     -1.069568395614624,    0.19999998807907104,   1.0])

    DeclActor(11200,   0,       16200,   1500,    11200,   1500,    16200,   0x007C, 0,  9,  0x0000)
    DeclActor(870,     0,       19400,   1500,    4294967206, 2000,    19400,   0x007C, 0,  8,  0x0000)
    DeclActor(4294966176, 0,       19360,   1500,    4294966176, 2000,    19360,   0x007C, 0,  8,  0x0000)
    DeclActor(4200,    0,       36290,   2500,    4200,    1700,    36290,   0x007C, 0,  26, 0x0000)

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "Cross Bell City")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "Cross Bell Cathedral direction")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "Mine town mining to Mainz")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")

    ChipFrameInfo(1096, 0)                                       # 0

    ScpFunction((
        "Function_0_448",          # 00, 0
        "Function_1_467",          # 01, 1
        "Function_2_F9D",          # 02, 2
        "Function_3_126B",         # 03, 3
        "Function_4_126F",         # 04, 4
        "Function_5_1450",         # 05, 5
        "Function_6_1584",         # 06, 6
        "Function_7_15D5",         # 07, 7
        "Function_8_1669",         # 08, 8
        "Function_9_1A1E",         # 09, 9
        "Function_10_1BF4",        # 0A, 10
        "Function_11_1D40",        # 0B, 11
        "Function_12_322E",        # 0C, 12
        "Function_13_32BE",        # 0D, 13
        "Function_14_32EF",        # 0E, 14
        "Function_15_3320",        # 0F, 15
        "Function_16_3351",        # 10, 16
        "Function_17_3382",        # 11, 17
        "Function_18_33B2",        # 12, 18
        "Function_19_33D7",        # 13, 19
        "Function_20_3C8D",        # 14, 20
        "Function_21_3D42",        # 15, 21
        "Function_22_40C2",        # 16, 22
        "Function_23_4369",        # 17, 23
        "Function_24_4A3C",        # 18, 24
        "Function_25_4D64",        # 19, 25
        "Function_26_4DBA",        # 1A, 26
    ))


    def Function_0_448(): pass

    label("Function_0_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_466")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_448")

    label("loc_466")

    Return()

    # Function_0_448 end

    def Function_1_467(): pass

    label("Function_1_467")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_4A5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A5")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 2)

    label("loc_4A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_949")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_532")
    SetScenarioFlags(0x38, 0)

    label("loc_532")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548")
    SetScenarioFlags(0x38, 1)

    label("loc_548")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E")
    SetScenarioFlags(0x38, 2)

    label("loc_55E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574")
    SetScenarioFlags(0x38, 3)

    label("loc_574")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    SetScenarioFlags(0x38, 4)

    label("loc_58A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A0")
    SetScenarioFlags(0x38, 5)

    label("loc_5A0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B6")
    SetScenarioFlags(0x38, 6)

    label("loc_5B6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    SetScenarioFlags(0x38, 7)

    label("loc_5CC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2")
    SetScenarioFlags(0x39, 0)

    label("loc_5E2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    SetScenarioFlags(0x39, 1)

    label("loc_5F8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E")
    SetScenarioFlags(0x39, 2)

    label("loc_60E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624")
    SetScenarioFlags(0x39, 3)

    label("loc_624")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63A")
    SetScenarioFlags(0x39, 4)

    label("loc_63A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_650")
    SetScenarioFlags(0x39, 5)

    label("loc_650")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_666")
    SetScenarioFlags(0x39, 6)

    label("loc_666")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C")
    SetScenarioFlags(0x39, 7)

    label("loc_67C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692")
    SetScenarioFlags(0x3A, 0)

    label("loc_692")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8")
    SetScenarioFlags(0x3A, 1)

    label("loc_6A8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    SetScenarioFlags(0x3A, 2)

    label("loc_6BE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D4")
    SetScenarioFlags(0x3A, 3)

    label("loc_6D4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA")
    SetScenarioFlags(0x3A, 4)

    label("loc_6EA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700")
    SetScenarioFlags(0x3A, 5)

    label("loc_700")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")
    SetScenarioFlags(0x3A, 6)

    label("loc_716")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    SetScenarioFlags(0x3A, 7)

    label("loc_72C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_742")
    SetScenarioFlags(0x3B, 0)

    label("loc_742")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_758")
    SetScenarioFlags(0x3B, 1)

    label("loc_758")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76E")
    SetScenarioFlags(0x3B, 2)

    label("loc_76E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_784")
    SetScenarioFlags(0x3B, 3)

    label("loc_784")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A")
    SetScenarioFlags(0x3B, 4)

    label("loc_79A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B0")
    SetScenarioFlags(0x3B, 5)

    label("loc_7B0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C6")
    SetScenarioFlags(0x3B, 6)

    label("loc_7C6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC")
    SetScenarioFlags(0x3B, 7)

    label("loc_7DC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F2")
    SetScenarioFlags(0x3D, 5)

    label("loc_7F2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    SetScenarioFlags(0x3D, 6)

    label("loc_808")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    SetScenarioFlags(0x3D, 7)

    label("loc_81E")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_949")

    label("loc_859")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_949")

    label("loc_87C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_949")

    label("loc_89F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_949")

    label("loc_8C2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_949")

    label("loc_8E5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_949")

    label("loc_908")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_949")

    label("loc_92B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_949")
    SetScenarioFlags(0x3C, 7)

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95F")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_991")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    SetChrPos(0x0, 1950, 0, 20570, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 7)

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_9C4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C4")
    SetChrPos(0x0, -1120, 0, 19360, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_9C4")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_A83")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 6)

    label("loc_A83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F39")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B22")
    SetScenarioFlags(0x38, 0)

    label("loc_B22")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B38")
    SetScenarioFlags(0x38, 1)

    label("loc_B38")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4E")
    SetScenarioFlags(0x38, 2)

    label("loc_B4E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B64")
    SetScenarioFlags(0x38, 3)

    label("loc_B64")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7A")
    SetScenarioFlags(0x38, 4)

    label("loc_B7A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B90")
    SetScenarioFlags(0x38, 5)

    label("loc_B90")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    SetScenarioFlags(0x38, 6)

    label("loc_BA6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC")
    SetScenarioFlags(0x38, 7)

    label("loc_BBC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD2")
    SetScenarioFlags(0x39, 0)

    label("loc_BD2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE8")
    SetScenarioFlags(0x39, 1)

    label("loc_BE8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE")
    SetScenarioFlags(0x39, 2)

    label("loc_BFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C14")
    SetScenarioFlags(0x39, 3)

    label("loc_C14")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2A")
    SetScenarioFlags(0x39, 4)

    label("loc_C2A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C40")
    SetScenarioFlags(0x39, 5)

    label("loc_C40")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C56")
    SetScenarioFlags(0x39, 6)

    label("loc_C56")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6C")
    SetScenarioFlags(0x39, 7)

    label("loc_C6C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C82")
    SetScenarioFlags(0x3A, 0)

    label("loc_C82")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")
    SetScenarioFlags(0x3A, 1)

    label("loc_C98")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAE")
    SetScenarioFlags(0x3A, 2)

    label("loc_CAE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC4")
    SetScenarioFlags(0x3A, 3)

    label("loc_CC4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA")
    SetScenarioFlags(0x3A, 4)

    label("loc_CDA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF0")
    SetScenarioFlags(0x3A, 5)

    label("loc_CF0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D06")
    SetScenarioFlags(0x3A, 6)

    label("loc_D06")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1C")
    SetScenarioFlags(0x3A, 7)

    label("loc_D1C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")
    SetScenarioFlags(0x3B, 0)

    label("loc_D32")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D48")
    SetScenarioFlags(0x3B, 1)

    label("loc_D48")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E")
    SetScenarioFlags(0x3B, 2)

    label("loc_D5E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D74")
    SetScenarioFlags(0x3B, 3)

    label("loc_D74")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8A")
    SetScenarioFlags(0x3B, 4)

    label("loc_D8A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA0")
    SetScenarioFlags(0x3B, 5)

    label("loc_DA0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB6")
    SetScenarioFlags(0x3B, 6)

    label("loc_DB6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")
    SetScenarioFlags(0x3B, 7)

    label("loc_DCC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    SetScenarioFlags(0x3D, 5)

    label("loc_DE2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF8")
    SetScenarioFlags(0x3D, 6)

    label("loc_DF8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0E")
    SetScenarioFlags(0x3D, 7)

    label("loc_E0E")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E49")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_F39")

    label("loc_E49")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_F39")

    label("loc_E6C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_F39")

    label("loc_E8F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_F39")

    label("loc_EB2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_F39")

    label("loc_ED5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF8")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_F39")

    label("loc_EF8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_F39")

    label("loc_F1B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F39")
    SetScenarioFlags(0x3C, 7)

    label("loc_F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F4D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)
    Jump("loc_F70")

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F5E")
    ClearScenarioFlags(0x22, 1)
    Jump("loc_F70")

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F70")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 23)

    label("loc_F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9C")
    SetMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")
    Event(0, 22)
    Jump("loc_F9C")

    label("loc_F99")

    Event(0, 21)

    label("loc_F9C")

    Return()

    # Function_1_467 end

    def Function_2_F9D(): pass

    label("Function_2_F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FB7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_FC9")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_FC9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE8")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)

    label("loc_FE8")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1096")
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    SetChrPos(0xA, -1090, 0, 19490, 350)
    OP_D5(0xA, 0x0, 0x55730, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)

    label("loc_1096")

    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_10B9")

    OP_10(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D3")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x1)

    label("loc_10D3")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EB")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_10EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FE")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_10FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1111")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1124")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1137")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_1137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114A")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115D")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_115D")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0x3, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1216")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_125E")
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    Jump("loc_126A")

    label("loc_125E")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)

    label("loc_126A")

    Return()

    # Function_2_F9D end

    def Function_3_126B(): pass

    label("Function_3_126B")

    Call(1, 6)
    Return()

    # Function_3_126B end

    def Function_4_126F(): pass

    label("Function_4_126F")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Examining the sign at the bus stop,\x01",
            "You can ride the power bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As with a powered car,\x01",
            "Please use it to move to various places.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_1336")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Do you want to move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Mine town mining town\x01",              # 0
            "Stop (near the puppet room)\x01",      # 1
            "quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E9")
    SetScenarioFlags(0x22, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_13F2")

    label("loc_13E9")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_13F2")

    Jump("loc_1448")

    label("loc_13F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1448")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_143F")
    SetScenarioFlags(0x22, 1)
    SetScenarioFlags(0x25, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1448")

    label("loc_143F")

    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_1448")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_4_126F end

    def Function_5_1450(): pass

    label("Function_5_1450")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1580")
    Fade(500)
    OP_68(10010, 600, 21560, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 10190, 0, 16230, 0)
    SetChrPos(0x1, 9210, 0, 16200, 0)
    SetChrPos(0x2, 8170, 0, 16290, 0)
    SetChrPos(0x3, 7240, 0, 16350, 0)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x8)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -40, 0, 30670, 105)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1536():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1536)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_1580")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_5_1450 end

    def Function_6_1584(): pass

    label("Function_6_1584")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, 10030, 0, 16580, 0)
    OP_31(0x1)
    OP_68(10030, 600, 16580, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x5)
    Return()

    # Function_6_1584 end

    def Function_7_15D5(): pass

    label("Function_7_15D5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1630")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1625")
    Sound(2502, 255, 100, 0)
    Jump("loc_162B")

    label("loc_1625")

    Sound(2503, 255, 100, 0)

    label("loc_162B")

    Jump("loc_1654")

    label("loc_1630")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_164E")
    Sound(3347, 255, 100, 0)
    Jump("loc_1654")

    label("loc_164E")

    Sound(3348, 255, 100, 0)

    label("loc_1654")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_15D5 end

    def Function_8_1669(): pass

    label("Function_8_1669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16DB")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FKa aa, if you look at this guy\x01",
            "You should be surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehuu, let's pick you up soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_16DB")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_170D")
    SetScenarioFlags(0x31, 2)

    label("loc_170D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_174D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1742")
    Sound(2499, 255, 100, 0)
    Jump("loc_1748")

    label("loc_1742")

    Sound(3537, 255, 100, 0)

    label("loc_1748")

    Jump("loc_1753")

    label("loc_174D")

    Sound(3344, 255, 100, 0)

    label("loc_1753")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_17CC")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17AC"),
        (SWITCH_DEFAULT, "loc_17BD"),
    )


    label("loc_17AC")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_17C7")

    label("loc_17BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C7")

    Jump("loc_1A0B")

    label("loc_17CC")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1800")
    MenuCmd(1, 0, "Take a break with a driving car")

    label("loc_1800")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1834"),
        (1, "loc_1938"),
        (2, "loc_19C9"),
        (SWITCH_DEFAULT, "loc_1A01"),
    )


    label("loc_1834")

    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1865")
    OP_70(0x1, 0x12C)
    OP_71(0x1, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_1875")

    label("loc_1865")

    OP_70(0x1, 0xF0)
    OP_71(0x1, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_1875")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18CB")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18EE")
    Sound(461, 0, 100, 0)

    label("loc_18EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_190E")
    OP_70(0x1, 0x14A)
    OP_71(0x1, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_191E")

    label("loc_190E")

    OP_70(0x1, 0x10E)
    OP_71(0x1, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_191E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x1, "light", 0x1, 0x1)
    OP_70(0x1, 0x0)
    Jump("loc_1753")

    label("loc_1938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_19AA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_196D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1985")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1980")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1985")

    label("loc_1980")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1985")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19C4")

    label("loc_19AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19BA")
    OP_AF(0xFB)
    Jump("loc_19C4")

    label("loc_19BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19C4")

    Jump("loc_1A0B")

    label("loc_19C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FC")

    label("loc_19E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19F2")
    OP_AF(0xFB)
    Jump("loc_19FC")

    label("loc_19F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19FC")

    Jump("loc_1A0B")

    label("loc_1A01")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A0B")

    Jump("loc_1753")

    label("loc_1A10")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_8_1669 end

    def Function_9_1A1E(): pass

    label("Function_9_1A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A30")
    Call(0, 10)
    Return()

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A65")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A77")
    Call(0, 10)
    Return()

    label("loc_1A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AE5")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FAnyway, now,\x01",
            "Let's concentrate on the accident-related investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B32")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The guiding bus seems to be out of service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA8")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001FThere is no business on Mainz.\x01",
            "There is no need to wait for the bus.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1BF0")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The guiding bus seems to be out of service.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1BF0")

    Call(0, 4)
    Return()

    # Function_9_1A1E end

    def Function_10_1BF4(): pass

    label("Function_10_1BF4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FThere is no business on Mainz.\x01",
            "There is no need to wait for the bus.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3D")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As the story progresses,\x01",
            "From the bus stops at various stops\x01",
            "It will be available.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because it is convenient for crossing the highway,\x01",
            "Please use it after the time has come.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_1D3D")

    EventEnd(0x3)
    Return()

    # Function_10_1BF4 end

    def Function_11_1D40(): pass

    label("Function_11_1D40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51107.itc", 0x1E)
    SoundLoad(468)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, -2900, -7900, 0)
    OP_D5(0xA, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    FadeToBright(1000, 0)
    BeginChrThread(0xA, 3, 0, 12)
    BeginChrThread(0xC, 1, 0, 18)
    OP_68(-3400, 2700, 4900, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19150, 0)
    OP_68(-4150, 4300, 8400, 7500)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0xA, 3)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1200, 18900, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12500, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x101, 750, 0, 19850, 45)
    SetChrPos(0x102, 750, 0, 19850, 45)
    SetChrPos(0x109, 750, 0, 19850, 45)
    SetChrPos(0x105, 750, 0, 19850, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(1000)
    OP_68(4300, 1200, 19250, 6000)
    MoveCamera(45, 16, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14650, 6000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 15)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 16)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000F#11PWell ……\x01",
            "Is Kaoru still there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PAnyway Sunday school\x01",
            "Let's go to the classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, never to the church\x01",
            "I do not think I will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PWaji you like worship\x01",
            "It looks like you have not gone at all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#5PI do not dislike the goddess but\x01",
            "I am not good at church air from long ago.\x02\x03",
            "#10302FThis, Muzu itch#2RYellowtail#Will not you get it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F#11PA religiously bad group\x01",
            "He is led, he says to him well ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x102,
        (
            "#00111F#12PFrequently fighting \"jihad\"\x01",
            "I did not say that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#5PHuh, that is rather rather\x01",
            "It is a hobby of Abbas.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2200, 0, 11250, 0)

    NpcTalk(
        0x9,
        "Daughter's voice",
        "#1P……that.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xDAC)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2291():
        OP_93(0x101, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2291)
    Sleep(50)

    def lambda_22A1():
        OP_93(0x102, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22A1)
    Sleep(50)

    def lambda_22B1():
        OP_93(0x109, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_22B1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#00005F#5PHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5POh……?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7202", 0)
    Fade(500)
    SetChrPos(0x101, 4650, 0, 19500, 180)
    SetChrPos(0x102, 4400, 0, 18200, 180)
    SetChrPos(0x109, 2900, 0, 18500, 180)
    SetChrPos(0x105, 3150, 0, 19800, 180)
    OP_68(3350, 1400, 17650, 0)
    MoveCamera(135, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14350, 0)
    OP_68(3400, 1400, 18600, 3000)

    def lambda_238D():
        OP_95(0xFE, 3800, 0, 16050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_238D)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x9,
        "Sister clothing girl",
        (
            "#13803F#11PSuddenly, I'm sorry.\x02\x03",
            "#13800FCross Bell Cathedral is\x01",
            "Is this OK?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PAh, yes, that's right.\x01",
            "(It's a big trunk … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_9B(0x0, 0x102, 0x0, 0x28A, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        "#00105F#6PRe, Lease! Is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Sister clothing girl",
        (
            "#13805F#11PMr. Erie - san …\x01",
            "It is long time no see.\x02\x03",
            "#13802FBy the way, I am from Crossbell\x01",
            "You mentioned it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PYeah … …!\x02\x03",
            "#00109FHuh, no way, Mr. Lease and\x01",
            "I can reunite in such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PEr …\x01",
            "Are you acquainted with Ellie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#11PWell, what I was studying abroad\x01",
            "I think I talked … ….\x02\x03",
            "#00102FTwo years ago, to Alteria law country\x01",
            "It became indebted to me when I studied abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#6PAlteria law country ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6POh, it's certainly the seven Yi-cha party\x01",
            "Was it the place where the home base was?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Sister clothing girl",
        "#13804F#11PYeah, that's right.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "── Nice to meet you.\x01",
            "It is lease Argento.\x02\x03",
            "This time, in Crossbell Cathedral\x01",
            "I decided to go to work.\x02\x03",
            "Thank you.\x02",
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
        "#00000F#6PHere it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F#6PThank you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00102F#6PIs that so……\x01",
            "Mr. Leith went to Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105F#6POh……?\x01",
            "But surely Mr. Lease …\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3540, 1400, 18670, 750)

    def lambda_28DD():
        OP_96(0xFE, 0x109A, 0x0, 0x4010, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28DD)

    def lambda_28F7():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28F7)
    Sleep(100)

    def lambda_2907():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2907)
    Sleep(100)

    def lambda_2917():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2917)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#13806F#11P(…… Ellie.\x01",
            "I have one request. )\x02\x03",
            "#13808F(I do not want to distinguish my status otherwise\x01",
            "could you? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P(……Ah……\x01",
            "And yeah, that's right. )\x02\x03",
            "#00108F(That……\x01",
            "Is there anything wrong with you? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11P(Well, which is to Ellie\x01",
            "I will tell you the details. )\x02\x03",
            "#13802F(About the situation of crossbell\x01",
            "I also want to ask you. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#6P(I understand.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PEr, erly?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00109F#11PHaha, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11PBecause there is a greeting of the appointment\x01",
            "I am sorry for this.\x02\x03",
            "#13800F……by the way\x01",
            "Do you guys also go to the cathedral?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#6PWell, I have a acquaintance child\x01",
            "I came to pick you up.\x02\x03",
            "#00100FProbably, in the classroom of Sunday school\x01",
            "I think that it is … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13804F#11PIs that so.\x01",
            "… Well then.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3620, 1400, 19740, 5000)

    def lambda_2C91():

        label("loc_2C91")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2C91")

    QueueWorkItem2(0x101, 2, lambda_2C91)

    def lambda_2CA3():

        label("loc_2CA3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2CA3")

    QueueWorkItem2(0x102, 2, lambda_2CA3)

    def lambda_2CB5():

        label("loc_2CB5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2CB5")

    QueueWorkItem2(0x109, 2, lambda_2CB5)

    def lambda_2CC7():

        label("loc_2CC7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2CC7")

    QueueWorkItem2(0x105, 2, lambda_2CC7)
    BeginChrThread(0x9, 3, 0, 17)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#11PI had something unique\x01",
            "I was Sister ….\x02\x03",
            "It was very calm\x01",
            "Is it older than we are?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#11PBecause it was on one of me\x01",
            "You should be 19 years old.\x02\x03",
            "#00100FWhen I was staying in Alteria\x01",
            "By chance I …\x02\x03",
            "#00109FHuhu, in various delicious shops\x01",
            "He took me along.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        "#10105F#12PIs it a delicious shop?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#5PYeah, look ah\x01",
            "He is a person I love to eat.\x02\x03",
            "#00102FIf I came to Crossbell\x01",
            "I have to introduce good shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PHuh, you surely\x01",
            "There seems to be introductions.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWada, what's wrong?\x01",
            "Stare staring ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F64():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F64)
    Sleep(100)

    def lambda_2F74():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F74)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x105,
        (
            "#10303F#12P……Disagreeable.\x02\x03",
            "#10300FI got an interesting sign.\x01",
            "Please think that it is your sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11PIt is! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PInteresting sign … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PSurely there's sister\x01",
            "I felt a pure feeling … ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PNo, if anything\x01",
            "I guess the atmosphere is not a Tada.\x02\x03",
            "#10302F…… Apparently someone\x01",
            "It seems I know something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00109F#11PWhat, what is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 350)

    ChrTalk(
        0x109,
        "#10100F#12PIs it? Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell, oh well.\x02\x03",
            "#00000FIt is almost time for sunset.\x01",
            "Let's pick up Ka'a soon.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00106F#11PThat's right.\x01",
            "(Waji, you're too sharp … …)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(14850, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 6300, 0, 24000, 45)
    SetScenarioFlags(0x127, 7)
    OP_29(0xA1, 0x1, 0xA)
    OP_1B(0x2, 0x0, 0x18)
    OP_1B(0x0, 0x0, 0x19)
    OP_66(0x1, 0x1)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM("ed7150", "ed7102")
    OP_24(0x1D4)
    EventEnd(0x5)
    Return()

    # Function_11_1D40 end

    def Function_12_322E(): pass

    label("Function_12_322E")

    SetChrPos(0xFE, 0, -2900, -7900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 0, -550, 0)
    OP_9F(0x1, 0, 350, 8800)
    OP_9F(0x1, -50, 0, 13200)
    OP_9F(0x1, -350, 0, 15050)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    OP_71(0x1, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_12_322E end

    def Function_13_32BE(): pass

    label("Function_13_32BE")


    def lambda_32C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32C3)
    OP_95(0xFE, 5600, 0, 20200, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_32BE end

    def Function_14_32EF(): pass

    label("Function_14_32EF")


    def lambda_32F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32F4)
    OP_95(0xFE, 4550, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_32EF end

    def Function_15_3320(): pass

    label("Function_15_3320")


    def lambda_3325():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3325)
    OP_95(0xFE, 4050, 0, 20250, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_3320 end

    def Function_16_3351(): pass

    label("Function_16_3351")


    def lambda_3356():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3356)
    OP_95(0xFE, 3050, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_3351 end

    def Function_17_3382(): pass

    label("Function_17_3382")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 6000, 0, 17000, 2000, 0x1)
    OP_95(0xFE, 8500, 0, 25900, 2000, 0x0)
    Return()

    # Function_17_3382 end

    def Function_18_33B2(): pass

    label("Function_18_33B2")

    Sound(468, 2, 100, 0)
    Sound(494, 0, 70, 0)
    Sleep(1500)
    Sound(459, 0, 100, 0)
    Sleep(5000)
    Sound(492, 0, 80, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_33B2 end

    def Function_19_33D7(): pass

    label("Function_19_33D7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SoundLoad(3599)
    OP_68(4650, 800, 21900, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16350, 0)
    SetChrPos(0x101, 13080, 0, 28350, 225)
    SetChrPos(0x102, 13200, 250, 30000, 225)
    SetChrPos(0x109, 14500, 250, 30050, 225)
    SetChrPos(0x105, 15650, 0, 29950, 225)
    SetChrPos(0x153, 11400, 250, 26600, 225)
    FadeToBright(1000, 0)
    OP_68(7500, 800, 23800, 3500)

    def lambda_349C():
        OP_95(0xFE, 10200, 0, 25750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_349C)

    def lambda_34B6():
        OP_95(0xFE, 9950, 150, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34B6)

    def lambda_34D0():
        OP_95(0xFE, 11300, 250, 27300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34D0)

    def lambda_34EA():
        OP_95(0xFE, 12450, 250, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_34EA)

    def lambda_3504():
        OP_95(0xFE, 7500, 0, 23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3504)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x153, 1)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        "#01109F#3599V#5P#40WWow, it's a car!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE0F)
    OP_C9(0x1, 0x80000000)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x101, 12700, 0, 26550, 270)
    SetChrPos(0x102, 13650, 0, 26000, 270)
    SetChrPos(0x109, 13800, 0, 27350, 270)
    SetChrPos(0x105, 14700, 0, 26500, 270)
    SetChrPos(0x153, 9750, 0, 24200, 270)
    OP_68(1050, 800, 21000, 0)
    MoveCamera(27, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17350, 0)
    SetCameraDistance(16350, 2500)

    def lambda_361C():
        OP_95(0xFE, 2650, 0, 21050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_361C)
    WaitChrThread(0x153, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x153,
        (
            "#01110F#11PIt's pretty beautiful!\x01",
            "Who came aboard?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 20)
    Sleep(1500)
    OP_68(2950, 1000, 21250, 6000)
    MoveCamera(27, 24, 0, 6000)
    SetCameraDistance(18000, 6000)

    def lambda_36A9():
        OP_96(0xFE, 0xE74, 0x0, 0x5366, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A9)
    Sleep(150)

    def lambda_36C6():
        OP_96(0xFE, 0x122A, 0x0, 0x5140, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36C6)
    Sleep(150)

    def lambda_36E3():
        OP_96(0xFE, 0x12C0, 0x0, 0x5686, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36E3)
    Sleep(150)

    def lambda_3700():
        OP_96(0xFE, 0x1644, 0x0, 0x5334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3700)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10112F#11PHaha ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHuh, this is for sure\x01",
            "You seem to be pleased.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x153, 0x5A, 0x1F4)

    ChrTalk(
        0x153,
        "#01100F#6PWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PKa aa, surprise by listening.\x02\x03",
            "#00000FWhat hides this car\x01",
            "We got on.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#01105F#6PHo, really! Is it?\x02\x03",
            "#01107FThe treasure hit the treasure! Is it?\x01",
            "Or you say you made it in turnip! Is it?\x02",
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
        (
            "#00006F#11PKeya …\x01",
            "Before I knew such knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PWell, if you are in the crossbell\x01",
            "I will often hear it … …\x02\x03",
            "#00100FKa'a-chan, this car\x01",
            "It was provided for work.\x02\x03",
            "So exactly\x01",
            "It's not ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01102F#6PYeah, I see.\x02\x03",
            "#01109FHowever, it is a good kao!\x01",
            "It's pretty cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PHehe, Kea-chan,\x01",
            "It seems I know that.\x02\x03",
            "#10102FWhy do not you try getting on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#6PWell, I want to get on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PHaha, I am overjoyed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11POh, that's no problem\x01",
            "Will not you go home by another route?\x02\x03",
            "#10304FAs I go through the port area\x01",
            "I'd like to pass through East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11POh, it may be nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11POK, on that course\x01",
            "Shall we return to the support section?\x02\x03",
            "#00000FNoel, could you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PYes, it is cheap.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#01109F#6P#4SWell then, Let's Go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_33D7 end

    def Function_20_3C8D(): pass

    label("Function_20_3C8D")


    def lambda_3C92():

        label("loc_3C92")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3C92")

    QueueWorkItem2(0xFE, 2, lambda_3C92)
    OP_96(0xFE, 0x4B0, 0x0, 0x5AD2, 0x7D0, 0x0)
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(800)
    OP_64(0x153)
    OP_96(0xFE, 0x8CA, 0x0, 0x5208, 0x7D0, 0x0)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(600)
    EndChrThread(0xFE, 0x2)
    OP_96(0xFE, 0x866, 0x0, 0x477C, 0x7D0, 0x0)
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(400)
    OP_96(0xFE, 0x8CA, 0x0, 0x5208, 0x7D0, 0x0)
    Return()

    # Function_20_3C8D end

    def Function_21_3D42(): pass

    label("Function_21_3D42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, 10000, 0)
    SetChrPos(0x102, 1000, 0, 9500, 0)
    SetChrPos(0x103, -750, 0, 8500, 0)
    SetChrPos(0x109, 0, 0, 7750, 0)
    SetChrPos(0x105, 1500, 0, 8000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 800, 10000, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(850, 800, 12900, 3000)
    MoveCamera(50, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)

    def lambda_3E17():
        OP_9B(0x0, 0x101, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E17)
    Sleep(50)

    def lambda_3E2F():
        OP_9B(0x0, 0x102, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E2F)
    Sleep(50)

    def lambda_3E47():
        OP_9B(0x0, 0x103, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E47)
    Sleep(50)

    def lambda_3E5F():
        OP_9B(0x0, 0x109, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E5F)
    Sleep(50)

    def lambda_3E77():
        OP_9B(0x0, 0x105, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E77)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    def lambda_3EA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EA4)

    def lambda_3EB1():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3EB1)
    Sleep(50)

    def lambda_3EC1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3EC1)
    Sleep(50)

    def lambda_3ED1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3ED1)
    Sleep(50)

    def lambda_3EE1():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3EE1)
    Sleep(50)

    def lambda_3EF1():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EF1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00008F#5PWhat is the hill above the waterfall … …\x01",
            "Is it a small suspension bridge hanging place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PYeah, positionally\x01",
            "It should just be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PIt seems that the guard is in the vicinity\x01",
            "Perhaps it is better to go secretly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PI see …\x01",
            "I have no time to explain the circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PThat's probably true…\x02\x03",
            "#10101FAnyway this way\x01",
            "Let's go until just before the suspension bridge.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 700, 0, 13950, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x166, 3)
    EventEnd(0x5)
    Return()

    # Function_21_3D42 end

    def Function_22_40C2(): pass

    label("Function_22_40C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 5100, 0, 19400, 270)
    SetChrPos(0x102, 3400, 0, 18350, 45)
    SetChrPos(0x103, 4700, 0, 20450, 180)
    SetChrPos(0x109, 1250, 0, 19500, 270)
    SetChrPos(0x105, 3500, 0, 20950, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-1250, 600, 18950, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(4150, 600, 19600, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(23500, 3000)
    Sound(461, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x109, 0xB4, 0x1F4)
    OP_95(0x109, 3000, 0, 19500, 2000, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00008F#11PWhat is the hill above the waterfall … …\x01",
            "Is it a small suspension bridge hanging place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PYeah, positionally\x01",
            "It should just be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PIt seems that the guard is in the vicinity\x01",
            "Perhaps it is better to go secretly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PI see …\x01",
            "I have no time to explain the circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PThat's probably true…\x02\x03",
            "#10101FAnyway this way\x01",
            "Let's go until just before the suspension bridge.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5100, 0, 19400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x166, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_22_40C2 end

    def Function_23_4369(): pass

    label("Function_23_4369")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(24150, 130, 33310, 0)
    MoveCamera(54, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21160, 0)
    SetChrPos(0x18D, 24890, 120, 31720, 270)
    SetChrPos(0x101, 23000, 130, 32259, 90)
    SetChrPos(0x102, 22060, 120, 31350, 90)
    SetChrPos(0x103, 22160, 130, 33020, 90)
    SetChrPos(0x104, 20520, 120, 31760, 90)
    SetChrPos(0x109, 20700, 130, 33000, 90)
    SetChrPos(0x105, 20830, 130, 30480, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4571")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "Drive Sister · Lease with a driving car\x01",
            "I sent it to Crossbell Cathedral.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7202", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FEveryone, you bother to send me\x01",
            "Thank you very much.\x02\x03",
            "#04402FYour guided car …\x01",
            "Very comfortable ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha, please be glad\x01",
            "I am also happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EB")

    label("loc_4571")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "Take a bus with Sister Lease,\x01",
            "I sent it to Crossbell Cathedral.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7202", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FEveryone, you bother to send me\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FNo, that's a big deal ….\x02\x03",
            "#10106FIf it is true our guiding car\x01",
            "It is a place I wanted to give you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04402FHehe, let's do it.\x01",
            "I look forward to your next opportunity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46EB")


    ChrTalk(
        0x101,
        (
            "#6P#00001Fby the way……\x01",
            "About \"star cup knight\"\x01",
            "To the cathedral people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04403FYes, I have not told anyone.\x02\x03",
            "#04408FTruly Archbishop Ellarda\x01",
            "It seems a bit thin …\x02\x03",
            "#04404FWell, I have to hit it badly\x01",
            "I think whether there is a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FWell, in the church too\x01",
            "There seems to be a lot of difficulties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FMr. Lease,\x01",
            "Please do not be unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, that and too much nerve\x01",
            "Do not wear down.\x02\x03",
            "#10302FIt looks bad for beauty too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FYeah … … Do not worry.\x02\x03",
            "#04400FThen, if there is something again\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, this is it.\x02",
    )

    CloseMessageWindow()
    OP_97(0x18D, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0x18D, 0x80)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright ……\x01",
            "Well then, we\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYes, that's OK.\x02",
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
            "Quest 【Monthly Monastery Investigation】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7C, 0x1, 0x4)
    OP_29(0x7C, 0x1, 0x5)
    OP_29(0x7C, 0x4, 0x10)
    RemoveParty(0x8C, 0x0)
    SetChrPos(0x0, 5530, 0, 23110, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_4369 end

    def Function_24_4A3C(): pass

    label("Function_24_4A3C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB8")

    ChrTalk(
        0x101,
        (
            "#00000FIs this Mainz Mountain Road ……\x02\x03",
            "I do not have any particular business,\x01",
            "Let's not stop going any further.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4AFE")

    label("loc_4AB8")


    ChrTalk(
        0x101,
        (
            "#00000FThere is no business on Mainz.\x01",
            "Let's not stop going any further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B50")

    ChrTalk(
        0x101,
        (
            "#00000FOops, this is the opposite direction.\x01",
            "Let's pick up Ka'a soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCA")

    ChrTalk(
        0x101,
        (
            "#00000FIs this Mainz Mountain Road ……\x02\x03",
            "I do not have any particular business,\x01",
            "Let's not stop going any further.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C10")

    label("loc_4BCA")


    ChrTalk(
        0x101,
        (
            "#00000FThere is no business on Mainz.\x01",
            "Let's not stop going any further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C8B")

    ChrTalk(
        0x101,
        (
            "#00001FA battle is going on ……\x02\x03",
            "But now anyway\x01",
            "I have to keep track of Randy 's footsteps.\x01",
            "- Let's return to the city once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CD1")

    ChrTalk(
        0x101,
        (
            "#00001FThere is no errands in the direction of the mountain road.\x01",
            "Let's turn back to life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D50")

    ChrTalk(
        0x101,
        (
            "#00001FCome this far to the city\x01",
            "I can not leave.\x02\x03",
            "Operation into the Orkis Tower -\x01",
            "You must make it successful at all costs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D50")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_24_4A3C end

    def Function_25_4D64(): pass

    label("Function_25_4D64")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's pick up Ka'a soon.\x01",
            "Then it is time to get back to the city.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -200, -500, 1530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_4D64 end

    def Function_26_4DBA(): pass

    label("Function_26_4DBA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South · Crossbell City\x01",
            "East · Crossbell Cathedral\x01",
            "Northwest · Mining Town Mainz 311 Serju\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_4DBA end

    SaveToFile()

Try(main)
