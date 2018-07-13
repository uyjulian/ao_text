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
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        "──Are you still awake?\x02",
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

    def lambda_2DF():
        OP_95(0xFE, -4000, 0, -3000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DF)

    def lambda_2F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2F9)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)

    def lambda_324():
        OP_95(0xFE, 0, 0, 4300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_324)
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
            "We depart early, tomorrow.\x01",
            "What about sleeping already?\x02",
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
            "#11P#07208F#30WAh...yes...\x02\x03",
            "#07203FI just want look over\x01",
            "these reports for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07303FThe military academy...?\x02\x03",
            "#07302FI would've never thought you'd devoted\x01",
            "yourself to your duties this seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FUh uh, after all I'm on the board of\x01",
            "directors, although in name only.\x02\x03",
            "#07200FThose kids seem to be doing their best,\x01",
            "so I must do at least this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07304FHmph...oh, well.\x02\x03",
            "#07300F──At any rate, about that matter,\x01",
            "it appears it's true.\x02\x03",
            "It seems Duke Cayenne's subordinate\x01",
            "is taking measures in secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07206FHim, eh...?\x01",
            "I didn't think it was that kind of man, though.\x02\x03",
            "#07200FDo you know the scale of his plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07303FNo, that's still unknown.\x02\x03",
            "#07300FThe intelligence division seem to have\x01",
            "failed to catch on that regard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07209FAhaha, although he reaps what he sows,\x01",
            "this is a disaster for the Chancellor too.\x02\x03",
            "#07202FUh uh, could they be planning to,\x01",
            "unexpectedly, include me as a target too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07306F...That's no laughing matter, you know.\x02\x03",
            "#07301FAs expected, wouldn't it be better to increase\x01",
            "the 7th Division personnel numbers?\x02\x03",
            "It should be still possible to include some more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07204FNo, it won't be necessary.\x02\x03",
            "Chancellor aside, if someone like\x01",
            "me did something like that, it would\x01",
            "ruin the image I created of myself.\x02\x03",
            "#07202FAlso──\x02",
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
            "#11P#07209FI have you㈱\x02\x03",
            "#07212FIf you protected me between your arms, \x01",
            "that would be more than enough!\x02",
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
        "#11P#07303F──Well then, I'll go to sleep early too.\x02",
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
            "#11P#07206FSorry, I got carried away.\x02\x03",
            "#07200FIn any case, I'd like to talk to the \x01",
            "crown princess during tomorrow.\x02\x03",
            "How are the arrangements?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#6P#07304FYes, I have contacted the Captain.\x02\x03",
            "#07302FIt's going to be after tomorrow's \x01",
            "luncheon meeting, towards evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07202FI see...\x01",
            "Hu hu, I guess it's been a year?\x02\x03",
            "#07206FIf Estelle and the others were there,\x01",
            "we could've held a reunion, eh?\x02\x03",
            "#07208FSince Schera seems to be busy, it appears\x01",
            "she has no time for a business trip...\x02",
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
            "#11P#07204FWell, I'll allow myself to enjoy\x01",
            "the most advanced urban\x01",
            "resort at the utmost.\x02\x03",
            "#07212FOh, don't worry, because I've got no \x01",
            "intention of getting in the way of\x01",
            "your rendezvous with the Captain㈱\x02\x03",
            "#07209FIf you wish, what about going on\x01",
            "a date at the rumored theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07306F──It's none of your business, idiot.\x02\x03",
            "#07303FStill, it seems to me that you're spouting \x01",
            "more stupid nonsense than usual.\x02\x03",
            "#07301F...It's not that you're thinking\x01",
            "to do something bad, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#07211F*gulp*...\x02\x03",
            "#07209FHa ha ha, come'ooon.\x01",
            "Of course it's not that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P#07308F(...Should I put him a rope\x01",
            "around the neck tomorrow?)\x02",
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
            "──Well, this is probably going\x01",
            "to be my last foreign travel.\x02\x03",
            "Continuing to sound out what\x01",
            "the Chancellor is trying to do...\x02\x03",
            "Probing his movements across\x01",
            "the entire continent...\x02\x03",
            "I'm causing a lot of troubles to\x01",
            "you as usual, but I'm counting\x01",
            "on your support── my best friend.\x02",
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
        "#6P#07304FHmph, that goes without saying.\x02",
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
