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
        "Function_4_D4F",          # 04, 4
        "Function_5_DB9",          # 05, 5
        "Function_6_138F",         # 06, 6
        "Function_7_173B",         # 07, 7
        "Function_8_1785",         # 08, 8
        "Function_9_17D1",         # 09, 9
        "Function_10_18A3",        # 0A, 10
        "Function_11_1975",        # 0B, 11
        "Function_12_19E4",        # 0C, 12
        "Function_13_1CD1",        # 0D, 13
        "Function_14_1FE3",        # 0E, 14
        "Function_15_2203",        # 0F, 15
        "Function_16_242F",        # 10, 16
        "Function_17_249B",        # 11, 17
        "Function_18_26A7",        # 12, 18
        "Function_19_28B9",        # 13, 19
        "Function_20_2ACF",        # 14, 20
        "Function_21_2CE5",        # 15, 21
        "Function_22_2D83",        # 16, 22
        "Function_23_2E21",        # 17, 23
        "Function_24_2EBF",        # 18, 24
        "Function_25_2F72",        # 19, 25
        "Function_26_302D",        # 1A, 26
        "Function_27_30E0",        # 1B, 27
        "Function_28_319E",        # 1C, 28
        "Function_29_3253",        # 1D, 29
        "Function_30_330A",        # 1E, 30
        "Function_31_337F",        # 1F, 31
        "Function_32_33AE",        # 20, 32
        "Function_33_33DD",        # 21, 33
        "Function_34_340C",        # 22, 34
        "Function_35_343B",        # 23, 35
        "Function_36_4054",        # 24, 36
        "Function_37_4BB7",        # 25, 37
        "Function_38_4CC4",        # 26, 38
        "Function_39_5E72",        # 27, 39
        "Function_40_5EAD",        # 28, 40
        "Function_41_5EE8",        # 29, 41
        "Function_42_66D7",        # 2A, 42
        "Function_43_722E",        # 2B, 43
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2")

    ChrTalk(
        0x8,
        (
            "#01000FWith the matter of the local referendum\x01",
            "for the national independence, many\x01",
            "official papers are coming in.\x02\x03",
            "There're some subjects I'm worried about, but...\x01",
            "Well, leave the other Sections to me.\x02\x03",
            "For the present, crisis management comes first.\x01",
            "Not just the Doll Studio inquiry,\x01",
            "cover support requests too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B90")

    label("loc_AD2")


    ChrTalk(
        0x8,
        (
            "#01000FAh, if you're looking for KeA, it seems\x01",
            "she just went out to shop for dinner.\x02\x03",
            "She said she was dropping by the\x01",
            "library for a bit... Well, if\x01",
            "you're worried go check yourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B90")

    Jump("loc_D4B")

    label("loc_B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(
        0x8,
        (
            "#01000FHey, I just came back\x01",
            "from the hospital too.\x02\x03",
            "#01003FYou continue with your job, proceed\x01",
            "with the "Cryptid" investigation.\x02\x03",
            "#01002FWhile the "Divine Blade of Wind" can't act,\x01",
            "you can increase your achievements by a lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4B")

    label("loc_C98")


    ChrTalk(
        0x8,
        (
            "#01003FYou continue with your job, proceed\x01",
            "with the "Cryptid" investigation.\x02\x03",
            "#01002FWhile the "Divine Blade of Wind" can't act,\x01",
            "you can increase your achievements by a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4B")

    TalkEnd(0xFE)
    Return()

    # Function_3_976 end

    def Function_4_D4F(): pass

    label("Function_4_D4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6D")
    Call(0, 5)
    Jump("loc_DB5")

    label("loc_D6D")


    ChrTalk(
        0x9,
        (
            "#01100FGood luck, everyone.\x02\x03",
            "#01109FKeA will wait for you here...\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB5")

    TalkEnd(0xFE)
    Return()

    # Function_4_D4F end

    def Function_5_DB9(): pass

    label("Function_5_DB9")

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
        "#00100FHere you are, KeA.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x12C)

    ChrTalk(
        0x9,
        "#5P#01100FAh, yes...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "#5P#01108F...Randy...\x01",
            "I wonder how he felt\x01",
            "when he wrote that letter.\x02\x03",
            "#01103FI wonder if he intends to...\x01",
            "Not see KeA and you all again.\x02",
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
            "#10300F...Who Randy is trying to fight seems\x01",
            "to be a very powerful opponent.\x02\x03",
            "#10303FMaybe it's no wonder at all that he's challenging\x01",
            "him with the resolve to part from everything.\x02\x03",
            "#10308FHis living place, his comrades...even his life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F...As if I'd let him leave the Support\x01",
            "Section with such a selfish resolve...\x02\x03",
            "Elie, Tio, Randy...\x01",
            "Noｱl, Wazy, Chief Sergei\x01",
            "and KeA and Zeit...\x02\x03",
            "#00001FEven if only one among them is missing,\x01",
            "we aren't the "Support Section" anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FLloyd... You're right.\x02\x03",
            "#00108FWithout even trying to understand\x01",
            "something like that, he's risking\x01",
            "his own life like he pleases...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00203FYes, I think severe punishment is needed.\x02",
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
            "#12P#10100FDon't worry, KeA, ok?\x01",
            "We'll bring back senior Randy without fault!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, we also finally just\x01",
            "got a solid lead too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01110FI see...\x02\x03",
            "#01104FGood luck, everyone.\x02\x03",
            "#01109FKeA will wait for you here...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah, we'll bring back Randy\x01",
            "here without fault.\x02",
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

    # Function_5_DB9 end

    def Function_6_138F(): pass

    label("Function_6_138F")

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
            "#12P#10302FHu hu, welcome to my castle.\x01",
            "...Just kidding.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1495")

    ChrTalk(
        0x1A5,
        "#5P#01105FWow, what a pretty room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C6")

    label("loc_1495")


    ChrTalk(
        0x101,
        (
            "#5P#00005FThis is...\x01",
            "Really a stylish room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C6")


    ChrTalk(
        0x109,
        (
            "#12P#10105FF-For real...\x01",
            "Somehow only this room looks\x01",
            "like a model home or something.\x02\x03",
            "#10106FHow to say it, didn't you become\x01",
            "quite familiar a bit too fast?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYes, it also looks like\x01",
            "there's a lot of quite\x01",
            "expensive-looking furniture...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, I asked an acquaintance of mine\x01",
            "and he did me the favor to get it for me.\x02\x03",
            "#10300FWell, if you're tired I don't mind you\x01",
            "coming here to relax whenever you want.\x02\x03",
            "Since we're here, it could be nice\x01",
            "to open that bottle over there to\x01",
            "celebrate my moving in, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00006FNo, that wouldn't be good, like you can imagine...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100020, 30, 121290, 0)
    SetScenarioFlags(0x13B, 5)
    EventEnd(0x5)
    Return()

    # Function_6_138F end

    def Function_7_173B(): pass

    label("Function_7_173B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174D")
    Call(0, 12)
    Jump("loc_1784")

    label("loc_174D")

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

    label("loc_1784")

    Return()

    # Function_7_173B end

    def Function_8_1785(): pass

    label("Function_8_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1797")
    Call(0, 13)
    Jump("loc_17D0")

    label("loc_1797")

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

    label("loc_17D0")

    Return()

    # Function_8_1785 end

    def Function_9_17D1(): pass

    label("Function_9_17D1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Now that I think about it, KeA said\x01",
            "she was going to Sunday School.\x02\x03",
            "Chief has gone out too, maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_17D1 end

    def Function_10_18A3(): pass

    label("Function_10_18A3")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F...Now that I think about it, KeA said\x01",
            "she was going to Sunday School.\x02\x03",
            "Chief has gone out too, maybe it\x01",
            "would be better going out together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, let's ask her.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_18A3 end

    def Function_11_1975(): pass

    label("Function_11_1975")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FKeA is going to Sunday School.\x01",
            "Let's use the back entrance as a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1975 end

    def Function_12_19E4(): pass

    label("Function_12_19E4")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A7E")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_1A7E")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100FThis is Tio's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FShe's currently on a business trip in\x01",
            "the autonomous state of Leman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, she went with Jona\x01",
            "to the Epstein Foundation\x01",
            "research lab.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWith the state laws revised, even\x01",
            "the orbal net spreading has been\x01",
            "proceeding. They are helping with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103FI don't understand complicated things, but...\x01",
            "They seem to have it hard too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C7C")

    ChrTalk(
        0x1A5,
        "#12P#01100FI hope Tio comes home fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CB9")

    label("loc_1C7C")


    ChrTalk(
        0x101,
        (
            "#00000FYeah, it would be nice if\x01",
            "she came back quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB9")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_12_19E4 end

    def Function_13_1CD1(): pass

    label("Function_13_1CD1")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D6B")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_1D6B")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThis is Randy's room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRandy is currently in the midst\x01",
            "of rehabilitation training at\x01",
            "Tangram Gate with the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FAh, if I remember correctly, during the Cult\x01",
            "incident they were served that drug, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYes...\x01",
            "Severe after-effects\x01",
            "didn't remain though.\x02\x03",
            "#10108FTo regain stamina and their senses\x01",
            "it seems it will take some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FI see...\x01",
            "I hope the CGF recover quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F8B")

    ChrTalk(
        0x1A5,
        "#12P#01100FI wish Randy too came back home fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FCB")

    label("loc_1F8B")


    ChrTalk(
        0x102,
        (
            "#00100FRight, I'd like for Randy too\x01",
            "to come home quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCB")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_13_1CD1 end

    def Function_14_1FE3(): pass

    label("Function_14_1FE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    OP_68(-460, 1300, 127470, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_203D")
    SetChrFlags(0x0, 0x8)

    label("loc_203D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2050")
    SetChrFlags(0x1, 0x8)

    label("loc_2050")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2063")
    SetChrFlags(0x2, 0x8)

    label("loc_2063")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2076")
    SetChrFlags(0x3, 0x8)

    label("loc_2076")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2089")
    SetChrFlags(0x4, 0x8)

    label("loc_2089")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209C")
    SetChrFlags(0x5, 0x8)

    label("loc_209C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20B5")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_20B5")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -460, 0, 127470, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FMaybe here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x349, 1)
    SetScenarioFlags(0x13C, 0)
    OP_66(0x2, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2164")
    Call(0, 38)

    label("loc_2164")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2177")
    ClearChrFlags(0x0, 0x8)

    label("loc_2177")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218A")
    ClearChrFlags(0x1, 0x8)

    label("loc_218A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_219D")
    ClearChrFlags(0x2, 0x8)

    label("loc_219D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B0")
    ClearChrFlags(0x3, 0x8)

    label("loc_21B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C3")
    ClearChrFlags(0x4, 0x8)

    label("loc_21C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D6")
    ClearChrFlags(0x5, 0x8)

    label("loc_21D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21EF")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_21EF")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_14_1FE3 end

    def Function_15_2203(): pass

    label("Function_15_2203")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2269")
    SetChrFlags(0x0, 0x8)

    label("loc_2269")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227C")
    SetChrFlags(0x1, 0x8)

    label("loc_227C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228F")
    SetChrFlags(0x2, 0x8)

    label("loc_228F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A2")
    SetChrFlags(0x3, 0x8)

    label("loc_22A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B5")
    SetChrFlags(0x4, 0x8)

    label("loc_22B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C8")
    SetChrFlags(0x5, 0x8)

    label("loc_22C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22E1")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_22E1")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -2420, 30, 126860, 315)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0000FMaybe here it's fine.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Lloyd's room.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x348, 1)
    SetScenarioFlags(0x13C, 1)
    OP_66(0x3, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2390")
    Call(0, 38)

    label("loc_2390")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A3")
    ClearChrFlags(0x0, 0x8)

    label("loc_23A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B6")
    ClearChrFlags(0x1, 0x8)

    label("loc_23B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C9")
    ClearChrFlags(0x2, 0x8)

    label("loc_23C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23DC")
    ClearChrFlags(0x3, 0x8)

    label("loc_23DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23EF")
    ClearChrFlags(0x4, 0x8)

    label("loc_23EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2402")
    ClearChrFlags(0x5, 0x8)

    label("loc_2402")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_241B")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_241B")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2203 end

    def Function_16_242F(): pass

    label("Function_16_242F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you acquire furniture items,\x01",
            "you can place them in the protagonists' rooms.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_249A")

    Return()

    # Function_16_242F end

    def Function_17_249B(): pass

    label("Function_17_249B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(49580, 1330, 129410, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F5")
    SetChrFlags(0x0, 0x8)

    label("loc_24F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2508")
    SetChrFlags(0x1, 0x8)

    label("loc_2508")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_251B")
    SetChrFlags(0x2, 0x8)

    label("loc_251B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_252E")
    SetChrFlags(0x3, 0x8)

    label("loc_252E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2541")
    SetChrFlags(0x4, 0x8)

    label("loc_2541")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2554")
    SetChrFlags(0x5, 0x8)

    label("loc_2554")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_256D")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_256D")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 49580, 30, 129410, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FIs it fine here?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Randy's room.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_261B")
    ClearChrFlags(0x0, 0x8)

    label("loc_261B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_262E")
    ClearChrFlags(0x1, 0x8)

    label("loc_262E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2641")
    ClearChrFlags(0x2, 0x8)

    label("loc_2641")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2654")
    ClearChrFlags(0x3, 0x8)

    label("loc_2654")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2667")
    ClearChrFlags(0x4, 0x8)

    label("loc_2667")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_267A")
    ClearChrFlags(0x5, 0x8)

    label("loc_267A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2693")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2693")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_17_249B end

    def Function_18_26A7(): pass

    label("Function_18_26A7")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2707")
    SetChrFlags(0x0, 0x8)

    label("loc_2707")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_271A")
    SetChrFlags(0x1, 0x8)

    label("loc_271A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_272D")
    SetChrFlags(0x2, 0x8)

    label("loc_272D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2740")
    SetChrFlags(0x3, 0x8)

    label("loc_2740")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2753")
    SetChrFlags(0x4, 0x8)

    label("loc_2753")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2766")
    SetChrFlags(0x5, 0x8)

    label("loc_2766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_277F")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_277F")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52070, 30, 123440, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0300FIs it fine here?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Randy's room.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_282D")
    ClearChrFlags(0x0, 0x8)

    label("loc_282D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2840")
    ClearChrFlags(0x1, 0x8)

    label("loc_2840")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2853")
    ClearChrFlags(0x2, 0x8)

    label("loc_2853")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2866")
    ClearChrFlags(0x3, 0x8)

    label("loc_2866")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2879")
    ClearChrFlags(0x4, 0x8)

    label("loc_2879")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_288C")
    ClearChrFlags(0x5, 0x8)

    label("loc_288C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_28A5")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_28A5")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_18_26A7 end

    def Function_19_28B9(): pass

    label("Function_19_28B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(100680, 1330, 127820, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2913")
    SetChrFlags(0x0, 0x8)

    label("loc_2913")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2926")
    SetChrFlags(0x1, 0x8)

    label("loc_2926")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2939")
    SetChrFlags(0x2, 0x8)

    label("loc_2939")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_294C")
    SetChrFlags(0x3, 0x8)

    label("loc_294C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295F")
    SetChrFlags(0x4, 0x8)

    label("loc_295F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2972")
    SetChrFlags(0x5, 0x8)

    label("loc_2972")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_298B")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_298B")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 100680, 30, 127820, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        "#10300FHu hu, could here be good?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Wazy's room.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A43")
    ClearChrFlags(0x0, 0x8)

    label("loc_2A43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A56")
    ClearChrFlags(0x1, 0x8)

    label("loc_2A56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A69")
    ClearChrFlags(0x2, 0x8)

    label("loc_2A69")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7C")
    ClearChrFlags(0x3, 0x8)

    label("loc_2A7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A8F")
    ClearChrFlags(0x4, 0x8)

    label("loc_2A8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA2")
    ClearChrFlags(0x5, 0x8)

    label("loc_2AA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2ABB")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2ABB")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_19_28B9 end

    def Function_20_2ACF(): pass

    label("Function_20_2ACF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_68(101940, 1330, 125580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B29")
    SetChrFlags(0x0, 0x8)

    label("loc_2B29")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B3C")
    SetChrFlags(0x1, 0x8)

    label("loc_2B3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B4F")
    SetChrFlags(0x2, 0x8)

    label("loc_2B4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B62")
    SetChrFlags(0x3, 0x8)

    label("loc_2B62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B75")
    SetChrFlags(0x4, 0x8)

    label("loc_2B75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B88")
    SetChrFlags(0x5, 0x8)

    label("loc_2B88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BA1")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_2BA1")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 101940, 30, 125580, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x105,
        "#10300FHu hu, could here be good?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new furniture was\x01",
            "added to Wazy's room.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C59")
    ClearChrFlags(0x0, 0x8)

    label("loc_2C59")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C6C")
    ClearChrFlags(0x1, 0x8)

    label("loc_2C6C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C7F")
    ClearChrFlags(0x2, 0x8)

    label("loc_2C7F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C92")
    ClearChrFlags(0x3, 0x8)

    label("loc_2C92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CA5")
    ClearChrFlags(0x4, 0x8)

    label("loc_2CA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CB8")
    ClearChrFlags(0x5, 0x8)

    label("loc_2CB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2CD1")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2CD1")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_20_2ACF end

    def Function_21_2CE5(): pass

    label("Function_21_2CE5")

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
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D65")
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

    label("loc_2D65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D81")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2D81")

    Return()

    # Function_21_2CE5 end

    def Function_22_2D83(): pass

    label("Function_22_2D83")

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
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E03")
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

    label("loc_2E03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E1F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2E1F")

    Return()

    # Function_22_2D83 end

    def Function_23_2E21(): pass

    label("Function_23_2E21")

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
            "Quit\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA1")
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

    label("loc_2EA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBD")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2EBD")

    Return()

    # Function_23_2E21 end

    def Function_24_2EBF(): pass

    label("Function_24_2EBF")

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
            "It is the Tristan.\x02",
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

    # Function_24_2EBF end

    def Function_25_2F72(): pass

    label("Function_25_2F72")

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
            "It is a mini punching bag.\x02",
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

    # Function_25_2F72 end

    def Function_26_302D(): pass

    label("Function_26_302D")

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
            "It is a surfboard.\x02",
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

    # Function_26_302D end

    def Function_27_30E0(): pass

    label("Function_27_30E0")

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
            "It is a jukebox.\x02",
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

    # Function_27_30E0 end

    def Function_28_319E(): pass

    label("Function_28_319E")

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
            "It is a comfy chair.\x02",
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

    # Function_28_319E end

    def Function_29_3253(): pass

    label("Function_29_3253")

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
            "It is a mini aquarium.\x02",
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

    # Function_29_3253 end

    def Function_30_330A(): pass

    label("Function_30_330A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_337E")
    OP_E0(0x16, 0x0)

    label("loc_337E")

    Return()

    # Function_30_330A end

    def Function_31_337F(): pass

    label("Function_31_337F")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_31_337F end

    def Function_32_33AE(): pass

    label("Function_32_33AE")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_32_33AE end

    def Function_33_33DD(): pass

    label("Function_33_33DD")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_33_33DD end

    def Function_34_340C(): pass

    label("Function_34_340C")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_34_340C end

    def Function_35_343B(): pass

    label("Function_35_343B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4053")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis366.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis367.itp")
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 51750, 130, 125650, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_34ED")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_34ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3506")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_3506")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others returned to the\x01",
            "Support Section on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled report to HQ\x01",
            "and decided to each take their rest.\x02",
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

    def lambda_36CF():
        OP_9B(0x0, 0xFE, 0xA, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36CF)

    def lambda_36E4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36E4)
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
        "#00300FWhat is it, time to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWell, there haven't been any special\x01",
            "requests from HQ today...\x02\x03",
            "#00001F...Don't tell me that you\x01",
            "have been drinking, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F*gulp*...\x01",
            "Naah, I'd never dare.\x02\x03",
            "#00300FAlright, then let's\x01",
            "go out at once!\x02",
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
            "#00000F(Though while I say that, since he's pretty\x01",
            "honest I'm not worried that much.)\x02",
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
            "#00005FBy the way...\x01",
            "Somehow...haven't the number of things increased?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(50440, 2200, 131009, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(21000, 3000)

    def lambda_3979():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3979)
    Sleep(200)

    def lambda_3989():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3989)
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
            "#00000FThat's...\x01",
            "A surfboard, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00303FYeah, actually it's a thing you can\x01",
            "only use on coastlands, but...\x02\x03",
            "#00300FSince waves form even on Elm Lake,\x01",
            "well, why don't go havin' fun there?\x02\x03",
            "#00309FDoin' that stuff, lake surfin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FI see, it seems you like that\x01",
            "quite a lot, Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_68(50390, 2200, 122310, 4000)
    MoveCamera(60, 25, 0, 4000)
    Sleep(1500)

    def lambda_3B21():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B21)
    Sleep(200)

    def lambda_3B31():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B31)
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
            "#00005FAnd that's...\x01",
            "...What was that again?\x02\x03",
            "#00003FIt looks like something\x01",
            "I saw in a magazine once.\x02",
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
            "#00303FIf you insert a 10 mira coin it\x01",
            "performs the music you want...\x02\x03",
            "#00302FWell, it's a machine you sometimes\x01",
            "find set in dingy bars or the likes.\x02",
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
            "#00003FHow can I say...\x01",
            "It makes a really nostalgic mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FHa ha, around Crossbell I\x01",
            "haven't seen 'em at all...\x02\x03",
            "#00302FIt's rather the standard machine\x01",
            "in remote countryside's bars\x01",
            "where there're no other amusements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FIs that so...?\x02\x03",
            "#00000FWas there one in the bars\x01",
            "you were going to before?\x02",
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
            "#00304F...Ha ha, it's nothing.\x02\x03",
            "#00300FSo, aren't we goin'?\x01",
            "Milady and the others are waitin'.\x02",
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
            "You got all of Randy's furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4014")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_4014")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_402D")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_402D")

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

    label("loc_4053")

    Return()

    # Function_35_343B end

    def Function_36_4054(): pass

    label("Function_36_4054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BB6")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_410C")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_410C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4125")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_4125")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That day, Lloyd and the others returned to the\x01",
            "Support Section on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled report to HQ\x01",
            "and decided to each take their rest.\x02",
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
        "#1PWazy, are you in?\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10300FYeah, come in at will.\x02",
    )

    CloseMessageWindow()
    OP_68(98850, 1330, 122760, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_42F3():
        OP_9B(0x0, 0xFE, 0x2, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42F3)

    def lambda_4308():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4308)
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
            "#10306FOh boy.\x01",
            "Is it time to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PWell, there haven't been any special\x01",
            "requests from HQ today...\x02\x03",
            "#00005F...Wait a second, Wazy.\x01",
            "You're sitting on a nice-looking chair, hm?\x02",
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
            "#10302FYeah, it's a comfort chair\x01",
            "made in Remiferia.\x02\x03",
            "#10304FBecause it was designed based\x01",
            "on ergonomic engineering, it\x01",
            "feels really good.\x02\x03",
            "#10300FDo you want to try sitting on it?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FHuh, can I?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10309FHu hu, please.\x02",
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

    def lambda_458F():

        label("loc_458F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_458F")

    QueueWorkItem2(0x105, 1, lambda_458F)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00000FUhm, well then──\x02",
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
            "#00003F............\x01",
            "...It's amazing.\x02\x03",
            "#00004FHow can I say it, it seems it\x01",
            "envelops your body completely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, I know, right?\x02\x03",
            "#10304FWell, it's a needed device\x01",
            "since it even eliminates\x01",
            "stress in that way.\x02\x03",
            "#10309FI'm the most popular at the store, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FAbout that, at least say it heals\x01",
            "the stress of the Support Section's\x01",
            "hard duties, not your host's one...\x02\x03",
            "#00002FAh... But that fish tank is nice,\x01",
            "it can really relax you.\x02",
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
            "#00005FBy the way...\x01",
            "Are fish tanks a hobby of yours too?\x02",
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
            "#10304FWell, if pushed I'd say that\x01",
            "I missed the old times, maybe?\x02",
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
        "#00005FWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F...Hu hu, I'm just talking to myself.\x02\x03",
            "#10300FMore importantly, is it alright\x01",
            "for you to be relaxing here?\x02\x03",
            "#10309FIt doesn't bother me at all, though.\x02",
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
            "#00001FEveryone's waiting, so,\x01",
            "quick, let's go!\x02",
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
            "You got all of Wazy's furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B7D")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_4B7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B96")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_4B96")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 2)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 114, 0, 0)
    IdleLoop()

    label("loc_4BB6")

    Return()

    # Function_36_4054 end

    def Function_37_4BB7(): pass

    label("Function_37_4BB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD7")
    SetChrFlags(0x0, 0x8)

    label("loc_4BD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BEA")
    SetChrFlags(0x1, 0x8)

    label("loc_4BEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BFD")
    SetChrFlags(0x2, 0x8)

    label("loc_4BFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C10")
    SetChrFlags(0x3, 0x8)

    label("loc_4C10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C23")
    SetChrFlags(0x4, 0x8)

    label("loc_4C23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C36")
    SetChrFlags(0x5, 0x8)

    label("loc_4C36")

    ClearChrFlags(0x101, 0x8)
    Call(0, 38)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C51")
    ClearChrFlags(0x0, 0x8)

    label("loc_4C51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C64")
    ClearChrFlags(0x1, 0x8)

    label("loc_4C64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C77")
    ClearChrFlags(0x2, 0x8)

    label("loc_4C77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C8A")
    ClearChrFlags(0x3, 0x8)

    label("loc_4C8A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C9D")
    ClearChrFlags(0x4, 0x8)

    label("loc_4C9D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CB0")
    ClearChrFlags(0x5, 0x8)

    label("loc_4CB0")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_37_4BB7 end

    def Function_38_4CC4(): pass

    label("Function_38_4CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E71")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis361.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis360.itp")
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    SoundLoad(3666)
    SoundLoad(3667)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D6A")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_4D6A")

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
            "That day, Lloyd and the others returned to the\x01",
            "Support Section on a break from their duties──\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They made their scheduled report to HQ\x01",
            "and decided to each take their rest.\x02",
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
            "#05203F*sigh*...the scheduled report is over too.\x02\x03",
            "#05209FIt would be nice if I could take a\x01",
            "nap but that's not the case, I guess...\x02",
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
            "#1P#3666VHey, hey.\x01",
            "Lloyd, are you in?\x02",
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

    def lambda_50AE():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_50AE)

    def lambda_50C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_50C3)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51B3")

    ChrTalk(
        0x101,
        (
            "#05205F#1POh, KeA.\x01",
            "You were out, right?\x02\x03",
            "#05203FDid you come back briefly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01100F#2PAh, yeah.\x01",
            "I had forgotten something.\x02\x03",
            "#01109FSo, when I felt Lloyd's presence,\x01",
            "I thought you could be in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B3")

    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#01110F#2P#3667VAh...!\x01",
            "It looks like there's something new!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE53)
    OP_C9(0x1, 0x80000000)
    OP_68(-170, 1330, 125490, 4000)
    MoveCamera(45, 22, 0, 4000)

    def lambda_523A():

        label("loc_523A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_523A")

    QueueWorkItem2(0x101, 1, lambda_523A)
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
            "#05202FHa ha...\x01",
            "Are they a bit rare, like  I think?\x02\x03",
            "#05204FI guess they're things\x01",
            "you don't usually see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01109FYes!\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    OP_68(360, 1330, 128889, 2500)
    SetCameraDistance(21500, 2500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_537B():
        OP_95(0xFE, 710, 0, 127430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_537B)
    Sleep(250)

    def lambda_5398():
        OP_95(0xFE, -130, 30, 126060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5398)
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
            "#01100FThis is...the same model\x01",
            "of the car over there?\x02\x03",
            "#01103FAlthough it looks like it has a\x01",
            "different shape from an orbal airship.\x02",
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
            "#05203FIt's called "airplane", and even\x01",
            "though it doesn't use orbal power,\x01",
            "it flies the skies like a bird.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01102FEeh...\x01",
            "I'd like to ride on it.\x02\x03",
            "#01105FAh, but "fictitious" means that\x01",
            "you can't ride it for real, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05205FY-Yes, I guess.\x02\x03",
            "#05203FI think that it's normally impossible to fly\x01",
            "in the sky without using orbal energy...\x02\x03",
            "#05208F(Well...although strange, maybe\x01",
            "it has been invented somewhere?)\x02",
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
        "#01110FHey hey, then, what's that!?\x02",
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
            "#05204FThere's sand inside it and you\x01",
            "can punch it and kick it.\x02\x03",
            "#05202FWell, it's not used for real boxing, but it's\x01",
            "something you use for a light training.\x02",
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
            "#01111FThen, it's made so to not hurt\x01",
            "that much when you hit it, eh?\x02",
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
            "#05204F(Still, really, her...wisdom? Well, she's\x01",
            "becoming smarter and smarter...)\x02",
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

    def lambda_5945():
        OP_95(0xFE, -2600, 0, 127600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5945)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_597A():

        label("loc_597A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_597A")

    QueueWorkItem2(0x101, 1, lambda_597A)
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

    def lambda_5A04():
        OP_95(0xFE, -1770, 30, 126630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A04)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x9, 500)
    OP_64(0xFFFF)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#05211F#2PH-Hey now.\x01",
            "KeA, are you ok?\x02",
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
            "#01109F#1PAhaha ha!\x01",
            "This is fun!\x02\x03",
            "#01110FMaybe KeA likes it a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#05209F#2PHa ha, I see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#05204F#2P(Now that I think about it...\x01",
            "Wasn't there one in big brother's room too?)\x02\x03",
            "(One bigger and heavier, that when I\x01",
            "tried to punch it, it hurted a lot...)\x02\x03",
            "#05200F(Uhhm, since it's used for that, could\x01",
            "a regular one be better, perhaps?)\x02",
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
            "#01102F#1PHey hey, can KeA play with it\x01",
            "when you aren't here, Lloyd?\x02\x03",
            "#01109FIt seems very nice to\x01",
            "train for tackles!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#05212F#2PAlright...\x01",
            "As long as you don't hurt yourself, ok?\x02\x03",
            "#05204F(Ha ha... I guess I'll be\x01",
            "using this for a little while.)\x02",
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
            "You got all of Lloyd's furniture!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5DE6")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_5DE6")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E07")
    ClearChrFlags(0x0, 0x8)

    label("loc_5E07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E1A")
    ClearChrFlags(0x1, 0x8)

    label("loc_5E1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E2D")
    ClearChrFlags(0x2, 0x8)

    label("loc_5E2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E40")
    ClearChrFlags(0x3, 0x8)

    label("loc_5E40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E53")
    ClearChrFlags(0x4, 0x8)

    label("loc_5E53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E66")
    ClearChrFlags(0x5, 0x8)

    label("loc_5E66")

    EventEnd(0x6)
    NewScene("c0120", 103, 0, 0)
    IdleLoop()

    label("loc_5E71")

    Return()

    # Function_38_4CC4 end

    def Function_39_5E72(): pass

    label("Function_39_5E72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EAC")
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
    Jump("Function_39_5E72")

    label("loc_5EAC")

    Return()

    # Function_39_5E72 end

    def Function_40_5EAD(): pass

    label("Function_40_5EAD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EE7")
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
    Jump("Function_40_5EAD")

    label("loc_5EE7")

    Return()

    # Function_40_5EAD end

    def Function_41_5EE8(): pass

    label("Function_41_5EE8")

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
        "#05206F#50W...Hmm...?\x02",
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
            "#05205F#5P#40W...Today is raining...?\x02\x03",
            "#05206FNow that I think about it, it seems it was\x01",
            "written on the weekly weather report...\x02",
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
        "#6P#60W#2S...Hmm......\x02",
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
        "#05205F#5P#30WCould it be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16630, 700)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x0)

    def lambda_61B6():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EA3C, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_61B6)
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
            "#05206F#11P#30WKeA...\x01",
            "She snuck in again?\x02\x03",
            "#05208FShe didn't do it at all as of late,\x01",
            "could something have happened...?\x02",
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
        "#05813F#3600V#6P#60W...Uhhm...\x02",
    )

    CloseMessageWindow()
    OP_24(0xE10)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#05809F#3601V#6P#60W...Ehehe...\x01",
            "Shizuku...over here...\x02\x03",
            "#05813F#3602V#2S...hmm...mumble mumble...\x02",
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
            "#05212F#11P#30WHa ha...it seems she's having a dream\x01",
            "where she's playing with Shizuku.\x02",
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
            "#05200F#11P#30WIt's still dawn...\x01",
            "I guess I'll sleep a bit more too...\x02",
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
            "#05206F#11P#30W(The D∴G Cult's Divine Child...\x01",
            "From an era of 500 years ago.)\x02\x03",
            "#05208F(With the Cult's remnants vanishing, even\x01",
            "the danger befalling on her has disappeared...)\x02\x03",
            "#05201F(She hasn't got any family anymore and\x01",
            "maybe it would be better not getting\x01",
            "back her memories ineptly, but...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x14, 0x0, 0x0, 0x0)

    def lambda_6594():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6594)

    def lambda_65AE():
        OP_96(0xFE, 0xBB8, 0x96, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65AE)
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
            "#05203F#11P#30W(...I'll devote myself to protect\x01",
            "Crossbell peace for now...)\x02\x03",
            "#05201F(In order to protect every day where\x01",
            "these children can live in peace too...)\x02",
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

    # Function_41_5EE8 end

    def Function_42_66D7(): pass

    label("Function_42_66D7")

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

    def lambda_67BA():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_67BA)
    Sleep(200)

    def lambda_67D7():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_67D7)
    Sleep(200)

    def lambda_67F4():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_67F4)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_682F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_682F)
    Sleep(400)

    def lambda_6843():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6843)
    Sleep(400)

    def lambda_6857():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6857)

    def lambda_6868():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6868)
    Sleep(300)

    def lambda_6885():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6885)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P──Say, Randy.\x02",
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
        "Uhm? What, Lloyd.\x02",
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
            "#00008F#11PYou know...\x01",
            "About your father...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306FAh, that...\x01\x02\x03",
            "#00300FI don't particularly mind it, you know?\x01",
            "It's no rare story in that kind of world.\x02\x03",
            "Also, when I broke away from the group,\x01",
            "I severed ties with my ol' man.\x02\x03",
            "#00304FIt doesn't mean I didn't feel anything, but...\x01",
            "Well, I felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I see.\x02\x03",
            "#00001FHowever, when you feel like it,\x01",
            "you can tell me everything, okay?\x02\x03",
            "After all, as the leader\x01",
            "there could be things I\x01",
            "can you advice on.\x02",
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
            "#00011F#11PAh, sorry.\x01",
            "Was I a bit impertinent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FHa ha, no, no.\x02\x03",
            "#00302FAll things considered, I\x01",
            "thought you've grown up too.\x02\x03",
            "#00309FHmm, your big bro here is deeply moved.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6E6B")

    ChrTalk(
        0x101,
        "#00006F#11PHey now...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P...It's just...that I'd want to be\x01",
            "of help to you in such moments.\x02\x03",
            "#00000FMaybe I'm not so reliable, but that's\x01",
            "what means to be "buddies", right?\x02",
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

    def lambda_6D6C():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6D6C)
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
            "#6P#00302F...Alright, got it. Maybe one\x01",
            "day I'll tell you everything.\x02\x03",
            "#00309FI'll count on you when that time comes──buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11PYeah...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F06")

    label("loc_6E6B")


    ChrTalk(
        0x101,
        "#00006F#11PHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...Well, if I feel like it I\x01",
            "could ask you for advice.\x02\x03",
            "#00300FI'll count on you, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PYeah...!\x02",
    )

    CloseMessageWindow()

    label("loc_6F06")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "Wazy's Voice",
        "#2P#2SOh, what're you doing?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Elie's Voice",
        "#2P#2SDid you forget something?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_700E")
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

    def lambda_6FF5():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6FF5)
    WaitChrThread(0x104, 1)

    label("loc_700E")


    def lambda_7013():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7013)

    ChrTalk(
        0x101,
        "#00011F#11PSorry, we'll be there immediately!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304FAlright then, let's begin our\x01",
            "work in a nice and relaxed way.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_70A7():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_70A7)
    Sleep(100)

    def lambda_70C4():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_70C4)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_70EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_70EB)
    Sleep(400)

    def lambda_70FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70FF)
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
            "You are now able to move everywhere\x01",
            "in Crossbell via orbal car.\x02\x03",
            "It is parked at the Special Support Section back\x01",
            "entrance facing West Street. Please try using it.\x07\x00\x02",
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

    # Function_42_66D7 end

    def Function_43_722E(): pass

    label("Function_43_722E")

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
        "#00007F...Shit...!\x02",
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
            "I went to set things once and for all.\x01",
            "See ya.                          Randy\x07\x00\x02",
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
            "#00106FLeaving behind only\x01",
            "s-such a note...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00008F...He completely...\x01",
            "Fooled us with his words, yesterday...\x02\x03",
            "#00010FDamn... He even left\x01",
            "behind his ENIGMA...\x02",
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

    def lambda_762B():
        OP_96(0xFE, 0xBEA0, 0x0, 0x1E1A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_762B)

    def lambda_7645():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7645)
    Sleep(300)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_7661():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7661)
    Sleep(100)

    def lambda_7671():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7671)

    def lambda_767E():
        OP_96(0xFE, 0xC2EC, 0x0, 0x1E078, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_767E)

    def lambda_7698():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7698)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt's no good, the people in the neighborhood\x01",
            "appear to not have seen him around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FHe probably went out deep at night\x01",
            "when there's no people around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#5PB-But where could he have...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00201FThat "to set things once and for all",\x01",
            "could it be referring to the Mainz area...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah...\x01",
            "It's very likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10107FThen, a communication from the CGF\x01",
            "deployed on the mountain path could arr...!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    NpcTalk(
        0x8,
        "Sergei's Voice",
        "#5P──That's a dim hope.\x02",
    )

    CloseMessageWindow()
    OP_68(50280, 1130, 123880, 1500)

    def lambda_78C7():
        OP_96(0xFE, 0xC350, 0x0, 0x1DA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_78C7)

    def lambda_78E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_78E1)
    Sleep(100)

    def lambda_78F5():

        label("loc_78F5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_78F5")

    QueueWorkItem2(0x109, 2, lambda_78F5)

    def lambda_7907():

        label("loc_7907")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7907")

    QueueWorkItem2(0x101, 2, lambda_7907)
    Sleep(100)

    def lambda_791C():

        label("loc_791C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_791C")

    QueueWorkItem2(0x105, 2, lambda_791C)

    def lambda_792E():

        label("loc_792E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_792E")

    QueueWorkItem2(0x102, 2, lambda_792E)

    def lambda_7940():

        label("loc_7940")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7940")

    QueueWorkItem2(0x103, 2, lambda_7940)

    def lambda_7952():

        label("loc_7952")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7952")

    QueueWorkItem2(0x9, 2, lambda_7952)
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
            "#12P#01006FJeez, although he always leave things scattered\x01",
            "around he strangely tidied up and went his way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(49000, 1330, 125100, 3000)
    MoveCamera(48, 23, 0, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_7A2C():
        OP_95(0xFE, 48000, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7A2C)
    WaitChrThread(0x8, 1)

    def lambda_7A4A():
        OP_95(0xFE, 46900, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7A4A)
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
            "#6P#01001F...I inquired the CGF too but it seems\x01",
            "they didn't catch sight of him.\x02\x03",
            "I guess that, although he's heading to Mainz,\x01",
            "he's not using a proper route.\x02\x03",
            "#01003FDespite appearances, he's a former veteran jaeger...\x01",
            "Deceiving a regular army?\x01",
            "He could do it as much as he likes.\x02",
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
            "#00106F#11P...Although I thought he trusted\x01",
            "us at least a little bit...\x02",
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
            "#12P#10306F...Well, I think we can only observe\x01",
            "how the situation goes for a little while.\x02\x03",
            "#10308FWe aren't jaegers specialists, less\x01",
            "of military movements on mountains.\x02\x03",
            "#10301FEven if we chased after him, I think\x01",
            "we wouldn't be able to find even a clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11P...No.\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7D65():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7D65)
    Sleep(50)

    def lambda_7D75():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7D75)
    Sleep(50)

    def lambda_7D85():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7D85)
    Sleep(50)

    def lambda_7D95():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7D95)
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
            "#00006F#5PI think that Randy didn't go to\x01",
            "the Mainz region during night.\x02\x03",
            "#00001FPerhaps...\x01",
            "It's even possible that he's\x01",
            "still in Crossbell City.\x02",
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
        "#12P#10105FHow can you tell!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...It's simple.\x02\x03",
            "#00008FIf Randy had been serious to\x01",
            "try to do something armed\x01",
            "against the "Red Constellation"...\x02\x03",
            "#00013FDo you think that he could do\x01",
            "something just with his current\x01",
            "specialized weapon, a Stunhalberd?\x02",
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
            "#5P#00206F...You have a point.\x01",
            "It would be unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01003FSo you're saying that he's\x01",
            "gone first to get something...\x02\x03",
            "#01001FWhatever weapon he was using in his jaeger days?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_825B")

    ChrTalk(
        0x101,
        "#00001F#11PYes...  \x02",
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
            "...Dang, in this case I wish\x01",
            "I had brought that with me.\x02",
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
            "#00003F#11P...Randy was saying that in the\x01",
            "past he used an orbal rifle with\x01",
            "quite the firepower.\x02\x03",
            "#00001FIt seems he has stored it\x01",
            "somewhere in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8371")

    label("loc_825B")


    ChrTalk(
        0x101,
        (
            "#00003F#11PYes... thinking about his personal\x01",
            "history it's no wonder he's used to\x01",
            "heavy weapons with a lot of firepower.\x02\x03",
            "#00008FStocking up on those it's not\x01",
            "impossible at all in the city...\x02\x03",
            "#00001FIt's also possible that he was keeping\x01",
            "his specialized weapon somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8371")


    ChrTalk(
        0x8,
        "#6P#01003FI see your point...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#11PT-Then, if we tour around\x01",
            "the places where he could\x01",
            "likely stop by in the city...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00202FWe could ascertain where\x01",
            "Mr. Randy is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10102FIndeed...!\x01",
            "It seems worthy to look into this!\x02",
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
            "#00001F#5PWazy...\x01",
            "Do you think my guess is wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FNo, hu hu...\x01",
            "I think it's really unexpected.\x02\x03",
            "#10304F──Why not? I thought that could\x01",
            "be the case, while I was listening.\x02\x03",
            "#10300FSo, if he has to stop somewhere, couldn't\x01",
            "it be a fishy place in the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PRight...\x02\x03",
            "#00003F──Like I thought, the one in the Downtown\x01",
            "environs is the fishiest one.\x02\x03",
            "#00001FMiss Ashley, the exchanger, \x01",
            "deals also in weapons...\x02\x03",
            "Somehow Master Guillaume too is\x01",
            "knowledgeable in heavy weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FOwner Drake of the casino\x01",
            "could also know something.\x02\x03",
            "#00201FIt seems that Mr. Randy was\x01",
            "constantly going there to have fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PYou're right...\x02\x03",
            "#00101FAlso, if I remember correctly,\x01",
            "isn't he someone Randy has\x01",
            "known since he came to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#01004FEh he...how unfortunate he is.\x02\x03",
            "#01002FHe wanted to scatter you well,\x01",
            "but it's going to be caught by\x01",
            "you all in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10112FUh uh, true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Of course.\x02\x03",
            "#00013FI can't, also as the leader, \x01",
            "forgive such selfishness.\x02",
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
            "#00007F#6PWe'll figure out where he is\x01",
            "and take him back for sure...!\x02",
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
            "#00107F#11PYes, let's bring him back even if\x01",
            "by putting a rope around his neck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#01108F...Is Randy going to be okay?\x02",
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

    def lambda_8A85():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A85)
    Sleep(50)

    def lambda_8A95():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8A95)
    Sleep(50)

    def lambda_8AA5():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8AA5)
    Sleep(50)

    def lambda_8AB5():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8AB5)
    Sleep(50)

    def lambda_8AC5():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8AC5)
    Sleep(50)

    def lambda_8AD5():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8AD5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x8, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#11PYeah...\x01",
            "We'll absolutely bring him back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PYes, you don't need to worry about anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00202FKeA, please house sit\x01",
            "together with Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#01122F...Yes.\x02\x03",
            "#01121FLloyd, guys...\x01",
            "Be very careful!\x02",
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

    # Function_43_722E end

    SaveToFile()

Try(main)
