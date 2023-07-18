import os


class SystemQueries:
    def execute_system_command(self, command):
        os.system(command)

    def execute_command(self, query):
        if "calculator" in query:
            self.execute_system_command("calc.exe")
            return "opening calculator"
        elif "notepad" in query:
            self.execute_system_command("notepad.exe")
            return "opening notepad"
        elif "file explorer" in query:
            self.execute_system_command("explorer")
            return "opening file explorer"
        elif "task manager" in query:
            self.execute_system_command("taskmgr")
            return "opening task manager"
        elif "paint" in query:
            self.execute_system_command("mspaint")
            return "opening paint"
        elif "command prompt" in query:
            self.execute_system_command("cmd.exe")
            return "opening command prompt"
        elif "control panel" in query:
            self.execute_system_command("control")
            return "opening control panel"
        else:
            return False
