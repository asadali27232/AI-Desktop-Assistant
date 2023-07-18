import os


class SystemQueries:
    def execute_system_command(self, command):
        os.system(command)

    def execute_command(self, query):
        if "calculator" in query:
            self.execute_system_command("calc.exe")
        elif "notepad" in query:
            self.execute_system_command("notepad.exe")
        elif "file explorer" in query:
            self.execute_system_command("explorer")
        elif "task manager" in query:
            self.execute_system_command("taskmgr")
        elif "paint" in query:
            self.execute_system_command("mspaint")
        elif "command prompt" in query:
            self.execute_system_command("cmd.exe")
        elif "control panel" in query:
            self.execute_system_command("control")
        else:
            pass
