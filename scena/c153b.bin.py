from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c153b.bin",                # FileName
        "c153b",                    # MapName
        "c153b",                    # Location
        0x00AE,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 174, 0, 0, 0, 1],
    )

    BuildStringList((
        "c153b",                  # 0
        "Mayor Dieter",           # 1
        "Chairman MacDowell",     # 2
        "Detective Dudley",       # 3
        "Commander Sonya",        # 4
        "Vice Commander Douglas", # 5
        "Chief Sergei",           # 6
        "Vice Chief Pierre",      # 7
        "Bureau Director?",       # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_190",          # 01, 1
        "Function_2_191",          # 02, 2
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_18F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_18F")

    Return()

    # Function_0_180 end

    def Function_1_190(): pass

    label("Function_1_190")

    Return()

    # Function_1_190 end

    def Function_2_191(): pass

    label("Function_2_191")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    LoadChrToIndex("chr/ch05802.itc", 0x1F)
    LoadChrToIndex("chr/ch05702.itc", 0x20)
    LoadChrToIndex("chr/ch44902.itc", 0x21)
    LoadChrToIndex("chr/ch06402.itc", 0x22)
    LoadChrToIndex("chr/ch02502.itc", 0x23)
    LoadChrToIndex("chr/ch00902.itc", 0x24)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 272800, 100, 6950, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 272800, 100, 4950, 270)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 269200, 100, 8950, 90)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 269200, 100, 6950, 90)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 269200, 100, 4950, 90)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 269200, 100, 2950, 90)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 269200, 100, 900, 90)
    OP_68(271500, -1100, 5950, 0)
    MoveCamera(90, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21000, 0)
    OP_68(271500, 900, 5950, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(271700, 800, 5950, 0)
    MoveCamera(36, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17630, 0)
    SetCameraDistance(16630, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#02503F#11PMy Goddess...\x02\x03",
            "#02501FI never thought one group\x01",
            "of jaegers could cause\x01",
            "something so appalling...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#02803FThere must be someone\x01",
            "behind all of this.\x02\x03",
            "#02801FThe same as with the\x01",
            "trade conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#01003FThe Erebonian Imperial\x01",
            "government...\x02\x03",
            "#01001FNo, to be specific, the\x01",
            ""Imperial Army\x01",
            "Intelligence Division".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#00606FI can't help but say it's highly\x01",
            "likely...\x02\x03",
            "#00601FEven in Crossbell, an intelligence\x01",
            "division officer kept in contact\x01",
            "with Red Constellation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PI-If it's like this, then do we\x01",
            "have any other choice but to beg\x01",
            "the Imperial government for mercy!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6POr otherwise, begging the\x01",
            "Republican government to\x01",
            "be our ally!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02803FWell, I already asked the Imperial\x01",
            "government earlier today.\x02\x03",
            "#02801FTheir reply was obvious. "We don't know\x01",
            "anything about it", they said.\x02\x03",
            "#02806FAnd, although this is my responsibility,\x01",
            "ever since the independence proposal, the\x01",
            "situation has been such that I cannot ask\x01",
            "for Republican assistance either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PN-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P...N-No! It's not your\x01",
            "fault at all, Mr. Mayor!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02503F#11PAt any rate... As things are, even as\x01",
            "the state government, we can only\x01",
            "issue a formal declaration of protest.\x02\x03",
            "#02500FStill... In any case, I'm worried\x01",
            "about the Mainz citizens' safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#02003F...After requesting a civilian\x01",
            "airship, we were able to confirm\x01",
            "the situation from the skies.\x02\x03",
            "#02001FAt present, there's no sign of\x01",
            "pillaging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHowever, the fact that the\x01",
            "Mainz citizens are being\x01",
            "held hostage hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm worried about their\x01",
            "food reserves. This can't\x01",
            "drag on for too long.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#11P#02803FOf course. Let's take\x01",
            "immediate\x01",
            "countermeasures.\x02\x03",
            "#02801F...How bad was the\x01",
            "damage to the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#02006FI have to say it was\x01",
            "enormous, in terms of both\x01",
            "personnel and material.\x02\x03",
            "#02001FAt present, all of our\x01",
            "spare assets are deployed\x01",
            "on the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#02806FI see...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02801F#5P─Our enemies are combat professionals,\x01",
            "but at the end of the day they're a\x01",
            "group that works for mira.\x02\x03",
            "Depending on how negotiations go, it's\x01",
            "we may be able to avoid any further\x01",
            "disaster.\x02\x03",
            "I want the police to look for such a\x01",
            "possibility and quell the citizens'\x01",
            "anxiety at the same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12P#00601FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PA-At once!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#01003FI guess I'll contact the\x01",
            "guild and try everything\x01",
            "we can...\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17130, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_191 end

    SaveToFile()

Try(main)
