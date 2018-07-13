from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1200.bin",                # FileName
        "c1200",                    # MapName
        "c1200",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1200", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x07',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 2000, 0, 0, 0, 0, 1, 26, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1200",                  # 0
        "Cunha",                  # 1
        "Hauser",                 # 2
        "Bishop",                 # 3
        "Old Man Quine",          # 4
        "Amisaah",                # 5
        "Nikol",                  # 6
        "Celine",                 # 7
        "Michey",                 # 8
        "M. W. L. Staff",         # 9
        "M. W. L. Staff",         # 10
        "Citizen",                # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Citizen",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Mechanic",               # 17
        "Roy",                    # 18
        "Meiling",                # 19
        "Zeit",                   # 20
        "KeA",                    # 21
        "Shizuku",                # 22
        "Tourist",                # 23
        "Boy",                    # 24
        "Citizen",                # 25
        "Section Chief Joe Ridge",# 26
        "Policeman",              # 27
        "Policeman",              # 28
        "Water Bus Guide",        # 29
        "Patrol Car",             # 30
        "Nielsen",                # 31
        "Cao",                    # 32
        "Lau",                    # 33
        "Yuri",                   # 34
        "Sykes",                  # 35
        "Reggie",                 # 36
        "暴走車",                 # 37
        "Patrol Car",             # 38
        "水上バス",               # 39
        "SE制御",                 # 40
        "Clyde",                  # 41
        "Young Man",              # 42
        "車",                     # 43
        "ボート",                 # 44
        "Olivier",                # 45
        "Central Square",         # 46
        "West Street",            # 47
        "Governmental District",  # 48
        "Residential Street",     # 49
        "Entertainment District", # 50
        "East Street",            # 51
        "Downtown",               # 52
        "Waterfront Area",        # 53
        "IBC",                    # 54
        "Station Street",         # 55
        "Back Street",            # 56
        "St. Ursula Byroad",      # 57
        "East Crossbell Highway", # 58
        "West Crossbell HIghway", # 59
        "Mainz Mountain Road",    # 60
        "Orchis Tower",           # 61
    ))

    AddCharChip((
        "chr/ch26000.itc",                   # 00
        "chr/ch49600.itc",                   # 01
        "chr/ch49700.itc",                   # 02
        "chr/ch10200.itc",                   # 03
        "chr/ch44500.itc",                   # 04
        "chr/ch44600.itc",                   # 05
        "chr/ch23000.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch20300.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch20500.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch25200.itc",                   # 0C
        "chr/ch26000.itc",                   # 0D
        "apl/ch50168.itc",                   # 0E
        "chr/ch21500.itc",                   # 0F
        "chr/ch28900.itc",                   # 10
        "chr/ch29100.itc",                   # 11
        "chr/ch24000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch21902.itc",                   # 14
        "chr/ch22200.itc",                   # 15
        "chr/ch49500.itc",                   # 16
        "chr/ch49100.itc",                   # 17
        "chr/ch02707.itc",                   # 18
        "chr/ch08200.itc",                   # 19
        "chr/ch08700.itc",                   # 1A
        "chr/ch30100.itc",                   # 1B
        "chr/ch30000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "chr/ch00000.itc",                   # 1E
        "chr/ch00000.itc",                   # 1F
        "chr/ch00000.itc",                   # 20
        "chr/ch46500.itc",                   # 21
        "apl/ch51272.itc",                   # 22
        "chr/ch21900.itc",                   # 23
        "chr/ch26600.itc",                   # 24
        "chr/ch45102.itc",                   # 25
    ))

    DeclNpc(4294954097, 0,       11500,   90,   257,  0x0, 0,   11,  0,   0,   1,   0,   11,  255,  0)
    DeclNpc(4294956826, 0,       13340,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294914826, 2000,    21149,   90,   257,  0x0, 0,   13,  0,   0,   2,   0,   13,  255,  0)
    DeclNpc(39669,   4294964796, 4294947917, 180,  257,  0x0, 0,   18,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(38439,   4294964806, 4294949217, 135,  257,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294949296, 0,       4294961546, 90,   385,  0x0, 0,   16,  0,   0,   4,   0,   18,  255,  0)
    DeclNpc(13000,   0,       4294957296, 0,    385,  0x0, 0,   17,  0,   0,   5,   0,   19,  255,  0)
    DeclNpc(9479,    4294966597, 159,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(6550,    4294966597, 4294964937, 315,  389,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5989,    4294966597, 2119,    225,  389,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4449,    4294966597, 4294966486, 90,   389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(4940,    4294966597, 4294965096, 90,   389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(3809,    4294966597, 4294963927, 45,   389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(39900,   4294964796, 3650,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4190,    4294966597, 1529,    135,  389,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(3809,    4294966597, 250,     90,   389,  0x0, 0,   10,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(4294967206, 4294966597, 4294965647, 90,   389,  0x0, 0,   1,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(86480,   4294964796, 19430,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   31,  255,  0)
    DeclNpc(8659,    4294966597, 670,     225,  405,  0x0, 0,   24,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(7190,    4294966597, 379,     90,   389,  0x0, 0,   25,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(8119,    4294966597, 4294966566, 0,    389,  0x0, 0,   26,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(7239,    4294966746, 3190,    180,  389,  0x0, 0,   20,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(7239,    4294966597, 1580,    0,    385,  0x0, 0,   21,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(47909,   4294964796, 16530,   180,  389,  0x0, 0,   23,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(4294949497, 0,       13369,   0,    389,  0x0, 0,   27,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(4294949296, 0,       4294961546, 90,   385,  0x0, 0,   28,  0,   0,   6,   0,   40,  255,  0)
    DeclNpc(4294949497, 0,       13369,   180,  389,  0x0, 0,   28,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(42450,   4294964796, 2329,    235,  389,  0x0, 0,   36,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(4294946057, 0,       14350,   90,   196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(7820,    4294966896, 3200,    180,  389,  0x0, 0,   37,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   33,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0000, 0, 65,  -13.5,                 27.5,                  1.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -13.75,                -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 66,  5.0,                   33.0,                  1.0,                   324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   -0.4166666865348816,   -11.0,                 -0.1428571492433548,   1.0])
    DeclEvent(0x0000, 0, 67,  -20.0,                 -29.0,                 -0.5,                  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   1.6666667461395264,    9.666666984558105,     0.0714285746216774,    1.0])
    DeclEvent(0x0000, 0, 68,  -29.0,                 23.329999923706055,    1.0,                   324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   9.666666984558105,     -1.944166660308838,    -0.1428571492433548,   1.0])
    DeclEvent(0x0000, 0, 78,  -0.23999999463558197,  6.5,                   -0.28999999165534973,  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   0.019999999552965164,  -2.1666667461395264,   0.0414285734295845,    1.0])
    DeclEvent(0x0000, 0, 79,  -0.09000000357627869,  -6.5,                  -0.20999999344348907,  324.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    0.0,                   0.007500000298023224,  2.1666667461395264,    0.030000001192092896,  1.0])
    DeclEvent(0x0000, 0, 93,  33.08000183105469,     0.07999999821186066,   -2.5,                  324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -11.026667594909668,   -0.006666666828095913, 0.625,                 1.0])

    DeclActor(16750,   4294966296, 4294951556, 1200,    16750,   0,       4294951556, 0x007C, 0,  10, 0x0000)
    DeclActor(82470,   4294964796, 15010,   1200,    79890,   4294963796, 8810,    0x007C, 0,  46, 0x0000)
    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  44, 0x0000)
    DeclActor(34000,   4294964796, 3400,    1500,    34000,   4294965796, 3400,    0x007C, 0,  105, 0x0000)
    DeclActor(7470,    4294966596, 3250,    1500,    7470,    4294966746, 3250,    0x007C, 0,  62, 0x0000)
    DeclActor(4294960156, 0,       13580,   1500,    4294960156, 1250,    13580,   0x007C, 0,  63, 0x0000)
    DeclActor(39300,   4294964796, 19050,   1500,    39300,   4294966046, 19050,   0x007C, 0,  64, 0x0000)
    DeclActor(4294953796, 1000,    27500,   2000,    4294953796, 3000,    27500,   0x007C, 0,  45, 0x0000)
    DeclActor(77220,   4294964796, 20290,   2000,    77220,   4294966296, 20290,   0x007C, 0,  106, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Governmental District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential Street")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Street")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ChipFrameInfo(3584, 0)                                       # 0

    ScpFunction((
        "Function_0_E00",          # 00, 0
        "Function_1_EB0",          # 01, 1
        "Function_2_F61",          # 02, 2
        "Function_3_109B",         # 03, 3
        "Function_4_11D5",         # 04, 4
        "Function_5_1286",         # 05, 5
        "Function_6_1337",         # 06, 6
        "Function_7_13E8",         # 07, 7
        "Function_8_14AC",         # 08, 8
        "Function_9_1C86",         # 09, 9
        "Function_10_2092",        # 0A, 10
        "Function_11_21E4",        # 0B, 11
        "Function_12_3519",        # 0C, 12
        "Function_13_4D48",        # 0D, 13
        "Function_14_5716",        # 0E, 14
        "Function_15_5F21",        # 0F, 15
        "Function_16_6059",        # 10, 16
        "Function_17_6191",        # 11, 17
        "Function_18_65E1",        # 12, 18
        "Function_19_67C6",        # 13, 19
        "Function_20_68A9",        # 14, 20
        "Function_21_69C7",        # 15, 21
        "Function_22_6AE0",        # 16, 22
        "Function_23_6C2D",        # 17, 23
        "Function_24_6CDF",        # 18, 24
        "Function_25_6D95",        # 19, 25
        "Function_26_6E5E",        # 1A, 26
        "Function_27_6E91",        # 1B, 27
        "Function_28_702F",        # 1C, 28
        "Function_29_715D",        # 1D, 29
        "Function_30_717B",        # 1E, 30
        "Function_31_71B1",        # 1F, 31
        "Function_32_71D5",        # 20, 32
        "Function_33_723E",        # 21, 33
        "Function_34_7321",        # 22, 34
        "Function_35_7437",        # 23, 35
        "Function_36_74E0",        # 24, 36
        "Function_37_7605",        # 25, 37
        "Function_38_76BC",        # 26, 38
        "Function_39_78EA",        # 27, 39
        "Function_40_7ABA",        # 28, 40
        "Function_41_7D1E",        # 29, 41
        "Function_42_80D5",        # 2A, 42
        "Function_43_8254",        # 2B, 43
        "Function_44_83ED",        # 2C, 44
        "Function_45_8953",        # 2D, 45
        "Function_46_8BA6",        # 2E, 46
        "Function_47_8C6B",        # 2F, 47
        "Function_48_959B",        # 30, 48
        "Function_49_9695",        # 31, 49
        "Function_50_96B4",        # 32, 50
        "Function_51_9AD5",        # 33, 51
        "Function_52_9B20",        # 34, 52
        "Function_53_9B81",        # 35, 53
        "Function_54_9BE2",        # 36, 54
        "Function_55_9C12",        # 37, 55
        "Function_56_9C40",        # 38, 56
        "Function_57_A558",        # 39, 57
        "Function_58_A658",        # 3A, 58
        "Function_59_A676",        # 3B, 59
        "Function_60_A6AA",        # 3C, 60
        "Function_61_A6DE",        # 3D, 61
        "Function_62_AC6C",        # 3E, 62
        "Function_63_ACC3",        # 3F, 63
        "Function_64_ACFB",        # 40, 64
        "Function_65_AD46",        # 41, 65
        "Function_66_AD9B",        # 42, 66
        "Function_67_AE12",        # 43, 67
        "Function_68_AE89",        # 44, 68
        "Function_69_AF00",        # 45, 69
        "Function_70_B323",        # 46, 70
        "Function_71_B4DE",        # 47, 71
        "Function_72_BCD5",        # 48, 72
        "Function_73_C7DE",        # 49, 73
        "Function_74_C815",        # 4A, 74
        "Function_75_C860",        # 4B, 75
        "Function_76_DA2F",        # 4C, 76
        "Function_77_DCCF",        # 4D, 77
        "Function_78_DD12",        # 4E, 78
        "Function_79_DDC2",        # 4F, 79
        "Function_80_DE72",        # 50, 80
        "Function_81_EEDC",        # 51, 81
        "Function_82_EEF9",        # 52, 82
        "Function_83_EF16",        # 53, 83
        "Function_84_EF33",        # 54, 84
        "Function_85_EFA6",        # 55, 85
        "Function_86_F019",        # 56, 86
        "Function_87_F12D",        # 57, 87
        "Function_88_F241",        # 58, 88
        "Function_89_F266",        # 59, 89
        "Function_90_F2B4",        # 5A, 90
        "Function_91_1038F",       # 5B, 91
        "Function_92_10C28",       # 5C, 92
        "Function_93_10C7E",       # 5D, 93
        "Function_94_10FF8",       # 5E, 94
        "Function_95_113D7",       # 5F, 95
        "Function_96_11405",       # 60, 96
        "Function_97_11B8E",       # 61, 97
        "Function_98_11C20",       # 62, 98
        "Function_99_11C6B",       # 63, 99
        "Function_100_11CB6",      # 64, 100
        "Function_101_11D01",      # 65, 101
        "Function_102_11D4C",      # 66, 102
        "Function_103_11D97",      # 67, 103
        "Function_104_11DE2",      # 68, 104
        "Function_105_11F37",      # 69, 105
        "Function_106_12098",      # 6A, 106
    ))


    def Function_0_E00(): pass

    label("Function_0_E00")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E38"),
        (1, "loc_E44"),
        (2, "loc_E50"),
        (3, "loc_E5C"),
        (4, "loc_E68"),
        (5, "loc_E74"),
        (6, "loc_E80"),
        (SWITCH_DEFAULT, "loc_E8C"),
    )


    label("loc_E38")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E44")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E50")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E5C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E68")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E74")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E8C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_E98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EAF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E98")

    label("loc_EAF")

    Return()

    # Function_0_E00 end

    def Function_1_EB0(): pass

    label("Function_1_EB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F60")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_EB0")

    label("loc_F60")

    Return()

    # Function_1_EB0 end

    def Function_2_F61(): pass

    label("Function_2_F61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_109A")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_F61")

    label("loc_109A")

    Return()

    # Function_2_F61 end

    def Function_3_109B(): pass

    label("Function_3_109B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D4")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 10000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 8000, 0x0)
    Jump("Function_3_109B")

    label("loc_11D4")

    Return()

    # Function_3_109B end

    def Function_4_11D5(): pass

    label("Function_4_11D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1285")
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    Jump("Function_4_11D5")

    label("loc_1285")

    Return()

    # Function_4_11D5 end

    def Function_5_1286(): pass

    label("Function_5_1286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1336")
    OP_95(0xFE, 18000, 0, -4300, 4000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 4000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 4000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 4000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 4000, 0x0)
    OP_95(0xFE, -13000, 0, -10000, 4000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 4000, 0x0)
    Jump("Function_5_1286")

    label("loc_1336")

    Return()

    # Function_5_1286 end

    def Function_6_1337(): pass

    label("Function_6_1337")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13E7")
    OP_95(0xFE, -13000, 0, -10000, 1000, 0x0)
    OP_95(0xFE, 13000, 0, -10000, 1000, 0x0)
    OP_95(0xFE, 18000, 0, -4300, 1000, 0x0)
    OP_95(0xFE, 18000, 0, 7040, 1000, 0x0)
    OP_95(0xFE, 13000, 0, 10000, 1000, 0x0)
    OP_95(0xFE, -12700, 0, 10000, 1000, 0x0)
    OP_95(0xFE, -18000, 0, 5200, 1000, 0x0)
    OP_95(0xFE, -18000, 0, -5750, 1000, 0x0)
    Jump("Function_6_1337")

    label("loc_13E7")

    Return()

    # Function_6_1337 end

    def Function_7_13E8(): pass

    label("Function_7_13E8")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1435")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1449")
    ClearMapObjFlags(0xD, 0x2000000)

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1458")
    ClearMapObjFlags(0xD, 0x2000000)

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1467")
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1488")
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1497")
    ClearMapObjFlags(0xF, 0x2000000)

    label("loc_1497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AB")
    ClearMapObjFlags(0xB, 0x2000000)

    label("loc_14AB")

    Return()

    # Function_7_13E8 end

    def Function_8_14AC(): pass

    label("Function_8_14AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E7")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156E")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1541")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_1560")

    label("loc_1541")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1560")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_1560")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16E7")

    label("loc_156E")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1646")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1619")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_1638")

    label("loc_1619")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1638")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_1638")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16E7")

    label("loc_1646")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BF")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_16DE")

    label("loc_16BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16DE")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_16DE")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16E7")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16FE")
    Jump("loc_1B60")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_170C")
    Jump("loc_1B60")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 1)), scpexpr(EXPR_END)), "loc_171A")
    Jump("loc_1B60")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1750")
    SetChrPos(0xB, 39670, -2500, -19380, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 38440, -2490, -18080, 180)
    Jump("loc_1B60")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1786")
    SetChrFlags(0x8, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x9, 0x16)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_1B60")

    label("loc_1786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17AF")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_1B60")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_186B")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x24, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1815")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 40740, -2500, -2330, 180)
    SetChrPos(0x17, 40630, -2500, -3760, 0)
    Jump("loc_1866")

    label("loc_1815")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrPos(0x16, 38970, -2500, 3640, 90)
    SetChrPos(0x12, 39450, -2500, -2530, 90)
    SetChrPos(0x14, 39750, -2500, -1190, 90)

    label("loc_1866")

    Jump("loc_1B60")

    label("loc_186B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1883")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_1B60")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_190D")
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x10)
    ClearChrFlags(0x26, 0x4)
    SetChrPos(0xB, -7150, 0, 12300, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C1")
    SetChrFlags(0xB, 0x10)

    label("loc_18C1")

    SetChrPos(0xC, -8150, 0, 12300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E1")
    SetChrFlags(0xC, 0x10)

    label("loc_18E1")

    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_93(0x23, 0xB4, 0x0)
    SetChrPos(0x23, -17800, 0, 15000, 180)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_1B60")

    label("loc_190D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A1A")
    BeginChrThread(0xA, 0, 0, 3)
    SetChrPos(0xB, -4350, 0, -8570, 45)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, -5350, 0, -8570, 45)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1999")
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_1999")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 0, 0, 0)
    SetChrPos(0x22, -1800, -310, 6250, 135)
    ClearChrFlags(0x23, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A15")
    ClearChrFlags(0x34, 0x80)
    SetChrPos(0x34, 9330, -690, -1000, 270)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 9330, -690, 600, 270)

    label("loc_1A15")

    Jump("loc_1B60")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A7E")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A43")
    SetChrFlags(0xB, 0x10)

    label("loc_1A43")

    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_1A6F")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)

    label("loc_1A6F")

    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_1B60")

    label("loc_1A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AD4")
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AC6")
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)

    label("loc_1AC6")

    SetChrChipByIndex(0x9, 0x16)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_1B60")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B60")
    SetChrChipByIndex(0xB, 0xE)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFD")
    SetChrFlags(0xB, 0x10)

    label("loc_1AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0C")
    SetChrFlags(0xC, 0x10)

    label("loc_1B0C")

    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_1B4F")
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x1E, 0x23)
    SetChrPos(0x1E, 41500, -2500, 160, 90)
    SetChrPos(0x1F, 41500, -2500, -1440, 90)
    Jump("loc_1B60")

    label("loc_1B4F")

    SetChrChipByIndex(0x1E, 0x14)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)

    label("loc_1B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B84")
    SetChrPos(0x18, 42400, -2500, -18000, 270)
    ClearChrFlags(0x18, 0x80)

    label("loc_1B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_END)), "loc_1BB1")
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BB1")
    ClearChrFlags(0xC, 0x10)

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    ClearScenarioFlags(0x22, 0)
    Event(0, 50)
    Jump("loc_1C49")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1BD9")
    ClearScenarioFlags(0x22, 1)
    Event(0, 96)
    Jump("loc_1C49")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1BED")
    ClearScenarioFlags(0x22, 2)
    Event(0, 95)
    Jump("loc_1C49")

    label("loc_1BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1C01")
    ClearScenarioFlags(0x22, 3)
    Event(0, 91)
    Jump("loc_1C49")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1C18")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x3, 0)
    Event(0, 56)
    Jump("loc_1C49")

    label("loc_1C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1C2C")
    ClearScenarioFlags(0x22, 5)
    Event(0, 76)
    Jump("loc_1C49")

    label("loc_1C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1C49")
    ClearScenarioFlags(0x22, 6)
    SetChrPos(0x0, 19290, 0, 17220, 180)

    label("loc_1C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C5A")
    Event(0, 75)

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C85")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1C85")

    Return()

    # Function_8_14AC end

    def Function_9_1C86(): pass

    label("Function_9_1C86")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D65")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1D65")

    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB8")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DB8")
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    OP_66(0x2, 0x1)

    label("loc_1DB8")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DEF")
    OP_1B(0x2, 0x0, 0x68)
    OP_66(0x7, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E11")
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)

    label("loc_1E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E65")
    ClearChrFlags(0x25, 0x80)
    OP_78(0xB, 0x25)
    SetChrPos(0x25, -21240, 0, 14350, 90)
    OP_D5(0x25, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)

    label("loc_1E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA6")
    ClearChrFlags(0x33, 0x80)
    OP_78(0xD, 0x33)
    SetChrPos(0x33, 40000, -4000, -22500, 90)
    OP_D5(0x33, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)

    label("loc_1EA6")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EFC")
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFC")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x12C, 0x0, 0x20)

    label("loc_1EFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F15")
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1F1B")

    label("loc_1F15")

    SetMapObjFlags(0x9, 0x4)

    label("loc_1F1B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_1F6E")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA6")
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_1FA6")

    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FCA")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1FCA")

    OP_52(0x1B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2030")
    OP_65(0x1, 0x1)

    label("loc_2030")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 79890, -3500, 8810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208D")
    OP_70(0x8, 0x0)
    Jump("loc_2091")

    label("loc_208D")

    OP_70(0x8, 0x1E)

    label("loc_2091")

    Return()

    # Function_9_1C86 end

    def Function_10_2092(): pass

    label("Function_10_2092")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218E")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_2117")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_2189")

    label("loc_2117")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2189")

    Jump("loc_21D8")

    label("loc_218E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_21D8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2092 end

    def Function_11_21E4(): pass

    label("Function_11_21E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2326")

    ChrTalk(
        0xFE,
        (
            "I was surprised by this sudden development, but...\x01",
            "If we don't make a show of strength,\x01",
            "won't the two major powers make fun of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I strongly\x01",
            "support President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Secretary Arios is there...\x01",
            "The two major powers won't be able\x01",
            "to do whatever they want any more!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B7")

    label("loc_2326")


    ChrTalk(
        0xFE,
        (
            "Of course I'm anxious.\x01",
            "But, I strongly support\x01",
            "President Dieter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two major powers won't be able\x01",
            "to do whatever they want any more!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B7")

    Jump("loc_3515")

    label("loc_23BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250B")

    ChrTalk(
        0xFE,
        (
            "The riverside office was completely destroyed... Rumor has\x01",
            "it that it was because of their connections to the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I wonder if the attack was\x01",
            "by a jaeger corps employed by the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That doesn't matter, but...\x01",
            "Anyway, I hope nothing\x01",
            "unnecessary happens in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25C2")

    label("loc_250B")


    ChrTalk(
        0xFE,
        (
            "It's become like this because\x01",
            "Crossbell has always been\x01",
            "a subordinate state...right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why it's necessary to\x01",
            "show the surrounding countries\x01",
            "our will to be independent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C2")

    Jump("loc_3515")

    label("loc_25C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F7")

    ChrTalk(
        0xFE,
        (
            "The CGF are having a tough time fighting\x01",
            "against that armed group, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumor has it that if Crossbell becomes independent,\x01",
            "the military will be strengthened so as to deal with\x01",
            "a situation like this without difficulty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell should be\x01",
            "independent...right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27BD")

    label("loc_26F7")


    ChrTalk(
        0xFE,
        (
            "Rumor has it that if Crossbell becomes independent,\x01",
            "the military will be strengthened so as to deal with\x01",
            "a situation like this without difficulty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell should be\x01",
            "independent...right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27BD")

    Jump("loc_3515")

    label("loc_27C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27D0")
    Jump("loc_3515")

    label("loc_27D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2931")

    ChrTalk(
        0xFE,
        (
            "There are already a lot of people who\x01",
            "approve of independence, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hmm, but I still\x01",
            "don't know much about\x01",
            "the pros and cons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I heard a civic forum\x01",
            "with the theme of independence will be held\x01",
            "at the City Meeting Hall tomorrow, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I should start asking questions now?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29D2")

    label("loc_2931")


    ChrTalk(
        0xFE,
        (
            "I heard a civic forum with the theme of independence\x01",
            "will be held at the City Meeting Hall tomorrow, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe I should start asking questions now?\x02",
    )

    CloseMessageWindow()

    label("loc_29D2")

    Jump("loc_3515")

    label("loc_29D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2A83")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, the referendum\x01",
            "on independence will be held just a\x01",
            "week from today, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, what to do. I'll have\x01",
            "to make up my mind soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3515")

    label("loc_2A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B42")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, the Arc-en-ciel\x01",
            "renewal performance is\x01",
            "finally opening soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The additional cast was\x01",
            "finally revealed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can no longer take my eyes off it!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BC2")

    label("loc_2B42")


    ChrTalk(
        0xFE,
        (
            "The additional cast member\x01",
            "is a girl named Sully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though she's still Sunday\x01",
            "School age... Honestly, I'm shocked!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC2")

    Jump("loc_3515")

    label("loc_2BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB9")

    ChrTalk(
        0xFE,
        (
            "I hardly saw her, but Captain\x01",
            "Julia's awesomeness is such that\x01",
            "you wouldn't think she's military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't mean it like\x01",
            "that, though I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like to be hugged tightly by\x01",
            "an awesome person like that㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2D0A")

    label("loc_2CB9")


    ChrTalk(
        0xFE,
        (
            "*sigh*, Captain Julia\x01",
            "is really lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want her to hug me tightly㈱\x02",
    )

    CloseMessageWindow()

    label("loc_2D0A")

    Jump("loc_3515")

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DB6")

    ChrTalk(
        0xFE,
        (
            "Earlier, an Eastern woman\x01",
            "walked toward East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She looked good in her\x01",
            "flowing long black hair and\x01",
            "suit. She was so cool...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32EA")

    label("loc_2DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F3D")

    ChrTalk(
        0xFE,
        (
            "I saw an Eastern woman\x01",
            "pass by just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She looked good in her\x01",
            "flowing long black hair and\x01",
            "suit. She was so cool...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(An Eastern woman with black hair...?)\x02\x03",
            "#00001FExcuse me, which way did she go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, I think she went\x01",
            "to East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FEast Street...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(I'm not sure if it's "her" or not,\x01",
            "but we should check it out.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    SetScenarioFlags(0x1C6, 6)
    Jump("loc_32EA")

    label("loc_2F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326B")

    ChrTalk(
        0xFE,
        (
            "She came from Liberl\x01",
            "Kingdom... Um, yeah,\x01",
            "Captain Julia Schwarz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw a pin-up photo\x01",
            "of her, and instantly\x01",
            "became her fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm told she has a fan\x01",
            "club in Liberl... I wonder\x01",
            "if foreigners can join.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00105FF-Fan club? That's the first\x01",
            "I've heard of it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, a certain magazine called\x01",
            "for it. Although it's unofficial,\x01",
            "I think it formed recently?\x02\x03",
            "#10102FThey send fan club members\x01",
            "Captain Julia's duty schedule\x01",
            "as well as precious photos!\x02\x03",
            "#10106FBut, it's too bad... \x01",
            "It seems you have to live\x01",
            "in Liberl to join.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Aw, really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FHmm. It really is too bad.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005F(Noｱl really knows her stuff.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Yeah. Probably even\x01",
            "more than we think.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14B, 0)
    Jump("loc_32EA")

    label("loc_326B")


    ChrTalk(
        0xFE,
        (
            "I wanted to join Captain\x01",
            "Julia's fan club, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I wonder if I have any distant\x01",
            "relatives or something in Liberl!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EA")

    Jump("loc_3515")

    label("loc_32EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_339A")

    ChrTalk(
        0xFE,
        "The Trade Conference is finally tomorrow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until now, I've only seen the VIPs\x01",
            "in magazines. I wonder if they all\x01",
            "have a different aura in person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3515")

    label("loc_339A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33A8")
    Jump("loc_3515")

    label("loc_33A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3515")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348F")

    ChrTalk(
        0xFE,
        (
            "Mayor Dieter never\x01",
            "misses a beat, does he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is wise, just, dynamic and\x01",
            "full of ideas, and on top of that\x01",
            "he's wealthy and handsome...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, just saying that\x01",
            "made my head spin, somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3515")

    label("loc_348F")


    ChrTalk(
        0xFE,
        (
            "Mayor Dieter never\x01",
            "misses a beat, does he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if he's worried about other things\x01",
            "outside of politics and finance too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3515")

    TalkEnd(0xFE)
    Return()

    # Function_11_21E4 end

    def Function_12_3519(): pass

    label("Function_12_3519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3550")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3550")
    Call(0, 90)
    Return()

    label("loc_3550")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A96")

    ChrTalk(
        0x1A2,
        "*sniff sniff*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hmm, this is a pretty nice smell!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Oh, young man! I see that you\x01",
            "understand the goodness of my noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Yeah, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I think it's on the level\x01",
            "of B-class gourmet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Y-You would identify my noodles as B-class...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph, out with you! \x01",
            "I've got no noodles to feed someone\x01",
            "without a sense of value!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "Miss, did I say\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_386B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_37B6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37B6)
    Sleep(50)

    def lambda_37C6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37C6)
    Sleep(50)

    def lambda_37D6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37D6)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FSayin' things like this will make everyone think\x01",
            "you're ignorant of the ways of the world, you see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A8B")

    label("loc_386B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_397A")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_38C4():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38C4)
    Sleep(50)

    def lambda_38D4():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38D4)
    Sleep(50)

    def lambda_38E4():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_38E4)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSaying things like this will make everyone think\x01",
            "you're ignorant of the ways of the world, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A8B")

    label("loc_397A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3A8B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_39D3():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39D3)
    Sleep(50)

    def lambda_39E3():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39E3)
    Sleep(50)

    def lambda_39F3():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39F3)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00106FShing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, saying things like this will\x01",
            "make everyone think you're ignorant\x01",
            "of the ways of the world, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A8B")

    TalkEnd(0x9)
    SetScenarioFlags(0x1DC, 1)
    Jump("loc_3B2C")

    label("loc_3A96")


    ChrTalk(
        0x9,
        "To think someone would say my noodles are B-class...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph, out with you! \x01",
            "I've got no noodles to feed someone\x01",
            "without a sense of value!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3B2C")

    Return()

    label("loc_3B2D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D44")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B87")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA7")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D3F")

    label("loc_3BA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BBB")
    Jump("loc_4D3F")

    label("loc_3BBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D3F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_3CA2")

    ChrTalk(
        0xFE,
        (
            "Hu hu, among young men too\x01",
            "there was still one with promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Use that recipe I gave you, and set\x01",
            "your sights on supreme noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I too will be secretly\x01",
            "cheering for all of you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3F")

    label("loc_3CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3D3E")

    ChrTalk(
        0xFE,
        "Hmm, so it's finally come to this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm already prepared for whatever happens. \x01",
            "Now that it's come to this, I can only push ahead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3F")

    label("loc_3D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E37")

    ChrTalk(
        0xFE,
        (
            "Over many years, my cart and I have experienced many\x01",
            "joys and sorrows, so it was quite a shock for it to be\x01",
            "destroyed...but I have to stay positive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this newly purchased cart, I plan\x01",
            "to do my best to make a fresh start!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3F")

    label("loc_3E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3EC2")

    ChrTalk(
        0xFE,
        (
            "It seems a bunch of complete\x01",
            "fools have appeared at Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, I want to splash them\x01",
            "with this piping hot broth!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3F")

    label("loc_3EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3B")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0xFE,
        "......*atchooon*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, it seems my body \x01",
            "has gotten a little cold.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FD0")

    label("loc_3F3B")


    ChrTalk(
        0xFE,
        (
            "Alright then, I suppose I'll\x01",
            "make a portion for myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By slurping noodles, both body and soul\x01",
            "become warm... No, they become piping hot!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD0")

    Jump("loc_4D3F")

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4111")

    ChrTalk(
        0xFE,
        (
            "Hmm? It seems my\x01",
            "crushed pepper\x01",
            "supply has run low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I've got to buy\x01",
            "more somewhere while\x01",
            "watching the time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_410C")

    ChrTalk(
        0x101,
        (
            "#00008F(I think we can get coverage for\x01",
            "the gourmet guide here, but...)\x02\x03",
            "#00003F(Now's not the time. Let's\x01",
            "not forget to stop by later.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410C")

    Jump("loc_4D3F")

    label("loc_4111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4184")

    ChrTalk(
        0xFE,
        "Hmm, today's noodles are well made.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taste the noodles I've put\x01",
            "all myself into it aplenty!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D3F")

    label("loc_4184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_42FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_427D")

    ChrTalk(
        0xFE,
        (
            "An independence proposal\x01",
            "is a drastic measure,\x01",
            "even for Mayor Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I see the mayor's\x01",
            "stance as proactive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right, in other words, survival\x01",
            "in everything one does is to\x01",
            "have just the bold mindset.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_42FA")

    label("loc_427D")


    ChrTalk(
        0xFE,
        (
            "Without challenge, there is no success...\x01",
            "Hmm, so the essence of the worlds of\x01",
            "politics and noodles are the same, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42FA")

    Jump("loc_4D3F")

    label("loc_42FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_441A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43CD")

    ChrTalk(
        0xFE,
        "A thousand customers have a thousand stories.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Through contact with customers, one part\x01",
            "of their story is revealed... This too is\x01",
            "one of the pleasures of running a cart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4415")

    label("loc_43CD")


    ChrTalk(
        0xFE,
        (
            "An old man and his granddaughter... \x01",
            "What a harmonious nice thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4415")

    Jump("loc_4D3F")

    label("loc_441A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_48E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44DE")

    ChrTalk(
        0xFE,
        (
            "Just now, a bright suited\x01",
            "young man with red hair\x01",
            "had some of my noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying "Maybe I'll go have some dessert,"\x01",
            "he headed for the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E1")

    label("loc_44DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_477C")

    ChrTalk(
        0xFE,
        (
            "Just now, a bright suited\x01",
            "young man with red hair had\x01",
            "some of my noodles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Saying he'd disclose my secret soup recipe,\x01",
            "he even entered the back of my cart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I narrowly succeeded in\x01",
            "driving him off, but...\x01",
            "What an unthinkable guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(A bright redheaded suited young man...)\x02\x03",
            "#00006F(...Judging fom his actions,\x01",
            "I feel like I'm reminded of a\x01",
            "certain character I know.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FWhere did that man go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he said "I think I'll go have some dessert"\x01",
            "and headed for the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FThe Entertainment District...\x02\x03",
            "#00003F(...Though I can't be\x01",
            "sure it's "him", shall\x01",
            "we give chase...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    SetScenarioFlags(0x1C7, 1)
    Jump("loc_48E1")

    label("loc_477C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484D")

    ChrTalk(
        0xFE,
        (
            "Hmm, now that the heads of state\x01",
            "have come to Crossbell, the\x01",
            "atmosphere is showy yet strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it's for security reasons, but I can't\x01",
            "help but be concerned at officers' gazes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48E1")

    label("loc_484D")


    ChrTalk(
        0xFE,
        (
            "The police stare at my cart\x01",
            "every so often. I wonder if\x01",
            "that's for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness. If it's like this, I\x01",
            "can't concentrate on my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E1")

    Jump("loc_4D3F")

    label("loc_48E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49C6")

    ChrTalk(
        0xFE,
        "Noodles have firmness! And mouthfeel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me just say this. My noodles\x01",
            "absolutely need not be eaten elegantly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is only by a hearty slurp\x01",
            "that their flavor can be enjoyed!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4A60")

    label("loc_49C6")


    ChrTalk(
        0xFE,
        (
            "Let me just say this. My noodles\x01",
            "absolutely need not be eaten elegantly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is only by a hearty slurp\x01",
            "that their flavor can be enjoyed!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A60")

    Jump("loc_4D3F")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_4ACA")

    ChrTalk(
        0xFE,
        "A girl with a pink umbrella?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I don't think\x01",
            "she's come this way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BDB")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7B")

    ChrTalk(
        0xFE,
        "The path of noodles is perseverance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I shall not lose to this trifling rain!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm worried somehow that the\x01",
            "rain will get into his food.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4BDB")

    label("loc_4B7B")


    ChrTalk(
        0xFE,
        (
            "Come now. Since you're here,\x01",
            "why not have a portion. It'll\x01",
            "warm your cold bodies right up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BDB")

    Jump("loc_4D3F")

    label("loc_4BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE2")

    ChrTalk(
        0xFE,
        (
            "The path of noodles is one day at a\x01",
            "time... And that path is unending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, through research,\x01",
            "I'm finally able to offer my\x01",
            "new noodles at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And their name? "Heavenly Noodles\x01",
            ""Sun"". You should have some!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4D3F")

    label("loc_4CE2")


    ChrTalk(
        0xFE,
        (
            "I've put my absolute pride\x01",
            "in my new noodles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm certain you'll\x01",
            "be satisfied too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3F")

    Jump("loc_3B37")

    label("loc_4D44")

    TalkEnd(0xFE)
    Return()

    # Function_12_3519 end

    def Function_13_4D48(): pass

    label("Function_13_4D48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E59")

    ChrTalk(
        0xFE,
        (
            "Because the trains were halted this morning,\x01",
            "I have considerably fewer deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Or rather, if things continue like this, I\x01",
            "wonder what's going to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's a lot more important than some job, isn't it...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4EF5")

    label("loc_4E59")


    ChrTalk(
        0xFE,
        (
            "Really. If things continue at this rate, I don't\x01",
            "know what's going to happen to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's a lot more important than some job, isn't it...\x02",
    )

    CloseMessageWindow()

    label("loc_4EF5")

    Jump("loc_5712")

    label("loc_4EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FB2")

    ChrTalk(
        0xFE,
        (
            "It's already been a week since the attack, huh...\x01",
            "I guess things are finally settling down around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I hope something like\x01",
            "that never happens again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5712")

    label("loc_4FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_50CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507C")

    ChrTalk(
        0xFE,
        (
            "The CGF are fighting the armed\x01",
            "group at Mainz, but it looks like\x01",
            "they're having a tough time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being independent with our own\x01",
            "military... I suppose that's important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_50C8")

    label("loc_507C")


    ChrTalk(
        0xFE,
        (
            "Being independent with our own\x01",
            "military... I suppose that's important.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C8")

    Jump("loc_5712")

    label("loc_50CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5169")

    ChrTalk(
        0xFE,
        (
            "Wah!? The letters on the address label\x01",
            "disappeared because of the rain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "B-But well, I can make\x01",
            "them out somehow, yeah.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_51FE")

    label("loc_5169")


    ChrTalk(
        0xFE,
        (
            "Returning to HQ to check the\x01",
            "address for each one would be\x01",
            "a considerable loss of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, but rainy days are\x01",
            "tough in a lot of ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51FE")

    Jump("loc_5712")

    label("loc_5203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5286")

    ChrTalk(
        0xFE,
        (
            "I looks like several\x01",
            "ambulances are running between\x01",
            "the station and West Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What could have happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5712")

    label("loc_5286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_52D6")

    ChrTalk(
        0xFE,
        "Alright, I'm fired up today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "An efficient route, hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5712")

    label("loc_52D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_53BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_537E")

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll do another\x01",
            "two deliveries and then have lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, thinking about it that\x01",
            "way gives me energy somehow!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_53B7")

    label("loc_537E")


    ChrTalk(
        0xFE,
        (
            "Just two more until lunch,\x01",
            "Two more until lunch...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53B7")

    Jump("loc_5712")

    label("loc_53BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_54AC")

    ChrTalk(
        0xFE,
        (
            "During the Trade Conference, the police\x01",
            "said no deliveries for the new City\x01",
            "Hall building area would be allow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because if there was a bomb or\x01",
            "something in a package, that wouldn't\x01",
            "be funny. Perfectly understandable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5712")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5566")

    ChrTalk(
        0xFE,
        (
            "I couldn't deliver my packages due\x01",
            "to the VIPs' visit this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But my workload is the same\x01",
            "a usual today... I've got\x01",
            "to make up the difference!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_557D")

    label("loc_5566")


    ChrTalk(
        0xFE,
        "Dash! Dash! Dash!\x02",
    )

    CloseMessageWindow()

    label("loc_557D")

    Jump("loc_5712")

    label("loc_5582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_55FC")

    ChrTalk(
        0xFE,
        "There's a lot of police officers on patrol, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I've got to be careful not to bump into them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5712")

    label("loc_55FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_56C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_5650")

    ChrTalk(
        0xFE,
        (
            "Sorry, but I'm working.\x01",
            "I haven't seen any little girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56BB")

    label("loc_5650")


    ChrTalk(
        0xFE,
        (
            "Hehe. Rain or storm?\x01",
            "Bring it on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...That's what I'd like to say, \x01",
            "but I'm fine without a storm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56BB")

    Jump("loc_5712")

    label("loc_56C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5712")

    ChrTalk(
        0xFE,
        (
            "*sigh*, busy, busy... Being a\x01",
            "deliveryman challenges one's stamina.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5712")

    TalkEnd(0xFE)
    Return()

    # Function_13_4D48 end

    def Function_14_5716(): pass

    label("Function_14_5716")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5805")

    ChrTalk(
        0xFE,
        (
            "What a foolish address...\x01",
            "The world may be deceived,\x01",
            "but I shall not be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "State independence this, State Guard that!\x01",
            "Does he really believe we can hold on\x01",
            "against the threat of the two major powers!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5864")

    label("loc_5805")


    ChrTalk(
        0xFE,
        (
            "O Goddess... Someone\x01",
            "like me matters not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But please, save my\x01",
            "granddaughter Amisaah!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5864")

    Jump("loc_5F1D")

    label("loc_5869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5909")

    ChrTalk(
        0xFE,
        (
            "Back then, if Amisaah and I had been\x01",
            "just a little too late escaping...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't help but feel terrified\x01",
            "when I think that, even now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_596A")

    ChrTalk(
        0xFE,
        (
            "Goodness, how sad. Just what\x01",
            "will tormenting the people\x01",
            "of Mainz accomplish!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_596A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5A0A")

    ChrTalk(
        0xFE,
        (
            "Hmm, so that thing I see in the\x01",
            "distance is called a ferris wheel, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Say, Amisaah. Want\x01",
            "to go to the theme park\x01",
            "with your grandpa?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5A6A")

    ChrTalk(
        0xFE,
        (
            "Wahahaha, what do you\x01",
            "think of that, Amisaah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't your grandpa great?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5ABF")

    ChrTalk(
        0xFE,
        "Wait! Amisaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now grandpa will catch\x01",
            "a big one, you'll see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F1D")

    label("loc_5ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5ACD")
    Jump("loc_5F1D")

    label("loc_5ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AE8")
    Call(0, 15)
    Jump("loc_5B37")

    label("loc_5AE8")


    ChrTalk(
        0xFE,
        (
            "Amisaah is truly a\x01",
            "kind and good child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...It makes me cry, somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_5B37")

    Jump("loc_5F1D")

    label("loc_5B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C11")

    ChrTalk(
        0xFE,
        (
            "The police said to refrain\x01",
            "from fishing during the\x01",
            "Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, it's fun viewing the city\x01",
            "with my granddaughter like\x01",
            "this every once in awhile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x2D, 0x0)
    SetChrFlags(0xB, 0x10)
    Jump("loc_5C45")

    label("loc_5C11")


    ChrTalk(
        0xFE,
        (
            "Oh, what have we here.\x01",
            "So that's "Michey", eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C45")

    Jump("loc_5CA6")

    label("loc_5C4A")


    ChrTalk(
        0xFE,
        (
            "Hmm. It must be fun,\x01",
            "dancing like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It would be fine if I\x01",
            "was younger, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA6")

    Jump("loc_5F1D")

    label("loc_5CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D92")

    ChrTalk(
        0xFE,
        (
            "I don't know if it's for the\x01",
            "Trade Conference, but those\x01",
            "police really stand out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "...Ah, I mustn't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Amisaah told me not\x01",
            "to complain again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_5E50")

    label("loc_5D92")


    ChrTalk(
        0xFE,
        (
            "According to Amisaah, complaining\x01",
            "isn't good for your health.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Setting aside whether it's correct, I\x01",
            "don't want to see Amisaah's sad face.\x01",
            "I'll try not to say anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E50")

    Jump("loc_5F1D")

    label("loc_5E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E63")
    Jump("loc_5F1D")

    label("loc_5E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5F1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7E")
    Call(0, 16)
    Jump("loc_5F1D")

    label("loc_5E7E")


    ChrTalk(
        0xFE,
        (
            "I detest both the world\x01",
            "and hospitals... I love\x01",
            "only my granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of that, I've decided\x01",
            "to listen to what she says as\x01",
            "much as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F1D")

    TalkEnd(0xFE)
    Return()

    # Function_14_5716 end

    def Function_15_5F21(): pass

    label("Function_15_5F21")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        (
            "*blowing*... These\x01",
            "noodles are hard to\x01",
            "eat when they're hot.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "Oh grandpa! Don't\x01",
            "be in such a rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh yeah! Amisaah will\x01",
            "blow on them for you.\x01",
            "One moment please.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "*blooowing*...\x01",
            "Alright, eat up♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh... Thank\x01",
            "you, Amisaah.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_15_5F21 end

    def Function_16_6059(): pass

    label("Function_16_6059")


    ChrTalk(
        0xC,
        (
            "Grandpa, I brought your\x01",
            "medicine today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm, thank you as always.\x01",
            "I'll take it later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That won't do. I know you\x01",
            "don't take it sometimes when\x01",
            "I take my eyes off you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll watch you take it\x01",
            "with your meal today, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-I see... You always see\x01",
            "things through, Amisaah.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_16_6059 end

    def Function_17_6191(): pass

    label("Function_17_6191")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6208")

    ChrTalk(
        0xFE,
        (
            "Like my grandpa says, this\x01",
            "has become a real war, I guess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hate that! And I'm scared...\x02",
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_6208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6254")

    ChrTalk(
        0xFE,
        (
            "The red building that was\x01",
            "there... It's completely gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_6254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6298")

    ChrTalk(
        0xFE,
        (
            "Grandpa, getting irritated\x01",
            "isn't good for you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_6298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_62E0")

    ChrTalk(
        0xFE,
        (
            "Eh? Are you\x01",
            "sure, grandpa!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yay! I'm so happy♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_62E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_633A")

    ChrTalk(
        0xFE,
        "Yes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that fish was a\x01",
            "big one. I'm looking\x01",
            "forward to dinner♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_633A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_63B2")

    ChrTalk(
        0xFE,
        (
            "There was a big movement\x01",
            "on grandpa's rod just now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So excited... I wonder\x01",
            "if he'll get a fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65DD")

    label("loc_63B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_63C0")
    Jump("loc_65DD")

    label("loc_63C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_641E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63DB")
    Call(0, 15)
    Jump("loc_6419")

    label("loc_63DB")


    ChrTalk(
        0xFE,
        "Grandpa, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you sad about something?\x02",
    )

    CloseMessageWindow()

    label("loc_6419")

    Jump("loc_65DD")

    label("loc_641E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_64CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_646D")

    ChrTalk(
        0xFE,
        "Look at that, grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Michey's in the park!\x02",
    )

    CloseMessageWindow()
    Jump("loc_64C7")

    label("loc_646D")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Grandpa, dance\x01",
            "with me next time!\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmm... \x01",
            "That would be \x01",
            "hard on me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_64C7")

    Jump("loc_65DD")

    label("loc_64CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_64DA")
    Jump("loc_65DD")

    label("loc_64DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_64E8")
    Jump("loc_65DD")

    label("loc_64E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_65DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6503")
    Call(0, 16)
    Jump("loc_65DD")

    label("loc_6503")


    ChrTalk(
        0xFE,
        (
            "I kept asking him, and recently\x01",
            "my stubborn grandpa finally\x01",
            "started taking his medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are times when he doesn't\x01",
            "if I don't watch him, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe. I'm glad I didn't\x01",
            "give up and kept asking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65DD")

    TalkEnd(0xFE)
    Return()

    # Function_17_6191 end

    def Function_18_65E1(): pass

    label("Function_18_65E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6699")

    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Renewal performance opening\x01",
            "night is finally tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not the case that I can calm\x01",
            "down because of the rain, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66AE")

    label("loc_6699")


    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    label("loc_66AE")

    Jump("loc_67C2")

    label("loc_66B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6762")

    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say it's important to rest,\x01",
            "but I just can't sit still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And when I move my body, I don't\x01",
            "think about unnecessary things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_67C2")

    label("loc_6762")


    ChrTalk(
        0xFE,
        "Eh, oh! Eh, oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so, whenever I run outside\x01",
            "lately, it's been with senior Celine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C2")

    TalkEnd(0xFE)
    Return()

    # Function_18_65E1 end

    def Function_19_67C6(): pass

    label("Function_19_67C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_686D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_682C")

    ChrTalk(
        0xFE,
        "I-I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't intend to lose. To\x01",
            "neither Nikol nor to Sully.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6868")

    label("loc_682C")


    ChrTalk(
        0xFE,
        (
            "I don't intend to lose. To\x01",
            "neither Nikol nor to Sully.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6868")

    Jump("loc_68A5")

    label("loc_686D")


    ChrTalk(
        0xFE,
        (
            "That Nikol... \x01",
            "I can't let him get\x01",
            "the jump on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68A5")

    TalkEnd(0xFE)
    Return()

    # Function_19_67C6 end

    def Function_20_68A9(): pass

    label("Function_20_68A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6913")

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Hiii everyooone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi! Let's have\x01",
            "fun today too, oook?☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6946")

    label("loc_6913")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi! Let's have\x01",
            "fun today too, oook?☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6946")

    Jump("loc_69C3")

    label("loc_694B")


    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi! That guy was\x01",
            "a lot of fun, huuuh☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "I'd looove it if he danced with\x01",
            "me at Wonderland next time☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69C3")

    TalkEnd(0xFE)
    Return()

    # Function_20_68A9 end

    def Function_21_69C7(): pass

    label("Function_21_69C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5D")

    ChrTalk(
        0xFE,
        (
            "Today, Michey has especially\x01",
            "come from Michelam!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got a lot of events ready for you,\x01",
            "so please enjoy them, everyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ADC")

    label("loc_6A5D")


    ChrTalk(
        0xFE,
        (
            "Ah, I'm surprised.\x01",
            "To think he danced so\x01",
            "well with Michey...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should've tried to\x01",
            "scout him while he was here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ADC")

    TalkEnd(0xFE)
    Return()

    # Function_21_69C7 end

    def Function_22_6AE0(): pass

    label("Function_22_6AE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B80")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, Michey's\x01",
            "dance show will\x01",
            "begin shortly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And in today's special event,\x01",
            "you can dance next to Michey!\x01",
            "Please participate, ok!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C29")

    label("loc_6B80")


    ChrTalk(
        0xFE,
        (
            "That blond man started by\x01",
            "playing Michey's dance BGM\x01",
            "with his instrument, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the middle of it, he danced with\x01",
            "Michey personally. Uh uh, what a fun guy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C29")

    TalkEnd(0xFE)
    Return()

    # Function_22_6AE0 end

    def Function_23_6C2D(): pass

    label("Function_23_6C2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C76")

    ChrTalk(
        0xFE,
        (
            "Beach, beach! I want\x01",
            "to swim on the beach!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C76")

    Jump("loc_6CDB")

    label("loc_6C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CAB")

    ChrTalk(
        0xFE,
        "Uwah, it's the real Michey!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CDB")

    label("loc_6CAB")


    ChrTalk(
        0xFE,
        (
            "I want to dance with\x01",
            "Michey too next time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CDB")

    TalkEnd(0xFE)
    Return()

    # Function_23_6C2D end

    def Function_24_6CDF(): pass

    label("Function_24_6CDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D31")

    ChrTalk(
        0xFE,
        (
            "So excited... \x01",
            "I wonder if the dance\x01",
            "show's starting soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D91")

    label("loc_6D31")


    ChrTalk(
        0xFE,
        (
            "That blond guy was\x01",
            "pretty cool, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he doesn't hold a\x01",
            "candle to Michey! Uhuhu.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D91")

    TalkEnd(0xFE)
    Return()

    # Function_24_6CDF end

    def Function_25_6D95(): pass

    label("Function_25_6D95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6DEE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE9")

    NpcTalk(
        0xFE,
        "Passenger",
        (
            "I'm looking forward to\x01",
            "the arcade boutique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DE9")

    Jump("loc_6E5A")

    label("loc_6DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E25")

    ChrTalk(
        0xFE,
        (
            "Hey! Calm down and\x01",
            "look over here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E5A")

    label("loc_6E25")


    ChrTalk(
        0xFE,
        (
            "It looks like the kids\x01",
            "are having a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E5A")

    TalkEnd(0xFE)
    Return()

    # Function_25_6D95 end

    def Function_26_6E5E(): pass

    label("Function_26_6E5E")

    TalkBegin(0xFE)

    NpcTalk(
        0xFE,
        "Passenger",
        "Uh uh, you're a kid too, eh?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_6E5E end

    def Function_27_6E91(): pass

    label("Function_27_6E91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F53")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6EFA")

    ChrTalk(
        0xFE,
        (
            "It looked like she\x01",
            "quite loved it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm so glad we went there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F4E")

    label("loc_6EFA")


    NpcTalk(
        0xFE,
        "Citizen",
        (
            "Ah, I'm looking forward to this. \x01",
            "I want to visit the theme park soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4E")

    Jump("loc_702B")

    label("loc_6F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FC6")

    ChrTalk(
        0xFE,
        "So this is the rumored Michey, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His loose facial expression\x01",
            "is simply irresistible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702B")

    label("loc_6FC6")


    ChrTalk(
        0xFE,
        (
            "Michey can\x01",
            "really dance well.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was looking down on him\x01",
            "thinking he was a stuffed animal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702B")

    TalkEnd(0xFE)
    Return()

    # Function_27_6E91 end

    def Function_28_702F(): pass

    label("Function_28_702F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7076")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7071")

    ChrTalk(
        0xFE,
        (
            "Uhuhu, I bought a\x01",
            "lot of souvenirs☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7071")

    Jump("loc_7159")

    label("loc_7076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70FA")

    ChrTalk(
        0xFE,
        (
            "Even though Wonderland's closed,\x01",
            "I'm lucky to see him in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like I've\x01",
            "become a Michey fan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7159")

    label("loc_70FA")


    ChrTalk(
        0xFE,
        (
            "I've become a\x01",
            "complete Michey fan!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to buy a lot of\x01",
            "souvenirs to take home!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7159")

    TalkEnd(0xFE)
    Return()

    # Function_28_702F end

    def Function_29_715D(): pass

    label("Function_29_715D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7174")
    Call(0, 47)
    Return()

    label("loc_7174")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_29_715D end

    def Function_30_717B(): pass

    label("Function_30_717B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71AD")
    Call(0, 61)
    Jump("loc_71B0")

    label("loc_71AD")

    Call(0, 69)

    label("loc_71B0")

    Return()

    # Function_30_717B end

    def Function_31_71B1(): pass

    label("Function_31_71B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71D4")
    Call(0, 70)

    label("loc_71D4")

    Return()

    # Function_31_71B1 end

    def Function_32_71D5(): pass

    label("Function_32_71D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_720F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F3")
    Call(0, 34)
    Jump("loc_720A")

    label("loc_71F3")


    ChrTalk(
        0x1B,
        "#01200FGrrrowl...\x02",
    )

    CloseMessageWindow()

    label("loc_720A")

    Jump("loc_723A")

    label("loc_720F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7220")
    Jump("loc_723A")

    label("loc_7220")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7231")
    Jump("loc_723A")

    label("loc_7231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_723A")

    label("loc_723A")

    TalkEnd(0xFE)
    Return()

    # Function_32_71D5 end

    def Function_33_723E(): pass

    label("Function_33_723E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_72F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725C")
    Call(0, 34)
    Jump("loc_72ED")

    label("loc_725C")


    ChrTalk(
        0x1C,
        (
            "#01109FOkay, Zeit. Jump over\x01",
            "Shizuku this time!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1B,
        "#01203FGrrrowl...woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#01106F..."It's dangerous so\x01",
            "I won't"? Hmm, I see.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_72ED")

    Jump("loc_731D")

    label("loc_72F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7303")
    Jump("loc_731D")

    label("loc_7303")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7314")
    Jump("loc_731D")

    label("loc_7314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_731D")

    label("loc_731D")

    TalkEnd(0xFE)
    Return()

    # Function_33_723E end

    def Function_34_7321(): pass

    label("Function_34_7321")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1C,
        (
            "#01100FAlright Shizuku, go\x01",
            "ahead and try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#06005FYeah, umm...\x02\x03",
            "#06000F...Mr. Zeit, your paw.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "#01200FWoof. (*paws*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#06005FWah... Zeit is really smart.\x02\x03",
            "#06002FUh uh, and his paw\x01",
            "pads are really soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#01109FI know, right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    OP_4C(0x1C, 0xFF)
    OP_4C(0x1D, 0xFF)
    OP_4C(0x1B, 0xFF)
    Return()

    # Function_34_7321 end

    def Function_35_7437(): pass

    label("Function_35_7437")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_74B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7455")
    Call(0, 34)
    Jump("loc_74AC")

    label("loc_7455")


    ChrTalk(
        0x1D,
        (
            "#06002FUh uh, you're really\x01",
            "smart, aren't you, Zeit?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1B, 0xFF)

    ChrTalk(
        0x1B,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1B, 0xFF)

    label("loc_74AC")

    Jump("loc_74DC")

    label("loc_74B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_74C2")
    Jump("loc_74DC")

    label("loc_74C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_74D3")
    Jump("loc_74DC")

    label("loc_74D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_74DC")

    label("loc_74DC")

    TalkEnd(0xFE)
    Return()

    # Function_35_7437 end

    def Function_36_74E0(): pass

    label("Function_36_74E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_7561")

    ChrTalk(
        0xFE,
        (
            "Since we're here we decided\x01",
            "to stop by Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I wonder how much\x01",
            "of it we'll be able to see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7601")

    label("loc_7561")


    ChrTalk(
        0xFE,
        (
            "Uh uh. Compared to Crossbell,\x01",
            "that place has a totally\x01",
            "different atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was noisy over in Entertainment\x01",
            "District, but it's pretty chill here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7601")

    TalkEnd(0xFE)
    Return()

    # Function_36_74E0 end

    def Function_37_7605(): pass

    label("Function_37_7605")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_765F")

    ChrTalk(
        0xFE,
        (
            "We decided to\x01",
            "go to Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to ride\x01",
            "the ferris wheel!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76B8")

    label("loc_765F")


    ChrTalk(
        0xFE,
        (
            "Hey mama...\x01",
            "This place is boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's hurry and go back to that shiny place.\x02",
    )

    CloseMessageWindow()

    label("loc_76B8")

    TalkEnd(0xFE)
    Return()

    # Function_37_7605 end

    def Function_38_76BC(): pass

    label("Function_38_76BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_781B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7795")

    ChrTalk(
        0xFE,
        (
            "There is no such thing as unending rain...\x01",
            "And no such thing as a forever cloudy sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I was trying to say\x01",
            "a nice thing but I couldn't\x01",
            "put it well on words.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7816")

    label("loc_7795")


    ChrTalk(
        0xFE,
        (
            "There is no such thing as unending rain...\x01",
            "And no such thing as an ever-full stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Hey, that made it even worse.\x02",
    )

    CloseMessageWindow()

    label("loc_7816")

    Jump("loc_78E6")

    label("loc_781B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_78E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_END)), "loc_788A")

    ChrTalk(
        0xFE,
        "A little girl with an umbrella...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I saw\x01",
            "one just now...\x01",
            "Or maybe not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78E6")

    label("loc_788A")


    ChrTalk(
        0xFE,
        (
            "Just what shape do\x01",
            "raindrops have, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Maybe I can see it if I squint?\x02",
    )

    CloseMessageWindow()

    label("loc_78E6")

    TalkEnd(0xFE)
    Return()

    # Function_38_76BC end

    def Function_39_78EA(): pass

    label("Function_39_78EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A07")

    ChrTalk(
        0xFE,
        (
            "Before long, the heads of state will\x01",
            "depart for Michelam from right here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While they're in the tower, we're going\x01",
            "over our blockade structure again here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business in the business\x01",
            "district, finish it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, understood.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7AB6")

    label("loc_7A07")


    ChrTalk(
        0xFE,
        (
            "Ever since the heads of state arrived from Michelam, \x01",
            "we've been reviewing our blockade structure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have business in the business\x01",
            "district, finish it quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AB6")

    TalkEnd(0xFE)
    Return()

    # Function_39_78EA end

    def Function_40_7ABA(): pass

    label("Function_40_7ABA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B69")

    ChrTalk(
        0xFE,
        (
            "Terrorists, huh... Though we\x01",
            "thought about them before,\x01",
            "it's likely they'll come here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, all we can do is\x01",
            "proceed per direction from HQ.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1A")

    label("loc_7B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7C34")

    ChrTalk(
        0xFE,
        "An event featuring Michey, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, they got proper\x01",
            "permission from the city,\x01",
            "so I don't see a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But this must be what they call\x01",
            "the M. W. L. service spirit, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1A")

    label("loc_7C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7D1A")

    ChrTalk(
        0xFE,
        (
            "Investigation into the actions of "Heiyue" is outside the\x01",
            "jurisdiction of the District Crime Prevention Section,\x01",
            "but... We of course need to remain on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I don't think they'll\x01",
            "do something publically.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1A")

    TalkEnd(0xFE)
    Return()

    # Function_40_7ABA end

    def Function_41_7D1E(): pass

    label("Function_41_7D1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7E62")

    ChrTalk(
        0xFE,
        (
            "Though the Heiyue office was completely\x01",
            "destroyed, it looks like this place was\x01",
            "mostly repaired in just a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And because of the upcoming\x01",
            "referendum, it seems not that\x01",
            "many citizens are depressed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think we'll feel the power of those who make\x01",
            "up their minds at the last minute, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D1")

    label("loc_7E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7F14")

    ChrTalk(
        0xFE,
        (
            "Some of them are in the city,\x01",
            "but most of the heads of\x01",
            "state are still at Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's talk of terrorists too. We\x01",
            "need to pay attention to security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D1")

    label("loc_7F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7FDA")

    ChrTalk(
        0xFE,
        (
            "It seems Chancellor Osborne is\x01",
            "visiting Michelam and President\x01",
            "Rocksmith is visiting IBC...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're each under heavy guard. No need\x01",
            "to worry about either for now, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80D1")

    label("loc_7FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_80D1")

    ChrTalk(
        0xFE,
        (
            "I'm standing by here so I\x01",
            "can rush in with my patrol\x01",
            "car if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though it won't stand up to the CGF armored cars,\x01",
            "it's tough and equipped with bulletproof glass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If necessary, it can also\x01",
            "be used as a shield.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D1")

    TalkEnd(0xFE)
    Return()

    # Function_41_7D1E end

    def Function_42_80D5(): pass

    label("Function_42_80D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_81C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_814D")

    ChrTalk(
        0x24,
        (
            "Thank you for using\x01",
            "the water bus today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "We will be waiting for\x01",
            "your next visit!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81C1")

    label("loc_814D")


    ChrTalk(
        0x24,
        (
            "The Michelam bound water\x01",
            "bus will soon depaaart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Visitors who are going to use it,\x01",
            "please embark quiiick!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81C1")

    Jump("loc_8250")

    label("loc_81C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_END)), "loc_8250")

    ChrTalk(
        0xFE,
        (
            "The Michelam-bound water bus\x01",
            "will be arriving shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll now begin the boarding\x01",
            "process. Line up and wait, please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8250")

    TalkEnd(0xFE)
    Return()

    # Function_42_80D5 end

    def Function_43_8254(): pass

    label("Function_43_8254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_83E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8350")

    ChrTalk(
        0xFE,
        (
            "The city's on high alert, but...\x01",
            "It's strangely\x01",
            "calm like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what kind of storm will the\x01",
            "heat of the Trade Conference create?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might not be too bad to spend the\x01",
            "day lost in idle thought like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_83E9")

    label("loc_8350")


    ChrTalk(
        0xFE,
        (
            "Just what kind of storm will the\x01",
            "heat of the Trade Conference create?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It might not be too bad to spend the\x01",
            "day lost in idle thought like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83E9")

    TalkEnd(0xFE)
    Return()

    # Function_43_8254 end

    def Function_44_83ED(): pass

    label("Function_44_83ED")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84E3")
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Heiyue Trade Company - Crossbell Branch"\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_84E6")

    label("loc_84E3")

    Call(0, 72)

    label("loc_84E6")

    Jump("loc_894F")

    label("loc_84EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8774")
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(20370, 0, 19380, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(20290, 0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x109, 18600, 0, 16600, 0)
    SetChrPos(0x105, 19700, 0, 16600, 0)
    SetChrPos(0x104, 19100, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Heiyue Trade Company - Crossbell Branch"\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00003F...Looks like\x01",
            "we're out of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FGuess so. Let's give up\x01",
            "and go somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Showing Shing Around The City]\x07\x00",
            " failed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x73, 0x1, 0xF)
    OP_29(0x73, 0x4, 0x40)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18910, 0, 13080, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Jump("loc_883C")

    label("loc_8774")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Heiyue Trade Company - Crossbell Branch"\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_883C")

    Jump("loc_894F")

    label("loc_8841")

    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Heiyue Trade Company - Crossbell Branch"\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_894F")

    ChrTalk(
        0x101,
        (
            "#00003FWe can't really enter\x01",
            "in such a place...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_894F")

    TalkEnd(0xFF)
    Return()

    # Function_44_83ED end

    def Function_45_8953(): pass

    label("Function_45_8953")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B55")

    ChrTalk(
        0x1A2,
        "Hmm, Crossbell Times, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...Oh yeah, their main office\x01",
            "is in this same Waterfront Area.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_89E9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89E9)

    def lambda_89F6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89F6)

    ChrTalk(
        0x101,
        "#00005F? Did you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Hmph, not really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "If pushed, I'd say I really\x01",
            "can't like the reporters\x01",
            "who snoop around our place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Even Republic financiers\x01",
            "order their finance magazine,\x01",
            "so that of course has value.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Hmm, what to say...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes. That's quite a young\x01",
            "age to sense such things.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_8BA2")

    label("loc_8B55")


    ChrTalk(
        0x1A2,
        (
            "Crossbell News will probably\x01",
            "turn us away, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Let's get going.\x02",
    )

    CloseMessageWindow()

    label("loc_8BA2")

    TalkEnd(0xFF)
    Return()

    # Function_45_8953 end

    def Function_46_8BA6(): pass

    label("Function_46_8BA6")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(75920, 0, 7460, 1500)
    MoveCamera(45, 24, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(11500, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C66")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_8C66")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_46_8BA6 end

    def Function_47_8C6B(): pass

    label("Function_47_8C6B")

    EventBegin(0x0)
    SoundLoad(483)
    Fade(500)
    OP_68(41500, -1500, -18000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 40400, -2500, -18600, 90)
    SetChrPos(0x102, 40200, -2500, -17400, 90)
    SetChrPos(0x103, 39300, -2500, -18600, 90)
    SetChrPos(0x104, 39100, -2500, -17400, 90)
    SetChrPos(0x109, 41400, -2500, -15600, 135)
    SetChrPos(0x105, 40200, -2500, -15600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x18, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9118")

    ChrTalk(
        0x18,
        "#11POh, you're from the Special Support Section, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes. Thank you for your\x01",
            "hard work in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PThank you very much for\x01",
            "getting this ready for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PNo, no, this is\x01",
            "my job, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11POh yeah, are you all right operating it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PI can operate it for you\x01",
            "if necessary, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FOh right, I forgot about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6PWell, if you can drive a car, I don't\x01",
            "think you'd have much trouble with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FShould we contact the\x01",
            "Chief with the ENIGMA?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#10105FNo, it's fine.\x02\x03",
            "#10100FI have experience operating\x01",
            "this kind of boat, you see.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FB4():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8FB4)
    Sleep(50)

    def lambda_8FC4():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8FC4)
    Sleep(50)

    def lambda_8FD4():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8FD4)
    Sleep(50)

    def lambda_8FE4():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8FE4)
    Sleep(50)

    def lambda_8FF4():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8FF4)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        "#12P#00002FOh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FHa ha, that's our Noｱl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FLooks like driving and navigating\x01",
            "are your forte, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10112FUh uh, this too is thanks to\x01",
            "Commander Sonya's training.\x02\x03",
            "#10100F──What do we do?\x01",
            "Is it time to board?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x165, 1)
    Jump("loc_915D")

    label("loc_9118")

    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#5P#10100F──What do we do?\x01",
            "Is it time to board?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    label("loc_915D")


    ChrTalk(
        0x101,
        (
            "#12P#00003FLet's see...\x02\x03",
            "#00008F(We have no idea what's out there. Also, I\x01",
            "wonder if we've left anything undone here.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When you board the boat and head for\x01",
            "your destination, you will not be able\x01",
            "to leave for the rest of the chapter.\x02\x03",
            "Quests and activities will close,\x01",
            "so please be aware of that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[We Still Have Things to Do]\x01",      # 0
            "[Head for the Marshlands]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_9323"),
        (0, "loc_9514"),
        (SWITCH_DEFAULT, "loc_959A"),
    )


    label("loc_9323")


    ChrTalk(
        0x109,
        "#5P#10102FRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PWell then, be\x01",
            "careful out there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51104.itc", 0x28)
    LoadEffect(0x0, "event\\ev315_00.eff")
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, 41600, -3700, -22500, 90)
    SetChrPos(0x101, 41200, -3700, -23500, 90)
    SetChrPos(0x102, 40200, -3100, -21700, 90)
    SetChrPos(0x103, 39200, -3100, -23700, 90)
    SetChrPos(0x104, 38400, -3100, -22500, 90)
    SetChrPos(0x105, 38400, -3100, -21500, 90)
    SetChrFlags(0x18, 0x8000)

    def lambda_9406():

        label("loc_9406")

        TurnDirection(0xFE, 0x33, 500)
        Yield()
        Jump("loc_9406")

    QueueWorkItem2(0x18, 2, lambda_9406)
    OP_68(40000, -2500, -22500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(17500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0xBB8, 0x7D0)
    BeginChrThread(0x33, 3, 0, 51)
    BeginChrThread(0x2F, 1, 0, 49)
    Sleep(2000)
    OP_68(50000, -2500, -22500, 5000)
    MoveCamera(70, 10, 0, 5000)
    SetCameraDistance(27500, 5000)
    BeginChrThread(0x33, 0, 0, 48)
    OP_6F(0x79)
    WaitChrThread(0x33, 0)
    StopBGM(0x1B58)
    OP_68(22140, 4000, 20700, 6000)
    MoveCamera(37, 21, 0, 6000)
    SetCameraDistance(26000, 6000)
    OP_6F(0x79)
    Sleep(300)
    SetCameraDistance(22000, 3000)
    Sleep(2000)
    StopSound(126, 1000, 50)
    StopSound(128, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x18, 0x2)
    WaitBGM()
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 0)
    NewScene("c1210", 0, 0, 0)
    IdleLoop()
    Jump("loc_959A")

    label("loc_9514")


    ChrTalk(
        0x109,
        "#5P#10100FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11PAlright then, just let me\x01",
            "know when you're ready.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 40000, -2500, -18000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x18, 0xFF)
    EventEnd(0x5)
    Jump("loc_959A")

    label("loc_959A")

    Return()

    # Function_47_8C6B end

    def Function_48_959B(): pass

    label("Function_48_959B")

    OP_96(0x33, 0xA410, 0xFFFFF060, 0xFFFFA81C, 0xBB8, 0x0)

    def lambda_95B4():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_95B4)
    Sleep(1000)

    def lambda_95D2():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_95D2)
    Sleep(1000)

    def lambda_95F0():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1770, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_95F0)
    Sleep(1000)

    def lambda_960E():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_960E)

    def lambda_961B():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_961B)

    def lambda_9628():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9628)

    def lambda_9635():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9635)

    def lambda_9642():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9642)

    def lambda_964F():
        OP_93(0xFE, 0x87, 0x1388)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_964F)

    def lambda_965C():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_965C)
    Sleep(1000)

    def lambda_967A():
        OP_9E(0xFE, 0xA410, 0xFFFE96AC, 0x7530, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_967A)
    WaitChrThread(0x33, 1)
    Return()

    # Function_48_959B end

    def Function_49_9695(): pass

    label("Function_49_9695")

    Sound(470, 0, 100, 0)
    Sound(482, 0, 60, 0)
    Sleep(5000)
    Sound(483, 2, 100, 0)
    Sleep(4000)
    StopSound(483, 2000, 90)
    Return()

    # Function_49_9695 end

    def Function_50_96B4(): pass

    label("Function_50_96B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(483)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("apl/ch51104.itc", 0x28)
    LoadChrToIndex("chr/ch00001.itc", 0x29)
    LoadChrToIndex("chr/ch00101.itc", 0x2A)
    LoadEffect(0x0, "event\\ev315_00.eff")
    OP_68(39650, -1200, -36850, 0)
    MoveCamera(56, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16610, 0)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0x33)
    SetChrPos(0x33, 50980, -4000, -30210, 270)
    OP_D5(0x33, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x18, 0xFF)
    SetChrPos(0x109, 49200, -3700, -30160, 270)
    SetChrPos(0x101, 53730, -3100, -29070, 1)
    SetChrPos(0x102, 51850, -3100, -29370, 270)
    SetChrPos(0x103, 52260, -3100, -30360, 300)
    SetChrPos(0x104, 50980, -3100, -30930, 270)
    SetChrPos(0x105, 53510, -3100, -31010, 280)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 42410, -2500, -18000, 180)
    OP_68(38240, -1200, -24640, 6000)
    MoveCamera(26, 25, 0, 6000)
    OP_6E(600, 5000)
    SetCameraDistance(16610, 5000)
    BeginChrThread(0x33, 0, 0, 54)
    BeginChrThread(0x33, 3, 0, 51)
    BeginChrThread(0x2F, 1, 0, 55)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    TurnDirection(0x104, 0x18, 0)
    Sleep(120)
    TurnDirection(0x102, 0x18, 0)
    Sleep(120)
    TurnDirection(0x105, 0x18, 0)
    Sleep(90)
    TurnDirection(0x103, 0x18, 0)
    Sleep(900)
    OP_93(0x102, 0x1E, 0x0)
    Sleep(300)
    Sleep(300)
    Sleep(150)
    EndChrThread(0x33, 0x3)
    WaitChrThread(0x33, 0)
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 52)
    Sleep(400)
    BeginChrThread(0x102, 1, 0, 53)
    Sleep(300)

    def lambda_9899():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9899)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x18, 0)
    Sleep(120)
    TurnDirection(0x18, 0x101, 0)

    def lambda_98C3():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_98C3)
    Sleep(100)

    def lambda_98DB():
        OP_9B(0x0, 0xFE, 0x5, 0x258, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_98DB)
    WaitChrThread(0x102, 1)

    def lambda_98F4():
        OP_9B(0x0, 0xFE, 0xF, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98F4)
    Sleep(800)
    Fade(1000)
    OP_68(38180, 0, -21930, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11490, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x101, 41000, -2500, -17960, 91)
    SetChrPos(0x102, 42180, -2500, -14850, 172)
    SetChrPos(0x103, 40190, -2500, -15950, 127)
    SetChrPos(0x104, 37640, -2500, -16670, 127)
    SetChrPos(0x109, 39080, -2500, -19420, 80)
    SetChrPos(0x105, 38110, -2500, -18360, 81)
    TurnDirection(0x18, 0x101, 0)
    OP_0D()
    Sleep(600)
    Sleep(300)
    OP_93(0x101, 0x0, 0x0)
    Sleep(300)
    OP_68(36420, 0, -4160, 6000)
    MoveCamera(39, 25, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(31000, 8000)

    def lambda_9A07():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A07)
    Sleep(60)

    def lambda_9A24():
        OP_95(0xFE, 37490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A24)
    Sleep(30)
    TurnDirection(0x18, 0x101, 500)

    def lambda_9A48():
        OP_95(0xFE, 38490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A48)
    Sleep(30)

    def lambda_9A65():
        OP_95(0xFE, 37990, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9A65)

    def lambda_9A7F():
        OP_95(0xFE, 39490, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A7F)
    Sleep(30)

    def lambda_9A9C():
        OP_95(0xFE, 38290, -2500, -790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A9C)
    Sleep(600)
    Sleep(300)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1E3)
    SetScenarioFlags(0x22, 2)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_96B4 end

    def Function_51_9AD5(): pass

    label("Function_51_9AD5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B1F")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_51_9AD5")

    label("loc_9B1F")

    Return()

    # Function_51_9AD5 end

    def Function_52_9B20(): pass

    label("Function_52_9B20")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x2)
    OP_9C(0xFE, 0xFFFFFE0C, 0xFFFFFC18, 0x9C4, 0x3E8, 0x5DC)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_52_9B20 end

    def Function_53_9B81(): pass

    label("Function_53_9B81")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x2)
    OP_9C(0xFE, 0xFFFFFE0C, 0xFFFFFC18, 0x9C4, 0x3E8, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_53_9B81 end

    def Function_54_9BE2(): pass

    label("Function_54_9BE2")

    OP_96(0x33, 0x9858, 0xFFFFF060, 0xFFFFA36C, 0x7D0, 0x0)
    TurnDirection(0x18, 0x33, 0)
    OP_96(0x33, 0x96C8, 0xFFFFF060, 0xFFFFA81C, 0x3E8, 0x0)
    Return()

    # Function_54_9BE2 end

    def Function_55_9C12(): pass

    label("Function_55_9C12")

    Sound(483, 2, 100, 0)
    Sleep(3000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sound(477, 0, 50, 0)
    Sleep(1000)
    Sound(484, 0, 70, 0)
    Sleep(4000)
    Sound(478, 0, 50, 0)
    Return()

    # Function_55_9C12 end

    def Function_56_9C40(): pass

    label("Function_56_9C40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44100.itc", 0x28)
    LoadChrToIndex("chr/ch47500.itc", 0x29)
    LoadChrToIndex("chr/ch23600.itc", 0x2A)
    SetChrChipByIndex(0x29, 0x28)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 0, 0, 11000, 180)
    SetChrChipByIndex(0x2A, 0x29)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -1000, 0, 9000, 45)
    SetChrChipByIndex(0x2B, 0x2A)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 1000, 0, 9000, 270)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x2C)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x2C, 4000, 0, 11000, 90)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    OP_78(0xB, 0x2D)
    OP_49()
    SetChrPos(0x2D, -48000, 2000, 23520, 90)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-6940, 5850, 2500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6780, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x2A,
        (
            "Maaan, speeding around this\x01",
            "vast city is the best, huh.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    ChrTalk(
        0x2A,
        (
            "Your driving has improved a lot,\x01",
            "you know that Reggie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "Hehe, I know, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x29, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Well, it's also because\x01",
            "of the high performance\x01",
            "of Yuri's car, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x29, 500)
    Sleep(50)

    ChrTalk(
        0x29,
        (
            "Heheh, damn straight. \x01",
            "It's Verne Corp.'s latest model,\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "...More importantly, Reggie.\x01",
            "You almost hit that middle-aged\x01",
            "man on the highway, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "Y-Yeah... I just barely\x01",
            "missed him somehow, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "But... Did you see the\x01",
            "look on his face!?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x29)
    OP_64(0x2A)
    OP_64(0x2B)

    ChrTalk(
        0x29,
        "#4S#1K#1P...Awesome!\x02",
    )


    ChrTalk(
        0x2A,
        "#4S#1K#3PYeah, awesome!!\x02",
    )


    ChrTalk(
        0x2B,
        "#4S#1K#2PYeah man, awesome!!\x02",
    )

    OP_57(0x1)
    OP_5A()
    OP_63(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x29)
    OP_64(0x2A)
    OP_64(0x2B)

    ChrTalk(
        0x2A,
        (
            "Wahahaha! \x01",
            "That old man was\x01",
            "scared silly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "Y-You'll run me over!!\x01",
            "Save me!! Right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Ahahaha! S-Stop it\x01",
            "Sykes! My belly's\x01",
            "going to burst!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Hu hu... Well, we'll be\x01",
            "here awhile so might\x01",
            "as well enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "Our new playground...\x01",
            "That's this Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-34730, 5840, 17160, 0)
    MoveCamera(332, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    Sound(457, 0, 100, 0)

    def lambda_A246():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_A246)
    OP_68(-29600, 5840, 16660, 2000)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_6F(0x1)
    OP_0D()
    Sleep(1200)
    StopSound(457, 1000, 100)
    Fade(500)
    OP_68(-6940, 5850, 2500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(6780, 0)
    OP_93(0x29, 0x13B, 0x0)
    OP_93(0x2A, 0x13B, 0x0)
    OP_93(0x2B, 0x13B, 0x0)
    OP_0D()
    Sleep(50)

    ChrTalk(
        0x29,
        (
            "Whoops... Looks like\x01",
            "the cops are here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(50)

    ChrTalk(
        0x2A,
        "Reggie, floor it!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)
    Sleep(50)

    ChrTalk(
        0x2B,
        (
            "Okay, shaking those guys off\x01",
            "will be like a walk in the park!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    BeginChrThread(0x2B, 1, 0, 58)
    Sleep(100)
    BeginChrThread(0x29, 1, 0, 59)
    Sleep(100)
    BeginChrThread(0x2A, 1, 0, 60)
    Sleep(800)
    Sound(485, 0, 100, 0)
    Sleep(50)
    Sound(100, 0, 50, 0)
    OP_71(0xC, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0xA)
    Sleep(500)
    WaitChrThread(0x2B, 1)

    def lambda_A3B5():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A3B5)

    def lambda_A3CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A3CA)
    WaitChrThread(0x2B, 2)
    Sleep(100)
    WaitChrThread(0x29, 1)

    def lambda_A3E6():
        OP_9B(0x0, 0xFE, 0xB4, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_A3E6)

    def lambda_A3FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A3FB)
    Sleep(100)
    WaitChrThread(0x2A, 1)

    def lambda_A413():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A413)

    def lambda_A428():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A428)
    Sleep(100)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x29, 2)
    WaitChrThread(0x2A, 1)
    WaitChrThread(0x2A, 2)
    Sound(100, 0, 50, 0)
    OP_71(0xC, 0x1F, 0x3C, 0x1, 0x0)
    Sleep(500)
    Sound(485, 0, 100, 0)
    OP_79(0xA)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1C3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xC, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, 11000, 90)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_74(0xC, 0x1E)
    Sound(470, 0, 50, 0)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    OP_0D()
    Sleep(800)
    BeginChrThread(0x2C, 1, 0, 57)
    Sleep(100)
    OP_68(18560, 1210, 10040, 1500)
    SetCameraDistance(30470, 1500)
    OP_6F(0x79)
    Sleep(50)
    OP_68(17250, 1210, -8950, 1200)
    OP_6F(0x1)
    Sleep(50)
    OP_68(-17400, 1210, -12130, 2500)
    OP_6F(0x1)
    WaitChrThread(0x2C, 1)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    OP_0D()
    Sleep(200)
    SetScenarioFlags(0x22, 6)
    NewScene("c1000", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_56_9C40 end

    def Function_57_A558(): pass

    label("Function_57_A558")

    Sound(494, 0, 100, 0)
    OP_98(0x2C, 0x3A98, 0x0, 0x0, 0x2710, 0x0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, 19020, 0, 10300)
    OP_9F(0x1, 19750, 0, 6120)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    Sound(458, 0, 100, 0)
    OP_98(0x2C, 0x0, 0x0, 0xFFFFC568, 0x3A98, 0x0)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, 18580, 0, -9470)
    OP_9F(0x1, 14650, 0, -11440)
    OP_9F(0x1, 10980, 0, -11590)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    OP_98(0x2C, 0xFFFF9688, 0x0, 0x0, 0x4E20, 0x0)
    Sound(492, 0, 100, 0)
    OP_9F(0x0, 0x2C)
    OP_9F(0x1, -18160, 0, -11990)
    OP_9F(0x1, -19820, 0, -15120)
    OP_9F(0x1, -19650, 0, -17640)
    OP_9F(0x2, 0x2C, 11000, 0x6)
    OP_98(0x2C, 0x0, 0x0, 0xFFFFB1E0, 0x3A98, 0x0)
    Return()

    # Function_57_A558 end

    def Function_58_A658(): pass

    label("Function_58_A658")

    OP_93(0x2B, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2B, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x2B, 0x0, 0x1F4)
    Return()

    # Function_58_A658 end

    def Function_59_A676(): pass

    label("Function_59_A676")

    OP_93(0x29, 0x0, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0x9C4, 0xBB8, 0x0)
    OP_93(0x29, 0x5A, 0x3E8)
    OP_9B(0x0, 0x29, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x29, 0xB4, 0x1F4)
    Return()

    # Function_59_A676 end

    def Function_60_A6AA(): pass

    label("Function_60_A6AA")

    OP_93(0x2A, 0x0, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0xFA0, 0xBB8, 0x0)
    OP_93(0x2A, 0x5A, 0x3E8)
    OP_9B(0x0, 0x2A, 0x0, 0x1388, 0xBB8, 0x0)
    OP_93(0x2A, 0xB4, 0x1F4)
    Return()

    # Function_60_A6AA end

    def Function_61_A6DE(): pass

    label("Function_61_A6DE")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1470, 1330, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12810, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    OP_4B(0x19, 0xFF)
    OP_0D()

    ChrTalk(
        0x19,
        (
            "That Meiling... \x01",
            "I wonder where she went...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FUh excuse us, are you\x01",
            "Meiling's brother?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)

    ChrTalk(
        0x19,
        (
            "Yeah that's me...\x01",
            "You need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FUh, we're Crossbell\x01",
            "Police's SSS.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that\x01",
            "they are looking for\x01",
            "Momo's umbrella.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x19,
        "...Oh, I see.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Meiling took the wrong\x01",
            "umbrella, and I didn't\x01",
            "realize it either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "My bad. I'd like to return\x01",
            "it as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FOn that note...\x01",
            "Where's Meiling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWasn't she taking\x01",
            "a walk with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Actually, Meiling and I just\x01",
            "started playing hide and seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Though it's a pain in this\x01",
            "rain, she insisted and I\x01",
            "went along with it, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x19, 0x5A, 0x1F4)
    Sleep(1000)
    OP_93(0x19, 0xB4, 0x1F4)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            "She's an expert\x01",
            "at hiding...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I'm not great at searching, so I'm\x01",
            "not sure how soon I'll find her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI-I see...\x02\x03",
            "#00000FWell in that case,\x01",
            "how about we help\x01",
            "you find her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Oh, that would\x01",
            "be great!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "I think she's hiding\x01",
            "somewhere here\x01",
            "in Waterfront Area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Probably somewhere\x01",
            "well hidden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "It might not be that\x01",
            "easy to find her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu. Shall we take\x01",
            "a look around, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -330, -700, -3820, 0)
    OP_93(0x19, 0xB4, 0x0)
    OP_4C(0x19, 0xFF)
    ClearChrFlags(0x19, 0x10)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    ClearChrFlags(0x1A, 0x80)
    SetScenarioFlags(0x133, 4)
    OP_29(0x6B, 0x1, 0x2)
    OP_C9(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_61_A6DE end

    def Function_62_AC6C(): pass

    label("Function_62_AC6C")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00012FUnder the bench... She's not there,\x01",
            "no matter how I think about it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_62_AC6C end

    def Function_63_ACC3(): pass

    label("Function_63_ACC3")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        "#00000F...She's not behind the cart either.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_63_ACC3 end

    def Function_64_ACFB(): pass

    label("Function_64_ACFB")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00006FBehind the shipping container!\x01",
            "...Guess she's not here.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_64_ACFB end

    def Function_65_AD46(): pass

    label("Function_65_AD46")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FIt's hide-and-seek, so\x01",
            "she wouldn't be indoors.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -14030, 2000, 24980, 180)
    EventEnd(0x4)
    Return()

    # Function_65_AD46 end

    def Function_66_AD9B(): pass

    label("Function_66_AD9B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeiling should be somewhere\x01",
            "in Waterfront Area. ...\x01",
            "Let's search a little harder.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 4500, 3050, 30320, 180)
    EventEnd(0x4)
    Return()

    # Function_66_AD9B end

    def Function_67_AE12(): pass

    label("Function_67_AE12")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeiling should be somewhere\x01",
            "in Waterfront Area. ...\x01",
            "Let's search a little harder.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -19940, 0, -25710, 359)
    EventEnd(0x4)
    Return()

    # Function_67_AE12 end

    def Function_68_AE89(): pass

    label("Function_68_AE89")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FMeiling should be somewhere\x01",
            "in Waterfront Area. ...\x01",
            "Let's search a little harder.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -25570, 2000, 23250, 90)
    EventEnd(0x4)
    Return()

    # Function_68_AE89 end

    def Function_69_AF00(): pass

    label("Function_69_AF00")

    TalkBegin(0x19)

    ChrTalk(
        0x19,
        (
            "You guys. It looks like you\x01",
            "haven't found Meiling yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If you really can't find her,\x01",
            "I'll give the give up signal\x01",
            "and ask her to come out, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "...What do you want to do?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Give Up\x01",      # 0
            "Quit\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B26C")
    EventBegin(0x0)
    Fade(500)
    OP_68(-1470, 1330, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12810, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    OP_93(0x19, 0xB4, 0x0)
    OP_4B(0x19, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00006F...Sorry. If you please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Well, we're out of options.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "In that case...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x19,
        "#4SMEILING, I GIVE UUUP!!#3S\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x19, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    SetChrPos(0x1A, 2590, -700, -2880, 270)
    OP_4B(0x1A, 0xFF)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        "...Ehehe, Meiling's the winner!♪\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, Meiling appeared before Lloyd\x01",
            "and the others who had given up...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told Meiling\x01",
            "that she had grabbed\x01",
            "Momo's umbrella.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(0, 71)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B31F")

    label("loc_B26C")


    ChrTalk(
        0x101,
        "#00000FNo, we want to search a little more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "I see. Good luck, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "By the way, don't count on me\x01",
            "too much... Because the sun\x01",
            "would probably set by then.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B31F")

    TalkEnd(0x19)
    Return()

    # Function_69_AF00 end

    def Function_70_B323(): pass

    label("Function_70_B323")

    EventBegin(0x0)
    Fade(500)
    OP_68(87940, -800, 17550, 0)
    MoveCamera(307, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14760, 0)
    SetChrPos(0x101, 86200, -2500, 17950, 37)
    SetChrPos(0x102, 85470, -2500, 16990, 37)
    SetChrPos(0x109, 84630, -2500, 16160, 37)
    SetChrPos(0x105, 83750, -2500, 15320, 37)
    OP_4B(0x1A, 0xFF)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002FYou wouldn't happen to\x01",
            "be Meiling, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, got her.\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x1A,
        "Eek, I was found!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A,
        "Wait, you're not my big bro.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Who are you misters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FAhaha, finally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell then, let's\x01",
            "report to Roy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Call(0, 71)
    EventEnd(0x5)
    Return()

    # Function_70_B323 end

    def Function_71_B4DE(): pass

    label("Function_71_B4DE")

    EventBegin(0x0)
    ClearScenarioFlags(0x133, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch21500.itc", 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_B925")
    OP_2C(0x6B, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The team called Roy to\x01",
            "Meiling's hiding spot...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told Meiling\x01",
            "that she had grabbed\x01",
            "Momo's umbrella.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(67920, -400, 17980, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13970, 0)
    SetChrPos(0x101, 68760, -2500, 19500, 90)
    SetChrPos(0x102, 68760, -2500, 18300, 90)
    SetChrPos(0x109, 67600, -2500, 18300, 90)
    SetChrPos(0x105, 67600, -2500, 19500, 90)
    SetChrPos(0x19, 70770, -2500, 19500, 270)
    SetChrPos(0x1A, 70700, -2500, 18300, 270)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_29(0x6B, 0x1, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00000F....So that's what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I see...\x01",
            "Meiling made a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Meiling, let's return the umbrella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Okay, big bro.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Here you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FThen, this one's yours.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_9B(0x1, 0x1A, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x1A, 0xB4, 0x320, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x2)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave Meiling her umbrella,\x01",
            "and received Momo's.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#6P#00100F*giggle*, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Nuh-uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Then, later I'll have\x01",
            "to tell that kid named\x01",
            "Momo that I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10309FHu hu. She's very together\x01",
            "for a girl her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Hmm, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If I were like her,\x01",
            "I'd have one or two jobs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012FW-Well anyway, \x01",
            "thanks for your help.\x02\x03",
            "#00000FPlease allow us\x01",
            "to return the\x01",
            "other umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Alright, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Please do.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Jump("loc_BCC8")

    label("loc_B925")

    OP_68(-1470, 1230, -4340, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12830, 0)
    SetChrPos(0x101, -750, -690, -3500, 0)
    SetChrPos(0x102, 250, -700, -3730, 0)
    SetChrPos(0x109, -750, -480, -5190, 0)
    SetChrPos(0x105, 250, -520, -5100, 0)
    SetChrPos(0x19, 250, -700, -1650, 180)
    SetChrPos(0x1A, -750, -700, -1650, 180)
    OP_4B(0x19, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_29(0x6B, 0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000F....So that's what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I see...\x01",
            "Meiling made a mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Meiling, let's return the umbrella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Okay, big bro.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Here you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FThen, this one's yours.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(500)
    OP_9B(0x1, 0x1A, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x1A, 0xB4, 0x320, 0x5DC, 0x0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x1A, 0x2)
    SetChrSubChip(0x1A, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave Meiling her umbrella,\x01",
            "and received Momo's.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#12P#00100F*giggle*, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Nuh-uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Then, later I'll have\x01",
            "to tell that kid named\x01",
            "Momo that I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10309FHu hu. She's very together\x01",
            "for a girl her age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Hmm, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If I were like her,\x01",
            "I'd have one or two jobs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FW-Well anyway, \x01",
            "thanks for your help.\x02\x03",
            "#00000FPlease allow us\x01",
            "to return the\x01",
            "other umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Alright, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Please do.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)

    label("loc_BCC8")

    SetScenarioFlags(0x22, 0)
    NewScene("c0210", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_71_B4DE end

    def Function_72_BCD5(): pass

    label("Function_72_BCD5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06300.itc", 0x28)
    LoadChrToIndex("chr/ch31400.itc", 0x29)
    OP_68(20370, 0, 19380, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19230, 0)
    SetChrPos(0x101, 18600, 0, 17800, 0)
    SetChrPos(0x102, 19700, 0, 17800, 0)
    SetChrPos(0x109, 18600, 0, 16600, 0)
    SetChrPos(0x105, 19700, 0, 16600, 0)
    SetChrPos(0x104, 19100, 0, 15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x27, 0x28)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x27, 0x4)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 19100, 0, 21700, 180)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0x29)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 19100, 0, 21700, 180)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and there\x01",
            "is a message plate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Heiyue Trade Company - Crossbell Branch"\x01",
            "※Please knock if you have business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x109,
        (
            "#6P#10101F"Heiyue Trade Company"...\x02\x03",
            "#10103FUhm. The person who runs this\x01",
            "office is called Cao, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FCao Lee, also known as the "White\x01",
            "Orchid Dragon", is the sharpest and\x01",
            "most capable person in "Heiyue".\x02\x03",
            "#10300FWould you like to pay him a visit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FWell, we do have\x01",
            "prior experience\x01",
            "working together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FYeah...\x02\x03",
            "#00301FI wanted to ask a little about the\x01",
            "Revache building matter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FOn that subject, Heiyue too\x01",
            "had aims on that building, but...\x02\x03",
            "#00001FIn the end, it ended up being\x01",
            "usurped by the Crimson & Co....\x01",
            "I wonder why?\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 0, 100, 0)
    Sleep(500)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(500)

    ChrTalk(
        0x27,
        (
            "──Hu hu, yes, it was\x01",
            "really regrettable.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x27, 3, 0, 73)
    Sleep(700)
    BeginChrThread(0x28, 3, 0, 74)
    Sleep(300)

    def lambda_C1E9():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C1E9)
    Sleep(50)

    def lambda_C201():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C201)
    Sleep(50)

    def lambda_C219():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C219)
    Sleep(50)

    def lambda_C231():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C231)
    Sleep(50)

    def lambda_C249():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C249)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#00005FB-Branch Manager Cao...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03200FGood day, ladies and\x01",
            "gentlemen of the SSS.\x02\x03",
            "#03209FActually, this is perfect timing!\x02\x03",
            "To be honest, I wish to borrow some\x01",
            "of your time and ask you for a favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FA favor...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#03200FIf you don't mind,\x01",
            "could you hear me out?\x02\x03",
            "#03204FOf course, you don't\x01",
            "have to if you're busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x27, 0x0, 0x1F4)

    def lambda_C3DC():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C3DC)
    Sleep(500)

    def lambda_C3F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_C3F9)
    WaitChrThread(0x27, 1)
    OP_9B(0x1, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#12P#00005FW-Wait a...!?\x02",
    )

    CloseMessageWindow()
    OP_97(0x28, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x28,
        (
            "...We are deeply sorry about this.\x01",
            "We are in a bit of a pickle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "But, if you do have some spare\x01",
            "time, by all means contact us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x28,
        (
            "Our door won't be locked for the time being,\x01",
            "so feel free to come and go as you please.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x28, 0x0, 0x1F4)

    def lambda_C545():
        OP_97(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C545)
    Sleep(500)

    def lambda_C562():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C562)
    WaitChrThread(0x28, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x104)

    ChrTalk(
        0x105,
        (
            "#12P#10309FAhaha. They're actually\x01",
            "terrifyingly welcoming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWazy, I don't think you're that\x01",
            "great at describing others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FSo, what should we do now?\x01",
            "It doesn't seem like a trap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FShould we play along with their request?\x01",
            "We might end up gaining some more intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI wonder... \x01",
            "(We're busy too and it seems there's no\x01",
            "need to get involved with them forcibly.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x153, 4)
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x2, 0x1)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18600, 0, 17800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_72_BCD5 end

    def Function_73_C7DE(): pass

    label("Function_73_C7DE")


    def lambda_C7E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_C7E3)

    def lambda_C7F4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C7F4)
    WaitChrThread(0x27, 1)
    OP_93(0x27, 0xB4, 0x1F4)
    Return()

    # Function_73_C7DE end

    def Function_74_C815(): pass

    label("Function_74_C815")


    def lambda_C81A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C81A)

    def lambda_C82B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C82B)
    WaitChrThread(0x28, 1)
    OP_95(0x28, 18100, 0, 19500, 2000, 0x0)
    OP_93(0x28, 0xB4, 0x1F4)
    Return()

    # Function_74_C815 end

    def Function_75_C860(): pass

    label("Function_75_C860")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xF9, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_68(20340, 100, 18050, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(16510, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_C9E3")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x104, 19680, 0, 18250, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_C93B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_C93B)

    def lambda_C955():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C955)
    Sleep(100)

    def lambda_C972():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C972)
    Sleep(50)

    def lambda_C98F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C98F)
    Sleep(100)

    def lambda_C9AC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C9AC)
    Sleep(50)

    def lambda_C9C9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C9C9)
    Jump("loc_CC2A")

    label("loc_C9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_CB09")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x109, 19680, 0, 18250, 180)
    SetChrPos(0x104, 18460, 0, 19360, 180)
    SetChrPos(0x105, 19600, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_CA61():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CA61)

    def lambda_CA7B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA7B)
    Sleep(100)

    def lambda_CA98():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA98)
    Sleep(50)

    def lambda_CAB5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CAB5)
    Sleep(100)

    def lambda_CAD2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CAD2)
    Sleep(50)

    def lambda_CAEF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CAEF)
    Jump("loc_CC2A")

    label("loc_CB09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_CC2A")
    SetChrPos(0x1A2, 18700, 0, 16660, 180)
    SetChrPos(0x102, 19540, 0, 16660, 180)
    SetChrPos(0x101, 18440, 0, 18250, 180)
    SetChrPos(0x105, 19680, 0, 18250, 180)
    SetChrPos(0x104, 19600, 0, 19360, 180)
    SetChrPos(0x109, 18460, 0, 19360, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_CB87():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CB87)

    def lambda_CBA1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CBA1)
    Sleep(100)

    def lambda_CBBE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CBBE)
    Sleep(50)

    def lambda_CBDB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CBDB)
    Sleep(100)

    def lambda_CBF8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CBF8)
    Sleep(50)

    def lambda_CC15():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CC15)

    label("loc_CC2A")

    OP_68(20080, 600, 15520, 3000)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(560, 3000)
    SetCameraDistance(16390, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_CC69():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_CC69)
    Sleep(50)

    def lambda_CC79():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CC79)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PAlright then, I'll get started with\x01",
            "the details, so pay attention!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306F(This brat, he's tryin' to act\x01",
            "tough in front of milady.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100F(Yeah, and in a very natural way, though.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10302F(Hu hu, he really likes\x01",
            "Elie, doesn't he?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "#12PWhat, got anything to say to me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FOh, no. Everything's fine.\x02\x03",
            "#00000FPlease go ahead with\x01",
            "your explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "#12PHu hu. Then I'll get straight to the point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAs I was saying before, I'd like\x01",
            "you guys to be my tour guides\x01",
            "and show me around the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PThe more places I\x01",
            "can see in Crossbell,\x01",
            "the better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBeforehand, I've decided that there's a\x01",
            "main spot I should eventually visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FMain spot...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PYeah, I want to go to the roof of the\x01",
            "Times department store in Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAnyway, take me there last.\x01",
            "Then I'll call your duty complete.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FI see. That's easy to understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FBy the way, are we free to decide\x01",
            "the route to take you there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PNo. It'd be a problem if you\x01",
            "took me to boring areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PTake me to the department\x01",
            "store by way of East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHow to say this... You have this\x01",
            "all planned out, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PHeheh, it's a special\x01",
            "trip. This level of\x01",
            "planning is only natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PBut, I don't have any\x01",
            "other plans besides that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PAt least take different side trips \x01",
            "I can enjoy with Miss Elie.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#11P#00109FAh, I'll be your guide too, you see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#6PNonsense, that's out of the question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#6PYou've got to enjoy this experience\x01",
            "too miss, even if only a little!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#5P#10109FAhaha, he's\x01",
            "totally in love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell, I get the general idea, but...\x02\x03",
            "#00000FBased on this conversation, we're basically\x01",
            "just normally walking around town.\x02\x03",
            "Are you okay with that, Shing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D46F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_D46F)
    Sleep(50)

    def lambda_D47F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D47F)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#00305FYeah, are there any\x01",
            "other options?\x02\x03",
            "#00300FSuch as going to Arc-\x01",
            "en-ciel or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10300FYeah, or the\x01",
            "Michelam theme park.\x02\x03",
            "#10304FWell, it's closed right now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12P―Hmph. You know I've already been to\x01",
            "those kind of famous places, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PThose places are certainly fun, and\x01",
            "I think it'd be fun to go again, but...\x01",
            "That's not my goal this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PI need to know lots\x01",
            "more about Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PFor that reason, I must look\x01",
            "not at tourist attractions, but\x01",
            "at how Crossbell really is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FHow Crossbell really is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYou thought about this that much, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FMan oh man. I wonder\x01",
            "what he'll grow up to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12P―Anyway,\x01",
            "understand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "#12PTime is short, so begin\x01",
            "the tour right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FUnderstood. Let's get going, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_D87C")
    OP_29(0x73, 0x1, 0x1)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#00300FThen, we'll go on ahead and\x01",
            "stand guard behind the scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100FRoger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10300FHu hu, later.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D9E1")

    label("loc_D87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_D92F")
    OP_29(0x73, 0x1, 0x2)
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10100FThen, we'll go on ahead.\x01",
            "Leave the watch to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FAlright, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10300FHu hu, later.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    Jump("loc_D9E1")

    label("loc_D92F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_D9E1")
    OP_29(0x73, 0x1, 0x3)
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#12P#10300FThen, we'll go on ahead.\x01",
            "Leave the rear guard to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10100FRoger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00300FWell, be careful, ok?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)

    label("loc_D9E1")

    OP_C9(0x0, 0x1000)
    OP_1B(0x2, 0x0, 0x68)
    SetScenarioFlags(0x153, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 18910, 0, 13080, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_75_C860 end

    def Function_76_DA2F(): pass

    label("Function_76_DA2F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31400.itc", 0x28)
    SetChrChipByIndex(0x28, 0x28)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 19190, -10, 14710, 180)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_68(19890, 4500, 11900, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27560, 0)
    SetChrPos(0x1A2, 18620, -10, 3410, 0)
    SetChrPos(0x102, 19450, -10, 3400, 0)
    SetChrPos(0x101, 18970, -10, 1840, 0)
    SetChrPos(0x104, 17790, -10, 610, 0)
    SetChrPos(0x109, 20110, -10, 910, 0)
    SetChrPos(0x105, 19260, -10, -170, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x4)
    OP_68(19890, 2500, 11900, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_DB60():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_DB60)

    def lambda_DB7A():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB7A)
    Sleep(50)

    def lambda_DB97():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB97)
    Sleep(50)

    def lambda_DBB4():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DBB4)
    Sleep(50)

    def lambda_DBD1():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DBD1)
    Sleep(50)

    def lambda_DBEE():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBEE)
    WaitChrThread(0x105, 1)
    OP_93(0x28, 0x5A, 0x0)
    OP_9B(0x1, 0x28, 0xB4, 0x3E8, 0x7D0, 0x0)
    BeginChrThread(0x1A2, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 77)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 77)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 77)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 77)
    Sleep(3000)
    BeginChrThread(0x28, 3, 0, 77)
    WaitChrThread(0x28, 3)
    Sleep(700)
    Sound(104, 0, 80, 0)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    OP_68(19890, 4500, 11900, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_76_DA2F end

    def Function_77_DCCF(): pass

    label("Function_77_DCCF")

    OP_95(0xFE, 19190, -10, 14710, 2000, 0x0)

    def lambda_DCE8():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DCE8)
    Sleep(3000)

    def lambda_DD05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD05)
    Return()

    # Function_77_DCCF end

    def Function_78_DD12(): pass

    label("Function_78_DD12")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -150, -310, 6250, 135)
    SetChrPos(0x102, -1300, -470, 5330, 135)
    SetChrPos(0x109, -1630, -240, 6620, 135)
    SetChrPos(0x105, -510, -80, 7550, 135)
    SetChrPos(0x104, -2890, -500, 5170, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-330, 1870, 1930, 0)
    MoveCamera(46, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14900, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x34, 0x8000)
    OP_0D()
    SoundLoad(821)
    Call(0, 80)
    Return()

    # Function_78_DD12 end

    def Function_79_DDC2(): pass

    label("Function_79_DDC2")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, -260, -190, -6920, 45)
    SetChrPos(0x102, -1180, -350, -6000, 45)
    SetChrPos(0x109, -1910, -70, -7580, 45)
    SetChrPos(0x105, -720, -10, -8490, 45)
    SetChrPos(0x104, -2890, -260, -6510, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(510, 1150, -6710, 0)
    MoveCamera(25, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14220, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x34, 0x8000)
    OP_0D()
    SoundLoad(821)
    Call(0, 80)
    Return()

    # Function_79_DDC2 end

    def Function_80_DE72(): pass

    label("Function_80_DE72")

    Sound(821, 2, 40, 0)

    ChrTalk(
        0x101,
        "#12P#00000FIt seems to be very lively...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIt appears that today they're\x01",
            "holding a Michey's event.\x02\x03",
            "#00104FIt seems they're having an exhibition\x01",
            "instead because Michelam is closed\x01",
            "during the Trade Conference period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FUh uh, if Tio was here she'd\x01",
            "probably like to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FHa ha, it seems they're doing\x01",
            "a dance show right now...\x01",
            "Since we're here, why don't we go have a lo...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FWait, is that...!?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(5070, 1800, -2680, 4000)
    MoveCamera(42, 27, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(12260, 4000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7160", 0)
    SetScenarioFlags(0x2, 3)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x34, 0x20)
    BeginChrThread(0xF, 1, 0, 86)
    BeginChrThread(0x34, 1, 0, 87)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    ChrTalk(
        0x17,
        "#6P#11AEeek, Micheeey!\x02",
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Sleep(1700)
    ClearScenarioFlags(0x2, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x34, 1)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x34, 0x20)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 3)
    BeginChrThread(0xF, 0, 0, 81)
    BeginChrThread(0x34, 0, 0, 81)
    BeginChrThread(0x34, 2, 0, 84)
    BeginChrThread(0xF, 2, 0, 85)
    WaitChrThread(0x34, 2)
    WaitChrThread(0xF, 2)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x34, 0x20)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xF, 0xB4, 0x0)
    OP_93(0x34, 0xB4, 0x0)
    Sleep(200)
    BeginChrThread(0xF, 1, 0, 87)
    BeginChrThread(0x34, 1, 0, 86)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)

    ChrTalk(
        0x16,
        (
            "#6P#11AHa ha, the young man taking part in it on\x01",
            "the spur of the moment is quite good too!\x02",
        )
    )

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Sleep(1700)
    ClearScenarioFlags(0x2, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x34, 1)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x34, 0x20)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 3)
    BeginChrThread(0xF, 0, 0, 81)
    BeginChrThread(0x34, 0, 0, 81)
    BeginChrThread(0x34, 2, 0, 85)
    BeginChrThread(0xF, 2, 0, 84)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Sleep(3200)
    ClearScenarioFlags(0x2, 3)
    SetScenarioFlags(0x2, 3)

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Come on, everybody!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SEnjoooy, Michey☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x22)
    SetChrSubChip(0x34, 0x0)
    OP_0D()
    ClearScenarioFlags(0x2, 4)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xF, 0, 0, 83)
    BeginChrThread(0xF, 2, 0, 88)
    BeginChrThread(0x34, 2, 0, 89)
    WaitChrThread(0xF, 2)
    WaitChrThread(0x34, 2)
    ClearScenarioFlags(0x2, 3)
    ClearScenarioFlags(0x2, 4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 140, -1, -1)
    SetChrName("Tourists")

    AnonymousTalk(
        0xFF,
        "#4SEnjoooy!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("Tourists")

    AnonymousTalk(
        0xFF,
        "#4SMicheeeey☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Sleep(1200)
    OP_64(0x34)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    Fade(1000)
    OP_68(8000, 1800, -1810, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    ClearChrFlags(0x34, 0x2)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x21)
    SetChrSubChip(0x34, 0x0)
    OP_93(0x34, 0x10E, 0x0)
    SetChrPos(0x101, 2520, -700, -410, 90)
    SetChrPos(0x102, 2520, -700, -1650, 90)
    SetChrPos(0x109, 1430, -700, -2270, 90)
    SetChrPos(0x105, 1410, -700, -1020, 90)
    SetChrPos(0x104, 1440, -700, 200, 90)
    OP_0D()
    Sleep(500)

    def lambda_E5A0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E5A0)
    Sleep(10)

    def lambda_E5B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E5B0)
    WaitChrThread(0x34, 1)

    def lambda_E5C1():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E5C1)
    Sleep(10)

    def lambda_E5D9():
        OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E5D9)
    WaitChrThread(0x34, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Olivier and Michey exchanged\x01",
            "a solid and firm handshake. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x34,
        (
            "#12P#13909FHah hah ha...\x01",
            "I couldn't have expected less, Michey.\x02\x03",
            "#13902FYour dancing sense...\x01",
            "To put it bluntly, hats off to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, you too young man,\x01",
            "you were really good☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Where did you learn to dance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#12P#13904FHmph, I have a taste\x01",
            "for ballroom dancing.\x02\x03",
            "By nature, I'd like to elegantly\x01",
            "dance with a lady, but dancing\x01",
            "with you was quite enjoyable too.\x02\x03",
            "#13902FI guess I can say I couldn't have\x01",
            "expected less from Crossbell mascot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, you make me blush☆\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(1760, 1600, -3500, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12200, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00006F(W-What the heck is that guy doing...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300F(It seems he trespassed on stage...)\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(And Mr. Mueller asked to not\x01",
            "attract attention as much as possible...\x01",
            "Seems really impossible now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E9E5():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E9E5)
    Sleep(10)

    def lambda_E9FD():
        OP_9B(0x1, 0xFE, 0xB4, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_E9FD)
    WaitChrThread(0x34, 1)
    OP_93(0x34, 0x10E, 0x1F4)
    Fade(500)
    OP_68(8000, 1800, -1810, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    OP_0D()

    ChrTalk(
        0x34,
        (
            "#12P#13905FOh...\x01",
            "It seems they came to pick me up.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x34, 0x0, 0x1F4)
    OP_6F(0x79)

    ChrTalk(
        0x34,
        (
            "#12P#13900FMichey, I'm sorry but\x01",
            "I have to go now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "My my, that's a pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, next time you have to\x01",
            "absolutely come to Wonderland too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#12P#13902FHmph, one day...\x01",
            "I'll fulfill your request for sure.\x02\x03",
            "#13904FThis parting is too much painful.\x01",
            "That's why our bond will\x01",
            "become irreplaceable.\x02\x03",
            "#13913F...Adiｾs, amigo...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Byebye☆\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x20)
    SetChrChipByIndex(0x34, 0x22)
    SetChrSubChip(0x34, 0x0)
    OP_0D()
    BeginChrThread(0x34, 2, 0, 89)
    WaitChrThread(0x34, 2)
    OP_64(0x34)
    Fade(500)
    ClearChrFlags(0x34, 0x2)
    ClearChrFlags(0x34, 0x10)
    ClearChrFlags(0x34, 0x20)
    SetChrFlags(0x34, 0x40)
    SetChrChipByIndex(0x34, 0x21)
    SetChrSubChip(0x34, 0x0)
    OP_93(0x34, 0x0, 0x0)
    OP_0D()

    def lambda_EC4E():

        label("loc_EC4E")

        TurnDirection(0xFE, 0x34, 500)
        Yield()
        Jump("loc_EC4E")

    QueueWorkItem2(0xF, 2, lambda_EC4E)
    OP_68(8890, 1800, 4180, 2000)
    OP_95(0x34, 10730, -700, 580, 4000, 0x0)
    OP_95(0x34, 10620, -700, 3010, 5000, 0x0)
    Sound(809, 0, 70, 0)
    OP_9D(0x34, 0x28DC, 0x0, 0x2440, 0xBB8, 0xBB8)
    Sound(30, 0, 100, 0)
    EndChrThread(0xF, 0x2)
    OP_95(0x34, 4950, 0, 15760, 4000, 0x0)
    SetChrFlags(0x34, 0x80)
    OP_6F(0x1)
    StopBGM(0xFA0)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x105, 0x0, 0x0)
    Fade(1000)
    OP_68(2820, 1800, -3080, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12910, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00011FAah...\x01",
            "H-He ran away again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FOh boy, somehow he's\x01",
            "accustomed to it, eh?\x02\x03",
            "#10300FNow that it's come to this, I think we\x01",
            "can narrow down to a certain extent\x01",
            "the places where he could flee too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106FA-At any rate, let's follow him!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 1570, -700, -240, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetScenarioFlags(0x156, 3)
    OP_29(0x76, 0x1, 0x3)
    SetChrPos(0xF, 9480, -700, 160, 270)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xF, 0xFF)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    StopSound(821, 1000, 30)
    EventEnd(0x5)
    Return()

    # Function_80_DE72 end

    def Function_81_EEDC(): pass

    label("Function_81_EEDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_EEF8")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_81_EEDC")

    label("loc_EEF8")

    Return()

    # Function_81_EEDC end

    def Function_82_EEF9(): pass

    label("Function_82_EEF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_EF15")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_82_EEF9")

    label("loc_EF15")

    Return()

    # Function_82_EEF9 end

    def Function_83_EF16(): pass

    label("Function_83_EF16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_EF32")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_83_EF16")

    label("loc_EF32")

    Return()

    # Function_83_EF16 end

    def Function_84_EF33(): pass

    label("Function_84_EF33")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFF5D8, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    OP_96(0xFE, 0x1FF4, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    Return()

    # Function_84_EF33 end

    def Function_85_EFA6(): pass

    label("Function_85_EFA6")

    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x834, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0x258, 0x7D0, 0x0)
    OP_96(0xFE, 0x28F0, 0xFFFFFD44, 0xFFFFFF06, 0x7D0, 0x0)
    OP_96(0xFE, 0x2472, 0xFFFFFD44, 0xFFFFFC18, 0x7D0, 0x0)
    Return()

    # Function_85_EFA6 end

    def Function_86_F019(): pass

    label("Function_86_F019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_F12C")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(100)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    Jump("Function_86_F019")

    label("loc_F12C")

    Return()

    # Function_86_F019 end

    def Function_87_F12D(): pass

    label("Function_87_F12D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_F240")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(100)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x2, 4)
    BeginChrThread(0xFE, 0, 0, 82)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x2, 4)
    Jump("Function_87_F12D")

    label("loc_F240")

    Return()

    # Function_87_F12D end

    def Function_88_F241(): pass

    label("Function_88_F241")

    Sound(809, 0, 80, 0)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0x10E, 0x0)
    Return()

    # Function_88_F241 end

    def Function_89_F266(): pass

    label("Function_89_F266")

    OP_63(0xFE, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(130)
    Sound(822, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(130)
    SetChrSubChip(0xFE, 0x4)
    Sleep(130)
    SetChrSubChip(0xFE, 0x5)
    Sleep(130)
    SetChrSubChip(0xFE, 0x6)
    Sleep(130)
    SetChrSubChip(0xFE, 0x7)
    Return()

    # Function_89_F266 end

    def Function_90_F2B4(): pass

    label("Function_90_F2B4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-12070, 2500, 10460, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(15780, 0)
    SetChrPos(0x101, -9870, 0, 11840, 0)
    SetChrPos(0x102, -11070, 0, 11840, 0)
    SetChrPos(0x103, -9870, 0, 10640, 0)
    SetChrPos(0x104, -11070, 0, 10640, 0)
    SetChrPos(0x109, -11070, 0, 9440, 0)
    SetChrPos(0x105, -9870, 0, 9440, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F393")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jump("loc_F3A7")

    label("loc_F393")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_F3A7")

    OP_0D()

    ChrTalk(
        0x9,
        (
            "So you've come.\x01",
            "Come on, come eat my noodles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FE-Eehm, we're from the\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Ah, that matter, eh?\x01",
            "I've heard the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're in luck.\x01",
            "And that's because you'll be able to fully\x01",
            "appreciate my supreme noodles for free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Come on, eat.\x01",
            "These are the "Heavenly Noodles "Sun""!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FHm, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FThe deep red soup\x01",
            "looks very spicy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hu hu, eat it, without complaining.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You'll be tempted by the heavenly\x01",
            "taste that lies beyond that spiciness!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003F(His enthusiasm concerns me, but...)\x01",
            "I-In any event, let's try eating them.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-9560, 2500, 11630, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(15700, 0)
    SetChrPos(0x9, -9810, 0, 13520, 135)
    SetChrPos(0x104, -8390, 0, 12300, 0)
    SetChrPos(0x101, -8250, 0, 11290, 0)
    SetChrPos(0x102, -7150, 0, 12270, 315)
    SetChrPos(0x103, -6100, 0, 12250, 315)
    SetChrPos(0x105, -9920, 0, 11790, 45)
    SetChrPos(0x109, -6860, 0, 11350, 315)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate the Heavenly Noodles "Sun".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F*slurp slurp*...\x01",
            "Indeed, they aren't only spicy,\x01",
            "they have a deep taste too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FYes, they really are delicious...\x02\x03",
            "#00106FHowever, what concern us\x01",
            "would be the soup splashes.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FI-Indeed...\x01",
            "It'd be tough to remove the stains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mrrr...the women customers\x01",
            "always think like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you can eat first-rate noodles,\x01",
            "stuff like soup splashes are an\x01",
            "insignificant problem!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...Yeah, exactly.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F...Mr. Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThe world of rich flavors expanding\x01",
            "beyond this soup exquisite spiciness...\x02\x03",
            "Then, the springy, curly noodles\x01",
            "coiling around in that soup...\x02\x03",
            "This quality is something only\x01",
            "a man could understand.\x02\x03",
            "#00302FSomehow I feel like I too understand the\x01",
            "ol' man strong feelings toward the noodles.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD21")

    ChrTalk(
        0x9,
        (
            "Ooh...that's right, that's right!\x01",
            "Then there still was a promising youngster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Fine, I'll specially teach you the\x01",
            "base recipe of these noodles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Devote all your self to it!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Spicy Hot Flat Noodles"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_FE12")

    label("loc_FD21")


    ChrTalk(
        0x9,
        (
            "Ooh...that's right, that's right!\x01",
            "Then there still was a promising youngster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Alright, to you I'll give\x01",
            "another portion for free!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Appreciate it in full!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x190, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FE12")

    TurnDirection(0x104, 0x9, 500)

    ChrTalk(
        0x104,
        "#00309FOoh, thanks ol' man!\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009F(Randy...\x01",
            "It seems he liked them a lot.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Hu hu, it would seem good to leave\x01",
            "this presentation to him, eh?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 7)
    SetScenarioFlags(0x172, 2)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_FFA2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FFA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_FFBF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FFBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_FFD2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FFD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_FFE5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FFE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_10002")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_10015")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_10032")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_10045")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_10062")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_10075")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_10092")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10092")

    OP_29(0x80, 0x1, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101BA")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished to collect data from six food places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_101B1")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report\x01",
            "to Miss Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all six members'\x01",
            "favourites yet, so why don't we\x01",
            "try our best a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_101B1")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_101BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102A5")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found the entire SSS\x01",
            "members' favourites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00004FWith this, we found all\x01",
            "six members' favourites.\x02\x03",
            "#00000FWe have plenty of data now.\x01",
            "Let's go now to the News Service to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_102A5")

    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_10321")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -18000, 0, -5750, 90)
    BeginChrThread(0xD, 0, 0, 4)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, 13000, 0, -10000, 0)
    BeginChrThread(0xE, 0, 0, 5)
    Jump("loc_10363")

    label("loc_10321")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -13200, 0, 11500, 90)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -52470, 2000, 21150, 90)
    BeginChrThread(0xA, 0, 0, 2)

    label("loc_10363")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10470, 0, 11840, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_90_F2B4 end

    def Function_91_1038F(): pass

    label("Function_91_1038F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    LoadChrToIndex("chr/ch47500.itc", 0x28)
    LoadChrToIndex("chr/ch27800.itc", 0x29)
    SoundLoad(462)
    SoundLoad(461)
    SoundLoad(470)
    SoundLoad(457)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetMapObjFlags(0xA, 0x1000)
    ClearMapObjFlags(0xA, 0x4)
    OP_78(0xA, 0x32)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x32, -3570, 2000, 21710, 270)
    OP_D5(0x32, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(17650, 0, -4330, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26020, 0)
    SetChrChipByIndex(0x30, 0x28)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrChipByIndex(0x31, 0x29)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x30, 16050, 0, -6150, 270)
    SetChrPos(0x31, 19620, -10, 4000, 180)
    SetChrPos(0x101, 340, -470, 5300, 315)
    SetChrPos(0x104, 1700, -620, 4480, 315)
    SetChrPos(0x105, 150, -700, 3820, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_104C9():
        OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_104C9)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0x30, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x30, 0xB4, 0x1F4)
    Sleep(800)
    OP_93(0x30, 0x10E, 0x1F4)
    WaitChrThread(0x31, 1)
    TurnDirection(0x31, 0x30, 500)

    ChrTalk(
        0x31,
        "Clyde, sorry to have made you waiting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x30, 0x31, 500)
    Sleep(500)
    OP_68(20210, 0, -4730, 2000)
    OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x31,
        "I brought what we talked about.\x02",
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x30, 0x0, 0x1F4, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Clyde received an attache case\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0x30, 0xB4, 0x1F4, 0x5DC, 0x0)
    WaitChrThread(0x30, 1)

    ChrTalk(
        0x30,
        "Thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "So...what about that issue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "Well, it seems she's quite\x01",
            "interested in it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "It's going to be decided later\x01",
            "at "Neue-Blanc" for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "Ha ha, that's perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "...Oh, it's about time for\x01",
            "the water bus to leave.\x01",
            "I'll go finish the preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "Then, I leave the rest to you.\x01",
            "If you can get this contract done,\x01",
            "you being at the top is assured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "Yes, please leave it to me!!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x31, 1, 0, 92)
    OP_68(22840, 0, -4880, 3000)
    Sleep(1500)

    def lambda_10806():
        OP_9B(0x0, 0x30, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_10806)
    WaitChrThread(0x30, 1)

    def lambda_1081F():

        label("loc_1081F")

        TurnDirection(0xFE, 0x31, 500)
        Yield()
        Jump("loc_1081F")

    QueueWorkItem2(0x30, 1, lambda_1081F)
    Sleep(4000)
    EndChrThread(0x30, 0x1)

    ChrTalk(
        0x30,
        "Alright...let's do this!\x02",
    )

    CloseMessageWindow()
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x6)
    Sound(27, 0, 100, 0)

    def lambda_1086E():
        OP_9B(0x0, 0x30, 0x10E, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_1086E)
    Sleep(2000)
    Fade(500)
    OP_68(-2520, 0, 26110, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31670, 0)
    SetChrPos(0x30, 1100, 2000, 23760, 270)
    OP_63(0x30, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_108E2():
        OP_9B(0x0, 0x30, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_108E2)
    WaitChrThread(0x30, 1)

    def lambda_108FB():
        OP_93(0x30, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_108FB)
    WaitChrThread(0x30, 1)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    OP_64(0x30)

    def lambda_10924():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_10924)

    def lambda_10939():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_10939)
    WaitChrThread(0x30, 1)
    WaitChrThread(0x30, 2)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    ClearChrFlags(0x32, 0x80)
    OP_78(0xA, 0x32)
    OP_49()
    SetChrPos(0x32, -3570, 2000, 21710, 270)
    OP_D5(0x32, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_0D()
    Sound(470, 0, 100, 0)
    SetCameraDistance(30470, 3000)
    OP_0D()
    Sleep(800)
    Sleep(800)
    OP_68(-15880, 0, 26510, 3000)
    Sound(457, 0, 100, 0)

    def lambda_109EC():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_109EC)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    WaitChrThread(0x32, 1)
    OP_6F(0x11)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x32, 0x80)
    ClearChrFlags(0x32, 0x8000)
    ClearMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_0D()
    Sleep(500)
    OP_68(2060, 0, 7960, 5000)
    MoveCamera(39, 19, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(27560, 5000)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#00305FSomehow it seems he went\x01",
            "somewhere in high spirits.\x02\x03",
            "#00303FIt seems he has an appointment\x01",
            "with that Vice Chief's wife at\x01",
            ""Neue-Blanc", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, what do we do?\x01",
            "It would be useless to\x01",
            "tail him more than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Let's contact Elie and the others\x01",
            "and go back to police HQ for now.\x02\x03",
            "#00001FI feel I have somehow understood...\x01",
            "The real identity of that man called Clyde.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_91_1038F end

    def Function_92_10C28(): pass

    label("Function_92_10C28")

    ClearChrFlags(0x31, 0x4)
    OP_9B(0x0, 0x31, 0x10E, 0xFA0, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1770, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x10E, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x5A, 0x1B58, 0x7D0, 0x0)
    OP_9B(0x0, 0x31, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x4)
    Return()

    # Function_92_10C28 end

    def Function_93_10C7E(): pass

    label("Function_93_10C7E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(35980, -1400, 370, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17240, 0)
    SetChrPos(0x101, 35590, -2500, 10, 90)
    SetChrPos(0x102, 35400, -2500, 980, 90)
    SetChrPos(0x103, 34850, -2500, -1070, 90)
    SetChrPos(0x104, 34050, -2500, -40, 90)
    SetChrPos(0x109, 33500, -2500, 960, 90)
    SetChrPos(0x105, 33050, -2500, -730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x24, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF4")
    SetScenarioFlags(0x176, 2)

    ChrTalk(
        0x24,
        (
            "The Michelam bound water\x01",
            "bus will soon depaaart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Visitors who are going to use it,\x01",
            "please embark quiiick!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FNow that I think about it...\x01",
            "We did receive a request\x01",
            "from the theme park, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIts content was something like\x01",
            ""I want you to help Michey".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10103FUhhm, I wonder what kind of job is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F............\x01",
            "In any case, let's head there\x01",
            "as quick as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha, peTiote,\x01",
            "you're really motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, somehow I have\x01",
            "a nice presentiment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(After we cross to Michelam, we\x01",
            "should accept the request unless\x01",
            "there is a very good reason to not.)\x02\x03",
            "(Should we go now...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FF4")

    Call(0, 94)
    Return()

    # Function_93_10C7E end

    def Function_94_10FF8(): pass

    label("Function_94_10FF8")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Go to the Theme Park\x01",      # 0
            "Quit\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11062"),
        (1, "loc_112FC"),
        (SWITCH_DEFAULT, "loc_113D6"),
    )


    label("loc_11062")


    ChrTalk(
        0x101,
        (
            "#6P#00000FThen, let's head\x01",
            "there immediately.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    SoundLoad(479)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x5, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_70(0x5, 0x1F)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x2E, 126220, -3850, -50690, 315)
    OP_D5(0x2E, 0x0, 0x4CE78, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x1F, 0x5A, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(478, 0, 100, 0)
    OP_79(0x9)
    Sound(477, 0, 100, 0)
    Sleep(200)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_111F3():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_111F3)
    WaitChrThread(0x2E, 1)

    def lambda_11211():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_11211)
    Sleep(2000)
    StopSound(126, 1000, 50)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x2E, 1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x1DF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Thus, Lloyd and the others headed\x01",
            "to Michelam with the water bus...\x02\x03",
            "They made their way to the front of the\x01",
            "theme park where the client was waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_113D6")

    label("loc_112FC")


    ChrTalk(
        0x101,
        "#6P#00003F...We should come again.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please check the shedule\x01",
            "when going to Michelam\x01",
            "for quests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 33190, -2500, 0, 270)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x24, 0xFF)
    ModifyEventFlags(0, 6, 0x80)
    EventEnd(0x5)
    Jump("loc_113D6")

    label("loc_113D6")

    Return()

    # Function_94_10FF8 end

    def Function_95_113D7(): pass

    label("Function_95_113D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 38840, -2500, -460, 270)
    OP_69(0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_95_113D7 end

    def Function_96_11405(): pass

    label("Function_96_11405")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(479)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x5, 0x2E)
    OP_49()
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    SetChrPos(0x2E, 51800, -3850, -4000, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0x2E, 126220, -3850, -50690, 315)
    OP_D5(0x2E, 0x0, 0x4CE78, 0x0, 0x0)
    BeginChrThread(0x2F, 1, 0, 97)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x0, 0x1)
    OP_68(59280, 17600, -8870, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(51010, 0)
    OP_68(59280, 8000, -8870, 10000)

    def lambda_1153A():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1153A)
    Sound(475, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x1, 0x1)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_D5(0x2E, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x2E, 54800, -3850, -4000, 0)
    Sound(476, 0, 100, 0)
    Sound(477, 0, 100, 0)

    def lambda_115EB():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_115EB)
    WaitChrThread(0x2E, 1)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    Sound(478, 0, 100, 0)
    Sleep(2000)
    Fade(500)
    SetMapObjFlags(0x7, 0x4)
    OP_68(40510, 400, -3870, 0)
    MoveCamera(56, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11290, 0)
    OP_0D()
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x12D, 0x168, 0x0, 0x20)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0xF1, 0x12C, 0x0, 0x20)
    Sleep(500)
    SetChrPos(0x101, 49180, -2500, -1680, 270)
    SetChrPos(0x102, 49180, -2500, -1680, 270)
    SetChrPos(0x104, 49180, -2500, -1680, 270)
    SetChrPos(0x109, 49180, -2500, -1680, 270)
    SetChrPos(0x105, 49180, -2500, -1680, 270)
    SetChrPos(0x103, 49180, -2500, -1680, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 98)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 99)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 100)
    Sleep(700)
    OP_68(36510, 400, -1860, 5000)
    BeginChrThread(0x109, 3, 0, 101)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 102)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 103)
    WaitChrThread(0x103, 3)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        "#00200F............\x02",
    )

    CloseMessageWindow()

    def lambda_117BC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_117BC)
    Sleep(50)

    def lambda_117CC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117CC)
    Sleep(50)

    def lambda_117DC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_117DC)
    Sleep(50)

    def lambda_117EC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_117EC)
    Sleep(50)

    def lambda_117FC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_117FC)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305F...Hey, Lloyd.\x01",
            "Has something\x01",
            "happened to peTiote?\x02\x03",
            "She's been like that\x01",
            "from when we met\x01",
            "till in the water bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FRight...\x01",
            "She's looking somewhere\x01",
            "in the distance, spacing out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSomehow she has \x01",
            "a lonesome air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FU-Uhhm...\x01",
            "I don't know what to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FUhhm, Tio.\x01",
            "Are you not feeling well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F............No.\x01",
            "I'm fine.\x02\x03",
            "#00202FI was a little confused, but...\x01",
            "I have sorted out my feelings.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00208F...It is like this that\x01",
            "people become adults...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Theme Park Side Job]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x86, 0x1, 0x9)
    OP_29(0x86, 0x1, 0xA)
    OP_29(0x86, 0x4, 0x10)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x2E, 51800, -3850, -2300, 0)
    SetChrFlags(0x2E, 0x80)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 40740, -2500, -2330, 180)
    SetChrPos(0x17, 40630, -2500, -3760, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x0, 36990, -2500, 190, 270)
    OP_69(0xFF, 0x0)
    OP_24(0x1DF)
    EventEnd(0x5)
    Return()

    # Function_96_11405 end

    def Function_97_11B8E(): pass

    label("Function_97_11B8E")

    Sound(479, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Sleep(8000)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_24(0x1DF)
    Return()

    # Function_97_11B8E end

    def Function_98_11C20(): pass

    label("Function_98_11C20")


    def lambda_11C25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11C25)

    def lambda_11C36():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C36)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 37640, -2500, 320, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_98_11C20 end

    def Function_99_11C6B(): pass

    label("Function_99_11C6B")


    def lambda_11C70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11C70)

    def lambda_11C81():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11C81)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 37640, -2500, -1280, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_99_11C6B end

    def Function_100_11CB6(): pass

    label("Function_100_11CB6")


    def lambda_11CBB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11CBB)

    def lambda_11CCC():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11CCC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 38890, -2500, 1500, 2000, 0x0)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_100_11CB6 end

    def Function_101_11D01(): pass

    label("Function_101_11D01")


    def lambda_11D06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11D06)

    def lambda_11D17():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11D17)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 39690, -2500, -1720, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_101_11D01 end

    def Function_102_11D4C(): pass

    label("Function_102_11D4C")


    def lambda_11D51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11D51)

    def lambda_11D62():
        OP_95(0xFE, 41760, -2500, -1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11D62)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 40640, -2500, 1110, 2000, 0x0)
    OP_93(0x105, 0xE1, 0x1F4)
    Return()

    # Function_102_11D4C end

    def Function_103_11D97(): pass

    label("Function_103_11D97")


    def lambda_11D9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11D9C)

    def lambda_11DAD():
        OP_95(0xFE, 41760, -2500, -1910, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11DAD)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 41340, -2500, -150, 1500, 0x0)
    OP_93(0x103, 0x10E, 0x1F4)
    Return()

    # Function_103_11D97 end

    def Function_104_11DE2(): pass

    label("Function_104_11DE2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EAE")

    ChrTalk(
        0x1A2,
        "Is East Street this way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, no...\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Thought so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...I think I told you to\x01",
            "go via East Street...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FYou're right...sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_11F23")

    label("loc_11EAE")


    ChrTalk(
        0x1A2,
        (
            "Hey, making stops along the way is fine,\x01",
            "but spare me the detours, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Take me to East Street at once.\x02",
    )

    CloseMessageWindow()

    label("loc_11F23")

    SetChrPos(0x0, -28110, 2000, 23520, 90)
    EventEnd(0x4)
    Return()

    # Function_104_11DE2 end

    def Function_105_11F37(): pass

    label("Function_105_11F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FF0")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(After we cross to Michelam, we\x01",
            "should accept the request unless\x01",
            "there is a very good reason to not.)\x02\x03",
            "(Should we go now...?)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 94)
    Jump("loc_12097")

    label("loc_11FF0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Michelam" Bound Water Bus - Schedule\x01\x01",
            "※The "Wonderland" theme park,\x01",
            "   pride of Michelam, is open!\x01",
            "   Please enjoy some fun moments!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)

    label("loc_12097")

    Return()

    # Function_105_11F37 end

    def Function_106_12098(): pass

    label("Function_106_12098")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　"Lupinus River - First Lighthouse"\x01\x01",
            "Authorized Personnel Only.\x01",
            "　　　　　～Crossbell City～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_106_12098 end

    SaveToFile()

Try(main)
