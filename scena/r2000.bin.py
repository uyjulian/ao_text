from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "バス",                   # 1
        "Sister Ries",            # 2
        "車",                     # 3
        "鉄鋼ドリュー",           # 4
        "SE制御",                 # 5
        "br2000",                 # 6
        "To Crossbell City",      # 7
        "To Crossbell Cathedral", # 8
        "To Mining Town Mainz",   # 9
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

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "To Crossbell Cathedral")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "To Mining Town Mainz")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")

    ChipFrameInfo(1096, 0)                                       # 0

    ScpFunction((
        "Function_0_448",          # 00, 0
        "Function_1_467",          # 01, 1
        "Function_2_F9D",          # 02, 2
        "Function_3_126B",         # 03, 3
        "Function_4_126F",         # 04, 4
        "Function_5_1479",         # 05, 5
        "Function_6_15AD",         # 06, 6
        "Function_7_15FE",         # 07, 7
        "Function_8_1692",         # 08, 8
        "Function_9_1A4E",         # 09, 9
        "Function_10_1C6A",        # 0A, 10
        "Function_11_1DF9",        # 0B, 11
        "Function_12_32F4",        # 0C, 12
        "Function_13_3384",        # 0D, 13
        "Function_14_33B5",        # 0E, 14
        "Function_15_33E6",        # 0F, 15
        "Function_16_3417",        # 10, 16
        "Function_17_3448",        # 11, 17
        "Function_18_3478",        # 12, 18
        "Function_19_349D",        # 13, 19
        "Function_20_3D30",        # 14, 20
        "Function_21_3DE5",        # 15, 21
        "Function_22_41A5",        # 16, 22
        "Function_23_448C",        # 17, 23
        "Function_24_4BCD",        # 18, 24
        "Function_25_5004",        # 19, 25
        "Function_26_5068",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135C")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you inspect the bus\x01",
            "stop sign, you can ride\x01",
            "the orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please use it to move to\x01",
            "various places the same way\x01",
            "you do with the orbal car.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_135C")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KIt's a bus stop. Ride the bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Mining Town Mainz\x01",                # 0
            "Bus Stop (Near Doll Studio)\x01",      # 1
            "Cancel\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1420")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1412")
    SetScenarioFlags(0x22, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_141B")

    label("loc_1412")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_141B")

    Jump("loc_1471")

    label("loc_1420")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1471")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1468")
    SetScenarioFlags(0x22, 1)
    SetScenarioFlags(0x25, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1471")

    label("loc_1468")

    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_1471")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_4_126F end

    def Function_5_1479(): pass

    label("Function_5_1479")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_15A9")
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

    def lambda_155F():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_155F)
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

    label("loc_15A9")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_5_1479 end

    def Function_6_15AD(): pass

    label("Function_6_15AD")

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

    # Function_6_15AD end

    def Function_7_15FE(): pass

    label("Function_7_15FE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_164E")
    Sound(2502, 255, 100, 0)
    Jump("loc_1654")

    label("loc_164E")

    Sound(2503, 255, 100, 0)

    label("loc_1654")

    Jump("loc_167D")

    label("loc_1659")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1677")
    Sound(3347, 255, 100, 0)
    Jump("loc_167D")

    label("loc_1677")

    Sound(3348, 255, 100, 0)

    label("loc_167D")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_15FE end

    def Function_8_1692(): pass

    label("Function_8_1692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1711")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FKeA will be surprised\x01",
            "when she sees this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, let's pick her\x01",
            "up right away.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_1711")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1743")
    SetScenarioFlags(0x31, 2)

    label("loc_1743")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1783")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1778")
    Sound(2499, 255, 100, 0)
    Jump("loc_177E")

    label("loc_1778")

    Sound(3537, 255, 100, 0)

    label("loc_177E")

    Jump("loc_1789")

    label("loc_1783")

    Sound(3344, 255, 100, 0)

    label("loc_1789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_17FE")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17DE"),
        (SWITCH_DEFAULT, "loc_17EF"),
    )


    label("loc_17DE")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_17F9")

    label("loc_17EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17F9")

    Jump("loc_1A3B")

    label("loc_17FE")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1830")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_1830")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1864"),
        (1, "loc_1968"),
        (2, "loc_19F9"),
        (SWITCH_DEFAULT, "loc_1A31"),
    )


    label("loc_1864")

    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1895")
    OP_70(0x1, 0x12C)
    OP_71(0x1, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_18A5")

    label("loc_1895")

    OP_70(0x1, 0xF0)
    OP_71(0x1, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_18A5")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18FB")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")
    Sound(461, 0, 100, 0)

    label("loc_191E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_193E")
    OP_70(0x1, 0x14A)
    OP_71(0x1, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_194E")

    label("loc_193E")

    OP_70(0x1, 0x10E)
    OP_71(0x1, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_194E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x1, "light", 0x1, 0x1)
    OP_70(0x1, 0x0)
    Jump("loc_1789")

    label("loc_1968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_19DA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_199D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_19B5")

    label("loc_199D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19B0")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_19B5")

    label("loc_19B0")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_19B5")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19F4")

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19EA")
    OP_AF(0xFB)
    Jump("loc_19F4")

    label("loc_19EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19F4")

    Jump("loc_1A3B")

    label("loc_19F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A12")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A2C")

    label("loc_1A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1A22")
    OP_AF(0xFB)
    Jump("loc_1A2C")

    label("loc_1A22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A2C")

    Jump("loc_1A3B")

    label("loc_1A31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A3B")

    Jump("loc_1789")

    label("loc_1A40")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_8_1692 end

    def Function_9_1A4E(): pass

    label("Function_9_1A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A60")
    Call(0, 10)
    Return()

    label("loc_1A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A97")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AA9")
    Call(0, 10)
    Return()

    label("loc_1AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B28")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FFor now anyway, let's\x01",
            "focus on the accident\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B7D")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C16")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business\x01",
            "in the Mainz region. There's\x01",
            "no need to wait for the bus.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1C66")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems the orbal bus service is not running.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1C66")

    Call(0, 4)
    Return()

    # Function_9_1A4E end

    def Function_10_1C6A(): pass

    label("Function_10_1C6A")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business\x01",
            "in the Mainz region. There's\x01",
            "no need to wait for the bus.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF6")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When the story advances,\x01",
            "you will be able to take\x01",
            "the bus at all bus stops.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They are convenient for traveling\x01",
            "on the highways, so please use\x01",
            "them when the time comes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_1DF6")

    EventEnd(0x3)
    Return()

    # Function_10_1C6A end

    def Function_11_1DF9(): pass

    label("Function_11_1DF9")

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
            "#00000F#11PWell then... I wonder if\x01",
            "KeA's still around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PAnyway, let's go to the\x01",
            "Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PMan, never thought I'd\x01",
            "set foot in a church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PYou don't seem very\x01",
            "religious, Wazy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#5PI don't hate the Goddess\x01",
            "or anything, I just\x01",
            "don't like churches.\x02\x03",
            "#10302FI mean, aren't they just\x01",
            "creepy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F#11PYou say that, even though\x01",
            "you're the leader of that\x01",
            "faith-based delinquent group...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x102,
        (
            "#00111F#12PDidn't you often call\x01",
            "fights "holy wars" and\x01",
            "such...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#5PHaha. If pushed, I'd say\x01",
            "that's what Abbas liked.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2200, 0, 11250, 0)

    NpcTalk(
        0x9,
        "Girl's Voice",
        "#1P...Ahem.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xDAC)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2366():
        OP_93(0x101, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2366)
    Sleep(50)

    def lambda_2376():
        OP_93(0x102, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2376)
    Sleep(50)

    def lambda_2386():
        OP_93(0x109, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2386)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#00005F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PWhat?\x02",
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

    def lambda_245D():
        OP_95(0xFE, 3800, 0, 16050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_245D)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x9,
        "Girl in Nun's Clothes",
        (
            "#13803F#11PSorry for interrupting.\x02\x03",
            "#13800FIs this the way to\x01",
            "Crossbell Cathedral?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PAh, yes, it is. (That's\x01",
            "a huge trunk...)\x02",
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
        "#00105F#6PR-Ries!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Girl in Nun's Clothes",
        (
            "#13805F#11PElie! Long time no see.\x02\x03",
            "#13802FThat's right, you said\x01",
            "you were from Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PYes!\x02\x03",
            "#00109FHaha, I never thought\x01",
            "I'd see you in a place\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUmm... Do you know her,\x01",
            "Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, I think I told you\x01",
            "I studied abroad in many\x01",
            "countries...\x02\x03",
            "#00102FRies was a great help to\x01",
            "me when I studied in the\x01",
            "Holy Nation of Arteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PThe Holy Nation Of\x01",
            "Arteria...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PWow, that's where the\x01",
            "seat of the Septian\x01",
            "Church is, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Girl in Nun's Clothes",
        "#13804F#11PYes, you're correct.\x02",
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
            "─How do you do. I'm Ries Argent.\x02\x03",
            "I've been assigned to Crossbell\x01",
            "Cathedral.\x02\x03",
            "Nice to meet you.\x02",
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
        "#00000F#6PL-Likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10104F#6PNice to meet you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00102F#6PI see. So you're heading\x01",
            "to Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#6POh? But I thought you...\x02",
    )

    CloseMessageWindow()
    OP_68(3540, 1400, 18670, 750)

    def lambda_2983():
        OP_96(0xFE, 0x109A, 0x0, 0x4010, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2983)

    def lambda_299D():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_299D)
    Sleep(100)

    def lambda_29AD():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_29AD)
    Sleep(100)

    def lambda_29BD():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_29BD)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#13806F#11P(...Elie, I have a favor\x01",
            "to ask.)\x02\x03",
            "#13808F(Could you keep quiet\x01",
            "about my position?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P(...Ah... You're quite\x01",
            "right.)\x02\x03",
            "#00108F(Uhm... There were some\x01",
            "reasons behind your\x01",
            "assignment here?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11P(Yes. I'll explain the\x01",
            "details before long,\x01",
            "Elie.)\x02\x03",
            "#13802F(I also want to ask you\x01",
            "about the situation in\x01",
            "Crossbell...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#6P(I-I understand.)\x02",
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
        "#00005F#6PUmm, Elie?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00109F#11PAhaha, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11PI need to report in, so\x01",
            "please excuse me.\x02\x03",
            "#13800F...By the way, are you\x01",
            "guys going to the\x01",
            "cathedral too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#6PYeah, we're here to pick\x01",
            "up a girl we know.\x02\x03",
            "#00100FShe's probably in the\x01",
            "Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13804F#11PI see... See you later,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3620, 1400, 19740, 5000)

    def lambda_2D26():

        label("loc_2D26")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2D26")

    QueueWorkItem2(0x101, 2, lambda_2D26)

    def lambda_2D38():

        label("loc_2D38")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2D38")

    QueueWorkItem2(0x102, 2, lambda_2D38)

    def lambda_2D4A():

        label("loc_2D4A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2D4A")

    QueueWorkItem2(0x109, 2, lambda_2D4A)

    def lambda_2D5C():

        label("loc_2D5C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2D5C")

    QueueWorkItem2(0x105, 2, lambda_2D5C)
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
            "#00002F#11PA sister with a unique\x01",
            "atmosphere about her...\x02\x03",
            "She's very calm too. Is\x01",
            "she older than us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#11PShe was one year older\x01",
            "than me, so she should\x01",
            "be 19.\x02\x03",
            "#00100FI met her when I was\x01",
            "staying in Arteria...\x02\x03",
            "#00109FHaha. She took me to a\x01",
            "lot of good restaurants.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        "#10105F#12PGood restaurants?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#5PYes. Despite\x01",
            "appearances, she loves\x01",
            "to eat.\x02\x03",
            "#00102FNow that she's here, I\x01",
            "have to introduce her to\x01",
            "Crossbell's restaurants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PHaha. I'm sure she'll\x01",
            "love them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#5PWazy, what's wrong?\x01",
            "You're staring...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FF2():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2FF2)
    Sleep(100)

    def lambda_3002():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3002)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x105,
        (
            "#10303F#12P...It's nothing.\x02\x03",
            "#10300FI was just thinking she\x01",
            "has an interesting\x01",
            "presence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11P!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5PAn interesting presence?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PAs might be expected from a\x01",
            "sister, she gave off a clean\x01",
            "and pure impression, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PNo. If pushed, I'd say\x01",
            "she isn't anyone\x01",
            "ordinary.\x02\x03",
            "#10302F...It looks a certain\x01",
            "someone knows something,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00109F#11PW-What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 350)

    ChrTalk(
        0x109,
        "#10100F#12P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PH-Hmm. Well, whatever.\x02\x03",
            "#00000FThe sun is about to set.\x01",
            "Let's go pick up KeA.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00106F#11PR-Right. (Wazy is way\x01",
            "too sharp...)\x02",
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

    # Function_11_1DF9 end

    def Function_12_32F4(): pass

    label("Function_12_32F4")

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

    # Function_12_32F4 end

    def Function_13_3384(): pass

    label("Function_13_3384")


    def lambda_3389():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3389)
    OP_95(0xFE, 5600, 0, 20200, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_3384 end

    def Function_14_33B5(): pass

    label("Function_14_33B5")


    def lambda_33BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33BA)
    OP_95(0xFE, 4550, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_33B5 end

    def Function_15_33E6(): pass

    label("Function_15_33E6")


    def lambda_33EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33EB)
    OP_95(0xFE, 4050, 0, 20250, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_33E6 end

    def Function_16_3417(): pass

    label("Function_16_3417")


    def lambda_341C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_341C)
    OP_95(0xFE, 3050, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_3417 end

    def Function_17_3448(): pass

    label("Function_17_3448")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 6000, 0, 17000, 2000, 0x1)
    OP_95(0xFE, 8500, 0, 25900, 2000, 0x0)
    Return()

    # Function_17_3448 end

    def Function_18_3478(): pass

    label("Function_18_3478")

    Sound(468, 2, 100, 0)
    Sound(494, 0, 70, 0)
    Sleep(1500)
    Sound(459, 0, 100, 0)
    Sleep(5000)
    Sound(492, 0, 80, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_3478 end

    def Function_19_349D(): pass

    label("Function_19_349D")

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

    def lambda_3562():
        OP_95(0xFE, 10200, 0, 25750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3562)

    def lambda_357C():
        OP_95(0xFE, 9950, 150, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_357C)

    def lambda_3596():
        OP_95(0xFE, 11300, 250, 27300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3596)

    def lambda_35B0():
        OP_95(0xFE, 12450, 250, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_35B0)

    def lambda_35CA():
        OP_95(0xFE, 7500, 0, 23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_35CA)
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
        "#01109F#3599V#5P#40WWah, a car!\x02",
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

    def lambda_36DB():
        OP_95(0xFE, 2650, 0, 21050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_36DB)
    WaitChrThread(0x153, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x153,
        (
            "#01110F#11PIt's so pretty! I wonder\x01",
            "whose it is.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 20)
    Sleep(1500)
    OP_68(2950, 1000, 21250, 6000)
    MoveCamera(27, 24, 0, 6000)
    SetCameraDistance(18000, 6000)

    def lambda_3760():
        OP_96(0xFE, 0xE74, 0x0, 0x5366, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3760)
    Sleep(150)

    def lambda_377D():
        OP_96(0xFE, 0x122A, 0x0, 0x5140, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_377D)
    Sleep(150)

    def lambda_379A():
        OP_96(0xFE, 0x12C0, 0x0, 0x5686, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_379A)
    Sleep(150)

    def lambda_37B7():
        OP_96(0xFE, 0x1644, 0x0, 0x5334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37B7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#10112F#11PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PHaha, I think you're\x01",
            "gonna love this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x153, 0x5A, 0x1F4)

    ChrTalk(
        0x153,
        "#01100F#6PHuh? What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PKeA, you're not going to\x01",
            "believe this.\x02\x03",
            "#00000FI'll be honest with you,\x01",
            "KeA. This is our car.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#01105F#6PR-REALLY!?\x02\x03",
            "#01107FDid you hit the\x01",
            "lottery!? Or hit it big\x01",
            "on the stock market!?\x02",
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
            "#00006F#11PKeA... Where did you\x01",
            "learn about those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PWell, those are common\x01",
            "topics of conversation\x01",
            "in Crossbell...\x02\x03",
            "#00100FKeA, this car was issued\x01",
            "to us for our job.\x02\x03",
            "So, to be precise, it's\x01",
            "not ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01102F#6POh, I see!\x02\x03",
            "#01109FBut it's good-looking!\x01",
            "And so cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PHaha, it looks like KeA\x01",
            "understands.\x02\x03",
            "#10102FWanna take a ride?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#6PYeah I wanna!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PHaha, she's really\x01",
            "happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PSince we're here, why\x01",
            "don't we take a\x01",
            "different route home?\x02\x03",
            "#10304FI want to try going via\x01",
            "Waterfront Area and East\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11POh, that's a good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PAll right, let's go home\x01",
            "that way.\x02\x03",
            "#00000FNoｱl, if you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PSure, that's no problem\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#01109F#6P#4SThen, let's gooo!\x02",
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

    # Function_19_349D end

    def Function_20_3D30(): pass

    label("Function_20_3D30")


    def lambda_3D35():

        label("loc_3D35")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3D35")

    QueueWorkItem2(0xFE, 2, lambda_3D35)
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

    # Function_20_3D30 end

    def Function_21_3DE5(): pass

    label("Function_21_3DE5")

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

    def lambda_3EBA():
        OP_9B(0x0, 0x101, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3EBA)
    Sleep(50)

    def lambda_3ED2():
        OP_9B(0x0, 0x102, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3ED2)
    Sleep(50)

    def lambda_3EEA():
        OP_9B(0x0, 0x103, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3EEA)
    Sleep(50)

    def lambda_3F02():
        OP_9B(0x0, 0x109, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F02)
    Sleep(50)

    def lambda_3F1A():
        OP_9B(0x0, 0x105, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F1A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    def lambda_3F47():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F47)

    def lambda_3F54():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F54)
    Sleep(50)

    def lambda_3F64():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F64)
    Sleep(50)

    def lambda_3F74():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F74)
    Sleep(50)

    def lambda_3F84():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F84)
    Sleep(50)

    def lambda_3F94():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F94)
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
            "#00008F#5PHigh ground before the waterfall,\x01",
            "he said... Is it the place with\x01",
            "the small suspension bridge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PYes. Location wise,\x01",
            "that's where it should\x01",
            "be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PThe CGF is nearby, so we\x01",
            "should approach as\x01",
            "stealthily as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PRight... We don't even\x01",
            "have time to explain the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12PThat's probably true...\x02\x03",
            "#10101FAnyway, let's keep\x01",
            "moving and head up to\x01",
            "the suspension bridge.\x02",
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

    # Function_21_3DE5 end

    def Function_22_41A5(): pass

    label("Function_22_41A5")

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
            "#00008F#11PHigh ground before the waterfall,\x01",
            "he said... Is it the place with\x01",
            "the small suspension bridge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PYes. Location wise,\x01",
            "that's where it should\x01",
            "be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PThe CGF is nearby, so we\x01",
            "should approach as\x01",
            "stealthily as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PRight... We don't even\x01",
            "have time to explain the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PThat's probably true...\x02\x03",
            "#10101FAnyway, let's keep\x01",
            "moving and head up to\x01",
            "the suspension bridge.\x02",
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

    # Function_22_41A5 end

    def Function_23_448C(): pass

    label("Function_23_448C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4698")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others\x01",
            "escorted Sister Ries to Crossbell\x01",
            "Cathedral using their orbal car.\x07\x00\x02",
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
            "#11P#04404FEveryone, thank you for\x01",
            "going out of your way to\x01",
            "escort me back.\x02\x03",
            "#04402FYour car has a terribly\x01",
            "great ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FHaha. I'm just glad you\x01",
            "enjoyed it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4831")

    label("loc_4698")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others\x01",
            "rode the bus with Sister Ries and\x01",
            "escorted her to Crossbell Cathedral.\x07\x00\x02",
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
            "#11P#04404FEveryone, thank you for\x01",
            "going out of your way to\x01",
            "escort me back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FNo, it was no big\x01",
            "deal...\x02\x03",
            "#10106FAlthough... I would've\x01",
            "liked to have given you\x01",
            "a ride in our orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04402FHaha. I'll be looking\x01",
            "forward to next time,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4831")


    ChrTalk(
        0x101,
        (
            "#6P#00001FBy the way... Do the\x01",
            "cathedral people know\x01",
            "about the Gralsritter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04403FNo, I haven't told\x01",
            "anyone.\x02\x03",
            "#04408FAlthough Archbishop\x01",
            "Eralda seems slightly\x01",
            "suspicious...\x02\x03",
            "#04404FWell, I don't think\x01",
            "it'll be a problem as\x01",
            "long as I'm careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHmm. Looks like they've\x01",
            "got it pretty rough\x01",
            "within the Church, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FRies, please don't do\x01",
            "anything reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe. And try not to be\x01",
            "too nervous.\x02\x03",
            "#10302FI heard it's bad for\x01",
            "your beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FI will... No need to\x01",
            "worry.\x02\x03",
            "#04400FWell then, I'll be\x01",
            "counting on your help in\x01",
            "the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, likewise.\x02",
    )

    CloseMessageWindow()
    OP_97(0x18D, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0x18D, 0x80)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#00000FAll right... I think\x01",
            "it's time for us to be\x01",
            "going, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200FYes, roger.\x02",
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
            "Quest [Temple of Moon\x01",
            "Investigation]\x07\x00\x01",
            "completed!\x02",
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

    # Function_23_448C end

    def Function_24_4BCD(): pass

    label("Function_24_4BCD")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6E")

    ChrTalk(
        0x101,
        (
            "#00000FMainz Mountain Path is this\x01",
            "way...\x02\x03",
            "We don't have any particular\x01",
            "business there, so let's not\x01",
            "proceed any further.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4CD7")

    label("loc_4C6E")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any particular\x01",
            "business in the Mainz region, so\x01",
            "let's not proceed any further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D31")

    ChrTalk(
        0x101,
        (
            "#00000FWhoops, this is the\x01",
            "wrong way. Let's go pick\x01",
            "up KeA right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD0")

    ChrTalk(
        0x101,
        (
            "#00000FMainz Mountain Path is this\x01",
            "way...\x02\x03",
            "We don't have any particular\x01",
            "business there, so let's not\x01",
            "proceed any further.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4E39")

    label("loc_4DD0")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any particular\x01",
            "business in the Mainz region, so\x01",
            "let's not proceed any further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED1")

    ChrTalk(
        0x101,
        (
            "#00001FA battle is occurring further\x01",
            "in...\x02\x03",
            "But right now, we've got to\x01",
            "retrace Randy's footsteps. Let's\x01",
            "return to the city for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F34")

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business\x01",
            "in the mountain path area.\x01",
            "Let's turn around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FF0")

    ChrTalk(
        0x101,
        (
            "#00001FWe've come this far. There's no way\x01",
            "we're leaving the city now.\x02\x03",
            "The Orchis Tower infiltration\x01",
            "operation... We have to do whatever\x01",
            "it takes to make it a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF0")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_24_4BCD end

    def Function_25_5004(): pass

    label("Function_25_5004")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's hurry and pick up\x01",
            "KeA. We'll return to the\x01",
            "city after that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -200, -500, 1530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_5004 end

    def Function_26_5068(): pass

    label("Function_26_5068")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            " South - Crossbell City\x01",
            " East - Crossbell Cathedral\x01",
            "Northwest - Mining Town Mainz  311 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_5068 end

    SaveToFile()

Try(main)
