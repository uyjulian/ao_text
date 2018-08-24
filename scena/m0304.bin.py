from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0304.bin",                # FileName
        "m0304",                    # MapName
        "m0304",                    # Location
        0x0000,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0304",                  # 0
        "Reins",                  # 1
        "SE制御",                 # 2
    ))

    AddCharChip((
        "chr/ch28100.itc",                   # 00
    ))

    DeclNpc(0,       0,       1629,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(232, 0)                                        # 0

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1A8",          # 02, 2
        "Function_3_1A9",          # 03, 3
        "Function_4_260",          # 04, 4
        "Function_5_210B",         # 05, 5
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_120"),
        (1, "loc_12C"),
        (2, "loc_138"),
        (3, "loc_144"),
        (4, "loc_150"),
        (5, "loc_15C"),
        (6, "loc_168"),
        (SWITCH_DEFAULT, "loc_174"),
    )


    label("loc_120")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_12C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_138")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_144")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_150")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_15C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_168")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_174")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_180")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_197")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_180")

    label("loc_197")

    Return()

    # Function_0_E8 end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_1A7")

    Return()

    # Function_1_198 end

    def Function_2_1A8(): pass

    label("Function_2_1A8")

    Return()

    # Function_2_1A8 end

    def Function_3_1A9(): pass

    label("Function_3_1A9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I think I'll have the chance to\x01",
            "meet with all of you again one\x01",
            "day as a member of R&A Research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well first of all, I'll be\x01",
            "praying for the success of\x01",
            "your operation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_1A9 end

    def Function_4_260(): pass

    label("Function_4_260")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x9, 1, 0, 5)
    OP_68(1090, 0, -8490, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 0, 0, -10650, 0)
    SetChrPos(0x102, 1100, 0, -10650, 0)
    SetChrPos(0x103, -1100, 0, -10650, 0)
    SetChrPos(0x104, 0, 0, -10650, 0)
    SetChrPos(0xF4, -1100, 0, -10650, 0)
    SetChrPos(0xF5, 1100, 0, -10650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)

    AnonymousTalk(
        0x101,
        (
            "#00001FSo it really did connect\x01",
            "to the Geofront...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00103FThis is no doubt a\x01",
            "portion of the\x01",
            "D-Division...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00205FThe presence has gotten\x01",
            "stronger.\x02\x03",
            "#00203FThere's just one,\x01",
            "however. There's\x01",
            "definitely someone here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A")

    AnonymousTalk(
        0x10A,
        "#00601F(Beyond this door...?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_505")

    label("loc_48A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CC")

    AnonymousTalk(
        0x109,
        (
            "#10101F(Further beyond this\x01",
            "door...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_505")

    label("loc_4CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_505")

    AnonymousTalk(
        0x106,
        (
            "#10701F(Beyond this\x01",
            "door.......)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_505")


    AnonymousTalk(
        0x103,
        (
            "#00201F(Yes, no doubt about\x01",
            "it.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B1")

    AnonymousTalk(
        0x105,
        (
            "#10400F(Is this place a warehouse or\x01",
            "something? Although it looks like\x01",
            "there's a window on the door.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6A1")

    label("loc_5B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_631")

    AnonymousTalk(
        0x106,
        (
            "#10705F(Could this place be a warehouse\x01",
            "or something? It looks like\x01",
            "there's a window on the door.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6A1")

    label("loc_631")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A1")

    AnonymousTalk(
        0x109,
        (
            "#10105F(Is this place a warehouse or\x01",
            "something? It seems there's a\x01",
            "window on the door.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6A1")


    AnonymousTalk(
        0x101,
        (
            "#00003F(I don't know, but...\x01",
            "Anyhow, that's\x01",
            "convenient.)\x02\x03",
            "#00000F(Let's observing the\x01",
            "situation inside from\x01",
            "here for a while.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x9, 0x1)
    OP_68(950, 0, 3180, 0)
    MoveCamera(42, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16090, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(10)
    PlayBGM("ed7302", 0)

    NpcTalk(
        0x8,
        "???",
        (
            "That's right, Colonel...\x01",
            "Yes, yes...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "???",
        (
            "Huh, did I say that?\x01",
            "Ahaha... I'm sorry,\x01",
            "Director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#N(That figure from\x01",
            "behind...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#N(Could he be... Reins\x01",
            "from Crossbell Times?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00205F#N(I wonder what he's\x01",
            "doing in a place like\x01",
            "this...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PUhhm... Are you the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWould you like to come\x01",
            "in for a small talk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#NOh man... He already\x01",
            "noticed us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#NWe can't let our guard\x01",
            "down, but for now, let's\x01",
            "do as he says.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(980, 900, -2510, 4500)
    MoveCamera(39, 16, 0, 4500)
    OP_6E(600, 4500)
    SetCameraDistance(18630, 4500)
    Sleep(2000)

    def lambda_9C5():
        OP_97(0xFE, 0x0, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C5)

    def lambda_9DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9DF)
    Sleep(100)

    def lambda_9F3():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F3)

    def lambda_A0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A0D)
    Sleep(100)

    def lambda_A21():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A21)

    def lambda_A3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A3B)
    Sleep(500)

    def lambda_A4F():
        OP_97(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4F)

    def lambda_A69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A69)
    Sleep(100)

    def lambda_A7D():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A7D)

    def lambda_A97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_A97)
    Sleep(100)

    def lambda_AAB():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_AAB)

    def lambda_AC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_AC5)
    WaitChrThread(0xF5, 1)

    ChrTalk(
        0x8,
        (
            "#5PHaha, it really is you\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, I never thought\x01",
            "I'd see you all here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(590, 400, 910, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16820, 3000)

    def lambda_B62():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B62)
    Sleep(50)

    def lambda_B7F():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B7F)
    Sleep(50)

    def lambda_B9C():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B9C)
    Sleep(50)

    def lambda_BB9():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BB9)
    Sleep(50)

    def lambda_BD6():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_BD6)
    Sleep(50)

    def lambda_BF3():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_BF3)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00001FYes, likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FCrossbell Times rookie\x01",
            "reporter, photographer,\x01",
            "and Grace's co-worker...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FAnd since you're here, that's not\x01",
            "all, huh.\x02\x03",
            "#00301FSo, how about you stop playin'\x01",
            "dumb and show us your true colors?\x02\x03",
            "Since you didn't even flinch when\x01",
            "you noticed us, tells me you're up\x01",
            "to somethin', isn't that right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, though I should say\x01",
            "that's just how I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PActually, I work for...\x01",
            "a private research\x01",
            "agency.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FA private research\x01",
            "agency...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, a company called\x01",
            ""R&A Research" in\x01",
            "Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F"R&A Research"... I feel\x01",
            "like I've heard that\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEA")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FHmm, I at least know the\x01",
            "name...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEA")


    ChrTalk(
        0x8,
        (
            "#5PWell, it's just a\x01",
            "recently formed small\x01",
            "company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlthough I think Director\x01",
            "Richard has quite a bit\x01",
            "of fame to his name.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E4")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00105FCould he be... Former\x01",
            "Colonel Richard of the\x01",
            "Liberl Royal Army?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00600FI see...now it makes\x01",
            "sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FElie, Mr. Dudley... Do\x01",
            "you know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603FYeah. Alan Richard.\x02\x03",
            "#00600F...He's the former intelligence\x01",
            "officer who lead the coup\x01",
            "d'etat in Liberl two years ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F3")

    label("loc_10E4")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00105FCould he be... Former\x01",
            "Colonel Richard of the\x01",
            "Liberl Royal Army?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FElie, do you know him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes. Alan Richard.\x02\x03",
            "#00101F...He's the former intelligence\x01",
            "officer who led the coup d'etat\x01",
            "in Liberl two years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F3")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FHe started that coup?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FThat's right. However, during the Liberl\x01",
            "phenomenon, he played a very active role\x01",
            "in helping solve the national crisis...\x02\x03",
            "#00100FAfterwards, I heard he received an\x01",
            "official pardon from Her Majesty the\x01",
            "Queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FA pardon...\x02\x03",
            "#00003FI see, so he started a\x01",
            "research agency to\x01",
            "revive his own career.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13CC")

    ChrTalk(
        0x106,
        (
            "#12P#10703FHow to say this... He\x01",
            "seems a sharp and able\x01",
            "person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1471")

    label("loc_13CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(
        0x105,
        (
            "#12P#10402FHehe. He seems to have\x01",
            "excellent character.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1471")

    label("loc_141D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(
        0x109,
        (
            "#12P#10106FHow to say this... He\x01",
            "seems to be an excellent\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1471")


    ChrTalk(
        0x8,
        (
            "#5PHmm, as expected of the\x01",
            "Support Section. You all know\x01",
            "a lot about this already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P―And so, do you\x01",
            "understand my position a\x01",
            "little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYes, I have a general\x01",
            "idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FI have one question. Why\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, because I believed one\x01",
            "day that I'd have a chance\x01",
            "to work with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PRevealing myself now or\x01",
            "later won't make any\x01",
            "difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, I haven't\x01",
            "told anyone at Crossbell\x01",
            "News, not even Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's a shameless request,\x01",
            "but could you please do me\x01",
            "a favor and keep it secret?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FSure. From what we've\x01",
            "heard, you're nothing\x01",
            "more than a third party.\x02\x03",
            "We have no intentions of\x01",
            "leaking your secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you very much. I\x01",
            "thought you'd say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FThat reminds me, we heard connecting\x01",
            "orbal communications is difficult\x01",
            "due to an effect of the mist, but...\x02\x03",
            "#00205FYou can use your communicator\x01",
            "without any problems, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, you mean this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe mist has an effect to be\x01",
            "sure, but this communicator can\x01",
            "send out powerful orbal waves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, its range is such\x01",
            "that it just barely\x01",
            "reaches outside Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, I was just having a\x01",
            "conversation with the director himself\x01",
            "who is in Altair City on business.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19B8")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FI see... Under these\x01",
            "circumstances, he's an\x01",
            "important contact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A76")

    label("loc_19B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A1C")

    ChrTalk(
        0x105,
        (
            "#12P#10404FI see... Under these\x01",
            "circumstances, he's an\x01",
            "important contact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A76")

    label("loc_1A1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A76")

    ChrTalk(
        0x109,
        (
            "#12P#10105FI see... Under these\x01",
            "circumstances, he's a\x01",
            "great contact.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A76")


    ChrTalk(
        0x104,
        (
            "#12P#00303FThat communicator... From the\x01",
            "look of it, it seems able to\x01",
            "use encrypted communications.\x02\x03",
            "#00302FI guess it'd even put the\x01",
            "army to shame, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHaha. Putting it to shame would be\x01",
            "a bit of an exaggeration but...\x01",
            "You know your stuff, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell for the time being, my\x01",
            "communications can't be\x01",
            "analyzed by the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, by the way, because this\x01",
            "communicator is a highly efficient\x01",
            "model, it cost me a whole lot of mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI was warned by the vice director to\x01",
            "not break it at all costs, so I'm\x01",
            "extra careful when carrying it around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAccordingly, please keep\x01",
            "the fact that I'm here\x01",
            "in the utmost secrecy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DEE")

    ChrTalk(
        0x106,
        (
            "#12P#10703F...A statement befitting\x01",
            "a secret agent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E98")

    label("loc_1DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E53")

    ChrTalk(
        0x109,
        (
            "#12P#10103FHow to say it... That was\x01",
            "a statement befitting a\x01",
            "secret agent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E98")

    label("loc_1E53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E98")

    ChrTalk(
        0x105,
        (
            "#12P#10404FHeh. How fitting for a\x01",
            "secret agent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E98")


    ChrTalk(
        0x8,
        (
            "#5PHaha, right. Really\x01",
            "though, my worries are\x01",
            "never ending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...That aside, we ended\x01",
            "up having quite the\x01",
            "talk, didn't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI intend to stay here and\x01",
            "keep being in with our people\x01",
            "outside Crossbell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'm a little worried about you all\x01",
            "as well. Please be very careful\x01",
            "when infiltrating Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FSure― Wait, I don't\x01",
            "remember telling you about\x01",
            "that.\x02\x03",
            "#00000FWell anyway, we don't have\x01",
            "the time for that, so we'll\x01",
            "excuse ourselves here.\x02\x03",
            "#00001FThe same to you, Reins. Be\x01",
            "very careful with what\x01",
            "you're doing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYes, of course.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_260 end

    def Function_5_210B(): pass

    label("Function_5_210B")

    Sound(32, 0, 30, 0)
    Sleep(700)
    Sound(33, 0, 20, 0)
    Sleep(700)
    Sound(32, 0, 40, 0)
    Sleep(700)
    Sound(33, 0, 30, 0)
    Sleep(700)

    label("loc_212F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2151")
    Sound(32, 0, 50, 0)
    Sleep(700)
    Sound(33, 0, 40, 0)
    Sleep(700)
    Jump("loc_212F")

    label("loc_2151")

    Return()

    # Function_5_210B end

    SaveToFile()

Try(main)
