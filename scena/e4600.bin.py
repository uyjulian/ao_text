from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4600.bin",                # FileName
        "e4600",                    # MapName
        "e4600",                    # Location
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
        "e4600",                  # 0
        "Campanella The Fool",    # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CC",           # 01, 1
        "Function_2_CD",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_CB")

    Return()

    # Function_0_BC end

    def Function_1_CC(): pass

    label("Function_1_CC")

    Return()

    # Function_1_CC end

    def Function_2_CD(): pass

    label("Function_2_CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadEffect(0x0, "event/ev14000.eff")
    SoundLoad(3885)
    SoundLoad(3886)
    SoundLoad(969)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -3000, 0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFrame(0x1, "piller", 0x2, "loop")
    SetMapObjFrame(0x1, "model4", 0x2, "loop")
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "piller", 0x2, "loop")
    SetMapObjFrame(0x6, "model4", 0x2, "loop")
    SetMapObjFlags(0x7, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_F3(100000)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W─I see. It looks like\x01",
            "it's proceeding well.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7580", 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3800, 12000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -10000, 3800, -8000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_68(-330, 2000, -1650, 0)
    MoveCamera(304, 29, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(18000, 5000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(1000)
    Fade(500)
    OP_68(0, 7250, 0, 0)
    MoveCamera(0, -10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(31150, 0)
    OP_68(0, 10900, 0, 0)
    MoveCamera(358, -9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24310, 0)
    OP_68(0, 7250, 0, 8000)
    MoveCamera(0, -5, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(20150, 8000)
    PlaceName2(340, 200, "c_plac64", 0x0, 2000)
    OP_6F(0x79)
    Fade(500)
    OP_93(0x8, 0x13B, 0x0)
    OP_68(-5610, 2000, -2300, 0)
    MoveCamera(8, 4, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19600, 0)
    MoveCamera(359, 4, 0, 30000)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("6th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, our preparations\x01",
            "are around 90% complete.\x02\x03",
            "We'll probably be done\x01",
            "with this order on time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("1st Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Good work, Doctor.\x02\x03",
            "─Campanella. What are\x01",
            "our Enforcers doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    ChrTalk(
        0x8,
        (
            "#04804F#12PIt seems that Bleublanc was playing\x01",
            "around until a little while ago, but\x01",
            "it seems he has already pulled out.\x02\x03",
            "#04800FRenne has left for Liberl and shows\x01",
            "no sign of returning.\x02\x03",
            "#04806FAnd about "her"... Well, it's fine\x01",
            "if we just wait and see, right?\x02\x03",
            "#04802FShe lent me some shikigami, but it\x01",
            "seems she has no intention of\x01",
            "intervening at present.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("1st Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm, understood.\x02\x03",
            "Let them do as they\x01",
            "please, the same as with\x01",
            "the meister.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("6th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Still, giving the Enforcers\x01",
            "complete freedom of action...\x02\x03",
            "Although it's something that\x01",
            "person decided, it's a rather\x01",
            "irrational Rule, isn't it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("1st Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everything is as the Grandmaster\x01",
            "wishes. There is no need to\x01",
            "question if it's right or wrong.\x02\x03",
            "More importantly─ It seems she\x01",
            "has arrived.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("6th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, you've come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_93(0x8, 0x87, 0x1F4)

    ChrTalk(
        0x8,
        "#04809F#5PHehe, right on time.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(10000, -1000, -8000, 0)
    MoveCamera(100, 80, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    OP_68(10000, 2500, -8000, 5000)
    MoveCamera(97, 12, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(18000, 5000)
    Sound(969, 2, 100, 0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "piller", 0x2, "up")
    SetMapObjFrame(0x7, "model4", 0x2, "up")
    Sleep(5000)
    StopSound(969, 1000, 100)
    Sleep(1000)
    Sound(970, 0, 100, 0)
    SetMapObjFrame(0x7, "piller", 0x2, "open")
    SetMapObjFrame(0x7, "model4", 0x2, "open")
    SetCameraDistance(16000, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(300)
    SetMapObjFrame(0x7, "model4", 0x2, "loop")
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10000, 3800, -8000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sleep(500)
    OP_6F(0x79)
    CancelBlur(1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(235, 130, -1, -1)
    SetChrName("7th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3885V#40W─I am sorry to have kept\x01",
            "you waiting.\x02\x03",
            "#3886VIt looks like you have\x01",
            "already started...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF2E)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("1st Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, we just started.\x02\x03",
            "About that matter, has\x01",
            "it been taken care of?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 130, -1, -1)
    SetChrName("7th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes. The rest has been\x01",
            "entirely left to the\x01",
            "Sinner.\x02\x03",
            "And─ Crossbell, was it?\x02\x03",
            "I have not set foot in\x01",
            "that land for a long\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#6P#NUhuhu. It's changed so\x01",
            "much, you'll be amazed,\x01",
            "you know?\x02\x03",
            "#04800FIt is probably the most\x01",
            "advanced metropolis of the\x01",
            "present orbal culture.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 170, -1, -1)
    SetChrName("6th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I intend to go see it\x01",
            "once more before its\x01",
            "completion.\x02\x03",
            "What do you say? Since\x01",
            "it's a rare occasion,\x01",
            "shall we meet up there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 130, -1, -1)
    SetChrName("7th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, I have no\x01",
            "objections.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_93(0x8, 0x0, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(310, 5500, -5790, 0)
    MoveCamera(359, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(25500, 1500)
    OP_6F(0x79)
    CancelBlur(1000)
    SetCameraDistance(23500, 50000)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("1st Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Then, I leave all further\x01",
            "details to the both of you.\x02\x03",
            "The "Phantasmal Blaze\x01",
            "Plan"... It is a crucial step\x01",
            "for that person's final plan.\x02\x03",
            "Can I count on you for the\x01",
            "preparations for its first\x01",
            "phase?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(0, 170, -1, -1)
    SetChrName("6th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe, understood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 170, -1, -1)
    SetChrName("7th Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everything is for the\x01",
            "Grandmaster.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(23500, 2500)
    FadeToDark(2500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x1388)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CD end

    SaveToFile()

Try(main)
