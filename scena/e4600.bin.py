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
            "#30W──I see. \x01",
            "It looks like it's proceeding well.\x02",
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
            "Yeah, our preparations should\x01",
            "be at around 90%.\x02\x03",
            "We'll probably be able to\x01",
            "make it in time for this order.\x02",
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
            "Good job, Doctor.\x02\x03",
            "──Campanella.\x01",
            "What about the "Enforcers" moves?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    ChrTalk(
        0x8,
        (
            "#04804F#12PIt seems that Bleublanc was \x01",
            "playing until a little while ago,\x01",
            "but it seems he already pulled out.\x02\x03",
            "#04800FRenne has left Liberl and it\x01",
            "seems she has not returned.\x02\x03",
            "#04806FAnd about "her"...\x01",
            "Well, is it fine if she just wait and see?\x02\x03",
            "#04802FShe lent me some bound spirits,\x01",
            "but it seems she has no intention\x01",
            "to intervene at all for now.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("1st Anguis")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hm, I understand.\x02\x03",
            "Like with the Meister, let\x01",
            "them do as they please.\x02",
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
            "Still, giving the "Enforcers"\x01",
            "entire movement liberty...\x02\x03",
            "Although it's something that person decided, \x01",
            "it's a somewhat irrational "rule", hm?\x02",
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
            "Everything is to the "Grandmaster"'s likings...\x01",
            "There is no need to question if it's right or wrong.\x02\x03",
            "More importantly──\x01",
            "It seems she has arrived.\x02",
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
        "#04809F#5PUh uh, just in time.\x02",
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
            "#3885V#40W──I am sorry to have kept you waiting.\x02\x03",
            "#3886VIt looks like you have already started...\x02",
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
            "No, we have started just now.\x02\x03",
            "About that matter,\x01",
            "is it already fine?\x02",
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
            "Yes, I left everything else\x01",
            "to the "sinful" sir.\x02\x03",
            "Also──\x01",
            "That was "Crossbell", right?\x02\x03",
            "It has been some time since\x01",
            "I went to that land too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#6P#NUhuhu, it has changed so\x01",
            "much to be left amazed, right?\x02\x03",
            "#04800FIt is probably the most advanced\x01",
            "metropolis of the present orbal culture.\x02",
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
            "Before it's completed, I too \x01",
            "intend to go see it once more.\x02\x03",
            "What do you say, since it's a rare\x01",
            "occasion, why not meeting there?\x02",
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
            "Yes, I have no objections.\x02",
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
            "──Then, I leave the hereafter\x01",
            "details to you both.\x02\x03",
            "The "Phantasmal Blaze Plan"...\x01",
            "It is an essential step\x01",
            "to that person's final plan...\x02\x03",
            "Please, take care of it as\x01",
            "the first stage of the scheme.\x02",
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
            "Uh uh, understood.\x02",
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
            "Everything is for the "Grandmaster".\x02",
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
