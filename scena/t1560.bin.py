from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1560.bin",                # FileName
        "t1560",                    # MapName
        "t1560",                    # Location
        0x0053,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 83, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1560",                  # 0
    ))

    ChipFrameInfo(160, 0)                                        # 0

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_B7",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_B6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B6")

    Return()

    # Function_1_A4 end

    def Function_2_B7(): pass

    label("Function_2_B7")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121")
    SetChrPos(0x1, 300, 0, 800, 90)

    label("loc_121")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140")
    SetChrPos(0x2, 300, 0, -800, 90)

    label("loc_140")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_15F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188")
    SetChrPos(0x4, -1700, 0, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_188")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1")
    SetChrPos(0x5, -1700, 0, 800, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1B1")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★[ 3F]")
    MenuCmd(1, 0, "  [ 2F]")
    MenuCmd(1, 0, "  [ 1F]")
    MenuCmd(1, 0, "  [Get Off]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C8")

    label("loc_21D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "  [ 3F]")
    MenuCmd(1, 0, "★[ 2F]")
    MenuCmd(1, 0, "  [ 1F]")
    MenuCmd(1, 0, "  [Get Off]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C8")

    label("loc_275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C8")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "  [ 3F]")
    MenuCmd(1, 0, "  [ 2F]")
    MenuCmd(1, 0, "★[ 1F]")
    MenuCmd(1, 0, "  [Get Off]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C8")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_36C")

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_328")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_36C")

    label("loc_328")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_361")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_36C")

    label("loc_361")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_397"),
        (1, "loc_3A7"),
        (2, "loc_3B7"),
        (SWITCH_DEFAULT, "loc_3C7"),
    )


    label("loc_397")

    EventEnd(0x5)
    NewScene("t1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_3C7")

    label("loc_3A7")

    EventEnd(0x5)
    NewScene("t1540", 103, 0, 0)
    IdleLoop()
    Jump("loc_3C7")

    label("loc_3B7")

    EventEnd(0x5)
    NewScene("t1530", 102, 0, 0)
    IdleLoop()
    Jump("loc_3C7")

    label("loc_3C7")

    Jump("loc_42A")

    label("loc_3CC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E8"),
        (1, "loc_3FE"),
        (2, "loc_414"),
        (SWITCH_DEFAULT, "loc_42A"),
    )


    label("loc_3E8")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_42A")

    label("loc_3FE")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1540", 103, 0, 0)
    IdleLoop()
    Jump("loc_42A")

    label("loc_414")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1530", 102, 0, 0)
    IdleLoop()
    Jump("loc_42A")

    label("loc_42A")

    Return()

    # Function_2_B7 end

    SaveToFile()

Try(main)
