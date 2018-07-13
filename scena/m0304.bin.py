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
        "Function_4_273",          # 04, 4
        "Function_5_2211",         # 05, 5
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
            "day as a R&A Research member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in any case, first of all I'll pray for \x01",
            "the success of your breaking into operation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_1A9 end

    def Function_4_273(): pass

    label("Function_4_273")

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
            "#00001FSo it really connected\x01",
            "to the Geofront...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00103FThis looks like a portion of the\x01",
            "D-Division without a doubt...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00205F...The presence has gotten stronger.\x02\x03",
            "#00203FIt is only one, however...\x01",
            "It seems it is true that someone is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B6")

    AnonymousTalk(
        0x10A,
        "#00601F(Beyond this door...?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_531")

    label("loc_4B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F8")

    AnonymousTalk(
        0x109,
        "#10101F(Further beyond this door...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_531")

    label("loc_4F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_531")

    AnonymousTalk(
        0x106,
        "#10701F(Beyond this door.......)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_531")


    AnonymousTalk(
        0x103,
        "#00201F(Yes, no doubt about it.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DD")

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
    Jump("loc_6CD")

    label("loc_5DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65D")

    AnonymousTalk(
        0x106,
        (
            "#10705F(Could this place be a warehouse or something?\x01",
            "It looks like there's a window on the door.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6CD")

    label("loc_65D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CD")

    AnonymousTalk(
        0x109,
        (
            "#10105F(Is this place a warehouse or something?\x01",
            "It seems there's a window on the door.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6CD")


    AnonymousTalk(
        0x101,
        (
            "#00003F(I don't know, but...\x01",
            "At any rate, that's convenient.)\x02\x03",
            "#00000F(Let's try to see the situation\x01",
            "inside from here for a little.)\x02",
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
            "Ahaha...I'm sorry, Director.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#N(That figure from behind...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00105F#N(Could he be...\x01",
            "Mr. Reins from\x01",
            "Crossbell Times?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#N(I wonder what is he doing in such a place...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PUhhm...are you over there the\x01",
            "Special Support Section members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWould you like to come\x01",
            "in for a light talk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#NOh man...\x01",
            "He had already noticed us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00001F#NWe can't let our guard down, but for\x01",
            "the time being, let's do how he says.\x02",
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

    def lambda_A19():
        OP_97(0xFE, 0x0, 0x0, 0x10CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A19)

    def lambda_A33():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A33)
    Sleep(100)

    def lambda_A47():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A47)

    def lambda_A61():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A61)
    Sleep(100)

    def lambda_A75():
        OP_97(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A75)

    def lambda_A8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A8F)
    Sleep(500)

    def lambda_AA3():
        OP_97(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA3)

    def lambda_ABD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_ABD)
    Sleep(100)

    def lambda_AD1():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_AD1)

    def lambda_AEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_AEB)
    Sleep(100)

    def lambda_AFF():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_AFF)

    def lambda_B19():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_B19)
    WaitChrThread(0xF5, 1)

    ChrTalk(
        0x8,
        "#5PHa ha, it was really you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, I would've never\x01",
            "dreamed to meet you\x01",
            "all in such a place.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(590, 400, 910, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(16820, 3000)

    def lambda_BC7():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC7)
    Sleep(50)

    def lambda_BE4():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE4)
    Sleep(50)

    def lambda_C01():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C01)
    Sleep(50)

    def lambda_C1E():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C1E)
    Sleep(50)

    def lambda_C3B():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_C3B)
    Sleep(50)

    def lambda_C58():
        OP_97(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_C58)
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
            "#12P#00103FCrossbell Times newcomer\x01",
            "journalist, a photographer,\x01",
            "Miss Grace's partner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWell, by meetin' you here it's\x01",
            "certain you aren't only those.\x02\x03",
            "#00301FWell man, what about not feignin' ignorance\x01",
            "and tellin' us your real identity on the double?\x02\x03",
            "Since you didn't hide when\x01",
            "you noticed us means you\x01",
            "had that intention too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, although I should say\x01",
            "that's in my character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PActually, I work for...\x01",
            "A private research agency.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FA private research agency...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, a company named\x01",
            ""R&A Research" \x01",
            "located in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105F"R&A Research"...\x01",
            "I have a feeling like I\x01",
            "already heard about it...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F83")

    ChrTalk(
        0x10A,
        "#12P#00603FHm, I know at least the name...\x02",
    )

    CloseMessageWindow()

    label("loc_F83")


    ChrTalk(
        0x8,
        (
            "#5PWell, it's just a small company\x01",
            "recently made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlthough I think that Director \x01",
            "Richard is famous in a way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1178")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00105FCould he be...\x01",
            "Former Colonel Richard who\x01",
            "belonged to the Royal Army?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#12P#00600FI see...now it makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FElie, Mr. Dudley...\x01",
            "Do you know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#12P#00603FYeah. Alan Richard.\x02\x03",
            "#00600F...He's the former intelligence officer\x01",
            "who caused the coup d'etat in Liberl\x01",
            "two years ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1290")

    label("loc_1178")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#00105FCould he be...\x01",
            "Former Colonel Richard who\x01",
            "belonged to the Royal Army?\x02",
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
            "#00101F...He's the former intelligence officer\x01",
            "who caused the coup d'etat in Liberl\x01",
            "two years ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1290")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00005FHe caused that coup...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FThat's right. However, at the time of the \x01",
            "Liberl phenomenon he played a very active \x01",
            "role in helping out with the national crisis...\x02\x03",
            "#00100FAfterwards, it is said he officially received\x01",
            "a pardon from Her Majesty the Queen.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1485")

    ChrTalk(
        0x106,
        (
            "#12P#10703FWhat can I say...\x01",
            "It seems he's quite a sharp and able person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1535")

    label("loc_1485")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DD")

    ChrTalk(
        0x105,
        (
            "#12P#10402FHu hu, it appears he's a\x01",
            "very excellent character.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1535")

    label("loc_14DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1535")

    ChrTalk(
        0x109,
        (
            "#12P#10106FWhat can I say...\x01",
            "It seems he's quite an excellent man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1535")


    ChrTalk(
        0x8,
        (
            "#5PHm, as expected from the SSS.\x01",
            "You're knowledgeable on this subject too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P―And so, did you understand\x01",
            "my position a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FYes, I have a general idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FHowever, why did you want\x01",
            "to reveal it to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, because I think that one\x01",
            "day there will be the chance to\x01",
            "work with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn that aspect, revealing it now\x01",
            "or later it's the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, I didn't tell it to\x01",
            "anyone at the News Service, \x01",
            "much less to Miss Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's a shameless request, but could you\x01",
            "please do me the favor to keep it secret?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes. From what we've heard,\x01",
            "you should be just outsiders.\x01\x02\x03",
            "We don't have the slightest intention\x01",
            "to leak out your secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you very much.\x01",
            "I thought you'd say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FBy the way, I heard orbal\x01",
            "communications were hard to go through\x01",
            "due to that mist's influence, but...\x02\x03",
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
            "#5POf course it is affected by the mist,\x01",
            "but this communicator is able to\x01",
            "just release powerful orbal waves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, its range is at a level that\x01",
            "just barely goes over Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way, I was just having a conversation \x01",
            "with the Director himself who has come to \x01",
            "Altair City on a business trip.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1ABB")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FI see... Under these circumstances,\x01",
            "he's a precious liaison.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B77")

    label("loc_1ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B1D")

    ChrTalk(
        0x105,
        (
            "#12P#10404FI see... Under these circumstances,\x01",
            "he's a precious liaison.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B77")

    label("loc_1B1D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B77")

    ChrTalk(
        0x109,
        (
            "#12P#10105FI see... Under these circumstances,\x01",
            "he's a great liaison.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B77")


    ChrTalk(
        0x104,
        (
            "#12P#00303FThat communicator...\x01",
            "From its looks it seems to be the type you \x01",
            "can use even for encrypted communications.\x02\x03",
            "#00302FIt would really put the\x01",
            "army to shame, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHa ha, putting it to shame would be\x01",
            "overestimating it, as you can imagine...\x01",
            "But you know your stuff, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, for the time being, communications\x01",
            "can't be analyzed by the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, by the way, being the case that this\x01",
            "communicator is highly efficient, it even\x01",
            "costed a lot of mira accordingly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSince I was warned by the Vice Director\x01",
            "to not break it at all costs, I pay a lot\x01",
            "of attention when carrying it around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PStill, please keep the utmost\x01",
            "secrecy from other people\x01",
            "that I'm in this place.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F29")

    ChrTalk(
        0x106,
        "#12P#10703F...Quite the private agency-like statement.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1F29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F87")

    ChrTalk(
        0x109,
        (
            "#12P#10103FHow to say it...\x01",
            "A really private agency-like statement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1F87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FD7")

    ChrTalk(
        0x105,
        "#12P#10404FHu hu, quite the private agency-like statement.\x02",
    )

    CloseMessageWindow()

    label("loc_1FD7")


    ChrTalk(
        0x8,
        (
            "#5PHa ha, that's right.\x01",
            "Really, my worries are unending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...That aside, we ended up\x01",
            "being quite deep in talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI intend to stay here and\x01",
            "keep being in contact with\x01",
            "the people outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou too everyone, please be\x01",
            "very careful when breaking\x01",
            "into Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYes― Wait, I think we\x01",
            "didn't talk about that.\x02\x03",
            "#00000FWell, in any case, since we don't\x01",
            "have time, we'll excuse us here.\x02\x03",
            "#00001FYou too Mr. Reins, be very\x01",
            "careful with what you're doing here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYes, but of course.\x02",
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

    # Function_4_273 end

    def Function_5_2211(): pass

    label("Function_5_2211")

    Sound(32, 0, 30, 0)
    Sleep(700)
    Sound(33, 0, 20, 0)
    Sleep(700)
    Sound(32, 0, 40, 0)
    Sleep(700)
    Sound(33, 0, 30, 0)
    Sleep(700)

    label("loc_2235")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2257")
    Sound(32, 0, 50, 0)
    Sleep(700)
    Sound(33, 0, 40, 0)
    Sleep(700)
    Jump("loc_2235")

    label("loc_2257")

    Return()

    # Function_5_2211 end

    SaveToFile()

Try(main)
