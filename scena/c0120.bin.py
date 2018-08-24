from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Chief Sergei",           # 1
        "KeA",                    # 2
        "手紙",                   # 3
        "エニグマ",               # 4
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
        "Function_4_D27",          # 04, 4
        "Function_5_D8E",          # 05, 5
        "Function_6_1315",         # 06, 6
        "Function_7_164D",         # 07, 7
        "Function_8_1697",         # 08, 8
        "Function_9_16E3",         # 09, 9
        "Function_10_1794",        # 0A, 10
        "Function_11_1845",        # 0B, 11
        "Function_12_18B4",        # 0C, 12
        "Function_13_1B91",        # 0D, 13
        "Function_14_1E75",        # 0E, 14
        "Function_15_2090",        # 0F, 15
        "Function_16_22B7",        # 10, 16
        "Function_17_2323",        # 11, 17
        "Function_18_2539",        # 12, 18
        "Function_19_2755",        # 13, 19
        "Function_20_2968",        # 14, 20
        "Function_21_2B7B",        # 15, 21
        "Function_22_2C1B",        # 16, 22
        "Function_23_2CBB",        # 17, 23
        "Function_24_2D5B",        # 18, 24
        "Function_25_2E0D",        # 19, 25
        "Function_26_2EC7",        # 1A, 26
        "Function_27_2F79",        # 1B, 27
        "Function_28_3036",        # 1C, 28
        "Function_29_30EA",        # 1D, 29
        "Function_30_31A0",        # 1E, 30
        "Function_31_3215",        # 1F, 31
        "Function_32_3244",        # 20, 32
        "Function_33_3273",        # 21, 33
        "Function_34_32A2",        # 22, 34
        "Function_35_32D1",        # 23, 35
        "Function_36_3EAA",        # 24, 36
        "Function_37_49FB",        # 25, 37
        "Function_38_4B08",        # 26, 38
        "Function_39_5C90",        # 27, 39
        "Function_40_5CCB",        # 28, 40
        "Function_41_5D06",        # 29, 41
        "Function_42_6478",        # 2A, 42
        "Function_43_6F7E",        # 2B, 43
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x349, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    Event(0, 14)

    label("loc_551")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x348, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_578")
    Event(0, 15)

    label("loc_578")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    Event(0, 37)

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34F, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E0")
    Event(0, 18)

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34E, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    Event(0, 17)

    label("loc_607")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    Event(0, 20)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABA")

    ChrTalk(
        0x8,
        (
            "#01000FMany official papers are coming in\x01",
            "regarding the independence referendum.\x02\x03",
            "There're some cases I'm worried about,\x01",
            "but... Well, we'll leave them to the\x01",
            "other sections.\x02\x03",
            "For now, crisis management takes\x01",
            "priority. Cover not just the Doll Studio\x01",
            "inquiry, but your support requests too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B87")

    label("loc_ABA")


    ChrTalk(
        0x8,
        (
            "#01000FAh, if you're looking for KeA, it seems\x01",
            "she just went out to shop for dinner.\x02\x03",
            "She said she was dropping by the library\x01",
            "for a bit... Well, if you're worried\x01",
            "about her, go check for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B87")

    Jump("loc_D23")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C81")

    ChrTalk(
        0x8,
        (
            "#01000FHey, I just came back from the\x01",
            "hospital myself.\x02\x03",
            "#01003FContinue with the Cryptids\x01",
            "investigation.\x02\x03",
            "#01002FWhile the Divine Blade of Wind is\x01",
            "out of commission, increase your\x01",
            "achievements as much as you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D23")

    label("loc_C81")


    ChrTalk(
        0x8,
        (
            "#01003FContinue with the Cryptids\x01",
            "investigation.\x02\x03",
            "#01002FWhile the Divine Blade of Wind is\x01",
            "out of commission, increase your\x01",
            "achievements as much as you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D23")

    TalkEnd(0xFE)
    Return()

    # Function_3_976 end

    def Function_4_D27(): pass

    label("Function_4_D27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D45")
    Call(0, 5)
    Jump("loc_D8A")

    label("loc_D45")


    ChrTalk(
        0x9,
        (
            "#01100FGood luck, everyone.\x02\x03",
            "#01109FKeA will wait for you\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8A")

    TalkEnd(0xFE)
    Return()

    # Function_4_D27 end

    def Function_5_D8E(): pass

    label("Function_5_D8E")

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
        (
            "#00100FKeA... So this is where\x01",
            "you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x12C)

    ChrTalk(
        0x9,
        "#5P#01100FAh, yeah...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#5P#01108F...I wonder how Randy\x01",
            "was feeling when he\x01",
            "wrote that letter.\x02\x03",
            "#01103FIt was as if he'll never\x01",
            "see us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00205FKeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FIt's because Randy is\x01",
            "fighting too powerful an\x01",
            "opponent.\x02\x03",
            "#10303FIt's understandable that\x01",
            "Randy's prepared to throw\x01",
            "away everything to face them.\x02\x03",
            "#10308FHis home, his friends... even\x01",
            "his very life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F...As if I'd let him leave\x01",
            "the Support Section with\x01",
            "such a selfish resolve.\x02\x03",
            "Elie, Tio, Randy... Noｱl,\x01",
            "Wazy, Chief Sergei and KeA\x01",
            "and Zeit...\x02\x03",
            "#00001FEven if only one among them\x01",
            "is missing, we aren't the\x01",
            ""Support Section" anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FLloyd... You're right.\x02\x03",
            "#00108FNot understanding that,\x01",
            "he went and put his own\x01",
            "life on the line...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FYes, I think severe\x01",
            "punishment is needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#01108F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FDon't worry, ok KeA?\x01",
            "We'll bring Randy back\x01",
            "without fail!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe, and we finally\x01",
            "have a solid lead on him\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01110FI see...\x02\x03",
            "#01104FGood luck, everyone.\x02\x03",
            "#01109FKeA will wait for you\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah, we'll bring Randy\x01",
            "back here without fail.\x02",
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

    # Function_5_D8E end

    def Function_6_1315(): pass

    label("Function_6_1315")

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
            "#12P#10302FHaha, welcome to my\x01",
            "castle. ...Just kidding.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141A")

    ChrTalk(
        0x1A5,
        "#5P#01105FWow, what a pretty room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1449")

    label("loc_141A")


    ChrTalk(
        0x101,
        (
            "#5P#00005FThis is... a very\x01",
            "stylish room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1449")


    ChrTalk(
        0x109,
        (
            "#12P#10105FR-Really... This room\x01",
            "looks like a model home\x01",
            "or something.\x02\x03",
            "#10106FHow to say it... Haven't\x01",
            "you settled in a bit too\x01",
            "quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FAnd you have a\x01",
            "collection of expensive\x01",
            "furniture as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHaha. An acquaintance of mine\x01",
            "got it for me.\x02\x03",
            "#10300FAnyway, feel free to come here\x01",
            "to relax whenever you like.\x02\x03",
            "Since we're here, why not\x01",
            "celebrate my move-in by opening\x01",
            "that bottle over there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FNo. I'm telling you,\x01",
            "it's out of the\x01",
            "question.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100020, 30, 121290, 0)
    SetScenarioFlags(0x13B, 5)
    EventEnd(0x5)
    Return()

    # Function_6_1315 end

    def Function_7_164D(): pass

    label("Function_7_164D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    Call(0, 12)
    Jump("loc_1696")

    label("loc_165F")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Tio's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1696")

    Return()

    # Function_7_164D end

    def Function_8_1697(): pass

    label("Function_8_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A9")
    Call(0, 13)
    Jump("loc_16E2")

    label("loc_16A9")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is Randy's room.\x01",
            "Let's not enter.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_16E2")

    Return()

    # Function_8_1697 end

    def Function_9_16E3(): pass

    label("Function_9_16E3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Oh yeah, KeA said she\x01",
            "was leaving for Sunday\x01",
            "School.\x02\x03",
            "Chief is out, so maybe\x01",
            "we should leave\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_16E3 end

    def Function_10_1794(): pass

    label("Function_10_1794")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Oh yeah, KeA said she\x01",
            "was leaving for Sunday\x01",
            "School.\x02\x03",
            "Chief is out, so maybe\x01",
            "we should leave\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FRight, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_1794 end

    def Function_11_1845(): pass

    label("Function_11_1845")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeA is going to Sunday\x01",
            "School. Let's use the rear\x01",
            "entrance as a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1845 end

    def Function_12_18B4(): pass

    label("Function_12_18B4")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_194E")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_194E")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FShe's working in Lｳman\x01",
            "State, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, she went to the\x01",
            "Epstein Foundation\x01",
            "research lab with Jona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith recent revisions to state law, development\x01",
            "of the orbal net has been proceeding. I wonder\x01",
            "if their trip is related to helping with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI don't understand complicated\x01",
            "things, but... They seem to\x01",
            "have it hard too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B4B")

    ChrTalk(
        0x1A5,
        (
            "#12P#01100FI hope Tio comes home\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B79")

    label("loc_1B4B")


    ChrTalk(
        0x101,
        (
            "#00000FYeah, I hope Tio comes\x01",
            "home soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B79")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_12_18B4 end

    def Function_13_1B91(): pass

    label("Function_13_1B91")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C2B")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_1C2B")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is in the middle of\x01",
            "rehabilitation training at\x01",
            "Tangram Gate with the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FAh, they were dosed with\x01",
            "that drug in the cult\x01",
            "incident, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYes... There were no\x01",
            "severe aftereffects,\x01",
            "though.\x02\x03",
            "#10108FIt will take some time\x01",
            "for them to recover their\x01",
            "stamina and senses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see... I hope the CGF\x01",
            "recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(
        0x1A5,
        (
            "#12P#01100FI hope Randy comes home\x01",
            "soon, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, seriously.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E5D")

    label("loc_1E26")


    ChrTalk(
        0x102,
        (
            "#00100FYes. I hope Randy comes\x01",
            "home soon as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5D")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_13_1B91 end

    def Function_14_1E75(): pass

    label("Function_14_1E75")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    OP_68(-460, 1300, 127470, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ECF")
    SetChrFlags(0x0, 0x8)

    label("loc_1ECF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE2")
    SetChrFlags(0x1, 0x8)

    label("loc_1EE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF5")
    SetChrFlags(0x2, 0x8)

    label("loc_1EF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F08")
    SetChrFlags(0x3, 0x8)

    label("loc_1F08")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1B")
    SetChrFlags(0x4, 0x8)

    label("loc_1F1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F2E")
    SetChrFlags(0x5, 0x8)

    label("loc_1F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F47")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_1F47")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -460, 0, 127470, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FMaybe here's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x349, 1)
    SetScenarioFlags(0x13C, 0)
    OP_66(0x2, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF1")
    Call(0, 38)

    label("loc_1FF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2004")
    ClearChrFlags(0x0, 0x8)

    label("loc_2004")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2017")
    ClearChrFlags(0x1, 0x8)

    label("loc_2017")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_202A")
    ClearChrFlags(0x2, 0x8)

    label("loc_202A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_203D")
    ClearChrFlags(0x3, 0x8)

    label("loc_203D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2050")
    ClearChrFlags(0x4, 0x8)

    label("loc_2050")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2063")
    ClearChrFlags(0x5, 0x8)

    label("loc_2063")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_207C")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_207C")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_14_1E75 end

    def Function_15_2090(): pass

    label("Function_15_2090")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F6")
    SetChrFlags(0x0, 0x8)

    label("loc_20F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2109")
    SetChrFlags(0x1, 0x8)

    label("loc_2109")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_211C")
    SetChrFlags(0x2, 0x8)

    label("loc_211C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_212F")
    SetChrFlags(0x3, 0x8)

    label("loc_212F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2142")
    SetChrFlags(0x4, 0x8)

    label("loc_2142")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2155")
    SetChrFlags(0x5, 0x8)

    label("loc_2155")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_216E")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_216E")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -2420, 30, 126860, 315)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FMaybe here's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x348, 1)
    SetScenarioFlags(0x13C, 1)
    OP_66(0x3, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2218")
    Call(0, 38)

    label("loc_2218")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222B")
    ClearChrFlags(0x0, 0x8)

    label("loc_222B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_223E")
    ClearChrFlags(0x1, 0x8)

    label("loc_223E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2251")
    ClearChrFlags(0x2, 0x8)

    label("loc_2251")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2264")
    ClearChrFlags(0x3, 0x8)

    label("loc_2264")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2277")
    ClearChrFlags(0x4, 0x8)

    label("loc_2277")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228A")
    ClearChrFlags(0x5, 0x8)

    label("loc_228A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22A3")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_22A3")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2090 end

    def Function_16_22B7(): pass

    label("Function_16_22B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2322")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you acquire furniture\x01",
            "items, you can place them\x01",
            "in the protagonists' rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_2322")

    Return()

    # Function_16_22B7 end

    def Function_17_2323(): pass

    label("Function_17_2323")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(49580, 1330, 129410, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_237D")
    SetChrFlags(0x0, 0x8)

    label("loc_237D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2390")
    SetChrFlags(0x1, 0x8)

    label("loc_2390")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A3")
    SetChrFlags(0x2, 0x8)

    label("loc_23A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B6")
    SetChrFlags(0x3, 0x8)

    label("loc_23B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C9")
    SetChrFlags(0x4, 0x8)

    label("loc_23C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23DC")
    SetChrFlags(0x5, 0x8)

    label("loc_23DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_23F5")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_23F5")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 49580, 30, 129410, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#0300FIf wonder if here's\x01",
            "alright.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Randy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34E, 1)
    SetScenarioFlags(0x13C, 2)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AD")
    ClearChrFlags(0x0, 0x8)

    label("loc_24AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C0")
    ClearChrFlags(0x1, 0x8)

    label("loc_24C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D3")
    ClearChrFlags(0x2, 0x8)

    label("loc_24D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E6")
    ClearChrFlags(0x3, 0x8)

    label("loc_24E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F9")
    ClearChrFlags(0x4, 0x8)

    label("loc_24F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250C")
    ClearChrFlags(0x5, 0x8)

    label("loc_250C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2525")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2525")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_17_2323 end

    def Function_18_2539(): pass

    label("Function_18_2539")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2599")
    SetChrFlags(0x0, 0x8)

    label("loc_2599")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AC")
    SetChrFlags(0x1, 0x8)

    label("loc_25AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25BF")
    SetChrFlags(0x2, 0x8)

    label("loc_25BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D2")
    SetChrFlags(0x3, 0x8)

    label("loc_25D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E5")
    SetChrFlags(0x4, 0x8)

    label("loc_25E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F8")
    SetChrFlags(0x5, 0x8)

    label("loc_25F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2611")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_2611")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52070, 30, 123440, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#0300FIf wonder if here's\x01",
            "alright.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Randy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34F, 1)
    SetScenarioFlags(0x13C, 3)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C9")
    ClearChrFlags(0x0, 0x8)

    label("loc_26C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26DC")
    ClearChrFlags(0x1, 0x8)

    label("loc_26DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26EF")
    ClearChrFlags(0x2, 0x8)

    label("loc_26EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2702")
    ClearChrFlags(0x3, 0x8)

    label("loc_2702")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2715")
    ClearChrFlags(0x4, 0x8)

    label("loc_2715")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2728")
    ClearChrFlags(0x5, 0x8)

    label("loc_2728")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2741")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2741")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_18_2539 end

    def Function_19_2755(): pass

    label("Function_19_2755")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(100680, 1330, 127820, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27AF")
    SetChrFlags(0x0, 0x8)

    label("loc_27AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C2")
    SetChrFlags(0x1, 0x8)

    label("loc_27C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D5")
    SetChrFlags(0x2, 0x8)

    label("loc_27D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E8")
    SetChrFlags(0x3, 0x8)

    label("loc_27E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27FB")
    SetChrFlags(0x4, 0x8)

    label("loc_27FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280E")
    SetChrFlags(0x5, 0x8)

    label("loc_280E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2827")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_2827")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 100680, 30, 127820, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, could here be\x01",
            "good?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Wazy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x13C, 4)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28DC")
    ClearChrFlags(0x0, 0x8)

    label("loc_28DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28EF")
    ClearChrFlags(0x1, 0x8)

    label("loc_28EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2902")
    ClearChrFlags(0x2, 0x8)

    label("loc_2902")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2915")
    ClearChrFlags(0x3, 0x8)

    label("loc_2915")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2928")
    ClearChrFlags(0x4, 0x8)

    label("loc_2928")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_293B")
    ClearChrFlags(0x5, 0x8)

    label("loc_293B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2954")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2954")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_19_2755 end

    def Function_20_2968(): pass

    label("Function_20_2968")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_68(101940, 1330, 125580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C2")
    SetChrFlags(0x0, 0x8)

    label("loc_29C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29D5")
    SetChrFlags(0x1, 0x8)

    label("loc_29D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E8")
    SetChrFlags(0x2, 0x8)

    label("loc_29E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FB")
    SetChrFlags(0x3, 0x8)

    label("loc_29FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0E")
    SetChrFlags(0x4, 0x8)

    label("loc_2A0E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A21")
    SetChrFlags(0x5, 0x8)

    label("loc_2A21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A3A")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_2A3A")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 101940, 30, 125580, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#10300FHehe, could here be\x01",
            "good?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New furniture was added\x01",
            "to Wazy's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x13C, 5)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AEF")
    ClearChrFlags(0x0, 0x8)

    label("loc_2AEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B02")
    ClearChrFlags(0x1, 0x8)

    label("loc_2B02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B15")
    ClearChrFlags(0x2, 0x8)

    label("loc_2B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B28")
    ClearChrFlags(0x3, 0x8)

    label("loc_2B28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B3B")
    ClearChrFlags(0x4, 0x8)

    label("loc_2B3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B4E")
    ClearChrFlags(0x5, 0x8)

    label("loc_2B4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B67")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2B67")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_20_2968 end

    def Function_21_2B7B(): pass

    label("Function_21_2B7B")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFD")
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

    label("loc_2BFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C19")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2C19")

    Return()

    # Function_21_2B7B end

    def Function_22_2C1B(): pass

    label("Function_22_2C1B")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C9D")
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

    label("loc_2C9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CB9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2CB9")

    Return()

    # Function_22_2C1B end

    def Function_23_2CBB(): pass

    label("Function_23_2CBB")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest Here\x01",      # 0
            "Cancel\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3D")
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

    label("loc_2D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D59")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2D59")

    Return()

    # Function_23_2CBB end

    def Function_24_2D5B(): pass

    label("Function_24_2D5B")

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
            "It's the Tristan.\x02",
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

    # Function_24_2D5B end

    def Function_25_2E0D(): pass

    label("Function_25_2E0D")

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
            "It's a mini punching\x01",
            "bag.\x02",
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

    # Function_25_2E0D end

    def Function_26_2EC7(): pass

    label("Function_26_2EC7")

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
            "It's a surfboard.\x02",
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

    # Function_26_2EC7 end

    def Function_27_2F79(): pass

    label("Function_27_2F79")

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
            "It's a jukebox.\x02",
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

    # Function_27_2F79 end

    def Function_28_3036(): pass

    label("Function_28_3036")

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
            "It's a comfy chair.\x02",
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

    # Function_28_3036 end

    def Function_29_30EA(): pass

    label("Function_29_30EA")

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
            "It's a mini aquarium.\x02",
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

    # Function_29_30EA end

    def Function_30_31A0(): pass

    label("Function_30_31A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3214")
    OP_E0(0x16, 0x0)

    label("loc_3214")

    Return()

    # Function_30_31A0 end

    def Function_31_3215(): pass

    label("Function_31_3215")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_31_3215 end

    def Function_32_3244(): pass

    label("Function_32_3244")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_32_3244 end

    def Function_33_3273(): pass

    label("Function_33_3273")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_33_3273 end

    def Function_34_32A2(): pass

    label("Function_34_32A2")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_34_32A2 end

    def Function_35_32D1(): pass

    label("Function_35_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA9")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis366.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis367.itp")
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 51750, 130, 125650, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3383")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3383")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_339C")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_339C")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others\x01",
            "returned to the Support Section\x01",
            "on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled\x01",
            "report to HQ and decided\x01",
            "to each take their rest.\x02",
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
        "Lloyd's Voice",
        "#1PRandy, can I?\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00300FYeah, come in.\x02",
    )

    CloseMessageWindow()
    OP_68(49870, 1300, 123830, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_3565():
        OP_9B(0x0, 0xFE, 0xA, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3565)

    def lambda_357A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_357A)
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
        "#00300FWhat, time to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, there haven't been\x01",
            "any special requests\x01",
            "from HQ today...\x02\x03",
            "#00001F...Don't tell me you've\x01",
            "been drinking, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F*gulp*... Naah, I'd\x01",
            "never dare.\x02\x03",
            "#00300FAlright, then let's go\x01",
            "out at once!\x02",
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
            "#00006FHonestly...\x02\x03",
            "#00000F(Although I say that,\x01",
            "since he's pretty honest\x01",
            "I'm not all that worried.)\x02",
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
            "#00005FBy the way... Hasn't the\x01",
            "stuff in here\x01",
            "multiplied, somehow?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(50440, 2200, 131009, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(21000, 3000)

    def lambda_37F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37F9)
    Sleep(200)

    def lambda_3809():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3809)
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
            "#00000FThat's... A surfboard,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00303FYeah. Actually, you can\x01",
            "only use them on the\x01",
            "coast, but...\x02\x03",
            "#00300FSince waves form even on\x01",
            "Elm Lake, well, why not\x01",
            "go have some fun there?\x02\x03",
            "#00309FLake surfin', I mean.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FI see, it seems you like\x01",
            "that quite a lot, Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_68(50390, 2200, 122310, 4000)
    MoveCamera(60, 25, 0, 4000)
    Sleep(1500)

    def lambda_3990():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3990)
    Sleep(200)

    def lambda_39A0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39A0)
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
            "#00005FAnd that's... ...What's\x01",
            "it called again?\x02\x03",
            "#00003FIt looks like something\x01",
            "I saw in a magazine\x01",
            "once.\x02",
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
            "#00303FIf you insert a 10 mira\x01",
            "coin it plays the music\x01",
            "you want...\x02\x03",
            "#00302FWell, it's a machine you\x01",
            "sometimes find in dingy\x01",
            "bars and the like.\x02",
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
            "#00004F...This is nice.\x02\x03",
            "#00003FHow can I say... It\x01",
            "makes me feel really\x01",
            "nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHaha. I haven't seen 'em at\x01",
            "all around Crossbell...\x02\x03",
            "#00302FIt's a standard machine in\x01",
            "countryside bars where\x01",
            "there's no other amusements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FSo that's how it is.\x02\x03",
            "#00000FWas there one in the\x01",
            "bars you went to before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, more or less.\x02\x03",
            "#00303F............\x02",
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
            "#00304F...Haha, it's nothing.\x02\x03",
            "#00300FSo, are we goin'? Milady\x01",
            "and the others are\x01",
            "waitin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's go.\x02",
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
            "Collected all of Randy's\x01",
            "furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E6A")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_3E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E83")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_3E83")

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

    label("loc_3EA9")

    Return()

    # Function_35_32D1 end

    def Function_36_3EAA(): pass

    label("Function_36_3EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49FA")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F62")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3F62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F7B")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_3F7B")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others\x01",
            "returned to the Support Section\x01",
            "on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled\x01",
            "report to HQ and decided\x01",
            "to each take their rest.\x02",
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
        "Lloyd's Voice",
        "#1PWazy, you there?\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10300FYeah, do come in.\x02",
    )

    CloseMessageWindow()
    OP_68(98850, 1330, 122760, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_4143():
        OP_9B(0x0, 0xFE, 0x2, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4143)

    def lambda_4158():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4158)
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
            "#10306FOh man. Isn't it about\x01",
            "time to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PWell, there haven't been any\x01",
            "special requests from HQ\x01",
            "today...\x02\x03",
            "#00005F...Wait a second, Wazy.\x01",
            "That's a nice-looking chair\x01",
            "you're sitting on, isn't it?\x02",
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
            "#10302FYeah, it's a comfort\x01",
            "chair made in Remiferia.\x02\x03",
            "#10304FBecause the design is\x01",
            "based on ergonomics, it\x01",
            "feels really good.\x02\x03",
            "#10300FWant to give it a try?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FOh, can I?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10309FHehe, please do.\x02",
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

    def lambda_43DE():

        label("loc_43DE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_43DE")

    QueueWorkItem2(0x105, 1, lambda_43DE)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FUmm, well then─\x02",
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
            "#00005FAh...\x02\x03",
            "#00003F............ ...It's\x01",
            "amazing.\x02\x03",
            "#00004FHow can I say it, it\x01",
            "seems like it envelops\x01",
            "your body completely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. I know, right?\x02\x03",
            "#10304FWell, it's a needed\x01",
            "device since it even\x01",
            "eliminates your stress.\x02\x03",
            "#10309FI'm the store's best\x01",
            "customer, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAbout that, let's just say it heals the\x01",
            "fatigue from your hard Support Section\x01",
            "duties, and not your host ones...\x02\x03",
            "#00002FAh... But that fish tank is nice. It's\x01",
            "really relaxing.\x02",
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
            "#00005FBy the way... Are fish\x01",
            "tanks another hobby of\x01",
            "yours?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10305FYeah...\x02\x03",
            "#10304FWell if pushed, I'd say\x01",
            "that I miss the old\x01",
            "times, maybe?\x02",
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
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F...Hehe, I'm just\x01",
            "talking to myself.\x02\x03",
            "#10300FMore importantly, is it\x01",
            "alright for you to be\x01",
            "relaxing here?\x02\x03",
            "#10309FIt doesn't bother me at\x01",
            "all, though.\x02",
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
            "#00011FO-Oh, that's right!\x02\x03",
            "#00001FEveryone's waiting, so\x01",
            "let's hurry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FOk, leader.\x02",
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
            "Collected all of Wazy's\x01",
            "furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49C1")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_49C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49DA")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_49DA")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 2)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 114, 0, 0)
    IdleLoop()

    label("loc_49FA")

    Return()

    # Function_36_3EAA end

    def Function_37_49FB(): pass

    label("Function_37_49FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A1B")
    SetChrFlags(0x0, 0x8)

    label("loc_4A1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A2E")
    SetChrFlags(0x1, 0x8)

    label("loc_4A2E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A41")
    SetChrFlags(0x2, 0x8)

    label("loc_4A41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A54")
    SetChrFlags(0x3, 0x8)

    label("loc_4A54")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A67")
    SetChrFlags(0x4, 0x8)

    label("loc_4A67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A7A")
    SetChrFlags(0x5, 0x8)

    label("loc_4A7A")

    ClearChrFlags(0x101, 0x8)
    Call(0, 38)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A95")
    ClearChrFlags(0x0, 0x8)

    label("loc_4A95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AA8")
    ClearChrFlags(0x1, 0x8)

    label("loc_4AA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ABB")
    ClearChrFlags(0x2, 0x8)

    label("loc_4ABB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ACE")
    ClearChrFlags(0x3, 0x8)

    label("loc_4ACE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AE1")
    ClearChrFlags(0x4, 0x8)

    label("loc_4AE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AF4")
    ClearChrFlags(0x5, 0x8)

    label("loc_4AF4")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_37_49FB end

    def Function_38_4B08(): pass

    label("Function_38_4B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C8F")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis361.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis360.itp")
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    SoundLoad(3666)
    SoundLoad(3667)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4BAE")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_4BAE")

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
            "That day, Lloyd and the others\x01",
            "returned to the Support Section\x01",
            "on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled\x01",
            "report to HQ and decided\x01",
            "to each take their rest.\x02",
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
            "#05203F*sigh*... The scheduled\x01",
            "report is over too.\x02\x03",
            "#05209FIt would be nice if I could\x01",
            "take a nap but that's not\x01",
            "the case, I guess...\x02",
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
        "KeA's Voice",
        (
            "#1P#3666VHey Lloyd, are you\x01",
            "there?\x02",
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
        "#05202FYeah, I am.\x02",
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

    def lambda_4EF0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4EF0)

    def lambda_4F05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4F05)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FEB")

    ChrTalk(
        0x101,
        (
            "#05205F#1POh, KeA. You were out,\x01",
            "right?\x02\x03",
            "#05203FStopping back home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01100F#2PAh, yeah. I had\x01",
            "forgotten something.\x02\x03",
            "#01109FAnd when I felt your\x01",
            "presence, I thought you\x01",
            "might be in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FEB")

    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#01110F#2P#3667VAh! There's more stuff\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE53)
    OP_C9(0x1, 0x80000000)
    OP_68(-170, 1330, 125490, 4000)
    MoveCamera(45, 22, 0, 4000)

    def lambda_5063():

        label("loc_5063")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5063")

    QueueWorkItem2(0x101, 1, lambda_5063)
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
            "#05202FHaha... I guess they're\x01",
            "a bit rare.\x02\x03",
            "#05204FThey're things you don't\x01",
            "usually see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FYeah!\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    OP_68(360, 1330, 128889, 2500)
    SetCameraDistance(21500, 2500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_5194():
        OP_95(0xFE, 710, 0, 127430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5194)
    Sleep(250)

    def lambda_51B1():
        OP_95(0xFE, -130, 30, 126060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51B1)
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
            "#01105F???\x02\x03",
            "#01100FThis is... The same\x01",
            "model of car over there?\x02\x03",
            "#01103FAlthough it looks like\x01",
            "it has a different shape\x01",
            "from an airship.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05200FYeah, this is a fictitious vehicle\x01",
            "that appears in a comic.\x02\x03",
            "#05203FIt's called an "airplane", and even\x01",
            "though it doesn't use orbal power, it\x01",
            "flies through the skies like a bird.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01102FWow... I'd like to ride\x01",
            "on it.\x02\x03",
            "#01105FAh, but "fictitious"\x01",
            "means that you can't\x01",
            "ride it for real, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05205FY-Yeah, I guess.\x02\x03",
            "#05203FI think that it's normally\x01",
            "impossible to fly in the sky\x01",
            "without using orbal energy...\x02\x03",
            "#05208F(Well... Maybe, unexpectedly,\x01",
            "someone has developed one\x01",
            "somewhere?)\x02",
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
        "#01110FHey, then, what's that!?\x02",
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
            "#05200FAh, that's a sandbag.\x02\x03",
            "#05204FThere's sand inside and you\x01",
            "can punch and kick it.\x02\x03",
            "#05202FWell, it's not used for real\x01",
            "boxing, but it's something\x01",
            "you use for light training.\x02",
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
            "#01111FSo, it's made to not\x01",
            "hurt so much when you\x01",
            "hit it, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05202FThat's right.\x02\x03",
            "#05204F(Still, I don't know if you\x01",
            "could call it wisdom, but she's\x01",
            "getting smarter and smarter...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    Sleep(500)

    ChrTalk(
        0x9,
        "#01101F#3PAaalright...\x02",
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
        "#05205FKeA?\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        "#01107F#1PLloyyyyd!\x02",
    )

    CloseMessageWindow()
    OP_68(-1760, 1330, 126770, 500)
    SetCameraDistance(19500, 500)

    def lambda_5765():
        OP_95(0xFE, -2600, 0, 127600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5765)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_579A():

        label("loc_579A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_579A")

    QueueWorkItem2(0x101, 1, lambda_579A)
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

    def lambda_5824():
        OP_95(0xFE, -1770, 30, 126630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5824)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x9, 500)
    OP_64(0xFFFF)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#05211F#2PH-Hey now. KeA, are you\x01",
            "ok?\x02",
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
            "#01109F#1PAhahaha! This is fun!\x02\x03",
            "#01110FKeA likes it a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05209F#2PHaha, is that right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#05204F#2P(Now that I think about\x01",
            "it... Wasn't there one in\x01",
            "Guy's room too?)\x02\x03",
            "(A bigger and heavier one,\x01",
            "that hurt a lot when I\x01",
            "tried punching it...)\x02\x03",
            "#05200F(Hmm. Since it's my room\x01",
            "and all. I wonder if a\x01",
            "real one would be better?)\x02",
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
            "#01102F#1PHey, can KeA play with\x01",
            "it when you're not here,\x01",
            "Lloyd?\x02\x03",
            "#01109FIt seems like it'd be\x01",
            "good training for\x01",
            "tackles!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#05212F#2PAlright... As long as\x01",
            "you don't hurt yourself,\x01",
            "ok?\x02\x03",
            "#05204F(Haha... I guess I'll be\x01",
            "using this one for a\x01",
            "while longer.)\x02",
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
            "Collected all of Lloyd's\x01",
            "furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5C04")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_5C04")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C25")
    ClearChrFlags(0x0, 0x8)

    label("loc_5C25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C38")
    ClearChrFlags(0x1, 0x8)

    label("loc_5C38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C4B")
    ClearChrFlags(0x2, 0x8)

    label("loc_5C4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C5E")
    ClearChrFlags(0x3, 0x8)

    label("loc_5C5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C71")
    ClearChrFlags(0x4, 0x8)

    label("loc_5C71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C84")
    ClearChrFlags(0x5, 0x8)

    label("loc_5C84")

    EventEnd(0x6)
    NewScene("c0120", 103, 0, 0)
    IdleLoop()

    label("loc_5C8F")

    Return()

    # Function_38_4B08 end

    def Function_39_5C90(): pass

    label("Function_39_5C90")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CCA")
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
    Jump("Function_39_5C90")

    label("loc_5CCA")

    Return()

    # Function_39_5C90 end

    def Function_40_5CCB(): pass

    label("Function_40_5CCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D05")
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
    Jump("Function_40_5CCB")

    label("loc_5D05")

    Return()

    # Function_40_5CCB end

    def Function_41_5D06(): pass

    label("Function_41_5D06")

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
        "#05206F#50WHmm?\x02",
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
            "#05205F#5P#40WIt's raining?\x02\x03",
            "#05206FI guess that was in the\x01",
            "weekly forecast...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sound(3026, 255, 80, 0)

    NpcTalk(
        0x9,
        "Voice",
        "#6P#60W#2SHmm~...\x02",
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
        "#05205F#5P#30WCould it be...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16630, 700)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x0)

    def lambda_5F98():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EA3C, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F98)
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
            "#05206F#11P#30WKeA... So you snuck in\x01",
            "again, huh.\x02\x03",
            "#05208FYou haven't done that\x01",
            "much lately. Is\x01",
            "something wrong?\x02",
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
        "#05813F#3600V#6P#60W...Mmm~...\x02",
    )

    CloseMessageWindow()
    OP_24(0xE10)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#05809F#3601V#6P#60W...Ehehe... Shizukuuu...\x01",
            "This waaay!...\x02\x03",
            "#05813F#3602V#2S...Mmm... *mumble*...\x02",
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
            "#05212F#11P#30WHaha... Looks like a\x01",
            "dream where she's\x01",
            "playing with Shizuku.\x02",
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
            "#05200F#11P#30WIt's still before\x01",
            "dawn... I guess I'll\x01",
            "sleep a bit more...\x02",
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
            "#05206F#11P#30W(The D∴G Cult's divine child...\x01",
            "From 500 years ago.)\x02\x03",
            "#05208F(The cult survivors are gone,\x01",
            "so she should be in no\x01",
            "danger...)\x02\x03",
            "#05201F(She has no family, so it might\x01",
            "be better not to forcibly\x01",
            "recover her memories, but...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x14, 0x0, 0x0, 0x0)

    def lambda_632D():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_632D)

    def lambda_6347():
        OP_96(0xFE, 0xBB8, 0x96, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6347)
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
            "#05203F#11P#30W(...For now, I'll devote\x01",
            "myself to protecting order\x01",
            "in Crossbell...)\x02\x03",
            "#05201F(And for protecting the\x01",
            "daily lives where these kids\x01",
            "can live without fear...)\x02",
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

    # Function_41_5D06 end

    def Function_42_6478(): pass

    label("Function_42_6478")

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

    def lambda_655B():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_655B)
    Sleep(200)

    def lambda_6578():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6578)
    Sleep(200)

    def lambda_6595():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6595)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_65D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_65D0)
    Sleep(400)

    def lambda_65E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_65E4)
    Sleep(400)

    def lambda_65F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_65F8)

    def lambda_6609():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6609)
    Sleep(300)

    def lambda_6626():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6626)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P...Say, Randy.\x02",
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
        "Huh? What's up Lloyd.\x02",
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
            "#00008F#11PYou know... About your\x01",
            "father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh, that...\x02\x03",
            "#00300FI don't particularly mind,\x01",
            "you know? It's not a rare\x01",
            "story in that world.\x02\x03",
            "And when I left the group,\x01",
            "I cut ties with my old\x01",
            "man.\x02\x03",
            "#00304FIt's not like I didn't\x01",
            "feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I see.\x02\x03",
            "#00001FBut if you do ever feel\x01",
            "like it, you can always\x01",
            "talk to me about it.\x02\x03",
            "As leader, I might be\x01",
            "able to advise you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11PAh, sorry. Was that too\x01",
            "pushy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHaha, no, no.\x02\x03",
            "#00302FI was just thinking that\x01",
            "you've grown up too, all\x01",
            "things considered.\x02\x03",
            "#00309FHmm, your big bro here\x01",
            "is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6BDA")

    ChrTalk(
        0x101,
        "#00006F#11PNow look here...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P...It's just, I want to\x01",
            "help you in times like\x01",
            "these.\x02\x03",
            "#00000FMaybe I'm not so reliable,\x01",
            "but that's what means to\x01",
            "be "buddies", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305FLloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_6ADF():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6ADF)
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
            "#6P#00302F...Alright, got it.\x01",
            "Maybe one day I'll tell\x01",
            "you everything.\x02\x03",
            "#00309FI'll count on you when\x01",
            "that time comes─ buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C7D")

    label("loc_6BDA")


    ChrTalk(
        0x101,
        "#00006F#11PNow look here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Well, if I do feel\x01",
            "like it, I might ask for\x01",
            "advice.\x02\x03",
            "#00300FI'll be counting on you\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah!\x02",
    )

    CloseMessageWindow()

    label("loc_6C7D")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        (
            "#2P#2SHuh, what are you guys\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        (
            "#2P#2SDid you forget\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6D8C")
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

    def lambda_6D73():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6D73)
    WaitChrThread(0x104, 1)

    label("loc_6D8C")


    def lambda_6D91():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6D91)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FAlright then, let's make\x01",
            "steady progress.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_6DFD():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6DFD)
    Sleep(100)

    def lambda_6E1A():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E1A)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_6E41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6E41)
    Sleep(400)

    def lambda_6E55():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E55)
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
            "You can now go anywhere in Crossbell\x01",
            "State via orbal car.\x02\x03",
            "It is parked at the Support Section's\x01",
            "rear entrance on West Street, so\x01",
            "please make good use of it.\x07\x00\x02",
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

    # Function_42_6478 end

    def Function_43_6F7E(): pass

    label("Function_43_6F7E")

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
        "#00007FShit!\x02",
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
            "I went to settle things once and for all.\x01",
            "See ya.\x01",
            "    Randy\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x103,
        "#00206F...No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00106FJ-Just leaving a note\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00008F...He completely...\x01",
            "fooled us with his words\x01",
            "yesterday, huh...\x02\x03",
            "#00010FDamn... He even left his\x01",
            "ENIGMA...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x9,
        "#01108F...Randy...\x02",
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

    def lambda_735E():
        OP_96(0xFE, 0xBEA0, 0x0, 0x1E1A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_735E)

    def lambda_7378():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7378)
    Sleep(300)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_7394():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7394)
    Sleep(100)

    def lambda_73A4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_73A4)

    def lambda_73B1():
        OP_96(0xFE, 0xC2EC, 0x0, 0x1E078, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_73B1)

    def lambda_73CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_73CB)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's no good, the people\x01",
            "in the area haven't seen\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FHe probably went out late\x01",
            "at night when there were\x01",
            "no people around, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PB-But where could he\x01",
            "have...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00201FThat "to settle things once\x01",
            "and for all". Could it be\x01",
            "referring to the Mainz area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PYeah... That's likely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FThen, a communication from\x01",
            "the CGF deployed on the\x01",
            "mountain path could arr...!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    NpcTalk(
        0x8,
        "Sergei's Voice",
        "#5P─That's unlikely.\x02",
    )

    CloseMessageWindow()
    OP_68(50280, 1130, 123880, 1500)

    def lambda_75E0():
        OP_96(0xFE, 0xC350, 0x0, 0x1DA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_75E0)

    def lambda_75FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_75FA)
    Sleep(100)

    def lambda_760E():

        label("loc_760E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_760E")

    QueueWorkItem2(0x109, 2, lambda_760E)

    def lambda_7620():

        label("loc_7620")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7620")

    QueueWorkItem2(0x101, 2, lambda_7620)
    Sleep(100)

    def lambda_7635():

        label("loc_7635")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7635")

    QueueWorkItem2(0x105, 2, lambda_7635)

    def lambda_7647():

        label("loc_7647")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7647")

    QueueWorkItem2(0x102, 2, lambda_7647)

    def lambda_7659():

        label("loc_7659")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7659")

    QueueWorkItem2(0x103, 2, lambda_7659)

    def lambda_766B():

        label("loc_766B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_766B")

    QueueWorkItem2(0x9, 2, lambda_766B)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x101,
        "#00011F#5PChief...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#12P#01006FMan. He cleaned up his\x01",
            "usual mess and left.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(49000, 1330, 125100, 3000)
    MoveCamera(48, 23, 0, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_7711():
        OP_95(0xFE, 48000, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7711)
    WaitChrThread(0x8, 1)

    def lambda_772F():
        OP_95(0xFE, 46900, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_772F)
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
            "#6P#01001F...I asked the CGF too but they haven't\x01",
            "spotted him.\x02\x03",
            "Even if he is headed for Mainz, he's\x01",
            "probably not using any kind of normal\x01",
            "route.\x02\x03",
            "#01003FDespite appearances, he's a former\x01",
            "veteran jaeger... Deceiving a regular\x01",
            "army? He could do it as much as he likes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10108FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P...I thought he relied\x01",
            "on us at least a\x01",
            "little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00208F#5P............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#12P#10306F...Well, I guess all we can\x01",
            "do is wait-and-see for a\x01",
            "while, huh.\x02\x03",
            "#10308FWe're nowhere near as\x01",
            "skilled as jaegers with\x01",
            "mountain combat operations.\x02\x03",
            "#10301FEven if we chased after\x01",
            "him, I don't think we'd\x01",
            "find any clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11P...No.\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7A17():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7A17)
    Sleep(50)

    def lambda_7A27():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7A27)
    Sleep(50)

    def lambda_7A37():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A37)
    Sleep(50)

    def lambda_7A47():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7A47)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    Sleep(500)

    ChrTalk(
        0x105,
        "#12P#10305FHuh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PMost likely, Randy\x01",
            "didn't go to Mainz last\x01",
            "night.\x02\x03",
            "#00001FIt's even possible that\x01",
            "he's still in Crossbell\x01",
            "City.\x02",
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
        "#00105F#11PWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FHow do you know!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...It's simple.\x02\x03",
            "#00008FIf Randy is seriously trying\x01",
            "to take up arms or something\x01",
            "against Red Constellation...\x02\x03",
            "#00013FDo you really think he'd be\x01",
            "able to do anything with his\x01",
            "current Stunhalberd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10111FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00206F...You have a point. No\x01",
            "matter how you think about\x01",
            "it, that would be irrational.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01003FThere was that weapon he\x01",
            "used in his jaeger\x01",
            "days...\x02\x03",
            "#01001FGetting that would've\x01",
            "come first.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_7EEB")

    ChrTalk(
        0x101,
        "#00001F#11PRight...\x02",
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
            "...Dang, if this is how\x01",
            "it is, I wish I had\x01",
            "brought "that" with me.\x02",
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
            "#00003F#11P...Randy said he used an\x01",
            "orbal rifle with considerable\x01",
            "firepower in the past.\x02\x03",
            "#00001FIt seems he stashed it\x01",
            "somewhere in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8018")

    label("loc_7EEB")


    ChrTalk(
        0x101,
        (
            "#00003F#11PYes... thinking about his personal\x01",
            "history, it's no surprise he's used to\x01",
            "heavy weapons with a lot of firepower.\x02\x03",
            "#00008FGetting your hands on weapons like\x01",
            "that in the city isn't impossible in\x01",
            "the slightest.\x02\x03",
            "#00001FIt's also possible that he was keeping\x01",
            "his special weapon somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8018")


    ChrTalk(
        0x8,
        "#6P#01003FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PT-Then, if we visit\x01",
            "places in the city he\x01",
            "likely visited...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00202FWe might be able to find\x01",
            "where Randy has gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FIndeed! It seems worth\x01",
            "looking into!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        "#00000F#5PYeah, I think so too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300F............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#00001F#5PWazy... Do you think I'm\x01",
            "off the mark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FNo, hehe... I was just\x01",
            "thinking it's unexpected.\x02\x03",
            "#10304F─Well why not? That's what\x01",
            "I thought while I was\x01",
            "listening.\x02\x03",
            "#10300FSo, if he stopped by\x01",
            "somewhere, couldn't it be\x01",
            "a shady place in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PRight...\x02\x03",
            "#00003F─Downtown might be the\x01",
            "shadiest place in the\x01",
            "city.\x02\x03",
            "#00001FAshley of the Exchange\x01",
            "Shop deals in weapons\x01",
            "under the table...\x02\x03",
            "And Master Guillaume seems\x01",
            "knowledgeable in heavy\x01",
            "weapons too, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FOwner Drake of the\x01",
            "casino may know\x01",
            "something as well.\x02\x03",
            "#00201FIt seems Randy was\x01",
            "always going there to\x01",
            "enjoy himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PYou're right...\x02\x03",
            "#00101FAlso, if I remember correctly,\x01",
            "hasn't Randy known him ever\x01",
            "since he came to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01004FHehe... I almost feel bad for\x01",
            "him.\x02\x03",
            "#01002FHe tried to throw you off, but\x01",
            "you guys are going to catch\x01",
            "him in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112FHaha, certainly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Of course.\x02\x03",
            "#00013FAs the leader as well, I\x01",
            "can't forgive such\x01",
            "selfishness.\x02",
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
            "#00007F#6PWe'll find him and bring\x01",
            "him back for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00203FNaturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PYes. We'll bring him back\x01",
            "even if we have to tie a\x01",
            "rope around his neck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01108F...Is Randy going to be\x01",
            "okay?\x02",
        )
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

    def lambda_86E9():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_86E9)
    Sleep(50)

    def lambda_86F9():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_86F9)
    Sleep(50)

    def lambda_8709():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8709)
    Sleep(50)

    def lambda_8719():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8719)
    Sleep(50)

    def lambda_8729():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8729)
    Sleep(50)

    def lambda_8739():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8739)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah... We'll definitely\x01",
            "bring him back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PYes, you don't need to\x01",
            "worry about anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00202FKeA, please watch the\x01",
            "place with Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01122F...Okay.\x02\x03",
            "#01121FLloyd, guys... Be very\x01",
            "careful, ok!?\x02",
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

    # Function_43_6F7E end

    SaveToFile()

Try(main)
