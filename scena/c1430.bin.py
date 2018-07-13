from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1430.bin",                # FileName
        "c1430",                    # MapName
        "c1430",                    # Location
        0x0032,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 50, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1430",                  # 0
        "Master Guillaume",       # 1
        "Chief Roberts",          # 2
        "Abbas",                  # 3
    ))

    AddCharChip((
        "chr/ch26400.itc",                   # 00
        "chr/ch06700.itc",                   # 01
        "chr/ch29300.itc",                   # 02
    ))

    DeclNpc(5619,    0,       5329,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294916017, 0,       15350,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)

    DeclActor(4150,    0,       4740,    1000,    5620,    1500,    5330,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(376, 0)                                        # 0

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_3D2",          # 02, 2
        "Function_3_466",          # 03, 3
        "Function_4_46A",          # 04, 4
        "Function_5_514",          # 05, 5
        "Function_6_830",          # 06, 6
        "Function_7_2389",         # 07, 7
        "Function_8_2A0B",         # 08, 8
        "Function_9_2B69",         # 09, 9
        "Function_10_32F9",        # 0A, 10
        "Function_11_3D77",        # 0B, 11
        "Function_12_42BF",        # 0C, 12
        "Function_13_42C9",        # 0D, 13
        "Function_14_4732",        # 0E, 14
        "Function_15_4EBC",        # 0F, 15
        "Function_16_5438",        # 10, 16
        "Function_17_5BF8",        # 11, 17
        "Function_18_610F",        # 12, 18
        "Function_19_62FF",        # 13, 19
        "Function_20_6413",        # 14, 20
        "Function_21_6D7A",        # 15, 21
        "Function_22_6F93",        # 16, 22
        "Function_23_750C",        # 17, 23
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B0"),
        (1, "loc_1BC"),
        (2, "loc_1C8"),
        (3, "loc_1D4"),
        (4, "loc_1E0"),
        (5, "loc_1EC"),
        (6, "loc_1F8"),
        (SWITCH_DEFAULT, "loc_204"),
    )


    label("loc_1B0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1BC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1C8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1D4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1E0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1EC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_204")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_227")

    Return()

    # Function_0_178 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_236")
    Jump("loc_3D1")

    label("loc_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_244")
    Jump("loc_3D1")

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_252")
    Jump("loc_3D1")

    label("loc_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D3")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_2AC")
    SetChrPos(0x8, 13130, 1000, 6290, 180)
    SetChrPos(0xA, 15170, 1000, 8560, 90)
    Jump("loc_2CE")

    label("loc_2AC")

    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0xA, 15240, 1000, 9210, 180)

    label("loc_2CE")

    Jump("loc_2E4")

    label("loc_2D3")

    SetChrPos(0x8, 15240, 1000, 7610, 90)

    label("loc_2E4")

    Jump("loc_3D1")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F7")
    Jump("loc_3D1")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_3D1")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_324")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_3D1")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_332")
    Jump("loc_3D1")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_340")
    Jump("loc_3D1")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34E")
    Jump("loc_3D1")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_3D1")

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_396")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0x9, 15240, 1000, 9210, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3D1")

    label("loc_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3B1")

    Jump("loc_3D1")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3D1")

    Return()

    # Function_1_228 end

    def Function_2_3D2(): pass

    label("Function_2_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4")
    OP_65(0x0, 0x1)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F6")
    OP_65(0x0, 0x1)

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408")
    OP_65(0x0, 0x1)

    label("loc_408")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_421")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_427")

    label("loc_421")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_427")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44E")
    Sound(128, 1, 50, 0)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_465")

    Return()

    # Function_2_3D2 end

    def Function_3_466(): pass

    label("Function_3_466")

    Call(0, 4)
    Return()

    # Function_3_466 end

    def Function_4_46A(): pass

    label("Function_4_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C")
    Call(0, 15)
    Return()

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_499")
    TalkBegin(0x8)
    Call(0, 8)
    TalkEnd(0x8)
    Return()

    label("loc_499")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C3")
    Call(0, 17)
    Return()

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    TalkBegin(0x8)
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
    Call(0, 9)
    Return()

    label("loc_50A")

    TalkBegin(0x8)
    Call(0, 5)
    TalkEnd(0x8)
    Return()

    # Function_4_46A end

    def Function_5_514(): pass

    label("Function_5_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Talk")
    MenuCmd(1, 0, "Remodel")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E")
    MenuCmd(1, 0, "Give U-Material")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8")
    MenuCmd(1, 0, "Ask About Metal Detector")

    label("loc_5B8")

    MenuCmd(1, 0, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5F7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_61B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63E")
    OP_AF(0xAD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_667")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_667")
    Call(0, 21)
    Return()

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Return()

    label("loc_69A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A9")

    label("loc_6A9")

    Jump("loc_53E")

    label("loc_6AE")

    Jump("loc_82F")

    label("loc_6B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_720")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",             # 0
            "Remodel\x01",          # 1
            "Make Weapon\x01",      # 2
            "Quit\x01",             # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_757")

    label("loc_720")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",         # 0
            "Remodel\x01",      # 1
            "Quit\x01",         # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_757")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_773")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_792")
    OP_AF(0xAE)
    Jump("loc_7D4")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7A2")
    OP_AF(0xAD)
    Jump("loc_7D4")

    label("loc_7A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7B2")
    OP_AF(0xAC)
    Jump("loc_7D4")

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7CB")
    OP_AF(0xAF)
    Jump("loc_7CD")

    label("loc_7CB")

    OP_AF(0xAB)

    label("loc_7CD")

    Jump("loc_7D4")

    label("loc_7D2")

    OP_AF(0xAA)

    label("loc_7D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82A")

    label("loc_7E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA")
    Call(0, 10)
    Jump("loc_82A")

    label("loc_7FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80E")
    Jump("loc_82A")

    label("loc_80E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_82A")

    Jump("loc_6BD")

    label("loc_82F")

    Return()

    # Function_5_514 end

    def Function_6_830(): pass

    label("Function_6_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97E")

    ChrTalk(
        0x8,
        (
            "Something like that appeared, eh...?\x01",
            "It's been one thing after another, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...If you're heading into that\x01",
            ""huge tree", make sure\x01",
            "you're fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If those monsters are going to\x01",
            "be your opponents, make sure\x01",
            "your weapons are enhanced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWe will. Thanks so much for your help!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A01")

    label("loc_97E")


    ChrTalk(
        0x8,
        (
            "You guys too have it tough...\x01",
            "But never lose heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can only remodel your weapons,\x01",
            "but I'll do all that I can for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A01")

    Jump("loc_2388")

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF2")

    ChrTalk(
        0x8,
        (
            "You guys... \x01",
            "Ha ha, you're safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you rendezvous with\x01",
            "Dudley and the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thankfully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOl' man Guillaume,\x01",
            "thanks again for your work\x01",
            "on my "Berserker".\x02\x03",
            "#00300FIt really saved me when\x01",
            "I was outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hehe, good then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, be sure to keep in\x01",
            "mind the machine's weak points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If that monster rifle ever\x01",
            "breaks, I can't guarantee I'll\x01",
            "be able to fix it up right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, I'll keep that\x01",
            "in mind when usin' it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Alright. If you understand, that's good enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We don't know what kind of tricks\x01",
            "the President's using either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys need to properly\x01",
            "maintain your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight. We will be counting on you again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 3)
    Jump("loc_D6D")

    label("loc_CF2")


    ChrTalk(
        0x8,
        (
            "We don't know what kind of tricks\x01",
            "the President's using either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys need to properly\x01",
            "maintain your weapons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6D")

    Jump("loc_2388")

    label("loc_D72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1A")

    ChrTalk(
        0x8,
        (
            "The Independent State of Crossbell\x01",
            "and the State Guard, huh... Big stuff again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Were you guys told about all this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNo, that was the first we heard of it to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FAnyway, we're gathering\x01",
            "information right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I see... So you guys have it tough too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anything could happen going forward.\x01",
            "Don't lose heart, and do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FSure. \x01",
            "Thanks, old man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FAC")

    label("loc_F1A")


    ChrTalk(
        0x8,
        (
            "But, well, to think we're picking a fight\x01",
            "with the two major powers so openly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway... I'll keep tabs on\x01",
            "the developments for awhile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAC")

    Jump("loc_2388")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1079")

    ChrTalk(
        0x8,
        (
            "For right now, I'll handle\x01",
            "reconstruction work by day\x01",
            "and factory work by night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though thanks to that I don't\x01",
            "have time to rest, I'm happy\x01",
            "people rely on me so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C0")

    label("loc_1079")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FA")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "I'll have that blade-\x01",
            "rifle repaired by the\x01",
            "day after tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, please\x01",
            "wait until then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C0")

    label("loc_10FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_END)), "loc_1182")

    ChrTalk(
        0x8,
        (
            "Now then, I think I'll process\x01",
            "the U-Materials right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Really, thanks for all your help, guys.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1233")

    label("loc_1182")


    ChrTalk(
        0x8,
        (
            "For right now, I'll handle\x01",
            "reconstruction work by day\x01",
            "and factory work by night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though thanks to that I don't\x01",
            "have time to rest, I'm happy\x01",
            "people rely on me so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1233")

    Jump("loc_12C0")

    label("loc_1238")


    ChrTalk(
        0x8,
        (
            "I had some of that\x01",
            "pork miso earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It gave me a\x01",
            "lot of energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. Thanks to that, the\x01",
            "work's progressing smoothly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C0")

    Jump("loc_2388")

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_136A")

    ChrTalk(
        0x8,
        (
            "That Randy had a worried\x01",
            "expression earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know the details, but...\x01",
            "It's in times like these that\x01",
            "you have to support your friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2388")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144A")

    ChrTalk(
        0x8,
        "They say there was a derailment yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm told that a giant monster\x01",
            "appeared and struck the train, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did it have enough strength to derail\x01",
            "a train? I don't get that story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C8")

    label("loc_144A")


    ChrTalk(
        0x8,
        (
            "Just what was that monster\x01",
            "that attacked the train?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It couldn't have that much strength... \x01",
            "I don't get that story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C8")

    Jump("loc_2388")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1588")

    ChrTalk(
        0x8,
        "Alright. With this, the orbal lamps repair is complete.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next is... Maintenance\x01",
            "of a tactical orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First is setting up\x01",
            "the scanning Quartz...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F7")

    label("loc_1588")


    ChrTalk(
        0x8,
        (
            "Quartz, Quartz...\x01",
            "Whoops, this one's for\x01",
            "the previous generation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Damn. This is\x01",
            "confusing as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F7")

    Jump("loc_2388")

    label("loc_15FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_169D")

    ChrTalk(
        0x8,
        (
            "Umm, next is the orbal lamps maintenance...\x01",
            "I think I've got five of them to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now then. I think I'll finish\x01",
            "them up before lunchtime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2388")

    label("loc_169D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_182C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1795")

    ChrTalk(
        0x8,
        (
            "There's arguments on both\x01",
            "sides, but the problem of state\x01",
            "independence is a delicate one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They say there's already a number of\x01",
            "supporters, but I wonder how many of them\x01",
            "really understand the issue's importance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1827")

    label("loc_1795")


    ChrTalk(
        0x8,
        (
            "What will the independence proposal\x01",
            "bring...? I honestly don't know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But anyhow, I'm worried about\x01",
            "the actions of the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1827")

    Jump("loc_2388")

    label("loc_182C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC9")

    ChrTalk(
        0x8,
        (
            "Hey, young lady.\x01",
            "It looks like you've ended\x01",
            "your Foundation work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes. If pushed, I'd\x01",
            "say I felt I had to.\x02\x03",
            "#00200FBy the way... My chief has\x01",
            "been stopping by this place\x01",
            "periodically, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha, I guess. Last time,\x01",
            "he came with a new orbal\x01",
            "staff blueprint, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Whoops, I wasn't supposed to\x01",
            "tell you that, young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That Roberts is so annoying. Keep what\x01",
            "I told you a secret for me, alright?\x02",
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
        0x103,
        (
            "#00203F...Yes. Please don't worry about it.\x02\x03",
            "#00211FWhen it comes to\x01",
            "orbal staff mods, \x01",
            "I mostly trust him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ha ha, you're certainly right about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I'm sure you know, young\x01",
            "lady, orbal staff mods are\x01",
            "crazily complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wouldn't touch them without\x01",
            "someone's assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUmm, I don't really\x01",
            "get it, but...\x02\x03",
            "#10100FWhy would Chief\x01",
            "Roberts keep something\x01",
            "like that from Tio?\x02\x03",
            "#10106FThis way of doing it is\x01",
            "rather...indirect, I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHa ha, well it's fine, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's not like any of us know that\x01",
            "person that well either, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes... But this is most likely\x01",
            "a form of fatherly love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F......I don't want to\x01",
            "acknowledge it, but I\x01",
            "suppose you're right.\x02\x03",
            "#00200FAnyway, I already got used to\x01",
            "this "exchange" of orbal staves.\x02\x03",
            "#00204FPlease don't worry about it, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 3)
    Jump("loc_1E4F")

    label("loc_1DC9")


    ChrTalk(
        0x8,
        (
            "By the way, I can modify your orbal staff\x01",
            "right away if you'd like, young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please just say the word whenever you need.\x02",
    )

    CloseMessageWindow()

    label("loc_1E4F")

    Jump("loc_2388")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3C")

    ChrTalk(
        0x8,
        (
            "I glanced at Orchis Tower\x01",
            "earlier. How to say...\x01",
            "Simply unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As an engineer I am interested\x01",
            "in the latest equipment, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How to say... \x01",
            "I have no interest in\x01",
            "displays of "power."\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FDD")

    label("loc_1F3C")


    ChrTalk(
        0x8,
        (
            "Orchis Tower is a completely\x01",
            "unthinkable building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As an engineer I am interested in\x01",
            "the latest equipment, but... \x01",
            "I can't get into it no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDD")

    Jump("loc_2388")

    label("loc_1FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2091")

    ChrTalk(
        0x8,
        (
            "For your Special\x01",
            "Support Section, only\x01",
            "the young lady is left, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, I'd like to tamper with that orbal\x01",
            "staff of hers again as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2388")

    label("loc_2091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2178")

    ChrTalk(
        0x8,
        "Today is a rare rainy day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't care about getting wet...\x01",
            "It's just that this moisture is the\x01",
            "enemy of precision instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You have to be precise when\x01",
            "fiddling with mechanical parts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21F3")

    label("loc_2178")


    ChrTalk(
        0x8,
        (
            "This moisture is the enemy\x01",
            "of precision instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You have to be precise when\x01",
            "fiddling with mechanical parts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F3")

    Jump("loc_2388")

    label("loc_21F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F4")

    ChrTalk(
        0x8,
        (
            "Please feel free to ask me whenever\x01",
            "you'd like to remodel your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I said it before, but I was an\x01",
            "Epstein Foundation engineer who\x01",
            "specialized in materials science.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You don't mind trusting my skill, right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2388")

    label("loc_22F4")


    ChrTalk(
        0x8,
        (
            "Please feel free to ask me whenever\x01",
            "you'd like to remodel your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You don't mind trusting my skill\x01",
            "with something like this, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2388")

    Return()

    # Function_6_830 end

    def Function_7_2389(): pass

    label("Function_7_2389")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x104, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, by the way, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "About the maintenance of that\x01",
            "blade rifle you asked me about...\x01",
            "Can you wait a little longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSure, I don't mind, but...\x02\x03",
            "#00301FIs there any kind of problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know if it's a problem, but it's because\x01",
            "there're all these darned custom parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They can't be substituted,\x01",
            "and reproducing them takes\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I think I'll be able to manage\x01",
            "yours better than your little\x01",
            "sister's chainsaw rifle, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F"Testa-Rossa", huh...\x01",
            "That's the real thing.\x02\x03",
            "#00301FI can't believe a little girl like her\x01",
            "can even wield such a weapon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            ""Testa-Rossa", the red head... It's the\x01",
            "name of a demon from an Imperial legend\x01",
            "that possessed a thousand weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There was a weapon I made\x01",
            "with the same name, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that this one\x01",
            "completely outclasses mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, don't worry about it.\x02\x03",
            "#00308FAnyhow, its origin is a very\x01",
            "special weapons workshop...\x02\x03",
            "#00301FIt's also made to order,\x01",
            "so it must be really tough.\x02\x03",
            "#00306FSorry, ol' man. I'm takin'\x01",
            "up your valuable time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, but thanks to you,\x01",
            "I learned something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I discovered techniques that could\x01",
            "be useful in making modded arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think it'll take a week until\x01",
            "the designs are ready, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh yeah, aren't you busy with\x01",
            "the reconstruction work?\x02\x03",
            "#00304FDon't get so stressed for me, you know,\x01",
            "I'm not in such a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, you kid don't need to\x01",
            "worry about this old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, I'll contact you\x01",
            "once repairs are completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You'll have to just wait until then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha...\x01",
            "Thanks, ol' man.\x02\x03",
            "I'll leave it to you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x18D, 5)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_2389 end

    def Function_8_2A0B(): pass

    label("Function_8_2A0B")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Oh, if it isn't Randy. So you've\x01",
            "finally rejoined the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, thankfully.\x02\x03",
            "#00304FAnyway, if there's a chance, I'd like\x01",
            "you to mod my weapons again, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure. As long as you've got the materials, \x01",
            "I'll always accept your requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you too, \x01",
            "don't overdo it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x14D, 2)
    Return()

    # Function_8_2A0B end

    def Function_9_2B69(): pass

    label("Function_9_2B69")

    EventBegin(0x0)
    Fade(500)
    OP_68(2470, 1400, 4820, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x101, 2240, 0, 4730, 90)
    SetChrPos(0x102, 870, 0, 5250, 90)
    SetChrPos(0x103, 1540, 0, 3220, 45)
    SetChrPos(0x104, 2040, 0, 6260, 135)
    SetChrPos(0xF4, 1080, 0, 6920, 135)
    SetChrPos(0xF5, 380, 0, 3940, 90)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11PStill, an unthinkable\x01",
            "thing has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI want to help you\x01",
            "guys too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...If I just had "that".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F"That"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P"Zemurian Ore", they call it. It's\x01",
            "the name of the metal found in the\x01",
            "ruins of that ancient civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBefore, some scholar somewhere\x01",
            "finally found a processing method,\x01",
            "and made some unthinkably hard items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf I had some of those, I could make some of\x01",
            "these super strong weapons I've designed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_END)), "loc_2EAD")

    ChrTalk(
        0x8,
        (
            "#11PEven more amazing than the ones\x01",
            "I made you before, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FEven more than those...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FThat really is amazing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF0")

    label("loc_2EAD")


    ChrTalk(
        0x104,
        "#6P#00305FA super amazing weapon...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FReally!?\x02",
    )

    CloseMessageWindow()

    label("loc_2EF0")


    ChrTalk(
        0x103,
        (
            "#12P#00202FBecause of the situation, we are in\x01",
            "desperate need of strong weapons, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, I could make them for you\x01",
            "right away if I had the materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmm. If I had five small shards,\x01",
            "that would be plenty to\x01",
            "make a weapon, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_3124")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_END)), "loc_3091")

    ChrTalk(
        0x101,
        (
            "#6P#00000F(Zemurian Ore... \x01",
            "We just got one from\x01",
            "that fortune teller.)\x02\x03",
            "#00003F(And shards,\x01",
            "huh... I got one\x01",
            "of those earlier.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_311F")

    label("loc_3091")


    ChrTalk(
        0x101,
        (
            "#6P#00000F(Zemurian Ore... \x01",
            "We just got one from\x01",
            "that fortune teller.)\x02\x03",
            "#00003F(And shards, huh... Maybe I\x01",
            "should look around for them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311F")

    Jump("loc_316E")

    label("loc_3124")


    ChrTalk(
        0x101,
        (
            "#6P#00003F(Shards, huh... Come to think\x01",
            "of it, I already have some.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_316E")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh, could it be you have\x01",
            "some idea about them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAlright, in that case, let me know when\x01",
            "you're ready for me to make a weapon for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSpeak with me again once\x01",
            "you've got a "Zemurian Ore"\x01",
            "or five "shards".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'll make a weapon for you immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x18A, 7)
    EventEnd(0x5)
    Return()

    # Function_9_2B69 end

    def Function_10_32F9(): pass

    label("Function_10_32F9")

    EventBegin(0x0)
    Fade(500)
    OP_68(2470, 1400, 4820, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x101, 2240, 0, 4730, 90)
    SetChrPos(0x102, 870, 0, 5250, 90)
    SetChrPos(0x103, 1540, 0, 3220, 45)
    SetChrPos(0x104, 2040, 0, 6260, 135)
    SetChrPos(0xF4, 1080, 0, 6920, 135)
    SetChrPos(0xF5, 380, 0, 3940, 90)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3587")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_3444")

    ChrTalk(
        0x8,
        (
            "#11PThat's a Zemurian Ore...!\x01",
            "Ha ha, you got some, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PUsing that, I can make\x01",
            "a weapon for 1 person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BF")

    label("loc_3444")


    ChrTalk(
        0x8,
        (
            "#11POoh, Zemurian Ore shards...\x01",
            "It seems you've gathered five!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PUsing that, I can make\x01",
            "a weapon for 1 person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BF")


    ChrTalk(
        0x8,
        (
            "#11PI can begin creating one anytime...\x01",
            "...So, do you want to try?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, by all means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHehe, nice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThink carefully about which\x01",
            "weapon you want me to make.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35BC")

    label("loc_3587")


    ChrTalk(
        0x8,
        "#11POh, have you decided which weapon you want?\x02",
    )

    CloseMessageWindow()

    label("loc_35BC")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Infinity (Lloyd)\x01",           # 0
            "Exia Ray (Elie)\x01",            # 1
            "Cosmo Collapser (Tio)\x01",      # 2
            "Denotic Abyss (Randy)\x01",      # 3
            "Arc Soleil (Noｱl)\x01",         # 4
            "Seventh Arms (Wazy)\x01",        # 5
            "Eieinoken (Rixia)\x01",          # 6
            "Himmel Tur (Dudley)\x01",        # 7
            "Quit\x01",                       # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CC1")

    ChrTalk(
        0x101,
        (
            "#6P#00000FThen, please, make\x01",
            "us this weapon.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_371A")
    SubItemNumber(0x396, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_376A")

    label("loc_371A")

    SubItemNumber(0x394, 5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_376A")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#11PAlright, so, it's time to\x01",
            "make my skills shine!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(956, 0, 100, 0)
    Sleep(500)
    Sound(378, 0, 100, 0)
    Sleep(800)
    Sound(956, 0, 100, 0)
    Sleep(900)
    Sound(288, 0, 50, 0)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11P...Alright, it's ready.\x01",
            "Take it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3870")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_3870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38CD")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x409),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x409, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_38CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392A")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x41D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_392A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3987")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x431),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x431, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_3987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E4")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x459),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x459, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_39E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A41")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x445),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x445, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_3A41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x464),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x464, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3AF6")

    label("loc_3A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF6")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x469),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x469, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C26")

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you very much, Master Guillaume.\x01",
            "We'll put it to good use for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHehe, no problem.\x01",
            "I too got more a blessing than I deserved\x01",
            "by being able to handle such material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PUse this thing to lead you to a solid\x01",
            "resolution of the Crossbell incident!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E0(0x14, 0x0)
    SetScenarioFlags(0x18B, 1)
    Jump("loc_3CB9")

    label("loc_3C26")


    ChrTalk(
        0x8,
        (
            "#11PBecause it's a time like this,\x01",
            "this thing should be useful too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnd so, shape up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, we'll use it with care.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3CB9")

    ClearScenarioFlags(0x0, 3)
    Jump("loc_3D47")

    label("loc_3CC1")


    ChrTalk(
        0x8,
        "#11PReally? Nothing can't be done if you have doubts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhen you decide what you want\x01",
            "me to make, just talk to me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3D47")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_32F9 end

    def Function_11_3D77(): pass

    label("Function_11_3D77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB0")
    Call(0, 17)
    Return()

    label("loc_3DB0")

    Call(0, 19)
    Return()

    label("loc_3DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD6")
    Call(0, 23)
    Return()

    label("loc_3DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4254")
    SetScenarioFlags(0x191, 5)
    TalkBegin(0xFE)

    ChrTalk(
        0x105,
        (
            "#10300FAnd? What are you helping\x01",
            "with here, Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FI am repairing what\x01",
            "materials I can and helping\x01",
            "with the processing.\x02\x03",
            "#04102FIt's a lot more detailed work than\x01",
            "I thought, but it's pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FFun, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou cook at Trinity,\x01",
            "if I remember\x01",
            "correctly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FYeah, before I did.\x02\x03",
            "I left it to Liang and\x01",
            "Azel recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. From the looks of things,\x01",
            "you've got nimble fingers, Abbas.\x02\x03",
            "#10304FCooking, manufacturing and of course\x01",
            "sewing are your specialties, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHeh, I feel like this is a\x01",
            "whole other side of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHow to say this... I think you'll\x01",
            "make a good house-husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHmm, but I feel like he's still\x01",
            "hiding lots of other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, I'm telling you\x01",
            "this to warn you, but\x01",
            "Abbas is only mine㈱\x02\x03",
            "#10304FWell, I could think about\x01",
            "renting him, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04100F...What are you talking about.\x02\x03",
            "Anyway, I plan to assist\x01",
            "Master Guillaume here\x01",
            "for awhile.\x02\x03",
            "Come anytime if you need something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FS-Sure...\x02\x03",
            "#00003F(Abbas, huh... There're a lot of\x01",
            "mysteries about him, huh.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_42BE")

    label("loc_4254")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "#04100FI plan to assist\x01",
            "Master Guillaume\x01",
            "here for awhile.\x02\x03",
            "Come anytime if you need something.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_42BE")

    Return()

    # Function_11_3D77 end

    def Function_12_42BF(): pass

    label("Function_12_42BF")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_12_42BF end

    def Function_13_42C9(): pass

    label("Function_13_42C9")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4629")

    ChrTalk(
        0x9,
        (
            "And so, these are the\x01",
            "blueprints for the orbal\x01",
            "staff Tio's now using...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh! I think I can expect higher\x01",
            "output from this construction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright. I think I'll be able to use\x01",
            "these when the young lady gets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ah, thank you so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With this, Tio will be able to use her orbal\x01",
            "staff even immediately after she gets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, it seems like the\x01",
            "young lady's return is delayed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, that's right! It looks like\x01",
            "she's gotten more work to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lately I've been contacting her every hour, \x01",
            "but I hardly ever receive a response. \x01",
            "I'm so worried about her!\x02",
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
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "...You care too much about her. That's the problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Chief Roberts... He's the same as always.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_4729")

    label("loc_4629")


    ChrTalk(
        0x9,
        (
            "I wonder if Tio's eating properly? \x01",
            "She'll ruin her health\x01",
            "if she works too hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ah, I'm still worried! I've got to try contacting\x01",
            "her again once I get back to the Foundation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(H-Hmm... As expected, \x01",
            "he's overprotective of her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4729")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_42C9 end

    def Function_14_4732(): pass

    label("Function_14_4732")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(0, 2000, 500, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16980, 0)
    SetChrPos(0x101, 0, 0, 1000, 45)
    SetChrPos(0x102, -1000, 0, 1000, 45)
    SetChrPos(0x109, 0, 0, 0, 45)
    SetChrPos(0x105, -1000, 0, 0, 45)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(600)
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11POh, you guys, huh.\x01",
            "It's been awhile.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2990, 1300, 3770, 2000)
    MoveCamera(49, 15, 0, 2000)
    OP_6E(440, 2000)
    SetCameraDistance(19900, 2000)

    def lambda_4830():
        OP_96(0xFE, 0xBB8, 0x0, 0xEBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4830)
    Sleep(400)

    def lambda_484D():
        OP_96(0xFE, 0x6A4, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_484D)
    Sleep(400)

    def lambda_486A():
        OP_96(0xFE, 0xCE4, 0x0, 0xAD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_486A)
    Sleep(400)

    def lambda_4887():
        OP_96(0xFE, 0x7D0, 0x0, 0x8DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4887)
    WaitChrThread(0x101, 1)

    def lambda_48A5():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48A5)
    WaitChrThread(0x102, 1)

    def lambda_48B6():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_48B6)
    WaitChrThread(0x109, 1)

    def lambda_48C7():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_48C7)
    WaitChrThread(0x105, 1)

    def lambda_48D8():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_48D8)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00000FHello, Master.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FIt has been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHa ha, well there's no\x01",
            "need to be so polite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHm, the Testaments' leader has\x01",
            "joined the Special Support Section,\x01",
            "just like the rumors said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PMan, what a shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, thanks for that.\x02\x03",
            "#10302FBy the way, you turned down my request \x01",
            "before, but will you accept to modify\x01",
            "my weapons going forward?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A7D():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4A7D)

    def lambda_4A8A():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A8A)
    TurnDirection(0x102, 0x105, 500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FWazy, how can you say such a shrewd thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHa ha. Well, I suppose.\x02",
    )

    CloseMessageWindow()

    def lambda_4B2B():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4B2B)

    def lambda_4B38():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B38)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "#11PIf it's not for picking up fights,\x01",
            "I'd be happy to do it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FRepair workshop "Guillaume Factory".\x02\x03",
            "#10104FIt looks like you take weapon\x01",
            "modification requests in addition\x01",
            "to repairs of orbal goods...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x109, 500)

    ChrTalk(
        0x8,
        "#5POh, you're a new face young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, although they're mods,\x01",
            "I only enhance to the extent\x01",
            "it's safe to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI got a business permit recently, and I\x01",
            "won't do any acts that violate the law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, if you get your hands on some\x01",
            "good materials, feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12PY-Yes, understood.\x02",
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※At "Guillaume Factory", you can use\x01\x07\x02",
            "U-Material and such to create weapons\x01",
            "that are stronger than normal.\x02\x03",
            "※By speaking to Guilliaume at the\x01",
            "counter and selecting [Remodel],\x01",
            "the modification menu will open.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 3000, 0, 3770, 45)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x138, 3)
    EventEnd(0x5)
    Return()

    # Function_14_4732 end

    def Function_15_4EBC(): pass

    label("Function_15_4EBC")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(4500, 1000, 5330, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 3000, 0, 5000, 90)
    SetChrPos(0x102, 2800, 0, 4000, 90)
    SetChrPos(0x103, 1700, 0, 4300, 90)
    SetChrPos(0x109, 1900, 0, 5300, 90)
    SetChrPos(0x105, 2700, 0, 6500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11POh, it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThat Randy! What has he\x01",
            "gone and done this time!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe asked me to service\x01",
            "something totally unusual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FI knew it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FWas that this morning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah. He showed up all\x01",
            "of a sudden at 5AM.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI was just finishing up an all-nighter\x01",
            "when he forced it on me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FThen... About the "something\x01",
            "totally unusual"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FWas it some kind\x01",
            "of heavy weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah... Although it\x01",
            "was in pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt hadn't been used in awhile\x01",
            "so I tuned up the mechanism\x01",
            "parts and exhaust unit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTo build such a thing in the first place,\x01",
            "you'd have to be some kinda crazy monster.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_526E")

    ChrTalk(
        0x105,
        (
            "#10308FThere's no mistake. It's\x01",
            "the orbal rifle Randy used.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52BE")

    label("loc_526E")


    ChrTalk(
        0x105,
        (
            "#10308FIt's just a guess, but I'd say it's\x01",
            "a custom orbal rifle for Randy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52BE")


    ChrTalk(
        0x101,
        (
            "#6P#00006FYeah...\x01",
            "No doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FMr. Guillaume, thank\x01",
            "you for the information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSure, no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI don't know the situation but... \x01",
            "He had quite a worried look on\x01",
            "his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAs his friends, please do\x01",
            "all that you can for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOf course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FRoger!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 2500, 0, 5330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x165, 7)
    OP_29(0xAA, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_15_4EBC end

    def Function_16_5438(): pass

    label("Function_16_5438")

    EventBegin(0x0)
    Fade(500)
    OP_68(13180, 2300, 7330, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13690, 1000, 7530, 180)
    SetChrPos(0x102, 12750, 1000, 7960, 180)
    SetChrPos(0x103, 13900, 1000, 8650, 180)
    SetChrPos(0x104, 12810, 1000, 9200, 180)
    SetChrPos(0x105, 13890, 1000, 9740, 180)
    SetChrPos(0x109, 12050, 1000, 9950, 180)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FMaster Guillaume, do you have\x01",
            "something like a metal detector \x01",
            "we can borrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "A metal detector...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I remember making\x01",
            "something like that awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh, bingo. I knew we could\x01",
            "count on an orbal engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I did make it half\x01",
            "for fun, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What're you using it for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, you see...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained they were helping Kanon\x01",
            "with the scrap collection.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "I see... In that case,\x01",
            "you'll definitely need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, I'll\x01",
            "lend it to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Give me a sec, I know\x01",
            "it's here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_572E():

        label("loc_572E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_572E")

    QueueWorkItem2(0x109, 0, lambda_572E)

    def lambda_5740():

        label("loc_5740")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5740")

    QueueWorkItem2(0x102, 0, lambda_5740)

    def lambda_5752():

        label("loc_5752")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5752")

    QueueWorkItem2(0x104, 0, lambda_5752)

    def lambda_5764():

        label("loc_5764")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5764")

    QueueWorkItem2(0x101, 0, lambda_5764)

    def lambda_5776():

        label("loc_5776")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5776")

    QueueWorkItem2(0x105, 0, lambda_5776)

    def lambda_5788():

        label("loc_5788")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5788")

    QueueWorkItem2(0x103, 0, lambda_5788)
    OP_95(0x8, 15210, 1000, 6330, 2000, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(1500)
    OP_95(0x8, 13130, 1000, 6290, 2000, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)

    ChrTalk(
        0x8,
        (
            "Ah, here it is.\x01",
            "Take it.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x375),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x375, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00205FIt is really well made.\x02\x03",
            "#00203FI think it is equal to\x01",
            "units the police uses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FT-That's pretty\x01",
            "amazing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Gwahaha, well, at least\x01",
            "it's in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, it's not all\x01",
            "that efficient. It's\x01",
            "nothing to be proud of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "So, you know how to use it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FI've used them many times\x01",
            "for customs inspections.\x02\x03",
            "#10102FWe should activate it in places\x01",
            "there's likely to be metal, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's the general idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you carefully search areas\x01",
            "where there's a response,\x01",
            "you should find some metal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You might find some other\x01",
            "things too, if you're lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see...\x01",
            "Got it.\x02\x03",
            "#00000FAlright, we'll put it to good use.\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※The metal detector can be used\x01",
            "only in the Downtown outdoors map.\x01",
            "Use it by pressing [△+L buttons].\x02\x03",
            "※You can also use it from\x01",
            "[ITEMS] in the camp menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x196, 5)
    OP_29(0x8E, 0x1, 0x7)
    SetChrPos(0x8, 13130, 1000, 6290, 180)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 12990, 1000, 9600, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_16_5438 end

    def Function_17_5BF8(): pass

    label("Function_17_5BF8")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(58, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 12710, 990, 10110, 90)
    SetChrPos(0x103, 13360, 1000, 7350, 90)
    SetChrPos(0x104, 12750, 1000, 8440, 90)
    SetChrPos(0x105, 13580, 1000, 9460, 90)
    SetChrPos(0x109, 12000, 1000, 9100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x105,
        "#10300FHu hu, hard at work, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FWazy... And the\x01",
            "Support Section too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yo. You saw our request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. For now I want to\x01",
            "ask about the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FFrom appearances, it looks\x01",
            "like the reconstruction\x01",
            "has a ways to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FYeah, exactly.\x02\x03",
            "The citizens of Downtown\x01",
            "are working together led\x01",
            "by the Testaments, but...\x02\x03",
            "There's still a lot of damage left,\x01",
            "and progress has been slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThat's right, the\x01",
            "demonized Wald\x01",
            "attacked Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FDo the citizens\x01",
            "know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FNo... Hardly anyone\x01",
            "noticed outside of\x01",
            "the Vipers.\x02\x03",
            "It must be because he appeared\x01",
            "in that grotesque form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt is too shocking... \x01",
            "It is better to keep this from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100F...Let's set that question\x01",
            "aside for now.\x02\x03",
            "What's important right now is to decide how\x01",
            "to proceed with the reconstruction work.\x02\x03",
            "Here in Downtown, we can't count on\x01",
            "government assistance. And we haven't\x01",
            "the funds to employ traders.\x02\x03",
            "It would be a great help if the Support\x01",
            "Section could lend us their assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FLet me see...\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_17_5BF8 end

    def Function_18_610F(): pass

    label("Function_18_610F")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Help With Reconstruction\x01",      # 0
            "Think About It For Now\x01",        # 1
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
        (0, "loc_618F"),
        (1, "loc_619F"),
        (SWITCH_DEFAULT, "loc_62FE"),
    )


    label("loc_618F")

    OP_29(0x8E, 0x4, 0x2)
    SetScenarioFlags(0x196, 0)
    Call(0, 20)
    Jump("loc_62FE")

    label("loc_619F")


    ChrTalk(
        0x101,
        (
            "#00006FWe want to help, but... It depends\x01",
            "on how our other work goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBy the way, can\x01",
            "we accept later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FYeah. If you can help,\x01",
            "the timing doesn't matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I won't force you. \x01",
            "Help us if you get free, alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. \x01",
            "We'll do whatever we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13510, 1000, 9270, 90)
    EventEnd(0x5)
    Jump("loc_62FE")

    label("loc_62FE")

    Return()

    # Function_18_610F end

    def Function_19_62FF(): pass

    label("Function_19_62FF")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(58, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 12710, 990, 10110, 90)
    SetChrPos(0x103, 13360, 1000, 7350, 90)
    SetChrPos(0x104, 12750, 1000, 8440, 90)
    SetChrPos(0x105, 13580, 1000, 9460, 90)
    SetChrPos(0x109, 12000, 1000, 9100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#04100FHmm, so, will you help with the\x01",
            "Downtown reconstruction work?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_19_62FF end

    def Function_20_6413(): pass

    label("Function_20_6413")


    ChrTalk(
        0x101,
        "#00000FYes, leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04100FHm, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, I thought you\x01",
            "guys might say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo, what should\x01",
            "we help with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FRight now, work is being performed\x01",
            "in three places primarily.\x02\x03",
            "Firstly, emergency food distribution\x01",
            "at "Lotus Heights".\x02\x03",
            "Secondly, scrap metal\x01",
            "recovery near Maison Imelda.\x02\x03",
            "And finally, building material\x01",
            "collection and processing \x01",
            "here in "Guillaume Factory".\x02\x03",
            "I would like the Support Section\x01",
            "to go to each place and\x01",
            "help with whatever's needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI see... So each of those\x01",
            "activities is important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FBy the way, what about the\x01",
            "work that's occurring here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right, we're gathering materials\x01",
            "to repair our damaged buildings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For now, I can use the workshop's\x01",
            "left over materials, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Just earlier, I noticed a big problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FA problem? What kind of problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To be frank, I don't have enough screws\x01",
            "and nails to assemble the materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I won't be able to repair\x01",
            "anything at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FYou can't use any\x01",
            "of the waste lying\x01",
            "around outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FHmm, I asked that little boy, Kanon,\x01",
            "for help with it for the time being, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if I had to say it,\x01",
            "it's being done for\x01",
            "fundraising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Additionally, there's a question of how strong they\x01",
            "are, so I'd like to use new wherever possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, that sounds like quite the predicament.\x02\x03",
            "#10300FThen, you just need\x01",
            "us to bring you some\x01",
            "screws and nails?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, I'm mostly\x01",
            "good on that front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What I really need is that\x01",
            ""U-Material" used for remodeling arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If I had that, I could\x01",
            "make whatever's needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F"U-Material", you say... \x01",
            "That seems pretty tough to find.\x02\x03",
            "#00200FHow many do you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I think 10\x01",
            "should do nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Can I ask you guys for that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. We'll bring them\x01",
            "here once we've collected them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04100FWe're counting on you, Special Support Section.\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_6BA6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BA6)
    Sleep(250)

    def lambda_6BB6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6BB6)
    Sleep(50)

    def lambda_6BC6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6BC6)
    Sleep(50)

    def lambda_6BD6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6BD6)
    Sleep(50)

    def lambda_6BE6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6BE6)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004FAlright, let's\x01",
            "get started.\x02\x03",
            "#00000FLet's ask about the scrap collection\x01",
            "and emergency food distribution too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FRoger, leader.\x02\x03",
            "When my old haunt is in a pinch,\x01",
            "I'm glad to pitch in and help.\x02",
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
            "Quest [Downtown Reconstruction Support]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8E, 0x1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13200, 1000, 8320, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_6413 end

    def Function_21_6D7A(): pass

    label("Function_21_6D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x38E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E23")

    ChrTalk(
        0x8,
        "Did you get that U-Material for me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Or rather, you don't\x01",
            "have enough, do you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I need 10 of 'em. Thanks\x01",
            "in advance for your help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F92")

    label("loc_6E23")


    ChrTalk(
        0x8,
        (
            "Oh... Looks like\x01",
            "you've gathered them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Will you hand over ten\x01",
            "of your U-Materials?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "Hand Them Over\x01",      # 0
            "Do Not\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6EE6"),
        (1, "loc_6EEE"),
        (SWITCH_DEFAULT, "loc_6F92"),
    )


    label("loc_6EE6")

    Call(0, 22)
    Jump("loc_6F92")

    label("loc_6EEE")


    ChrTalk(
        0x8,
        (
            "I see. Well, it can't be helped.\x01",
            "You guys must need 'em yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you do have the spares, it'd be\x01",
            "a big help if you could hand them over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F92")

    label("loc_6F92")

    Return()

    # Function_21_6D7A end

    def Function_22_6F93(): pass

    label("Function_22_6F93")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(58, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 12710, 990, 10110, 90)
    SetChrPos(0x103, 13360, 1000, 7350, 90)
    SetChrPos(0x104, 12750, 1000, 8440, 90)
    SetChrPos(0x105, 13580, 1000, 9460, 90)
    SetChrPos(0x109, 12000, 1000, 9100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0xA, 15240, 1000, 9210, 180)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FYes, here you go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x38E, 10)

    ChrTalk(
        0x8,
        (
            "Hehe, thanks. \x01",
            "Don't mind if I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now the repair prospects\x01",
            "are looking up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, we're happy to help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIf you're doin' repair\x01",
            "work, can we help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYeah, we're good\x01",
            "at manual labor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, I can't really\x01",
            "ask that of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's only right for the Downtown\x01",
            "citizens to repair Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FAbbas and the Testaments\x01",
            "will supervise them.\x02\x03",
            "#10309FWell, good luck with everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FYou act like you are not one of them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04102FHu hu, it's fine.\x01",
            "Wazy has his own\x01",
            "role to play.\x02\x03",
            "#04100F...I thank you again,\x01",
            "Special Support Section.\x02\x03",
            "If you're still free, please\x01",
            "help at the other places.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 2)
    OP_29(0x8E, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7491")

    ChrTalk(
        0x101,
        (
            "#00000FYeah, leave it to us.\x02\x03",
            "#00005FSay, we've helped at all the\x01",
            "main places, haven't we...\x02\x03",
            "#00000FNext, let's patrol Downtown\x01",
            "helping with the small stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FThank you for all your\x01",
            "help. I'll see you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Jump("loc_74AF")

    label("loc_7491")


    ChrTalk(
        0x101,
        "#00000FAlright, we will.\x02",
    )

    CloseMessageWindow()

    label("loc_74AF")

    SetChrPos(0x8, 13130, 1000, 6290, 180)
    SetChrPos(0xA, 15170, 1000, 8560, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13840, 1000, 8410, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_6F93 end

    def Function_23_750C(): pass

    label("Function_23_750C")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0xA, 15240, 1000, 9210, 180)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 13840, 1000, 9610, 90)
    SetChrPos(0x103, 13840, 1000, 7210, 90)
    SetChrPos(0x104, 12750, 1000, 8410, 90)
    SetChrPos(0x105, 12750, 1000, 9610, 90)
    SetChrPos(0x109, 12750, 1000, 7210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0xA,
        "#04100FHow did it go...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could it be that you've\x01",
            "finished helping everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we helped out at the main stations.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FI see...\x01",
            "Good work.\x02\x03",
            "It's almost time for the emergency food\x01",
            "distribution. You should kill time until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThen, we'll make another\x01",
            "patrol around Downtown.\x02\x03",
            "#00104FThere might be something\x01",
            "left we can help with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FThank you for all your\x01",
            "help. I'll see you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7101", "ed7150")
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_750C end

    SaveToFile()

Try(main)
