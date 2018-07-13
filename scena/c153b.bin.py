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
            "#02501FI'd never thought one group of jaegers\x01",
            "could cause such a monstrous thing...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#02803F...No doubt that someone\x01",
            "is behind this.\x02\x03",
            "#02801FAlso, at the same time of the Trade Conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#01003FThe Erebonian Imperial government...\x02\x03",
            "#01001FNo, daring to be specific, the\x01",
            ""Imperial Army Intelligence Division"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#00606FI can state that that possibility\x01",
            "is very high...\x02\x03",
            "#00601FEven in Crossbell, an intelligence\x01",
            "bureau officer exchanged messages\x01",
            "frequently with the "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PB-Being this the situation, we\x01",
            "can only beg the Imperial\x01",
            "government for mercy, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6POr otherwise, begging the Republican\x01",
            "government to become our ally...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02803FWell, with the occasion, during the day\x01",
            "I already inquired the Imperial government.\x02\x03",
            "#02801FI knew their obvious reply...\x01",
            ""We don't know anything about it", it was.\x02\x03",
            "#02806F...Also, this is my responsibility. After the \x01",
            "independence proposal, I am not in a situation \x01",
            "I can ask the Republican government to aid us.\x02",
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
            "#6P...N-No!\x01",
            "It's not the mayor's fault at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02503F#11PAt any rate... In this situation, even as\x01",
            "the autonomous state government, we can\x01",
            "only issue a formal protest declaration.\x02\x03",
            "#02500FStill... In any case, I'm worried\x01",
            "about Mainz citizens' safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#02003F...After requesting a civilian airliner, we could\x01",
            "somehow check the situation from the skies.\x02\x03",
            "#02001FAt present, pillaging acts and similars\x01",
            "appear to have not occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHowever, Mainz citizens\x01",
            "are hostages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm worried for their emergency food.\x01",
            "We can't dilly-dally.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#11P#02803FOf course, let's take immediate countermeasures.\x02\x03",
            "#02801F...At what level was the CGF damage?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#02006F...I have to say it was very great,\x01",
            "humanly and materially.\x02\x03",
            "#02001FAt present, we are fully deployed\x01",
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
            "#02801F#5P──Our enemies are war professionals,\x01",
            "but after all they're a mira employed group.\x02\x03",
            "According to negotiations, it's also possible that\x01",
            "we can hold back a bigger disaster than this.\x02\x03",
            "I want the members of the police to\x01",
            "look for such a possibility and, at the\x01",
            "same time, to quell the citizens' anxiety.\x02",
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
            "#6P#01003FI guess I'll contact the Guild too\x01",
            "and try all possible means...\x02",
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
