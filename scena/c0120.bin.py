from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0120.bin",                # FileName
        "c0120",                    # MapName
        "c0120",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0120",                  # 0
        "Sergey Manager",           # 1
        "Keya",                 # 2
        "letter",                   # 3
        "Enigma",               # 4
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
    ))

    DeclNpc(100089,  29,      65750,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  8,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(4294966436, 0,       128259,  1200,    4294966436, 3000,    128259,  0x007C, 0,  24, 0x0000)
    DeclActor(4294964506, 0,       127470,  1200,    4294964506, 2000,    127470,  0x007C, 0,  25, 0x0000)
    DeclActor(49300,   30,      129770,  1200,    49300,   3500,    129770,  0x007C, 0,  26, 0x0000)
    DeclActor(53410,   0,       123840,  1200,    53410,   2000,    123840,  0x007C, 0,  27, 0x0000)
    DeclActor(100740,  30,      129180,  1200,    100740,  1500,    129180,  0x007C, 0,  28, 0x0000)
    DeclActor(102940,  30,      125380,  1200,    102940,  2000,    125380,  0x007C, 0,  29, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  21, 0x0000)
    DeclActor(48000,   0,       127860,  1200,    47560,   1500,    128630,  0x007C, 0,  22, 0x0000)
    DeclActor(102450,  0,       127940,  1200,    102450,  1500,    127940,  0x007C, 0,  23, 0x0000)

    ChipFrameInfo(1132, 0)                                       # 0

    ScpFunction((
        "Function_0_46C",          # 00, 0
        "Function_1_51C",          # 01, 1
        "Function_2_724",          # 02, 2
        "Function_3_976",          # 03, 3
        "Function_4_C66",          # 04, 4
        "Function_5_CDB",          # 05, 5
        "Function_6_1260",         # 06, 6
        "Function_7_1569",         # 07, 7
        "Function_8_15BC",         # 08, 8
        "Function_9_1611",         # 09, 9
        "Function_10_16CE",        # 0A, 10
        "Function_11_178B",        # 0B, 11
        "Function_12_17E2",        # 0C, 12
        "Function_13_1A9E",        # 0D, 13
        "Function_14_1D7A",        # 0E, 14
        "Function_15_1F96",        # 0F, 15
        "Function_16_21BE",        # 10, 16
        "Function_17_221B",        # 11, 17
        "Function_18_2428",        # 12, 18
        "Function_19_263B",        # 13, 19
        "Function_20_284D",        # 14, 20
        "Function_21_2A5F",        # 15, 21
        "Function_22_2B04",        # 16, 22
        "Function_23_2BA9",        # 17, 23
        "Function_24_2C4E",        # 18, 24
        "Function_25_2D03",        # 19, 25
        "Function_26_2DBC",        # 1A, 26
        "Function_27_2E71",        # 1B, 27
        "Function_28_2F37",        # 1C, 28
        "Function_29_2FF2",        # 1D, 29
        "Function_30_30AD",        # 1E, 30
        "Function_31_3122",        # 1F, 31
        "Function_32_3151",        # 20, 32
        "Function_33_3180",        # 21, 33
        "Function_34_31AF",        # 22, 34
        "Function_35_31DE",        # 23, 35
        "Function_36_3D2F",        # 24, 36
        "Function_37_47C7",        # 25, 37
        "Function_38_48D4",        # 26, 38
        "Function_39_5945",        # 27, 39
        "Function_40_5980",        # 28, 40
        "Function_41_59BB",        # 29, 41
        "Function_42_611A",        # 2A, 42
        "Function_43_6B8E",        # 2B, 43
    ))


    def Function_0_46C(): pass

    label("Function_0_46C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A4"),
        (1, "loc_4B0"),
        (2, "loc_4BC"),
        (3, "loc_4C8"),
        (4, "loc_4D4"),
        (5, "loc_4E0"),
        (6, "loc_4EC"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_51B")

    Return()

    # Function_0_46C end

    def Function_1_51C(): pass

    label("Function_1_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_670")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特里斯坦号', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    Event(0, 14)

    label("loc_551")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你沙袋', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_578")
    Event(0, 15)

    label("loc_578")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    Event(0, 37)

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('点唱机', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E0")
    Event(0, 18)

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冲浪板', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    Event(0, 17)

    label("loc_607")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你水族馆', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    Event(0, 20)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('安乐椅', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
    Event(0, 19)

    label("loc_655")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_670")
    Event(0, 6)

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_67E")
    Jump("loc_6FA")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_68C")
    Jump("loc_6FA")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_6B6")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 49960, 30, 123630, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_6FA")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_6FA")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_END)), "loc_6EC")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 99500, 30, 65530, 180)

    label("loc_6EC")

    Jump("loc_6FA")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6FA")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_711")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 41)
    Jump("loc_723")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_723")
    ClearScenarioFlags(0x23, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 43)

    label("loc_723")

    Return()

    # Function_1_51C end

    def Function_2_724(): pass

    label("Function_2_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_739")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_783")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D7")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FE")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    Jump("loc_812")

    label("loc_7FE")

    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_82F")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_83E")

    label("loc_82F")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_851")
    OP_1B(0x2, 0x0, 0x2A)

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B")
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x2)
    OP_65(0x2, 0x1)

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A")
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x2)
    OP_65(0x3, 0x1)
    Jump("loc_896")

    label("loc_88A")

    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x2)

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B0")
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x2)
    OP_65(0x4, 0x1)

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x2)
    OP_65(0x5, 0x1)
    Jump("loc_8D5")

    label("loc_8CF")

    SetMapObjFlags(0xF, 0x4)

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EF")
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x2)
    OP_65(0x6, 0x1)

    label("loc_8EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_909")
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x2)
    OP_65(0x7, 0x1)

    label("loc_909")

    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_928")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_93B")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_93B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95D")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_95D")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_975")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_975")

    Return()

    # Function_2_724 end

    def Function_3_976(): pass

    label("Function_3_976")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F")

    ChrTalk(
        0x8,
        (
            "#01000FIn the case of national independence referendum,\x01",
            "Different papers are coming.\x02\x03",
            "I've got questions to worry about ……\x01",
            "Well, leave this to another section.\x02\x03",
            "For now, crisis management is the first choice.\x01",
            "Not just listening to the puppet factory,\x01",
            "You should also cover support requests.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B0C")

    label("loc_A7F")


    ChrTalk(
        0x8,
        (
            "#01000FOh, if you are in Kiha\x01",
            "It seems that I went shopping for dinner.\x02\x03",
            "I was somewhat close to the library … …\x01",
            "Well, if you worry, go get to see the situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C")

    Jump("loc_C62")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE2")

    ChrTalk(
        0x8,
        (
            "#01000FYeah, I also just arrived\x01",
            "I came back from the hospital.\x02\x03",
            "#01003FIf you continue,\x01",
            "Advance the investigation of \"Phantom beast\".\x02\x03",
            "#01002FBefore the \"sword of the wind\" moved\x01",
            "You should at the most improve your results.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C62")

    label("loc_BE2")


    ChrTalk(
        0x8,
        (
            "#01003FIf you continue,\x01",
            "Advance the investigation of \"Phantom beast\".\x02\x03",
            "#01002FBefore the \"sword of the wind\" moved\x01",
            "You should at the most improve your results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62")

    TalkEnd(0xFE)
    Return()

    # Function_3_976 end

    def Function_4_C66(): pass

    label("Function_4_C66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C84")
    Call(0, 5)
    Jump("loc_CD7")

    label("loc_C84")


    ChrTalk(
        0x9,
        (
            "#01100FGood luck guys.\x02\x03",
            "#01109FKia, where\x01",
            "I'm waiting for everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD7")

    TalkEnd(0xFE)
    Return()

    # Function_4_C66 end

    def Function_5_CDB(): pass

    label("Function_5_CDB")

    EventBegin(0x0)
    Fade(500)
    OP_68(49470, 1300, 122080, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22450, 0)
    SetChrPos(0x101, 49340, 0, 122340, 0)
    SetChrPos(0x102, 50640, 0, 122340, 0)
    SetChrPos(0x103, 49970, 0, 121240, 0)
    SetChrPos(0x109, 48730, 0, 121240, 0)
    SetChrPos(0x105, 51310, 0, 121240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00100FKa'a-chan … You were here.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x12C)

    ChrTalk(
        0x9,
        "#5P#01100FOh, yes ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#5P#01108F…… Randy,\x01",
            "When I wrote that Tegami\x01",
            "How did it feel?\x02\x03",
            "#01103FI will not meet key people anymore ……\x01",
            "I wonder what was going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FKeya …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F…… Randy is trying to fight\x01",
            "It seems to be too mighty.\x02\x03",
            "#10303FEven if you're challenging with the preparedness to let go of everything\x01",
            "Perhaps nothing is strange.\x02\x03",
            "#10308FWhereabouts, fellows … even my own life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F…… With such a selfish selfishness\x01",
            "I will let you go through the support section.\x02\x03",
            "Eli, Tio, Randy ……\x01",
            "Noel, Wadi, Sergey Manager\x01",
            "Zeite in the key a …\x02\x03",
            "#00001FIf someone in this is missing,\x01",
            "We are not \"support department\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FLloyd … well.\x02\x03",
            "#00108FDo not try to understand such a thing,\x01",
            "Doing something for yourself without permission ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00203FWell, I guess it is severely punishable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#01108F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FDo not worry, Kia-chan.\x01",
            "Because seniors take absolutely home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, finally clues\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01110Fis that so……\x02\x03",
            "#01104FGood luck, everyone.\x02\x03",
            "#01109FKia, where\x01",
            "I'm waiting for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FOh, always with Randy\x01",
            "I will come back here.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x16B, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, 49970, 0, 121240, 0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    EventEnd(0x5)
    Return()

    # Function_5_CDB end

    def Function_6_1260(): pass

    label("Function_6_1260")

    EventBegin(0x0)
    Fade(500)
    OP_68(100360, 630, 124300, 0)
    MoveCamera(36, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 98820, 0, 123690, 315)
    SetChrPos(0x1, 100820, 0, 123690, 45)
    SetChrPos(0x2, 100680, 30, 121540, 0)
    SetChrPos(0x3, 99070, 30, 121530, 0)
    SetChrPos(0x4, 100020, 0, 124500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWelcome to my castle.\x01",
            "…… Anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_135E")

    ChrTalk(
        0x1A5,
        "#5P#01105FWow, beautiful rooms.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1397")

    label("loc_135E")


    ChrTalk(
        0x101,
        (
            "#5P#00005FAgain ……\x01",
            "It is truly a fashionable room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1397")


    ChrTalk(
        0x109,
        (
            "#12P#10105FHo, indeed …\x01",
            "Only in this room\x01",
            "It's like a model room.\x02\x03",
            "#10106FSomehow,\x01",
            "Is not it too early to familiar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYeah, moreover\x01",
            "Furniture that seems to be quite expensive\x01",
            "It seems to be complete … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, ask someone you know\x01",
            "I got it procured.\x02\x03",
            "#10300FWell, whenever you feel tired\x01",
            "You do not mind reaching me.\x02\x03",
            "It's been awfully crowded.\x01",
            "I try to open the bottle there\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00006FNo, it is useless for drift … …\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100020, 30, 121290, 0)
    SetScenarioFlags(0x13B, 5)
    EventEnd(0x5)
    Return()

    # Function_6_1260 end

    def Function_7_1569(): pass

    label("Function_7_1569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157B")
    Call(0, 12)
    Jump("loc_15BB")

    label("loc_157B")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Tio.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_15BB")

    Return()

    # Function_7_1569 end

    def Function_8_15BC(): pass

    label("Function_8_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CE")
    Call(0, 13)
    Jump("loc_1610")

    label("loc_15CE")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the room of Randy.\x01",
            "Let's stop entering.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1610")

    Return()

    # Function_8_15BC end

    def Function_9_1611(): pass

    label("Function_9_1611")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FSpeaking of which, Ka'aa\x01",
            "I told you to go to Sunday school.\x02\x03",
            "The manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's call out.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1611 end

    def Function_10_16CE(): pass

    label("Function_10_16CE")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FSpeaking of which, Ka'aa\x01",
            "I told you to go to Sunday school.\x02\x03",
            "The manager also went out,\x01",
            "You may as well go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FWell, let's call out.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_16CE end

    def Function_11_178B(): pass

    label("Function_11_178B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKa'a is a Sunday school from now.\x01",
            "The back door is a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_178B end

    def Function_12_17E2(): pass

    label("Function_12_17E2")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23860, 0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_187C")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_187C")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FSurely now, in Les Autonomous states\x01",
            "Are you on a business trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, with Jonah\x01",
            "Epstein Foundation's\x01",
            "I am going to the laboratory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith the amendment of the Autonomous State Law, the power net also\x01",
            "Diffusion is proceeding,\x01",
            "I guess that helped the relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI do not know the difficult thing ….\x01",
            "It seems quite tough.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A50")

    ChrTalk(
        0x1A5,
        "#12P#01100FTio, I hope to get back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A86")

    label("loc_1A50")


    ChrTalk(
        0x101,
        (
            "#00000FOh, as soon as I return\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A86")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_12_17E2 end

    def Function_13_1A9E(): pass

    label("Function_13_1A9E")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23800, 0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B38")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_1B38")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy 's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is now,\x01",
            "With the troops of the Belgard gate\x01",
            "It is in the midst of rehabilitation training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FOh, surely in a cult incident\x01",
            "Did you have the case of the example?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYup……\x01",
            "Something terrible as sequelae\x01",
            "I do not remember.\x02\x03",
            "#10108FTo regain physical strength and can\x01",
            "It looks like it will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FReally……\x01",
            "I want the guard to recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0x1A5,
        "#12P#01100FI wonder if Randy will come back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D62")

    label("loc_1D24")


    ChrTalk(
        0x102,
        (
            "#00100FWell, Randy also\x01",
            "I want to get back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D62")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_13_1A9E end

    def Function_14_1D7A(): pass

    label("Function_14_1D7A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    OP_68(-460, 1300, 127470, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD4")
    SetChrFlags(0x0, 0x8)

    label("loc_1DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE7")
    SetChrFlags(0x1, 0x8)

    label("loc_1DE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DFA")
    SetChrFlags(0x2, 0x8)

    label("loc_1DFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0D")
    SetChrFlags(0x3, 0x8)

    label("loc_1E0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E20")
    SetChrFlags(0x4, 0x8)

    label("loc_1E20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E33")
    SetChrFlags(0x5, 0x8)

    label("loc_1E33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E4C")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_1E4C")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -460, 0, 127470, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FIs it okay here?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the room of Lloyd\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('特里斯坦号', 1)
    SetScenarioFlags(0x13C, 0)
    OP_66(0x2, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")
    Call(0, 38)

    label("loc_1EF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0A")
    ClearChrFlags(0x0, 0x8)

    label("loc_1F0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1D")
    ClearChrFlags(0x1, 0x8)

    label("loc_1F1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F30")
    ClearChrFlags(0x2, 0x8)

    label("loc_1F30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F43")
    ClearChrFlags(0x3, 0x8)

    label("loc_1F43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F56")
    ClearChrFlags(0x4, 0x8)

    label("loc_1F56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F69")
    ClearChrFlags(0x5, 0x8)

    label("loc_1F69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F82")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_1F82")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_14_1D7A end

    def Function_15_1F96(): pass

    label("Function_15_1F96")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x2)
    OP_68(-2420, 1330, 126860, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFC")
    SetChrFlags(0x0, 0x8)

    label("loc_1FFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200F")
    SetChrFlags(0x1, 0x8)

    label("loc_200F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2022")
    SetChrFlags(0x2, 0x8)

    label("loc_2022")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2035")
    SetChrFlags(0x3, 0x8)

    label("loc_2035")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2048")
    SetChrFlags(0x4, 0x8)

    label("loc_2048")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_205B")
    SetChrFlags(0x5, 0x8)

    label("loc_205B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2074")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_2074")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -2420, 30, 126860, 315)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FIs it okay here?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the room of Lloyd\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('迷你沙袋', 1)
    SetScenarioFlags(0x13C, 1)
    OP_66(0x3, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211F")
    Call(0, 38)

    label("loc_211F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2132")
    ClearChrFlags(0x0, 0x8)

    label("loc_2132")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2145")
    ClearChrFlags(0x1, 0x8)

    label("loc_2145")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2158")
    ClearChrFlags(0x2, 0x8)

    label("loc_2158")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_216B")
    ClearChrFlags(0x3, 0x8)

    label("loc_216B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_217E")
    ClearChrFlags(0x4, 0x8)

    label("loc_217E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2191")
    ClearChrFlags(0x5, 0x8)

    label("loc_2191")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21AA")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_21AA")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_15_1F96 end

    def Function_16_21BE(): pass

    label("Function_16_21BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When I get furniture items\x01",
            "You can put it in the support room 's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_221A")

    Return()

    # Function_16_21BE end

    def Function_17_221B(): pass

    label("Function_17_221B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(49580, 1330, 129410, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2275")
    SetChrFlags(0x0, 0x8)

    label("loc_2275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2288")
    SetChrFlags(0x1, 0x8)

    label("loc_2288")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229B")
    SetChrFlags(0x2, 0x8)

    label("loc_229B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22AE")
    SetChrFlags(0x3, 0x8)

    label("loc_22AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C1")
    SetChrFlags(0x4, 0x8)

    label("loc_22C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D4")
    SetChrFlags(0x5, 0x8)

    label("loc_22D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22ED")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_22ED")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 49580, 30, 129410, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FIs it OK here?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In Randy's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('冲浪板', 1)
    SetScenarioFlags(0x13C, 2)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239C")
    ClearChrFlags(0x0, 0x8)

    label("loc_239C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AF")
    ClearChrFlags(0x1, 0x8)

    label("loc_23AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C2")
    ClearChrFlags(0x2, 0x8)

    label("loc_23C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D5")
    ClearChrFlags(0x3, 0x8)

    label("loc_23D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E8")
    ClearChrFlags(0x4, 0x8)

    label("loc_23E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23FB")
    ClearChrFlags(0x5, 0x8)

    label("loc_23FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2414")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2414")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_17_221B end

    def Function_18_2428(): pass

    label("Function_18_2428")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFlags(0xF, 0x4)
    OP_68(52070, 1330, 123440, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2488")
    SetChrFlags(0x0, 0x8)

    label("loc_2488")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249B")
    SetChrFlags(0x1, 0x8)

    label("loc_249B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AE")
    SetChrFlags(0x2, 0x8)

    label("loc_24AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C1")
    SetChrFlags(0x3, 0x8)

    label("loc_24C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D4")
    SetChrFlags(0x4, 0x8)

    label("loc_24D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E7")
    SetChrFlags(0x5, 0x8)

    label("loc_24E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2500")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_2500")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52070, 30, 123440, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FIs it OK here?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In Randy's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('点唱机', 1)
    SetScenarioFlags(0x13C, 3)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AF")
    ClearChrFlags(0x0, 0x8)

    label("loc_25AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C2")
    ClearChrFlags(0x1, 0x8)

    label("loc_25C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D5")
    ClearChrFlags(0x2, 0x8)

    label("loc_25D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E8")
    ClearChrFlags(0x3, 0x8)

    label("loc_25E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25FB")
    ClearChrFlags(0x4, 0x8)

    label("loc_25FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_260E")
    ClearChrFlags(0x5, 0x8)

    label("loc_260E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2627")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2627")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_18_2428 end

    def Function_19_263B(): pass

    label("Function_19_263B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(100680, 1330, 127820, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2695")
    SetChrFlags(0x0, 0x8)

    label("loc_2695")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26A8")
    SetChrFlags(0x1, 0x8)

    label("loc_26A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26BB")
    SetChrFlags(0x2, 0x8)

    label("loc_26BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CE")
    SetChrFlags(0x3, 0x8)

    label("loc_26CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E1")
    SetChrFlags(0x4, 0x8)

    label("loc_26E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F4")
    SetChrFlags(0x5, 0x8)

    label("loc_26F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_270D")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_270D")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 100680, 30, 127820, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        "#10300FHuh, I wonder where I can go.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wadi's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('安乐椅', 1)
    SetScenarioFlags(0x13C, 4)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C1")
    ClearChrFlags(0x0, 0x8)

    label("loc_27C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D4")
    ClearChrFlags(0x1, 0x8)

    label("loc_27D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E7")
    ClearChrFlags(0x2, 0x8)

    label("loc_27E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27FA")
    ClearChrFlags(0x3, 0x8)

    label("loc_27FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280D")
    ClearChrFlags(0x4, 0x8)

    label("loc_280D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2820")
    ClearChrFlags(0x5, 0x8)

    label("loc_2820")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2839")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2839")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_19_263B end

    def Function_20_284D(): pass

    label("Function_20_284D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_68(101940, 1330, 125580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A7")
    SetChrFlags(0x0, 0x8)

    label("loc_28A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28BA")
    SetChrFlags(0x1, 0x8)

    label("loc_28BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28CD")
    SetChrFlags(0x2, 0x8)

    label("loc_28CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E0")
    SetChrFlags(0x3, 0x8)

    label("loc_28E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28F3")
    SetChrFlags(0x4, 0x8)

    label("loc_28F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2906")
    SetChrFlags(0x5, 0x8)

    label("loc_2906")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_291F")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_291F")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 101940, 30, 125580, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        "#10300FHuh, I wonder where I can go.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wadi's room\x01",
            "New furniture was added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('迷你水族馆', 1)
    SetScenarioFlags(0x13C, 5)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29D3")
    ClearChrFlags(0x0, 0x8)

    label("loc_29D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E6")
    ClearChrFlags(0x1, 0x8)

    label("loc_29E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F9")
    ClearChrFlags(0x2, 0x8)

    label("loc_29F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0C")
    ClearChrFlags(0x3, 0x8)

    label("loc_2A0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A1F")
    ClearChrFlags(0x4, 0x8)

    label("loc_2A1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A32")
    ClearChrFlags(0x5, 0x8)

    label("loc_2A32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A4B")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2A4B")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_20_284D end

    def Function_21_2A5F(): pass

    label("Function_21_2A5F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE6")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2AE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B02")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2B02")

    Return()

    # Function_21_2A5F end

    def Function_22_2B04(): pass

    label("Function_22_2B04")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8B")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2B8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA7")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2BA7")

    Return()

    # Function_22_2B04 end

    def Function_23_2BA9(): pass

    label("Function_23_2BA9")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To take a break here\x01",      # 0
            "quit\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C30")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2C4C")

    Return()

    # Function_23_2BA9 end

    def Function_24_2C4E(): pass

    label("Function_24_2C4E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis361.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is the Tristan issue.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_2C4E end

    def Function_25_2D03(): pass

    label("Function_25_2D03")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis360.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a mini sand bag.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_25_2D03 end

    def Function_26_2DBC(): pass

    label("Function_26_2DBC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis366.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a surfboard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_26_2DBC end

    def Function_27_2E71(): pass

    label("Function_27_2E71")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis367.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a jukebox.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7592", 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_2E71 end

    def Function_28_2F37(): pass

    label("Function_28_2F37")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis368.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a comfort chair.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_2F37 end

    def Function_29_2FF2(): pass

    label("Function_29_2FF2")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis369.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a mini aquarium.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_29_2FF2 end

    def Function_30_30AD(): pass

    label("Function_30_30AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3121")
    OP_E0(0x16, 0x0)

    label("loc_3121")

    Return()

    # Function_30_30AD end

    def Function_31_3122(): pass

    label("Function_31_3122")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_31_3122 end

    def Function_32_3151(): pass

    label("Function_32_3151")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_32_3151 end

    def Function_33_3180(): pass

    label("Function_33_3180")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_33_3180 end

    def Function_34_31AF(): pass

    label("Function_34_31AF")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_34_31AF end

    def Function_35_31DE(): pass

    label("Function_35_31DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2E")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis366.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis367.itp")
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 51750, 130, 125650, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3290")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3290")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32A9")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_32A9")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On that day, Lloyd's\x01",
            "Returning to the support section between support activities ----\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take a regular contact with the headquarters\x01",
            "I decided to take a break each time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(51630, 1830, 125550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(51630, 1330, 125550, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 49870, 0, 119410, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "#1PRandy, is it okay?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00300FOh, why.\x02",
    )

    CloseMessageWindow()
    OP_68(49870, 1300, 123830, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_3438():
        OP_9B(0x0, 0xFE, 0xA, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3438)

    def lambda_344D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_344D)
    OP_68(50750, 1300, 124710, 2000)
    MoveCamera(45, 21, 0, 2000)
    SetCameraDistance(21500, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x104, 500)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00300FWhat is it supposed to go soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I also have business contact from the headquarters\x01",
            "I did not have anything today.\x02\x03",
            "#00001F…… No way but I think\x01",
            "You did not make a full drink or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FGiggle\x01",
            "Iya, sonna kotoha.\x02\x03",
            "#00300FUtsushi-son\x01",
            "I will finally get out!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 51300, 30, 125650, 270)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x4)
    OP_0D()
    TurnDirection(0x104, 0x101, 500)
    Sleep(500)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#00006FAbsolutely …\x02\x03",
            "#00000F(It's quite serious as I say it\x01",
            "I do not worry too much, though. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(750)

    ChrTalk(
        0x101,
        (
            "#00005Fby the way……\x01",
            "Something has increased a lot?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(50440, 2200, 131009, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(21000, 3000)

    def lambda_36C6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36C6)
    Sleep(200)

    def lambda_36D6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 31)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000Fthis is……\x01",
            "Is it certainly a surfboard?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00303FOh, originally only by the seaside\x01",
            "I can not use it, is it a silymone ……\x02\x03",
            "#00300FWaves will stand on Lake Elm as well\x01",
            "At least, I do not have to play.\x02\x03",
            "#00309FWhat is Lake Surfing?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FWell, Randy is like that.\x01",
            "I heard that he likes quite a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_68(50390, 2200, 122310, 4000)
    MoveCamera(60, 25, 0, 4000)
    Sleep(1500)

    def lambda_3855():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3855)
    Sleep(200)

    def lambda_3865():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3865)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 33)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fthat is……\x01",
            "Er, what was it?\x02\x03",
            "#00003FIn a magazine or something\x01",
            "It seems like I have seen it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300FIt's a jukebox.\x02\x03",
            "#00303F10 If you put in miracoin\x01",
            "It will play your favorite song ……\x02\x03",
            "#00302FWell, at the end of the bar\x01",
            "It is a machine that is occasionally placed.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    Sleep(500)
    SetCameraDistance(18000, 5000)
    Sleep(500)
    OP_95(0x104, 51250, 30, 123870, 2000, 0x1)
    OP_95(0x104, 52210, 30, 123640, 2000, 0x0)
    Sleep(1000)
    StopBGM(0xBB8)
    Sound(99, 0, 100, 0)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x1, 0xA, 0x0, 0x8)
    Sleep(1500)
    OP_71(0xC, 0xA, 0x45, 0x0, 0x20)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7592", 0)
    Sleep(1500)
    OP_93(0x104, 0xB4, 0x1F4)
    OP_95(0x104, 52190, 0, 122140, 1000, 0x0)
    TurnDirection(0x104, 0x101, 500)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00004F…… Nice, this.\x02\x03",
            "#00003FWhat is it …?\x01",
            "It makes me feel very nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHa, per crossbell\x01",
            "I do not see it much …\x02\x03",
            "#00302FThere is no other entertainment,\x01",
            "If it is something like a rice cottage\x01",
            "It's rather a classic machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FIs it so……\x02\x03",
            "#00000FRandy used it before\x01",
            "Was there also a bar area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, well.\x02\x03",
            "#00303F…………………………………….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005FRandy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F…… Haha, whatever.\x02\x03",
            "#00300FAre you going soon?\x01",
            "Are your ladies waiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, shall we go?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I got all the furniture of Randy!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x104, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3CEF")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_3CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3D08")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_3D08")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_74(0xC, 0x1E)
    OP_70(0xC, 0x0)
    SetScenarioFlags(0x12D, 0)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 105, 0, 0)
    IdleLoop()

    label("loc_3D2E")

    Return()

    # Function_35_31DE end

    def Function_36_3D2F(): pass

    label("Function_36_3D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C6")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis368.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis369.itp")
    LoadChrToIndex("chr/ch03002.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, 100630, 200, 129169, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3DE7")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3DE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E00")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_3E00")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On that day, Lloyd's\x01",
            "Returning to the support section between support activities ----\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take a regular contact with the headquarters\x01",
            "I decided to take a break each time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(100220, 1830, 128539, 0)
    MoveCamera(33, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(100250, 1330, 128590, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 99800, 0, 119340, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "#1PWas this review helpful?\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10300FOh, do not hesitate to enter.\x02",
    )

    CloseMessageWindow()
    OP_68(98850, 1330, 122760, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_3F8E():
        OP_9B(0x0, 0xFE, 0x2, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F8E)

    def lambda_3FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FA3)
    OP_68(99510, 1330, 125860, 3000)
    MoveCamera(33, 20, 0, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(1000)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#10306FWhew.\x01",
            "Do you want to leave soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6POh, I also have business contact from the headquarters\x01",
            "I did not have anything today.\x02\x03",
            "#00005FWaa … ….\x01",
            "Do not you sit in a good chair?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99910, 1330, 128039, 2000)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 31)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10302FOh, made of Remiferia\x01",
            "Comfort chair.\x02\x03",
            "#10304FBased on ergonomics\x01",
            "Because it is designed\x01",
            "It feels really good.\x02\x03",
            "#10300FWould you like to sit down on a trial?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FWill it be okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10309FHuh, please.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    Sleep(500)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, 100240, 30, 128600, 192)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x4)
    OP_0D()
    OP_93(0x105, 0xE1, 0x1F4)
    OP_95(0x105, 98960, 30, 128789, 1000, 0x0)

    def lambda_4200():

        label("loc_4200")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4200")

    QueueWorkItem2(0x105, 1, lambda_4200)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FWell, then then ──\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    SetCameraDistance(20500, 2500)
    OP_95(0x101, 100460, 30, 126150, 2000, 0x1)
    OP_95(0x101, 100420, 30, 128020, 2000, 0x0)
    EndChrThread(0x105, 0x1)
    OP_93(0x105, 0x3C, 0x0)
    Sleep(500)
    OP_6F(0x79)
    Fade(500)
    Sound(898, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 100590, 200, 129080, 225)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(1000)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FAh……\x02\x03",
            "#00003F…………………………\x01",
            "……… awesome, this is.\x02\x03",
            "#00004FWhat is it, as if the body were\x01",
            "It seems to be wrapped …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, is not it?\x02\x03",
            "#10304FWell, in this way\x01",
            "You can also relieve stress\x01",
            "It is a necessary ingenuity.\x02\x03",
            "#10309FAs the number one in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThat's not a host\x01",
            "Tired of the hard duties of the support department\x01",
            "Please say for healing … …\x02\x03",
            "#00002FAh … … but that tank is nice,\x01",
            "Certainly I can relax.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(100920, 1330, 128039, 2500)
    MoveCamera(45, 20, 0, 2500)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_93(0x105, 0x78, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 33)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fby the way……\x01",
            "Is that aquarium also a hobby of Wadi?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10305FAh……\x02\x03",
            "#10304FIf it is rather\x01",
            "Because it used to be nostalgic, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F…… Huh, this story.\x02\x03",
            "#10300FFrom here more\x01",
            "Amenity#2RRelax#Can I do it?\x02\x03",
            "#10309FI do not mind as much as I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x40)
    SetChrPos(0x101, 100240, 30, 128600, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    TurnDirection(0x101, 0x105, 0)
    OP_68(100140, 1330, 128180, 500)
    MoveCamera(45, 20, 0, 500)
    SetCameraDistance(21000, 500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00011FWell, that was right!\x02\x03",
            "#00001FEveryone will be waiting,\x01",
            "I will hurry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FOK, leader.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "We got all the furniture of Wadi!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x105, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_478D")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_478D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_47A6")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_47A6")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 2)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 114, 0, 0)
    IdleLoop()

    label("loc_47C6")

    Return()

    # Function_36_3D2F end

    def Function_37_47C7(): pass

    label("Function_37_47C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E7")
    SetChrFlags(0x0, 0x8)

    label("loc_47E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47FA")
    SetChrFlags(0x1, 0x8)

    label("loc_47FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_480D")
    SetChrFlags(0x2, 0x8)

    label("loc_480D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4820")
    SetChrFlags(0x3, 0x8)

    label("loc_4820")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4833")
    SetChrFlags(0x4, 0x8)

    label("loc_4833")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4846")
    SetChrFlags(0x5, 0x8)

    label("loc_4846")

    ClearChrFlags(0x101, 0x8)
    Call(0, 38)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4861")
    ClearChrFlags(0x0, 0x8)

    label("loc_4861")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4874")
    ClearChrFlags(0x1, 0x8)

    label("loc_4874")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4887")
    ClearChrFlags(0x2, 0x8)

    label("loc_4887")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_489A")
    ClearChrFlags(0x3, 0x8)

    label("loc_489A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48AD")
    ClearChrFlags(0x4, 0x8)

    label("loc_48AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48C0")
    ClearChrFlags(0x5, 0x8)

    label("loc_48C0")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_37_47C7 end

    def Function_38_48D4(): pass

    label("Function_38_48D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5944")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis361.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis360.itp")
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    SoundLoad(3666)
    SoundLoad(3667)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_497A")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_497A")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 2400, 900, 125400, 180)
    SetMapObjFlags(0x8, 0x4)
    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "On that day, Lloyd's\x01",
            "Returning to the support section between support activities ----\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take a regular contact with the headquarters\x01",
            "I decided to take a break each time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(1820, 1830, 125210, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(1820, 1330, 125210, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#05203FFu … … regular contacts are over.\x02\x03",
            "#05209FI wish I could take a nap like this\x01",
            "I do not want to translate that … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x9, -100, 0, 119480, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x1000)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x9,
        "Ka'a voice",
        (
            "#1P#3666VHey Hey.\x01",
            "Lloyd, are you here?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE52)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0x101, 0x3)
    Sleep(250)
    SetChrSubChip(0x101, 0x4)
    Sleep(150)
    SetChrSubChip(0x101, 0x5)
    Sleep(500)
    SetChrSubChip(0x101, 0x6)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#05202FOh, let's go.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1)
    SetChrPos(0x101, 1280, 30, 125030, 225)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    OP_68(-420, 1330, 122210, 2500)
    OP_0D()
    OP_95(0x101, 400, 30, 123890, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(-170, 1330, 122810, 2000)

    def lambda_4C6A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C6A)

    def lambda_4C7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4C7F)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D67")

    ChrTalk(
        0x101,
        (
            "#05205F#1PThat, Kia,\x01",
            "You were out?\x02\x03",
            "#05203FDid you come back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01100F#2POh, yeah.\x01",
            "Because there was a lost item.\x02\x03",
            "#01109FBecause of Lloyd's sign\x01",
            "I wonder if she is there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D67")

    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#01110F#2P#3667VAh……!\x01",
            "Something is increasing!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE53)
    OP_C9(0x1, 0x80000000)
    OP_68(-170, 1330, 125490, 4000)
    MoveCamera(45, 22, 0, 4000)

    def lambda_4DDC():

        label("loc_4DDC")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_4DDC")

    QueueWorkItem2(0x101, 1, lambda_4DDC)
    OP_95(0x9, -2180, 30, 126470, 2000, 0x0)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x2D, 0x1F4)
    OP_95(0x9, 10, 30, 127370, 2000, 0x0)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_95(0x9, 400, 30, 125890, 2000, 0x0)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05202Fmy mother……\x01",
            "Would not it be somewhat unusual?\x02\x03",
            "#05204FWhat you see normally\x01",
            "It will not exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FWow!\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    OP_68(360, 1330, 128889, 2500)
    SetCameraDistance(21500, 2500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_4F18():
        OP_95(0xFE, 710, 0, 127430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F18)
    Sleep(250)

    def lambda_4F35():
        OP_95(0xFE, -130, 30, 126060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F35)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x0)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 31)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105FIs it? Is it? Is it?\x02\x03",
            "#01100FThis is there\x01",
            "It is the same moisture as a car, is not it?\x02\x03",
            "#01103FWhat is an airship?\x01",
            "It looks like the shape is different.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05200FOh, this comes out in the movie\x01",
            "Fictitious rides.\x02\x03",
            "#05203FSay \"airplane\"\x01",
            "Without using the power\x01",
            "The sky can fly like a bird.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01102FWow ….\x01",
            "Maybe I want to ride a bit.\x02\x03",
            "#01105FOh, but what you say is kaku\x01",
            "You really did not fly?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05205FWell, I think so.\x02\x03",
            "#05203FI can not fly in the sky without using power\x01",
            "I think that it is impossible usually ……\x02\x03",
            "#05208F(No … … unexpectedly somewhere.\x01",
            "Are you being developed? )\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_63(0x9, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_93(0x9, 0x10E, 0x1F4)

    ChrTalk(
        0x9,
        "#01110FHey, then what is that! Is it?\x02",
    )

    CloseMessageWindow()
    OP_68(-1580, 1330, 126880, 2000)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 33)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05200FOh, that is a sand bag.\x02\x03",
            "#05204FWith sand in it\x01",
            "You can hit and kick.\x02\x03",
            "#05202FWell, it's not for full-blown fighting\x01",
            "Though it is for light training.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01103FI see.\x02\x03",
            "#01111FWell then, even if you hit it\x01",
            "You made it so that it does not hurt?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05202FSuch that.\x02\x03",
            "#05204F(But, really, it is intelligent\x01",
            "I'm getting wiser and steadier … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    Sleep(500)

    ChrTalk(
        0x9,
        "#01101F#3PWell …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-830, 1330, 126920, 2000)
    SetCameraDistance(20500, 2000)
    TurnDirection(0x101, 0x9, 500)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#05205FKeya?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "#01107F#1PLloyd ~~~ っ!\x02",
    )

    CloseMessageWindow()
    OP_68(-1760, 1330, 126770, 500)
    SetCameraDistance(19500, 500)

    def lambda_5468():
        OP_95(0xFE, -2600, 0, 127600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5468)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_549D():

        label("loc_549D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_549D")

    QueueWorkItem2(0x101, 1, lambda_549D)
    WaitChrThread(0x9, 1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x1, 0x50, 0x0, 0x8)
    Sound(811, 0, 100, 0)
    Sound(815, 0, 30, 0)
    Sound(114, 0, 40, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_9C(0x9, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    SetCameraDistance(20500, 2000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5527():
        OP_95(0xFE, -1770, 30, 126630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5527)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x9, 500)
    OP_64(0xFFFF)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#05211F#2PHey, hey.\x01",
            "Kaoru, are you all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x2)
    OP_98(0x9, 0xC8, 0x0, 0x0, 0x3E8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01109F#1PHahaha!\x01",
            "It's fun, kore!\x02\x03",
            "#01110FKa'a, maybe not!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05209F#2PHaha, that's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#05204F#2P(by the way……\x01",
            "It was also in my older brother 's room. )\x02\x03",
            "(More decky and heavy fellow\x01",
            "It hurts a lot when I hit it on a test … …)\x02\x03",
            "#05200F(Well, I'm sorry.\x01",
            "Serious things would be better? )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(200)
    OP_63(0x9, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#01102F#1PHey, when there is no Lloyd\x01",
            "Do you ask me to play with you?\x02\x03",
            "#01109FTo practice tackling\x01",
            "Looks a little expensive!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#05212F#2PIt's good, but……\x01",
            "Does not it hurt your body?\x02\x03",
            "#05204F(Hahaha … … for a while\x01",
            "Shall I use this? )\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I got everything for Lloyd's furniture!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_58B9")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_58B9")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58DA")
    ClearChrFlags(0x0, 0x8)

    label("loc_58DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58ED")
    ClearChrFlags(0x1, 0x8)

    label("loc_58ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5900")
    ClearChrFlags(0x2, 0x8)

    label("loc_5900")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5913")
    ClearChrFlags(0x3, 0x8)

    label("loc_5913")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5926")
    ClearChrFlags(0x4, 0x8)

    label("loc_5926")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5939")
    ClearChrFlags(0x5, 0x8)

    label("loc_5939")

    EventEnd(0x6)
    NewScene("c0120", 103, 0, 0)
    IdleLoop()

    label("loc_5944")

    Return()

    # Function_38_48D4 end

    def Function_39_5945(): pass

    label("Function_39_5945")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_597F")
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x9)
    Sleep(200)
    SetChrSubChip(0xFE, 0xA)
    Sleep(200)
    SetChrSubChip(0xFE, 0xB)
    Sleep(200)
    SetChrSubChip(0xFE, 0xA)
    Sleep(200)
    SetChrSubChip(0xFE, 0x9)
    Sleep(200)
    Jump("Function_39_5945")

    label("loc_597F")

    Return()

    # Function_39_5945 end

    def Function_40_5980(): pass

    label("Function_40_5980")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59BA")
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrSubChip(0xFE, 0x6)
    Sleep(200)
    SetChrSubChip(0xFE, 0x7)
    Sleep(200)
    SetChrSubChip(0xFE, 0x6)
    Sleep(200)
    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    Jump("Function_40_5980")

    label("loc_59BA")

    Return()

    # Function_40_5980 end

    def Function_41_59BB(): pass

    label("Function_41_59BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51108.itc", 0x1E)
    LoadChrToIndex("apl/ch51109.itc", 0x1F)
    SoundLoad(128)
    SoundLoad(3600)
    SoundLoad(3601)
    SoundLoad(3602)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x3)
    SetChrPos(0x9, 2550, -100, 125550, 180)
    BeginChrThread(0x9, 3, 0, 39)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 3000, 150, 125900, 180)
    OP_7D(0xDC, 0xDC, 0xDC, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "rhuton", 0x0, 0x1)
    OP_68(0, 1100, 131000, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18000, 0)
    Sound(883, 0, 70, 0)
    Sleep(2300)
    Sound(128, 2, 10, 0)
    Sleep(150)
    OP_25(0x80, 0x14)
    Sleep(150)
    OP_25(0x80, 0x1E)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#05206F#50W…… …?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(2800, 1100, 125650, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05205F#5P#40W…… It's raining today … …\x02\x03",
            "#05206FBy the way, to weekly forecast of magazines\x01",
            "It seems like it was written …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sound(3026, 255, 80, 0)

    NpcTalk(
        0x9,
        "voice",
        "#6P#60W#2S……….\x02",
    )

    CloseMessageWindow()
    OP_24(0xBD2)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x3)
    Sleep(100)
    SetChrSubChip(0x101, 0x4)
    Sleep(500)

    ChrTalk(
        0x101,
        "#05205F#5P#30WDid you mean ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16630, 700)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x0)

    def lambda_5C6C():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EA3C, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5C6C)
    SetChrSubChip(0x101, 0x5)
    Sleep(150)
    SetChrSubChip(0x101, 0x6)
    Sleep(150)
    SetChrSubChip(0x101, 0x7)
    WaitChrThread(0x9, 1)
    OP_79(0x8)
    OP_6F(0x79)
    Sleep(500)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#05206F#11P#30WKeya …\x01",
            "Have you entered again?\x02\x03",
            "#05208FRecently I did not have much\x01",
            "What's wrong……?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x3)
    Sleep(150)
    SetChrSubChip(0x9, 0x2)
    Sleep(150)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    SetChrSubChip(0x9, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        "#05813F#3600V#6P#60W…… … …………\x02",
    )

    CloseMessageWindow()
    OP_24(0xE10)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#05809F#3601V#6P#60W…… Hehe …\x01",
            "Shizuku …… Here it is … …\x02\x03",
            "#05813F#3602V#2S…… … … Mumbo … …………\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE12)
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x9, 3, 0, 40)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#05212F#11P#30WHahaha …… Shizuku\x01",
            "It looks like a dream playing.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetChrSubChip(0x101, 0x8)
    Sleep(150)
    SetChrSubChip(0x101, 0x9)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05200F#11P#30WIt's still dawn ……\x01",
            "I will sleep a little more … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetChrSubChip(0x101, 0x8)
    Sleep(150)
    SetChrSubChip(0x101, 0x7)
    Sleep(500)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#05206F#11P#30W(D∴ G Church's son …\x01",
            "Are you from the era 500 years ago? )\x02\x03",
            "#05208F(The remnants of the group are gone\x01",
            "The danger never came … …)\x02\x03",
            "#05201F(Since there are no more families anymore,\x01",
            "The one not to regain memory poorly\x01",
            "It might be nice … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x14, 0x0, 0x0, 0x0)

    def lambda_5FEF():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5FEF)

    def lambda_6009():
        OP_96(0xFE, 0xBB8, 0x96, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6009)
    SetChrSubChip(0x101, 0x7)
    Sleep(150)
    SetChrSubChip(0x101, 0x6)
    Sleep(150)
    SetChrSubChip(0x101, 0x5)
    Sleep(150)
    SetChrSubChip(0x101, 0x4)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    OP_79(0x8)
    Sleep(1800)

    ChrTalk(
        0x101,
        (
            "#05203F#11P#30W(… … Now that we are going to cross-border security\x01",
            "Let's concentrate on defending … …)\x02\x03",
            "#05201F(These kids can live with peace of mind\x01",
            "Even for defending every day … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x3)
    SetCameraDistance(17630, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    ReplaceBGM("ed7150", "ed7000")
    Sleep(1000)
    SetScenarioFlags(0x22, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_59BB end

    def Function_42_611A(): pass

    label("Function_42_611A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_61FD():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_61FD)
    Sleep(200)

    def lambda_621A():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_621A)
    Sleep(200)

    def lambda_6237():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6237)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_6272():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6272)
    Sleep(400)

    def lambda_6286():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6286)
    Sleep(400)

    def lambda_629A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_629A)

    def lambda_62AB():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62AB)
    Sleep(300)

    def lambda_62C8():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62C8)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P── Hey, Randy.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x104,
        "Hmm? What a Lloyd.\x02",
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
        (
            "#00008F#11PThat……\x01",
            "It's about your father.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, that is ……\x02\x03",
            "#00300FSomething you do not mind separately?\x01",
            "It is not uncommon in that world.\x02\x03",
            "Besides, when I left the group\x01",
            "My father and I have broken hearts.\x02\x03",
            "#00304FI do not feel anything ……\x01",
            "Well, I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P……I see.\x02\x03",
            "#00001FBut, if you feel like it\x01",
            "Please let me know a variety of things?\x02\x03",
            "Once, as a leader\x01",
            "I may be able to ride consultation\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11POh, sorry.\x01",
            "Was it a bit cheeky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHa ha, it is different.\x02\x03",
            "#00302FWhatever you say\x01",
            "I thought that you also grew.\x02\x03",
            "#00309FWell, my older brother is deeply impressed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6828")

    ChrTalk(
        0x101,
        "#00006F#11PYou know.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P…… That time, like this\x01",
            "I want you to manage it somehow.\x02\x03",
            "#00000FAlthough it may not be reliable\x01",
            "Is not it \"buddy\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd …\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_6747():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6747)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00302F… …. OK, which story\x01",
            "Perhaps it will be heard.\x02\x03",
            "#00309FThat time I will ask - ___ 0.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PAh……!\x02",
    )

    CloseMessageWindow()
    Jump("loc_68BA")

    label("loc_6828")


    ChrTalk(
        0x101,
        "#00006F#11PYou know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F… Well, if you feel like it\x01",
            "I might consult him.\x02\x03",
            "#00300FAt that time I will ask for your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PAh……!\x02",
    )

    CloseMessageWindow()

    label("loc_68BA")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Voice of Wadi",
        "#2P#2SWhat are you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Ely's voice",
        "#2P#2SBoth of them are lost articles?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_69B1")
    SetCameraDistance(22500, 700)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_6998():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6998)
    WaitChrThread(0x104, 1)

    label("loc_69B1")


    def lambda_69B6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_69B6)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, I will go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FWell then,\x01",
            "When you start working, it is all.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_6A2A():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A2A)
    Sleep(100)

    def lambda_6A47():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A47)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_6A6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6A6E)
    Sleep(400)

    def lambda_6A82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A82)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With a driving car, across the crossbell\x01",
            "It is now possible to move.\x02\x03",
            "At the back door of the Special Affairs Support Division on Nishi Dori\x01",
            "Please stop using it because it is stopped.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_42_611A end

    def Function_43_6B8E(): pass

    label("Function_43_6B8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50005.itc", 0x1E)
    LoadChrToIndex("apl/ch50091.itc", 0x1F)
    LoadChrToIndex("apl/ch50092.itc", 0x20)
    LoadChrToIndex("apl/ch50011.itc", 0x21)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis030.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    OP_68(50000, 1030, 127600, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 48600, 30, 125100, 90)
    SetChrPos(0x102, 51050, 30, 125000, 270)
    SetChrPos(0x103, 51050, 30, 126500, 225)
    SetChrPos(0x109, 50000, 0, 119000, 0)
    SetChrPos(0x105, 50000, 0, 119300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 50000, 0, 119000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 47300, 30, 126200, 135)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x1E)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 49700, 300, 125500, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x12)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 49800, 350, 125100, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    Sleep(500)
    Sound(886, 0, 80, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#00007F… … Damn it …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7567", 0)
    OP_68(50000, 1030, 125100, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Sound(18, 0, 60, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I will add a kelly.\x01",
            "See you. Randy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x103,
        "#00206F… that … … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FHere\x01",
            "Leave only the write down ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00008F…… exactly …\x01",
            "I was deceived by yesterday 's words …\x02\x03",
            "#00010FFucking … until Enigma\x01",
            "I will leave it ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01108F……… Randy …………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(103, 0, 100, 0)

    def lambda_6F6F():
        OP_96(0xFE, 0xBEA0, 0x0, 0x1E1A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F6F)

    def lambda_6F89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F89)
    Sleep(300)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_6FA5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FA5)
    Sleep(100)

    def lambda_6FB5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FB5)

    def lambda_6FC2():
        OP_96(0xFE, 0xC2EC, 0x0, 0x1E078, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6FC2)

    def lambda_6FDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6FDC)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's no good, people around me\x01",
            "It seems I have not seen it at all …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FPerhaps, in the late night without a crowd\x01",
            "I guess it went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PBut, where the hell … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00201FThe thing that comes with Keli is\x01",
            "Is it in the Mainz direction …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PAh……\x01",
            "That probability will be high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FThen we are developing in the mountain path\x01",
            "Contact from the guard ……!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    NpcTalk(
        0x8,
        "Sergei's voice",
        "#5P─ ─ It's thin, hopeful.\x02",
    )

    CloseMessageWindow()
    OP_68(50280, 1130, 123880, 1500)

    def lambda_71AF():
        OP_96(0xFE, 0xC350, 0x0, 0x1DA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_71AF)

    def lambda_71C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_71C9)
    Sleep(100)

    def lambda_71DD():

        label("loc_71DD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_71DD")

    QueueWorkItem2(0x109, 2, lambda_71DD)

    def lambda_71EF():

        label("loc_71EF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_71EF")

    QueueWorkItem2(0x101, 2, lambda_71EF)
    Sleep(100)

    def lambda_7204():

        label("loc_7204")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7204")

    QueueWorkItem2(0x105, 2, lambda_7204)

    def lambda_7216():

        label("loc_7216")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7216")

    QueueWorkItem2(0x102, 2, lambda_7216)

    def lambda_7228():

        label("loc_7228")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7228")

    QueueWorkItem2(0x103, 2, lambda_7228)

    def lambda_723A():

        label("loc_723A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_723A")

    QueueWorkItem2(0x9, 2, lambda_723A)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x101,
        "#00011F#5PManager……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#12P#01006FIt was a mess that I always messed up\x01",
            "Strangely make it pretty and go away.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(49000, 1330, 125100, 3000)
    MoveCamera(48, 23, 0, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_72F4():
        OP_95(0xFE, 48000, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72F4)
    WaitChrThread(0x8, 1)

    def lambda_7312():
        OP_95(0xFE, 46900, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7312)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x9, 0x2)

    ChrTalk(
        0x8,
        (
            "#6P#01001F… … I also contacted the guard\x01",
            "It is said that the appearance of a guy has not been confirmed.\x02\x03",
            "Probably, even if I head to Mainz\x01",
            "Do not use a real route.\x02\x03",
            "#01003FEven so, former hunter of Battle of Battle ……\x01",
            "To blind the eyes of the regular army\x01",
            "You can do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10108FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P…… a little bit about us\x01",
            "I thought you were relying on me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00208F#5P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#12P#10306FWait, see how it's going\x01",
            "You may only have a look.\x02\x03",
            "#10308FThe more military actions in mountainous areas\x01",
            "There is no field of specialty of hunting soldiers.\x02\x03",
            "#10301FAs if to chase, even clues\x01",
            "I guess they can not find it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11P─ ─ No.\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_75C1():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_75C1)
    Sleep(50)

    def lambda_75D1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_75D1)
    Sleep(50)

    def lambda_75E1():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_75E1)
    Sleep(50)

    def lambda_75F1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75F1)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    Sleep(500)

    ChrTalk(
        0x105,
        "#12P#10305FHuh……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PPerhaps Randy will also be in the evening\x01",
            "I think that I have not gone to Mainz direction.\x02\x03",
            "#00001FPossibly …\x01",
            "I am still in Crossbell City\x01",
            "There may even be possibilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#11PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FHow do you understand! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P… … It's simple.\x02\x03",
            "#00008FIf Randy is serious\x01",
            "Armed activities of \"red constellation\"\x01",
            "If you are trying to do something ……\x02\x03",
            "#00013FThe gift of now … …\x01",
            "Stanhalvard alone\x01",
            "Do you think it will manage somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10111FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206F……surely.\x01",
            "Whatever you think, there is impossibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01003FWhat I mean is that he was a hunter\x01",
            "Armed with some sort of … …\x02\x03",
            "#01001FWas it not enough to procure it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_7A82")

    ChrTalk(
        0x101,
        "#00001F#11PYes……\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "…… Well, in such a case\x01",
            "You should bring it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    VolumeBGM(0x64, 0x3E8)

    ChrTalk(
        0x101,
        (
            "#00003F#11P…… Randy is a long time ago,\x01",
            "A considerable fire power guide rifle\x01",
            "He said that he was using it.\x02\x03",
            "#00001FSomewhere in the crossbell\x01",
            "It seems to be keeping it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B65")

    label("loc_7A82")


    ChrTalk(
        0x101,
        (
            "#00003F#11PYes … think from a career\x01",
            "With considerable fire heavy weapons\x01",
            "It is not amusing to be able to communicate.\x02\x03",
            "#00008FTo procure them in the city\x01",
            "It is not impossible … ….\x02\x03",
            "#00001FSomewhere to put old goods\x01",
            "It may have been kept.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B65")


    ChrTalk(
        0x8,
        "#6P#01003Fgot it……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PWell then, in the city\x01",
            "A place he seems to drop in\x01",
            "Turn around … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00202FRandy's whereabouts\x01",
            "You may be able to locate it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102Fsurely……!\x01",
            "It seems worth investigating!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00000F#5POh, I thought so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300F…………………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F#5PWadi\x01",
            "Do you think that it is misplaced?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FNo, he …\x01",
            "I thought it was unexpected as expected.\x02\x03",
            "#10304F── It's not okay?\x01",
            "I thought it was a process by listening.\x02\x03",
            "#10300FSo, if he were to drop in\x01",
            "I wonder where in the city is suspicious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PThat's right.\x02\x03",
            "#00003F─ ─ after all around the old city\x01",
            "It might be the most doubtful.\x02\x03",
            "#00001FAshley of the exchange shop\x01",
            "We handle weapons on the back … …\x02\x03",
            "Guillaume boss\x01",
            "It seems to be detailed for handling heavy weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FThe casino's Drake owner also\x01",
            "You might know something.\x02\x03",
            "#00201FMr. Randy, frequently\x01",
            "I guess I went to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PI see …\x02\x03",
            "#00101FAnd surely, Randy\x01",
            "Since I came to Crossbell\x01",
            "I wonder if you were acquainted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01004FKuku … … It was a disaster.\x02\x03",
            "#01002FSuccessful distribution#2RUp#I meant that\x01",
            "For you, in no time\x01",
            "You will be grabbed by the tail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112FHuh, sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P…… Of course.\x02\x03",
            "#00013FThis kind of selfishness, as a leader\x01",
            "I can not forgive it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00007F#6PSomehow grasp the destination\x01",
            "I definitely have to bring them back …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00203FIt is a shrine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PYeah, even if you stretch the rope around your neck\x01",
            "Let's take home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01108F…… Randy, are you all right?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_81E5():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_81E5)
    Sleep(50)

    def lambda_81F5():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_81F5)
    Sleep(50)

    def lambda_8205():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8205)
    Sleep(50)

    def lambda_8215():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8215)
    Sleep(50)

    def lambda_8225():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8225)
    Sleep(50)

    def lambda_8235():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8235)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#11PAh……\x01",
            "Because I will definitely take home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PYeah, I do not need to worry about anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00202FKa'a with Zeit\x01",
            "Please stay on home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01122F… …. Well.\x02\x03",
            "#01121FLloyd's also ……\x01",
            "Please be careful!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7150", "ed7151")
    ReplaceBGM("ed7101", "ed7151")
    SetScenarioFlags(0x165, 5)
    SetScenarioFlags(0x23, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_6B8E end

    SaveToFile()

Try(main)
