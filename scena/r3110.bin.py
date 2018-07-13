from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3110.bin",                # FileName
        "r3110",                    # MapName
        "r3110",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x17,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 102, 0, 1, 0, 2],
    )

    BuildStringList((
        "r3110",                  # 0
        "Lau",                    # 1
    ))

    AddCharChip((
        "chr/ch31400.itc",                   # 00
    ))

    DeclNpc(8170,    0,       25590,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(5620,    0,       4294945296, 1200,    5080,    4294966796, 4294949936, 0x007C, 0,  10, 0x0000)
    DeclActor(9050,    0,       25630,   1000,    8590,    1500,    25370,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_1D8",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_292",          # 03, 3
        "Function_4_2BE",          # 04, 4
        "Function_5_56F",          # 05, 5
        "Function_6_61B",          # 06, 6
        "Function_7_86A",          # 07, 7
        "Function_8_CCA",          # 08, 8
        "Function_9_D88",          # 09, 9
        "Function_10_E3B",         # 0A, 10
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_160"),
        (1, "loc_16C"),
        (2, "loc_178"),
        (3, "loc_184"),
        (4, "loc_190"),
        (5, "loc_19C"),
        (6, "loc_1A8"),
        (SWITCH_DEFAULT, "loc_1B4"),
    )


    label("loc_160")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_16C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_178")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_184")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_190")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_19C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1D7")

    Return()

    # Function_0_128 end

    def Function_1_1D8(): pass

    label("Function_1_1D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_1F4")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1F4")
    ClearChrFlags(0x8, 0x80)

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_203")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)

    label("loc_203")

    Return()

    # Function_1_1D8 end

    def Function_2_204(): pass

    label("Function_2_204")

    ClearMapObjFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21C")
    OP_66(0x1, 0x1)
    Jump("loc_241")

    label("loc_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_23D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238")
    OP_65(0x1, 0x1)
    ClearChrFlags(0x8, 0x80)

    label("loc_238")

    Jump("loc_241")

    label("loc_23D")

    OP_66(0x1, 0x1)

    label("loc_241")

    Sound(127, 1, 100, 0)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 5080, -500, -17360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_2_204 end

    def Function_3_292(): pass

    label("Function_3_292")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is firmly shut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_3_292 end

    def Function_4_2BE(): pass

    label("Function_4_2BE")

    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E5")
    TurnDirection(0xFE, 0x101, 0)

    label("loc_2E5")


    ChrTalk(
        0x101,
        "#00005FYou're from the Heiyue...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Thank you for your hard work.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 5)

    label("loc_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F")
    Call(0, 5)
    Jump("loc_404")

    label("loc_34F")


    ChrTalk(
        0xFE,
        (
            "...Due to countermeasures against the\x01",
            ""Red Constellation", Master Cao won't\x01",
            "have time to meet you for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the "barrier" is released,\x01",
            "we will contact you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404")

    Jump("loc_56B")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_488")

    ChrTalk(
        0xFE,
        (
            "At present, Master Cao is\x01",
            "being busy at his hiding place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, pay him a visit on another occasion.\x02",
    )

    CloseMessageWindow()
    Jump("loc_56B")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_56B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3")
    Call(0, 5)
    Jump("loc_56B")

    label("loc_4A3")


    ChrTalk(
        0xFE,
        (
            "Please, come visit us after the\x01",
            "circumstances have improved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it will be feasible to meet\x01",
            "Master Cao, please speak to me and I\x01",
            "will bring you to his hiding place again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Goodbye.\x02",
    )

    CloseMessageWindow()

    label("loc_56B")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BE end

    def Function_5_56F(): pass

    label("Function_5_56F")


    ChrTalk(
        0xFE,
        (
            "You can meet Master Cao\x01",
            "in his hiding place now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...What do you want to do?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Meet Cao\x01",      # 0
            "Quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_60D"),
        (1, "loc_615"),
        (SWITCH_DEFAULT, "loc_61A"),
    )


    label("loc_60D")

    Call(0, 6)
    Jump("loc_61A")

    label("loc_615")

    Jump("loc_61A")

    label("loc_61A")

    Return()

    # Function_5_56F end

    def Function_6_61B(): pass

    label("Function_6_61B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x10E, 0x0)
    ClearChrFlags(0x8, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(7430, 600, 26010, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23040, 0)
    Call(0, 8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_682")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_682")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_69B")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_69B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C9")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6ED")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_711")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_711")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_735")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_735")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_759")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_759")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77D")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A1")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7C5")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C5")

    FadeToBright(250, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "...I understand.\x01",
            "Then, this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will guide you\x01",
            "to Master Cao.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    Sleep(700)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(127, 1000, 30)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4700", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_6_61B end

    def Function_7_86A(): pass

    label("Function_7_86A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(7430, 600, 26010, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23040, 0)
    Call(0, 8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8C9")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_8C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8E2")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_8E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_910")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_910")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_934")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_934")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_958")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_958")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97C")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A0")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9C4")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E8")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0C")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0C")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFC")

    ChrTalk(
        0x8,
        (
            "#11PPlease, come visit us after the\x01",
            "circumstances have improved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhen it will be feasible to meet\x01",
            "Master Cao, please speak to me and I\x01",
            "will bring you to his hiding place again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...Goodbye.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C0C")

    label("loc_AFC")


    ChrTalk(
        0x8,
        (
            "#11P...Due to countermeasures against the\x01",
            ""Red Constellation", Master Cao won't\x01",
            "have time to meet you for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAfter the "barrier" is released,\x01",
            "we will contact you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PUnderstood.\x02\x03",
            "#00001F...Please, be careful too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...Goodbye.\x02",
    )

    CloseMessageWindow()

    label("loc_C0C")

    OP_93(0x8, 0x5A, 0x1F4)
    SetChrFlags(0x8, 0x40)
    Sleep(500)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)

    def lambda_C39():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C39)
    Sleep(500)

    def lambda_C51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C51)
    Sleep(1000)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)
    Sleep(500)
    SetChrPos(0x0, 6680, 0, 25520, 89)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC0")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_CC0")

    SetScenarioFlags(0x0, 0)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_7_86A end

    def Function_8_CCA(): pass

    label("Function_8_CCA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEA")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CFF")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D14")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D29")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D3E")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D53")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D68")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D7D")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D7D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_8_CCA end

    def Function_9_D88(): pass

    label("Function_9_D88")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_DB6"),
        (1, "loc_DCC"),
        (2, "loc_DE2"),
        (3, "loc_DF8"),
        (4, "loc_E0E"),
        (5, "loc_E24"),
        (SWITCH_DEFAULT, "loc_E3A"),
    )


    label("loc_DB6")

    SetChrPos(0xFE, 6190, 0, 25480, 89)
    Jump("loc_E3A")

    label("loc_DCC")

    SetChrPos(0xFE, 6530, 0, 26710, 135)
    Jump("loc_E3A")

    label("loc_DE2")

    SetChrPos(0xFE, 5760, 0, 24300, 89)
    Jump("loc_E3A")

    label("loc_DF8")

    SetChrPos(0xFE, 4670, 0, 25670, 89)
    Jump("loc_E3A")

    label("loc_E0E")

    SetChrPos(0xFE, 5510, 0, 27070, 135)
    Jump("loc_E3A")

    label("loc_E24")

    SetChrPos(0xFE, 4440, 0, 24100, 89)
    Jump("loc_E3A")

    label("loc_E3A")

    Return()

    # Function_9_D88 end

    def Function_10_E3B(): pass

    label("Function_10_E3B")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(4120, 1000, -18910, 1500)
    MoveCamera(45, 34, 0, 1500)
    OP_6E(400, 1500)
    SetCameraDistance(30000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFB")
    OP_E2(0x2)
    MiniGame(0x6, 0x1C, 0x15F4, 0x0, 0xFFFFAA10, 0x0, 0x13D8, 0xFFFFFE0C, 0xFFFFBC30)

    label("loc_EFB")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_E3B end

    SaveToFile()

Try(main)
