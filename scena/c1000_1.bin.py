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
            "#00005FYes, Special Support Section,\x01",
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
            "#2711V#30WHello, Mr. Lloooyd!\x02\x03",
            "#2712V#30WThank you for your hard work in the raaain.\x02",
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
            "#00002FAh, Fran?\x02\x03",
            "#00000FIs something wrong?\x01",
            "Has an urgent request come in?\x02",
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
            "Ehm, well...\x02\x03",
            "Do you remember Mainz\x01",
            "Town Mayor, Bickson?\x02",
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
            "#00001F...Could it be that something has\x01",
            "happened at the mining town?\x02",
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
            "Yes, it appears that monsters\x01",
            "showed up inside the mine...\x02\x03",
            "Ah, however, it seems it's\x01",
            "an old mine located a little\x01",
            "far away from the town.\x02",
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
            "#00001FI don't think it's strange for monsters\x01",
            "to appear in such a place...\x02",
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
            "Yes, and it's not that any harm\x01",
            "came to the miners too.\x02\x03",
            "It's just that it appears that something\x01",
            "very strange is happening inside...\x02\x03",
            "To sum it up, he asks if you\x01",
            "could investigate just in case.\x02",
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
            "#00003FSomething very strange...\x01",
            "That's a bit incomprehensible.\x02\x03",
            "#00000F──All right.\x01",
            "We took care of the urgent requests in the\x01",
            "city, so we'll head to Mainz from now on.\x02",
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
            "Yes, pleeease.\x02\x03",
            "Ah, I'm taking the opportunity to also tell\x01",
            "you that, just before, a Wanted Monster\x01",
            "request appeared for Mainz Mountain Path.\x02\x03",
            "Please deal with it if you\x01",
            "have time on your hands.\x02",
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
            "Also, unlike Crossbell City, it appears that\x01",
            "there's a clear sky on Mainz Mountain Path.\x02\x03",
            "Since you can, why not going\x01",
            "there with your orbal car?\x02",
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
            "#00004FIs that so? Got it.\x02\x03",
            "#00000FThank you, Fran.\x01",
            "If something comes up, contact us again.\x02",
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
            "Yes, then excuse meee.\x07\x00\x02",
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
        "#10105FIt seemed from Fran.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 40, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00101FIt seems something has\x01",
            "happened in the Mainz region?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006FYeah, in an old mine it seems\x01",
            "something strange is going on.\x02\x03",
            "#00000FWe have cleared the support requests inside\x01",
            "the city, so let's go after we're prepared.\x02\x03",
            "#00002FOh, since it appears the weather is clear \x01",
            "over there, we could go with the car.\x02",
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
            "#10100FIf we're going to the mining town with the car,\x01",
            "then let's go to the Support Section back \x01",
            "entrance.\x02",
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
            "A new Wanted Monster was added to the Detective\x01",
            "Notebook and the Support Section terminal.\x07\x00\x02",
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
