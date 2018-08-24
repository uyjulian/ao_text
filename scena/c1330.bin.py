from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1330.bin",                # FileName
        "c1330",                    # MapName
        "c1330",                    # Location
        0x001B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1330",                  # 0
    ))

    ChipFrameInfo(160, 0)                                        # 0

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_A5",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Return()

    # Function_1_A4 end

    def Function_2_A5(): pass

    label("Function_2_A5")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 2200, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F")
    SetChrPos(0x1, 500, 0, -500, 90)

    label("loc_10F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E")
    SetChrPos(0x2, 500, 0, 500, 90)

    label("loc_12E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_14D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C")
    SetChrPos(0x4, -1900, 0, -600, 90)

    label("loc_16C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B")
    SetChrPos(0x5, -1900, 0, 600, 90)

    label("loc_18B")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★[16F]\x01",          # 0
            "  [ 1F]\x01",          # 1
            "  [B5F]\x01",          # 2
            "  [Get Off]\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_278")

    label("loc_1E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [16F]\x01",          # 0
            "★[ 1F]\x01",          # 1
            "  [B5F]\x01",          # 2
            "  [Get Off]\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_278")

    label("loc_233")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278")

    Menu(
        0,
        10,
        10,
        0,
        (
            "  [16F]\x01",          # 0
            "  [ 1F]\x01",          # 1
            "★[B5F]\x01",          # 2
            "  [Get Off]\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_278")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_322")

    label("loc_29F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DB")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    OP_24(0x67)
    Jump("loc_322")

    label("loc_2DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_317")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    OP_24(0x67)
    Jump("loc_322")

    label("loc_317")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_34D"),
        (1, "loc_35D"),
        (2, "loc_36D"),
        (SWITCH_DEFAULT, "loc_37D"),
    )


    label("loc_34D")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_37D")

    label("loc_35D")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_37D")

    label("loc_36D")

    EventEnd(0x5)
    NewScene("c1320", 102, 0, 0)
    IdleLoop()
    Jump("loc_37D")

    label("loc_37D")

    Jump("loc_3E0")

    label("loc_382")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_39E"),
        (1, "loc_3B4"),
        (2, "loc_3CA"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_39E")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_3E0")

    label("loc_3B4")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_3E0")

    label("loc_3CA")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1320", 102, 0, 0)
    IdleLoop()
    Jump("loc_3E0")

    label("loc_3E0")

    Return()

    # Function_2_A5 end

    SaveToFile()

Try(main)
