import time  # Time imported to make the code interface easier to use
import pywebio
from pywebio.input import input
from pywebio.output import put_text

def main():
    # List of all the possible camera settings
    isoList = [6400, 3200, 1600, 800, 400, 200, 100, 50]
    aptreList = [2, 2.8, 4, 5.6, 8, 11, 16, 22]
    ssList = [30, 60, 125, 250, 500, 1000, 2000, 4000]
    # Dictionaires of all the default camera settings for each lighting condition
    defIsos = {
        "Snow/Sand": 100,
        "Sunny": 200,
        "Lightly cloudy": 400,
        "Cloudy": 800,
        "Overcast": 1600,
        "Sunset/Shade": 3200,
        "Dusk": 3200,
    }
    defSss = {
        "Snow/Sand": 125,
        "Sunny": 250,
        "Lightly cloudy": 500,
        "Cloudy": 1000,
        "Overcast": 2000,
        "Sunset/Shade": 4000,
        "Dusk": 4000,
    } 
    defAptres = {
        "Snow/Sand": 22,
        "Sunny": 16,
        "Lightly cloudy": 11,
        "Cloudy": 8,
        "Overcast": 5.6,
        "Sunset/Shade": 4,
        "Dusk": 2.8,
    }
    # Functions that ask for the ISO, Shutterspeed & Aperture, which also handles errors
    def askIso():
        while True:
            try:
                iso = float(input("\nWhat is your preference for the ISO? "))
                if iso in isoList:
                    break
                put_text(
                    "Invalid ISO entered. Please try again with a number on the table."
                )
                time.sleep(1.5)
            except Exception as error:
                put_text(error, "Please try again with a number on the table.")
                time.sleep(1.5)
        return iso

    def askAptre():
        while True:
            try:
                aptre = float(input("\nWhat is your preference for the Aperture? f/"))
                if aptre in aptreList:
                    break
                put_text(
                    "Invalid Aperture entered. Please try again with a number on the table."
                )
                time.sleep(1.5)
            except Exception as error:
                put_text(error, "Please try again with a number on the table.")
                time.sleep(1.5)
        return aptre

    def askSs():
        while True:
            try:
                ss = float(input("\nWhat is your preference for the Shutter Speed? 1/"))
                if ss in ssList:
                    break
                put_text(
                    "Invalid Shutter Speed entered. Please try again with a number on the table."
                )
                time.sleep(1.5)
            except Exception as error:
                put_text(error, "Please try again with a number on the table.")
                time.sleep(1.5)
        return ss

    # Functions that warn the user if the selected settings or too bright or dark
    def tooDark():
        put_text(
            "\nToo dark! Please increase your settings by",
            ((-totalStops) - (indexDef - indexLowest)),
            "stop(s).\nProgram will restart.",
        )

    def tooBright():
        put_text(
            "\nToo bright! Please decrease your settings by",
            totalStops - (indexBrightest - indexDef),
            "stop(s).\nProgram will restart.",
        )

    # Functions that index out the default ISO, Shutterspeed & Aperture for manual mode
    def defIso():
        for key, value in defIsos.items():
            if key == lighting:
                defIso = defIsos[lighting]
        return defIso

    def defAptre():
        for key, value in defAptres.items():
            if key == lighting:
                defAptre = defAptres[lighting]
        return defAptre

    def defSs():
        for key, value in defSss.items():
            if key == lighting:
                defSs = defSss[lighting]
        return defSs

    # Indexing and calculations for the autmatic modes
    def autoCalculate():
        for key, value in Isos.items():
            if key == lighting:
                iso = Isos[lighting]
        for key, value in Sss.items():
            if key == lighting:
                ss = Sss[lighting]
        for key, value in Aptres.items():
            if key == lighting:
                aptre = Aptres[lighting]
        put_text("\nYour lighting conditon is:\n" + lighting)
        time.sleep(0.25)
        put_text("\nYour recommended settings are:")
        time.sleep(0.25)
        put_text("\nISO " + str(iso))
        time.sleep(0.25)
        put_text("\nShutter Speed 1/" + str(ss) + "s")
        time.sleep(0.25)
        put_text("\nAperture f/" + str(aptre))

    # Ask for the preferred camera mode
    modes = {
        1: "Manual",
        2: "Portrait",
        3: "Landscape",
        4: "Sports Action",
        5: "Aperture Priority",
        6: "Shutter Priority",
    }
    # Help user to understand the defferent modes
    modesInfo = {
        "Manual": "Adjust Aperture, Shutter Speed and ISO manually.",
        "Potrait": "Emphasises subject by blurring away the background.",
        "Landscape": "Shoots the entire range of scenery in sharp focus with vivid colours",
        "Sports Action": "Shoots fast motion at higher Shutter speeds. TIP: Use in bright places.",
        "Aperture Priority": "Adjusts Aperture to change range that is in focus and background blur.",
        "Shutter Priority": "Adjusts Shutter Speed to change the expression of a moving object.",
    }
    for key in modes:
        put_text("\n", key, " : ", modes[key])
    while True:
        try:
            mode = int(input("\nWhat mode will you be using?\nType '0' for help. "))
            if mode in range(0, 7):
                break
            put_text(
                "Invalid number entered. Please try again with a number from 1 - 6. Or type '0' for help."
            )
            time.sleep(1.5)
        except Exception as error:
            put_text(
                error,
                "Please try again with a number from 1 - 6. Or type '0' for help.",
            )
            time.sleep(1.5)
    pywebio.output.clear()
    # Help mode, which helps user to decide on a camera mode
    if mode == 0:
        put_text("\nYou can choose from the following modes:\n")
        for key in modesInfo:
            put_text("\n" + key, " : ", modesInfo[key])
            time.sleep(0.5)
        time.sleep(1.5)
        main()
    else:
        # Ask for the preffered lighting
        lightings = {
            7: "Snow/Sand",
            6: "Sunny",
            5: "Lightly cloudy",
            4: "Cloudy",
            3: "Overcast",
            2: "Sunset/Shade",
            1: "Dusk",
        }
        for key in lightings:
            put_text("\n", key, " : ", lightings[key])
        while True:
            try:
                lighting = int(input("\nWhat is your lighting condition? "))
                if lighting in range(1, 8):
                    break
                put_text(
                    "Invalid number entered. Please try again with a number from 1 - 7."
                )
                time.sleep(1.5)
            except Exception as error:
                put_text(error, "Please try again with a number from 1 - 7.")
                time.sleep(1.5)
        for key, value in lightings.items():
            if key == lighting:
                lighting = value
        if mode == 1 or mode == 5 or mode == 6:
            put_text(
                "\n+--------+---------------+-------------+\n|     ISO    |   Shutterspeed   |   Aperture    |\n+--------+---------------+-------------+\n|     6400     |         1/30s         |       f/2.0       |\n|     3200     |         1/60s         |       f/2.8       |\n|     1600     |         1/125s        |       f/4.0       |\n|     800      |         1/250s        |       f/5.6       |\n|     400      |         1/500s        |       f/8.0       |\n|     200      |        1/1000s        |        f/11       |\n|     100      |        1/2000s        |        f/16       |\n|      50      |        1/4000s        |        f/22       |\n+--------+---------------+-------------+\nAbove is a table of all the available settings. This will assist in choosing the correct ISO, Shutter Speed and Aperture."
            )
        time.sleep(1.5)
        # Manual mode
        if mode == 1:
            settings = {1: "ISO", 2: "Shutter Speed", 3: "Aperture"}
            for key in settings:
                put_text("\n", key, " : ", settings[key])
            while True:
                try:
                    setting = int(input("\nWhich setting do you want recommended? "))
                    if setting in range(1, 4):
                        break
                    put_text(
                        "Invalid number entered. Please try again with a number from 1 - 3."
                    )
                    time.sleep(1.5)
                except Exception as error:
                    put_text(error, "Please try again with a number from 1 - 3.")
                    time.sleep(1.5)
            for key, value in settings.items():
                if key == setting:
                    setting = value
            # ISO
            if setting == "ISO":
                aptre = askAptre()
                ss = askSs()
                defAptre = defAptre()
                defSs = defSs()
                defIso = defIso()
                aptreStops = aptreList.index(defAptre) - aptreList.index(aptre)
                ssStops = ssList.index(defSs) - ssList.index(ss)
                indexBrightest = isoList.index(50)
                indexLowest = isoList.index(6400)
                indexDef = isoList.index(defIso)
                totalStops = aptreStops + ssStops
                isoStops = indexDef + totalStops
                if totalStops >= 0:
                    if totalStops > (indexBrightest - indexDef):
                        tooBright()
                        time.sleep(1)
                        main()
                    elif totalStops <= (indexBrightest - indexDef):
                        put_text("\nYour lighting conditon is:\n" + lighting)
                        time.sleep(0.25)
                        put_text("\nYour selected settings are:")
                        time.sleep(0.25)
                        put_text("\nAperture f/" + str(aptre))
                        time.sleep(0.25)
                        put_text("\nShutter Speed 1/" + str(ss) + "s")
                        time.sleep(0.25)
                        put_text("\n\nYour recommended setting is:")
                        time.sleep(0.25)
                        put_text("\nISO " + str(isoList[isoStops]))
                if totalStops < 0:
                    if -(totalStops) > (indexDef - indexLowest):
                        tooDark()
                        time.sleep(1)
                        main()
                    else:
                        put_text("\nYour lighting conditon is:\n" + lighting)
                        time.sleep(0.25)
                        put_text("\nYour selected settings are:")
                        time.sleep(0.25)
                        put_text("\nAperture f/" + str(aptre))
                        time.sleep(0.25)
                        put_text("\nShutter Speed 1/" + str(ss) + "s")
                        time.sleep(0.25)
                        put_text("\n\nYour recommended setting is:")
                        time.sleep(0.25)
                        put_text("\nISO " + str(isoList[isoStops]))
            # Shutter Speed
            if setting == "Shutter Speed":
                iso = askIso()
                aptre = askAptre()
                defIso = defIso()
                defAptre = defAptre()
                defSs = defSs()
                isoStops = isoList.index(defIso) - isoList.index(iso)
                aptreStops = aptreList.index(defAptre) - aptreList.index(aptre)
                indexBrightest = ssList.index(4000)
                indexLowest = ssList.index(30)
                indexDef = ssList.index(defSs)
                totalStops = isoStops + aptreStops
                ssStops = indexDef + totalStops
                if totalStops >= 0:
                    if totalStops > (indexBrightest - indexDef):
                        tooBright()
                        time.sleep(1)
                        main()
                    elif totalStops <= (indexBrightest - indexDef):
                        put_text("\nYour lighting conditon is:\n" + lighting)
                        time.sleep(0.25)
                        put_text("\nYour selected settings are:")
                        time.sleep(0.25)
                        put_text("\nISO " + str(iso))
                        time.sleep(0.25)
                        put_text("\nAperture f/" + str(aptre))
                        time.sleep(0.25)
                        put_text("\n\nYour recommended setting is:")
                        time.sleep(0.25)
                        put_text("\nShutter Speed 1/" + str(ssList[ssStops]) + "s")
                if totalStops < 0:
                    if -(totalStops) > (indexDef - indexLowest):
                        tooDark()
                        time.sleep(1)
                        main()
                    else:
                        put_text("\nYour lighting conditon is:\n" + lighting)
                        time.sleep(0.25)
                        put_text("\nYour selected settings are:")
                        time.sleep(0.25)
                        put_text("\nISO " + str(iso))
                        time.sleep(0.25)
                        put_text("\nAperture f/" + str(aptre))
                        time.sleep(0.25)
                        put_text("\n\nYour recommended setting is:")
                        time.sleep(0.25)
                        put_text("\nShutter Speed 1/" + str(ssList[ssStops]) + "s")
            # Aperture
            if setting == "Aperture":
                iso = askIso()
                ss = askSs()
                defIso = defIso()
                defSs = defSs()
                defAptre = defAptre()
                isoStops = isoList.index(defIso) - isoList.index(iso)
                ssStops = ssList.index(defSs) - ssList.index(ss)
                indexBrightest = aptreList.index(22)
                indexLowest = aptreList.index(2)
                indexDef = aptreList.index(defAptre)
                totalStops = isoStops + ssStops
                aptreStops = indexDef + totalStops
                if totalStops >= 0:
                    if totalStops > (indexBrightest - indexDef):
                        tooBright()
                        time.sleep(1)
                        main()
                    elif totalStops <= (indexBrightest - indexDef):
                        put_text("\nYour lighting conditon is:\n" + lighting)
                        time.sleep(0.25)
                        put_text("\nYour selected settings are:")
                        time.sleep(0.25)
                        put_text("\nISO " + str(iso))
                        time.sleep(0.25)
                        put_text("\nShutter Speed 1/" + str(ss) + "s")
                        time.sleep(0.25)
                        put_text("\n\nYour recommended setting is:")
                        time.sleep(0.25)
                        put_text("\nAperture f/" + str(aptreList[aptreStops]))
                if totalStops < 0:
                    if -(totalStops) > (indexDef - indexLowest):
                        tooDark()
                        time.sleep(1)
                        main()
                    else:
                        put_text("\nYour lighting conditon is:\n" + lighting)
                        time.sleep(0.25)
                        put_text("\nYour selected settings are:")
                        time.sleep(0.25)
                        put_text("\nISO " + str(iso))
                        time.sleep(0.25)
                        put_text("\nShutter Speed 1/" + str(ss) + "s")
                        time.sleep(0.25)
                        put_text("\n\nYour recommended setting is:")
                        time.sleep(0.25)
                        put_text("\nAperture f/" + str(aptreList[aptreStops]))
        # Potrait mode
        if mode == 2:
            Isos = {
                "Snow/Sand": 100,
                "Sunny": 100,
                "Lightly cloudy": 100,
                "Cloudy": 100,
                "Overcast": 400,
                "Sunset/Shade": 800,
                "Dusk": 1600,
            }
            Sss = {
                "Snow/Sand": 2000,
                "Sunny": 2000,
                "Lightly cloudy": 800,
                "Cloudy": 800,
                "Overcast": 2000,
                "Sunset/Shade": 4000,
                "Dusk": 4000,
            }
            Aptres = {
                "Snow/Sand": 2.8,
                "Sunny": 2,
                "Lightly cloudy": 2,
                "Cloudy": 2,
                "Overcast": 2,
                "Sunset/Shade": 2,
                "Dusk": 2,
            }
            autoCalculate()
        # Landscape mode
        if mode == 3:
            Isos = {
                "Snow/Sand": 100,
                "Sunny": 100,
                "Lightly cloudy": 400,
                "Cloudy": 100,
                "Overcast": 100,
                "Sunset/Shade": 200,
                "Dusk": 100,
            }
            Sss = {
                "Snow/Sand": 125,
                "Sunny": 250,
                "Lightly cloudy": 500,
                "Cloudy": 1000,
                "Overcast": 2000,
                "Sunset/Shade": 4000,
                "Dusk": 4000,
            }
            Aptres = {
                "Snow/Sand": 22,
                "Sunny": 22,
                "Lightly cloudy": 22,
                "Cloudy": 22,
                "Overcast": 22,
                "Sunset/Shade": 16,
                "Dusk": 16,
            }
            autoCalculate()
        # Sports Action mode
        if mode == 4:
            Isos = {
                "Snow/Sand": 100,
                "Sunny": 200,
                "Lightly cloudy": 400,
                "Cloudy": 800,
                "Overcast": 1600,
                "Sunset/Shade": 3200,
                "Dusk": 3200,
            }
            Sss = {
                "Snow/Sand": 2000,
                "Sunny": 2000,
                "Lightly cloudy": 2000,
                "Cloudy": 2000,
                "Overcast": 4000,
                "Sunset/Shade": 4000,
                "Dusk": 4000,
            }
            Aptres = {
                "Snow/Sand": 5.6,
                "Sunny": 5.6,
                "Lightly cloudy": 22,
                "Cloudy": 5.6,
                "Overcast": 4,
                "Sunset/Shade": 4,
                "Dusk": 2.8,
            }
            autoCalculate()
        # Aperture Priority
        if mode == 5:
            aptre = askAptre()
            iso = defIso()
            defSs = defSs()
            defAptre = defAptre()
            totalStops = aptreList.index(defAptre) - aptreList.index(aptre)
            indexBrightest = aptreList.index(22)
            indexLowest = aptreList.index(2)
            indexDef = ssList.index(defSs)
            ssStops = indexDef + totalStops
            if totalStops >= 0:
                if totalStops > (indexBrightest - indexDef):
                    tooBright()
                    time.sleep(1)
                    main()
                elif totalStops <= (indexBrightest - indexDef):
                    put_text("\nYour lighting conditon is:\n" + lighting)
                    time.sleep(0.25)
                    put_text("\nYour selected setting is:")
                    time.sleep(0.25)
                    put_text("\nAperture f/" + str(aptre))
                    time.sleep(0.25)
                    put_text("\n\nYour recommended settings are:")
                    time.sleep(0.25)
                    put_text("\nISO " + str(iso))
                    time.sleep(0.25)
                    put_text("\nShutter Speed 1/" + str(ssList[ssStops]) + "s")

            if totalStops < 0:
                if -(totalStops) > (indexDef - indexLowest):
                    tooDark()
                    time.sleep(1)
                    main()
                else:
                    put_text("\nYour lighting conditon is:\n" + lighting)
                    time.sleep(0.25)
                    put_text("\nYour selected setting is:")
                    time.sleep(0.25)
                    put_text("\nAperture f/" + str(aptre))
                    time.sleep(0.25)
                    put_text("\n\nYour recommended settings are:")
                    time.sleep(0.25)
                    put_text("\nISO " + str(iso))
                    time.sleep(0.25)
                    put_text("\nShutter Speed 1/" + str(ssList[ssStops]) + "s")
        # Shutter Priority
        if mode == 6:
            ss = askSs()
            iso = defIso()
            defAptre = defAptre()
            defSs = defSs()
            totalStops = ssList.index(defSs) - ssList.index(ss)
            indexBrightest = ssList.index(30)
            indexLowest = ssList.index(4000)
            indexDef = aptreList.index(defAptre)
            aptreStops = indexDef + totalStops
            if totalStops >= 0:
                if totalStops > (indexBrightest - indexDef):
                    tooBright()
                    time.sleep(1)
                    main()
                elif totalStops <= (indexBrightest - indexDef):
                    put_text("\nYour lighting conditon is:\n" + lighting)
                    time.sleep(0.25)
                    put_text("\nYour selected setting is:")
                    time.sleep(0.25)
                    put_text("\nShutter Speed 1/" + str(ss) + "s")
                    time.sleep(0.25)
                    put_text("\n\nYour recommended settings are:")
                    time.sleep(0.25)
                    put_text("\nISO " + str(iso))
                    time.sleep(0.25)
                    put_text("\nAperture f/" + str(aptreList[aptreStops]))
            if totalStops < 0:
                if -(totalStops) > (indexDef - indexLowest):
                    tooDark()
                    time.sleep(1)
                    main()
                else:
                    put_text("\nYour lighting conditon is:\n" + lighting)
                    time.sleep(0.25)
                    put_text("\nYour selected setting is:")
                    time.sleep(0.25)
                    put_text("\nShutter Speed 1/" + str(ss) + "s")
                    time.sleep(0.25)
                    put_text("\n\nYour recommended settings are:")
                    time.sleep(0.25)
                    put_text("\nISO " + str(iso))
                    time.sleep(0.25)
                    put_text("\nAperture f/" + str(aptreList[aptreStops]))
    # Restart
    time.sleep(1.5)  # Slows down time using "import time"
    restart = input("\n\nDo you wish to rerun the program? ")
    if restart.lower() in ("yes", "y", "yeah", "yea", "ye"):
        pywebio.output.clear()
        main()  # Calls function to rerun code
    else:
        time.sleep(0.5)
        put_text("\nThank you\n")
        exit()  # Exit


main()  # Calls function to run code

