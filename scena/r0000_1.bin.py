from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0000_1.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [100, 0, 0, 0, 83952996, 83952897, 5, 1, 1380, 1281, 1281, 1281, 84215045, 5, 83887460, 1280, 512, 5, 0, 2, 0, 0, 0],
    )

    BuildStringList((
        "r0000_1",                # 0
    ))

    ChipFrameInfo(356, 0)                                        # 0

    ScpFunction((
        "Function_0_164",          # 00, 0
        "Function_1_1FE",          # 01, 1
        "Function_2_250",          # 02, 2
        "Function_3_D6B",          # 03, 3
        "Function_4_151F",         # 04, 4
        "Function_5_192C",         # 05, 5
        "Function_6_1C8F",         # 06, 6
        "Function_7_1CD4",         # 07, 7
    ))


    def Function_0_164(): pass

    label("Function_0_164")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You found something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3")
    Call(1, 5)
    Jump("loc_1FD")

    label("loc_1B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB")
    Call(1, 4)
    Jump("loc_1FD")

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 5)), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    Call(1, 3)
    Jump("loc_1FD")

    label("loc_1FA")

    Call(1, 2)

    label("loc_1FD")

    Return()

    # Function_0_164 end

    def Function_1_1FE(): pass

    label("Function_1_1FE")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228")
    Call(1, 5)
    Jump("loc_24F")

    label("loc_228")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C")
    Call(1, 4)
    Jump("loc_24F")

    label("loc_24C")

    Call(1, 3)

    label("loc_24F")

    Return()

    # Function_1_1FE end

    def Function_2_250(): pass

    label("Function_2_250")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_619")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2AF"),
        (1, "loc_2FE"),
        (2, "loc_34D"),
        (3, "loc_39C"),
        (4, "loc_3EB"),
        (5, "loc_43A"),
        (6, "loc_489"),
        (7, "loc_4D8"),
        (8, "loc_527"),
        (9, "loc_576"),
        (SWITCH_DEFAULT, "loc_5C5"),
    )


    label("loc_2AF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x200),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x200, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_2FE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x201),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x201, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_34D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x202),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x202, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_39C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x203),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x203, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_3EB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x204),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x204, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_43A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x205),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x205, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_489")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x206),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x206, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_4D8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x207),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x207, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_527")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x208),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x208, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_576")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x209),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x209, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_5C5")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_614")

    label("loc_614")

    Jump("loc_D6A")

    label("loc_619")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6E9"),
        (18, "loc_6E9"),
        (25, "loc_6E9"),
        (1, "loc_74B"),
        (19, "loc_74B"),
        (26, "loc_74B"),
        (2, "loc_7AD"),
        (20, "loc_7AD"),
        (27, "loc_7AD"),
        (3, "loc_80E"),
        (21, "loc_80E"),
        (28, "loc_80E"),
        (4, "loc_86F"),
        (22, "loc_86F"),
        (29, "loc_86F"),
        (5, "loc_8D0"),
        (23, "loc_8D0"),
        (30, "loc_8D0"),
        (6, "loc_932"),
        (24, "loc_932"),
        (31, "loc_932"),
        (7, "loc_995"),
        (8, "loc_9E7"),
        (9, "loc_A39"),
        (10, "loc_A8B"),
        (11, "loc_ADD"),
        (12, "loc_B2F"),
        (13, "loc_B81"),
        (14, "loc_BD3"),
        (15, "loc_C25"),
        (16, "loc_C77"),
        (17, "loc_CC9"),
        (SWITCH_DEFAULT, "loc_D1B"),
    )


    label("loc_6E9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I Earth Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_74B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I Water Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x1, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_7AD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I Fire Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x2, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_80E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I Wind Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x3, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_86F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I Time Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x4, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_8D0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I Space Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x5, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_932")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I Mirage Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_995")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x186),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x186, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_9E7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x187, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_A39")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x188),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x188, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_A8B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_ADD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12C, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_B2F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12D, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_B81")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12E, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_BD3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12F, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_C25")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x130),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x130, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_C77")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x131),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x131, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_CC9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x132),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x132, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_D1B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D6A")

    label("loc_D6A")

    Return()

    # Function_2_250 end

    def Function_3_D6B(): pass

    label("Function_3_D6B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E05"),
        (1, "loc_E54"),
        (2, "loc_EA3"),
        (3, "loc_EF2"),
        (4, "loc_F41"),
        (5, "loc_F90"),
        (6, "loc_FDF"),
        (7, "loc_102E"),
        (8, "loc_107D"),
        (9, "loc_10CC"),
        (10, "loc_111B"),
        (11, "loc_116A"),
        (12, "loc_11B9"),
        (13, "loc_1208"),
        (14, "loc_1257"),
        (15, "loc_12A6"),
        (16, "loc_12F5"),
        (17, "loc_1344"),
        (18, "loc_1393"),
        (19, "loc_13E2"),
        (20, "loc_1431"),
        (21, "loc_1480"),
        (22, "loc_14CF"),
        (SWITCH_DEFAULT, "loc_151E"),
    )


    label("loc_E05")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x64, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_E54")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x68, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_EA3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_EF2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x70),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x70, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_F41")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x74, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_F90")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x78, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_FDF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_102E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x80),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x80, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_107D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x84),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x84, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_10CC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x88),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x88, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_111B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x8C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_116A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x92, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_11B9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_1208")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_1257")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_12A6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3F, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_12F5")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x40),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x40, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_1344")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x41, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_1393")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x42, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_13E2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x43),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x43, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_1431")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x44, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_1480")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x45),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x45, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_14CF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x46, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_151E")

    label("loc_151E")

    Return()

    # Function_3_D6B end

    def Function_4_151F(): pass

    label("Function_4_151F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1577"),
        (1, "loc_15C6"),
        (2, "loc_1615"),
        (3, "loc_1664"),
        (4, "loc_16B3"),
        (5, "loc_1702"),
        (6, "loc_1751"),
        (7, "loc_17A0"),
        (8, "loc_17EF"),
        (9, "loc_183E"),
        (10, "loc_188D"),
        (11, "loc_18DC"),
        (SWITCH_DEFAULT, "loc_192B"),
    )


    label("loc_1577")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x65, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_15C6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x69, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_1615")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_1664")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x71),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x71, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_16B3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x75),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x75, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_1702")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x79, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_1751")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_17A0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x81, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_17EF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x85, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_183E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x89),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x89, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_188D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x8D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_18DC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x93),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x93, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_192B")

    label("loc_192B")

    Return()

    # Function_4_151F end

    def Function_5_192C(): pass

    label("Function_5_192C")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1978"),
        (1, "loc_19C7"),
        (2, "loc_1A16"),
        (3, "loc_1A65"),
        (4, "loc_1AB4"),
        (5, "loc_1B03"),
        (6, "loc_1B52"),
        (7, "loc_1BA1"),
        (8, "loc_1BF0"),
        (9, "loc_1C3F"),
        (SWITCH_DEFAULT, "loc_1C8E"),
    )


    label("loc_1978")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x66, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_19C7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6A, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1A16")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1A65")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x72, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1AB4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x76, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1B03")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7A, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1B52")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1BA1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x82, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1BF0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x8A, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1C3F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x94),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x94, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C8E")

    label("loc_1C8E")

    Return()

    # Function_5_192C end

    def Function_6_1C8F(): pass

    label("Function_6_1C8F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You found something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 7)
    TalkEnd(0xFF)
    ClearMapFlags(0x80)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C8F end

    def Function_7_1CD4(): pass

    label("Function_7_1CD4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2156")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1D3F"),
        (1, "loc_1D91"),
        (2, "loc_1DE3"),
        (3, "loc_1E35"),
        (4, "loc_1E87"),
        (5, "loc_1ED9"),
        (6, "loc_1F28"),
        (7, "loc_1F77"),
        (8, "loc_1FC6"),
        (9, "loc_2015"),
        (10, "loc_2064"),
        (11, "loc_20B3"),
        (SWITCH_DEFAULT, "loc_2102"),
    )


    label("loc_1D3F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x186),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x186, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1D91")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x187, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1DE3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x188),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x188, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1E35")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1E87")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18A, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1ED9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1F28")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1F77")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_1FC6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12F, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_2015")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x130),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x130, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_2064")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x131),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x131, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_20B3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x132),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x132, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_2102")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2151")

    label("loc_2151")

    Jump("loc_29A0")

    label("loc_2156")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_21F0"),
        (1, "loc_2242"),
        (2, "loc_2294"),
        (3, "loc_22E6"),
        (4, "loc_2338"),
        (5, "loc_238A"),
        (6, "loc_23DC"),
        (7, "loc_242E"),
        (8, "loc_2480"),
        (9, "loc_24D2"),
        (10, "loc_2524"),
        (11, "loc_2576"),
        (12, "loc_25C8"),
        (13, "loc_261A"),
        (14, "loc_266C"),
        (15, "loc_26BE"),
        (16, "loc_2710"),
        (17, "loc_2762"),
        (18, "loc_27B4"),
        (19, "loc_2806"),
        (20, "loc_2858"),
        (21, "loc_28AA"),
        (22, "loc_28FC"),
        (SWITCH_DEFAULT, "loc_294E"),
    )


    label("loc_21F0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x134),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x134, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2242")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x135),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x135, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2294")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x136, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_22E6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x137),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x137, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2338")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x138),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x138, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_238A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x139),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x139, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_23DC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13A, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_242E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13B, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2480")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13C, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_24D2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13D, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2524")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x8 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13E, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2576")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13F, 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_25C8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x140),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x140, 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_261A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x141),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x4 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x141, 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_266C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x142),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x142, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_26BE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x143, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2710")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x144, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2762")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x145),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x145, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_27B4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x146),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x146, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2806")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x147),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x5 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x147, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_2858")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x148, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_28AA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x149),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x149, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_28FC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14A, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_294E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x2 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14A, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_29A0")

    label("loc_29A0")

    Return()

    # Function_7_1CD4 end

    SaveToFile()

Try(main)
