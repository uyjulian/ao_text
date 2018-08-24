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
        "Function_6_836",          # 06, 6
        "Function_7_2342",         # 07, 7
        "Function_8_29C4",         # 08, 8
        "Function_9_2B0F",         # 09, 9
        "Function_10_329E",        # 0A, 10
        "Function_11_3D1E",        # 0B, 11
        "Function_12_4260",        # 0C, 12
        "Function_13_426A",        # 0D, 13
        "Function_14_46C7",        # 0E, 14
        "Function_15_4E22",        # 0F, 15
        "Function_16_538E",        # 10, 16
        "Function_17_5B46",        # 11, 17
        "Function_18_6057",        # 12, 18
        "Function_19_6245",        # 13, 19
        "Function_20_6356",        # 14, 20
        "Function_21_6C9E",        # 15, 21
        "Function_22_6EB6",        # 16, 22
        "Function_23_7425",        # 17, 23
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")
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

    MenuCmd(1, 0, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5F9")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_61D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640")
    OP_AF(0xAD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_669")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_669")
    Call(0, 21)
    Return()

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Return()

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AB")

    label("loc_6AB")

    Jump("loc_53E")

    label("loc_6B0")

    Jump("loc_835")

    label("loc_6B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_835")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_724")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",             # 0
            "Remodel\x01",          # 1
            "Make Weapon\x01",      # 2
            "Cancel\x01",           # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_75D")

    label("loc_724")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",         # 0
            "Remodel\x01",      # 1
            "Cancel\x01",       # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_779")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_779")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_798")
    OP_AF(0xAE)
    Jump("loc_7DA")

    label("loc_798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7A8")
    OP_AF(0xAD)
    Jump("loc_7DA")

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7B8")
    OP_AF(0xAC)
    Jump("loc_7DA")

    label("loc_7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7D1")
    OP_AF(0xAF)
    Jump("loc_7D3")

    label("loc_7D1")

    OP_AF(0xAB)

    label("loc_7D3")

    Jump("loc_7DA")

    label("loc_7D8")

    OP_AF(0xAA)

    label("loc_7DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_830")

    label("loc_7E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_800")
    Call(0, 10)
    Jump("loc_830")

    label("loc_800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_830")

    label("loc_814")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_830")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_830")

    Jump("loc_6BF")

    label("loc_835")

    Return()

    # Function_5_514 end

    def Function_6_836(): pass

    label("Function_6_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97F")

    ChrTalk(
        0x8,
        (
            "Something like that\x01",
            "appeared, eh? It's been one\x01",
            "thing after another, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...If you're heading into\x01",
            "that Huge Tree, make sure\x01",
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
        (
            "#00000FWe will. Thanks so much\x01",
            "for your help!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9FD")

    label("loc_97F")


    ChrTalk(
        0x8,
        (
            "You guys have it\x01",
            "tough... But never lose\x01",
            "heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can only modify your\x01",
            "weapons, but I'll do all\x01",
            "that I can for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FD")

    Jump("loc_2341")

    label("loc_A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDC")

    ChrTalk(
        0x8,
        (
            "You guys... Haha, you're\x01",
            "safe!\x02",
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
        "#00000FYes, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOld man Guillaume, your\x01",
            "work on my Berserker...\x01",
            "Thanks again.\x02\x03",
            "#00300FIt really saved me\x01",
            "outside the city.\x02",
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
            "However, be sure to keep\x01",
            "in mind the machine's\x01",
            "weak points.\x02",
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
            "#00300FYeah, I'll keep that in\x01",
            "mind when using it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright. If you\x01",
            "understand, that's good\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We don't know what kind\x01",
            "of tricks the President's\x01",
            "using either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys need to\x01",
            "properly maintain your\x01",
            "weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight. Thanks again for\x01",
            "all your help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 3)
    Jump("loc_D57")

    label("loc_CDC")


    ChrTalk(
        0x8,
        (
            "We don't know what kind\x01",
            "of tricks the President's\x01",
            "using either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys need to\x01",
            "properly maintain your\x01",
            "weapons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D57")

    Jump("loc_2341")

    label("loc_D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF2")

    ChrTalk(
        0x8,
        (
            "The Crossbell Independent\x01",
            "State State Guard, huh...\x01",
            "Another big thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you guys hear about\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo, this is the first\x01",
            "we've heard of it.\x02",
        )
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
        (
            "I see... So you guys\x01",
            "have it tough too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anything could happen\x01",
            "going forward. Don't lose\x01",
            "heart, and do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304FSure. Thanks, old man.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F81")

    label("loc_EF2")


    ChrTalk(
        0x8,
        (
            "But, well, to think we're\x01",
            "picking a fight with the\x01",
            "major powers so openly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway... I'll keep tabs\x01",
            "on the developments for\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F81")

    Jump("loc_2341")

    label("loc_F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_104E")

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
    Jump("loc_1294")

    label("loc_104E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CF")
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
            "Well, please wait until\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_10CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_END)), "loc_1156")

    ChrTalk(
        0x8,
        (
            "Now then, I think I'll\x01",
            "process the U-Material\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Really, thanks for all\x01",
            "your help, guys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1207")

    label("loc_1156")


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

    label("loc_1207")

    Jump("loc_1294")

    label("loc_120C")


    ChrTalk(
        0x8,
        (
            "I had some of that pork\x01",
            "miso earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It gave me a lot of\x01",
            "energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. Thanks to that,\x01",
            "the work's progressing\x01",
            "smoothly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1294")

    Jump("loc_2341")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_133E")

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
    Jump("loc_2341")

    label("loc_133E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141E")

    ChrTalk(
        0x8,
        (
            "They say there was a\x01",
            "derailment yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm told that a giant\x01",
            "monster appeared and\x01",
            "struck the train, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did it have enough strength\x01",
            "to derail a train? I don't\x01",
            "get that story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_149B")

    label("loc_141E")


    ChrTalk(
        0x8,
        (
            "Just what was that\x01",
            "monster that attacked\x01",
            "the train?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It couldn't have that\x01",
            "much strength... I don't\x01",
            "get that story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149B")

    Jump("loc_2341")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155A")

    ChrTalk(
        0x8,
        (
            "Alright. With this, the\x01",
            "orbal lamp repair is\x01",
            "complete.\x02",
        )
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
            "First is setting up the\x01",
            "scanning quartz...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15C9")

    label("loc_155A")


    ChrTalk(
        0x8,
        (
            "Quartz, quartz...\x01",
            "Whoops, this one's for\x01",
            "the previous generation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Damn. This is confusing\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C9")

    Jump("loc_2341")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_166F")

    ChrTalk(
        0x8,
        (
            "Umm, next is the orbal light\x01",
            "maintenance... I think I've\x01",
            "got five of them to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now then. I think I'll\x01",
            "finish them up before\x01",
            "lunchtime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2341")

    label("loc_166F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175A")

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
            "They say there are already a number\x01",
            "of supporters, but only some of them\x01",
            "understand the issue's importance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17E8")

    label("loc_175A")


    ChrTalk(
        0x8,
        (
            "What will the independence\x01",
            "proposal bring...? I\x01",
            "honestly don't know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But anyhow, I'm worried\x01",
            "about the actions of the\x01",
            "major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E8")

    Jump("loc_2341")

    label("loc_17ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D91")

    ChrTalk(
        0x8,
        (
            "Hey, young lady. It\x01",
            "looks like you've ended\x01",
            "your foundation work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes. If pushed, I'd say I\x01",
            "felt I had to.\x02\x03",
            "#00200FBy the way... The chief has\x01",
            "been stopping by this place\x01",
            "periodically, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I guess. Last time,\x01",
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
            "Whoops, I wasn't\x01",
            "supposed to tell you\x01",
            "that, young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That Roberts is so annoying.\x01",
            "Keep what I told you a\x01",
            "secret for me, alright?\x02",
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
            "#00203F...Sure. Please don't\x01",
            "worry about it.\x02\x03",
            "#00211FWhen it comes to orbal\x01",
            "staff mods, I mostly\x01",
            "trust him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, you're certainly\x01",
            "right about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I'm sure you know, young\x01",
            "lady, orbal staff mods are\x01",
            "unthinkably complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wouldn't touch them\x01",
            "without someone's\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUmm, I don't really get\x01",
            "it, but...\x02\x03",
            "#10100FWhy would Chief Roberts\x01",
            "keep something like that\x01",
            "from Tio?\x02\x03",
            "#10106FThis way of doing it is\x01",
            "rather... indirect, I'd\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHaha, well it's fine,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's not like any of us\x01",
            "know the chief that well\x01",
            "either, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes... But this is most\x01",
            "likely a form of\x01",
            "fatherly love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F......I don't want to\x01",
            "acknowledge it, but I\x01",
            "suppose you're right.\x02\x03",
            "#00200FAnyhow, I've already gotten\x01",
            "used to this "exchange" of\x01",
            "orbal staves.\x02\x03",
            "#00204FPlease don't worry about\x01",
            "it, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 3)
    Jump("loc_1E17")

    label("loc_1D91")


    ChrTalk(
        0x8,
        (
            "By the way, I can modify\x01",
            "your orbal staff right away\x01",
            "if you'd like, young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please just say the word\x01",
            "whenever you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E17")

    Jump("loc_2341")

    label("loc_1E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F03")

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
            "As an engineer I am\x01",
            "interested in the latest\x01",
            "equipment, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How to say... I have no\x01",
            "interest in displays of\x01",
            ""power".\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FA3")

    label("loc_1F03")


    ChrTalk(
        0x8,
        (
            "Orchis Tower is a\x01",
            "completely unthinkable\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As an engineer I am interested in\x01",
            "the latest equipment, but... I\x01",
            "can't get into it no matter what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA3")

    Jump("loc_2341")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_204C")

    ChrTalk(
        0x8,
        (
            "For your Special Support\x01",
            "Section, only Tio is\x01",
            "left, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, I'd like to tinker with\x01",
            "that orbal staff of hers\x01",
            "again as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2341")

    label("loc_204C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2133")

    ChrTalk(
        0x8,
        (
            "Today is a rare rainy\x01",
            "day.\x02",
        )
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
            "You have to be precise\x01",
            "when fiddling with\x01",
            "mechanical parts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21AE")

    label("loc_2133")


    ChrTalk(
        0x8,
        (
            "This moisture is the\x01",
            "enemy of precision\x01",
            "instruments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You have to be precise\x01",
            "when fiddling with\x01",
            "mechanical parts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AE")

    Jump("loc_2341")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AE")

    ChrTalk(
        0x8,
        (
            "Please feel free to ask\x01",
            "me whenever you'd like\x01",
            "to modify your weapons.\x02",
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
        (
            "You don't mind trusting\x01",
            "my skill, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2341")

    label("loc_22AE")


    ChrTalk(
        0x8,
        (
            "Please feel free to ask\x01",
            "me whenever you'd like\x01",
            "to modify your weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You don't mind trusting\x01",
            "my skill with something\x01",
            "like this, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2341")

    Return()

    # Function_6_836 end

    def Function_7_2342(): pass

    label("Function_7_2342")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x104, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, it's you, Randy.\x02",
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
            "#00305FSure, I don't mind,\x01",
            "but...\x02\x03",
            "#00301FIs there some kind of\x01",
            "problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know if it's a problem,\x01",
            "but it's because there are all\x01",
            "these darned custom parts.\x02",
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
            "#00306FTesta-Rossa, huh... That\x01",
            "thing's somethin' else.\x02\x03",
            "#00301FI can't believe a little\x01",
            "girl like her can even\x01",
            "wield such a weapon, but...\x02",
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
            "There was a weapon I\x01",
            "made with the same name,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that this one\x01",
            "completely outclasses\x01",
            "mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, don't worry about\x01",
            "it.\x02\x03",
            "#00308FAnyhow, it's origin is a\x01",
            "very special weapons\x01",
            "workshop...\x02\x03",
            "#00301FIt's also order-made, so\x01",
            "no wonder it's hard to\x01",
            "repair.\x02\x03",
            "#00306FSorry, old man. We've\x01",
            "taken up your valuable\x01",
            "time.\x02",
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
            "I discovered several\x01",
            "techniques that could be\x01",
            "useful in making modded arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think it'll take a\x01",
            "week until the designs\x01",
            "are ready, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh yeah, and aren't you\x01",
            "busy with the\x01",
            "reconstruction work?\x02\x03",
            "#00304FShould we come back\x01",
            "another time when you\x01",
            "aren't so busy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh, you kids don't need\x01",
            "to worry about this old\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, I'll contact you\x01",
            "once repairs are\x01",
            "completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Wait until then for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FSure... Thanks, old man.\x02\x03",
            "I'll leave it to you,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x18D, 5)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_2342 end

    def Function_8_29C4(): pass

    label("Function_8_29C4")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Oh, if it isn't Randy. So\x01",
            "you've finally rejoined\x01",
            "the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, thankfully.\x02\x03",
            "#00304FAnyway, if there's a\x01",
            "chance, I'd like you to mod\x01",
            "my weapons again, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure. As long as you've\x01",
            "got the materials, just\x01",
            "bring them this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, don't overdo it.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x14D, 2)
    Return()

    # Function_8_29C4 end

    def Function_9_2B0F(): pass

    label("Function_9_2B0F")

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
            "#11PI want to help you guys\x01",
            "too, but...\x02",
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
            "#11P"Zemuria Stones", they're called. It's\x01",
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
            "#11PIf I had some of those, I\x01",
            "could make some of these super\x01",
            "strong weapons I've designed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_END)), "loc_2E54")

    ChrTalk(
        0x8,
        (
            "#11PEven more amazing than\x01",
            "the ones I made you\x01",
            "before, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FEven more than those!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FThat really is\x01",
            "amazing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E94")

    label("loc_2E54")


    ChrTalk(
        0x104,
        "#6P#00305FA super amazing weapon!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FReally!?\x02",
    )

    CloseMessageWindow()

    label("loc_2E94")


    ChrTalk(
        0x103,
        (
            "#12P#00202FBecause of the situation,\x01",
            "we're in desperate need\x01",
            "of strong weapons, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, I could make them\x01",
            "for you right away if I\x01",
            "had the materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmm. If I had five small\x01",
            "shards, that would be plenty\x01",
            "to make a weapon, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_30C5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_END)), "loc_3033")

    ChrTalk(
        0x101,
        (
            "#6P#00000F(Zemurian Ore... We just\x01",
            "got one from that\x01",
            "fortune teller.)\x02\x03",
            "#00003F(And shards, huh... I\x01",
            "got one of those\x01",
            "earlier.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C0")

    label("loc_3033")


    ChrTalk(
        0x101,
        (
            "#6P#00000F(Zemurian Ore... We just\x01",
            "got one from that\x01",
            "fortune teller.)\x02\x03",
            "#00003F(And shards, huh...\x01",
            "Maybe I should look\x01",
            "around for them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C0")

    Jump("loc_310F")

    label("loc_30C5")


    ChrTalk(
        0x101,
        (
            "#6P#00003F(Shards, huh... Come to\x01",
            "think of it, I already\x01",
            "have some.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310F")

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
            "#11PAlright, in that case, let me\x01",
            "know when you're ready for me\x01",
            "to make a weapon for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSpeak with me again once\x01",
            "you've got a "Zemuria\x01",
            "Stone" or five "shards".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll make a weapon for\x01",
            "you immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, we understand.\x02",
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

    # Function_9_2B0F end

    def Function_10_329E(): pass

    label("Function_10_329E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3526")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_33EE")

    ChrTalk(
        0x8,
        (
            "#11PThat's a Zemuria Stone!\x01",
            "Haha, so you actually\x01",
            "got one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI can use that to make a\x01",
            "weapon for one of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_33EE")


    ChrTalk(
        0x8,
        (
            "#11POh, Zemuria Fragments...\x01",
            "You collected five of\x01",
            "them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI can use that to make a\x01",
            "weapon for one of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3465")


    ChrTalk(
        0x8,
        (
            "#11PI can start making it\x01",
            "anytime... Well, want to\x01",
            "try it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHehe, very well then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhich weapon shall I\x01",
            "make? Consider it\x01",
            "carefully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3560")

    label("loc_3526")


    ChrTalk(
        0x8,
        (
            "#11POh, have you decided\x01",
            "which weapon you want\x01",
            "made?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3560")


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
            "Yeyingzhijian (Rixia)\x01",      # 6
            "Himmel Tur (Dudley)\x01",        # 7
            "Cancel\x01",                     # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C66")

    ChrTalk(
        0x101,
        (
            "#6P#00000FThen, if you'd make this\x01",
            "weapon for us please?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_36D0")
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
    Jump("loc_3720")

    label("loc_36D0")

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

    label("loc_3720")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#11PAlright, I'll give this\x01",
            "everything I've got!\x02",
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
            "#11P...Alright, it's done.\x01",
            "Go ahead and take it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382F")
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
    Jump("loc_3AB5")

    label("loc_382F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388C")
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
    Jump("loc_3AB5")

    label("loc_388C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E9")
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
    Jump("loc_3AB5")

    label("loc_38E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3946")
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
    Jump("loc_3AB5")

    label("loc_3946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A3")
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
    Jump("loc_3AB5")

    label("loc_39A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A00")
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
    Jump("loc_3AB5")

    label("loc_3A00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5D")
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
    Jump("loc_3AB5")

    label("loc_3A5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB5")
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

    label("loc_3AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC0")

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you very much,\x01",
            "Master Guilliaume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHehe, it's fine. Just being able to\x01",
            "work with a material like this is more\x01",
            "blessing than this engineer deserves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PUse it, and bring this\x01",
            "Crossbell incident to a\x01",
            "conclusion!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E0(0x14, 0x0)
    SetScenarioFlags(0x18B, 1)
    Jump("loc_3C5E")

    label("loc_3BC0")


    ChrTalk(
        0x8,
        (
            "#11PPrecisely because of this\x01",
            "situation, this will be\x01",
            "of use, I'm sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnd so, hang in there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, we'll put it to\x01",
            "good use.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3C5E")

    ClearScenarioFlags(0x0, 3)
    Jump("loc_3CEE")

    label("loc_3C66")


    ChrTalk(
        0x8,
        (
            "#11PReally? Nothing can't be\x01",
            "done if you have doubts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POnce you've decided the\x01",
            "weapon you want made,\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3CEE")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_329E end

    def Function_11_3D1E(): pass

    label("Function_11_3D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D57")
    Call(0, 17)
    Return()

    label("loc_3D57")

    Call(0, 19)
    Return()

    label("loc_3D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D7D")
    Call(0, 23)
    Return()

    label("loc_3D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F3")
    SetScenarioFlags(0x191, 5)
    TalkBegin(0xFE)

    ChrTalk(
        0x105,
        (
            "#10300FAnd? What are you\x01",
            "helping with here,\x01",
            "Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FI am repairing what\x01",
            "materials I can and helping\x01",
            "with the processing.\x02\x03",
            "#04102FIt's a lot more detailed\x01",
            "work than I thought, but\x01",
            "it's pretty fun.\x02",
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
            "#00100FYou cook at Trinity, if\x01",
            "I remember correctly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FYeah, before I did.\x02\x03",
            "Liang and Azel have been\x01",
            "doing it recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. From the looks of\x01",
            "things, you've got nimble\x01",
            "fingers, Abbas.\x02\x03",
            "#10304FCooking, manufacturing and\x01",
            "of course sewing are your\x01",
            "specialties, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHeh, I feel like this is\x01",
            "a whole other side of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHow to say this... I\x01",
            "think you'll make a good\x01",
            "house-husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHmm, but I feel like\x01",
            "he's still hiding lots\x01",
            "of other things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha. Let me just say\x01",
            "this. Abbas is mine㈱\x02\x03",
            "#10304FWell, it might be better\x01",
            "to think of it as a\x01",
            "rental.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04100F...What are you talking\x01",
            "about.\x02\x03",
            "Anyway, I plan to assist\x01",
            "Master Guilliaume here\x01",
            "for a while.\x02\x03",
            "Come anytime if you need\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FS-Sure...\x02\x03",
            "#00003F(Abbas, huh... There are\x01",
            "a lot of mysteries about\x01",
            "him, huh.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_425F")

    label("loc_41F3")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "#04100FI plan to assist Master\x01",
            "Guilliaume here for a\x01",
            "while.\x02\x03",
            "Come anytime if you need\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_425F")

    Return()

    # Function_11_3D1E end

    def Function_12_4260(): pass

    label("Function_12_4260")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_12_4260 end

    def Function_13_426A(): pass

    label("Function_13_426A")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C6")

    ChrTalk(
        0x9,
        (
            "And so, these are the\x01",
            "blueprints for the orbal\x01",
            "staff Tio's now using, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh! I think we can\x01",
            "expect higher output\x01",
            "from this construction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright. I think I'll be\x01",
            "able to use these when\x01",
            "the young lady gets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ah, thanks so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With this, Tio will be able to\x01",
            "use her orbal staff immediately\x01",
            "after she gets back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By the way, it seems\x01",
            "like the young lady's\x01",
            "return is delayed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, that's right! It\x01",
            "looks like she's gotten\x01",
            "more work to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lately I've been contacting her every\x01",
            "hour, but I hardly ever receive a\x01",
            "response. I'm so worried about her!\x02",
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
        (
            "...You care too much\x01",
            "about her. That's the\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Chief Roberts... He's\x01",
            "the same as always.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_46BE")

    label("loc_45C6")


    ChrTalk(
        0x9,
        (
            "I wonder if Tio's eating\x01",
            "properly? And she'll break\x01",
            "if she works too hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ah, I'm still worried! I've got\x01",
            "to try contacting her again once\x01",
            "I get back to the foundation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(H-Hmm... As expected,\x01",
            "he's overprotective of\x01",
            "her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46BE")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_426A end

    def Function_14_46C7(): pass

    label("Function_14_46C7")

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
            "#11POh, you guys, huh. It's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2990, 1300, 3770, 2000)
    MoveCamera(49, 15, 0, 2000)
    OP_6E(440, 2000)
    SetCameraDistance(19900, 2000)

    def lambda_47C6():
        OP_96(0xFE, 0xBB8, 0x0, 0xEBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47C6)
    Sleep(400)

    def lambda_47E3():
        OP_96(0xFE, 0x6A4, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47E3)
    Sleep(400)

    def lambda_4800():
        OP_96(0xFE, 0xCE4, 0x0, 0xAD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4800)
    Sleep(400)

    def lambda_481D():
        OP_96(0xFE, 0x7D0, 0x0, 0x8DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_481D)
    WaitChrThread(0x101, 1)

    def lambda_483B():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_483B)
    WaitChrThread(0x102, 1)

    def lambda_484C():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_484C)
    WaitChrThread(0x109, 1)

    def lambda_485D():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_485D)
    WaitChrThread(0x105, 1)

    def lambda_486E():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_486E)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00000FHello, Master.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FIt's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHaha, well there's no\x01",
            "need to be so polite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBut the Testaments' leader has\x01",
            "joined the Special Support Section,\x01",
            "just like the rumors said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PMan, what a twist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe, thanks for that.\x02\x03",
            "#10302FBy the way, you refused me\x01",
            "before. Will you be able to\x01",
            "modify my weapons going forward?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A00():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4A00)

    def lambda_4A0D():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A0D)
    TurnDirection(0x102, 0x105, 500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FWazy, you're so\x01",
            "calculating...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHaha. Well, I suppose.\x02",
    )

    CloseMessageWindow()

    def lambda_4A9F():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4A9F)

    def lambda_4AAC():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AAC)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "#11PIf it's not for your\x01",
            "brawls, I'd be happy to\x01",
            "do it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FRepair workshop Guillaume\x01",
            "Factory.\x02\x03",
            "#10104FIt looks like you take weapon\x01",
            "modification requests in addition\x01",
            "to orbal goods repairs...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x109, 500)

    ChrTalk(
        0x8,
        (
            "#5POh, you're a new face\x01",
            "young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, regarding mods, I do\x01",
            "them only to the extent\x01",
            "that it's safe to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI got a business permit\x01",
            "recently, and won't be\x01",
            "accused of violating the law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, if you get your hands\x01",
            "on some good materials,\x01",
            "feel free to ask about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12PA-Alright, understood.\x02",
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
            "※At Guillaume Factory, you can\x01",
            "use \x07\x02",
            "U-Material\x07\x05",
            " to create weapons\x01",
            "that are stronger than normal.\x02\x03",
            "※By speaking to Guillaume at the\x01",
            "counter and selecting [Modify],\x01",
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

    # Function_14_46C7 end

    def Function_15_4E22(): pass

    label("Function_15_4E22")

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
            "#11PThat Randy! What's he\x01",
            "gone and done this\x01",
            "time!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe asked me to service\x01",
            "something totally\x01",
            "unusual...\x02",
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
            "#11PI was just finishing up\x01",
            "an all-nighter when he\x01",
            "forced it on me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FThen... About the\x01",
            ""something totally\x01",
            "unusual"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FWas it some kind of\x01",
            "heavy weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYeah... Although it was\x01",
            "in pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt hadn't been used in a while\x01",
            "so I tuned up the mechanism\x01",
            "parts and exhaust unit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTo build such a thing in the\x01",
            "first place, you'd have to\x01",
            "be some kinda crazy monster.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_51D3")

    ChrTalk(
        0x105,
        (
            "#10308FThere's no mistake. It's\x01",
            "the orbal rifle Randy\x01",
            "used.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5223")

    label("loc_51D3")


    ChrTalk(
        0x105,
        (
            "#10308FIt's just a guess, but\x01",
            "I'd say it's a custom\x01",
            "orbal rifle for Randy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5223")


    ChrTalk(
        0x101,
        (
            "#6P#00006FYeah... No doubt about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FMaster Guillaume, thank\x01",
            "you for the info.\x02",
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
            "#11PI don't know the\x01",
            "situation but... He had a\x01",
            "worried look on his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAs his friends, please\x01",
            "do all that you can for\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FRight!\x02",
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

    # Function_15_4E22 end

    def Function_16_538E(): pass

    label("Function_16_538E")

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
            "#00000FMaster Guilliaume, do you\x01",
            "have something like a metal\x01",
            "detector we can borrow?\x02",
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
            "I think I remember\x01",
            "making something like\x01",
            "that a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FBingo. I knew we could\x01",
            "count on an orbal\x01",
            "engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I did make it half\x01",
            "in fun, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What are ya usin' it\x01",
            "for?\x02",
        )
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
            "Explained they were\x01",
            "helping Kanon with the\x01",
            "scrap collection.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "I see... In that case,\x01",
            "you'll definitely need\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, I'll lend it to\x01",
            "ya.\x02",
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

    def lambda_567F():

        label("loc_567F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_567F")

    QueueWorkItem2(0x109, 0, lambda_567F)

    def lambda_5691():

        label("loc_5691")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5691")

    QueueWorkItem2(0x102, 0, lambda_5691)

    def lambda_56A3():

        label("loc_56A3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_56A3")

    QueueWorkItem2(0x104, 0, lambda_56A3)

    def lambda_56B5():

        label("loc_56B5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_56B5")

    QueueWorkItem2(0x101, 0, lambda_56B5)

    def lambda_56C7():

        label("loc_56C7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_56C7")

    QueueWorkItem2(0x105, 0, lambda_56C7)

    def lambda_56D9():

        label("loc_56D9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_56D9")

    QueueWorkItem2(0x103, 0, lambda_56D9)
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
        "Ah, here it is. Take it.\x02",
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
            "#00205FIt's really well made.\x02\x03",
            "#00203FI think it's equal to\x01",
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
            "Gahaha, well, at least\x01",
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
        (
            "So, ya know how ta use\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FI've used them many\x01",
            "times for customs\x01",
            "inspections.\x02\x03",
            "#10102FWe should activate it in\x01",
            "places there's likely to\x01",
            "be metal, right?\x02",
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
            "where there's a response, you\x01",
            "should find some metal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You might find some\x01",
            "other things too, if\x01",
            "you're lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... Got it.\x02\x03",
            "#00000FAlright, we'll put it to\x01",
            "good use.\x02",
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
            "Use it by pressing [△+Ｌ buttons].\x02\x03",
            "※You can also use it from [ITEMS]\x01",
            "in the camp menu.\x07\x00\x02",
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

    # Function_16_538E end

    def Function_17_5B46(): pass

    label("Function_17_5B46")

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
        (
            "#10300FHehe. Hard at work, I\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FWazy... And the Support\x01",
            "Section too.\x02",
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
            "There's still a lot of\x01",
            "damage left, and progress\x01",
            "has been slow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThat's right, the\x01",
            "demonized Wald attacked\x01",
            "Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FDo the citizens know\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FNo... Hardly anyone\x01",
            "noticed outside of the\x01",
            "Vipers.\x02\x03",
            "It must be because he\x01",
            "appeared in that\x01",
            "grotesque form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt's too shocking...\x01",
            "It's better to keep this\x01",
            "from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100F...Let's set that question aside for\x01",
            "now.\x02\x03",
            "What's important right now is to\x01",
            "decide how to proceed with the\x01",
            "reconstruction work.\x02\x03",
            "Here in Downtown, we can't count on\x01",
            "government assistance. And we haven't\x01",
            "the funds to employ merchants.\x02\x03",
            "It would be a great help if the\x01",
            "Support Section would lend us their\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FLet me think...\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_17_5B46 end

    def Function_18_6057(): pass

    label("Function_18_6057")

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
            "Help with reconstruction\x01",      # 0
            "Think about it for now\x01",        # 1
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
        (0, "loc_60D7"),
        (1, "loc_60E7"),
        (SWITCH_DEFAULT, "loc_6244"),
    )


    label("loc_60D7")

    OP_29(0x8E, 0x4, 0x2)
    SetScenarioFlags(0x196, 0)
    Call(0, 20)
    Jump("loc_6244")

    label("loc_60E7")


    ChrTalk(
        0x101,
        (
            "#00006FWe want to help, but...\x01",
            "It depends on how our\x01",
            "other work goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBy the way, can we\x01",
            "accept later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FYeah. If you can help,\x01",
            "the timing doesn't\x01",
            "matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I won't force you.\x01",
            "Help us if you get free,\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. We'll do\x01",
            "whatever we can.\x02",
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
    Jump("loc_6244")

    label("loc_6244")

    Return()

    # Function_18_6057 end

    def Function_19_6245(): pass

    label("Function_19_6245")

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
            "#04100FHmm, so you'll help with\x01",
            "the Downtown\x01",
            "reconstruction work?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_19_6245 end

    def Function_20_6356(): pass

    label("Function_20_6356")


    ChrTalk(
        0x101,
        "#00000FYeah, leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04100FI thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, I thought you guys\x01",
            "might say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FSo, how can we help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FRight now, work is occurring in\x01",
            "three places primarily.\x02\x03",
            "Firstly, emergency food\x01",
            "distribution out of Lotus\x01",
            "Heights.\x02\x03",
            "Secondly, scrap metal recovery\x01",
            "near Maison Imelda.\x02\x03",
            "And finally, building material\x01",
            "collection and processing here\x01",
            "in Guillaume Factory.\x02\x03",
            "I would like the support\x01",
            "section to go to each place and\x01",
            "help with whatever's needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI see... So each of\x01",
            "those activities is\x01",
            "important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FBy the way, what about\x01",
            "the work that's\x01",
            "occurring here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right, we're gathering\x01",
            "materials to repair our\x01",
            "damaged buildings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For now, I can use the\x01",
            "workshop's left over\x01",
            "materials, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just earlier, I noticed\x01",
            "a big problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FA problem? What kind of\x01",
            "problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To be frank, I don't have\x01",
            "enough screws and nails to\x01",
            "assemble the materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I won't be able to\x01",
            "repair anything at this\x01",
            "rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FYou can't use any of the\x01",
            "waste lying around\x01",
            "outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FHmm, I asked that Kanon\x01",
            "kid for help with it for\x01",
            "the time being, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if I had to say\x01",
            "it, they're doing\x01",
            "fundraising for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Additionally, there's a question\x01",
            "of how strong they are, so I'd\x01",
            "like to use new wherever possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FMan, that sounds like\x01",
            "quite the predicament.\x02\x03",
            "#10300FThen, you just need us\x01",
            "to bring you some screws\x01",
            "and nails?\x02",
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
            "What I really need is\x01",
            "that "U-Material" used\x01",
            "for remodeling arms.\x02",
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
            "#00203FU-Material, you say...\x01",
            "That seems pretty tough\x01",
            "to find.\x02\x03",
            "#00200FHow many do you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I think 10 should\x01",
            "do nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Can I ask you guys for\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. We'll bring\x01",
            "them here once we've\x01",
            "collected them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FWe're counting on you,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_6ACA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6ACA)
    Sleep(250)

    def lambda_6ADA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6ADA)
    Sleep(50)

    def lambda_6AEA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6AEA)
    Sleep(50)

    def lambda_6AFA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6AFA)
    Sleep(50)

    def lambda_6B0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6B0A)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004FAlright, let's get\x01",
            "started.\x02\x03",
            "#00000FLet's ask about scrap\x01",
            "collection and emergency\x01",
            "food distribution too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FRoger, leader.\x02\x03",
            "When my old haunt's in a\x01",
            "pinch, I'm glad to pitch\x01",
            "in and help.\x02",
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
            "Quest [Downtown\x01",
            "Reconstruction: Help\x01",
            "Wanted]\x07\x00",
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

    # Function_20_6356 end

    def Function_21_6C9E(): pass

    label("Function_21_6C9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x38E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D47")

    ChrTalk(
        0x8,
        (
            "Did you get that\x01",
            "U-Material for me?\x02",
        )
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
            "in advance for your\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB5")

    label("loc_6D47")


    ChrTalk(
        0x8,
        (
            "Oh... Looks like you've\x01",
            "gathered them.\x02",
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
            "Hand them over\x01",      # 0
            "Don't\x01",               # 1
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
        (0, "loc_6E09"),
        (1, "loc_6E11"),
        (SWITCH_DEFAULT, "loc_6EB5"),
    )


    label("loc_6E09")

    Call(0, 22)
    Jump("loc_6EB5")

    label("loc_6E11")


    ChrTalk(
        0x8,
        (
            "I see. Well, it can't be\x01",
            "helped. You guys must\x01",
            "need 'em yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you do have the\x01",
            "spares, it'd be a big help\x01",
            "if you could hand them over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB5")

    label("loc_6EB5")

    Return()

    # Function_21_6C9E end

    def Function_22_6EB6(): pass

    label("Function_22_6EB6")

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
            "Hehe, thanks. Don't mind\x01",
            "if I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With this, the repair\x01",
            "prospects are looking\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha, we're happy to\x01",
            "help.\x02",
        )
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
            "#10109FYeah, we're good at\x01",
            "manual labor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, I can't ask that of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's only right for the\x01",
            "Downtown citizens to\x01",
            "repair Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FAbbas and the Testaments\x01",
            "will supervise them.\x02\x03",
            "#10309FWell, good luck with\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FYou act like you're not\x01",
            "one of them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04102FHaha it's fine. Wazy has\x01",
            "his own role to play.\x02\x03",
            "#04100FI thank you again,\x01",
            "Special Support Section.\x02\x03",
            "If you're still free,\x01",
            "please help at the other\x01",
            "stations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 2)
    OP_29(0x8E, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73AA")

    ChrTalk(
        0x101,
        (
            "#00000FYeah, leave it to us.\x02\x03",
            "#00005FSay, we've helped at all\x01",
            "the main stations,\x01",
            "haven't we...\x02\x03",
            "#00000FNext, let's patrol\x01",
            "Downtown helping with\x01",
            "the small stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FThanks for all your\x01",
            "help. I'll see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Jump("loc_73C8")

    label("loc_73AA")


    ChrTalk(
        0x101,
        "#00000FAlright, we will.\x02",
    )

    CloseMessageWindow()

    label("loc_73C8")

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

    # Function_22_6EB6 end

    def Function_23_7425(): pass

    label("Function_23_7425")

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
        "#04100FHow did it go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could it be that you've\x01",
            "finished helping\x01",
            "everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we helped out with\x01",
            "everyone's main needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FI see... Good work.\x02\x03",
            "It's almost time for the\x01",
            "emergency food distribution. You\x01",
            "should kill time until then.\x02",
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
            "#04100FThanks for all your\x01",
            "help. I'll see you\x01",
            "later.\x02",
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

    # Function_23_7425 end

    SaveToFile()

Try(main)
