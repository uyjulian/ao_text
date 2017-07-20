from ScenarioHelper import *

def main():
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
        "Mayor of Dieter",         # 1
        "McDowell",         # 2
        "Dudley investigator",         # 3
        "Sonya Command",           # 4
        "Douglas deputy command",         # 5
        "Sergey Manager",           # 6
        "Pierre deputy director",         # 7
        "Director-General",                 # 8
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
            "#02503F#11PWhat a thing to happen…\x02\x03",
            "#02501FNo way it was a big deal this far\x01",
            "It is said that a solitary warrior causes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P#02803F…… There is something behind us\x01",
            "There is no mistake.\x02\x03",
            "#02801FIt's just like with the trade conference\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#01003FThe Erebonia government\x02\x03",
            "#01001FNo, if you dare to identify it\x01",
            "Is it \"Imperial Army Information Bureau\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12P#00606FIf the possibility is high\x01",
            "I can not help but say …\x02\x03",
            "#00601FEven with this crossbell\x01",
            "The officer of the information department \"red constellation\"\x01",
            "I kept in touch frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PHere it is,\x01",
            "Only trying to cry on the Imperial Government\x01",
            "I do not think so! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6POr ask the Republic Government\x01",
            "Or getting to be on your side … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02803FNo, already in the daytime\x01",
            "I am inquiring the Imperial Government.\x02\x03",
            "#02801FNaturally you will reply …\x01",
            "It was \"I do not remember\".\x02\x03",
            "#02806F…… And this is my responsibility\x01",
            "Since Independent Recommendation, the Republic Government also\x01",
            "I am not in a situation to ask for cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PN-no way\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6P……No!\x01",
            "Never the mayor's responsibility!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02503F#11PEither way …\x01",
            "As it is, as autonomous state government\x01",
            "There is no choice but to issue a formal protest statement.\x02\x03",
            "#02500FBut … anyway\x01",
            "I am concerned about the safety of Mainz residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#02003F… … Ask a private flying boat\x01",
            "I managed to confirm from the sky somehow.\x02\x03",
            "#02001FAt the present time, acts such as looting\x01",
            "There is no indication of being done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PHowever, residents of Mainz,\x01",
            "The situation of being a hostage does not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI am worried about stockpiling of food,\x01",
            "I can not do gozugu.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#11P#02803FWe will of course plan a counterattack right away\x02\x03",
            "#02801F…… The damage of the guard\x01",
            "How much was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#6P#02006F…… both human and physical damage\x01",
            "I can not help being said to be enormous.\x02\x03",
            "#02001FCurrently, all of the reserve strength\x01",
            "It is a situation that is developing on the mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#02806FI see…\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#02801F#5P── The opponent is a battle pro\x01",
            "It is a group hired by Mira to the last.\x02\x03",
            "Depending on the negotiations, more disasters\x01",
            "There is also the possibility of being stopped.\x02\x03",
            "To the police,\x01",
            "At the same time as we suppress civic unrest\x01",
            "I also want you to explore the possibilities around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#12P#00601FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PAt once!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#01003FAlso contact the guild\x01",
            "Do you want to try your hand …?\x02",
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
