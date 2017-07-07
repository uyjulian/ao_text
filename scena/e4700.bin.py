from ScenarioHelper import *

def main():
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
        "Row",                   # 1
        "Tsao",                 # 2
        "camera",                 # 3
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
        "Function_10_1980",        # 0A, 10
        "Function_11_2598",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BBE")

    ChrTalk(
        0x9,
        (
            "#5P#03200FHe bought me well.\x02\x03",
            "#03204FWith Randy\x01",
            "Noel is also a long time.\x02\x03",
            "#03209FIt seems there were twists and turns,\x01",
            "I am able to merge safely and are the most important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWhew, it became a cooperative relationship\x01",
            "I was surprised when I heard it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FTsaoさんも\x01",
            "It seems as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAnd … inside the \"Fort of the Sun\"\x01",
            "You were lurking, were not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_D1F")

    ChrTalk(
        0x9,
        (
            "#5P#03200FHe bought me well.\x02\x03",
            "#03204FRandy is also a long time.\x02\x03",
            "#03209FFor resistance activities\x01",
            "He seems to have worked,\x01",
            "Is not there change?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWhew, it became a cooperative relationship\x01",
            "I was surprised when I heard it … …\x02\x03",
            "#00301FYou look alright as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAnd … inside the \"Fort of the Sun\"\x01",
            "You were lurking, were not you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E20")

    ChrTalk(
        0x9,
        (
            "#5P#03200FHe bought me well.\x02\x03",
            "#03209FLloyd, after all, \"black moon\"\x01",
            "Did you feel like you can come?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, no … That's why.\x02\x03",
            "#00001FOr inside the \"Fort of the Sun\"\x01",
            "You were lurking, were not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")


    ChrTalk(
        0x9,
        (
            "#5P#03204FYeah, I used the \"cult\"\x01",
            "There are facilities,\x01",
            "It is convenient for latency.\x02\x03",
            "#03200FAnd here, the defense forces and\x01",
            "Even with \"red constellation\"\x01",
            "You can not get in.\x02\x03",
            "As for the hidden passage that everyone has come through,\x01",
            "I have not noticed the existence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FHuh, indeed.\x02\x03",
            "#10402FThere was also a way guided to him there\x01",
            "A fairly complex route\x01",
            "I guess you used it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FThat's right … only us\x01",
            "I do not feel like I can come here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "… … Did you notice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHuh, that's fine.\x01",
            "Do not forget the other words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#12P#10701F…… Black Monday,\x01",
            "For a while in this place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03200FYeah, while looking at the trend here\x01",
            "I am going to wait for the aircraft.\x02\x03",
            "#03203FCrossbell city barrier ……\x01",
            "As long as we do not manage that\x01",
            "It can not move to move it.\x02\x03",
            "#03200FDefense Army and \"Red Constellation\"\x01",
            "You also want to make a partner from the front\x01",
            "Somewhat frustrating.\x02\x03",
            "#03206FWell, if \"silver\" is at hand\x01",
            "There was a method also here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10703F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FHuh, whatever\x01",
            "It probably is not a rock method.\x02\x03",
            "#10402FHer hands are soiled thoroughly,\x01",
            "Is it a brute force and blood smelling way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03210FWell, how is it ….\x01",
            "I will leave it to your imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F…… As I took over here,\x01",
            "Absolutely to Lisha\x01",
            "I will not let such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10705FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FI agree……\x02\x03",
            "#00200FDirty the hands of Lisha\x01",
            "Even if we solve this incident,\x01",
            "I think Ka'a will grieve.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1494")

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, in a place that took a somewhat brute force method\x01",
            "It is not even possible to go as planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FI agree……\x01",
            "The opponent plays Ka'aa's \"miracle\"\x01",
            "That's why I put it in my hands.\x02\x03",
            "#10101FAnyway, over this\x01",
            "I only have to find another way\x01",
            "Is not it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1655")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_157E")

    ChrTalk(
        0x107,
        (
            "#12P#01200F#3CBesides, I took a somewhat brute force method\x01",
            "It will not be easy to proceed as planned.\x02\x03",
            "Whatever, the opponent makes his \"miracle\"\x01",
            "Because it is putting in the hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FAnyway, over this\x01",
            "I guess you have to find another way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1655")

    label("loc_157E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1655")

    ChrTalk(
        0x107,
        (
            "#12P#01200F#3CBesides, I took a somewhat brute force method\x01",
            "It will not be easy to proceed as planned.\x02\x03",
            "Whatever, the opponent makes his \"miracle\"\x01",
            "Because it is putting in the hand.\x02\x03",
            "#01203FThis is the way it is, another way\x01",
            "There is no choice but to explore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1655")


    ChrTalk(
        0x9,
        (
            "#5P#03203F…… Yeah, I know.\x01",
            "Now that you do not have the pieces to do,\x01",
            "There is no reason to stick to it.\x02\x03",
            "#03200FTo break through this situation\x01",
            "You are no longer\x01",
            "There is no choice but to rely on it.\x02\x03",
            "#03204FFor us also,\x01",
            "At most it moves around\x01",
            "Please disturb the President.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FWell, please leave it to me.\x02\x03",
            "#00003FWhen there is something there\x01",
            "Thank you for your collaboration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10703F… … Please be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03209FHuh, no way from \"silver\"\x01",
            "It is said that you can receive such words.\x02\x03",
            "#03204F… Well then, I am here\x01",
            "I will let you get rude.\x02\x03",
            "#03200FRow、彼らを元の場所まで\x01",
            "Please give me a guide.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Ha ha.\x02",
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
            "ロイドたちは帰り際、Tsaoから\x07\x02\x01",
            "#14IBurst orb\x07\x05",
            "Received.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('爆灵宝玉', 1)
    SetScenarioFlags(0x1BE, 6)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1951")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_196A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_196A")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7F6 end

    def Function_10_1980(): pass

    label("Function_10_1980")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19F2")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_19F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1A0B")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1A0B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A39")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A5D")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A81")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1A81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA5")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AC9")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AED")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B11")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B35")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B35")

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
            "#5P#03204FYou are a member of the Special Affairs Division, are not you?\x02\x03",
            "No way, with Mr. MacDael\x01",
            "\"Crossbell independent country\" of\x01",
            "To accomplish ineffective declaration …\x02\x03",
            "#03210FWhat a painful event has happened so far\x01",
            "I did not expect it either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah, with the cooperation of many people\x01",
            "Somehow far\x01",
            "I was able to get it done.\x02\x03",
            "#00001F\"Crossbar\" to protect Crossbell City\x01",
            "I also understood how to release it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIf you can cancel even \"barrier\"\x01",
            "In Crosbell City where Kia-a is\x01",
            "You can enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHuh, I'm a bit gradual\x01",
            "Surely the situation has turned around.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E3C")

    ChrTalk(
        0x106,
        (
            "#12P#10701Fby the way……\x01",
            "How is the latent situation of \"Black moon\"?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8C")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E8C")

    ChrTalk(
        0x105,
        (
            "#12P#10402Fby the way……\x01",
            "How is the latent situation there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8C")


    ChrTalk(
        0x9,
        (
            "#5P#03200FYeah, I was searching for us\x01",
            "\"Red constellation\" once raised,\x01",
            "It's a place to take a break.\x02\x03",
            "#03204FDefense forces, who were patrolling the highway,\x01",
            "It seems that he returned to a unit.\x02\x03",
            "#03200FIn this situation,\x01",
            "The resistance of Mainz direction is also\x01",
            "For the time being, it escaped the difficulty.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FFA")

    ChrTalk(
        0x109,
        (
            "#12P#10103FThe three Lieutenant Mireille\x01",
            "I was worried … ….\x02\x03",
            "#10102FWith this for now\x01",
            "It's a sense of relief, Randy-senpai!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_1FFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_207C")

    ChrTalk(
        0x105,
        (
            "#12P#10404FMireilleu also,\x01",
            "Anyway it seems to be okay.\x02\x03",
            "#10402FHuff, Randy.\x01",
            "You guys were relieved, did not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207C")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#12P#00303FNo … I can not rest assured.\x02\x03",
            "#00301FRegardless of the defense army,\x01",
            "Uncle yourself as invalid declaration\x01",
            "I guess if I care about it.\x02\x03",
            "Probably, I raised it once\x01",
            "To prepare thorough preparation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FOf course, that possibility would be high.\x02\x03",
            "#03201FMore than done in Mainz\x01",
            "Thorough \"hunting\" begins,\x01",
            "It should be a matter of time any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00010FHuh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00208FThere is no circumstance that I can not escape completely\x01",
            "Sounds good to hear …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03206FWell, everyone has a \"barrier\"\x01",
            "I will break it soon\x01",
            "I expect it.\x02\x03",
            "#03200FIf that loses even,\x01",
            "From protecting war dead battlefields\x01",
            "You can turn it offensive.\x02\x03",
            "#03204FWhen that happens again,\x01",
            "We also release the Crossbell City\x01",
            "I will cooperate with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F……I understand.\x02\x03",
            "Overcome the defense of \"association\"\x01",
            "To cancel the barrier\x01",
            "It will not be easy, but …\x02\x03",
            "#00000FTsaoさんたちや\x01",
            "Even for resistance,\x01",
            "I will definitely do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYeah … let's do our best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHuh, it's as reliable as it is.\x02\x03",
            "#03200F… Well then, I am here\x01",
            "I will let you get rude.\x02\x03",
            "#03204FRow、彼らを元の場所まで\x01",
            "Please give me a guide.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Ha ha.\x02",
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
            "ロイドたちは帰り際、Tsaoから\x07\x02\x01",
            "#14IZelum powder\x07\x05",
            "Received.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('还魂粉', 1)
    SetScenarioFlags(0x1BE, 7)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2569")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2582")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2582")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1980 end

    def Function_11_2598(): pass

    label("Function_11_2598")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_25C6"),
        (1, "loc_25DC"),
        (2, "loc_25F2"),
        (3, "loc_2608"),
        (4, "loc_261E"),
        (5, "loc_2634"),
        (SWITCH_DEFAULT, "loc_264A"),
    )


    label("loc_25C6")

    SetChrPos(0xFE, -8720, 6000, -3540, 0)
    Jump("loc_264A")

    label("loc_25DC")

    SetChrPos(0xFE, -7650, 6000, -3710, 0)
    Jump("loc_264A")

    label("loc_25F2")

    SetChrPos(0xFE, -9860, 6000, -4019, 0)
    Jump("loc_264A")

    label("loc_2608")

    SetChrPos(0xFE, -6540, 6000, -3770, 0)
    Jump("loc_264A")

    label("loc_261E")

    SetChrPos(0xFE, -8820, 6000, -5420, 0)
    Jump("loc_264A")

    label("loc_2634")

    SetChrPos(0xFE, -7260, 6000, -5220, 0)
    Jump("loc_264A")

    label("loc_264A")

    Return()

    # Function_11_2598 end

    SaveToFile()

Try(main)
