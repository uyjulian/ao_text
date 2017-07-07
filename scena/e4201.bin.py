﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4201.bin",                # FileName
        "e4201",                    # MapName
        "e4201",                    # Location
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
        "e4201",                  # 0
        "Knight Cesar",           # 1
        "Adjunct Marcus",         # 2
        "Sister · Lease",       # 3
        "Father Kevin",             # 4
        "For APL display",              # 5
        "SE control",                 # 6
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(360, 0)                                        # 0

    ScpFunction((
        "Function_0_168",          # 00, 0
        "Function_1_178",          # 01, 1
        "Function_2_179",          # 02, 2
        "Function_3_873",          # 03, 3
        "Function_4_8F8",          # 04, 4
        "Function_5_959",          # 05, 5
        "Function_6_988",          # 06, 6
        "Function_7_9B2",          # 07, 7
        "Function_8_9D5",          # 08, 8
        "Function_9_9FF",          # 09, 9
        "Function_10_A72",         # 0A, 10
    ))


    def Function_0_168(): pass

    label("Function_0_168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_177")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_177")

    Return()

    # Function_0_168 end

    def Function_1_178(): pass

    label("Function_1_178")

    Return()

    # Function_1_178 end

    def Function_2_179(): pass

    label("Function_2_179")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch48400.itc", 0x20)
    LoadChrToIndex("apl/ch51728.itc", 0x21)
    SoundLoad(132)
    SoundLoad(868)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3000, 0, -13000, 180)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x1000)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2500, -500, -13000, 180)
    SetChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3500, 0, -13000, 180)
    SetChrFlags(0xA, 0x8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2250, 0, -2600, 0)
    BeginChrThread(0x8, 0, 0, 3)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 14750, 0, -2380, 315)
    BeginChrThread(0x9, 0, 0, 4)
    Sound(132, 2, 60, 0)
    Sound(868, 2, 40, 0)
    BeginChrThread(0xD, 1, 0, 9)
    OP_68(-87080, 3400, 29630, 0)
    MoveCamera(322, 4, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(77770, 0)
    FadeToBright(1000, 0)
    OP_68(-87080, 3400, 29630, 4500)
    MoveCamera(324, 7, 0, 4500)
    OP_6E(500, 4500)
    SetCameraDistance(67500, 4500)
    Sleep(4400)
    OP_68(-89870, 1500, 33150, 0)
    MoveCamera(22, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(47450, 0)
    Fade(500)
    SetCameraDistance(40450, 3500)
    Sleep(1000)
    BeginChrThread(0xD, 2, 0, 10)
    Sleep(2000)
    Sleep(1000)
    OP_68(1230, 1500, 6790, 10000)
    MoveCamera(328, 14, 0, 10000)
    OP_6E(500, 10000)
    SetCameraDistance(47040, 10000)
    OP_6F(0x79)
    PlayBGM("ed7574", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(3000, 1130, -13000, 0)
    MoveCamera(311, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    Fade(500)
    OP_68(3000, 1002, -13000, 25000)
    MoveCamera(321, 12, 0, 25000)
    OP_6E(500, 25000)
    SetCameraDistance(17500, 25000)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#04306F#6P#40W……… Hokkaido …………\x02\x03",
            "#04310F…… Battle duty is\x01",
            "Was it impolite truly ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13811F#11P……what goes around comes around.\x02\x03",
            "#13806FIn the real world \"Stigmata#4RStigma#The power of\x01",
            "I do not want to release it over there ……\x02\x03",
            "#13801FIf my sister were there,\x01",
            "I think he got angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04306F#6P#30WNo good …… Also to the president\x01",
            "Meguro is likely to be scolded … …\x02\x03",
            "#04308FYou also destroy Mercapa …\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3000, 1400, -13000, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    MoveCamera(3, 3, 0, 0)
    Fade(500)
    BeginChrThread(0xB, 0, 0, 5)
    OP_0D()
    BeginChrThread(0xC, 0, 0, 6)
    WaitChrThread(0xC, 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#04303F#6P#30WHaa … when it comes to repair impossible\x01",
            "I guess I'm going to be a guardian knight … …?\x02\x03",
            "#04300FWell, once that happens,\x01",
            "Do you want to get back from the rookie?\x02\x03",
            "#04304FIf you become a regular knight\x01",
            "Even if it comes with support … well …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#13812F#11P……fool.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 7)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xB,
        "#04305F#5P#30WOya … Hey …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13813F#11P#30W……Was good……\x01",
            "……… It's really safe ………\x02\x03",
            "The place my sister was aiming for was\x01",
            "I still have been a long time ago ……\x02\x03",
            "#13812FReally … … to be unreasonable ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04308F#5P#30Wlease……\x02\x03",
            "#04304F… …. Sorry ….\x01",
            "Is there still a long way to go …?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3030, 1360, -14200, 12000)
    SetCameraDistance(16000, 12000)
    MoveCamera(358, 15, 0, 12000)
    BeginChrThread(0xC, 0, 0, 8)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0xB,
        (
            "#04303F#5P#30W…… From now on\x01",
            "To be amazed\x01",
            "There may be something … …\x02\x03",
            "#04300FWill you support without discernment …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#13814F#11P#30W… … Naturally …\x01",
            "It can not be left alone … …\x02",
        )
    )

    CloseMessageWindow()
    StopSound(132, 1000, 50)
    StopSound(868, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4213", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_179 end

    def Function_3_873(): pass

    label("Function_3_873")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F7")
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x3E8, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x5A, 0x3E8, 0x3E8, 0x0)
    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x10E, 0x3E8, 0x3E8, 0x0)
    Sleep(2000)
    OP_9B(0x0, 0xFE, 0x10E, 0xDAC, 0x3E8, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    Jump("Function_3_873")

    label("loc_8F7")

    Return()

    # Function_3_873 end

    def Function_4_8F8(): pass

    label("Function_4_8F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_958")
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(1000)
    OP_9B(0x1, 0xFE, 0x5A, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(700)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(1000)
    OP_9B(0x1, 0xFE, 0x10E, 0x3E8, 0x3E8, 0x0)
    Jump("Function_4_8F8")

    label("loc_958")

    Return()

    # Function_4_8F8 end

    def Function_5_959(): pass

    label("Function_5_959")

    OP_68(3030, 1660, -14200, 25000)
    MoveCamera(359, 12, 0, 25000)
    OP_6E(500, 15000)
    SetCameraDistance(20000, 19000)
    Return()

    # Function_5_959 end

    def Function_6_988(): pass

    label("Function_6_988")

    Sound(812, 0, 100, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(450)
    Return()

    # Function_6_988 end

    def Function_7_9B2(): pass

    label("Function_7_9B2")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x5)
    Sleep(150)
    SetChrSubChip(0xFE, 0x6)
    Sleep(150)
    SetChrSubChip(0xFE, 0x7)
    Sleep(450)
    Return()

    # Function_7_9B2 end

    def Function_8_9D5(): pass

    label("Function_8_9D5")

    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x8)
    Sleep(150)
    SetChrSubChip(0xFE, 0x9)
    Sleep(150)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(450)
    Return()

    # Function_8_9D5 end

    def Function_9_9FF(): pass

    label("Function_9_9FF")

    Sound(203, 0, 25, 0)
    Sleep(900)
    Sound(203, 0, 25, 0)
    Sleep(600)
    Sound(887, 0, 15, 0)
    Sleep(500)
    Sound(203, 0, 25, 0)
    Sleep(900)
    Sound(203, 0, 20, 0)
    Sleep(600)
    Sound(887, 0, 15, 0)
    Sleep(500)
    Sound(203, 0, 20, 0)
    Sleep(900)
    Sound(203, 0, 15, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 10, 0)
    Sleep(900)
    Sound(203, 0, 10, 0)
    Sleep(600)
    Sound(887, 0, 10, 0)
    Sleep(500)
    Sound(203, 0, 5, 0)
    Return()

    # Function_9_9FF end

    def Function_10_A72(): pass

    label("Function_10_A72")

    OP_25(0x364, 0x23)
    Sleep(200)
    OP_25(0x364, 0x1E)
    Sleep(200)
    OP_25(0x364, 0x19)
    Sleep(200)
    OP_25(0x364, 0x14)
    Return()

    # Function_10_A72 end

    SaveToFile()

Try(main)
