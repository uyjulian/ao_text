from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e430b.bin",                # FileName
        "e430b",                    # MapName
        "e430b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e430b",                  # 0
        "Lovely Girl",            # 1
        "White Falcon",           # 2
        "Female Officer",         # 3
        "Airship",                # 4
        "Demon Wald",             # 5
        "Ogre Sigmund",           # 6
        "Bloody Shirley",         # 7
        "Jaeger",                 # 8
        "Jaeger",                 # 9
        "Jaeger",                 # 10
        "Jaeger",                 # 11
        "Jaeger",                 # 12
        "Jaeger",                 # 13
        "Jaeger",                 # 14
        "Jaeger",                 # 15
        "Jaeger",                 # 16
        "Jaeger",                 # 17
        "SE制御",                 # 18
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(704, 0)                                        # 0

    ScpFunction((
        "Function_0_2C0",          # 00, 0
        "Function_1_30F",          # 01, 1
        "Function_2_356",          # 02, 2
        "Function_3_1334",         # 03, 3
        "Function_4_138B",         # 04, 4
        "Function_5_13AD",         # 05, 5
        "Function_6_13CF",         # 06, 6
        "Function_7_1411",         # 07, 7
        "Function_8_1432",         # 08, 8
        "Function_9_1518",         # 09, 9
        "Function_10_1800",        # 0A, 10
        "Function_11_1DC4",        # 0B, 11
        "Function_12_1ECB",        # 0C, 12
    ))


    def Function_0_2C0(): pass

    label("Function_0_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2D4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_30E")

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_2EB")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 8)
    Jump("loc_30E")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_2FF")
    ClearScenarioFlags(0x22, 2)
    Event(0, 10)
    Jump("loc_30E")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_30E")
    ClearScenarioFlags(0x22, 3)
    Event(0, 9)

    label("loc_30E")

    Return()

    # Function_0_2C0 end

    def Function_1_30F(): pass

    label("Function_1_30F")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF0A070D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_331")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_331")

    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x2, 0x2)
    ClearMapObjFlags(0x3, 0x4)
    Return()

    # Function_1_30F end

    def Function_2_356(): pass

    label("Function_2_356")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch13800.itc", 0x1F)
    LoadChrToIndex("chr/ch11200.itc", 0x20)
    LoadChrToIndex("chr/ch13801.itc", 0x21)
    LoadChrToIndex("chr/ch13802.itc", 0x22)
    LoadChrToIndex("apl/ch51206.itc", 0x23)
    CreatePortrait(0, 16, 192, 528, 256, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis502.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07101.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    SoundLoad(847)
    SoundLoad(496)
    SoundLoad(132)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x14B, 0x1AE, 0x0, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x20)
    SetChrBattleFlags(0x8, 0x20)
    SetChrPos(0x8, 2998500, 52600, 14500, 270)

    def lambda_490():
        OP_98(0xFE, 0xA, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_490)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, 3000000, 52600, 8000, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(3000000, 53100, 4000, 0)
    MoveCamera(259, -13, -10, 0)
    OP_6E(900, 0)
    SetCameraDistance(107500, 0)
    Sound(496, 2, 50, 0)
    Sound(132, 2, 60, 0)
    OP_68(3000000, 52100, 8000, 9000)
    MoveCamera(215, -7, 0, 9000)
    SetCameraDistance(47500, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(800)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    BeginChrThread(0x19, 1, 0, 7)
    Fade(500)
    OP_68(2997640, 55600, 14290, 0)
    OP_68(2997640, 54200, 14290, 2500)
    MoveCamera(224, 11, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11790, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#40WWhat a nice breeze...\x02\x03",
            "This stream of clouds... I wonder\x01",
            "if it's clear over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Sound(846, 0, 100, 0)
    BeginChrThread(0x19, 1, 0, 6)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    MoveCamera(225, 17, 0, 5000)
    SetCameraDistance(27500, 5000)
    OP_93(0x8, 0x2D, 0x190)
    Sleep(3000)
    ClearChrFlags(0x9, 0x80)

    def lambda_701():

        label("loc_701")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_701")

    QueueWorkItem2(0x9, 2, lambda_701)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(500)

    def lambda_71C():

        label("loc_71C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_71C")

    QueueWorkItem2(0x8, 2, lambda_71C)
    WaitChrThread(0x9, 3)
    Fade(500)
    OP_68(2997640, 54200, 14290, 0)
    MoveCamera(224, 11, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12290, 0)
    SetCameraDistance(11790, 1500)
    EndChrThread(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    EndChrThread(0x9, 0x2)
    SetChrPos(0x9, 2998900, 54100, 14100, 0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_7A6():
        OP_96(0xFE, 0x2DC274, 0xCF6C, 0x3714, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7A6)

    def lambda_7C0():

        label("loc_7C0")

        OP_A0(0xFE, 1500, 0x0, 0x1)
        Yield()
        Jump("loc_7C0")

    QueueWorkItem2(0x9, 2, lambda_7C0)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x2)
    StopSound(847, 500, 70)
    Fade(250)
    SetChrSubChip(0x8, 0x1)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#08009F#5PScree!\x02\x03",
            "#08000FScree, scree, scree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07004FHaha. Good work, as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    Sound(18, 0, 60, 0)
    SetChrSubChip(0x8, 0x2)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#07001F#30W...............\x02\x03",
            "#07003FAs I thought. There's\x01",
            "trouble brewing even in the\x01",
            "Republic.\x02\x03",
            "And Heiyue and a leading\x01",
            "jaeger corps are getting\x01",
            "involved...\x02\x03",
            "#07008FThen, as for those acting as\x01",
            "the Blood and Iron\x01",
            "Chancellor's subordinates...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#08000F#5PScree?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_64(0x8)
    Sleep(300)
    Fade(250)
    Sound(18, 0, 30, 0)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11P#07004FHaha, it's nothing.\x02\x03",
            "#07002FI'm heading northeast tomorrow,\x01",
            "so come ride with us, ok?\x02\x03",
            "#07009FEven if you are a falcon, it'd\x01",
            "be hard for you to make an\x01",
            "international trip by yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#08009F#5PScree.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    OP_93(0x8, 0x5A, 0x0)

    def lambda_AD6():

        label("loc_AD6")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_AD6")

    QueueWorkItem2(0x8, 2, lambda_AD6)
    Sound(847, 0, 60, 0)

    def lambda_AEE():
        OP_9D(0xFE, 0x2DBB08, 0xCF6C, 0x2FA8, 0x3E8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AEE)

    def lambda_B0B():

        label("loc_B0B")

        OP_A0(0xFE, 1500, 0x0, 0x1)
        Yield()
        Jump("loc_B0B")

    QueueWorkItem2(0x9, 2, lambda_B0B)

    def lambda_B1D():
        OP_93(0xFE, 0x2D, 0x64)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_B1D)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x2)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B60():
        OP_98(0xFE, 0xFFFFFFF6, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B60)
    EndChrThread(0x8, 0x2)
    Sleep(300)
    BeginChrThread(0x9, 3, 0, 4)
    Sleep(700)

    NpcTalk(
        0xA,
        "Calm Voice",
        (
            "#11P─Your Highness. You're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2999150, 54400, 14400, 3000)
    MoveCamera(204, 14, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(11250, 3000)

    def lambda_BEA():

        label("loc_BEA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_BEA")

    QueueWorkItem2(0x8, 2, lambda_BEA)

    def lambda_BFC():

        label("loc_BFC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_BFC")

    QueueWorkItem2(0x9, 2, lambda_BFC)
    ClearChrFlags(0xA, 0x20)

    def lambda_C13():
        OP_97(0xFE, 0x0, 0x0, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C13)

    def lambda_C2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C2D)
    WaitChrThread(0xA, 1)

    def lambda_C42():
        OP_97(0xFE, 0xFFFFFCE0, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C42)
    WaitChrThread(0xA, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 5)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#12P#07002FHaha... I wanted to feel\x01",
            "the wind.\x02\x03",
            "#07004FLooks like I'm a little\x01",
            "nervous for tomorrow's\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xA,
        "Haha. Surely you jest.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x9, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        (
            "#5P#07105FAh, Sieg. So you've\x01",
            "returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P#08000FScree, scree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#07003F...Here.\x02\x03",
            "#07001FI received a report from\x01",
            "R&A research.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x8, 500)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#5P#07101FFrom Sir Richard...!?\x02\x03",
            "#07103FI'll take a look.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E84():
        OP_99(0xFE, 0x8, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E84)
    WaitChrThread(0xA, 1)
    Sound(802, 0, 100, 0)
    Sleep(700)

    def lambda_EA5():
        OP_96(0xFE, 0x2DC3A0, 0xCD78, 0x319C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EA5)
    WaitChrThread(0xA, 1)
    Sleep(300)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(500)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#5P#07105F...Radical nationalists...\x01",
            "And the Republican\x01",
            "government's actions, huh.\x02\x03",
            "#07101FIt appears the situation is\x01",
            "developing more quickly than\x01",
            "we anticipated on all fronts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#07003FYes. I must consult with\x01",
            "the prince on this when\x01",
            "I see him.\x02\x03",
            "#07000FAlso─ Maybe I'll rely on\x01",
            "him for a small\x01",
            "connection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#07105FA connection... you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#07004FYes. I still need to\x01",
            "ascertain whether it can\x01",
            "really be counted on, though.\x02\x03",
            "#07002FIt's possible they will come\x01",
            "to our aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#5P#07102FOh, the ones Estelle and\x01",
            "Joshua were talking about.\x02\x03",
            "#07104FI see. It seems there's\x01",
            "value in contacting people\x01",
            "other than the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12P#07004FYes...\x02",
    )

    CloseMessageWindow()
    OP_68(2999090, 55210, 15940, 2500)
    MoveCamera(221, 1, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(9600, 2500)
    OP_93(0x8, 0x10E, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#5P#07003F─It's been two years since the\x01",
            "signing of the Non-Aggression\x01",
            "Pact proposed by grandmother.\x02\x03",
            "War has been avoided, but it\x01",
            "seems unseen pressure is building\x01",
            "throughout the continent.\x02\x03",
            "#07008FWe must somehow find a new\x01",
            "framework to succeed the non-\x01",
            "aggression pact...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(10600, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopSound(496, 1000, 20)
    StopSound(132, 1000, 60)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x34F)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_356 end

    def Function_3_1334(): pass

    label("Function_3_1334")

    SetChrPos(0xFE, 3015800, 57600, 27500, 45)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 2993600, 57600, 19900)
    OP_9F(0x1, 2995100, 55300, 12300)
    OP_9F(0x1, 2998600, 54300, 11300)
    OP_9F(0x1, 2999300, 53300, 14000)
    OP_9F(0x2, 0xFE, 7000, 0x2)
    Return()

    # Function_3_1334 end

    def Function_4_138B(): pass

    label("Function_4_138B")

    Sound(100, 0, 100, 0)
    OP_71(0x1, 0x320, 0x384, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x385, 0x3E8, 0x0, 0x20)
    Return()

    # Function_4_138B end

    def Function_5_13AD(): pass

    label("Function_5_13AD")

    Sound(100, 0, 100, 0)
    OP_71(0x1, 0x3E9, 0x44C, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x14B, 0x1AE, 0x0, 0x20)
    Return()

    # Function_5_13AD end

    def Function_6_13CF(): pass

    label("Function_6_13CF")

    Sleep(800)
    Sound(847, 2, 20, 0)
    Sleep(300)
    OP_25(0x34F, 0x19)
    Sleep(300)
    OP_25(0x34F, 0x1E)
    Sleep(300)
    OP_25(0x34F, 0x23)
    Sleep(300)
    OP_25(0x34F, 0x28)
    Sleep(300)
    OP_25(0x34F, 0x2D)
    Sleep(300)
    OP_25(0x34F, 0x32)
    Sleep(300)
    OP_25(0x34F, 0x37)
    Sleep(300)
    OP_25(0x34F, 0x3C)
    Return()

    # Function_6_13CF end

    def Function_7_1411(): pass

    label("Function_7_1411")

    OP_25(0x1F0, 0x2D)
    Sleep(300)
    OP_25(0x1F0, 0x28)
    Sleep(300)
    OP_25(0x1F0, 0x23)
    Sleep(300)
    OP_25(0x1F0, 0x1E)
    Sleep(300)
    OP_25(0x1F0, 0x19)
    Return()

    # Function_7_1411 end

    def Function_8_1432(): pass

    label("Function_8_1432")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(125)
    SoundLoad(897)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_68(0, 0, 0, 0)
    MoveCamera(117, -9, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(24000, 0)
    PlayBGM("ed7560", 0)
    ReplaceBGM("ed7513", "ed7560")
    Sound(125, 2, 100, 0)
    Sound(897, 2, 100, 0)
    MoveCamera(117, -15, 0, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(125, 500, 100)
    StopSound(897, 500, 100)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t108B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1432 end

    def Function_9_1518(): pass

    label("Function_9_1518")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(125)
    SoundLoad(897)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_68(0, 0, 0, 0)
    MoveCamera(130, -10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20350, 0)
    Sound(125, 2, 50, 0)
    Sound(897, 2, 50, 0)
    MoveCamera(130, -13, 0, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(200, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00004F...What a splendid moon...\x02\x03",
            "#00000FCould it be because there's\x01",
            "fewer street lights than in\x01",
            "Crossbell City?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 140, -1, -1)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        (
            "#01809F#30W*giggle*, that's\x01",
            "right...\x02\x03",
            "#01810F#30W............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006FUhhm...\x02\x03",
            "#00002FThis morning, Wazy told\x01",
            "me something strange.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 140, -1, -1)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        "#01805FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 170, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00001FI'd suddenly wake up in the\x01",
            "middle of the night and run\x01",
            "into a lone girl, he said.\x02\x03",
            "#00012FHonestly, it was cryptic,\x01",
            "but I think he got it\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 140, -1, -1)
    SetChrName("Rixia")

    AnonymousTalk(
        0xFF,
        "#01809FHaha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(125, 2000, 40)
    StopSound(897, 2000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("t108B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1518 end

    def Function_10_1800(): pass

    label("Function_10_1800")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03350.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch41900.itc", 0x20)
    LoadEffect(0x0, "event/ev17087.eff")
    SoundLoad(2765)
    SoundLoad(497)
    SoundLoad(825)
    SoundLoad(868)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, 0, 10000, 0, 0)
    OP_D5(0xB, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x65, 0x82, 0x0, 0x20)
    OP_87(0x0, 0x0, 0x0, "Null_burn_l", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    OP_87(0x0, 0x1, 0x0, "Null_burn_r", 0x7, 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x5DC, 0x5DC, 0x7D0, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x2, 0xC)
    OP_49()
    SetChrPos(0xC, 2700, 21410, -9400, 240)
    OP_D5(0xC, 0x0, 0x3A980, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x47E, 0x4A6, 0x0, 0x20)
    SetChrFlags(0xC, 0x1)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 0, 21410, -11400, 180)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1800, 21410, -11200, 180)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 1300, 21410, -5000, 180)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 2500, 21410, -5000, 180)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -1300, 21410, -5000, 180)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -2500, 21410, -5000, 180)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 1300, 21410, -3800, 180)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 2500, 21410, -3800, 180)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -1300, 21410, -3800, 180)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -2500, 21410, -3800, 180)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 700, 21410, -6900, 180)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -700, 21410, -6900, 180)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 350000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xD2, 0x96, 0xAA, 0x0, 0x0)
    OP_11(0x6F, 0x27, 0x38, 0xA, 0x514, 0x0)
    OP_68(0, 21910, -8500, 0)
    MoveCamera(38, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(22000, 0)
    BeginChrThread(0x19, 1, 0, 12)
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(300, 200, -1, -1)

    NpcTalk(
        0xD,
        "Wazy",
        "#10310F#4P#N─Wald!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(300, 200, -1, -1)

    NpcTalk(
        0xD,
        "Noｱl",
        "#10107F#4P#NT-That girl too!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(300, 200, -1, -1)

    NpcTalk(
        0xD,
        "Lloyd",
        (
            "#00010F#4P#NUgh, they've even got an\x01",
            "airship!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 21690, -8500, 3000)
    MoveCamera(15, -7, -25, 3000)
    SetCameraDistance(32000, 8000)
    Sound(499, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 11)
    BeginChrThread(0xD, 3, 0, 11)
    BeginChrThread(0xE, 3, 0, 11)
    BeginChrThread(0xC, 3, 0, 11)
    BeginChrThread(0xF, 3, 0, 11)
    BeginChrThread(0x10, 3, 0, 11)
    BeginChrThread(0x11, 3, 0, 11)
    BeginChrThread(0x12, 3, 0, 11)
    BeginChrThread(0x13, 3, 0, 11)
    BeginChrThread(0x14, 3, 0, 11)
    BeginChrThread(0x15, 3, 0, 11)
    BeginChrThread(0x16, 3, 0, 11)
    BeginChrThread(0x17, 3, 0, 11)
    BeginChrThread(0x18, 3, 0, 11)
    Sleep(2000)
    StopSound(497, 2000, 90)
    Sleep(2000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 150, -1, -1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)

    AnonymousTalk(
        0x104,
        "#00310F#5S#24A#2765VOOOOOOOOOOH!!\x02",
    )

    Sleep(2000)
    FadeToDark(2000, 0, -1)
    CloseMessageWindow()
    OP_0D()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopSound(825, 2000, 60)
    StopSound(868, 2000, 70)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c018D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1800 end

    def Function_11_1DC4(): pass

    label("Function_11_1DC4")


    def lambda_1DC9():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DC9)
    Sleep(200)

    def lambda_1DE6():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DE6)
    Sleep(200)

    def lambda_1E03():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E03)
    Sleep(200)

    def lambda_1E20():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E20)
    Sleep(200)

    def lambda_1E3D():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E3D)
    Sleep(200)

    def lambda_1E5A():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E5A)
    Sleep(200)

    def lambda_1E77():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E77)
    Sleep(200)

    def lambda_1E94():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E94)
    Sleep(200)

    def lambda_1EB1():
        OP_98(0xFE, 0x0, 0x4E20, 0x7A120, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EB1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1DC4 end

    def Function_12_1ECB(): pass

    label("Function_12_1ECB")

    Sound(497, 2, 40, 0)
    Sound(825, 2, 10, 0)
    Sound(868, 2, 40, 0)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x339, 0x14)
    OP_25(0x364, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    OP_25(0x339, 0x1E)
    OP_25(0x364, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    OP_25(0x339, 0x28)
    OP_25(0x364, 0x46)
    Sleep(200)
    OP_25(0x1F1, 0x50)
    OP_25(0x339, 0x32)
    OP_25(0x364, 0x50)
    Sleep(200)
    OP_25(0x1F1, 0x5A)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x64)
    OP_25(0x339, 0x46)
    Return()

    # Function_12_1ECB end

    SaveToFile()

Try(main)
