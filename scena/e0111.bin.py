from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0111.bin",                # FileName
        "e0111",                    # MapName
        "e0111",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0111",                  # 0
        "Shirley",                # 1
        "Jaeger Gareth",          # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(220, 0)                                        # 0

    ScpFunction((
        "Function_0_DC",           # 00, 0
        "Function_1_EC",           # 01, 1
        "Function_2_ED",           # 02, 2
        "Function_3_112",          # 03, 3
    ))


    def Function_0_DC(): pass

    label("Function_0_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)

    label("loc_EB")

    Return()

    # Function_0_DC end

    def Function_1_EC(): pass

    label("Function_1_EC")

    Return()

    # Function_1_EC end

    def Function_2_ED(): pass

    label("Function_2_ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_111")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_2_ED")

    label("loc_111")

    Return()

    # Function_2_ED end

    def Function_3_112(): pass

    label("Function_3_112")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51201.itc", 0x1E)
    LoadChrToIndex("apl/ch51261.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    SoundLoad(460)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 52800, 100, -200, 270)
    SetChrPos(0x104, 52100, 200, 350, 180)
    SetChrPos(0x105, 52800, 100, -1100, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 50400, 150, 350, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 47800, 100, 700, 0)
    BeginChrThread(0x101, 3, 0, 2)
    OP_68(44700, 1100, 0, 0)
    MoveCamera(319, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17100, 0)
    Sound(460, 2, 100, 0)
    OP_68(50700, 1100, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(2428, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe, gorgeous indeed.\x02\x03",
            "Do jaegers really make\x01",
            "this much?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#04600F#5PHmm, maybe we're special?\x02\x03",
            "#04604FWe have a lot of aristocrats and influential\x01",
            "nobles as regular customers. It's normal to\x01",
            "get around a million mira from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10305FWhoo♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FThat much...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWhen you employ top-class\x01",
            "jaegers, you even pay a retainer.\x02\x03",
            "#00301FTheir weapons are only the latest\x01",
            "models, of course. Are you guys\x01",
            "gonna get an airship soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04604F#5PAhaha, not yet.\x02\x03",
            "#04602FLiberlian warships are good in\x01",
            "terms of strength but don't appear\x01",
            "on the black market that often.\x02\x03",
            "#04609FWell, if needed, we could\x01",
            "infiltrate and steal one, though.♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00008F(...She's kidding,\x01",
            "right?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Well, let's just leave\x01",
            "it at that.)\x02",
        )
    )

    CloseMessageWindow()
    StopSound(460, 2000, 100)
    OP_68(53000, 1100, 0, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_112 end

    SaveToFile()

Try(main)
