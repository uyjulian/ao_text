from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000_1.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [88, 720921, 0, -16777216, 11796682, 28573696, 256, 16777216, 256, 0, 0, 256, -65280, 1660944639, 1936291423, 12336, 11831, 29801, 112, 202, 1, 0, 0],
    )

    BuildStringList((
        "c1000_1",                # 0
    ))

    ChipFrameInfo(88, 0)                                         # 0

    ScpFunction((
        "Function_0_58",           # 00, 0
    ))


    def Function_0_58(): pass

    label("Function_0_58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis232.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis233.itp")
    SoundLoad(803)
    SoundLoad(2711)
    SoundLoad(2712)
    Sleep(500)
    Sound(803, 2, 100, 0)
    Sleep(1600)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_25(0x80, 0x28)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00005FSpecial Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2711V#30WHello, Lloyd!\x02\x03",
            "#2712V#30WGood work in the rain,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA98)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FOh, Fran.\x02\x03",
            "#00000FWhat's wrong? An urgent\x01",
            "request?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Umm, well...\x02\x03",
            "Do you remember Mayor\x01",
            "Bickson of Mainz?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FYeah, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F...Did something happen\x01",
            "up at the mining town?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, it seems monsters\x01",
            "have appeared in the\x01",
            "mine...\x02\x03",
            "Though, they appeared in\x01",
            "the old mine a little\x01",
            "ways from town.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F...?\x02\x03",
            "#00001FI'm pretty sure it isn't\x01",
            "strange for monsters to show\x01",
            "up in a place like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, apparently, all of\x01",
            "the miners are unhurt.\x02\x03",
            "It's just, it appears\x01",
            "that something strange is\x01",
            "going on inside...\x02\x03",
            "Mayor Bickson is asking\x01",
            "if you could investigate,\x01",
            "just to be safe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FSomething strange... That's\x01",
            "rather nonspecific.\x02\x03",
            "#00000F─Understood. Our urgent requests\x01",
            "in the city are finished, so\x01",
            "we'll head for Mainz.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, please do!\x02\x03",
            "Ah, there's another thing I need\x01",
            "to tell you: A wanted monster was\x01",
            "spotted on Mainz Mountain Path.\x02\x03",
            "Please deal with it if you have\x01",
            "extra time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002FI see, understood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Also, unlike Crossbell\x01",
            "City, there's clear skies\x01",
            "on Mainz Mountain Path.\x02\x03",
            "Since you have a car, how\x01",
            "about going there using\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004FThat's right...\x01",
            "Understood.\x02\x03",
            "#00000FThanks Fran. Contact us\x01",
            "again if anything\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes, well goodbye, then.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(800)
    SetMessageWindowPos(240, 110, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10105FThat was Fran, wasn't\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 40, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00101FSomething happened\x01",
            "around Mainz?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006FYeah, something strange occurred\x01",
            "at the old mine.\x02\x03",
            "#00000FWe took care of the support\x01",
            "requests in the city, so let's go\x01",
            "there once we're ready.\x02\x03",
            "#00002FOh yeah, there's clear weather on\x01",
            "the mountain path now, so I think\x01",
            "we should go using our car.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 30, -1, -1)

    AnonymousTalk(
        0x105,
        "#10304FRoger, leader.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10100FIf we're going by car,\x01",
            "let's head to the Support\x01",
            "Section rear entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A new wanted monster was added\x01",
            "to the Detective Notebook and\x01",
            "Support Section terminal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6D, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x12)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x128, 7)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_25(0x80, 0x64)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_0_58 end

    SaveToFile()

Try(main)
