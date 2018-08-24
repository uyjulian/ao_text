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
        "Function_3_551",          # 03, 3
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52F")
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD")
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
            "Elie\x01",        # 0
            "Tio\x01",         # 1
            "Randy\x01",       # 2
            "Wazy\x01",        # 3
            "Noｱl\x01",       # 4
            "Rixia\x01",       # 5
            "KeA\x01",         # 6
            "Fran\x01",        # 7
            "Cecil\x01",       # 8
            "Ilya\x01",        # 9
            "Sully\x01",       # 10
            "Cancel\x01",      # 11
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    Jump("loc_2BD")

    label("loc_1CD")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_218"),
        (1, "loc_227"),
        (2, "loc_236"),
        (3, "loc_245"),
        (4, "loc_254"),
        (5, "loc_263"),
        (6, "loc_272"),
        (7, "loc_281"),
        (8, "loc_290"),
        (9, "loc_29F"),
        (10, "loc_2AE"),
        (SWITCH_DEFAULT, "loc_2BD"),
    )


    label("loc_218")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_227")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_236")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_245")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_254")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_263")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_272")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_281")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_290")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_29F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_2AE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD")

    label("loc_2BD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_309"),
        (1, "loc_336"),
        (2, "loc_363"),
        (3, "loc_390"),
        (4, "loc_3BD"),
        (5, "loc_3EA"),
        (6, "loc_417"),
        (7, "loc_444"),
        (8, "loc_471"),
        (9, "loc_49E"),
        (10, "loc_4CB"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_309")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_336")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_363")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_390")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_3BD")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_3EA")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_417")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_444")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_471")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_49E")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_4CB")

    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x13, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_502")

    label("loc_4F8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_502")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_516")
    Jump("loc_52F")

    label("loc_516")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A")
    Jump("loc_52F")

    label("loc_52A")

    Jump("Function_2_A9")

    label("loc_52F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5C), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54E")
    SetScenarioFlags(0x22, 0)
    NewScene("t1350", 0, 0, 0)
    IdleLoop()
    Jump("loc_550")

    label("loc_54E")

    OP_B9(0x2)

    label("loc_550")

    Return()

    # Function_2_A9 end

    def Function_3_551(): pass

    label("Function_3_551")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57B")
    MoveCamera(350, -5, 0, 20000)
    OP_6F(0x40)
    MoveCamera(10, -5, 0, 20000)
    OP_6F(0x40)
    Jump("Function_3_551")

    label("loc_57B")

    Return()

    # Function_3_551 end

    SaveToFile()

Try(main)
