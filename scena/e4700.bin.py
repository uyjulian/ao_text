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
        "Function_10_1AB2",        # 0A, 10
        "Function_11_27F5",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(
        0x9,
        (
            "#5P#03200FHu hu, thank you for coming.\x02\x03",
            "#03204FLong time no see too,\x01",
            "Mr. Randy, Miss Noｱl.\x02\x03",
            "#03209FIt seems there were some vicissitudes,\x01",
            "but I am glad you could meet safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FMan, I was shocked when I heard\x01",
            "we have a cooperative relationship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FMr. Cao,\x01",
            "you seem the same as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAlso...you've been staying\x01",
            "at the "Fort of Sun"?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_D41")

    ChrTalk(
        0x9,
        (
            "#5P#03200FHu hu, thank you for coming.\x02\x03",
            "#03204FLong time no see, Mr. Randy.\x02\x03",
            "#03209FIt seems you were working\x01",
            "hard in the Resistance...\x01",
            "How are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FMan, I was shocked when I heard\x01",
            "we have a cooperative relationship...\x02\x03",
            "#00301FYou seem to be the same as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAlso...you've been staying\x01",
            "at the "Fort of Sun"?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E3C")

    ChrTalk(
        0x9,
        (
            "#5P#03200FHu hu, thank you for coming.\x02\x03",
            "#03209FAs I thought, Mr. Lloyd, you were \x01",
            "worried about me and came...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006FN-No...that's not that.\x02\x03",
            "#00001FRather, you've been staying\x01",
            "at the "Fort of Sun"?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")


    ChrTalk(
        0x9,
        (
            "#5P#03204FYes, there're the facilities\x01",
            "the "Cult" was using too...\x01",
            "It's convenient in many aspects for hiding.\x02\x03",
            "#03200FFurthermore, even the State Guard\x01",
            "and the "Red Constellation" can't\x01",
            "easily get inside.\x02\x03",
            "They won't notice the existence of the\x01",
            "secret passage you all came through too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FHu hu, that's true.\x02\x03",
            "#10402FEven the road he showed us...\x01",
            "It seems he used a quite\x01",
            "complex route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FRight...I don't think we could reach\x01",
            "this place again alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...You noticed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHu hu, that's all right.\x01",
            "But please, no words to others.\x02",
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
            "#5P#03200FYes, I intend to bide my time here\x01",
            "while observing the situation.\x02\x03",
            "#03203FThe Crossbell barrier...\x01",
            "Unless something is done about that,\x01",
            "we can't move too.\x02\x03",
            "#03200FFacing directly the State Guard\x01",
            "and the "Red Constellation"\x01",
            "would be a bit too hard.\x02\x03",
            "#03206FWell, if we had Master "Yin" with us, \x01",
            "we would have a way, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10703F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10404FHu hu, it wouldn't be a\x01",
            "decent way anyway, hm?\x02\x03",
            "#10402FA forcible and bloody way, like having\x01",
            "her completely dirty her hands, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03210FWell, I wonder...\x01",
            "I will leave that to your imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F...After having got her back from you,\x01",
            "we absolutely won't make Rixia\x01",
            "do such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10705FMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FRight... \x02\x03",
            "#00200FEven if Miss Rixia dirtied her hands\x01",
            "and solved this case, I think that\x01",
            "KeA would be sad.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_151B")

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, it's not even assured that, by taking\x01",
            "a forcible method, it would go as planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FYou're right...\x01",
            "The enemy has control\x01",
            "over KeA's "miracles".\x02\x03",
            "#10101FIn any case, having things\x01",
            "become like this, we can\x01",
            "only look for another way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_151B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_163B")

    ChrTalk(
        0x107,
        (
            "#12P#01200F#3CAlso, it's not even assured that, by taking a\x01",
            "forcible method, it would go as planned, hm?\x02\x03",
            "After all, the enemy is in possession\x01",
            "of the Divine Child's "miracles".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FAnyway, having things become like this, \x01",
            "we can only look for another way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1747")

    label("loc_163B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1747")

    ChrTalk(
        0x107,
        (
            "#12P#01200F#3CAlso, it's not even assured that, by taking a\x01",
            "forcible method, it would go as planned, hm?\x02\x03",
            "After all, the enemy is in possession\x01",
            "of the Divine Child's "miracles".\x02\x03",
            "#01203FHaving things become like this,\x01",
            "we can only search for another way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1747")


    ChrTalk(
        0x9,
        (
            "#5P#03203F...Yes, I know.\x01",
            "Now that I don't have any pawn to move,\x01",
            "I have no reason to be stubborn too.\x02\x03",
            "#03200FIn order to break out of\x01",
            "this situation, I can \x01",
            "only rely on you now.\x02\x03",
            "#03204FFor our sake too, please move\x01",
            "around as much as possible\x01",
            "and stir the President's party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYes, please leave it to us.\x02\x03",
            "#00003FYou too, when something happen,\x01",
            "please give us your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#12P#10703F...Please, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03209FHu hu, never I would have imagined\x01",
            "to receive such words from Master "Yin".\x02\x03",
            "#03204F...Well then, I will \x01",
            "excuse myself here.\x02\x03",
            "#03200FLau, please guide them\x01",
            "to where they came from.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Sir.\x02",
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
            "As a parting gift, Lloyd and the others received a\x01",
            "#14IBurst Orb from Cao.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1A83")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1A83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1A9C")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1A9C")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7F6 end

    def Function_10_1AB2(): pass

    label("Function_10_1AB2")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B24")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1B24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B3D")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1B3D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B6B")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B8F")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BB3")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BD7")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BFB")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C1F")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C43")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C67")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1C67")

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
            "#5P#03204FNothing less expected from the SSS.\x02\x03",
            "To think you accomplished the declaration\x01",
            "of invalidity for the "Independent State of\x01",
            "Crossbell" with Chairman MacDowell...\x02\x03",
            "#03210FTo think that such a thrilling event,\x01",
            "that even I didn't anticipate, happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes, because of the cooperation\x01",
            "of a lot of people we somehow\x01",
            "managed to reach this much.\x02\x03",
            "#00001FWe figured out a method to dissolve\x01",
            "the "barrier" protecting Crossbell too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIf we could even dissolve the "barrier",\x01",
            "we could enter Crossbell City where\x01",
            "KeA is at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHu hu, it is just a little bit, but the\x01",
            "situation has been changing for the better.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FF9")

    ChrTalk(
        0x106,
        (
            "#12P#10701FBy the way...\x01",
            "How is the "Heiyue" hiding situation?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2044")

    label("loc_1FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2044")

    ChrTalk(
        0x105,
        (
            "#12P#10402FBy the way...\x01",
            "How's your hiding situation?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2044")


    ChrTalk(
        0x9,
        (
            "#5P#03200FWell, the "Red Constellation" that was \x01",
            "looking for us has withdrawn for now,\x01",
            "so we can take a short breath.\x02\x03",
            "#03204FThe State Guard that was patrolling the\x01",
            "highways seems to have gone back too.\x02\x03",
            "#03200FGiven the situation, the\x01",
            "Mainz area Resistance\x01",
            "can escape harm for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(
        0x109,
        (
            "#12P#10103FI was worried about Second\x01",
            "Lieutenant Mireille, but...\x02\x03",
            "#10102FWith this, we can stay\x01",
            "relieved, senior Randy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2294")

    label("loc_21F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2294")

    ChrTalk(
        0x105,
        (
            "#12P#10404FIt seems that Miss Mireille and the\x01",
            "others will be all right for some time.\x02\x03",
            "#10402FHu hu, Randy.\x01",
            "Aren't you relieved too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2294")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    ChrTalk(
        0x104,
        (
            "#12P#00303FNo...I can't.\x02\x03",
            "#00301FAside the State Guard, uncle\x01",
            "and the others won't give a damn\x01",
            "about the declaration of invalidity.\x02\x03",
            "Probably, even their withdrawal\x01",
            "was just to make perfect preparations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FNaturally, the probability is very high.\x02\x03",
            "#03201FIt should be only a matter of time\x01",
            "since a more thorough "hunt" than\x01",
            "the one happened in Mainz occurs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00010F......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00208FIt really seems right to say that it's a\x01",
            "situation to not let our guard down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03206FWell, I expect you all\x01",
            "to quickly destroy\x01",
            "the "barrier".\x02\x03",
            "#03200FWithout that, we can turn\x01",
            "to attack from a state of\x01",
            "war of complete defense.\x02\x03",
            "#03204FWhen that happens,\x01",
            "we will cooperate too\x01",
            "to free Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...Understood.\x02\x03",
            "Getting through the "Society"'s\x01",
            "defences and dissolving the\x01",
            "barrier won't be easy, but...\x02\x03",
            "#00000FWe'll do it for sure,\x01",
            "for Mr. Cao, his men\x01",
            "and the Resistance too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYes...let's do our best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#03204FHu hu, how trustworthy.\x02\x03",
            "#03200F...Well then, I will \x01",
            "excuse myself here.\x02\x03",
            "#03204FLau, please guide them\x01",
            "to where they came from.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "Sir.\x02",
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
            "As a parting gift, Lloyd and the others received a\x01",
            "#14IZelam Powder from Cao.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27C6")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_27C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27DF")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_27DF")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1AB2 end

    def Function_11_27F5(): pass

    label("Function_11_27F5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_2823"),
        (1, "loc_2839"),
        (2, "loc_284F"),
        (3, "loc_2865"),
        (4, "loc_287B"),
        (5, "loc_2891"),
        (SWITCH_DEFAULT, "loc_28A7"),
    )


    label("loc_2823")

    SetChrPos(0xFE, -8720, 6000, -3540, 0)
    Jump("loc_28A7")

    label("loc_2839")

    SetChrPos(0xFE, -7650, 6000, -3710, 0)
    Jump("loc_28A7")

    label("loc_284F")

    SetChrPos(0xFE, -9860, 6000, -4019, 0)
    Jump("loc_28A7")

    label("loc_2865")

    SetChrPos(0xFE, -6540, 6000, -3770, 0)
    Jump("loc_28A7")

    label("loc_287B")

    SetChrPos(0xFE, -8820, 6000, -5420, 0)
    Jump("loc_28A7")

    label("loc_2891")

    SetChrPos(0xFE, -7260, 6000, -5220, 0)
    Jump("loc_28A7")

    label("loc_28A7")

    Return()

    # Function_11_27F5 end

    SaveToFile()

Try(main)
