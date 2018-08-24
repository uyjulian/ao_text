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
        "Function_5_527",          # 05, 5
        "Function_6_5CF",          # 06, 6
        "Function_7_81C",          # 07, 7
        "Function_8_C58",          # 08, 8
        "Function_9_D16",          # 09, 9
        "Function_10_DC9",         # 0A, 10
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E5")
    TurnDirection(0xFE, 0x101, 0)

    label("loc_2E5")


    ChrTalk(
        0x101,
        "#00005FYou're from Heiyue...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Thanks for your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 5)

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348")
    Call(0, 5)
    Jump("loc_3F8")

    label("loc_348")


    ChrTalk(
        0xFE,
        (
            "...Due to countermeasures against Red\x01",
            "Constellation, Master Cao won't have\x01",
            "time to meet with you for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the Barrier is\x01",
            "released, we'll contact\x01",
            "you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F8")

    Jump("loc_523")

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_464")

    ChrTalk(
        0xFE,
        (
            "At present, Master Cao\x01",
            "is busy at our hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come again\x01",
            "another time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_523")

    label("loc_464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47F")
    Call(0, 5)
    Jump("loc_523")

    label("loc_47F")


    ChrTalk(
        0xFE,
        (
            "Please visit us again if\x01",
            "the situation develops\x01",
            "further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are able to meet with\x01",
            "Cao, speak to me and I'll\x01",
            "show you to our hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Goodbye.\x02",
    )

    CloseMessageWindow()

    label("loc_523")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BE end

    def Function_5_527(): pass

    label("Function_5_527")


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
        "...What will you do?\x02",
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
            "Cancel\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5C1"),
        (1, "loc_5C9"),
        (SWITCH_DEFAULT, "loc_5CE"),
    )


    label("loc_5C1")

    Call(0, 6)
    Jump("loc_5CE")

    label("loc_5C9")

    Jump("loc_5CE")

    label("loc_5CE")

    Return()

    # Function_5_527 end

    def Function_6_5CF(): pass

    label("Function_6_5CF")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_636")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_636")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_64F")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_64F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67D")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A1")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C5")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E9")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70D")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_731")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_731")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_755")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_755")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_779")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_779")

    FadeToBright(250, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "...Understood. Then,\x01",
            "follow me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will show you to\x01",
            "Master Cao.\x02",
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

    # Function_6_5CF end

    def Function_7_81C(): pass

    label("Function_7_81C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(7430, 600, 26010, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23040, 0)
    Call(0, 8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87B")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_87B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_894")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_894")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C2")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E6")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90A")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92E")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_952")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_952")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_976")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_976")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99A")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BE")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BE")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8A")

    ChrTalk(
        0x8,
        (
            "#11PPlease visit us again if\x01",
            "the situation develops\x01",
            "further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you are able to meet with\x01",
            "Cao, speak to me and I'll\x01",
            "show you to our hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...Goodbye.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9A")

    label("loc_A8A")


    ChrTalk(
        0x8,
        (
            "#11P...Due to countermeasures against Red\x01",
            "Constellation, Master Cao won't have\x01",
            "time to meet with you for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAfter the Barrier is\x01",
            "released, we'll contact\x01",
            "you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PUnderstood.\x02\x03",
            "#00001F...Please, be careful\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...Goodbye.\x02",
    )

    CloseMessageWindow()

    label("loc_B9A")

    OP_93(0x8, 0x5A, 0x1F4)
    SetChrFlags(0x8, 0x40)
    Sleep(500)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)

    def lambda_BC7():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BC7)
    Sleep(500)

    def lambda_BDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BDF)
    Sleep(1000)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)
    Sleep(500)
    SetChrPos(0x0, 6680, 0, 25520, 89)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C35")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4E")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_C4E")

    SetScenarioFlags(0x0, 0)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_7_81C end

    def Function_8_C58(): pass

    label("Function_8_C58")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C78")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C8D")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CA2")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB7")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CCC")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE1")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF6")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D0B")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D0B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_8_C58 end

    def Function_9_D16(): pass

    label("Function_9_D16")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_D44"),
        (1, "loc_D5A"),
        (2, "loc_D70"),
        (3, "loc_D86"),
        (4, "loc_D9C"),
        (5, "loc_DB2"),
        (SWITCH_DEFAULT, "loc_DC8"),
    )


    label("loc_D44")

    SetChrPos(0xFE, 6190, 0, 25480, 89)
    Jump("loc_DC8")

    label("loc_D5A")

    SetChrPos(0xFE, 6530, 0, 26710, 135)
    Jump("loc_DC8")

    label("loc_D70")

    SetChrPos(0xFE, 5760, 0, 24300, 89)
    Jump("loc_DC8")

    label("loc_D86")

    SetChrPos(0xFE, 4670, 0, 25670, 89)
    Jump("loc_DC8")

    label("loc_D9C")

    SetChrPos(0xFE, 5510, 0, 27070, 135)
    Jump("loc_DC8")

    label("loc_DB2")

    SetChrPos(0xFE, 4440, 0, 24100, 89)
    Jump("loc_DC8")

    label("loc_DC8")

    Return()

    # Function_9_D16 end

    def Function_10_DC9(): pass

    label("Function_10_DC9")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
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
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8B")
    OP_E2(0x2)
    MiniGame(0x6, 0x1C, 0x15F4, 0x0, 0xFFFFAA10, 0x0, 0x13D8, 0xFFFFFE0C, 0xFFFFBC30)

    label("loc_E8B")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_DC9 end

    SaveToFile()

Try(main)
