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
        "Function_3_D64",          # 03, 3
        "Function_4_1518",         # 04, 4
        "Function_5_1925",         # 05, 5
        "Function_6_1C88",         # 06, 6
        "Function_7_1CCD",         # 07, 7
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

    Jump("loc_D63")

    label("loc_619")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6E9"),
        (18, "loc_6E9"),
        (25, "loc_6E9"),
        (1, "loc_74A"),
        (19, "loc_74A"),
        (26, "loc_74A"),
        (2, "loc_7AB"),
        (20, "loc_7AB"),
        (27, "loc_7AB"),
        (3, "loc_80B"),
        (21, "loc_80B"),
        (28, "loc_80B"),
        (4, "loc_86B"),
        (22, "loc_86B"),
        (29, "loc_86B"),
        (5, "loc_8CB"),
        (23, "loc_8CB"),
        (30, "loc_8CB"),
        (6, "loc_92C"),
        (24, "loc_92C"),
        (31, "loc_92C"),
        (7, "loc_98E"),
        (8, "loc_9E0"),
        (9, "loc_A32"),
        (10, "loc_A84"),
        (11, "loc_AD6"),
        (12, "loc_B28"),
        (13, "loc_B7A"),
        (14, "loc_BCC"),
        (15, "loc_C1E"),
        (16, "loc_C70"),
        (17, "loc_CC2"),
        (SWITCH_DEFAULT, "loc_D14"),
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
            "#56IEarth Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_74A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57IWater Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x1, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_7AB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58IFire Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x2, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_80B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59IWind Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x3, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_86B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60ITime Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x4, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_8CB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61ISpace Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x5, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_92C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62IMirage Sepith\x07\x00",
            " x10 picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D63")

    label("loc_98E")

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
    Jump("loc_D63")

    label("loc_9E0")

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
    Jump("loc_D63")

    label("loc_A32")

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
    Jump("loc_D63")

    label("loc_A84")

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
    Jump("loc_D63")

    label("loc_AD6")

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
    Jump("loc_D63")

    label("loc_B28")

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
    Jump("loc_D63")

    label("loc_B7A")

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
    Jump("loc_D63")

    label("loc_BCC")

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
    Jump("loc_D63")

    label("loc_C1E")

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
    Jump("loc_D63")

    label("loc_C70")

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
    Jump("loc_D63")

    label("loc_CC2")

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
    Jump("loc_D63")

    label("loc_D14")

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
    Jump("loc_D63")

    label("loc_D63")

    Return()

    # Function_2_250 end

    def Function_3_D64(): pass

    label("Function_3_D64")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_DFE"),
        (1, "loc_E4D"),
        (2, "loc_E9C"),
        (3, "loc_EEB"),
        (4, "loc_F3A"),
        (5, "loc_F89"),
        (6, "loc_FD8"),
        (7, "loc_1027"),
        (8, "loc_1076"),
        (9, "loc_10C5"),
        (10, "loc_1114"),
        (11, "loc_1163"),
        (12, "loc_11B2"),
        (13, "loc_1201"),
        (14, "loc_1250"),
        (15, "loc_129F"),
        (16, "loc_12EE"),
        (17, "loc_133D"),
        (18, "loc_138C"),
        (19, "loc_13DB"),
        (20, "loc_142A"),
        (21, "loc_1479"),
        (22, "loc_14C8"),
        (SWITCH_DEFAULT, "loc_1517"),
    )


    label("loc_DFE")

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
    Jump("loc_1517")

    label("loc_E4D")

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
    Jump("loc_1517")

    label("loc_E9C")

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
    Jump("loc_1517")

    label("loc_EEB")

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
    Jump("loc_1517")

    label("loc_F3A")

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
    Jump("loc_1517")

    label("loc_F89")

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
    Jump("loc_1517")

    label("loc_FD8")

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
    Jump("loc_1517")

    label("loc_1027")

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
    Jump("loc_1517")

    label("loc_1076")

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
    Jump("loc_1517")

    label("loc_10C5")

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
    Jump("loc_1517")

    label("loc_1114")

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
    Jump("loc_1517")

    label("loc_1163")

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
    Jump("loc_1517")

    label("loc_11B2")

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
    Jump("loc_1517")

    label("loc_1201")

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
    Jump("loc_1517")

    label("loc_1250")

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
    Jump("loc_1517")

    label("loc_129F")

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
    Jump("loc_1517")

    label("loc_12EE")

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
    Jump("loc_1517")

    label("loc_133D")

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
    Jump("loc_1517")

    label("loc_138C")

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
    Jump("loc_1517")

    label("loc_13DB")

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
    Jump("loc_1517")

    label("loc_142A")

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
    Jump("loc_1517")

    label("loc_1479")

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
    Jump("loc_1517")

    label("loc_14C8")

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
    Jump("loc_1517")

    label("loc_1517")

    Return()

    # Function_3_D64 end

    def Function_4_1518(): pass

    label("Function_4_1518")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1570"),
        (1, "loc_15BF"),
        (2, "loc_160E"),
        (3, "loc_165D"),
        (4, "loc_16AC"),
        (5, "loc_16FB"),
        (6, "loc_174A"),
        (7, "loc_1799"),
        (8, "loc_17E8"),
        (9, "loc_1837"),
        (10, "loc_1886"),
        (11, "loc_18D5"),
        (SWITCH_DEFAULT, "loc_1924"),
    )


    label("loc_1570")

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
    Jump("loc_1924")

    label("loc_15BF")

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
    Jump("loc_1924")

    label("loc_160E")

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
    Jump("loc_1924")

    label("loc_165D")

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
    Jump("loc_1924")

    label("loc_16AC")

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
    Jump("loc_1924")

    label("loc_16FB")

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
    Jump("loc_1924")

    label("loc_174A")

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
    Jump("loc_1924")

    label("loc_1799")

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
    Jump("loc_1924")

    label("loc_17E8")

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
    Jump("loc_1924")

    label("loc_1837")

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
    Jump("loc_1924")

    label("loc_1886")

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
    Jump("loc_1924")

    label("loc_18D5")

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
    Jump("loc_1924")

    label("loc_1924")

    Return()

    # Function_4_1518 end

    def Function_5_1925(): pass

    label("Function_5_1925")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1971"),
        (1, "loc_19C0"),
        (2, "loc_1A0F"),
        (3, "loc_1A5E"),
        (4, "loc_1AAD"),
        (5, "loc_1AFC"),
        (6, "loc_1B4B"),
        (7, "loc_1B9A"),
        (8, "loc_1BE9"),
        (9, "loc_1C38"),
        (SWITCH_DEFAULT, "loc_1C87"),
    )


    label("loc_1971")

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
    Jump("loc_1C87")

    label("loc_19C0")

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
    Jump("loc_1C87")

    label("loc_1A0F")

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
    Jump("loc_1C87")

    label("loc_1A5E")

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
    Jump("loc_1C87")

    label("loc_1AAD")

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
    Jump("loc_1C87")

    label("loc_1AFC")

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
    Jump("loc_1C87")

    label("loc_1B4B")

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
    Jump("loc_1C87")

    label("loc_1B9A")

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
    Jump("loc_1C87")

    label("loc_1BE9")

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
    Jump("loc_1C87")

    label("loc_1C38")

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
    Jump("loc_1C87")

    label("loc_1C87")

    Return()

    # Function_5_1925 end

    def Function_6_1C88(): pass

    label("Function_6_1C88")

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

    # Function_6_1C88 end

    def Function_7_1CCD(): pass

    label("Function_7_1CCD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_214F")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1D38"),
        (1, "loc_1D8A"),
        (2, "loc_1DDC"),
        (3, "loc_1E2E"),
        (4, "loc_1E80"),
        (5, "loc_1ED2"),
        (6, "loc_1F21"),
        (7, "loc_1F70"),
        (8, "loc_1FBF"),
        (9, "loc_200E"),
        (10, "loc_205D"),
        (11, "loc_20AC"),
        (SWITCH_DEFAULT, "loc_20FB"),
    )


    label("loc_1D38")

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
    Jump("loc_214A")

    label("loc_1D8A")

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
    Jump("loc_214A")

    label("loc_1DDC")

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
    Jump("loc_214A")

    label("loc_1E2E")

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
    Jump("loc_214A")

    label("loc_1E80")

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
    Jump("loc_214A")

    label("loc_1ED2")

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
    Jump("loc_214A")

    label("loc_1F21")

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
    Jump("loc_214A")

    label("loc_1F70")

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
    Jump("loc_214A")

    label("loc_1FBF")

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
    Jump("loc_214A")

    label("loc_200E")

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
    Jump("loc_214A")

    label("loc_205D")

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
    Jump("loc_214A")

    label("loc_20AC")

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
    Jump("loc_214A")

    label("loc_20FB")

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
    Jump("loc_214A")

    label("loc_214A")

    Jump("loc_2999")

    label("loc_214F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_21E9"),
        (1, "loc_223B"),
        (2, "loc_228D"),
        (3, "loc_22DF"),
        (4, "loc_2331"),
        (5, "loc_2383"),
        (6, "loc_23D5"),
        (7, "loc_2427"),
        (8, "loc_2479"),
        (9, "loc_24CB"),
        (10, "loc_251D"),
        (11, "loc_256F"),
        (12, "loc_25C1"),
        (13, "loc_2613"),
        (14, "loc_2665"),
        (15, "loc_26B7"),
        (16, "loc_2709"),
        (17, "loc_275B"),
        (18, "loc_27AD"),
        (19, "loc_27FF"),
        (20, "loc_2851"),
        (21, "loc_28A3"),
        (22, "loc_28F5"),
        (SWITCH_DEFAULT, "loc_2947"),
    )


    label("loc_21E9")

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
    Jump("loc_2999")

    label("loc_223B")

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
    Jump("loc_2999")

    label("loc_228D")

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
    Jump("loc_2999")

    label("loc_22DF")

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
    Jump("loc_2999")

    label("loc_2331")

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
    Jump("loc_2999")

    label("loc_2383")

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
    Jump("loc_2999")

    label("loc_23D5")

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
    Jump("loc_2999")

    label("loc_2427")

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
    Jump("loc_2999")

    label("loc_2479")

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
    Jump("loc_2999")

    label("loc_24CB")

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
    Jump("loc_2999")

    label("loc_251D")

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
    Jump("loc_2999")

    label("loc_256F")

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
    Jump("loc_2999")

    label("loc_25C1")

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
    Jump("loc_2999")

    label("loc_2613")

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
    Jump("loc_2999")

    label("loc_2665")

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
    Jump("loc_2999")

    label("loc_26B7")

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
    Jump("loc_2999")

    label("loc_2709")

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
    Jump("loc_2999")

    label("loc_275B")

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
    Jump("loc_2999")

    label("loc_27AD")

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
    Jump("loc_2999")

    label("loc_27FF")

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
    Jump("loc_2999")

    label("loc_2851")

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
    Jump("loc_2999")

    label("loc_28A3")

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
    Jump("loc_2999")

    label("loc_28F5")

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
    Jump("loc_2999")

    label("loc_2947")

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
    Jump("loc_2999")

    label("loc_2999")

    Return()

    # Function_7_1CCD end

    SaveToFile()

Try(main)
