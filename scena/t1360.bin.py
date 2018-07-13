from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1360.bin",                # FileName
        "t1360",                    # MapName
        "t1360",                    # Location
        0x00B8,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 184, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1360",                  # 0
    ))

    ChipFrameInfo(164, 0)                                        # 0

    ScpFunction((
        "Function_0_A4",           # 00, 0
        "Function_1_A8",           # 01, 1
        "Function_2_A9",           # 02, 2
        "Function_3_54F",          # 03, 3
    ))


    def Function_0_A4(): pass

    label("Function_0_A4")

    Event(0, 2)
    Return()

    # Function_0_A4 end

    def Function_1_A8(): pass

    label("Function_1_A8")

    Return()

    # Function_1_A8 end

    def Function_2_A9(): pass

    label("Function_2_A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52D")
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetChrPos(0x101, 500, 300, 3, 0)
    SetChrFlags(0x101, 0x8)
    OP_68(0, 2200, 0, 0)
    MoveCamera(10, -5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(11440, 0)
    PlayBGM("ed7590", 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB")
    BeginChrThread(0x0, 1, 0, 3)
    FadeToBright(500, 0)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(120, 308, 28, 1)

    AnonymousTalk(
        0xFF,
        (
            "With whom will you ride?",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        250,
        48,
        1,
        (
            "Elie\x01",       # 0
            "Tio\x01",        # 1
            "Randy\x01",      # 2
            "Wazy\x01",       # 3
            "Noｱl\x01",      # 4
            "Rixia\x01",      # 5
            "KeA\x01",        # 6
            "Fran\x01",       # 7
            "Cecil\x01",      # 8
            "Ilya\x01",       # 9
            "Sully\x01",      # 10
            "Quit\x01",       # 11
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    Jump("loc_2BB")

    label("loc_1CB")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_216"),
        (1, "loc_225"),
        (2, "loc_234"),
        (3, "loc_243"),
        (4, "loc_252"),
        (5, "loc_261"),
        (6, "loc_270"),
        (7, "loc_27F"),
        (8, "loc_28E"),
        (9, "loc_29D"),
        (10, "loc_2AC"),
        (SWITCH_DEFAULT, "loc_2BB"),
    )


    label("loc_216")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_225")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_234")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_243")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_252")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_261")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_270")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_27F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_28E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_29D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_2AC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BB")

    label("loc_2BB")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_307"),
        (1, "loc_334"),
        (2, "loc_361"),
        (3, "loc_38E"),
        (4, "loc_3BB"),
        (5, "loc_3E8"),
        (6, "loc_415"),
        (7, "loc_442"),
        (8, "loc_46F"),
        (9, "loc_49C"),
        (10, "loc_4C9"),
        (SWITCH_DEFAULT, "loc_4F6"),
    )


    label("loc_307")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_334")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_361")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_38E")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_3BB")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_3E8")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_415")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_442")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_46F")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_49C")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_4C9")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_500")

    label("loc_4F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_500")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    Jump("loc_52D")

    label("loc_514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_528")
    Jump("loc_52D")

    label("loc_528")

    Jump("Function_2_A9")

    label("loc_52D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54C")
    SetScenarioFlags(0x22, 0)
    NewScene("t1350", 0, 0, 0)
    IdleLoop()
    Jump("loc_54E")

    label("loc_54C")

    OP_B9(0x2)

    label("loc_54E")

    Return()

    # Function_2_A9 end

    def Function_3_54F(): pass

    label("Function_3_54F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_579")
    MoveCamera(350, -5, 0, 20000)
    OP_6F(0x40)
    MoveCamera(10, -5, 0, 20000)
    OP_6F(0x40)
    Jump("Function_3_54F")

    label("loc_579")

    Return()

    # Function_3_54F end

    SaveToFile()

Try(main)
