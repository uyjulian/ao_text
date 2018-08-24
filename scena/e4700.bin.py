from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4700.bin",                # FileName
        "e4700",                    # MapName
        "e4700",                    # Location
        0x0000,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -8840, 6000, 2420, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4700",                  # 0
        "Lau",                    # 1
        "Cao",                    # 2
        "カメラ",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(280, 0)                                        # 0

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_17C",          # 01, 1
        "Function_2_17D",          # 02, 2
        "Function_3_545",          # 03, 3
        "Function_4_603",          # 04, 4
        "Function_5_6B6",          # 05, 5
        "Function_6_702",          # 06, 6
        "Function_7_75A",          # 07, 7
        "Function_8_7A8",          # 08, 8
        "Function_9_7F6",          # 09, 9
        "Function_10_1B4D",        # 0A, 10
        "Function_11_2848",        # 0B, 11
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146")
    Event(0, 2)
    Jump("loc_17B")

    label("loc_146")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A")
    Event(0, 10)
    Jump("loc_17B")

    label("loc_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B")
    Event(0, 9)

    label("loc_17B")

    Return()

    # Function_0_118 end

    def Function_1_17C(): pass

    label("Function_1_17C")

    Return()

    # Function_1_17C end

    def Function_2_17D(): pass

    label("Function_2_17D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetCameraDistance(24440, 0)
    Call(0, 3)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BD")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D6")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1D6")

    OP_68(497800, -20000, 13130, 0)
    SetChrPos(0x8, 498100, -21000, 11910, 180)
    SetChrPos(0xA, 498100, -21000, 14500, 180)
    OP_6B(0xA)
    BeginChrThread(0x8, 1, 0, 6)
    BeginChrThread(0xA, 1, 0, 5)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_270")
    BeginChrThread(0x101, 1, 0, 4)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_26A")
    BeginChrThread(0x101, 1, 0, 8)
    Jump("loc_270")

    label("loc_26A")

    BeginChrThread(0x101, 1, 0, 7)

    label("loc_270")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B4")
    BeginChrThread(0x102, 1, 0, 4)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2AE")
    BeginChrThread(0x102, 1, 0, 8)
    Jump("loc_2B4")

    label("loc_2AE")

    BeginChrThread(0x102, 1, 0, 7)

    label("loc_2B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F8")
    BeginChrThread(0x103, 1, 0, 4)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2F2")
    BeginChrThread(0x103, 1, 0, 8)
    Jump("loc_2F8")

    label("loc_2F2")

    BeginChrThread(0x103, 1, 0, 7)

    label("loc_2F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33C")
    BeginChrThread(0x104, 1, 0, 4)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_336")
    BeginChrThread(0x104, 1, 0, 8)
    Jump("loc_33C")

    label("loc_336")

    BeginChrThread(0x104, 1, 0, 7)

    label("loc_33C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_380")
    BeginChrThread(0x105, 1, 0, 4)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_37A")
    BeginChrThread(0x105, 1, 0, 8)
    Jump("loc_380")

    label("loc_37A")

    BeginChrThread(0x105, 1, 0, 7)

    label("loc_380")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C4")
    BeginChrThread(0x106, 1, 0, 4)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3BE")
    BeginChrThread(0x106, 1, 0, 8)
    Jump("loc_3C4")

    label("loc_3BE")

    BeginChrThread(0x106, 1, 0, 7)

    label("loc_3C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_408")
    BeginChrThread(0x109, 1, 0, 4)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_402")
    BeginChrThread(0x109, 1, 0, 8)
    Jump("loc_408")

    label("loc_402")

    BeginChrThread(0x109, 1, 0, 7)

    label("loc_408")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44C")
    BeginChrThread(0x107, 1, 0, 4)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_446")
    BeginChrThread(0x107, 1, 0, 8)
    Jump("loc_44C")

    label("loc_446")

    BeginChrThread(0x107, 1, 0, 7)

    label("loc_44C")

    FadeToBright(2000, 0)
    OP_0D()

    label("loc_456")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_475")
    Jump("loc_47D")

    label("loc_475")

    Sleep(50)
    Jump("loc_456")

    label("loc_47D")

    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49F")
    EndChrThread(0x0, 0x1)

    label("loc_49F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B2")
    EndChrThread(0x1, 0x1)

    label("loc_4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4C5")
    EndChrThread(0x2, 0x1)

    label("loc_4C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D8")
    EndChrThread(0x3, 0x1)

    label("loc_4D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4EB")
    EndChrThread(0x4, 0x1)

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4FE")
    EndChrThread(0x5, 0x1)

    label("loc_4FE")

    OP_6B(0xFF)
    SetChrFlags(0x8, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_522")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_522")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_53B")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_53B")

    NewScene("e4700", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_2_17D end

    def Function_3_545(): pass

    label("Function_3_545")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_565")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57A")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58F")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A4")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B9")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CE")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E3")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F8")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_3_545 end

    def Function_4_603(): pass

    label("Function_4_603")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_631"),
        (1, "loc_647"),
        (2, "loc_65D"),
        (3, "loc_673"),
        (4, "loc_689"),
        (5, "loc_69F"),
        (SWITCH_DEFAULT, "loc_6B5"),
    )


    label("loc_631")

    SetChrPos(0xFE, 497600, -21000, 14530, 180)
    Jump("loc_6B5")

    label("loc_647")

    SetChrPos(0xFE, 499000, -21000, 15240, 180)
    Jump("loc_6B5")

    label("loc_65D")

    SetChrPos(0xFE, 497600, -21000, 16120, 180)
    Jump("loc_6B5")

    label("loc_673")

    SetChrPos(0xFE, 499000, -21000, 16740, 180)
    Jump("loc_6B5")

    label("loc_689")

    SetChrPos(0xFE, 497600, -21000, 17990, 180)
    Jump("loc_6B5")

    label("loc_69F")

    SetChrPos(0xFE, 499000, -21000, 18390, 180)
    Jump("loc_6B5")

    label("loc_6B5")

    Return()

    # Function_4_603 end

    def Function_5_6B6(): pass

    label("Function_5_6B6")

    OP_95(0xFE, 498180, -21000, 3500, 2000, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 498180, -21000, 3500)
    OP_9F(0x1, 497180, -21000, 2500)
    OP_9F(0x1, 495180, -21000, 1500)
    OP_9F(0x2, 0xFE, 1000, 0x0)
    Return()

    # Function_5_6B6 end

    def Function_6_702(): pass

    label("Function_6_702")

    OP_95(0xFE, 498180, -21000, -230, 2000, 0x1)
    OP_95(0xFE, 495000, -21000, -230, 2000, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_739():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_739)
    OP_95(0xFE, 489890, -21000, -230, 2000, 0x0)
    Return()

    # Function_6_702 end

    def Function_7_75A(): pass

    label("Function_7_75A")

    OP_95(0xFE, 499000, -21000, -430, 2000, 0x0)
    OP_95(0xFE, 495000, -21000, -430, 2000, 0x1)

    def lambda_787():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_787)
    OP_95(0xFE, 489890, -21000, -430, 2000, 0x0)
    Return()

    # Function_7_75A end

    def Function_8_7A8(): pass

    label("Function_8_7A8")

    OP_95(0xFE, 497600, -21000, 0, 2000, 0x1)
    OP_95(0xFE, 495000, -21000, 0, 2000, 0x1)

    def lambda_7D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7D5)
    OP_95(0xFE, 489890, -21000, 0, 2000, 0x0)
    Return()

    # Function_8_7A8 end

    def Function_9_7F6(): pass

    label("Function_9_7F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 3)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x1F)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7900, 6000, -670, 180)
    SetChrPos(0x8, -9100, 6000, 210, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_868")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_868")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_881")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_881")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D3")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F7")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91B")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93F")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_963")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_987")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_987")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AB")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AB")

    OP_68(-20060, 6200, -53820, 0)
    MoveCamera(58, 11, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(16700, 0)
    FadeToBright(2000, 0)
    OP_68(-12270, 8000, -29610, 7000)
    MoveCamera(31, 13, 0, 7000)
    OP_6E(520, 7000)
    SetCameraDistance(20250, 7000)
    Sleep(7600)
    Fade(500)
    OP_68(-13990, 8800, -7980, 0)
    MoveCamera(46, 9, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(10780, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BF6")

    ChrTalk(
        0x9,
        (
            "#5P#03200FThank you for gracing us with\x01",
            "your presence.\x02\x03",
            "#03204FLong time no see too, Randy,\x01",
            "Noｱl.\x02\x03",
            "#03209FIt seems there were some twists\x01",
            "and turns, but I am glad you all\x01",
            "managed to get back together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FMan, was I shocked when I\x01",
            "heard we were cooperating\x01",
            "with you guys, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FYou seem the same as\x01",
            "always, Cao.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAlso... You've been\x01",
            "staying at the Fort of\x01",
            "the Sun?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(
        0x9,
        (
            "#5P#03200FThank you for gracing us\x01",
            "with your presence.\x02\x03",
            "#03204FLong time no see, Randy.\x02\x03",
            "#03209FIt seems you were doing\x01",
            "quite well in the\x01",
            "Resistance... How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FMan, was I shocked when I\x01",
            "heard we were cooperating\x01",
            "with you guys, but...\x02\x03",
            "#00301FYou seem to be the same\x01",
            "as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAlso... You've been\x01",
            "staying at the Fort of\x01",
            "the Sun?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8C")

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E8C")

    ChrTalk(
        0x9,
        (
            "#5P#03200FThank you for gracing us\x01",
            "with your presence.\x02\x03",
            "#03209FAs I thought, Lloyd, you\x01",
            "were worried about me and\x01",
            "came straight here...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FN-No... That's not it.\x02\x03",
            "#00001FRather, have you been\x01",
            "staying at the Fort of\x01",
            "the Sun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8C")


    ChrTalk(
        0x9,
        (
            "#5P#03204FYes, we've decided that it's a convenient place\x01",
            "in many aspects for hiding. The facilities the\x01",
            ""Cult" used have also been useful to us.\x02\x03",
            "#03200FFurthermore, even the State Guard and Red\x01",
            "Constellation can't easily get inside.\x02\x03",
            "They haven't even noticed the existence of the\x01",
            "secret passage you all came through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FHaha, that's true.\x02\x03",
            "#10402FEven the path he showed\x01",
            "us... He used quite a\x01",
            "complex route, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FRight... I don't think\x01",
            "we could reach this\x01",
            "place again alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...So you noticed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FThat's all right. But\x01",
            "please, not a word of\x01",
            "this to anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10701F...Are all the Heiyue\x01",
            "staying here for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03200FYes, I intend to bide my time\x01",
            "here while observing the\x01",
            "situation.\x02\x03",
            "#03203FThe Crossbell barrier... Unless\x01",
            "something is done about that, our\x01",
            "movements are restricted as well.\x02\x03",
            "#03200FEngaging the State Guard and Red\x01",
            "Constellation head on would be...\x01",
            "a little difficult.\x02\x03",
            "#03206FWell, if we had Master Yin with\x01",
            "us, we'd have some chance,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10703F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FHeh, it wouldn't be a very\x01",
            "tasteful way to get things\x01",
            "done.\x02\x03",
            "#10402FA forcible and bloody way,\x01",
            "like having her completely\x01",
            "dirty her hands, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03210FWell, I wonder... I'll\x01",
            "leave that to your\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F...After taking her back from\x01",
            "you, I'll absolutely never make\x01",
            "Rixia do anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10705FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FRight...\x02\x03",
            "#00200FEven if Rixia dirtied her\x01",
            "hands and solved this case,\x01",
            "I think KeA would be sad.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_15B7")

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, there's no guarantee that\x01",
            "such a forceful method would even\x01",
            "go as planned in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FYou're right... The enemy\x01",
            "has control over KeA's\x01",
            "Miracles.\x02\x03",
            "#10101FIn any case, since things\x01",
            "have come to this, we have\x01",
            "to try something else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F1")

    label("loc_15B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_16DC")

    ChrTalk(
        0x107,
        (
            "#12P#01200F#3CAlso, there's no guarantee that\x01",
            "a plan making use of forceful\x01",
            "methods would succeed.\x02\x03",
            "After all, the enemy is in\x01",
            "possession of the Divine\x01",
            "Child's 'Miracles'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FAnyway, since things have come\x01",
            "to this point, we can only\x01",
            "look for some other method.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F1")

    label("loc_16DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_17F1")

    ChrTalk(
        0x107,
        (
            "#12P#01200F#3CAlso, there's no guarantee that\x01",
            "a plan making use of forceful\x01",
            "methods would succeed.\x02\x03",
            "After all, the enemy is in\x01",
            "possession of the Divine\x01",
            "Child's 'Miracles'.\x02\x03",
            "#01203FAs this is the case, there is\x01",
            "no choice but to explore\x01",
            "another method of approach.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F1")


    ChrTalk(
        0x9,
        (
            "#5P#03203F...Yes, I know. Now that I no\x01",
            "longer have any pawns left to move,\x01",
            "I have no reason to be stubborn.\x02\x03",
            "#03200FIn order to break out of this\x01",
            "situation, I can only rely on you\x01",
            "now.\x02\x03",
            "#03204FFor our sake too, please do all you\x01",
            "can to rattle our dear President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes, please leave it to\x01",
            "us.\x02\x03",
            "#00003FAnd if something does\x01",
            "happen, I'll be counting\x01",
            "on you to lend us a hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10703F...Please, stay safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03209FNever I would have\x01",
            "imagined to receive such\x01",
            "words from Master Yin.\x02\x03",
            "#03204F...Well then, I'll\x01",
            "excuse myself here.\x02\x03",
            "#03200FLau, please guide them\x01",
            "on their way back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Yes, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As a parting gift, Lloyd and the\x01",
            "others received a \x01\x07\x02",
            "#14IBurst Orb\x07\x05",
            " from Cao.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x20C, 1)
    SetScenarioFlags(0x1BE, 6)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B1E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1B1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B37")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1B37")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7F6 end

    def Function_10_1B4D(): pass

    label("Function_10_1B4D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 3)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x1F)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7900, 6000, -670, 180)
    SetChrPos(0x8, -9100, 6000, 210, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BBF")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1BBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BD8")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1BD8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C06")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C2A")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C2A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C4E")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C72")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C96")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C96")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CBA")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1CBA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CDE")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D02")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1D02")

    OP_68(-20060, 6200, -53820, 0)
    MoveCamera(58, 11, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(16700, 0)
    FadeToBright(2000, 0)
    OP_68(-12270, 8000, -29610, 7000)
    MoveCamera(31, 13, 0, 7000)
    OP_6E(520, 7000)
    SetCameraDistance(20250, 7000)
    Sleep(7600)
    Fade(500)
    OP_68(-13990, 8800, -7980, 0)
    MoveCamera(46, 9, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(10780, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#5P#03204FI would expect nothing less from the\x01",
            "SSS.\x02\x03",
            "To think you delivered the "Independent\x01",
            "State of Crossbell" declaration of\x01",
            "invalidity with Chairman MacDowell...\x02\x03",
            "#03210FTo think such a thrilling event\x01",
            "occurred. Even I could never have\x01",
            "anticipated it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes, it's because of the cooperation\x01",
            "of many different people that we\x01",
            "were able to get this far.\x02\x03",
            "#00001FWe've figured out a way to release\x01",
            "the Barrier protecting Crossbell as\x01",
            "well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIf we can release the Barrier,\x01",
            "we can enter Crossbell City\x01",
            "where KeA currently is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHehe. It's been slow, but\x01",
            "the situation has been\x01",
            "changing for the better.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2078")

    ChrTalk(
        0x106,
        (
            "#12P#10701FBy the way... How is\x01",
            "Heiyue's situation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BD")

    label("loc_2078")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20BD")

    ChrTalk(
        0x105,
        (
            "#12P#10402FBy the way... What's\x01",
            "your situation?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BD")


    ChrTalk(
        0x9,
        (
            "#5P#03200FWell, the Red Constellation unit that\x01",
            "was looking for us has withdrawn for\x01",
            "now, so we can catch our breath.\x02\x03",
            "#03204FThe State Guard unit patrolling the\x01",
            "highways seems to have returned to\x01",
            "base as well.\x02\x03",
            "#03200FGiven the situation, the Mainz area\x01",
            "resistance should be out of danger\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(
        0x109,
        (
            "#12P#10103FI was worried about 2nd\x01",
            "Lt. Mireille, but...\x02\x03",
            "#10102FWith this, we can rest\x01",
            "easy for now, Randy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F9")

    label("loc_2273")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22F9")

    ChrTalk(
        0x105,
        (
            "#12P#10404FIt seems Mireille and\x01",
            "the others will be all\x01",
            "right for some time.\x02\x03",
            "#10402FRandy. Aren't you\x01",
            "relieved?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F9")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#12P#00303FNo... I can't be.\x02\x03",
            "#00301FSetting aside the State Guard, uncle\x01",
            "and the others won't give a damn\x01",
            "about the declaration of invalidity.\x02\x03",
            "Even their withdrawal was most\x01",
            "likely just to make sure their\x01",
            "preparations are perfect...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FNaturally, that's likely.\x02\x03",
            "#03201FIt should be only a matter of\x01",
            "time until a more thorough "hunt"\x01",
            "than the one in Mainz occurs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00010F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00208FIndeed, it seems we\x01",
            "can't let our guard down\x01",
            "just yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03206FWell, I hope you all\x01",
            "destroy the barrier for us\x01",
            "very soon.\x02\x03",
            "#03200FIf you do, we can change\x01",
            "from a purely defensive\x01",
            "stance to an offensive one.\x02\x03",
            "#03204FWhen we do, we'll once\x01",
            "again assist you in\x01",
            "liberating Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...Understood.\x02\x03",
            "Getting through the Ouroboros'\x01",
            "defenses and releasing the\x01",
            "barrier won't be easy, but...\x02\x03",
            "#00000FWe'll do it for sure. For you\x01",
            "and your men and the\x01",
            "resistance too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes... Let's do our\x01",
            "best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHehe, how promising.\x02\x03",
            "#03200F...Well then, I'll\x01",
            "excuse myself here.\x02\x03",
            "#03204FLau, please guide them\x01",
            "on their way back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Yes, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "As a parting gift, Lloyd and\x01",
            "the others received a\x01",
            "#14I\x07\x02",
            "Zeram Powder\x07\x05",
            " from Cao.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1FE, 1)
    SetScenarioFlags(0x1BE, 7)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2819")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2819")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2832")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2832")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1B4D end

    def Function_11_2848(): pass

    label("Function_11_2848")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_2876"),
        (1, "loc_288C"),
        (2, "loc_28A2"),
        (3, "loc_28B8"),
        (4, "loc_28CE"),
        (5, "loc_28E4"),
        (SWITCH_DEFAULT, "loc_28FA"),
    )


    label("loc_2876")

    SetChrPos(0xFE, -8720, 6000, -3540, 0)
    Jump("loc_28FA")

    label("loc_288C")

    SetChrPos(0xFE, -7650, 6000, -3710, 0)
    Jump("loc_28FA")

    label("loc_28A2")

    SetChrPos(0xFE, -9860, 6000, -4019, 0)
    Jump("loc_28FA")

    label("loc_28B8")

    SetChrPos(0xFE, -6540, 6000, -3770, 0)
    Jump("loc_28FA")

    label("loc_28CE")

    SetChrPos(0xFE, -8820, 6000, -5420, 0)
    Jump("loc_28FA")

    label("loc_28E4")

    SetChrPos(0xFE, -7260, 6000, -5220, 0)
    Jump("loc_28FA")

    label("loc_28FA")

    Return()

    # Function_11_2848 end

    SaveToFile()

Try(main)
