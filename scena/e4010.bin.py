from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4010.bin",                # FileName
        "e4010",                    # MapName
        "e4010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4010",                  # 0
        "Blond Young Man",        # 1
        "Black-Haired Soldier",   # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    Return()

    # Function_1_E8 end

    def Function_2_E9(): pass

    label("Function_2_E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11102.itc", 0x1E)
    LoadChrToIndex("chr/ch11300.itc", 0x1F)
    LoadChrToIndex("apl/ch51205.itc", 0x20)
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis503.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    SetChrPos(0x0, -7000, 0, 2000, 0)
    SetChrPos(0x1, -7000, 0, 2000, 0)
    SetChrPos(0x2, -7000, 0, 2000, 0)
    SetChrPos(0x3, -7000, 0, 2000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 50, 7100, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7500, 0, -3000, 90)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Youth's Voice")

    AnonymousTalk(
        0xFF,
        "─So you're still awake.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x5)
    OP_68(-6000, 1000, -3000, 0)
    MoveCamera(309, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    PlayBGM("ed7515", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(0, 1000, 5900, 8000)
    MoveCamera(315, 21, 0, 8000)
    SetCameraDistance(18500, 8000)

    def lambda_2DB():
        OP_95(0xFE, -4000, 0, -3000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DB)

    def lambda_2F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2F5)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)

    def lambda_320():
        OP_95(0xFE, 0, 0, 4300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_320)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "We're leaving early tomorrow. How\x01",
            "about getting to sleep already?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x8,
        (
            "#11P#07208F#30WOh, right...\x02\x03",
            "#07203FI just want to briefly\x01",
            "look over these reports.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07303FThe military academy,\x01",
            "huh...\x02\x03",
            "#07302FTo think you'd make such\x01",
            "a serious effort towards\x01",
            "your duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FHaha. In the end, I'm only a\x01",
            "member of the board of\x01",
            "directors on paper, though.\x02\x03",
            "#07200FIt looks like those kids are\x01",
            "trying their hardest. I owe\x01",
            "them at least this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07304FHmph... Well fine, then.\x02\x03",
            "#07300F─However, about that\x01",
            "matter, it seems it's\x01",
            "true.\x02\x03",
            "Duke Cayenne's\x01",
            "subordinates are acting\x01",
            "in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07206FHim, huh? I wondered\x01",
            "whether he was that kind\x01",
            "of man.\x02\x03",
            "#07200FDo we know what he's\x01",
            "planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07303FNo, that's still unclear.\x02\x03",
            "#07300FIt seems the intelligence\x01",
            "division failed to learn\x01",
            "it as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07209FAhaha. Though he got what he\x01",
            "deserves, this is a disaster\x01",
            "for the chancellor, too.\x02\x03",
            "#07202FHaha, could he be planning\x01",
            "on targeting me, as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07306FThat's no laughing\x01",
            "matter.\x02\x03",
            "#07301FShould we reinforce the\x01",
            "escort with personnel\x01",
            "from the 7th Division?\x02\x03",
            "It's still possible to\x01",
            "include a few more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FNo, that won't be\x01",
            "necessary.\x02\x03",
            "Unlike the chancellor,\x01",
            "it'd ruin my image if I\x01",
            "did something like that.\x02\x03",
            "#07202FAlso─\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(400)
    Sound(822, 0, 100, 0)
    OP_63(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetCameraDistance(18200, 400)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#11P#07209FI have you!㈱\x02\x03",
            "#07212FIf you held me in your arms\x01",
            "and protected me, that\x01",
            "alone would be enough!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#11P#07303F─Well then, I'm going to\x01",
            "bed early, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#11P#07206FSorry, I got carried\x01",
            "away.\x02\x03",
            "#07200FIn any case, I'd like to\x01",
            "talk to the princess\x01",
            "tomorrow.\x02\x03",
            "How are those\x01",
            "arrangements going?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#6P#07304FI received word from the\x01",
            "captain.\x02\x03",
            "#07302FIt'll be tomorrow after\x01",
            "the luncheon, towards\x01",
            "evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07202FI see. Haha, so it's\x01",
            "been a whole year.\x02\x03",
            "#07206FExcluding Estelle and\x01",
            "the others, I guess it's\x01",
            "a class reunion.\x02\x03",
            "#07208FSchera's busy too. It\x01",
            "seems she doesn't have\x01",
            "time for a trip abroad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P#07303F...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FWell, I suppose I'll have to\x01",
            "be satisfied with the world's\x01",
            "leading urban resort.\x02\x03",
            "#07212FAh, I don't intend to\x01",
            "interrupt the date between you\x01",
            "and the captain, so rest easy㈱\x02\x03",
            "#07209FIf you like, how about going\x01",
            "to a certain theme park for\x01",
            "that date?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07306F─That's none of your\x01",
            "business, idiot.\x02\x03",
            "#07303FBut, it seems you're\x01",
            "spouting more stupid\x01",
            "nonsense than usual.\x02\x03",
            "#07301FYou wouldn't be thinking\x01",
            "of doing anything bad,\x01",
            "would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07211F*gulp*...\x02\x03",
            "#07209FHahaha, come'ooon. I\x01",
            "wouldn't dream of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07308F(I think I'll put a rope\x01",
            "around his neck\x01",
            "tomorrow.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "─Well, this'll probably be my last\x01",
            "trip abroad.\x02\x03",
            "Looking into those after the\x01",
            "chancellor's life, probing\x01",
            "developments across the\x02\x03",
            "continent...\x02\x03",
            "I know I'm a pain as usual, but I\x01",
            "am counting you─ friend.\x02",
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

    ChrTalk(
        0x9,
        "#6P#07304FHmph, of course.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
