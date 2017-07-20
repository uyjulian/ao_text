from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1650.bin",                # FileName
        "t1650",                    # MapName
        "t1650",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 88, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1650",                  # 0
        "Professor Seyland",         # 1
    ))

    AddCharChip((
        "chr/ch44802.itc",                   # 00
    ))

    DeclNpc(110690,  150,     57000,   270,  453,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)

    DeclActor(109380,  0,       57000,   1500,    110690,  1500,    57000,   0x007E, 0,  2,  0x0000)

    ChipFrameInfo(264, 0)                                        # 0

    ScpFunction((
        "Function_0_108",          # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_1CA",          # 02, 2
        "Function_3_1CE",          # 03, 3
        "Function_4_493",          # 04, 4
        "Function_5_1197",         # 05, 5
        "Function_6_11E2",         # 06, 6
        "Function_7_122D",         # 07, 7
        "Function_8_1278",         # 08, 8
        "Function_9_12C9",         # 09, 9
        "Function_10_1314",        # 0A, 10
        "Function_11_2F8B",        # 0B, 11
    ))


    def Function_0_108(): pass

    label("Function_0_108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_13E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_14D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_14D")

    Return()

    # Function_0_108 end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_160")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_160")

    OP_1B(0x1, 0x0, 0xB)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D")
    OP_66(0x0, 0x1)

    label("loc_18D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1C9")

    Return()

    # Function_1_14E end

    def Function_2_1CA(): pass

    label("Function_2_1CA")

    Call(0, 3)
    Return()

    # Function_2_1CA end

    def Function_3_1CE(): pass

    label("Function_3_1CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    Call(0, 10)
    Return()

    label("loc_1FA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399")

    ChrTalk(
        0x8,
        (
            "For those patients with that medicine\x01",
            "Most of the treatment was over,\x01",
            "Some have not issued an interrogation table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First, Crossbell City,\x01",
            "Dino boy living in the old city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next, the troupe of alkane shell\x01",
            "Artist, Nicole members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And the Crossbell Guard\x01",
            "A crew member at the Belgard gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tell them the circumstances,\x01",
            "I would like you to collect the interview table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once all gathered,\x01",
            "Please come back to report here again.\x01",
            "Well then, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_48F")

    label("loc_399")


    ChrTalk(
        0x8,
        (
            "Crossbell City,\x01",
            "Dino boy living in the old city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Theater company alkane shell\x01",
            "Artist, Nicole members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And the Crossbell Guard\x01",
            "A crew member at the Belgard gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tell them the circumstances,\x01",
            "I would like you to collect the interview table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well then, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    label("loc_48F")

    TalkEnd(0x8)
    Return()

    # Function_3_1CE end

    def Function_4_493(): pass

    label("Function_4_493")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 59520, 0, 59900, 0)
    OP_68(57330, 1000, 58820, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 57250, 0, 59010, 90)
    SetChrPos(0x102, 56500, 0, 57980, 90)
    SetChrPos(0x109, 56600, 0, 59920, 135)
    SetChrPos(0x105, 54680, 0, 57620, 90)
    SetChrPos(0x104, 55270, 0, 59030, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00000F─ ─ I'm sorry, I will excuse you.\x01",
            "I am a person in the Special Affairs Division … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Female voice",
        "Come in\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, 110690, 150, 57000, 270)
    SetChrSubChip(0x8, 0x1)
    OP_68(100830, 1250, 48810, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 98390, 0, 49590, 90)
    SetChrPos(0x102, 98390, 0, 49590, 90)
    SetChrPos(0x104, 98390, 0, 49590, 90)
    SetChrPos(0x109, 98390, 0, 49590, 90)
    SetChrPos(0x105, 98390, 0, 49590, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 7)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 8)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 9)
    OP_68(105790, 1250, 52080, 3000)
    MoveCamera(62, 24, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)

    NpcTalk(
        0x8,
        "A female doctor",
        "Hmm. You finally came huh\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A female doctor",
        (
            "From the time you were expecting\x01",
            "It's over 2 minutes but ….\x01",
            "Well it looks good to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00306F(No, it looks like I'm kinda stupid ……\x01",
            "It must be a beautiful woman. )\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "A female doctor",
        (
            "Well, for the time to come, come over here.\x01",
            "It's hard to talk at this distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FR-right\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_68(108640, 950, 57250, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20000, 5000)

    def lambda_8D2():
        OP_95(0xFE, 107920, 0, 57770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D2)
    Sleep(500)

    def lambda_8EF():
        OP_95(0xFE, 107840, 0, 56600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EF)
    Sleep(500)

    def lambda_90C():
        OP_95(0xFE, 106710, 0, 58390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90C)
    Sleep(700)

    def lambda_929():
        OP_95(0xFE, 106120, 0, 57330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_929)
    Sleep(500)

    def lambda_946():
        OP_95(0xFE, 106680, 0, 56190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_946)
    WaitChrThread(0x101, 1)

    def lambda_964():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_964)
    WaitChrThread(0x102, 1)

    def lambda_975():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_975)
    WaitChrThread(0x109, 1)

    def lambda_986():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_986)
    WaitChrThread(0x104, 1)

    def lambda_997():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_997)
    WaitChrThread(0x105, 1)

    def lambda_9A8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A8)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#00100FUm, you are\x01",
            "Professor Seyland, is not it?\x02\x03",
            "#00103FThe ingredients of Gnostic\x01",
            "It was that the analysis result came out - ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P─ ─ bad, but before that\x01",
            "There is something I want to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTo you guys, first of all\x01",
            "I would like you to clean up first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThe request you submitted right?\x02\x03",
            "#10301FGnostic analysis results\x01",
            "After having you hand it over\x01",
            "Is it useless?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt also relates to the analysis result this time\x01",
            "I would like to clean up in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBecause it was the damage of Gnostic\x01",
            "It is related to patients.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10105FI see.. So that's' it\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F……I understand,\x01",
            "I will be there first.\x02\x03",
            "#00000FCan you fill us in on the details of the case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, I'd like to ask you guys\x01",
            "It is \"collection of interview table\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… After the case faction of the example,\x01",
            "Hospitals are \"Gnostic\" victims\x01",
            "I focused on after-care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe treatment of most patients\x01",
            "It ended as usual … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe interview table written lastly,\x01",
            "Several patients have not submitted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FAnd the result is the brutal strength that we saw\x01",
            "Certainly also in the analysis results\x01",
            "It seems to be related.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYes. I'd like you to take care of this quickly\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Opinion chart is not coming back\x01",
            "There are three patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PFirst, Crossbell City,\x01",
            "A boy living in the old city, Dino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNext, the troupe of alkane shell\x01",
            "Artist, Nicole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd the Crossbell Guard\x01",
            "Cres who is a member of the Belgard gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTell the situation to the above patients,\x01",
            "I would like you to collect the interview table.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see. All people we know then\x02\x03",
            "#00303FThe Old Town and the two of Alcan Shell\x01",
            "If you search in town you will find it soon.\x02\x03",
            "#00302FCress senpai, perhaps at the cafeteria of the Belgard gate\x01",
            "I guess I'm eating a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah. Let's go right away then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWell then I'll leave it to you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhen collection is over, here again\x01",
            "Come for report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAt that time, on the analysis result of Gnostic\x01",
            "Let's say we will talk again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Request of a new professor】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x152, 2)
    OP_29(0x70, 0x1, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 107500, 0, 57000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_4_493 end

    def Function_5_1197(): pass

    label("Function_5_1197")


    def lambda_119C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_119C)

    def lambda_11AD():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11AD)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 105730, 0, 50340, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_5_1197 end

    def Function_6_11E2(): pass

    label("Function_6_11E2")


    def lambda_11E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11E7)

    def lambda_11F8():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11F8)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 104600, 0, 50890, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_6_11E2 end

    def Function_7_122D(): pass

    label("Function_7_122D")


    def lambda_1232():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1232)

    def lambda_1243():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1243)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 105690, 0, 48970, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_7_122D end

    def Function_8_1278(): pass

    label("Function_8_1278")


    def lambda_127D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_127D)

    def lambda_128E():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128E)
    WaitChrThread(0x109, 1)
    Sound(107, 0, 100, 0)
    OP_95(0x109, 104810, 0, 49520, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_8_1278 end

    def Function_9_12C9(): pass

    label("Function_9_12C9")


    def lambda_12CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12CE)

    def lambda_12DF():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12DF)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 103660, 0, 49780, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_9_12C9 end

    def Function_10_1314(): pass

    label("Function_10_1314")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(108640, 950, 57250, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 107920, 0, 57770, 90)
    SetChrPos(0x102, 107840, 0, 56600, 90)
    SetChrPos(0x109, 106120, 0, 57330, 90)
    SetChrPos(0x105, 106680, 0, 56190, 90)
    SetChrPos(0x104, 106710, 0, 58390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11PYou're back\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's about 5 minutes over the expected time, but …\x01",
            "Well it's a running point.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#6P#00306F(S-she's definitley scary)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWell, the recovery of the interview table\x01",
            "I'm done …… Here it is.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over all medical forms\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber('尼克鲁的问诊表', 1)
    SubItemNumber('迪诺的问诊表', 1)
    SubItemNumber('库雷斯队员的问诊表', 1)

    ChrTalk(
        0x8,
        "#11PHmm\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x102,
        (
            "#6P#00101FAA no……\x01",
            "Did you have any problems?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        "#11PNo, the opposite\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAs far as the questionnaire table was seen,\x01",
            "There seems to be no sequelae.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThat's it for now\x01",
            "All of Gnostic taking\x01",
            "The treatment is completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PNice work\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI-is that right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FEhe, that's great\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FAlthough it was rather troublesome\x01",
            "I am honored to serve you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSo fast, but Gnostic\x01",
            "Let's report the analysis results to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDo you have a minute?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#6P#00001FAh……\x01",
            "Yes, please!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(103000, 1050, 57370, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22900, 0)
    SetChrPos(0x8, 103000, 150, 58690, 180)
    SetChrPos(0x109, 102150, 150, 58690, 180)
    SetChrPos(0x102, 103850, 150, 58690, 180)
    SetChrPos(0x105, 102150, 150, 55850, 0)
    SetChrPos(0x101, 103000, 150, 55880, 0)
    SetChrPos(0x104, 103850, 150, 55890, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P── Gnostic\x01",
            "Results thoroughly analyzed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFirst of all, to Gnostic\x01",
            "Force \"Brain Limiter\"\x01",
            "It turned out that there was an effect to remove.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FBrain limiter …\x01",
            "I mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn the first place,\x01",
            "The physical ability which it has originally\x01",
            "It is said that half can not be used.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo reduce the load on the body,\x01",
            "To be able to draw out the brain\x01",
            "It restricts unconsciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis limiter\x01",
            "It can be released intentionally\x01",
            "If you can……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn theory, that individual has\x01",
            "Ability to the limit\x01",
            "It should be able to demonstrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FIn other words, what is Gnostic\x01",
            "It is not just a drug to strengthen muscular strength … …\x02\x03",
            "#10301FPotential that is not usually used\x01",
            "Is it a drug to be forcibly withdrawn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PBut it actually unlocks the physical and mental power a person is capable of\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POf course, unconsciously it took\x01",
            "If you remove the limiter,\x01",
            "The burden on the body is considerable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FIndeed, after a cult incident\x01",
            "The guards are\x01",
            "It seems that he was considerably exhausted.\x02\x03",
            "#00303FFor a while you can move a single finger\x01",
            "It seems that there was kitsui ……\x02\x03",
            "#00302FWell, exquisite rehabilitation training\x01",
            "Thanks for doing, finally\x01",
            "I can regain the can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10104FWell we were able to beat them back using all our strength\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FYeah… Barely\x02\x03",
            "#00101FDepending on the increased rugosity and cans\x01",
            "Win gamble winning streaks\x01",
            "There were people who did it.\x02\x03",
            "#00108FAt the same time, personality and behavior\x01",
            "It seemed to have changed suddenly … …\x02\x03",
            "#00101FEven those, Gnostic\x01",
            "Because I am removing the brain limiter,\x01",
            "Can you explain it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PSo then you can explain exactly how Gnosis removed that limiter\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFor this medicine the work of the five senses\x01",
            "The dramatically enhancing action\x01",
            "It is confirmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt becomes nervous as a side effect,\x01",
            "Emotional instability\x01",
            "I also know that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt changes to a ferocious personality\x01",
            "It will be connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FAnd the result is the brutal strength that we saw\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FSurely one by one\x01",
            "There seems to be an explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P── However, biochemically to the last\x01",
            "That's all I can explain.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHowever, that's as far as we can explain medically and scientifically\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFor some indications\x01",
            "It can only be called non-scientific.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSpecifically, as I mentioned earlier\x01",
            "Efficacy of invoking tsuki ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd you guys witnessed it a couple of times\x01",
            "Demonicization#6RDemonize#\"It is a physical variation phenomenon called.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FR-right…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FI forgot about that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F…… It causes the demonicization\x01",
            "Red type gnostic ……\x02\x03",
            "#00001FWhat is still blue type\x01",
            "Was it a different ingredient?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWell about that\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PActually, the glue type of the blue type also\x01",
            "Red type gnostic as well\x01",
            "There is no change in terms of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAt least as far as science can determine\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FI-is that right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, the difference in that color\x01",
            "It is due to differences in processing during refining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere is no difference in the main ingredient,\x01",
            "Molecular structure is almost the same …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNevertheless, the red type is\x01",
            "An unexplainable explanation such as physical variation\x01",
            "It is causing phenomena …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P─ ─ honestly, being a demonicization\x01",
            "\"Hallucinence\" you saw much of fear\x01",
            "I think the best thing is to think.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#00306FNo well that is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10108FErnest secretary's demonicization\x01",
            "I have also witnessed … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI know it.\x01",
            "─ ─ So that's the limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe identity of a drug called Gnostic\x01",
            "Only from the field of biochemistry\x01",
            "It is not an approach to unravel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAs a carrier of state-of-the-art modern medicine\x01",
            "It is quite a trivial opinion, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PModern medicine is not a panacea.\x01",
            "About this matter of mind and soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd Gnostic probably,\x01",
            "To resonate with them and the body\x01",
            "I guess they have some kind of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PPerhaps Joachim also has a whole picture of Gnostic\x01",
            "There was no difference that I had not grasped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBased on the mysteries that were transferred to the cult\x01",
            "Completing it while trial and error,\x01",
            "It should have been successful in mass production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FCertainly, such a thing\x01",
            "It seems like the person himself admitted … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FOh, the ritual done in various places\x01",
            "Based on data, while trial and error\x01",
            "She said that it was completed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmm. Like I thought\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe was capable and enthusiastic\x01",
            "I could not get enough of genius\x01",
            "He was not the owner of the idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAnd maybe that's what drew him to the bad side\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FCould it be..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FThat Joachim and personal\x01",
            "Are you acquainted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, you are a remiferia\x01",
            "It is my friend who was studying at a medical university.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI did not see him since I graduated\x01",
            "About occasional latest research results etc.\x01",
            "I was exchanging with a letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, in this way\x01",
            "Abusing the skill of the doctor, to yourself\x01",
            "It is said that it will destroy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00108FProfessor…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10103FI'm so sorry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNo, that was a personal issue\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P─ ─ Anyway,\x01",
            "That's all I can report from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn order to approach the truth of Gnostic\x01",
            "We will need another approach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThis is just my intiution but\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt is said to be the raw material of Gnostic\x01",
            "The character of \"Plumroma grass\" plant\x01",
            "I think that it will be the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FThe Pleroma Flower…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FTo the cult's database\x01",
            "It is the name that was written …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FBut in the end what kind of plant\x01",
            "Where did you get it from?\x01",
            "I do not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, I also got to know each other.\x01",
            "I attempted botanists and others\x01",
            "The applicable item could not be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhether it was a new species that was transmitted only to the cult,\x01",
            "Or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn any case, considering the efficacy of medicine,\x01",
            "The plant also has the property \"impossible\"\x01",
            "It can be inferred that it is possessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00101FImpossible composition…\"\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHuh, somehow in occultism\x01",
            "It has become interesting, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F── Professor Seyland.\x01",
            "Thank you very much.\x02\x03",
            "#00000FThanks to what I had vaguely until now\x01",
            "I feel I was able to sort out to some extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWell that's good then\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRegarding the ingredient investigation of Gnostic\x01",
            "I will cancel once here … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlso, if you know something\x01",
            "Do not hesitate to call on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo the end from the standpoint of a doctor\x01",
            "Let me say your opinion.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1314 end

    def Function_11_2F8B(): pass

    label("Function_11_2F8B")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Exit from research building】\x01",      # 0
            "【quit】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FF0"),
        (1, "loc_3009"),
        (SWITCH_DEFAULT, "loc_3021"),
    )


    label("loc_2FF0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_3021")

    label("loc_3009")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_3021")

    label("loc_3021")

    Return()

    # Function_11_2F8B end

    SaveToFile()

Try(main)
