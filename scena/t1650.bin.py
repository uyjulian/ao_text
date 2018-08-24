from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Professor Seiland",      # 1
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
        "Function_4_4C7",          # 04, 4
        "Function_5_11E5",         # 05, 5
        "Function_6_1230",         # 06, 6
        "Function_7_127B",         # 07, 7
        "Function_8_12C6",         # 08, 8
        "Function_9_1317",         # 09, 9
        "Function_10_1362",        # 0A, 10
        "Function_11_3207",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0")

    ChrTalk(
        0x8,
        (
            "Nearly all drug patients have completed\x01",
            "treatment, but some haven't submitted\x01",
            "their medical questionnaires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Firstly, Dino, a young\x01",
            "boy who lives in\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next is Nikol, Arc-en-\x01",
            "Ciel artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Finally, CGF member\x01",
            "Cless, stationed at\x01",
            "Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want you to explain the\x01",
            "situation and collect their\x01",
            "questionnaires for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once you have them all,\x01",
            "return here and report. I'm\x01",
            "counting on all of you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C3")

    label("loc_3C0")


    ChrTalk(
        0x8,
        (
            "Dino, a boy who lives in\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nikol, Arc-en-Ciel\x01",
            "artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Finally, CGF member\x01",
            "Cless, stationed at\x01",
            "Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want you to explain the\x01",
            "situation and collect their\x01",
            "questionnaires for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, I'm counting\x01",
            "on all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C3")

    TalkEnd(0x8)
    Return()

    # Function_3_1CE end

    def Function_4_4C7(): pass

    label("Function_4_4C7")

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
            "#6P#00000F─Excuse us, we're the\x01",
            "Special Support\x01",
            "Section....\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman's Voice",
        "Please come in.\x02",
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
        "Woman Doctor",
        "You're finally here.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman Doctor",
        (
            "You're about 2 minutes later\x01",
            "than I expected, but... Well,\x01",
            "they say you're good, so, fine.\x02",
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
            "#12P#00306F(She seems scary\x01",
            "somehow... though she's\x01",
            "certainly beautiful.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman Doctor",
        (
            "Come here at once. It's\x01",
            "hard to talk from this\x01",
            "distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FR-Right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_68(108640, 950, 57250, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20000, 5000)

    def lambda_91D():
        OP_95(0xFE, 107920, 0, 57770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91D)
    Sleep(500)

    def lambda_93A():
        OP_95(0xFE, 107840, 0, 56600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93A)
    Sleep(500)

    def lambda_957():
        OP_95(0xFE, 106710, 0, 58390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_957)
    Sleep(700)

    def lambda_974():
        OP_95(0xFE, 106120, 0, 57330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_974)
    Sleep(500)

    def lambda_991():
        OP_95(0xFE, 106680, 0, 56190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_991)
    WaitChrThread(0x101, 1)

    def lambda_9AF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AF)
    WaitChrThread(0x102, 1)

    def lambda_9C0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C0)
    WaitChrThread(0x109, 1)

    def lambda_9D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9D1)
    WaitChrThread(0x104, 1)

    def lambda_9E2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E2)
    WaitChrThread(0x105, 1)

    def lambda_9F3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9F3)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#00100FUmm, Professor Seiland, I\x01",
            "presume?\x02\x03",
            "#00103FI heard the Gnosis\x01",
            "component analysis\x01",
            "results were published...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P─Sorry, I've have a\x01",
            "favor to ask beforehand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'd like all of you to\x01",
            "take care of that first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThe request you\x01",
            "submitted right?\x02\x03",
            "#10301FYou can't give us the\x01",
            "Gnosis analysis results\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe request concerns the\x01",
            "analysis results, so I'd like\x01",
            "you to take care of it first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBecause it concerns the\x01",
            "patients who were harmed\x01",
            "by Gnosis.\x02",
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
        "#6P#10105FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...Understood. We'll do\x01",
            "that first.\x02\x03",
            "#00000FCan you tell us the\x01",
            "details of your request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes. I'd like you all to\x01",
            ""collect medical\x01",
            "questionnaires".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...After the cult incident,\x01",
            "the hospital focused on caring\x01",
            "for the "Gnosis" victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNearly all patients have\x01",
            "completed treatment,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIn the end, several patients\x01",
            "haven't submitted the medical\x01",
            "questionnaire I asked them to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI see... That certainly\x01",
            "would affect the\x01",
            "analysis results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes. I'd like you to\x01",
            "take care of this\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...I'm missing the\x01",
            "questionnaires from 3\x01",
            "patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDino, of Crossbell\x01",
            "City's Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNikol, Arc-en-Ciel\x01",
            "artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PCless, stationed at\x01",
            "Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PExplain the situation to\x01",
            "each patient and collect\x01",
            "their questionnaires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see. We know all of them\x01",
            "personally.\x02\x03",
            "#00303FWe'll probably find Dino\x01",
            "and Nikol in the city if\x01",
            "we look around.\x02\x03",
            "#00302FCless is probably having a\x01",
            "meal in the Bellguard Gate\x01",
            "mess hall around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FAlright, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POnce you've collected\x01",
            "them, return here and\x01",
            "report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll give you the Gnosis\x01",
            "analysis results then.\x02",
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
            "Quest [New Professor's\x01",
            "Request]\x07\x00",
            " started!\x02",
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

    # Function_4_4C7 end

    def Function_5_11E5(): pass

    label("Function_5_11E5")


    def lambda_11EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11EA)

    def lambda_11FB():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11FB)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 105730, 0, 50340, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_5_11E5 end

    def Function_6_1230(): pass

    label("Function_6_1230")


    def lambda_1235():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1235)

    def lambda_1246():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1246)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 104600, 0, 50890, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_6_1230 end

    def Function_7_127B(): pass

    label("Function_7_127B")


    def lambda_1280():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1280)

    def lambda_1291():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1291)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 105690, 0, 48970, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_7_127B end

    def Function_8_12C6(): pass

    label("Function_8_12C6")


    def lambda_12CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12CB)

    def lambda_12DC():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_12DC)
    WaitChrThread(0x109, 1)
    Sound(107, 0, 100, 0)
    OP_95(0x109, 104810, 0, 49520, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_8_12C6 end

    def Function_9_1317(): pass

    label("Function_9_1317")


    def lambda_131C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_131C)

    def lambda_132D():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_132D)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 103660, 0, 49780, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_9_1317 end

    def Function_10_1362(): pass

    label("Function_10_1362")

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
        "#11P...So you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou're five minutes later\x01",
            "than expected, but...\x01",
            "Well, it's passable.\x02",
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
        "#6P#00306F(S-She IS scary...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FUmm, we've collected the\x01",
            "forms. Here you go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd handed the medical\x01",
            "questionnaires to\x01",
            "Professor Seiland.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32D, 1)
    SubItemNumber(0x32E, 1)
    SubItemNumber(0x32F, 1)

    ChrTalk(
        0x8,
        "#11P...Hmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x102,
        (
            "#6P#00101FE-Excuse me... Is there\x01",
            "a problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11P...No, it's the\x01",
            "opposite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBased on the questionnaires,\x01",
            "all patients are free of the\x01",
            "drug's effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThis means the treatment\x01",
            "of the patients who took\x01",
            "Gnosis is now complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PNice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FHaha, that's great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIt was a lot of running\x01",
            "around, but It's an honor\x01",
            "to have been of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, I'll inform you of\x01",
            "the Gnosis analysis\x01",
            "results immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDo you have a moment?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        "#6P#00001FY-Yes, please do!\x02",
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
            "#5P─Regarding the results\x01",
            "of the Gnosis\x01",
            "analysis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFirstly, I figured that Gnosis\x01",
            "has the effect of forcefully\x01",
            "releasing the "brain limiters".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FBrain limiters...you\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo begin with, humans are thought to\x01",
            "normally use not even half of the\x01",
            "physical abilities they possess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo decrease stress on the\x01",
            "body, unconsciously, the brain\x01",
            "places limiters on abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it were possible to\x01",
            "intentionally release\x01",
            "these limiters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn theory, the individual\x01",
            "would be able to perform up to\x01",
            "the limits of their abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FIn other words, Gnosis is not a\x01",
            "drug that simply enhances\x01",
            "strength...\x02\x03",
            "#10301FSo you're saying it's a drug that\x01",
            "forcibly draws out a person's\x01",
            "normally unused latent abilities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNaturally, if the limiters are\x01",
            "removed, is places considerable\x01",
            "stress on the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FIndeed. After the cult incident, the\x01",
            "Guardian Force troops were rather\x01",
            "exhausted.\x02\x03",
            "#00303FFor a little while, they couldn't even\x01",
            "lift a single finger.\x02\x03",
            "#00302FWell, thanks to the strict\x01",
            "rehabilitation training they did, they\x01",
            "finally came back to their senses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10104FYes... It seems so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FSpeaking of senses...\x02\x03",
            "#00101FThere was a man with a string\x01",
            "of gambling wins who relied on\x01",
            "heightened luck and senses.\x02\x03",
            "#00108FAt the same time, his\x01",
            "personality and conduct\x01",
            "suddenly changed, too.\x02\x03",
            "#00101FCould those changes be\x01",
            "explained by the effect of\x01",
            "Gnosis on brain limiters?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmm, it could be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe drug is confirmed to\x01",
            "rapidly increase the user's\x01",
            "five senses, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe also know that side effects\x01",
            "of the drug include nervousness\x01",
            "and emotional instability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThose are likely the cause of\x01",
            "the aggressive personality\x01",
            "the man developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10100FThat does seem to\x01",
            "explain everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P─However, that is the full\x01",
            "extent of what can be\x01",
            "explained biochemically.\x02",
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
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRegarding several\x01",
            "effects, I can only say\x01",
            "they're unscientific.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSpecifically, the case where\x01",
            "the user's luck increased,\x01",
            "that you just mentioned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd also the "Demonization"\x01",
            "metamorphosis phenomenon that you\x01",
            "have witnessed several times already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00303FThat too, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F...The cause of\x01",
            "Demonization is the red-\x01",
            "type Gnosis...\x02\x03",
            "#00001FIt has different\x01",
            "components than the blue\x01",
            "type, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAbout that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PActually, the blue and red\x01",
            "Gnosis are no different in\x01",
            "terms of ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn terms of chemistry,\x01",
            "at least.\x02",
        )
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
        "#12P#00005FR-Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes. The color difference\x01",
            "is due to a difference in\x01",
            "the degree of refinement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere is no difference in the main\x01",
            "ingredients, and the molecular\x01",
            "structure is an almost exact match...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut regardless of that, the red type\x01",
            "causes a metamorphosis phenomenon\x01",
            "that defies explanation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...Honestly, the most likely explanation\x01",
            "of Demonization I can think of is an\x01",
            ""illusion" you all saw due to great fear.\x02",
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
        (
            "#12P#00306FNo, that's totally not\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10108FI witnessed Secretary\x01",
            "Ernest's Demonization\x01",
            "myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI know. ...That's why\x01",
            "this is the limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PUsing an approach to\x01",
            "explain Gnosis using\x01",
            "only biochemistry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FYou have a pretty high\x01",
            "opinion of modern\x01",
            "medicine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PModern medicine is not all-\x01",
            "powerful. Especially regarding\x01",
            "problems of the mind and soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd it's likely that Gnosis\x01",
            "has some hidden effect on the\x01",
            "body with regard to those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI have no doubt that\x01",
            "even Joachim didn't know\x01",
            "the full story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PUsing the cult's secret rituals as a base,\x01",
            "he only perfected the drug using trial and\x01",
            "error, and succeeded in mass producing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FI think he himself\x01",
            "confirmed that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah. He said that, using each lodge's\x01",
            "ritual data as a base, he perfected\x01",
            "the drug through trial and error.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmm. As I thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe was skilled and\x01",
            "enthusiastic, but didn't\x01",
            "have the mind of a genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMaybe that's what drew\x01",
            "him to the dark side.\x02",
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
        "#12P#00005FCould it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FDid you know Joachim\x01",
            "personally?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, he was my colleague\x01",
            "when I was studying at\x01",
            "Remiferia Medical School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI never saw him after we graduated,\x01",
            "but we exchanged letters occasionally\x01",
            "about our latest research results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut I never thought he'd abuse\x01",
            "medical technology like that and\x01",
            "even destroy his own body...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00108FProfessor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10103F...My sympathies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, don't worry about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P─In any case, that's all\x01",
            "I can report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo find the truth about\x01",
            "Gnosis, a different\x01",
            "approach is needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThis is entirely my\x01",
            "intuition, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI think the characteristics of\x01",
            "Pleroma Grass, an ingredient\x01",
            "of Gnosis, could be the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001FThe Pleroma Grass...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FThat name was recorded\x01",
            "in the cult's\x01",
            "database...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FBut in the end, we never learned\x01",
            "what kind of plant it is or\x01",
            "where it was obtained, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes. I asked my colleagues too,\x01",
            "including a botanist, but I\x01",
            "didn't find any relevant answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PCould it be a species\x01",
            "only the cult has access\x01",
            "to? Or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn any case, thinking about the\x01",
            "drug's effects, I guess that that\x01",
            "plant has "impossible" properties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FImpossible\x01",
            "properties...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHaha. This is getting\x01",
            "interesting now that\x01",
            "it's somehow occult.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F...Thank you very much, Professor\x01",
            "Seiland.\x02\x03",
            "#00000FThanks to you, I feel we understand\x01",
            "past events that were unclear up\x01",
            "until now, to a certain degree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIs that so? Well good\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll temporarily suspend\x01",
            "the Gnosis component\x01",
            "analysis, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you learn anything\x01",
            "else, please feel free\x01",
            "to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll at least be able to\x01",
            "give you a doctor's\x01",
            "opinion on the matter.\x02",
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

    # Function_10_1362 end

    def Function_11_3207(): pass

    label("Function_11_3207")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exit the Research Building]\x01",      # 0
            "[Cancel]\x01",                          # 1
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
        (0, "loc_3274"),
        (1, "loc_328D"),
        (SWITCH_DEFAULT, "loc_32A5"),
    )


    label("loc_3274")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_32A5")

    label("loc_328D")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_32A5")

    label("loc_32A5")

    Return()

    # Function_11_3207 end

    SaveToFile()

Try(main)
