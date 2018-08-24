from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c121d.bin",                # FileName
        "c121d",                    # MapName
        "c121d",                    # Location
        0x0021,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c121d",                  # 0
        "Jaeger",                 # 1
        "Jaeger",                 # 2
        "Ogre Sigmund",           # 3
        "Member",                 # 4
        "Member",                 # 5
        "Cao",                    # 6
        "Crescent Moon Ring",     # 7
        "SE制御",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(436, 0)                                        # 0

    ScpFunction((
        "Function_0_1B4",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_1C5",          # 02, 2
        "Function_3_13FB",         # 03, 3
        "Function_4_1413",         # 04, 4
        "Function_5_14DA",         # 05, 5
        "Function_6_1679",         # 06, 6
        "Function_7_16A2",         # 07, 7
        "Function_8_1764",         # 08, 8
        "Function_9_1790",         # 09, 9
        "Function_10_1846",        # 0A, 10
        "Function_11_189E",        # 0B, 11
        "Function_12_19EB",        # 0C, 12
        "Function_13_1B52",        # 0D, 13
        "Function_14_1B9A",        # 0E, 14
        "Function_15_1BE2",        # 0F, 15
    ))


    def Function_0_1B4(): pass

    label("Function_0_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1C3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_1C3")

    Return()

    # Function_0_1B4 end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    Return()

    # Function_1_1C4 end

    def Function_2_1C5(): pass

    label("Function_2_1C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    LoadChrToIndex("apl/ch51535.itc", 0x23)
    LoadChrToIndex("chr/ch03350.itc", 0x24)
    LoadChrToIndex("chr/ch03352.itc", 0x25)
    LoadChrToIndex("chr/ch03356.itc", 0x26)
    LoadChrToIndex("chr/ch41950.itc", 0x28)
    LoadChrToIndex("chr/ch41951.itc", 0x29)
    LoadChrToIndex("chr/ch06300.itc", 0x2D)
    LoadChrToIndex("apl/ch51515.itc", 0x2E)
    LoadChrToIndex("chr/ch31500.itc", 0x32)
    LoadChrToIndex("chr/ch31551.itc", 0x33)
    LoadChrToIndex("chr/ch31552.itc", 0x34)
    LoadChrToIndex("chr/ch31553.itc", 0x35)
    LoadChrToIndex("chr/ch31556.itc", 0x36)
    LoadChrToIndex("chr/ch12500.itc", 0x37)
    LoadChrToIndex("chr/ch12551.itc", 0x38)
    LoadChrToIndex("chr/ch12552.itc", 0x39)
    LoadChrToIndex("chr/ch12553.itc", 0x3A)
    LoadChrToIndex("chr/ch12556.itc", 0x3B)
    LoadEffect(0x0, "event/ev15036.eff")
    LoadEffect(0x1, "event/ev15040.eff")
    LoadEffect(0x2, "event/eva01_01.eff")
    LoadEffect(0x3, "event/ev15037.eff")
    LoadEffect(0x4, "battle/ms00001.eff")
    LoadEffect(0x5, "battle/cr033000.eff")
    LoadEffect(0x6, "event/ev15038.eff")
    LoadEffect(0x7, "event/ev15039.eff")
    LoadEffect(0x8, "event\\ev307_00.eff")
    SoundLoad(868)
    SoundLoad(926)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xB, 0x36)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x39)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x20)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x10)
    SetMapObjFrame(0xFF, "ato_yuka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_mado", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_tukue", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_nuki03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage04", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xB, -73500, 0, 600, 180)
    SetChrPos(0xC, -74350, 0, 1750, 180)
    SetChrPos(0xE, -74350, 0, 1750, 180)
    SetChrPos(0xA, -74150, -4000, -9450, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4A3():
        OP_95(0xFE, -74000, -4000, -6450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4A3)

    def lambda_4BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_4BD)
    OP_68(-74150, -3000, -9450, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_68(-74150, -3000, -6450, 1750)
    SetCameraDistance(22000, 1750)
    Sound(868, 2, 20, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 3)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x5)
    Sound(531, 0, 80, 0)
    Sound(538, 0, 80, 0)
    BeginChrThread(0xE, 1, 0, 4)
    BeginChrThread(0xB, 1, 0, 5)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xA,
        "#04512F#12PIt's useless.\x02",
    )

    CloseMessageWindow()
    OP_68(-74150, -500, -2390, 500)
    MoveCamera(51, 12, 5, 500)
    OP_6E(300, 500)
    SetCameraDistance(37250, 500)
    OP_6F(0x79)
    Sound(4132, 255, 100, 0)
    Sound(893, 0, 100, 0)
    Sound(538, 0, 100, 0)
    Sound(926, 2, 100, 0)
    OP_A1(0xA, 0x9C4, 0x4, 0x0, 0x0, 0x0, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, -700, 0, 0, -45, 180, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    SetChrSubChip(0xA, 0x1)
    Sleep(50)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 700, 0, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)
    SetChrChipByIndex(0xB, 0x35)
    Sound(501, 0, 100, 0)
    BeginChrThread(0xB, 0, 0, 10)
    Sound(809, 0, 100, 0)

    def lambda_66E():
        OP_9D(0xFE, 0xFFFEE0E4, 0x0, 0x640, 0xFA, 0xFA0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_66E)

    ChrTalk(
        0xB,
        "#5P#10AGah...\x02",
    )

    Sleep(100)
    SetChrChipByIndex(0xC, 0x3A)
    Sound(501, 0, 100, 0)
    BeginChrThread(0xC, 0, 0, 10)

    def lambda_6B0():
        OP_9D(0xFE, 0xFFFEDD92, 0x0, 0xABE, 0xFA, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B0)

    ChrTalk(
        0xC,
        "#6P#10A...Urgh...\x02",
    )

    Sleep(1900)
    SetChrSubChip(0xA, 0x3)
    OP_24(0x39E)
    Sound(308, 0, 100, 0)
    Sound(538, 0, 100, 0)
    Sleep(500)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x23)
    ClearChrFlags(0xA, 0x4)

    def lambda_711():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_711)
    MoveCamera(40, 7, 5, 3000)
    SetCameraDistance(34250, 3000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x34)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x39)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xB, -38800, 0, 5500, 180)
    SetChrPos(0xC, -35600, 0, 3900, 225)
    SetChrPos(0xA, -38800, -1550, -1700, 0)
    ClearChrFlags(0xA, 0x4)

    def lambda_799():
        OP_95(0xFE, -38800, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_799)
    OP_68(-38800, -1000, -1500, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(26300, 0)
    OP_68(-38800, 800, 1000, 1000)
    MoveCamera(45, 25, 0, 1000)
    SetCameraDistance(24300, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xB, 0, 0, 6)
    BeginChrThread(0xC, 0, 0, 8)
    WaitChrThread(0xA, 1)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x3)
    Sleep(200)
    SetChrSubChip(0xA, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(893, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, 0, 750, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-37350, 800, 4900, 500)
    MoveCamera(45, 23, -5, 500)
    SetCameraDistance(26500, 500)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 7)

    ChrTalk(
        0xB,
        "#5P#10AGwaah!\x02",
    )

    Sleep(100)
    EndChrThread(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 9)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xC,
        "#5PH-How regrettable...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    OP_68(-34500, 1000, 0, 2500)
    MoveCamera(45, 30, -5, 2500)
    SetCameraDistance(24000, 2500)
    SetChrChipByIndex(0xA, 0x23)
    OP_95(0xA, -36150, 0, 1000, 2000, 0x0)
    OP_95(0xA, -34950, 0, 0, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    Sound(893, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x25)
    OP_A1(0xA, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x1)
    Sleep(50)
    SetChrSubChip(0xA, 0x2)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, -1500, 0, 500, 0, 10, 270, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(880, 0, 100, 0)
    Sound(165, 0, 100, 0)
    Sound(196, 0, 80, 0)
    SetMapObjFrame(0x0, "c12dor52:Layer1(1)", 0x2, "アニメ")
    SetMapObjFrame(0x0, "c12dor52:Layer2(2)", 0x2, "アニメ")
    SetMapObjFrame(0x0, "c12dor52:Layer3(3)", 0x2, "アニメ")
    SetMapObjFrame(0x0, "c12dor52:Layer4(4)", 0x2, "アニメ")
    Sleep(1000)
    SetCameraDistance(23000, 2000)
    SetChrChipByIndex(0xA, 0x23)

    def lambda_A54():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A54)

    def lambda_A69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_A69)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x1)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5000, 0, 0, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 5500, 0, 0, 270)
    ClearChrFlags(0xD, 0x80)
    OP_68(-5000, 1000, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23000, 0)

    def lambda_AF7():
        OP_95(0xFE, 1750, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AF7)

    def lambda_B11():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_B11)
    OP_68(4250, 1000, 0, 4000)
    SetCameraDistance(25000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 3)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        (
            "My my. I'm afraid I'll need to ask\x01",
            "you to be a little quieter when\x01",
            "visiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0xA,
        (
            "#04504F#6PHehe. I've got a busy\x01",
            "schedule, you see.\x02\x03",
            "#04500F─At any rate, White\x01",
            "Orchid Dragon. I\x01",
            "expected no less.\x02\x03",
            "With these few\x01",
            "employees... Did you\x01",
            "anticipate our raid?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#03203F#11PYes, more or less.\x02\x03",
            "#03200FNo mercenaries other than you guys would\x01",
            "be reckless enough to bust in through\x01",
            "the front door like that, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04502F#6PHehe. And in spite of\x01",
            "that you didn't run and\x01",
            "waited for us...\x02\x03",
            "Are you saying you want\x01",
            "to fight me, the Ogre?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#03204F#11PHaha, not particularly.\x02\x03",
            "Against an opponent like you,\x01",
            "I have to admit even Master\x01",
            "Yin would be at disadvantage.\x02\x03",
            "#03210FI'm just waiting here to\x01",
            "confirm one small thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04505F#6POh? And what is that,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#03209F#11PIt's simple, really.\x02\x03",
            "#03202F─Who exactly is your\x01",
            "current contractor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04504F#6PHehe... Hahaha....\x02\x03",
            "#04512F─As I thought, you show\x01",
            "some promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 3, 0, 11)
    BeginChrThread(0xD, 1, 0, 13)
    OP_68(4750, 1000, 0, 500)
    MoveCamera(35, 30, 0, 500)
    SetCameraDistance(22500, 500)
    Sleep(500)
    OP_82(0x190, 0x0, 0xBB8, 0x190)
    Sound(4133, 255, 100, 0)

    ChrTalk(
        0xA,
        "#04507F#6P#5S#10AHaaaaah!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 3)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)
    BeginChrThread(0xA, 3, 0, 12)
    BeginChrThread(0xD, 1, 0, 14)
    OP_68(7250, 1000, 0, 500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xD,
        "#03201F#7AHah...!\x02",
    )

    WaitChrThread(0xA, 3)
    WaitChrThread(0xD, 1)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2E)
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x0, 0xD, 0x32, 0x12C)
    Sound(844, 0, 100, 0)

    def lambda_1062():
        OP_9D(0xFE, 0x2710, 0xFFFFEC78, 0xFFFFFF9C, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1062)
    Sleep(50)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    Sound(991, 0, 100, 0)
    Sound(833, 0, 50, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 7900, 900, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "mae_mado", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_mado", 0x1, 0x1)
    WaitChrThread(0xD, 1)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 15)
    OP_68(7450, 1000, -100, 1000)
    SetChrChipByIndex(0xA, 0x23)
    OP_95(0xA, 7450, 0, -100, 2000, 0x0)
    OP_93(0xA, 0x5A, 0x1F4)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xA,
        "#04504F#5PHmph, he got away.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, -3750, 0, 500, 90)
    SetChrPos(0x9, -3000, 0, -500, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x8,
        "Voice",
        "─Master Sigmund!\x02",
    )

    CloseMessageWindow()
    OP_68(5000, 1000, 0, 2000)
    MoveCamera(45, 18, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(23500, 2000)

    def lambda_11F6():
        OP_95(0xFE, 1750, 0, -500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11F6)
    Sleep(100)

    def lambda_1213():
        OP_95(0xFE, 1000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1213)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#04500F#5PWhat about Cao's\x01",
            "subordinate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PI'm terribly sorry. He\x01",
            "suffered injuries,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#04504F#5PHehe. He got away, did\x01",
            "he?\x02\x03",
            "#04500FWhatever. He can hide in\x01",
            "the darkness and sharpen\x01",
            "his fangs.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#04502F#11P─Alright. Let's apply\x01",
            "the "finishing touches".\x02\x03",
            "Let's blow up this place\x01",
            "and head to the IBC\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Jaegers")

    AnonymousTalk(
        0xFF,
        "#4SJa─!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(868, 1000, 20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c030B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C5 end

    def Function_3_13FB(): pass

    label("Function_3_13FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1412")
    OP_A0(0xFE, 5000, 0x10, 0x17)
    Jump("Function_3_13FB")

    label("loc_1412")

    Return()

    # Function_3_13FB end

    def Function_4_1413(): pass

    label("Function_4_1413")

    BeginChrThread(0xE, 0, 0, 3)
    Sound(637, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0xFE, 0xA, 0x1F4, 0x3A98, 0x0)
    StopEffect(0x0, 0x0)
    EndChrThread(0xE, 0x0)
    Sound(532, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(566, 0, 60, 0)
    Sound(196, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_96(0xFE, 0xFFFEDD60, 0xFFFFEE6C, 0xFFFFEED0, 0x3A98, 0x0)
    Return()

    # Function_4_1413 end

    def Function_5_14DA(): pass

    label("Function_5_14DA")

    Sound(241, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -73850, -1800, -2000, 180, 0, 0, 1000, 1000, 1000, 0xA, 0, 1000, 0, 0)
    Sleep(100)
    Sound(241, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -73850, -1800, -2000, 180, 0, 0, 1000, 1000, 1000, 0xA, 0, 1000, 0, 0)
    Sleep(100)
    Sound(241, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -73850, -1800, -2000, 180, 0, 0, 1000, 1000, 1000, 0xA, 0, 1000, 0, 0)
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, 1000, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xA, 0x4, -1000, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_5_14DA end

    def Function_6_1679(): pass

    label("Function_6_1679")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x2)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFF6870, 0x1F4, 0x3E8, 0x2EE, 0xBB8)
    Return()

    # Function_6_1679 end

    def Function_7_16A2(): pass

    label("Function_7_16A2")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_16F1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_16F1)
    OP_9D(0xFE, 0xFFFF66E0, 0x3E8, 0x1B58, 0x4B0, 0x1388)
    EndChrThread(0xFE, 0x3)
    Sound(196, 0, 80, 0)
    Sound(815, 0, 100, 0)

    def lambda_1731():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1731)
    OP_96(0xFE, 0xFFFF66E0, 0x0, 0x1B58, 0xBB8, 0x0)
    SetChrSubChip(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    Return()

    # Function_7_16A2 end

    def Function_8_1764(): pass

    label("Function_8_1764")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x38)
    OP_96(0xFE, 0xFFFF6870, 0x0, 0x3E8, 0x1388, 0x0)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_1764 end

    def Function_9_1790(): pass

    label("Function_9_1790")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_17D9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_17D9)
    OP_9D(0xFE, 0xFFFF79D2, 0x3E8, 0x12C0, 0x4B0, 0x1388)
    EndChrThread(0xFE, 0x3)
    Sound(501, 0, 100, 0)

    def lambda_1813():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1813)
    OP_96(0xFE, 0xFFFF79D2, 0x0, 0x12C0, 0xBB8, 0x0)
    SetChrSubChip(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    Return()

    # Function_9_1790 end

    def Function_10_1846(): pass

    label("Function_10_1846")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_10_1846 end

    def Function_11_189E(): pass

    label("Function_11_189E")

    SetChrFlags(0xFE, 0x20)
    Sound(893, 0, 100, 0)

    def lambda_18AE():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_18AE)
    SetChrChipByIndex(0xA, 0x25)
    OP_A1(0xA, 0x7D0, 0x2, 0x0, 0x1)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, -1500, 0, 500, 0, 10, 270, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(196, 0, 80, 0)
    Sound(165, 0, 100, 0)
    Sound(992, 0, 100, 0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x4, 0, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetChrSubChip(0xA, 0x2)
    SetMapObjFrame(0xFF, "ato_yuka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_tukue", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hane", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae_tukue", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    WaitChrThread(0xA, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_11_189E end

    def Function_12_19EB(): pass

    label("Function_12_19EB")

    SetChrFlags(0xFE, 0x20)

    def lambda_19F5():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19F5)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x3)
    Sound(538, 0, 100, 0)
    Sound(4134, 255, 100, 0)
    PlayEffect(0x5, 0xFF, 0xA, 0x5, 0, 750, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 80, 0)
    Sound(165, 0, 100, 0)
    Sound(992, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x4, 0, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetChrSubChip(0xA, 0x4)
    SetMapObjFrame(0xFF, "ato_yuka03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_nuki03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ato_yuka02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato_tukue", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae_isu", 0x0, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    WaitChrThread(0xA, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_12_19EB end

    def Function_13_1B52(): pass

    label("Function_13_1B52")

    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2E)
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x0, 0xD, 0x32, 0x12C)
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x1996, 0x0, 0xFFFFFDA8, 0x1F4, 0xFA0)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_13_1B52 end

    def Function_14_1B9A(): pass

    label("Function_14_1B9A")

    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2E)
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x0, 0xD, 0x32, 0x12C)
    Sound(250, 0, 100, 0)
    OP_9D(0xFE, 0x1D1A, 0x0, 0xFFFFFF9C, 0x1F4, 0xFA0)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_14_1B9A end

    def Function_15_1BE2(): pass

    label("Function_15_1BE2")

    Sleep(700)
    Sound(976, 0, 70, 0)
    Return()

    # Function_15_1BE2 end

    SaveToFile()

Try(main)
