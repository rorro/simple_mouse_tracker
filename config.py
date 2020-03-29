from pathlib import Path

class Config():
    def __init__(self):
        self.SCRIPT_FOLDER_PATH = str(Path(__file__).parent)
        self.HOME_FOLDER = str(Path.home())
        self.CONFIG_FILE = self.HOME_FOLDER + "/" + ".simplemousetracker"

        self.DEFAULT_CONFIG = [
                "# The keybinding for starting/stopping the mouse tracking.",
                "# Valid modifiers: control, shift, super (windows key), alt.",
                "# Read more about valid bindings at https://github.com/timeyyy/system_hotkey",
                "start_tracking=control-s",
                "",
                "# The keybinding for pausing/resuming the mouse tracking.",
                "pause_tracking=control-p",
                "",
                "# Where to save the tracked files. Leave blank to save in same",
                "# folder as the script. The path should be absolute.",
                "# If folder doesn't exist, nothing will be saved.",
                "save_folder=",
                "",
                "# Colored lines when exporting/showing tracked data.",
                "# Only true is true, everything else is false.",
                "colored_speed=true",
                "",
                "# Default color for drawing tracked data.",
                "# Only applies when colored_speed is set to false.",
                "default_color=#000000",
                "",
                "",
                ]

        # Default config values.
        # They are here to make sure the program works if the config
        # file is not configured correctly.
        self.start_tracking_binding = ("control", "s")
        self.pause_tracking_binding = ("control", "p")
        self.save_folder = self.SCRIPT_FOLDER_PATH
        self.colored_speed = True
        self.default_color = "#000000"

        if not Path(self.CONFIG_FILE).is_file():
            print("Config file doesn't exist. Creating default.")
            config = open(self.CONFIG_FILE, "w")
            config.write("\n".join(self.DEFAULT_CONFIG))
            config.close()
        else:
            config = open(self.CONFIG_FILE, "r")

            for line in config:
                line = line.rstrip()
                if not line or line.startswith("#"):
                    continue

                split = line.split("=")
                lhs = split[0]
                rhs = split[1]

                if lhs == "start_tracking":
                    keys = rhs.split("-")
                    if len(keys) == 1:
                        self.start_tracking_binding = rhs
                    else:
                        self.start_tracking_binding = tuple(keys)
                elif lhs == "pause_tracking":
                    keys = rhs.split("-")
                    if len(keys) == 1:
                        self.pause_tracking_binding = rhs
                    else:
                        self.pause_tracking_binding = tuple(keys)
                elif lhs == "save_folder":
                    self.save_folder = rhs
                elif lhs == "colored_speed":
                    if rhs != "true":
                        self.colored_speed = False
                elif lhs == "default_color":
                    self.default_color = rhs

            config.close()

