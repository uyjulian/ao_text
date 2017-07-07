from ScenarioHelper import *

def main():
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
        "Clown Campanella",     # 1
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
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W─ ─ I see.\x01",
            "It seems quite smooth.\x02",
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
    SetChrName("The sixth pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, the preparation here too\x01",
            "There was a prospect of 90.\x02\x03",
            "In this order\x01",
            "I will manage in time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("First pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Good job, doctor.\x02\x03",
            "── Campanella.\x01",
            "\"Enforcer#6RLegion#\"What's their move?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    ChrTalk(
        0x8,
        (
            "#04804F#12PA while ago Bull Blanc\x01",
            "It seems I was playing,\x01",
            "It looks like I pulled out my hands already.\x02\x03",
            "#04800FAfter Ren left to Libert\x01",
            "There is no sign of returning.\x02\x03",
            "#04806FAnd about \"her\" …\x01",
            "Well, is not it good to see?\x02\x03",
            "#04802FThe expression god lent me,\x01",
            "For the moment I intend to intervene\x01",
            "It seems nothing at all.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("First pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm, I understand.\x02\x03",
            "Like Meister,\x01",
            "Please leave it to their will.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("The sixth pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But \"enforcer\"\x01",
            "Do you give all the freedom of action …?\x02\x03",
            "Despite what he decided,\x01",
            "It is somewhat unreasonable \"rule\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("First pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everything is an \"owner\" 's thought …\x01",
            "There is no need to ask anything.\x02\x03",
            "More than that ──\x01",
            "You seem to have come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("The sixth pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, did you come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_93(0x8, 0x87, 0x1F4)

    ChrTalk(
        0x8,
        "#04809F#5PHuh, it's on time.\x02",
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
    SetChrName("The seventh pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3885V#40W── We kept you waiting.\x02\x03",
            "#3886VIt seems you are already starting.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF2E)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("First pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, I just started.\x02\x03",
            "About the case of example\x01",
            "Are you sure?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 130, -1, -1)
    SetChrName("The seventh pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, afterwards to \"Catch\"\x01",
            "I left everything to you.\x02\x03",
            "So then\x01",
            "It was \"crossbell\".\x02\x03",
            "To go to this place is\x01",
            "I also have not seen for a long time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#04804F#6P#NUhufu, like so much change\x01",
            "Do not you make your eyes round?\x02\x03",
            "#04800FIn modern power civilization\x01",
            "It will be a state-of-the-art big city.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 170, -1, -1)
    SetChrName("The sixth pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Again before I completed it again,\x01",
            "I am going to look out.\x02\x03",
            "Please do not worry\x01",
            "Shall we meet in the field?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 130, -1, -1)
    SetChrName("The seventh pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, there is no objection.\x02",
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
    SetChrName("First pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Then, you two.\x01",
            "After that we will leave the restriction.\x02\x03",
            "\"Phantomhurgh#4RNuclear power plant#plan\"……\x01",
            "For his final plan\x01",
            "It is an indispensable step.\x02\x03",
            "A mechanism as a first step,\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(0, 170, -1, -1)
    SetChrName("The sixth pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, I understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 170, -1, -1)
    SetChrName("The seventh pillar")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Everything is for the \"owner\".\x02",
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
