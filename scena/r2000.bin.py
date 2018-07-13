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
        "Function_5_148D",         # 05, 5
        "Function_6_15C1",         # 06, 6
        "Function_7_1612",         # 07, 7
        "Function_8_16A6",         # 08, 8
        "Function_9_1A5D",         # 09, 9
        "Function_10_1C85",        # 0A, 10
        "Function_11_1E2D",        # 0B, 11
        "Function_12_34F0",        # 0C, 12
        "Function_13_3580",        # 0D, 13
        "Function_14_35B1",        # 0E, 14
        "Function_15_35E2",        # 0F, 15
        "Function_16_3613",        # 10, 16
        "Function_17_3644",        # 11, 17
        "Function_18_3674",        # 12, 18
        "Function_19_3699",        # 13, 19
        "Function_20_3F71",        # 14, 20
        "Function_21_4026",        # 15, 21
        "Function_22_43F5",        # 16, 22
        "Function_23_46EB",        # 17, 23
        "Function_24_4EAA",        # 18, 24
        "Function_25_5307",        # 19, 25
        "Function_26_536B",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136D")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you inspect the bus stop signboard,\x01",
            "you will be able to ride the orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please use it to move to various places\x01",
            "the same way you do with the orbal car.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_136D")


    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThere is a bus stop.\x01",
            "Move by bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Mining Town Mainz\x01",                  # 0
            "Bus Stop (Nearby Doll Studio)\x01",      # 1
            "Quit\x01",                               # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1434")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1426")
    SetScenarioFlags(0x22, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_142F")

    label("loc_1426")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_142F")

    Jump("loc_1485")

    label("loc_1434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1485")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_147C")
    SetScenarioFlags(0x22, 1)
    SetScenarioFlags(0x25, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1485")

    label("loc_147C")

    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_1485")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_4_126F end

    def Function_5_148D(): pass

    label("Function_5_148D")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_15BD")
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

    def lambda_1573():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1573)
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

    label("loc_15BD")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_5_148D end

    def Function_6_15C1(): pass

    label("Function_6_15C1")

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

    # Function_6_15C1 end

    def Function_7_1612(): pass

    label("Function_7_1612")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_166D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1662")
    Sound(2502, 255, 100, 0)
    Jump("loc_1668")

    label("loc_1662")

    Sound(2503, 255, 100, 0)

    label("loc_1668")

    Jump("loc_1691")

    label("loc_166D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_168B")
    Sound(3347, 255, 100, 0)
    Jump("loc_1691")

    label("loc_168B")

    Sound(3348, 255, 100, 0)

    label("loc_1691")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1612 end

    def Function_8_16A6(): pass

    label("Function_8_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1724")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FWhen she sees this,\x01",
            "KeA will be surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, let's go pick her up quick.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_1724")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1756")
    SetScenarioFlags(0x31, 2)

    label("loc_1756")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_179C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1796")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_178B")
    Sound(2499, 255, 100, 0)
    Jump("loc_1791")

    label("loc_178B")

    Sound(3537, 255, 100, 0)

    label("loc_1791")

    Jump("loc_179C")

    label("loc_1796")

    Sound(3344, 255, 100, 0)

    label("loc_179C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_180F")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17EF"),
        (SWITCH_DEFAULT, "loc_1800"),
    )


    label("loc_17EF")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_180A")

    label("loc_1800")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180A")

    Jump("loc_1A4A")

    label("loc_180F")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1841")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_1841")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1873"),
        (1, "loc_1977"),
        (2, "loc_1A08"),
        (SWITCH_DEFAULT, "loc_1A40"),
    )


    label("loc_1873")

    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18A4")
    OP_70(0x1, 0x12C)
    OP_71(0x1, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_18B4")

    label("loc_18A4")

    OP_70(0x1, 0xF0)
    OP_71(0x1, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_18B4")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_190A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192D")
    Sound(461, 0, 100, 0)

    label("loc_192D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_194D")
    OP_70(0x1, 0x14A)
    OP_71(0x1, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_195D")

    label("loc_194D")

    OP_70(0x1, 0x10E)
    OP_71(0x1, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_195D")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x1, "light", 0x1, 0x1)
    OP_70(0x1, 0x0)
    Jump("loc_179C")

    label("loc_1977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_19E9")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_19AC")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_19C4")

    label("loc_19AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19BF")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_19C4")

    label("loc_19BF")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_19C4")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A03")

    label("loc_19E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19F9")
    OP_AF(0xFB)
    Jump("loc_1A03")

    label("loc_19F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A03")

    Jump("loc_1A4A")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A21")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A3B")

    label("loc_1A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1A31")
    OP_AF(0xFB)
    Jump("loc_1A3B")

    label("loc_1A31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A3B")

    Jump("loc_1A4A")

    label("loc_1A40")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A4A")

    Jump("loc_179C")

    label("loc_1A4F")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_8_16A6 end

    def Function_9_1A5D(): pass

    label("Function_9_1A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A6F")
    Call(0, 10)
    Return()

    label("loc_1A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AAA")
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

    label("loc_1AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ABC")
    Call(0, 10)
    Return()

    label("loc_1ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3F")
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
            "#00000FFor now anyway, let's focus\x01",
            "on the accident investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B94")
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

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C31")
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
            "#00001FWe don't have any business in the Mainz region.\x01",
            "There's no need to wait for the bus.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1C81")
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

    label("loc_1C81")

    Call(0, 4)
    Return()

    # Function_9_1A5D end

    def Function_10_1C85(): pass

    label("Function_10_1C85")

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
            "#00000FWe don't have any business in the Mainz region.\x01",
            "There's no need to wait for the bus.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2A")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When the story advances, you\x01",
            "will be able to use the buses\x01",
            "from all the bus stops.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Since they are convenient for going back and forth on\x01",
            "the highways, please use them when the time comes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_1E2A")

    EventEnd(0x3)
    Return()

    # Function_10_1C85 end

    def Function_11_1E2D(): pass

    label("Function_11_1E2D")

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
            "#00000F#11PWell then... I wonder\x01",
            "if KeA is still around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#12PAt any rate, let's try to go to\x01",
            "the Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5POh boy, I'd never thought I\x01",
            "would've gone to a church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PIt seems that you don't\x01",
            "worship at all, Wazy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#5PIt's not that I hate the Goddess, but\x01",
            "I've always been bad with the churches'\x01",
            "atmosphere for as long as I can remember.\x02\x03",
            "#10302FI mean, don't they feel creepy? No?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F#11PYou're one to say it after you lead\x01",
            "a religious-ish delinquent group...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x102,
        (
            "#00111F#12PWeren't you often saying that\x01",
            "fights were "holy wars"...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#5PUh uh, if pushed I'd say\x01",
            "that's Abbas' tastes.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2200, 0, 11250, 0)

    NpcTalk(
        0x9,
        "Girl's Voice",
        "#1P...Excuse me.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xDAC)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_23ED():
        OP_93(0x101, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23ED)
    Sleep(50)

    def lambda_23FD():
        OP_93(0x102, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23FD)
    Sleep(50)

    def lambda_240D():
        OP_93(0x109, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_240D)
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
        "#00105F#5POh...?\x02",
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

    def lambda_24E5():
        OP_95(0xFE, 3800, 0, 16050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24E5)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x9,
        "Girl in Nun's Clothes",
        (
            "#13803F#11PSorry for calling you abruptly.\x02\x03",
            "#13800FAm I going in the right direction\x01",
            "for Crossbell Cathedral?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PAh, yes you're.\x01",
            "(What a big trunk...)\x02",
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
        "#00105F#6PM-Miss Ries!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Girl in Nun's Clothes",
        (
            "#13805F#11PMiss Elie...\x01",
            "It's been a long time.\x02\x03",
            "#13802FNow that I think about it, you\x01",
            "said you were from Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PYes...!\x02\x03",
            "#00109F*giggle*, to think I could meet again\x01",
            "Miss Ries in such a place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUhhm...\x01",
            "Is she your acquaintance, Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes, I think I told you I studied\x01",
            "abroad in many countries...\x02\x03",
            "#00102FTwo years ago, when I was studying in the\x01",
            "Holy Nation of Arteria, she took care of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#6PThe Holy Nation of Arteria...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PEeh, isn't the place where the Septian\x01",
            "Church headquarters are located?\x02",
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
            "──Nice to meet you.\x01",
            "I am Ries Argent.\x02\x03",
            "This time, I was appointed\x01",
            "to the Crossbell Cathedral.\x02\x03",
            "It's nice to meet you all.\x02",
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
            "#00102F#6PI see... You were assigned to the\x01",
            "Crossbell Cathedral, Miss Ries.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105F#6POh...?\x01",
            "But, I'm sure that Miss Ries...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3540, 1400, 18670, 750)

    def lambda_2AAE():
        OP_96(0xFE, 0x109A, 0x0, 0x4010, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2AAE)

    def lambda_2AC8():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AC8)
    Sleep(100)

    def lambda_2AD8():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2AD8)
    Sleep(100)

    def lambda_2AE8():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2AE8)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#13806F#11P(...Miss Elie, I have\x01",
            "a favor to ask.)\x02\x03",
            "#13808F(Could you not say a word\x01",
            "about my social status?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6P(...Ah... \x01",
            "You're very right.)\x02\x03",
            "#00108F(Uhm... Were there some reasons\x01",
            "behind your assignment here?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11P(Yes. In time, I will tell you\x01",
            "the details, Miss Elie.)\x02\x03",
            "#13802F(I also want to ask you about\x01",
            "the situation in Crossbell...)\x02",
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
        "#00005F#6PUhhm, Elie?\x02",
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
            "#13803F#11PSince I have to go around to greet people,\x01",
            "I will excuse myself now.\x02\x03",
            "#13800F...By the way, do you all have something\x01",
            "to do at the cathedral too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#6PUhm, we came to pick\x01",
            "up a child we know.\x02\x03",
            "#00100FWe think that she could be in\x01",
            "the Sunday School classroom...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13804F#11PIs that so?\x01",
            "...Then, see you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3620, 1400, 19740, 5000)

    def lambda_2E9E():

        label("loc_2E9E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2E9E")

    QueueWorkItem2(0x101, 2, lambda_2E9E)

    def lambda_2EB0():

        label("loc_2EB0")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2EB0")

    QueueWorkItem2(0x102, 2, lambda_2EB0)

    def lambda_2EC2():

        label("loc_2EC2")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2EC2")

    QueueWorkItem2(0x109, 2, lambda_2EC2)

    def lambda_2ED4():

        label("loc_2ED4")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2ED4")

    QueueWorkItem2(0x105, 2, lambda_2ED4)
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
            "#00002F#11PShe's a Sister possessing some\x01",
            "kind of a unique atmosphere...\x02\x03",
            "She was really calm...\x01",
            "Is she older than us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00104F#11PShe was one year older than me,\x01",
            "so she should be 19 years old.\x02\x03",
            "#00100FI met her by chance when\x01",
            "I was staying in Arteria...\x02\x03",
            "#00109F*giggle*, she took me to\x01",
            "many beautiful stores.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        "#10105F#12PBeautiful stores, it is?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        (
            "#00104F#5PYes. Despite appearances, she's\x01",
            "someone who loves to eat.\x02\x03",
            "#00102FSince she's come to Crossbell, I have \x01",
            "to introduce her to some nice stores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#12PUh uh, it seems it would be\x01",
            "worth to do that for sure.\x02",
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
            "You've been watching steadily...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31CD():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_31CD)
    Sleep(100)

    def lambda_31DD():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_31DD)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    ChrTalk(
        0x105,
        (
            "#10303F#12P...It's nothing.\x02\x03",
            "#10300FI was thinking that she's a woman\x01",
            "with an interesting presence.\x02",
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
        "#00001F#5PAn interesting presence...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#11PAs might be expected from a Sister, she\x01",
            "gave off a clean and pure vibe, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PNo, if I had to say, her air wasn't\x01",
            "that of a normal person.\x02\x03",
            "#10302F...It appears that a certain someone\x01",
            "knows about something, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00109F#11PW-What could you be referring to?\x02",
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
            "#00006F#5PU-Uhhm, oh, well.\x02\x03",
            "#00000FThe sun is about to set.\x01",
            "Let's go pick up KeA quick.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#00106F#11PR-Right.\x01",
            "(Wazy is too sharp...)\x02",
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

    # Function_11_1E2D end

    def Function_12_34F0(): pass

    label("Function_12_34F0")

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

    # Function_12_34F0 end

    def Function_13_3580(): pass

    label("Function_13_3580")


    def lambda_3585():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3585)
    OP_95(0xFE, 5600, 0, 20200, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_3580 end

    def Function_14_35B1(): pass

    label("Function_14_35B1")


    def lambda_35B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35B6)
    OP_95(0xFE, 4550, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_35B1 end

    def Function_15_35E2(): pass

    label("Function_15_35E2")


    def lambda_35E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35E7)
    OP_95(0xFE, 4050, 0, 20250, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_35E2 end

    def Function_16_3613(): pass

    label("Function_16_3613")


    def lambda_3618():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3618)
    OP_95(0xFE, 3050, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_3613 end

    def Function_17_3644(): pass

    label("Function_17_3644")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 6000, 0, 17000, 2000, 0x1)
    OP_95(0xFE, 8500, 0, 25900, 2000, 0x0)
    Return()

    # Function_17_3644 end

    def Function_18_3674(): pass

    label("Function_18_3674")

    Sound(468, 2, 100, 0)
    Sound(494, 0, 70, 0)
    Sleep(1500)
    Sound(459, 0, 100, 0)
    Sleep(5000)
    Sound(492, 0, 80, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_3674 end

    def Function_19_3699(): pass

    label("Function_19_3699")

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

    def lambda_375E():
        OP_95(0xFE, 10200, 0, 25750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_375E)

    def lambda_3778():
        OP_95(0xFE, 9950, 150, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3778)

    def lambda_3792():
        OP_95(0xFE, 11300, 250, 27300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3792)

    def lambda_37AC():
        OP_95(0xFE, 12450, 250, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37AC)

    def lambda_37C6():
        OP_95(0xFE, 7500, 0, 23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_37C6)
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

    def lambda_38DC():
        OP_95(0xFE, 2650, 0, 21050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_38DC)
    WaitChrThread(0x153, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x153,
        (
            "#01110F#11PHow pretty it is!\x01",
            "Who came in this, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 20)
    Sleep(1500)
    OP_68(2950, 1000, 21250, 6000)
    MoveCamera(27, 24, 0, 6000)
    SetCameraDistance(18000, 6000)

    def lambda_3969():
        OP_96(0xFE, 0xE74, 0x0, 0x5366, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3969)
    Sleep(150)

    def lambda_3986():
        OP_96(0xFE, 0x122A, 0x0, 0x5140, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3986)
    Sleep(150)

    def lambda_39A3():
        OP_96(0xFE, 0x12C0, 0x0, 0x5686, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_39A3)
    Sleep(150)

    def lambda_39C0():
        OP_96(0xFE, 0x1644, 0x0, 0x5334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39C0)
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
            "#10304F#11PUh uh, it really seems she's\x01",
            "going to be happy for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x153, 0x5A, 0x1F4)

    ChrTalk(
        0x153,
        "#01100F#6PHmm, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PKeA, listen and be surprised.\x02\x03",
            "#00000FTo tell you the truth,\x01",
            "we came in this car.\x02",
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
            "#01107FDid you hit the lottery!?\x01",
            "Or did you profit with stocks!?\x02",
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
            "#00006F#11PKeA... When did you\x01",
            "learn those things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PWell, being in Crossbell you\x01",
            "hear a lot about those...\x02\x03",
            "#00100FKeA, this car was given\x01",
            "to us for job use.\x02\x03",
            "That's why, to be precise,\x01",
            "it's not ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01102F#6PEeeh, I see.\x02\x03",
            "#01109FBut it's good-looking!\x01",
            "And very cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#11PUh uh, it seems KeA\x01",
            "gets her beauty.\x02\x03",
            "#10102FDo you want to ride it now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01110F#6PYes, I want to!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11PHa ha, she's really happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PYeah, since we have the chance, why\x01",
            "don't we go home via a different route?\x02\x03",
            "#10304FI'd like to pass through the Waterfront\x01",
            "Area and then through the East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PMy, it could be nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PAll right, let's go home\x01",
            "doing that course.\x02\x03",
            "#00000FNoｱl, can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PYes, it's a simple request.\x02",
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

    # Function_19_3699 end

    def Function_20_3F71(): pass

    label("Function_20_3F71")


    def lambda_3F76():

        label("loc_3F76")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3F76")

    QueueWorkItem2(0xFE, 2, lambda_3F76)
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

    # Function_20_3F71 end

    def Function_21_4026(): pass

    label("Function_21_4026")

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

    def lambda_40FB():
        OP_9B(0x0, 0x101, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_40FB)
    Sleep(50)

    def lambda_4113():
        OP_9B(0x0, 0x102, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4113)
    Sleep(50)

    def lambda_412B():
        OP_9B(0x0, 0x103, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_412B)
    Sleep(50)

    def lambda_4143():
        OP_9B(0x0, 0x109, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4143)
    Sleep(50)

    def lambda_415B():
        OP_9B(0x0, 0x105, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_415B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    def lambda_4188():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4188)

    def lambda_4195():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4195)
    Sleep(50)

    def lambda_41A5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41A5)
    Sleep(50)

    def lambda_41B5():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_41B5)
    Sleep(50)

    def lambda_41C5():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41C5)
    Sleep(50)

    def lambda_41D5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41D5)
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
            "#00008F#5PA high ground before the waterfall...\x01",
            "The place where the small suspension bridge is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6PYes. Location wise, it should\x01",
            "be just right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PIt appears the CGF is nearby, so\x01",
            "we should get close stealthily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PYou're right... We don't even have\x01",
            "the time to explain the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12P...Yes, it could really be the case.\x02\x03",
            "#10101FAnyway, let's keep moving and\x01",
            "go before the suspension bridge.\x02",
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

    # Function_21_4026 end

    def Function_22_43F5(): pass

    label("Function_22_43F5")

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
            "#00008F#11PA high ground before the waterfall...\x01",
            "The place where the small suspension bridge is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PYes. Location wise, it should\x01",
            "be just right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PIt appears the CGF is nearby, so\x01",
            "we should get close stealthily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYou're right... We don't even have\x01",
            "the time to explain the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6P...Yes, it could really be the case.\x02\x03",
            "#10101FAnyway, let's keep moving and\x01",
            "go before the suspension bridge.\x02",
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

    # Function_22_43F5 end

    def Function_23_46EB(): pass

    label("Function_23_46EB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4932")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others\x01",
            "escorted Sister Ries to the Crossbell\x01",
            "Cathedral using the orbal car.\x07\x00\x02",
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
            "#11P#04404FEveryone, thank you very much for going\x01",
            "out of your way to escort me back.\x02\x03",
            "#04402FAbout everyone's orbal car...\x01",
            "I really loved the feeling while riding in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109FUh uh, I too am glad\x01",
            "that you enjoyed it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AEE")

    label("loc_4932")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others\x01",
            "escorted Sister Ries to the Crossbell\x01",
            "Cathedral riding the bus together.\x07\x00\x02",
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
            "#11P#04404FEveryone, thank you very much for going\x01",
            "out of your way to escort me back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FNo, we didn't do anything special...\x02\x03",
            "#10106FAlthough...I would've actually liked\x01",
            "to have made you ride our orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04402FUh uh, by all means, let's do\x01",
            "that on the next opportunity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AEE")


    ChrTalk(
        0x101,
        (
            "#6P#00001FBy the way...\x01",
            "You didn't tell to the cathedral people\x01",
            "about you being a "Gralsritter"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04403FNo, I didn't tell anyone.\x02\x03",
            "#04408FAlthough I'm sure Archbishop Eralda\x01",
            "had a slight inkling about it...\x02\x03",
            "#04404FWell, unless I arise suspicions\x01",
            "I think it won't be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FUhhm, it seems that in the Church\x01",
            "they're havin' it tough too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FMiss Ries, please don't\x01",
            "do anything reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FUh uh, also, don't fray\x01",
            "your nerves too much.\x02\x03",
            "#10302FIt seems it's bad for your beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18D,
        (
            "#11P#04404FYes...do not worry about it.\x02\x03",
            "#04400FThen, I will be counting on you\x01",
            "if something happens again.\x02",
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
            "#11P#00000FAll right...\x01",
            "Then, shall\x01",
            "we go too?\x02",
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
            "Quest [The Temple of Moon Investigation]\x07\x00",
            " completed!\x02",
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

    # Function_23_46EB end

    def Function_24_4EAA(): pass

    label("Function_24_4EAA")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F58")

    ChrTalk(
        0x101,
        (
            "#00000FThis way leads to Mainz Mountain Path...\x02\x03",
            "We don't have any particular business there,\x01",
            "so let's not proceed any more than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4FC8")

    label("loc_4F58")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any particular business in the Mainz\x01",
            "region, so let's not proceed any more than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5024")

    ChrTalk(
        0x101,
        (
            "#00000FOops, this is the opposite direction.\x01",
            "Let's go pick up KeA quick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50D0")

    ChrTalk(
        0x101,
        (
            "#00000FThis way leads to Mainz Mountain Path...\x02\x03",
            "We don't have any particular business there,\x01",
            "so let's not proceed any more than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5140")

    label("loc_50D0")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any particular business in the Mainz\x01",
            "region, so let's not proceed any more than this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51DE")

    ChrTalk(
        0x101,
        (
            "#00001FA battle is going on further here...\x02\x03",
            "However, in any case we must\x01",
            "follow Randy's traces now.\x01",
            "Let's temporarily return to the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_524F")

    ChrTalk(
        0x101,
        (
            "#00001FWe don't have any business on the mountain\x01",
            "path area. Let's retrace our steps quietly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_524F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52F3")

    ChrTalk(
        0x101,
        (
            "#00001FWe came this far, we can't\x01",
            "leave the city premises.\x02\x03",
            "The Orchis Tower breaking into operation...\x01",
            "We have to make it succeed at all costs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F3")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_24_4EAA end

    def Function_25_5307(): pass

    label("Function_25_5307")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FLet's go pick up KeA quick.\x01",
            "We'll go back to the city after that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -200, -500, 1530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_5307 end

    def Function_26_536B(): pass

    label("Function_26_536B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South - Crossbell City\x01",
            "East - Crossbell Cathedral\x01",
            "North West - Mining Town Mainz  311 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_536B end

    SaveToFile()

Try(main)
