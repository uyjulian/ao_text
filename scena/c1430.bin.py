from ScenarioHelper import *

def main():
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
        "Guillaume Masakata",           # 1
        "Roberts boss",           # 2
        "Abbas",               # 3
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
        "Function_6_851",          # 06, 6
        "Function_7_21EB",         # 07, 7
        "Function_8_27E6",         # 08, 8
        "Function_9_2921",         # 09, 9
        "Function_10_3082",        # 0A, 10
        "Function_11_3B69",        # 0B, 11
        "Function_12_4056",        # 0C, 12
        "Function_13_4060",        # 0D, 13
        "Function_14_443E",        # 0E, 14
        "Function_15_4B57",        # 0F, 15
        "Function_16_5094",        # 10, 16
        "Function_17_5822",        # 11, 17
        "Function_18_5CEB",        # 12, 18
        "Function_19_5EEA",        # 13, 19
        "Function_20_5FEE",        # 14, 20
        "Function_21_686E",        # 15, 21
        "Function_22_6A5C",        # 16, 22
        "Function_23_6FAF",        # 17, 23
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B8")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "talk")
    MenuCmd(1, 0, "Ask for remodeling")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_598")
    MenuCmd(1, 0, "Pass U material")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C0")
    MenuCmd(1, 0, "Ask about metal detector")

    label("loc_5C0")

    MenuCmd(1, 0, "quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_601")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_625")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_625")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648")
    OP_AF(0xAD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_671")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671")
    Call(0, 21)
    Return()

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Return()

    label("loc_6A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B3")

    label("loc_6B3")

    Jump("loc_53E")

    label("loc_6B8")

    Jump("loc_850")

    label("loc_6BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",              # 0
            "Ask for remodeling\x01",            # 1
            "Ask for creation of weapons\x01",      # 2
            "quit\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_778")

    label("loc_738")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "Ask for remodeling\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_778")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_778")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_794")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_794")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7B3")
    OP_AF(0xAE)
    Jump("loc_7F5")

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7C3")
    OP_AF(0xAD)
    Jump("loc_7F5")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D3")
    OP_AF(0xAC)
    Jump("loc_7F5")

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7EC")
    OP_AF(0xAF)
    Jump("loc_7EE")

    label("loc_7EC")

    OP_AF(0xAB)

    label("loc_7EE")

    Jump("loc_7F5")

    label("loc_7F3")

    OP_AF(0xAA)

    label("loc_7F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84B")

    label("loc_804")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")
    Call(0, 10)
    Jump("loc_84B")

    label("loc_81B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82F")
    Jump("loc_84B")

    label("loc_82F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_84B")

    Jump("loc_6C7")

    label("loc_850")

    Return()

    # Function_5_514 end

    def Function_6_851(): pass

    label("Function_6_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986")

    ChrTalk(
        0x8,
        (
            "Such a thing appeared … …\x01",
            "It is a foolish thing that I got the hardest thing again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "… …. you, that \"big tree\"\x01",
            "If you plan to get in,\x01",
            "Keep preparing thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Melancholic guys\x01",
            "If you are trying to be a partner, you can also strengthen your weapons\x01",
            "It is too much from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah … well, thanks!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A10")

    label("loc_986")


    ChrTalk(
        0x8,
        (
            "You guys are also serious … …\x01",
            "You definitely do not get frustrated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I could only do the remodeling of weapons,\x01",
            "Because I will do as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A10")

    Jump("loc_21EA")

    label("loc_A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBC")

    ChrTalk(
        0x8,
        (
            "You …\x01",
            "Haha, was it safe!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With Dudley and others\x01",
            "You seem to have joined successfully?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thanks to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FGuillaume's Osan,\x01",
            "Repair of \"Berserger\" …\x01",
            "Again with you.\x02\x03",
            "#00300FWhile I am outside the city\x01",
            "I was saved a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, that's good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, there is a weak point in the engineering department\x01",
            "Keep it in your head properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That monster rifle,\x01",
            "If you break this time immediately you can fix it\x01",
            "Guarantee from hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, when I use it\x01",
            "It's only in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Okay, I hope I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The president side also, what kind of hand\x01",
            "I do not know whether to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys also maintain weapons\x01",
            "Keep it firm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, thank you for your help.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 3)
    Jump("loc_D2A")

    label("loc_CBC")


    ChrTalk(
        0x8,
        (
            "The president side also, what kind of hand\x01",
            "I do not know whether to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys also maintain weapons\x01",
            "Keep it firm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A")

    Jump("loc_21EA")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(
        0x8,
        (
            "Is it a defense army in the crossbell independent country ……\x01",
            "Well, it was disappointing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Have you been told this story?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNo, we were all new ears.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FWell, anyway now\x01",
            "I am gathering information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That's right … … you too hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think that there are various things in the future,\x01",
            "Keep it like hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FAh.\x01",
            "Thank you, Osan.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F29")

    label("loc_EAF")


    ChrTalk(
        0x8,
        (
            "But well, against the two major countries\x01",
            "This also sells quarrels dignified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway … for a while\x01",
            "I have to watch the progression.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F29")

    Jump("loc_21EA")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FEB")

    ChrTalk(
        0x8,
        (
            "Currently in the daytime, the reconstruction relationship,\x01",
            "In the night I feel like a studio relationship\x01",
            "I have my job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you I have no time to rest,\x01",
            "Some kind of dependency is\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1071")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "For the blade rifle\x01",
            "Somehow in the day after tomorrow\x01",
            "I will repair it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, until then\x01",
            "Please wait at best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_1071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_END)), "loc_10E3")

    ChrTalk(
        0x8,
        (
            "Well, at once\x01",
            "Do you process U material?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Thank you so much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1189")

    label("loc_10E3")


    ChrTalk(
        0x8,
        (
            "Currently in the daytime, the reconstruction relationship,\x01",
            "In the night I feel like a studio relationship\x01",
            "I have my job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to you I have no time to rest,\x01",
            "Some kind of dependency is\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1189")

    Jump("loc_121B")

    label("loc_118E")


    ChrTalk(
        0x8,
        (
            "I also like soup broth earlier\x01",
            "We received it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Plenty of energy\x01",
            "I had you fill it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hello, thanks\x01",
            "Work is also fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121B")

    Jump("loc_21EA")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12B7")

    ChrTalk(
        0x8,
        (
            "Randy's guy, pretty much\x01",
            "I gave up my thoughtful face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not know detailed circumstances ……\x01",
            "At such times, you guys\x01",
            "I will support you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_12B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_141B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(
        0x8,
        "The leadership derailed yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anything I heard suddenly Dekae\x01",
            "She seems to have taken off the train … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you also want to brag about the train opponent?\x01",
            "It is a story that I do not understand well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1416")

    label("loc_138C")


    ChrTalk(
        0x8,
        (
            "What are the compounds that attacked the train?\x01",
            "What on earth did you want to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No way I'm proud of my strength …\x01",
            "I do not understand it anyhow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1416")

    Jump("loc_21EA")

    label("loc_141B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_154A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C4")

    ChrTalk(
        0x8,
        "Cattle, this is the end of the repair of the guide light.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What's next?\x01",
            "It's maintenance of the tactical auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all, for inspection\x01",
            "Prepare crystal circuit, and …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1545")

    label("loc_14C4")


    ChrTalk(
        0x8,
        (
            "Crystal circuit, crystal circuit …\x01",
            "Oops, this one\x01",
            "It is a standard a generation ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wait, as usual\x01",
            "I do not want to confuse it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1545")

    Jump("loc_21EA")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15D6")

    ChrTalk(
        0x8,
        (
            "Well, next time you repair the lights … …\x01",
            "Indeed, about five cases have been accumulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, by lunch time\x01",
            "Do you want to clean up with cigarette?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_171A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1699")

    ChrTalk(
        0x8,
        (
            "Although various discussions have been done,\x01",
            "The independence problem is horribly\x01",
            "It's a delicate problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It is said that there are already a number of people who agree,\x01",
            "How much human beings constantly value the importance of things\x01",
            "I guess you are grasping it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1715")

    label("loc_1699")


    ChrTalk(
        0x8,
        (
            "What advocacy of independence brings … …\x01",
            "To be honest I also do not know well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, as before\x01",
            "It is a place to worry about trends in 2 major countries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1715")

    Jump("loc_21EA")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD6")

    ChrTalk(
        0x8,
        (
            "Yo, Lady.\x01",
            "Apparently the work of the Foundation\x01",
            "It seems to have a delimiter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FYes, if anything\x01",
            "It is a feeling that I forced it.\x02\x03",
            "#00200Fby the way……\x01",
            "The boss regularly goes here\x01",
            "You are making a face, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, well.\x01",
            "Even before this design drawing of the new magician\x01",
            "It is a place I left behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oops, this story is to young lady\x01",
            "I guess I could not say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Roberts' guy, I'm out of laziness.\x01",
            "Do not tell me what I said?\x02",
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
            "#00203F…… No, do not mind.\x02\x03",
            "#00211FThe chief is responsible for remodeling the magician\x01",
            "What is involved is,\x01",
            "I was almost convinced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As my girl knows as well,\x01",
            "The magical structure of a magical wand is\x01",
            "It's terribly complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if I am a treasure, without anyone's cooperation\x01",
            "It is from tiptoe with tears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FEr, to me\x01",
            "I do not quite understand it ….\x02\x03",
            "#10100FHow come Roberts?\x01",
            "To that, to Tio\x01",
            "Will it be a secret?\x02\x03",
            "#10106FThat way too much\x01",
            "It is said that it is hollowing or something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FHey, what should I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe also talk about that person\x01",
            "I do not understand well ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah … but probably\x01",
            "This is also a kind of conscience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F………………………………\x01",
            "I do not want to understand,\x01",
            "I think that's the place.\x02\x03",
            "#00200FAnyway, to interact with the magician#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#\x01",
            "about#8R噵 噵 噵 噵#I got used to it.\x02\x03",
            "#00204FDo not mind too much of you too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 3)
    Jump("loc_1D41")

    label("loc_1CD6")


    ChrTalk(
        0x8,
        (
            "Well, for the time being, Miss Lady's magic wand is also\x01",
            "I can do it remodeling at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please tell me when you need it anytime.\x02",
    )

    CloseMessageWindow()

    label("loc_1D41")

    Jump("loc_21EA")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E44")

    ChrTalk(
        0x8,
        (
            "What is the Orchise Tower a while ago?\x01",
            "I caught a glimpse of you,\x01",
            "What … what a hell out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The state-of-the-art facilities\x01",
            "I am interested as a technology store … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What kind?\x01",
            "Try showing off \"power\"\x01",
            "I do not like him anyhow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EDB")

    label("loc_1E44")


    ChrTalk(
        0x8,
        (
            "The Orkis Tower is,\x01",
            "It is totally outrageous building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The state-of-the-art facilities\x01",
            "I am interested as a technology store … …\x01",
            "You do not like me anyhow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDB")

    Jump("loc_21EA")

    label("loc_1EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F69")

    ChrTalk(
        0x8,
        (
            "Also,\x01",
            "Afterwards Mr. Thio\x01",
            "It is only to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heck, I will give that magician again as soon as possible.\x01",
            "Try it and it 's funny.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_1F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_20A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2037")

    ChrTalk(
        0x8,
        "It is rare today that it will rain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's damp and enemy …\x01",
            "Wow, this moisture is\x01",
            "Something troublesome for precision machinery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When fiddling with the engine department something\x01",
            "I will use pretty neurons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A3")

    label("loc_2037")


    ChrTalk(
        0x8,
        (
            "If you are humid,\x01",
            "Something troublesome for precision machinery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When fiddling with the engine department something\x01",
            "I will use pretty neurons.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A3")

    Jump("loc_21EA")

    label("loc_20A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217C")

    ChrTalk(
        0x8,
        (
            "Asking for the remodeling of weapons\x01",
            "Please feel free to call out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As I mentioned earlier, even in the past\x01",
            "Material engineering at the Epstein Foundation\x01",
            "There are things I was specializing in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Do not you trust your arms?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21EA")

    label("loc_217C")


    ChrTalk(
        0x8,
        (
            "Asking for the remodeling of weapons\x01",
            "Please feel free to call out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it is such a nurse,\x01",
            "Do not you trust your arms?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EA")

    Return()

    # Function_6_851 end

    def Function_7_21EB(): pass

    label("Function_7_21EB")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x104, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Ou, that's Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The blade rifle I was asked for\x01",
            "It's about repairing ……\x01",
            "Wait a little more, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOf course it does not matter …\x02\x03",
            "#00301FWas it also a problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A problem, chan\x01",
            "It's almost an original part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Replacement of parts is also ineffective,\x01",
            "When trying to reproduce, by all means\x01",
            "It takes time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, that your cousin used it\x01",
            "Chainsaw rifle than Mon\x01",
            "It seems that something will still be in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F\"Tester = Rossa\" or …\x01",
            "Ah, it is a thing, it is a substitute.\x02\x03",
            "#00301FTo be masterful like a girl never\x01",
            "Although I did not expect it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "\"Red head#6RTester-Rossa#\"…\x01",
            "It comes out in an old tale around the empire\x01",
            "It is the name of a devil with a thousand weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I, too, to the weapon that I finished before\x01",
            "I have ever given the same name … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Apparently completely\x01",
            "It seems that you are getting overwhelmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, do not mind.\x02\x03",
            "#00308FIn any case, the source is\x01",
            "It is a rather special weapon workshop … …\x02\x03",
            "#00301FAnd it's a special order item\x01",
            "That is certainly tough.\x02\x03",
            "#00306FSorry, Osan.\x01",
            "Let me take time and effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heck, thanks well\x01",
            "Let me study.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Technologies that could be used for remodeling armor too\x01",
            "I could discover it a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, for another week to drift\x01",
            "I guess it's a fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThat's right, but now it's about reconstruction\x01",
            "I am busy with work.\x02\x03",
            "#00304FBecause I do not scorch,\x01",
            "You do not have to hurry and be surprised?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heck, the brat is brought together\x01",
            "You do not care about the Osan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, once the repair is over\x01",
            "I will also contact you from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Until then, wait for at most.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302Fmy mother……\x01",
            "I am saved, Osan.\x02\x03",
            "Surely, I left it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x18D, 5)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_21EB end

    def Function_8_27E6(): pass

    label("Function_8_27E6")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Oh, is not Randy?\x01",
            "Finally I returned to the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, thanks, sir.\x02\x03",
            "#00304FAnyway, if there is another opportunity\x01",
            "I will ask you to strengthen your weapons, Osassu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh yes, even the material is\x01",
            "Do it at any time and do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you also\x01",
            "You are at the greatest possible to skip it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x14D, 2)
    Return()

    # Function_8_27E6 end

    def Function_9_2921(): pass

    label("Function_9_2921")

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
            "#11PBut what is outrageous\x01",
            "It has come to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI, too, to you something\x01",
            "I helped out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P…… I wish I had \"that\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F\"that\"……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P\"Zemria stone\"\x01",
            "A relic of ancient civilization\x01",
            "There is a metal being told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PFormerly, some great scholar\x01",
            "Finally I found a processing method,\x01",
            "It is a rare and hard substitute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf there is that, I am designing it now\x01",
            "You ought to be able to build weapons.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_END)), "loc_2C42")

    ChrTalk(
        0x8,
        (
            "#11PFormerly, I made it for you\x01",
            "I'll give you even more than a weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FMore than before …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FThat guy is bad … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C86")

    label("loc_2C42")


    ChrTalk(
        0x104,
        "#6P#00305FSomething weapons …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105Freally! Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_2C86")


    ChrTalk(
        0x103,
        (
            "#12P#00202FThis is the situation, and strong weapons\x01",
            "I would like a hand out from his throat, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, as long as there is material\x01",
            "I can make it even soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, even small pieces\x01",
            "About five, to build weapons\x01",
            "It should be enough, but ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_END)), "loc_2ECE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石碎片', 0x0)"), scpexpr(EXPR_END)), "loc_2E31")

    ChrTalk(
        0x101,
        (
            "#6P#00000F(Zemuria Stone ……\x01",
            "Just fortune teller\x01",
            "I just got it. )\x02\x03",
            "#00003F(It is a piece ……\x01",
            "Just like that\x01",
            "Like having it. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC9")

    label("loc_2E31")


    ChrTalk(
        0x101,
        (
            "#6P#00000F(Zemuria Stone ……\x01",
            "Just fortune teller\x01",
            "I just got it. )\x02\x03",
            "#00003F(It is a piece ……\x01",
            "You may try looking. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC9")

    Jump("loc_2F17")

    label("loc_2ECE")


    ChrTalk(
        0x101,
        (
            "#6P#00003F(It is a piece …… That reminds me,\x01",
            "You seem to have such a thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F17")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PCover\x01",
            "Perhaps perhaps heart?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POkay, I guess so\x01",
            "Prepare to make weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P\"Zemria stone\" or\x01",
            "If you get 5 \"pieces\" of it,\x01",
            "Talk to me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PBecause we will build weapons soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, I understand.\x02",
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

    # Function_9_2921 end

    def Function_10_3082(): pass

    label("Function_10_3082")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3323")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_END)), "loc_31D9")

    ChrTalk(
        0x8,
        (
            "#11PThat's Zemria Stone …!\x01",
            "Haha, did you get in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you use that,\x01",
            "I can build a weapon for one person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3255")

    label("loc_31D9")


    ChrTalk(
        0x8,
        (
            "#11POh, fragments of Zemria Stone ……\x01",
            "Five pieces gathered!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you use that,\x01",
            "I can build a weapon for one person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3255")


    ChrTalk(
        0x8,
        (
            "#11PIt is set to work anytime … …\x01",
            "… … How are you going to try it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHello, it's okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhich weapons to build,\x01",
            "Please think carefully and choose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_334F")

    label("loc_3323")


    ChrTalk(
        0x8,
        "#11PWho is the weapon you want to build?\x02",
    )

    CloseMessageWindow()

    label("loc_334F")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Infinity (Lloyd)\x01",        # 0
            "Exceli Lei (Eli)\x01",        # 1
            "Cosmo Collapse (Tio)\x01",        # 2
            "Dinotic Abyss (Randy)\x01",      # 3
            "Ark Soleil (Noel)\x01",        # 4
            "Seventh arm (Wadi)\x01",          # 5
            "Daisuke Ken (Leisha)\x01",      # 6
            "Himmeltroa (Dudley)\x01",      # 7
            "quit\x01",                                # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD1")

    ChrTalk(
        0x101,
        (
            "#6P#00000FSo, this weapon\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_END)), "loc_3518")
    SubItemNumber('塞姆里亚石', 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_3566")

    label("loc_3518")

    SubItemNumber('塞姆里亚石碎片', 5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I handed five pieces.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_3566")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#11POkay, so yeah then\x01",
            "Let's warm arm!\x02",
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
            "#11PWell … I can do it.\x01",
            "Do not accept it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3681")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '无限之光'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('无限之光', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3681")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E2")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '能天使威光'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('能天使威光', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_36E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3743")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '宇宙崩坏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('宇宙崩坏', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A4")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '屠龙深渊'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('屠龙深渊', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_37A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3805")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '日耀弧光'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('日耀弧光', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3866")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '七耀圣腕'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('七耀圣腕', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3866")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C7")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '曳影之剑'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('曳影之剑', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_38C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3923")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '制裁'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('制裁', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A39")

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you, Guillaume Master.\x01",
            "You surely let me use it effectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHehe, that's good.\x01",
            "I can handle such materials\x01",
            "I'm also a monk to exhaust as a technician.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWith this guy, you can use Crossbell incidents\x01",
            "Please do it firmly to solve it!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E0(0x14, 0x0)
    SetScenarioFlags(0x18B, 1)
    Jump("loc_3AC9")

    label("loc_3A39")


    ChrTalk(
        0x8,
        (
            "#11PBecause it is such a time\x01",
            "This one should be useful as well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PBe honest, do it firmly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, I will take care of it carefully.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3AC9")

    ClearScenarioFlags(0x0, 3)
    Jump("loc_3B39")

    label("loc_3AD1")


    ChrTalk(
        0x8,
        "#11PReally? Well it's a way to get lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POnce we've decided what weapon we want to build\x01",
            "Please give me a voice again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3B39")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_3082 end

    def Function_11_3B69(): pass

    label("Function_11_3B69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA2")
    Call(0, 17)
    Return()

    label("loc_3BA2")

    Call(0, 19)
    Return()

    label("loc_3BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC8")
    Call(0, 23)
    Return()

    label("loc_3BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE8")
    SetScenarioFlags(0x191, 5)
    TalkBegin(0xFE)

    ChrTalk(
        0x105,
        (
            "#10300FSo, Abbas is here\x01",
            "What are you doing to help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FOh, now as far as I can\x01",
            "Repairing and processing of building materials\x01",
            "I am being helped.\x02\x03",
            "#04102FAlthough unexpectedly a lot of detailed work,\x01",
            "It is quite fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIt's fun, or …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSurely, Mr. Abbas\x01",
            "Cooking in Trinity\x01",
            "Was it being done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FOh, before.\x02\x03",
            "Recently to Liang and Azer\x01",
            "It is trustworthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHugh, Abbas looks like this\x01",
            "Because the hands are dexterous.\x02\x03",
            "#10304FOf course not only cooking and work,\x01",
            "Even sewing is a fun thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, that guy\x01",
            "I feel like a new side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWhat I should say …\x01",
            "He seemed to be a good husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, but not much.\x01",
            "It seems to be hidden elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuh, I will tell you\x01",
            "Abbas is only me\x01",
            "Because it's stuff\x02\x03",
            "#10304FWell, as long as rental\x01",
            "You may think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#04100F…… What on earth are you talking about?\x02\x03",
            "Anyway, I will stay for a while\x01",
            "Here I will help Guillaumemaster\x01",
            "I'm planning to do it.\x02\x03",
            "If there is something, come anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, ah ……\x02\x03",
            "#00003F(Abbas? ….\x01",
            "It is a very mysterious person. )\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_4055")

    label("loc_3FE8")

    TalkBegin(0xFE)

    ChrTalk(
        0xA,
        (
            "#04100FI will stay here for a while\x01",
            "Guillaume helping the boss\x01",
            "I'm planning to do it.\x02\x03",
            "If there is something, come anytime.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_4055")

    Return()

    # Function_11_3B69 end

    def Function_12_4056(): pass

    label("Function_12_4056")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_12_4056 end

    def Function_13_4060(): pass

    label("Function_13_4060")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4356")

    ChrTalk(
        0x9,
        (
            "Well, this is\x01",
            "Now used by Tio\x01",
            "It is a design drawing of a magazine ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, this is also a high output\x01",
            "It is a construction that I can expect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lady, when her lady got home\x01",
            "I will make it available.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, it really helps me ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even after Tio returned by this\x01",
            "It seems that you can use the magician without delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's it, my girlfriend, something back home\x01",
            "I heard that it is prolonged?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, that's right!\x01",
            "It seems that the work has increased a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if communication is made every other hour recently\x01",
            "Because it rarely responds,\x01",
            "I do not care!\x02",
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
        "…… That's right, that's the cause.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Roberts, Chief, as usual … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_4435")

    label("loc_4356")


    ChrTalk(
        0x9,
        (
            "Tio, you have dinner\x01",
            "Are you eating properly?\x01",
            "It is impossible or impossible to break your body ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahhh, I got worried again ~!\x01",
            "I will try to communicate again when I return to the Foundation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(No……\x01",
            "You are too overprotective as expected. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4435")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_4060 end

    def Function_14_443E(): pass

    label("Function_14_443E")

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
            "#11POh, you guys.\x01",
            "It's been a while sincerely.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2990, 1300, 3770, 2000)
    MoveCamera(49, 15, 0, 2000)
    OP_6E(440, 2000)
    SetCameraDistance(19900, 2000)

    def lambda_4541():
        OP_96(0xFE, 0xBB8, 0x0, 0xEBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4541)
    Sleep(400)

    def lambda_455E():
        OP_96(0xFE, 0x6A4, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_455E)
    Sleep(400)

    def lambda_457B():
        OP_96(0xFE, 0xCE4, 0x0, 0xAD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_457B)
    Sleep(400)

    def lambda_4598():
        OP_96(0xFE, 0x7D0, 0x0, 0x8DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4598)
    WaitChrThread(0x101, 1)

    def lambda_45B6():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45B6)
    WaitChrThread(0x102, 1)

    def lambda_45C7():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_45C7)
    WaitChrThread(0x109, 1)

    def lambda_45D8():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45D8)
    WaitChrThread(0x105, 1)

    def lambda_45E9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_45E9)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00000FHello, my boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100Flong time no see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, so much\x01",
            "Do not be confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHowever, I heard about rumors,\x01",
            "Testers' leader\x01",
            "Do not join the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI was bruised at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, that kind of.\x02\x03",
            "#10302FBy the way it was declined before,\x01",
            "In the future I will also remodel my gifts\x01",
            "You take care of it, are not you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4771():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4771)

    def lambda_477E():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_477E)
    TurnDirection(0x102, 0x105, 500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FWadi, I can not do such a thing …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWell, that's right.\x02",
    )

    CloseMessageWindow()

    def lambda_4810():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4810)

    def lambda_481D():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_481D)
    TurnDirection(0x102, 0x8, 500)

    ChrTalk(
        0x8,
        (
            "#11PI do not use it for a fight\x01",
            "May I ask you to ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FRepair shop \"Guillaume Studio\".\x02\x03",
            "#10104FIn addition to repairing the conductive products,\x01",
            "Weapon remodeling etc\x01",
            "I heard that he is undertaking … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x109, 500)

    ChrTalk(
        0x8,
        "#5POisa is also a new face.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, even if I remodel it\x01",
            "At most not to risk\x01",
            "It is about to strengthen the mon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI recently took business license,\x01",
            "I should not imitate touching the law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, if you get something good\x01",
            "Please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#12POk, yes, I understand.\x02",
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
            "※ \"Guillaume Studio\"\x01\x07\x02",
            "U material\x07\x05",
            "Using material items such as\x01",
            "Equipment that is more effective than normal can be obtained.\x02\x03",
            "Talk to Guillaume at the counter\x01",
            "If you select \"Ask for remodeling\"\x01",
            "A menu is displayed and you can modify it.\x07\x00\x02",
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

    # Function_14_443E end

    def Function_15_4B57(): pass

    label("Function_15_4B57")

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
        "#11POh, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PRandy's guy,\x01",
            "How the hell did you do? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSomething is unusual\x01",
            "I was asked for maintenance … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FIs that correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FIt is about this morning, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, around 5 o'clock\x01",
            "You visited a shop suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt was just the beginning of the night\x01",
            "I accepted it with the momentum … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FSo …\x01",
            "What is \"an unusual thing\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAs expected after all …\x01",
            "Is it kind of a heavy weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh … but,\x01",
            "It's just a rough unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI have not used it for a while\x01",
            "Engine part and exhaust unit etc\x01",
            "I did maintenance all the way … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAw, after assembling\x01",
            "I guess it will be a thing like a monster.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_4EE3")

    ChrTalk(
        0x105,
        (
            "#10308FRandy's using it\x01",
            "It seems that there is no mistake in the guiding rifle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2B")

    label("loc_4EE3")


    ChrTalk(
        0x105,
        (
            "#10308FTo be aware, Randy used it\x01",
            "Is it a custom-made guide rifle?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F2B")


    ChrTalk(
        0x101,
        (
            "#6P#00006FAh……\x01",
            "There is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FMr. Guillaume.\x01",
            "Thank you for the information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, that's good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI do not know the circumstances … …\x01",
            "A face that I thought for quite a while\x01",
            "I did it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou, my fellow\x01",
            "Be as powerful as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FI understand.\x02",
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

    # Function_15_4B57 end

    def Function_16_5094(): pass

    label("Function_16_5094")

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
            "#00000FEr, Guillaume Parents ……\x01",
            "I like something like a metal detector\x01",
            "Do you have it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "A metal detector…?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Indeed this kind of thing\x01",
            "I remember making it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FOh, it's a bingo.\x01",
            "As expected it is an orbient technician.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, almost half of the play\x01",
            "I made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "But it looks like you have a good use in mind\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, that is\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "With Cannon's help\x01",
            "We explained that waste material recovery is carried out.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "I see……\x01",
            "Well it certainly seems necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Okay, you guys\x01",
            "I will lend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wait a second, certainly in the back\x01",
            "It should have been okay.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5365():

        label("loc_5365")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5365")

    QueueWorkItem2(0x109, 0, lambda_5365)

    def lambda_5377():

        label("loc_5377")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5377")

    QueueWorkItem2(0x102, 0, lambda_5377)

    def lambda_5389():

        label("loc_5389")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5389")

    QueueWorkItem2(0x104, 0, lambda_5389)

    def lambda_539B():

        label("loc_539B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_539B")

    QueueWorkItem2(0x101, 0, lambda_539B)

    def lambda_53AD():

        label("loc_53AD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53AD")

    QueueWorkItem2(0x105, 0, lambda_53AD)

    def lambda_53BF():

        label("loc_53BF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53BF")

    QueueWorkItem2(0x103, 0, lambda_53BF)
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
            "It was there.\x01",
            "Huh, do not accept it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '金属探测器'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('金属探测器', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        (
            "#00205FIt looks better made than I was expecting\x02\x03",
            "#00203FEven what is used by police\x01",
            "It might be comparable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FWell, that is fine.\x01",
            "It is amazing …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it looks like\x01",
            "Firmly arrange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Actually, fuel economy of the guide is bad\x01",
            "I was able to boast so much\x01",
            "I'm not a monk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You know how to use it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FSeveral times in immigration inspection\x01",
            "I have used it.\x02\x03",
            "#10102FIn places where metal is likely\x01",
            "Is it okay to start it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Good that sounds good\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Where the reaction is likely to occur\x01",
            "If you investigate carefully\x01",
            "You should find the metal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also, good luck\x01",
            "You may find other monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see……\x01",
            "I understand.\x02\x03",
            "#00000FOk then we'll put it to good use\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ Metal Detector is in the old city\x01",
            "It can only be used on outdoor maps.\x01",
            "Use it with \"△ button + L button\".\x02\x03",
            "※ Also, from the camp menu\x01",
            "It can also be used from [ITEMS].\x07\x00\x02",
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

    # Function_16_5094 end

    def Function_17_5822(): pass

    label("Function_17_5822")

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
        "#10300FHehe, you're working hard\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FWadi\x01",
            "Are they also part of the support department?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, you saw our request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, for now tentatively\x01",
            "I thought about asking about the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FAs far as seeing the outside,\x01",
            "The reconstruction is still to come.\x01",
            "It is an impression ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FYeah, it is\x02\x03",
            "Tests were led,\x01",
            "In the residents' total in the old city\x01",
            "I am working but …\x02\x03",
            "The scars of attacks are still large,\x01",
            "Progress is not good either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FYes, old city\x01",
            "Wald who turned into a demon\x01",
            "It was a raid …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FResidents are\x01",
            "Do you know about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FNo … in addition to Viper\x01",
            "People who are aware\x01",
            "There will be almost nothing.\x02\x03",
            "Anyway, such a\x01",
            "It appeared in a heteromorphic appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt will be a lot of shock ……\x01",
            "I guess it is better not to speak out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100F… for the moment,\x01",
            "Let's throw that story.\x02\x03",
            "What is important now is reconstruction work\x01",
            "How to proceed.\x02\x03",
            "In this old city,\x01",
            "I can not expect cooperation of the administration\x01",
            "There is no funds to hire vendors.\x02\x03",
            "Hopefully, the power of the Special Affairs Support Division\x01",
            "I will lend it if you lend me it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FRight..\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_17_5822 end

    def Function_18_5CEB(): pass

    label("Function_18_5CEB")

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
            "Assist in the restoration of the Old Town\x01",      # 0
            "I think once\x01",            # 1
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
        (0, "loc_5D5F"),
        (1, "loc_5D6F"),
        (SWITCH_DEFAULT, "loc_5EE9"),
    )


    label("loc_5D5F")

    OP_29(0x8E, 0x4, 0x2)
    SetScenarioFlags(0x196, 0)
    Call(0, 20)
    Jump("loc_5EE9")

    label("loc_5D6F")


    ChrTalk(
        0x101,
        (
            "#00006FI would like to cooperate if possible, but …\x01",
            "There are places depending on other work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FBy the way, I will revisit later\x01",
            "Can I undertake it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FOh, if you can cooperate\x01",
            "Timing is always OK.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I will not say that I forcibly.\x01",
            "Will you help me if I get free?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI understand,\x01",
            "I try to do best if possible.\x02",
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
    Jump("loc_5EE9")

    label("loc_5EE9")

    Return()

    # Function_18_5CEB end

    def Function_19_5EEA(): pass

    label("Function_19_5EEA")

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
            "#04100FHmm, reconstruction work in the old city\x01",
            "Will you help me?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_19_5EEA end

    def Function_20_5FEE(): pass

    label("Function_20_5FEE")


    ChrTalk(
        0x101,
        "#00000FYes. Leave it to us\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04100FOh that's wonderful\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hello, if you are\x01",
            "I thought that would say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSo, we\x01",
            "What should I help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FOh, now mainly in three places\x01",
            "I am doing work.\x02\x03",
            "One is \"Lotus Heights\"\x01",
            "Cooked out being done.\x02\x03",
            "One is a trace of Maison Imerda\x01",
            "Waste material recovery work being done.\x02\x03",
            "At the end this place -\x01",
            "At \"Guillaume Studio\"\x01",
            "Collection and processing of construction materials.\x02\x03",
            "I went to the support department to each place,\x01",
            "Each one needs it\x01",
            "I would like to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI see……\x01",
            "Every one seems important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FIncidentally, here\x01",
            "What is the work being done?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, here's a broken building\x01",
            "I am looking at the building materials to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once, it was left over at the workshop\x01",
            "It seems to be possible to use materials as well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I noticed a problem\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FA problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Spreading, for building building materials\x01",
            "Screws and nails are not enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even at this rate, even the repair\x01",
            "If it does not stay like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FI have scattered everything outside … …\x01",
            "Something waste falling down\x01",
            "Can not you use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FHmm, for a child named canon at first\x01",
            "I am asking you ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, that is rather rather\x01",
            "For financing\x01",
            "It is getting done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It also has strength problems,\x01",
            "I should use as much new as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FSeems quite difficult\x02\x03",
            "#10300FWell then, from somewhere\x01",
            "Picking up screws and nails\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, more definitely than that\x01",
            "There are good ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I am using it for remodeling armor etc.\x01",
            "Use \"U material\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With that material,\x01",
            "You can make things around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F\"U Material\" is … …\x01",
            "Procurement seems to be very difficult though.\x02\x03",
            "#00200FHow many do you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not mind …\x01",
            "There are as many as 10 pieces, fishing will come.\x02",
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
            "#00000FI understand.\x01",
            "I will bring it when collected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#04100FWe're counting on you SSS\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_66BE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66BE)
    Sleep(250)

    def lambda_66CE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_66CE)
    Sleep(50)

    def lambda_66DE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66DE)
    Sleep(50)

    def lambda_66EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_66EE)
    Sleep(50)

    def lambda_66FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_66FE)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004FWell, that's right\x01",
            "Are you going to start to help?\x02\x03",
            "#00000FAlso for those who cook and recover waste materials\x01",
            "Let's go talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FGot it, Leader\x02\x03",
            "It is time when the old nest is difficult,\x01",
            "I will let it get dry.\x02",
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
            "Quest 【Reconstruction assistance of old city】\x07\x00",
            "I started!\x02",
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

    # Function_20_5FEE end

    def Function_21_686E(): pass

    label("Function_21_686E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('Ｕ材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6910")

    ChrTalk(
        0x8,
        "Will you hand over U material?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……\x01",
            "It is not enough number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are ten required here.\x01",
            "I asked for your best regards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A5B")

    label("loc_6910")


    ChrTalk(
        0x8,
        (
            "Whoa\x01",
            "Apparently it was a collection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "U material total 10 pieces,\x01",
            "Will you hand it over here?\x02",
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
            "hand over\x01",          # 0
            "Do not hand it over.\x01",      # 1
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
        (0, "loc_69D0"),
        (1, "loc_69D8"),
        (SWITCH_DEFAULT, "loc_6A5B"),
    )


    label("loc_69D0")

    Call(0, 22)
    Jump("loc_6A5B")

    label("loc_69D8")


    ChrTalk(
        0x8,
        (
            "Is it okay, well?\x01",
            "It will be necessary for you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if you can afford\x01",
            "I will save it if you give way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A5B")

    label("loc_6A5B")

    Return()

    # Function_21_686E end

    def Function_22_6A5C(): pass

    label("Function_22_6A5C")

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
        "#00000FYes, go ahead\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I handed 10 pieces.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('Ｕ材料', 10)

    ChrTalk(
        0x8,
        (
            "Hello, thank you.\x01",
            "Please do not hesitate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The prospect of this repair\x01",
            "It is as good as it arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FEhe, We're glad to be of help\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIf you do repair work\x01",
            "May I help you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FYes Yes,\x01",
            "I have confidence if I have strong labor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, indeed\x01",
            "Do not ask until that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Old city is residents of old city\x01",
            "It is supposed to fix the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FAbbas and Testamentz\x01",
            "I will lead you.\x02\x03",
            "#10309FDo your best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FYou talk like you're not one of them\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04102FHuh, that's fine.\x01",
            "With us already already\x01",
            "Rolling is different.\x02\x03",
            "#04100F… … I will reward you a second time,\x01",
            "Special Affairs Division.\x02\x03",
            "If I still have my hands free\x01",
            "Please help other places.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 2)
    OP_29(0x8E, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F2B")

    ChrTalk(
        0x101,
        (
            "#00000FYes. Leave it to us\x02\x03",
            "#00005FThe main place was\x01",
            "I almost finished helping …\x02\x03",
            "#00000FAs we go around the old town\x01",
            "I am doing fine help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FIt will be appreciated if you do so.\x01",
            "…… See you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Jump("loc_6F52")

    label("loc_6F2B")


    ChrTalk(
        0x101,
        "#00000FYeah, we'll do that\x02",
    )

    CloseMessageWindow()

    label("loc_6F52")

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

    # Function_22_6A5C end

    def Function_23_6FAF(): pass

    label("Function_23_6FAF")

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
        "#04100FHow was it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Perhaps,\x01",
            "Have you finished helping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, all the main needs\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FReally……\x01",
            "It was a pain.\x02\x03",
            "I have time to cook.\x01",
            "It is advisable to crush the time until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell then, for a while\x01",
            "Shall we go round the old town?\x02\x03",
            "#00104FI still have fine help\x01",
            "It may be left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04100FIt will be appreciated if you do so.\x01",
            "…… See you later.\x02",
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

    # Function_23_6FAF end

    SaveToFile()

Try(main)
