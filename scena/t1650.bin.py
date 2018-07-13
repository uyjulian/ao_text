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
        "Function_4_591",          # 04, 4
        "Function_5_1429",         # 05, 5
        "Function_6_1474",         # 06, 6
        "Function_7_14BF",         # 07, 7
        "Function_8_150A",         # 08, 8
        "Function_9_155B",         # 09, 9
        "Function_10_15A6",        # 0A, 10
        "Function_11_3632",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446")

    ChrTalk(
        0x8,
        (
            "About the patients of that drug, the treatment\x01",
            "is almost over, but there're persons of whom\x01",
            "I don't have a medical questionnaire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "First of all, in Crossbell City, there's a\x01",
            "young boy called Dino who lives in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Next, we have an artist called Nikol,\x01",
            "a member of the Arc-en-ciel troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, a soldier named Cless in service\x01",
            "in the Crossbell CGF at Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want you to tell them the situation\x01",
            "and get their medical questionnaires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When you have gathered them all,\x01",
            "come back here again to report.\x01",
            "So, I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_58D")

    label("loc_446")


    ChrTalk(
        0x8,
        (
            "Crossbell City, a young boy\x01",
            "called Dino who lives in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nikol, an artist, member\x01",
            "of the Arc-en-ciel troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, a soldier named Cless in service\x01",
            "in the Crossbell CGF at Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want you to tell them the situation\x01",
            "and get their medical questionnaires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well then, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    label("loc_58D")

    TalkEnd(0x8)
    Return()

    # Function_3_1CE end

    def Function_4_591(): pass

    label("Function_4_591")

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
            "#6P#00000F──Excuse us, we're coming in.\x01",
            "We're from the Special Support Section....\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman's Voice",
        "Come in.\x02",
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
        "Hm, finally here I see.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman Doctor",
        (
            "You're about 2 minutes later than\x01",
            "the time I was expecting, but...\x01",
            "Well, they say you're good, so, fine.\x02",
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
            "#12P#00306F(S-Somehow she seems weird...\x01",
            "Although no doubt she's a beauty.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman Doctor",
        (
            "Well, in any case, come here.\x01",
            "At this distance it's hard to talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FY-You're right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_68(108640, 950, 57250, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20000, 5000)

    def lambda_A1B():
        OP_95(0xFE, 107920, 0, 57770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1B)
    Sleep(500)

    def lambda_A38():
        OP_95(0xFE, 107840, 0, 56600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A38)
    Sleep(500)

    def lambda_A55():
        OP_95(0xFE, 106710, 0, 58390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A55)
    Sleep(700)

    def lambda_A72():
        OP_95(0xFE, 106120, 0, 57330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A72)
    Sleep(500)

    def lambda_A8F():
        OP_95(0xFE, 106680, 0, 56190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A8F)
    WaitChrThread(0x101, 1)

    def lambda_AAD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAD)
    WaitChrThread(0x102, 1)

    def lambda_ABE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABE)
    WaitChrThread(0x109, 1)

    def lambda_ACF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ACF)
    WaitChrThread(0x104, 1)

    def lambda_AE0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AE0)
    WaitChrThread(0x105, 1)

    def lambda_AF1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#00100FEhm, you're Professor\x01",
            "Seiland, am I right?\x02\x03",
            "#00103FAbout the analysis results \x01",
            "of the Gnosis' ingredients──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P──Sorry but before that,\x01",
            "I've got a favor to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'd like you to be done\x01",
            "with that first of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThe matter you issued a request for, right?\x02\x03",
            "#10301FI guess you can't\x01",
            "give us the Gnosis\x01",
            "analysis results?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBecause it regards the analysis result,\x01",
            "I want you to take care of that first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBecause it's related to the patients\x01",
            "who suffered damage from Gnosis.\x02",
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
        "#6P#10105FI see, so that's what it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...Understood.\x01",
            "We'll do that first.\x02\x03",
            "#00000FCould we know the request contents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHm, what I want to ask you is to\x01",
            ""collect medical questionnaires".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...After that Cult incident, the hospital\x01",
            "concentrated its effort on the after care\x01",
            "of the "Gnosis" victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe treatment of almost all\x01",
            "patients has been completed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIn the end, some patients didn't submit the\x01",
            "medical questionnaire I asked to fill in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI see...\x01",
            "It really seems that it also\x01",
            "involves the analysis results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHm, I want you to do it fast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...There're three persons who haven't \x01",
            "returned their medical questionnaire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PFirst, in Crossbell City, a young boy\x01",
            "called Dino who lives in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNext, Nikol, an artist, member\x01",
            "of the Arc-en-ciel troupe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, a soldier in service in the Crossbell\x01",
            "CGF at Bellguard Gate, Cless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI want you to explain the situation to the aforementioned\x01",
            "patients and collect their medical questionnaires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see, they seem all known names.\x02\x03",
            "#00303FFor the guys at Downtown and the\x01",
            "Arc-en-ciel, if we look for them\x01",
            "in the city, we'll find 'em out.\x02\x03",
            "#00302FAs for senior Cless, he'll be probably\x01",
            "havin' a meal at the Bellguard Gate mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, let's go at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PThen, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhen you've finished collecting them,\x01",
            "return here and report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhen you do that, I'll officially talk\x01",
            "about the Gnosis analysis results.\x02",
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
            "Quest [New Professor's Request]\x07\x00",
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

    # Function_4_591 end

    def Function_5_1429(): pass

    label("Function_5_1429")


    def lambda_142E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_142E)

    def lambda_143F():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_143F)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 105730, 0, 50340, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_5_1429 end

    def Function_6_1474(): pass

    label("Function_6_1474")


    def lambda_1479():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1479)

    def lambda_148A():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_148A)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 104600, 0, 50890, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_6_1474 end

    def Function_7_14BF(): pass

    label("Function_7_14BF")


    def lambda_14C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14C4)

    def lambda_14D5():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14D5)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 105690, 0, 48970, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_7_14BF end

    def Function_8_150A(): pass

    label("Function_8_150A")


    def lambda_150F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_150F)

    def lambda_1520():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1520)
    WaitChrThread(0x109, 1)
    Sound(107, 0, 100, 0)
    OP_95(0x109, 104810, 0, 49520, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_8_150A end

    def Function_9_155B(): pass

    label("Function_9_155B")


    def lambda_1560():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1560)

    def lambda_1571():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1571)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 103660, 0, 49780, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_9_155B end

    def Function_10_15A6(): pass

    label("Function_10_15A6")

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
            "#11PYou're five minutes later than what I thought, but...\x01",
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
        "#6P#00306F(S-She IS weird...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FUhhm, we've finished collecting the\x01",
            "medical questionnaires...here they're.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed over the medical questionnaires to Professor Seiland.\x07\x00\x02",
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
        "#11P...Hm.........\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x102,
        (
            "#6P#00101FE-Excuse me...\x01",
            "Is there any problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        "#11P...No, it's the opposite.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAccording to what I'm seeing,\x01",
            "it seems there're no after-effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWith this, for the time being,\x01",
            "the treatment of all the Gnosis\x01",
            "recipients is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGood job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FI-I see...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FUh uh, thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIt took us quite some time to do,\x01",
            "but it's an honor to have been of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThen, I know it's sudden, but I'll report\x01",
            "to you the Gnosis analysis results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PCan you make me company for a bit?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#6P#00001FAh...\x01",
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
            "#5P──The results of a Gnosis\x01",
            "thorough analysis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFirst and foremost, I figured that\x01",
            "Gnosis has the effect of forcefully\x01",
            "release the "brain limiters".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FBrain limiters...\x01",
            "What does it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo begin with, man is regarded as\x01",
            "not being able to use even half of the \x01",
            "physical abilities it naturally has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo decrease the burden on the body,\x01",
            "the brain put unconscious limiters\x01",
            "to the abilities it can draw out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it was possible to\x01",
            "intentionally release\x01",
            "these limiters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn theory, it could become possible\x01",
            "to display abilities up to the limit\x01",
            "a single person possesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FIn other words, Gnosis is not a drug to\x01",
            "solely enhance physical strength, but...\x02\x03",
            "#10301FA drug that forcibly draws out the latent\x01",
            "faculties that aren't normally used?\x02",
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
            "#5PNaturally, if the limiters that were\x01",
            "unconsciously active are released,\x01",
            "the strain on the body is extreme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FIndeed, after the Cult incident\x01",
            "the CGF guys seemed to be\x01",
            "pretty exhausted.\x02\x03",
            "#00303FIt seems they were in such a bad state\x01",
            "that they couldn't even lift a finger...\x02\x03",
            "#00302FWell, thanks to the strict rehabilitation\x01",
            "practice that they did, it seems they were\x01",
            "finally able to get back their senses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10104FYes...it seems so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103F...Speaking of...senses.\x02\x03",
            "#00101FThere was also a man who\x01",
            "kept winning at gambling relying\x01",
            "on heightened luck and senses.\x02\x03",
            "#00108FAt the same time, it seems that personality,\x01",
            "speech and conduct had a complete change....\x02\x03",
            "#00101FCould those too be explained\x01",
            "because Gnosis released the\x01",
            "brain limiters, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHm, that could be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAfter all, it's also confirmed for this\x01",
            "drug the effect of rapidly increasing\x01",
            "the five senses functions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI also figured that as side\x01",
            "effects there're nervousness\x01",
            "and an emotional instability state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThose are probably related with\x01",
            "the change to a brutal personality.\x02",
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
            "#5P#10100FIndeed, the explanation\x01",
            "is adequate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P──Still, this is the extent of what\x01",
            "can be explained biochemically.\x02",
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
        "#12P#00005FWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRegarding some effects, I can\x01",
            "only say they're unscientific.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PConcretely, the effect to call in luck\x01",
            "that you spoke about moments ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd what you have witnessed many times too.\x01",
            "The metamorphose phenomenon called "demonize".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105F...T-True...\x02",
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
            "#12P#00003F...What causes "demonize"\x01",
            "is the red type of Gnosis...\x02\x03",
            "#00001FAs expected, it's made with different\x01",
            "ingredients than the blue type one?\x02",
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
            "#5PActually, the blue type of Gnosis\x01",
            "and the red type of Gnosis are\x01",
            "no different, ingredients wise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PBiochemically, at least.\x02",
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
            "#5PYeah, the color difference is\x01",
            "given by the refining process.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere's no difference in the main ingredients\x01",
            "and even the molecular structure almost fits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDespite that, the red type\x01",
            "causes a phenomenon impossible\x01",
            "to explain like a metamorphosis...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P──Frankly, what I could think that "demonize"\x01",
            "matches best is an "hallucination" that you all\x01",
            "had due to too much terror.\x02",
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
        "#12P#00306FNo, that's not totally it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10108FI have witnessed Secretary\x01",
            "Ernest's demonize myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI know.\x01",
            "──That's why this is a limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe approach to only explain from\x01",
            "the sphere of biochemistry the true\x01",
            "nature of the drug called Gnosis.\x02",
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
            "#12P#10302FQuite a commendable view for someone in\x01",
            "charge of cutting-edge medical care, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PModern medical care is not almighty, you know.\x01",
            "Regarding mind and soul problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd Gnosis probably hides some\x01",
            "functions to make resonate the\x01",
            "body with those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'm sure that not even Joachim had\x01",
            "grasped the full details of Gnosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe made it perfect by trial and error with\x01",
            "the secret rituals transmitted by the Cult \x01",
            "and only succeeded in its mass production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101FI'm sure that he himself\x01",
            "confirmed that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah, he said he completed it by trial\x01",
            "and error on the basis of the data of \x01",
            "the rituals performed throughout the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHm, as expected then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat guy had skills and was zealous,\x01",
            "but he didn't have the outstanding\x01",
            "mindset of a genius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAnd in the end he went wrong...\x02",
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
            "#12P#00305FDid you personally\x01",
            "know that Joachim?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, he was my colleague when I was studying\x01",
            "at the medical college in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI didn't meet him after graduation,\x01",
            "but now and then we exchanged letters\x01",
            "about the latest research results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, I'd never thought he would've\x01",
            "misused medical techniques in such a way\x01",
            "and that he even destroyed his own body...\x02",
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
        "#5P#10103F...You have my sympathies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNo, I said something trifling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P──In any case, this\x01",
            "is all I can report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PTo face the truth about Gnosis,\x01",
            "a different approach is needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThis is just my intuition, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI think that the characteristics of the\x01",
            ""Pleroma Grass" plant, the base ingredient\x01",
            "for the Gnosis, is going to be the key to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F"Pleroma Grass"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FThat's a name that was recorded\x01",
            "in the Cult's database...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FHowever, in the end we didn't\x01",
            "get what kind of plant it is\x01",
            "and where we can get it, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, I tried to inquire a\x01",
            "botanist I know, but he didn't\x01",
            "find anything corresponding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt could be a new species only\x01",
            "transmitted in the Cult or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn any event, thinking about the drug\x01",
            "effects, I can suppose that that plant\x01",
            "has got "unbelievable" properties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00101F"Unbelievable properties"...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHu hu, since it's somehow occult,\x01",
            "it's become interesting, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F──Professor Seiland,\x01",
            "thank you very much.\x02\x03",
            "#00000FThanks to you, I feel that we've been\x01",
            "able to sort out to a certain degree\x01",
            "some things that were vague until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIs that so? I'm glad for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll temporarily interrupt the Gnosis\x01",
            "ingredients investigation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf you figure out something again,\x01",
            "don't hesitate to come visit me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAfter all I'll at least give you an opinion,\x01",
            "if you're fine for it to be from a doctor's perspective.\x02",
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

    # Function_10_15A6 end

    def Function_11_3632(): pass

    label("Function_11_3632")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exit the Research Laboratory Building]\x01",      # 0
            "[Quit]\x01",                                       # 1
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
        (0, "loc_36A8"),
        (1, "loc_36C1"),
        (SWITCH_DEFAULT, "loc_36D9"),
    )


    label("loc_36A8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_36D9")

    label("loc_36C1")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_36D9")

    label("loc_36D9")

    Return()

    # Function_11_3632 end

    SaveToFile()

Try(main)
